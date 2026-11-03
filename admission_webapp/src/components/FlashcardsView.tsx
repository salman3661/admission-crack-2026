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
    setTimeout(() => {
      setCurrentIndex((prev) => (prev + 1 < cardsList.length ? prev + 1 : 0));
    }, 150);
  };

  const prevCard = () => {
    setIsFlipped(false);
    setTimeout(() => {
      setCurrentIndex((prev) => (prev - 1 >= 0 ? prev - 1 : cardsList.length - 1));
    }, 150);
  };

  const markMastered = () => {
    if (!cardsList[currentIndex]) return;
    setMasteredIds((prev) => new Set(prev).add(cardsList[currentIndex].id));
    nextCard();
  };

  const markReview = () => {
    if (!cardsList[currentIndex]) return;
    setMasteredIds((prev) => {
      const next = new Set(prev);
      next.delete(cardsList[currentIndex].id);
      return next;
    });
    nextCard();
  };

  const shuffleCards = () => {
    setIsFlipped(false);
    setCardsList([...cardsList].sort(() => Math.random() - 0.5));
    setCurrentIndex(0);
  };

  const resetProgress = () => {
    setMasteredIds(new Set());
    setCurrentIndex(0);
    setIsFlipped(false);
  };

  if (cardsList.length === 0) {
    return (
      <div className="py-16 text-center max-w-md mx-auto px-4">
        <Sparkles className="w-10 h-10 text-zinc-400 dark:text-zinc-600 mx-auto mb-2 animate-pulse" />
        <h3 className="text-base font-bold text-zinc-800 dark:text-zinc-200">কোনো শর্টকাট কার্ড পাওয়া যায়নি</h3>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-1">দয়া করে উপরে অন্য সপ্তাহ বা বিষয় নির্বাচন করুন।</p>
      </div>
    );
  }

  const currentCard = cardsList[currentIndex];
  const isMastered = masteredIds.has(currentCard.id);
  const masteredCount = cardsList.filter((c) => masteredIds.has(c.id)).length;
  const progressPercent = Math.round((masteredCount / cardsList.length) * 100);

  return (
    <div className="max-w-2xl mx-auto py-4 px-3 sm:px-4 flex flex-col items-center">
      
      {/* Top Header & Progress */}
      <div className="w-full flex items-center justify-between pb-3 gap-2 border-b border-zinc-200/80 dark:border-zinc-800">
        <div>
          <h2 className="text-sm sm:text-base font-extrabold text-zinc-900 dark:text-white flex items-center gap-1.5">
            <span>💡 অ্যাক্টিভ রিকল শর্টকাট</span>
            <span className="text-[11px] font-mono px-2 py-0.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-700">
              {currentIndex + 1} / {cardsList.length}
            </span>
          </h2>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-1.5">
          <button
            onClick={shuffleCards}
            className="flex items-center gap-1 px-2.5 py-1 rounded-xl bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 border border-zinc-200 dark:border-zinc-800 text-xs font-semibold shadow-sm transition-all"
            title="শাফল"
          >
            <Shuffle className="w-3.5 h-3.5" />
            <span className="hidden xs:inline">শাফল</span>
          </button>
          <button
            onClick={resetProgress}
            className="flex items-center gap-1 px-2.5 py-1 rounded-xl bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 hover:bg-zinc-100 dark:hover:bg-zinc-800 border border-zinc-200 dark:border-zinc-800 text-xs font-semibold shadow-sm transition-all"
            title="রিসেট"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span className="hidden xs:inline">রিসেট</span>
          </button>
        </div>
      </div>

      {/* Progress Bar & Stats */}
      <div className="w-full my-3">
        <div className="flex items-center justify-between text-xs font-semibold mb-1">
          <span className="text-zinc-600 dark:text-zinc-400 flex items-center gap-1">
            <Flame className="w-3.5 h-3.5 text-amber-500" />
            আয়ত্ত করা: <strong className="text-emerald-600 dark:text-emerald-400">{masteredCount}</strong> / {cardsList.length}
          </span>
          <span className="text-[#056839] dark:text-emerald-400 font-mono font-bold">{progressPercent}%</span>
        </div>
        <div className="w-full bg-zinc-200 dark:bg-zinc-800 h-1.5 rounded-full overflow-hidden">
          <div 
            className="bg-gradient-to-r from-[#00B09B] to-[#96C93D] h-full transition-all duration-300"
            style={{ width: `${progressPercent}%` }}
          />
        </div>
      </div>

      {/* 3D Flip Flashcard */}
      <div 
        className="w-full h-80 sm:h-88 perspective-1000 my-2 cursor-pointer select-none"
        onClick={() => setIsFlipped(!isFlipped)}
      >
        <div 
          className={`w-full h-full relative transition-transform duration-500 transform-style-3d rounded-2xl ${
            isFlipped ? 'rotate-y-180' : ''
          }`}
        >
          {/* Card Front (Trigger / Question) */}
          <div className="absolute inset-0 w-full h-full bg-white dark:bg-zinc-900 rounded-2xl p-5 sm:p-6 border border-zinc-200/90 dark:border-zinc-800 shadow-sm flex flex-col justify-between backface-hidden group hover:border-[#056839]/50 transition-all">
            <div className="flex items-center justify-between">
              <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 uppercase tracking-wider">
                {currentCard.subject} • {currentCard.topic}
              </span>
              <div className="flex items-center gap-1.5">
                {isMastered && (
                  <span className="flex items-center gap-1 text-[10px] font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-200 dark:border-emerald-500/20">
                    <CheckCircle className="w-3 h-3" /> মনে আছে
                  </span>
                )}
              </div>
            </div>

            <div className="my-auto py-3 text-center overflow-x-auto no-scrollbar">
              <span className="inline-block p-2 rounded-xl bg-zinc-100 dark:bg-zinc-800 text-[#056839] dark:text-emerald-400 mb-2 border border-zinc-200 dark:border-zinc-700">
                <HelpCircle className="w-5 h-5" />
              </span>
              <div className="text-base sm:text-xl font-bold text-zinc-900 dark:text-white tracking-wide leading-relaxed">
                <MathText content={currentCard.front} />
              </div>
            </div>

            <div className="flex items-center justify-center gap-1.5 text-xs text-zinc-400 dark:text-zinc-500 font-medium">
              <RotateCw className="w-3.5 h-3.5 text-[#056839] dark:text-emerald-400" />
              <span>কার্ডের শর্টকাট দেখতে ট্যাপ করুন</span>
            </div>
          </div>

          {/* Card Back (Solution / Breakdown) */}
          <div className="absolute inset-0 w-full h-full bg-white dark:bg-zinc-900 rounded-2xl p-5 sm:p-6 border border-[#056839]/40 dark:border-emerald-500/40 shadow-sm flex flex-col justify-between backface-hidden rotate-y-180 overflow-y-auto no-scrollbar">
            <div className="flex items-center justify-between border-b border-zinc-100 dark:border-zinc-800 pb-2">
              <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-50 dark:bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-500/20 uppercase tracking-wider">
                মাস্টার শর্টকাট ও ছন্দ
              </span>
              <span className="text-xs font-semibold text-zinc-400">
                {currentCard.subject}
              </span>
            </div>

            <div className="my-auto py-3 text-left overflow-x-auto no-scrollbar text-xs sm:text-sm">
              <MathText content={currentCard.back} block />
            </div>

            <div className="pt-2 text-center text-[11px] text-zinc-400 border-t border-zinc-100 dark:border-zinc-800">
              পুনরায় প্রশ্ন দেখতে ট্যাপ করুন
            </div>
          </div>
        </div>
      </div>

      {/* Response Controls */}
      <div className="w-full flex items-center justify-between gap-2 mt-2">
        <button
          onClick={prevCard}
          className="p-2.5 rounded-xl bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 hover:bg-zinc-100 dark:hover:bg-zinc-800 border border-zinc-200 dark:border-zinc-800 shadow-sm transition-all"
          title="পূর্ববর্তী"
        >
          <ChevronLeft className="w-4 h-4" />
        </button>

        <div className="flex items-center gap-2 flex-1 justify-center max-w-xs">
          <button
            onClick={markReview}
            className="flex-1 flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-white dark:bg-zinc-900 hover:bg-rose-50 dark:hover:bg-rose-950/40 text-rose-700 dark:text-rose-300 border border-rose-300 dark:border-rose-900/40 text-xs font-bold shadow-sm transition-all"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>আবার পড়ব</span>
          </button>

          <button
            onClick={markMastered}
            className="flex-1 flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold shadow-sm transition-all active:scale-95"
          >
            <CheckCircle className="w-3.5 h-3.5" />
            <span>মনে আছে</span>
          </button>
        </div>

        <button
          onClick={nextCard}
          className="p-2.5 rounded-xl bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 hover:bg-zinc-100 dark:hover:bg-zinc-800 border border-zinc-200 dark:border-zinc-800 shadow-sm transition-all"
          title="পরবর্তী"
        >
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>

    </div>
  );
};
