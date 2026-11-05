import React, { useState, useEffect, useMemo } from 'react';
import { 
  RotateCw, 
  CheckCircle, 
  RotateCcw, 
  Shuffle, 
  HelpCircle, 
  Sparkles, 
  ChevronLeft, 
  ChevronRight,
  Flame,
  ShieldAlert,
  Zap,
  Award
} from 'lucide-react';
import type { FlashcardItem, SubjectType, WeekFilterType } from '../types';
import { MathText } from './MathText';

interface FlashcardsViewProps {
  flashcards: FlashcardItem[];
  selectedWeek: WeekFilterType;
  selectedSubject: SubjectType;
}

interface DeckMeta {
  id: string;
  title: string;
  icon: string;
  badge: string;
  color: string;
  scope: string;
}

const CURATED_DECKS: DeckMeta[] = [
  {
    id: 'du_speed',
    title: 'DU No-Calculator Speed Tricks',
    icon: '🎯',
    badge: '৫০ কার্ডস',
    color: 'from-emerald-500 to-teal-600',
    scope: 'ভেক্টর ট্রিপলেট, আনুমানিক বর্গমূল ও লগ, দ্রাব্যতা ও বাফার pH শর্টকাট',
  },
  {
    id: 'medical_exceptions',
    title: 'Medical Textbook Exceptions & Values',
    icon: '🩺',
    badge: '৬০ কার্ডস',
    color: 'from-rose-500 to-red-600',
    scope: 'আজমল ও হাসান স্যারের ছক, পর্যায়বৃত্ত ব্যতিক্রম ও ইসহাক স্যারের একক-মান',
  },
  {
    id: 'english_vocab',
    title: 'High-Yield Medical Prepositions & Vocab',
    icon: '🇬🇧',
    badge: '৫০ কার্ডস',
    color: 'from-blue-500 to-indigo-600',
    scope: 'মেডিকেল ১৫-মার্কস ইংলিশ: Prepositions, Vocab ও Spelling',
  },
  {
    id: 'gk_matrix',
    title: '🇧🇩 1971 Liberation War & Core Bangladesh GK Matrix',
    icon: '🇧🇩',
    badge: '৪০ কার্ডস',
    color: 'from-amber-500 to-orange-600',
    scope: 'মেডিকেল ১০-মার্কস জিকে: ১৯৭১ মুক্তিযুদ্ধ, ১১ সেক্টর, সংবিধান ও জাতিসংঘ',
  },
];

