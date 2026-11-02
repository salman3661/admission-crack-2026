import React, { useMemo } from 'react';
import katex from 'katex';

interface MathTextProps {
  content: string;
  className?: string;
  block?: boolean;
}

export const MathText: React.FC<MathTextProps> = ({ content, className = '', block = false }) => {
  const renderedHtml = useMemo(() => {
    if (!content) return '';

    let text = content;

    // Step 1: Replace $$...$$ with block math placeholders
    const displayMathBlocks: string[] = [];
    text = text.replace(/\$\$(.*?)\$\$/gs, (_, math) => {
      try {
        const rendered = katex.renderToString(math.trim(), {
          displayMode: true,
          throwOnError: false,
        });
        displayMathBlocks.push(rendered);
      } catch {
        displayMathBlocks.push(`<span class="text-rose-500 dark:text-rose-400 font-mono">$$${math}$$</span>`);
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
        });
        inlineMathBlocks.push(rendered);
      } catch {
        inlineMathBlocks.push(`<span class="text-rose-500 dark:text-rose-400 font-mono">$${math}$</span>`);
      }
      return `___INLINE_MATH_${inlineMathBlocks.length - 1}___`;
    });

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
  }, [content]);

  if (block) {
    return (
      <div
        className={`leading-relaxed text-slate-800 dark:text-slate-200 ${className}`}
        dangerouslySetInnerHTML={{ __html: renderedHtml }}
      />
    );
  }

  return (
    <span
      className={`leading-relaxed text-slate-800 dark:text-slate-200 ${className}`}
      dangerouslySetInnerHTML={{ __html: renderedHtml }}
    />
  );
};
