import React, { useMemo } from 'react';
import katex from 'katex';

interface MathTextProps {
  content?: string;
  text?: string;
  className?: string;
  block?: boolean;
}

/** Parses markdown table text into headers and rows */
export function parseMarkdownTable(text: string): { headers: string[]; rows: string[][] } | null {
  if (!text || !text.includes('|')) return null;
  const lines = text.trim().split(/\r?\n/).map(l => l.trim()).filter(Boolean);
  if (lines.length < 2) return null;

  // Delimiter line matches |---| or |:---|---:| or similar
  const delimiterIndex = lines.findIndex(l => /^\|?(\s*:?-+:?\s*\|)+\s*:?-+:?\s*\|?$/.test(l));
  if (delimiterIndex < 1) return null;

  const headerLine = lines[delimiterIndex - 1];
  const headers = headerLine
    .split('|')
    .map(c => c.trim())
    .filter((c, i, arr) => !(i === 0 && c === '') && !(i === arr.length - 1 && c === ''));

  const rows: string[][] = [];
  for (let i = delimiterIndex + 1; i < lines.length; i++) {
    const line = lines[i];
    if (!line.includes('|')) continue;
    const cells = line
      .split('|')
      .map(c => c.trim())
      .filter((c, idx, arr) => !(idx === 0 && c === '') && !(idx === arr.length - 1 && c === ''));
    if (cells.length > 0) {
      rows.push(cells);
    }
  }

  if (headers.length > 0 && rows.length > 0) {
    return { headers, rows };
  }
  return null;
}

const katexCache = new Map<string, string>();

function renderKatexSafe(math: string, displayMode: boolean): string {
  const cacheKey = `${displayMode ? 'D:' : 'I:'}${math}`;
  const cached = katexCache.get(cacheKey);
  if (cached) return cached;

  try {
    const rendered = katex.renderToString(math, {
      displayMode,
      throwOnError: false,
      strict: 'ignore',
    });
    // Keep cache bounded to 2000 items
    if (katexCache.size > 2000) {
      const firstKey = katexCache.keys().next().value;
      if (firstKey) katexCache.delete(firstKey);
    }
    katexCache.set(cacheKey, rendered);
    return rendered;
  } catch {
    const fallback = displayMode 
      ? `<span class="text-rose-500 font-mono">$$${math}$$</span>`
      : `<span class="text-rose-500 font-mono">$${math}$</span>`;
    return fallback;
  }
}