export const FlashcardsView: React.FC<FlashcardsViewProps> = ({
  flashcards,
}) => {
  const [selectedDeckId, setSelectedDeckId] = useState<string>('du_speed');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [masteredIds, setMasteredIds] = useState<Set<string>>(() => {
    try {
      const saved = localStorage.getItem('admission_flashcards_mastered');
      return saved ? new Set(JSON.parse(saved)) : new Set();
    } catch {
      return new Set();
    }
  });

  // Persist mastered IDs
  useEffect(() => {
    try {
      localStorage.setItem('admission_flashcards_mastered', JSON.stringify(Array.from(masteredIds)));
    } catch (e) {
      console.error('Failed to save mastered flashcards', e);
    }
  }, [masteredIds]);

  // Filter flashcards by active deck
  const activeDeckCards = useMemo(() => {
    if (selectedDeckId === 'all') {
      return flashcards;
    }
    return flashcards.filter((card) => card.deck_id === selectedDeckId);
  }, [flashcards, selectedDeckId]);

  const [cardsList, setCardsList] = useState<FlashcardItem[]>(activeDeckCards);

  // Sync cards list when deck changes or flashcards update
  useEffect(() => {
    setCardsList(activeDeckCards);
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [activeDeckCards]);

  // Keyboard navigation & shortcuts
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Don't trigger if user is in an input
      if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement).tagName)) return;

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

  const resetCurrentDeckProgress = () => {
    const currentDeckCardIds = new Set(cardsList.map((c) => c.id));
    setMasteredIds((prev) => {
      const next = new Set(prev);
      currentDeckCardIds.forEach((id) => next.delete(id));
      return next;
    });
    setCurrentIndex(0);
    setIsFlipped(false);
  };

  // Deck progress stats
  const masteredCount = cardsList.filter((c) => masteredIds.has(c.id)).length;
  const progressPercent = cardsList.length > 0 
    ? Math.round((masteredCount / cardsList.length) * 100) 
    : 0;

  const currentCard = cardsList[currentIndex] || cardsList[0] || {};
  const isCurrentMastered = currentCard?.id ? masteredIds.has(currentCard.id) : false;

  const frontText = currentCard.front || (currentCard as any).question || (currentCard as any).title || (currentCard as any).prompt || currentCard.topic || "কনটেন্ট লোড হচ্ছে...";
  const backText = currentCard.back || (currentCard as any).answer || (currentCard as any).shortcut || (currentCard as any).formula || (currentCard as any).explanation || currentCard.concept || "";
  const cardHack = currentCard.hack || (currentCard as any).shortcut || '';
  const cardTrap = currentCard.trap || (currentCard as any).negative_trap || (currentCard as any).trap_insight || '';

  // Compute progress for each deck
  const deckProgressMap = useMemo(() => {
    const map: Record<string, { mastered: number; total: number }> = {};
    CURATED_DECKS.forEach((deck) => {
      const deckCards = flashcards.filter((c) => c.deck_id === deck.id);
      const m = deckCards.filter((c) => masteredIds.has(c.id)).length;
      map[deck.id] = { mastered: m, total: deckCards.length };
    });
    return map;
  }, [flashcards, masteredIds]);

  if (!currentCard || cardsList.length === 0) {
    return (
      <div className="py-16 text-center max-w-md mx-auto px-4">
        <Sparkles className="w-10 h-10 text-zinc-400 dark:text-zinc-600 mx-auto mb-2 animate-pulse" />
        <h3 className="text-base font-bold text-zinc-800 dark:text-zinc-200">কোনো ফ্ল্যাশকার্ড পাওয়া যায়নি</h3>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-1">দয়া করে অন্য কোনো ডেক নির্বাচন করুন।</p>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto py-5 px-3 sm:px-4 flex flex-col items-center">
      
      {/* 1. CURATED TOPIC DECKS SELECTOR */}
      <div className="w-full mb-5">
        <div className="text-center sm:text-left mb-3">
          <div className="flex items-center justify-center sm:justify-start gap-2 mb-1">
            <span className="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 flex items-center gap-1">
              <Award className="w-3.5 h-3.5 text-[#056839] dark:text-emerald-400" />
              অ্যাক্টিভ রিকল ডেক্স (Active Recall Decks)
            </span>
            <span className="text-xs font-mono font-bold text-zinc-500">
              {flashcards.length}টি হাই-ইল্ড কার্ড
            </span>
          </div>
          <h1 className="text-lg sm:text-xl font-black text-zinc-900 dark:text-white">
            কিউরেটেড টপিক ডেক নির্বাচন করুন
          </h1>
        </div>

        {/* Deck Pills */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
          {CURATED_DECKS.map((deck) => {
            const isActive = selectedDeckId === deck.id;
            const progress = deckProgressMap[deck.id] || { mastered: 0, total: 0 };
            const pct = progress.total > 0 ? Math.round((progress.mastered / progress.total) * 100) : 0;

            return (
              <button
                key={deck.id}
                onClick={() => setSelectedDeckId(deck.id)}
                className={`p-3 rounded-2xl text-left transition-all border relative overflow-hidden cursor-pointer ${
                  isActive
                    ? 'bg-white dark:bg-zinc-900 border-[#056839] shadow-md ring-2 ring-[#056839]/20 scale-[1.01]'
                    : 'bg-white/80 dark:bg-zinc-900/60 border-zinc-200/80 dark:border-zinc-800 hover:bg-white dark:hover:bg-zinc-900'
                }`}
              >
                <div className="flex items-start justify-between gap-2 mb-1.5">
                  <div className="flex items-center gap-2">
                    <span className="text-lg">{deck.icon}</span>
                    <div>
                      <span className="text-xs sm:text-sm font-bold text-zinc-900 dark:text-white leading-tight block">
                        {deck.title}
                      </span>
                      <span className="text-[10px] text-zinc-500 dark:text-zinc-400 block mt-0.5 line-clamp-1">
                        {deck.scope}
                      </span>
                    </div>
                  </div>
                  <span className={`text-[10px] font-mono px-2 py-0.5 rounded-full font-bold shrink-0 ${
                    isActive
                      ? 'bg-[#056839] text-white'
                      : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400'
                  }`}>
                    {progress.mastered}/{progress.total}
                  </span>
                </div>

                {/* Micro progress bar per deck */}
                <div className="w-full bg-zinc-100 dark:bg-zinc-800 h-1.5 rounded-full overflow-hidden mt-2">
                  <div 
                    className="bg-gradient-to-r from-[#00B09B] to-[#96C93D] h-full transition-all duration-300"
                    style={{ width: `${pct}%` }}
                  />
                </div>
              </button>
            );
          })}
        </div>

        {/* Option for All Decks */}
        <div className="mt-2 flex justify-end">
          <button
            onClick={() => setSelectedDeckId('all')}
            className={`text-xs font-bold px-3 py-1 rounded-xl transition-all cursor-pointer ${
              selectedDeckId === 'all'
                ? 'bg-zinc-800 text-white dark:bg-zinc-200 dark:text-zinc-900'
                : 'text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200'
            }`}
          >
            🌐 সব ডেক একসাথে ({flashcards.length} কার্ডস)
          </button>
        </div>
      </div>

      {/* 2. DECK SUMMARY & ACTIONS */}
      <div className="w-full bg-white dark:bg-zinc-900 rounded-3xl p-4 sm:p-5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm mb-4">
        <div className="flex items-center justify-between pb-3 border-b border-zinc-100 dark:border-zinc-800/80 gap-2 flex-wrap">
          <div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-mono font-bold px-2 py-0.5 rounded-md bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300">
                কার্ড #{currentIndex + 1} / {cardsList.length}
              </span>
              <span className="text-xs font-semibold text-zinc-500">
                {currentCard.topic}
              </span>
            </div>
          </div>

          {/* Action buttons */}
          <div className="flex items-center gap-2">
            <button
              onClick={shuffleCards}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-200 dark:hover:bg-zinc-700 text-xs font-bold transition-all cursor-pointer"
              title="শাফল বা এলোমেলো করুন"
            >
              <Shuffle className="w-3.5 h-3.5" />
              <span>শাফল</span>
            </button>
            <button
              onClick={resetCurrentDeckProgress}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200 dark:hover:bg-zinc-700 text-xs font-bold transition-all cursor-pointer"
              title="এই ডেকের প্রোগ্রেস রিসেট করুন"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>রিসেট</span>
            </button>
          </div>
        </div>

        {/* Progress Bar & Counter */}
        <div className="pt-3">
          <div className="flex items-center justify-between text-xs font-bold mb-1.5">
            <span className="text-zinc-700 dark:text-zinc-300 flex items-center gap-1.5">
              <Flame className="w-4 h-4 text-amber-500" />
              <span>{masteredCount}/{cardsList.length} আয়ত্ত করা হয়েছে</span>
            </span>
            <span className="text-[#056839] dark:text-emerald-400 font-mono">
              {progressPercent}%
            </span>
          </div>
          <div className="w-full bg-zinc-100 dark:bg-zinc-800 h-2 rounded-full overflow-hidden">
            <div 
              className="bg-gradient-to-r from-[#00B09B] to-[#96C93D] h-full transition-all duration-300 rounded-full"
              style={{ width: `${progressPercent}%` }}
            />
          </div>
        </div>
      </div>

      {/* 3. UNIVERSAL HIGH-CONTRAST FLASHCARD */}
      <div 
        className="w-full my-2 cursor-pointer select-none transition-all duration-300"
        onClick={() => setIsFlipped(!isFlipped)}
      >
        <div 
          className={`w-full rounded-3xl p-5 sm:p-7 border-2 transition-all duration-300 shadow-md flex flex-col justify-between ${
            isFlipped 
              ? 'bg-white dark:bg-zinc-900 border-emerald-500/60 dark:border-emerald-500/50 shadow-emerald-500/5' 
              : 'bg-white dark:bg-zinc-900 border-zinc-200/90 dark:border-zinc-800 hover:border-[#056839]/60'
          }`}
        >
          {/* Top Bar */}
          <div className="flex items-center justify-between gap-2 border-b border-zinc-100 dark:border-zinc-800/80 pb-3">
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 rounded-full text-xs font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20">
                {currentCard.subject || 'Admission'}
              </span>
              <span className="text-xs font-semibold text-zinc-500 dark:text-zinc-400">
                {currentCard.deck_title || currentCard.topic}
              </span>
            </div>

            <div className="flex items-center gap-2">
              {isFlipped ? (
                <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 flex items-center gap-1">
                  <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
                  মাস্টার সল্যুশন
                </span>
              ) : (
                <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700 flex items-center gap-1">
                  <HelpCircle className="w-3.5 h-3.5" />
                  প্রশ্ন কার্ড
                </span>
              )}
              {isCurrentMastered && (
                <span className="flex items-center gap-1 text-[11px] font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-200 dark:border-emerald-500/20">
                  <CheckCircle className="w-3.5 h-3.5" /> আয়ত্ত
                </span>
              )}
            </div>
          </div>

          {/* Universal Card Container */}
          <div className="min-h-[220px] flex items-center justify-center p-6 text-center w-full my-auto">
            {!isFlipped ? (
              <div className="text-slate-900 dark:text-slate-100 font-semibold text-lg leading-relaxed max-w-full overflow-x-auto no-scrollbar">
                <MathText text={frontText} content={frontText} />
              </div>
            ) : (
              <div className="w-full space-y-3 text-left">
                {/* Primary Solution & Core Concept */}
                <div className="p-4 rounded-2xl bg-zinc-50 dark:bg-zinc-800/60 border border-zinc-200/70 dark:border-zinc-700/60 text-slate-900 dark:text-slate-100 font-semibold text-base sm:text-lg leading-relaxed overflow-x-auto no-scrollbar">
                  <div className="flex items-center gap-1.5 text-xs font-bold text-emerald-700 dark:text-emerald-400 mb-1.5">
                    <span className="text-amber-500">💡</span>
                    <span>কোর কনসেপ্ট ও সমাধান:</span>
                  </div>
                  <MathText text={currentCard.concept || backText || frontText} content={currentCard.concept || backText || frontText} />
                </div>

                {/* ⚡ 5-Second Hack if present */}
                {cardHack && (
                  <div className="p-3.5 rounded-2xl bg-amber-500/10 dark:bg-amber-950/20 border border-amber-500/20 text-slate-900 dark:text-slate-100 text-xs sm:text-sm font-semibold leading-relaxed overflow-x-auto no-scrollbar">
                    <div className="flex items-center gap-1.5 text-xs font-bold text-amber-700 dark:text-amber-400 mb-1">
                      <Zap className="w-3.5 h-3.5 text-amber-500" />
                      <span>৫-সেকেন্ড স্পিড হ্যাক:</span>
                    </div>
                    <MathText text={cardHack} content={cardHack} />
                  </div>
                )}

                {/* ⚠️ Trap Alert if present */}
                {cardTrap && (
                  <div className="p-3.5 rounded-2xl bg-rose-500/10 dark:bg-rose-950/20 border border-rose-500/20 text-slate-900 dark:text-slate-100 text-xs sm:text-sm font-semibold leading-relaxed overflow-x-auto no-scrollbar">
                    <div className="flex items-center gap-1.5 text-xs font-bold text-rose-700 dark:text-rose-400 mb-1">
                      <ShieldAlert className="w-3.5 h-3.5 text-rose-500" />
                      <span>কমন নেগেটিভ ট্র্যাপ অ্যালার্ট:</span>
                    </div>
                    <MathText text={cardTrap} content={cardTrap} />
                  </div>
                )}

                {/* Direct Fallback if neither concept nor hack nor trap */}
                {!currentCard.concept && !cardHack && !cardTrap && (
                  <div className="text-slate-900 dark:text-slate-100 font-semibold text-lg leading-relaxed max-w-full overflow-x-auto no-scrollbar text-center">
                    <MathText text={backText || frontText} content={backText || frontText} />
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Bottom Flip Prompt */}
          <div className="flex items-center justify-center gap-2 text-xs text-zinc-400 dark:text-zinc-500 font-bold border-t border-zinc-100 dark:border-zinc-800/80 pt-3">
            <RotateCw className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
            <span>{isFlipped ? 'পুনরায় প্রশ্ন দেখতে ট্যাপ করুন' : 'কার্ডের সমাধান, ৫-সেকেন্ড হ্যাক ও ট্র্যাপ দেখতে ট্যাপ করুন'}</span>
          </div>
        </div>
      </div>

      {/* 4. RESPONSE & NAVIGATION CONTROLS */}
      <div className="w-full flex items-center justify-between gap-3 mt-4">
        <button
          onClick={prevCard}
          className="p-3 rounded-2xl bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 border border-zinc-200/80 dark:border-zinc-800 shadow-sm transition-all cursor-pointer"
          title="পূর্ববর্তী কার্ড (ArrowLeft)"
        >
          <ChevronLeft className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-3 flex-1 justify-center max-w-sm">
          <button
            onClick={markReview}
            className="flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-white dark:bg-zinc-900 hover:bg-rose-50 dark:hover:bg-rose-950/30 text-rose-700 dark:text-rose-300 border border-rose-200 dark:border-rose-900/40 text-xs sm:text-sm font-bold shadow-xs transition-all active:scale-95 cursor-pointer"
            title="আবার পড়ুন (কীবোর্ড ১ চাপুন)"
          >
            <RotateCcw className="w-4 h-4" />
            <span>আবার পড়ব [1]</span>
          </button>

          <button
            onClick={markMastered}
            className="flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs sm:text-sm font-bold shadow-md transition-all active:scale-95 cursor-pointer"
            title="মনে আছে (কীবোর্ড ২ চাপুন)"
          >
            <CheckCircle className="w-4 h-4" />
            <span>মনে আছে [2]</span>
          </button>
        </div>

        <button
          onClick={nextCard}
          className="p-3 rounded-2xl bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 border border-zinc-200/80 dark:border-zinc-800 shadow-sm transition-all cursor-pointer"
          title="পরবর্তী কার্ড (ArrowRight)"
        >
          <ChevronRight className="w-5 h-5" />
        </button>
      </div>

      {/* Keyboard Shortcuts Hint */}
      <div className="mt-4 text-[11px] text-zinc-400 dark:text-zinc-500 font-mono text-center hidden sm:block">
        [Space] উল্টান • [←] পূর্ববর্তী • [→] পরবর্তী • [1] আবার পড়ব • [2] মনে আছে
      </div>

    </div>
  );
};
