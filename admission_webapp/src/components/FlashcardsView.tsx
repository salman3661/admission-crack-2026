import React, { useState, useEffect } from 'react';
import { 
  RotateCw, 
  CheckCircle, 
  RotateCcw, 
  Shuffle, 
  HelpCircle, 
  Sparkles, 
  ChevronLeft, 
  ChevronRight,
  Flame
} from 'lucide-react';
import type { FlashcardItem, SubjectType, WeekFilterType } from '../types';
import { MathText } from './MathText';

interface FlashcardsViewProps {
  flashcards: FlashcardItem[];
  selectedWeek: WeekFilterType;
  selectedSubject: SubjectType;
}

export const FlashcardsView: React.FC<FlashcardsViewProps> = ({
  flashcards,
  selectedWeek,
  selectedSubject,
}) => {
  // Filter flashcards
  const filteredCards = flashcards.filter((card) => {
    const matchWeek = selectedWeek === 'all' || card.week_id === selectedWeek;
    const matchSubject = selectedSubject === 'All' || card.subject === selectedSubject;
    return matchWeek && matchSubject;
  });

  const [cardsList, setCardsList] = useState<FlashcardItem[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [masteredIds, setMasteredIds] = useState<Set<string>>(new Set());

  // Update card list on filter change
  useEffect(() => {
    setCardsList(filteredCards);
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [selectedWeek, selectedSubject, flashcards]);

  // Keyboard navigation & shortcuts
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.code === 'Space') {
        e.preventDefault();
        setIsFlipped((prev) => !prev);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        nextCard();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        prevCard();
      } else if (e.key === '1') {
        markReview();
      } else if (e.key === '2') {
        markMastered();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentIndex, cardsList.length, isFlipped]);

  const nextCard = () => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev + 1) % (cardsList.length || 1));
  };

  const prevCard = () => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev - 1 + cardsList.length) % (cardsList.length || 1));
  };

  const markMastered = () => {
    if (cardsList.length === 0) return;
    const currentId = cardsList[currentIndex].id;
    setMasteredIds((prev) => new Set(prev).add(currentId));
    nextCard();
  };

  const markReview = () => {
    if (cardsList.length === 0) return;
    const currentId = cardsList[currentIndex].id;
    setMasteredIds((prev) => {
      const next = new Set(prev);
      next.delete(currentId);
      return next;
    });
    nextCard();
  };

  const shuffleCards = () => {
    setIsFlipped(false);
    const shuffled = [...cardsList].sort(() => Math.random() - 0.5);
    setCardsList(shuffled);
    setCurrentIndex(0);
  };

  const resetProgress = () => {
    setMasteredIds(new Set());
    setIsFlipped(false);
    setCurrentIndex(0);
  };

  if (cardsList.length === 0) {
    return (
      <div className="py-20 text-center">
        <Sparkles className="w-12 h-12 text-slate-400 dark:text-slate-600 mx-auto mb-3 animate-pulse" />
        <h3 className="text-lg font-bold text-slate-800 dark:text-slate-300">কোনো ফ্ল্যাশকার্ড পাওয়া যায়নি</h3>
        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">দয়া করে ফিল্টার পরিবর্তন করে চেষ্টা করুন।</p>
      </div>
    );
  }

  const currentCard = cardsList[currentIndex];
  const isMastered = masteredIds.has(currentCard.id);
  const masteredCount = cardsList.filter((c) => masteredIds.has(c.id)).length;
  const progressPercent = Math.round((masteredCount / cardsList.length) * 100);

  return (
    <div className="max-w-3xl mx-auto py-8 px-4 flex flex-col items-center">
      {/* Top Header & Progress */}
      <div className="w-full flex flex-wrap items-center justify-between pb-4 gap-3 border-b border-slate-200 dark:border-slate-800">
        <div className="flex items-center gap-3">
          <span className="p-2 rounded-xl bg-brand-500/10 text-brand-600 dark:text-brand-400 border border-brand-500/20">
            <Sparkles className="w-5 h-5" />
          </span>
          <div>
            <h2 className="text-base sm:text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
              অ্যাক্টিভ রিকল ফ্ল্যাশকার্ড
              <span className="text-xs px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-normal">
                {cardsList.length}টি কার্ড
              </span>
            </h2>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              ক্লিক করুন বা <kbd className="px-1 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-[10px] border border-slate-200 dark:border-slate-700">Space</kbd> চেপে কার্ড উল্টান
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-2">
          <button
            onClick={shuffleCards}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-800 text-xs font-semibold shadow-sm transition-all"
            title="কার্ড উলটপালট করুন"
          >
            <Shuffle className="w-3.5 h-3.5" />
            <span>শাফল</span>
          </button>
          <button
            onClick={resetProgress}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-800 text-xs font-semibold shadow-sm transition-all"
            title="প্রগ্রেস রিসেট করুন"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>রিসেট</span>
          </button>
        </div>
      </div>

      {/* Progress Bar & Stats */}
      <div className="w-full my-4">
        <div className="flex items-center justify-between text-xs font-semibold mb-1.5">
          <span className="text-slate-600 dark:text-slate-400 flex items-center gap-1.5">
            <Flame className="w-4 h-4 text-amber-500 dark:text-amber-400" />
            মাস্টার করা হয়েছে: <strong className="text-emerald-600 dark:text-emerald-400">{masteredCount}</strong> / {cardsList.length}
          </span>
          <span className="text-brand-600 dark:text-brand-400 font-mono font-bold">{progressPercent}%</span>
        </div>
        <div className="w-full bg-slate-200 dark:bg-slate-900 h-2 rounded-full overflow-hidden border border-slate-200 dark:border-slate-800">
          <div 
            className="bg-gradient-to-r from-brand-500 to-emerald-400 h-full transition-all duration-300"
            style={{ width: `${progressPercent}%` }}
          />
        </div>
      </div>

      {/* 3D Flip Flashcard */}
      <div 
        className="w-full h-80 sm:h-96 perspective-1000 my-4 cursor-pointer select-none"
        onClick={() => setIsFlipped(!isFlipped)}
      >
        <div 
          className={`w-full h-full relative transition-transform duration-500 transform-style-3d rounded-3xl ${
            isFlipped ? 'rotate-y-180' : ''
          }`}
        >
          {/* Card Front (Trigger / Question) */}
          <div className="absolute inset-0 w-full h-full bg-gradient-to-b from-white via-slate-50 to-slate-100 dark:from-slate-900 dark:via-slate-900/95 dark:to-slate-950 rounded-3xl p-6 sm:p-8 border border-slate-200 dark:border-slate-800 shadow-xl dark:shadow-2xl flex flex-col justify-between backface-hidden group hover:border-brand-400 dark:hover:border-brand-500/40 transition-all">
            <div className="flex items-center justify-between">
              <span className="px-2.5 py-1 rounded-lg text-xs font-bold bg-brand-50 dark:bg-brand-500/10 text-brand-700 dark:text-brand-300 border border-brand-200 dark:border-brand-500/20 uppercase tracking-wider">
                {currentCard.subject} • {currentCard.topic}
              </span>
              <div className="flex items-center gap-2">
                {isMastered && (
                  <span className="flex items-center gap-1 text-[11px] font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-200 dark:border-emerald-500/20">
                    <CheckCircle className="w-3.5 h-3.5" /> মনে আছে
                  </span>
                )}
                <span className="text-xs font-mono text-slate-500 dark:text-slate-400">
                  {currentIndex + 1} / {cardsList.length}
                </span>
              </div>
            </div>

            <div className="my-auto py-4 text-center">
              <span className="inline-block p-2 rounded-2xl bg-slate-100 dark:bg-slate-800/80 text-brand-600 dark:text-brand-400 mb-3 border border-slate-200 dark:border-slate-700/50">
                <HelpCircle className="w-6 h-6" />
              </span>
              <div className="text-lg sm:text-2xl font-bold text-slate-900 dark:text-white tracking-wide leading-relaxed">
                <MathText content={currentCard.front} />
              </div>
            </div>

            <div className="flex items-center justify-center gap-2 text-xs text-slate-500 dark:text-slate-400 font-medium">
              <RotateCw className="w-3.5 h-3.5 text-brand-500 dark:text-brand-400 animate-spin-slow" />
              <span>কার্ডের উত্তর দেখতে ক্লিক করুন</span>
            </div>
          </div>

          {/* Card Back (Solution / Breakdown) */}
          <div className="absolute inset-0 w-full h-full bg-gradient-to-b from-white via-slate-50 to-slate-100 dark:from-slate-900 dark:via-slate-900/95 dark:to-slate-950 rounded-3xl p-6 sm:p-8 border border-brand-300 dark:border-brand-500/40 shadow-xl dark:shadow-2xl flex flex-col justify-between backface-hidden rotate-y-180 overflow-y-auto">
            <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800/80 pb-3">
              <span className="px-2.5 py-1 rounded-lg text-xs font-bold bg-emerald-50 dark:bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-500/20 uppercase tracking-wider">
                মাস্টার সলিউশন ও হ্যাকস
              </span>
              <span className="text-xs text-slate-500 dark:text-slate-400">
                {currentCard.subject}
              </span>
            </div>

            <div className="my-auto py-3 text-left">
              <MathText content={currentCard.back} block />
            </div>

            <div className="pt-2 text-center text-xs text-slate-500 dark:text-slate-400 border-t border-slate-200 dark:border-slate-800/60">
              পুনরায় প্রশ্ন দেখতে ক্লিক করুন
            </div>
          </div>
        </div>
      </div>

      {/* Spaced Repetition Response Controls */}
      <div className="w-full flex items-center justify-between gap-3 mt-4">
        <button
          onClick={prevCard}
          className="p-3 rounded-2xl bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-800 shadow-sm transition-all"
          title="পূর্ববর্তী কার্ড"
        >
          <ChevronLeft className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-3 flex-1 justify-center">
          <button
            onClick={markReview}
            className="flex-1 max-w-[200px] flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-white dark:bg-slate-900 hover:bg-rose-50 dark:hover:bg-rose-950/40 text-rose-700 dark:text-rose-300 hover:text-rose-800 dark:hover:text-rose-200 border border-rose-300 dark:border-rose-500/30 hover:border-rose-400 dark:hover:border-rose-500/60 text-sm font-bold shadow-sm transition-all"
          >
            <RotateCcw className="w-4 h-4" />
            <span>আবার পড়ব (1)</span>
          </button>

          <button
            onClick={markMastered}
            className="flex-1 max-w-[200px] flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white border border-emerald-400/40 text-sm font-bold shadow-lg shadow-emerald-600/20 transition-all"
          >
            <CheckCircle className="w-4 h-4" />
            <span>মনে আছে (2)</span>
          </button>
        </div>

        <button
          onClick={nextCard}
          className="p-3 rounded-2xl bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-800 shadow-sm transition-all"
          title="পরবর্তী কার্ড"
        >
          <ChevronRight className="w-5 h-5" />
        </button>
      </div>
    </div>
  );
};