const MathTextComponent: React.FC<MathTextProps> = ({ content, text: propText, className = '', block = false }) => {
  const renderedHtml = useMemo(() => {
    const rawContent = content ?? propText ?? '';
    if (!rawContent) return '';

    let text = rawContent;

    // Normalize standard LaTeX wrappers \[ \] and \( \)
    text = text.replace(/\\\[([\s\S]*?)\\\]/g, '$$$$$1$$$$');
    text = text.replace(/\\\(([\s\S]*?)\\\)/g, '$$$1$$');

    // Auto-fix literal missing backslashes for common math symbols
    text = text.replace(/(?<!\\)\btimes\b/g, '\\times');
    text = text.replace(/(?<!\\)\bimplies\b/g, '\\implies');
    text = text.replace(/(?<!\\)\bapprox\b/g, '\\approx');
    text = text.replace(/\\textm\b|(?<!\\)\btextm\b/g, '\\text{m}');

    // Protect Unicode inside subscripts/superscripts
    text = text.replace(/_\{([^\x00-\x7F]+)\}/g, '_{\\text{$1}}');
    text = text.replace(/\^\{([^\x00-\x7F]+)\}/g, '^{\\text{$1}}');

    // Auto-wrap if entire string contains bare LaTeX command
    if (!text.includes('$') && /\\[a-zA-Z]+/.test(text)) {
      if (!/[\u0980-\u09FF]/.test(text)) {
        text = `$${text.trim()}$`;
      }
    }

    // Step 1: Replace $$...$$ with block math placeholders
    const displayMathBlocks: string[] = [];
    text = text.replace(/\$\$(.*?)\$\$/gs, (_, math) => {
      let cleanMath = math.trim();
      cleanMath = cleanMath.replace(/(?<!\\)\b(times|implies|frac|Delta|approx|pm|sqrt|alpha|beta|rho|sigma|lambda|theta|omega|pi|to|le|ge|neq|sim|propto)\b/g, '\\$1');
      const rendered = renderKatexSafe(cleanMath, true);
      displayMathBlocks.push(`<div class="overflow-x-auto no-scrollbar py-1 my-1">${rendered}</div>`);
      return `___DISPLAY_MATH_${displayMathBlocks.length - 1}___`;
    });

    // Step 2: Replace $...$ with inline math placeholders
    const inlineMathBlocks: string[] = [];
    text = text.replace(/\$(.*?)\$/g, (_, math) => {
      let cleanMath = math.trim();
      cleanMath = cleanMath.replace(/(?<!\\)\b(times|implies|frac|Delta|approx|pm|sqrt|alpha|beta|rho|sigma|lambda|theta|omega|pi|to|le|ge|neq|sim|propto)\b/g, '\\$1');
      const rendered = renderKatexSafe(cleanMath, false);
      inlineMathBlocks.push(`<span class="inline-block max-w-full overflow-x-auto no-scrollbar align-middle">${rendered}</span>`);
      return `___INLINE_MATH_${inlineMathBlocks.length - 1}___`;
    });

    // Step 2b: Fallback for any bare LaTeX commands outside $ (e.g. \sqrt, \frac, \log, \pm)
    if (/\\[a-zA-Z]+/.test(text)) {
      text = text.replace(/([^\s\u0980-\u09FF]*\\[a-zA-Z]+(?:\{[^{}]*\}|\[[^[\]]*\]|[^\s\u0980-\u09FF])*)/g, (match) => {
        const trimmed = match.trim();
        if (!trimmed || !trimmed.includes('\\')) return match;
        const rendered = renderKatexSafe(trimmed, false);
        inlineMathBlocks.push(`<span class="inline-block max-w-full overflow-x-auto no-scrollbar align-middle">${rendered}</span>`);
        return `___INLINE_MATH_${inlineMathBlocks.length - 1}___`;
      });
    }

    // Step 2c: Handle markdown table blocks
    const tableBlocks: string[] = [];
    if (text.includes('|')) {
      const lines = text.split(/\r?\n/);
      let tableBuffer: string[] = [];
      let inTable = false;
      const newLines: string[] = [];

      const flushTable = () => {
        if (tableBuffer.length >= 2) {
          const tableStr = tableBuffer.join('\n');
          const parsed = parseMarkdownTable(tableStr);
          if (parsed) {
            const tableHtml = `
<div class="w-full overflow-x-auto my-3 rounded-xl border border-slate-200 dark:border-slate-800 shadow-xs" style="-webkit-overflow-scrolling: touch;">
  <table class="w-full text-left border-collapse min-w-[280px]">
    <thead>
      <tr class="bg-slate-100 dark:bg-slate-800 text-xs font-semibold text-slate-700 dark:text-slate-200 border-b border-slate-200 dark:border-slate-700">
        ${parsed.headers.map(h => `<th class="py-2.5 px-3 text-xs font-semibold text-slate-700 dark:text-slate-200 border-b border-slate-200 dark:border-slate-700">${h}</th>`).join('')}
      </tr>
    </thead>
    <tbody>
      ${parsed.rows.map(row => `
        <tr class="even:bg-slate-50/50 dark:even:bg-slate-800/30 border-b border-slate-100 dark:border-slate-800/60 transition-colors">
          ${row.map(cell => `<td class="py-2 px-3 text-xs text-slate-800 dark:text-slate-100 border-b border-slate-100 dark:border-slate-800/60 leading-relaxed font-normal">${cell}</td>`).join('')}
        </tr>
      `).join('')}
    </tbody>
  </table>
</div>`;
            tableBlocks.push(tableHtml);
            newLines.push(`___TABLE_BLOCK_${tableBlocks.length - 1}___`);
          } else {
            newLines.push(...tableBuffer);
          }
        } else if (tableBuffer.length > 0) {
          newLines.push(...tableBuffer);
        }
        tableBuffer = [];
        inTable = false;
      };

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const trimmed = line.trim();
        const isTableLine = trimmed.startsWith('|') || (trimmed.endsWith('|') && trimmed.includes('|'));

        if (isTableLine) {
          tableBuffer.push(line);
          inTable = true;
        } else {
          if (inTable) {
            flushTable();
          }
          newLines.push(line);
        }
      }
      if (inTable) {
        flushTable();
      }

      text = newLines.join('\n');
    }

    // Step 3: Handle markdown formatting
    // Bold **text**
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong class="font-bold text-slate-900 dark:text-slate-100">$1</strong>');
    
    // Inline code `code`
    text = text.replace(/`([^`]+)`/g, '<code class="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-amber-700 dark:text-amber-300 font-mono text-sm border border-slate-300 dark:border-slate-700/60">$1</code>');

    // Bullet points (leading • or -)
    text = text.replace(/^•\s*(.*?)$/gm, '<div class="flex items-start gap-2 my-1"><span class="text-brand-600 dark:text-brand-400 font-bold">•</span><span>$1</span></div>');
    text = text.replace(/^-\s*(.*?)$/gm, '<div class="flex items-start gap-2 my-1"><span class="text-cyan-600 dark:text-cyan-400 font-bold">-</span><span>$1</span></div>');

    // Newlines that aren't already wrapped in div or table placeholders
    text = text.replace(/\n(?!(?:<div|<\/div|___TABLE_BLOCK_))/g, '<br />');

    // Step 4: Re-insert table & math blocks
    text = text.replace(/___TABLE_BLOCK_(\d+)___/g, (_, idx) => tableBlocks[parseInt(idx)]);
    text = text.replace(/___DISPLAY_MATH_(\d+)___/g, (_, idx) => displayMathBlocks[parseInt(idx)]);
    text = text.replace(/___INLINE_MATH_(\d+)___/g, (_, idx) => inlineMathBlocks[parseInt(idx)]);

    return text;
  }, [content, propText]);

  if (block) {
    return (
      <div
        className={`leading-relaxed ${className || 'text-inherit'}`}
        dangerouslySetInnerHTML={{ __html: renderedHtml }}
      />
    );
  }

  return (
    <span
      className={`leading-relaxed ${className || 'text-inherit'}`}
      dangerouslySetInnerHTML={{ __html: renderedHtml }}
    />
  );
};

export const MathText = React.memo(MathTextComponent);

