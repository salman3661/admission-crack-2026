import React, { useMemo } from 'react';
import katex from 'katex';

interface MathTextProps {
  content?: string;
  text?: string;
  className?: string;
  block?: boolean;
}

export const MathText: React.FC<MathTextProps> = ({ content, text: propText, className = '', block = false }) => {
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
      try {
        const rendered = katex.renderToString(math.trim(), {
          displayMode: true,
          throwOnError: false,
          strict: 'ignore',
        });
        displayMathBlocks.push(`<div class="overflow-x-auto no-scrollbar py-1 my-1">${rendered}</div>`);
      } catch {
        displayMathBlocks.push(`<div class="overflow-x-auto no-scrollbar py-1 my-1 text-rose-500 dark:text-rose-400 font-mono">$$${math}$$</div>`);
      }
      return `___DISPLAY_MATH_${displayMathBlocks.length - 1}___`;
    });

    // Step 2: Replace $...$ with inline math placeholders
    const inlineMathBlocks: string[] = [];
    text = text.replace(/\$(.*?)\$/g, (_, math) => {
      try {
        const rendered = katex.renderToString(math.trim(), {
          displayMode: false,
          throwOnError: false,
          strict: 'ignore',
        });
        inlineMathBlocks.push(`<span class="inline-block max-w-full overflow-x-auto no-scrollbar align-middle">${rendered}</span>`);
      } catch {
        inlineMathBlocks.push(`<span class="text-rose-500 dark:text-rose-400 font-mono">$${math}$</span>`);
      }
      return `___INLINE_MATH_${inlineMathBlocks.length - 1}___`;
    });

    // Step 2b: Fallback for any bare LaTeX commands outside $ (e.g. \sqrt, \frac, \log, \pm)
    if (/\\[a-zA-Z]+/.test(text)) {
      text = text.replace(/([^\s\u0980-\u09FF]*\\[a-zA-Z]+(?:\{[^{}]*\}|\[[^[\]]*\]|[^\s\u0980-\u09FF])*)/g, (match) => {
        const trimmed = match.trim();
        if (!trimmed || !trimmed.includes('\\')) return match;
        try {
          const rendered = katex.renderToString(trimmed, {
            displayMode: false,
            throwOnError: false,
            strict: 'ignore',
          });
          inlineMathBlocks.push(`<span class="inline-block max-w-full overflow-x-auto no-scrollbar align-middle">${rendered}</span>`);
          return `___INLINE_MATH_${inlineMathBlocks.length - 1}___`;
        } catch {
          return match;
        }
      });
    }

    // Step 3: Handle markdown formatting
    // Bold **text**
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong class="font-bold text-slate-900 dark:text-slate-100">$1</strong>');
    
    // Inline code `code`
    text = text.replace(/`([^`]+)`/g, '<code class="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-amber-700 dark:text-amber-300 font-mono text-sm border border-slate-300 dark:border-slate-700/60">$1</code>');

    // Bullet points (leading • or -)
    text = text.replace(/^•\s*(.*?)$/gm, '<div class="flex items-start gap-2 my-1"><span class="text-brand-600 dark:text-brand-400 font-bold">•</span><span>$1</span></div>');
    text = text.replace(/^-\s*(.*?)$/gm, '<div class="flex items-start gap-2 my-1"><span class="text-cyan-600 dark:text-cyan-400 font-bold">-</span><span>$1</span></div>');

    // Newlines that aren't already wrapped in div
    text = text.replace(/\n(?!(?:<div|<\/div))/g, '<br />');

    // Step 4: Re-insert math blocks
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
