import React from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import type { AppMode } from '../types';

interface CategorySwitcherProps {
  currentMode: AppMode;
  onSelectMode: (mode: AppMode) => void;
}

const sequence: { id: AppMode; label: string }[] = [
  { id: 'slides', label: '⚡ কোর ফর্মুলা' },
  { id: 'flashcards', label: '💡 শর্টকাট ভল্ট' },
  { id: 'vault', label: '⚠️ ট্র্যাপ ক্যাপসুল' },
  { id: 'exam', label: '📝 মডেল টেস্ট' },
];

export const CategorySwitcher: React.FC<CategorySwitcherProps> = ({
  currentMode,
  onSelectMode,
}) => {
  const currentIndex = sequence.findIndex((s) => s.id === currentMode);
  if (currentIndex === -1) return null;

  const prevItem = sequence[(currentIndex - 1 + sequence.length) % sequence.length];
  const nextItem = sequence[(currentIndex + 1) % sequence.length];

  return (
    <div className="max-w-4xl mx-auto px-4 mt-8 pt-4 pb-4 border-t border-zinc-200/80 dark:border-zinc-800">
      <div className="flex items-center justify-between gap-3">
        <button
          onClick={() => {
            onSelectMode(prevItem.id);
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }}
          className="flex-1 max-w-[190px] flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-800 text-xs font-bold shadow-sm transition-all active:scale-95"
        >
          <ChevronLeft className="w-4 h-4 shrink-0 text-zinc-400" />
          <span className="truncate">{prevItem.label}</span>
        </button>

        <span className="text-[10px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-wider shrink-0">
          নেক্সট সেকশন
        </span>

        <button
          onClick={() => {
            onSelectMode(nextItem.id);
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }}
          className="flex-1 max-w-[190px] flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold shadow-md shadow-[#056839]/20 transition-all active:scale-95"
        >
          <span className="truncate">{nextItem.label}</span>
          <ChevronRight className="w-4 h-4 shrink-0" />
        </button>
      </div>
    </div>
  );
};

