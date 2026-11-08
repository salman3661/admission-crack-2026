import React, { useState, useEffect, useMemo, useRef } from 'react';
import { 
  RotateCw, 
  CheckCircle, 
  HelpCircle, 
  Sparkles, 
  ChevronLeft, 
  ChevronRight, 
  Flame, 
  ShieldAlert, 
  Zap, 
  Award, 
  Search, 
  Layers, 
  LayoutGrid, 
  Bookmark, 
  Shuffle, 
  ArrowLeft,
  Calendar,
  Check,
  X
} from 'lucide-react';
import { MathText } from './MathText';
import type { RecentGKCard, RecentGKMonthMeta, AppMode } from '../types';
import rawData from '../data/recent_gk_monthly.json';

export interface ActiveRecallViewProps {
  onSelectMode?: (mode: AppMode) => void;
  initialMonth?: string;
}

interface MonthlyGKData {
  months: RecentGKMonthMeta[];
  total_cards: number;
  data: Record<string, RecentGKCard[]>;
  cards: RecentGKCard[];
}

const gkData = rawData as MonthlyGKData;

const CATEGORIES = [
  'সব ক্যাটাগরি',
  'জাতীয় অর্জন ও প্রশাসন',
  'মেগা প্রকল্প ও অর্থনীতি',
  'আন্তর্জাতিক ও ভূরাজনীতি',
  'পুরস্কার ও সম্মেলন',
  'দিবস ও পরিবেশ',
  'ক্রীড়া ও রেকর্ড'
];

export const ActiveRecallView: React.FC<ActiveRecallViewProps> = ({
  onSelectMode,
  initialMonth = 'all'
}) => {
  const [selectedMonth, setSelectedMonth] = useState<string>(initialMonth);
  const [selectedCategory, setSelectedCategory] = useState<string>('সব ক্যাটাগরি');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [viewMode, setViewMode] = useState<'card' | 'grid'>('card');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const sliderRef = useRef<HTMLDivElement>(null);

  // Leitner / Mastery persistence
  const [masteredIds, setMasteredIds] = useState<Set<string>>(() => {
    try {
      const saved = localStorage.getItem('admission_monthly_gk_mastered');
      return saved ? new Set(JSON.parse(saved)) : new Set();
    } catch {
      return new Set();
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('admission_monthly_gk_mastered', JSON.stringify(Array.from(masteredIds)));
    } catch (e) {
      console.error('Failed to save mastered GK cards', e);
    }
  }, [masteredIds]);

  // Filtered Cards based on month, category, and search query
  const filteredCards = useMemo(() => {
    let pool: RecentGKCard[] = [];
    if (selectedMonth === 'all') {
      pool = gkData.cards;
    } else {
      pool = gkData.data[selectedMonth] || [];
    }

    if (selectedCategory !== 'সব ক্যাটাগরি') {
      pool = pool.filter((c) => c.category === selectedCategory);
    }

    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase().trim();
      pool = pool.filter(
        (c) =>
          c.topic.toLowerCase().includes(q) ||
          c.front.toLowerCase().includes(q) ||
          c.concept.toLowerCase().includes(q) ||
          c.hack.toLowerCase().includes(q) ||
          c.trap.toLowerCase().includes(q)
      );
    }

    return pool;
  }, [selectedMonth, selectedCategory, searchQuery]);

  const [cardsList, setCardsList] = useState<RecentGKCard[]>(filteredCards);

  useEffect(() => {
    setCardsList(filteredCards);
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [filteredCards]);

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
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
      } else if (e.key.toLowerCase() === 's') {
        shuffleCards();
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

  const shuffleCards = () => {
    setIsFlipped(false);
    const shuffled = [...cardsList].sort(() => Math.random() - 0.5);
    setCardsList(shuffled);
    setCurrentIndex(0);
  };

  const currentCard: RecentGKCard | undefined = cardsList[currentIndex];
  const isCurrentMastered = currentCard ? masteredIds.has(currentCard.id) : false;

  const markMastered = () => {
    if (!currentCard) return;
    setMasteredIds((prev) => {
      const next = new Set(prev);
      next.add(currentCard.id);
      return next;
    });
    nextCard();
  };

  const markReview = () => {
    if (!currentCard) return;
    setMasteredIds((prev) => {
      const next = new Set(prev);
      next.delete(currentCard.id);
      return next;
    });
    nextCard();
  };

  const toggleMastered = (id: string, e?: React.MouseEvent) => {
    if (e) e.stopPropagation();
    setMasteredIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  };

  // Scroll month slider horizontally
  const scrollSlider = (direction: 'left' | 'right') => {
    if (sliderRef.current) {
      const amount = direction === 'left' ? -220 : 220;
      sliderRef.current.scrollBy({ left: amount, behavior: 'smooth' });
    }
  };

  const masteredCount = useMemo(() => {
    return cardsList.filter((c) => masteredIds.has(c.id)).length;
  }, [cardsList, masteredIds]);

  const totalMasteredAll = masteredIds.size;
  const progressPercent = cardsList.length > 0 ? Math.round((masteredCount / cardsList.length) * 100) : 0;

  return (
    <div className="max-w-5xl mx-auto px-3 sm:px-4 py-4 sm:py-6">
      
      {/* 1. TOP HEADER & BREADCRUMB */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-5">
        <div>
          <div className="flex items-center gap-2 mb-1">
            {onSelectMode && (
              <button
                onClick={() => onSelectMode('decks')}
                className="p-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition-colors cursor-pointer"
                title="হোমে ফিরে যান"
              >
                <ArrowLeft className="w-4 h-4" />
              </button>
            )}
            <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase tracking-wider bg-emerald-600 text-white flex items-center gap-1 shadow-xs">
              <Sparkles className="w-3 h-3" />
              UDVASH 2026 MONTHLY GK HIGHLIGHTS
            </span>
            <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-amber-500/15 text-amber-700 dark:text-amber-400 ring-1 ring-amber-500/30">
              {gkData.total_cards} টি হাই-ইয়েল্ড কার্ডস
            </span>
          </div>

          <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white flex items-center gap-2">
            <span>📅 সাম্প্রতিক সাধারণ জ্ঞান (জানুয়ারি – অক্টোবর ২০২৬)</span>
          </h1>
          <p className="text-xs text-slate-600 dark:text-slate-400 mt-0.5">
            উদ্ভাসের মান্থলি জিকে লেকচার ও পিডিএফ নোটের ১০০% ভর্তি-প্রাসঙ্গিক অ্যাক্টিভ রিকল ফ্ল্যাশকার্ড ও ট্র্যাপ ডিফেন্স
          </p>
        </div>

        {/* Global Progress Pill */}
        <div className="flex items-center gap-2.5 bg-white/80 dark:bg-slate-900/80 p-2.5 rounded-2xl ring-1 ring-slate-200/80 dark:ring-slate-800/80 shadow-xs self-start sm:self-auto">
          <div className="w-9 h-9 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold text-sm">
            <Flame className="w-5 h-5 text-amber-500" />
          </div>
          <div>
            <div className="text-[10px] text-slate-500 font-bold">মোট আয়ত্ত</div>
            <div className="text-xs font-black text-slate-900 dark:text-white font-mono">
              {totalMasteredAll} / {gkData.total_cards} ({Math.round((totalMasteredAll / gkData.total_cards) * 100)}%)
            </div>
          </div>
        </div>
      </div>

      {/* 2. MONTH-WISE HORIZONTAL SLIDER TABS */}
      <div className="relative mb-3.5 group">
        <button
          onClick={() => scrollSlider('left')}
          className="absolute left-0 top-1/2 -translate-y-1/2 z-10 w-7 h-7 rounded-full bg-white/90 dark:bg-slate-800/90 shadow-md ring-1 ring-slate-200 dark:ring-slate-700 flex items-center justify-center text-slate-700 dark:text-slate-300 hover:scale-105 active:scale-95 transition-all hidden sm:flex cursor-pointer"
          aria-label="Scroll left"
        >
          <ChevronLeft className="w-4 h-4" />
        </button>

        <div
          ref={sliderRef}
          className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none px-1 scroll-smooth"
        >
          {/* 'All' Tab */}
          <button
            onClick={() => setSelectedMonth('all')}
            className={`px-3.5 py-2 rounded-2xl text-xs font-bold shrink-0 transition-all cursor-pointer flex items-center gap-1.5 ring-1 ${
              selectedMonth === 'all'
                ? 'bg-[#056839] text-white ring-[#056839] shadow-sm shadow-emerald-600/30'
                : 'bg-white/80 dark:bg-slate-900/80 text-slate-700 dark:text-slate-300 ring-slate-200/80 dark:ring-slate-800/80 hover:bg-slate-100 dark:hover:bg-slate-800'
            }`}
          >
            <Calendar className="w-3.5 h-3.5" />
            <span>সব মাস</span>
            <span className={`px-1.5 py-0.2 rounded-full text-[10px] font-mono ${
              selectedMonth === 'all' ? 'bg-white/25 text-white' : 'bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
            }`}>
              {gkData.total_cards}
            </span>
          </button>

          {/* Month Tabs */}
          {gkData.months.map((m) => {
            const count = gkData.data[m.id]?.length || 0;
            const isSelected = selectedMonth === m.id;
            return (
              <button
                key={m.id}
                onClick={() => setSelectedMonth(m.id)}
                className={`px-3.5 py-2 rounded-2xl text-xs font-bold shrink-0 transition-all cursor-pointer flex items-center gap-2 ring-1 ${
                  isSelected
                    ? 'bg-[#056839] text-white ring-[#056839] shadow-sm shadow-emerald-600/30'
                    : 'bg-white/80 dark:bg-slate-900/80 text-slate-700 dark:text-slate-300 ring-slate-200/80 dark:ring-slate-800/80 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
              >
                <span>{m.label_bn}</span>
                <span className={`text-[9px] px-1.5 py-0.5 rounded-md font-medium hidden md:inline-block ${
                  isSelected ? 'bg-emerald-700/60 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                }`}>
                  {m.badge}
                </span>
                <span className={`px-1.5 py-0.2 rounded-full text-[10px] font-mono ${
                  isSelected ? 'bg-white/25 text-white' : 'bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                }`}>
                  {count}
                </span>
              </button>
            );
          })}
        </div>

        <button
          onClick={() => scrollSlider('right')}
          className="absolute right-0 top-1/2 -translate-y-1/2 z-10 w-7 h-7 rounded-full bg-white/90 dark:bg-slate-800/90 shadow-md ring-1 ring-slate-200 dark:ring-slate-700 flex items-center justify-center text-slate-700 dark:text-slate-300 hover:scale-105 active:scale-95 transition-all hidden sm:flex cursor-pointer"
          aria-label="Scroll right"
        >
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>

      {/* 3. FILTER, SEARCH & VIEW MODE BAR */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-2.5 mb-4">
        {/* Category Pills (Horizontal scroll on mobile) */}
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
          {CATEGORIES.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-2.5 py-1 rounded-xl text-[11px] font-bold shrink-0 transition-all cursor-pointer ${
                selectedCategory === cat
                  ? 'bg-emerald-500/20 text-emerald-800 dark:text-emerald-300 ring-1 ring-emerald-500/40'
                  : 'bg-slate-100 dark:bg-slate-800/70 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Search & Toggle view */}
        <div className="flex items-center gap-2">
          <div className="relative flex-1 sm:w-48">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="টপিক বা তথ্য খুঁজুন..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-8 pr-2.5 py-1.5 rounded-xl text-xs bg-white dark:bg-slate-900 ring-1 ring-slate-200 dark:ring-slate-800 focus:ring-2 focus:ring-emerald-500 outline-none text-slate-900 dark:text-white"
            />
          </div>

          <div className="flex items-center rounded-xl bg-slate-100 dark:bg-slate-800 p-0.5 ring-1 ring-slate-200 dark:ring-slate-700 shrink-0">
            <button
              onClick={() => setViewMode('card')}
              className={`px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1 transition-colors cursor-pointer ${
                viewMode === 'card'
                  ? 'bg-white dark:bg-slate-900 text-emerald-700 dark:text-emerald-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400'
              }`}
              title="অ্যাক্টিভ রিকল কার্ড"
            >
              <Layers className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">ফ্ল্যাশকার্ড</span>
            </button>
            <button
              onClick={() => setViewMode('grid')}
              className={`px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1 transition-colors cursor-pointer ${
                viewMode === 'grid'
                  ? 'bg-white dark:bg-slate-900 text-emerald-700 dark:text-emerald-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400'
              }`}
              title="চিটশিট গ্রিড ভিউ"
            >
              <LayoutGrid className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">চিটশিট</span>
            </button>
          </div>
        </div>
      </div>

      {/* 4. MAIN CARD / GRID VIEW */}
      {cardsList.length === 0 ? (
        <div className="p-12 text-center rounded-3xl bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80">
          <HelpCircle className="w-10 h-10 text-slate-400 mx-auto mb-2" />
          <h3 className="text-base font-bold text-slate-800 dark:text-slate-200">কোনো ফ্ল্যাশকার্ড পাওয়া যায়নি</h3>
          <p className="text-xs text-slate-500 mt-1">অন্য কোনো ফিল্টার বা মাস নির্বাচন করুন।</p>
        </div>
      ) : viewMode === 'card' && currentCard ? (
        /* =========================================================================
           ACTIVE RECALL 3D FLIP CARD MODE
           ========================================================================= */
        <div className="space-y-4">
          
          {/* Card Meta & Step Progress */}
          <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-1 font-medium">
            <div className="flex items-center gap-2">
              <span className="px-2 py-0.5 rounded-lg bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 font-mono font-bold text-[11px]">
                কার্ড {currentIndex + 1} / {cardsList.length}
              </span>
              <span className="font-semibold text-slate-700 dark:text-slate-300">
                {currentCard.month_bn} ২০২৬
              </span>
            </div>

            <div className="flex items-center gap-3">
              <span className="text-[11px] font-mono text-emerald-600 dark:text-emerald-400 font-bold">
                {masteredCount} আয়ত্ত ({progressPercent}%)
              </span>
              <button
                onClick={shuffleCards}
                className="flex items-center gap-1 text-[11px] hover:text-emerald-600 cursor-pointer"
                title="কার্ড শাফল করুন (S)"
              >
                <Shuffle className="w-3 h-3" />
                <span className="hidden sm:inline">শাফল</span>
              </button>
            </div>
          </div>

          {/* Progress bar */}
          <div className="w-full h-1.5 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-emerald-500 to-teal-500 transition-all duration-300"
              style={{ width: `${((currentIndex + 1) / cardsList.length) * 100}%` }}
            />
          </div>

          {/* 3D Flip Card Container */}
          <div className="perspective-1000 min-h-[380px] sm:min-h-[420px] select-none">
            <div
              onClick={() => setIsFlipped(!isFlipped)}
              className={`relative w-full min-h-[380px] sm:min-h-[420px] transform-style-3d transition-transform duration-500 cursor-pointer rounded-3xl ${
                isFlipped ? 'rotate-y-180' : ''
              }`}
            >
              
              {/* ---------------- FRONT FACE ---------------- */}
              <div className="absolute inset-0 backface-hidden rounded-3xl p-6 sm:p-8 backdrop-blur-xl bg-white/95 dark:bg-slate-900/95 ring-1 ring-slate-200/90 dark:ring-slate-800/90 shadow-md flex flex-col justify-between hover:ring-emerald-500/60 transition-all">
                <div>
                  <div className="flex items-center justify-between gap-2 mb-4">
                    <div className="flex items-center gap-2 flex-wrap">
                      <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/30">
                        {currentCard.category}
                      </span>
                      <span className="px-2 py-0.5 rounded-md text-[10px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">
                        {currentCard.topic}
                      </span>
                    </div>

                    <div className="flex items-center gap-1.5">
                      {isCurrentMastered && (
                        <span className="flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500 text-white shadow-xs">
                          <Check className="w-3 h-3" /> আয়ত্ত
                        </span>
                      )}
                      <button
                        onClick={(e) => toggleMastered(currentCard.id, e)}
                        className={`p-1.5 rounded-xl transition-colors ${
                          isCurrentMastered
                            ? 'text-amber-500 bg-amber-500/10'
                            : 'text-slate-400 hover:text-amber-500 hover:bg-slate-100 dark:hover:bg-slate-800'
                        }`}
                        title="মাস্টার হিসেবে চিহ্নিত করুন"
                      >
                        <Bookmark className="w-4 h-4" />
                      </button>
                    </div>
                  </div>

                  {/* Question Prompt */}
                  <div className="mt-4 sm:mt-6">
                    <span className="text-[11px] font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider flex items-center gap-1 mb-2">
                      <Sparkles className="w-3.5 h-3.5" />
                      অ্যাক্টিভ রিকল প্রশ্ন
                    </span>
                    <h2 className="text-lg sm:text-2xl font-black text-slate-900 dark:text-white leading-relaxed">
                      {currentCard.front}
                    </h2>
                  </div>
                </div>

                <div>
                  {/* Exam Targets */}
                  <div className="flex items-center gap-1.5 flex-wrap mb-4">
                    <span className="text-[11px] text-slate-500 font-medium">টার্গেট:</span>
                    {currentCard.exam_targets.map((t) => (
                      <span
                        key={t}
                        className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300"
                      >
                        {t}
                      </span>
                    ))}
                  </div>

                  {/* Flip Prompt Hint */}
                  <div className="pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
                    <span className="flex items-center gap-1 text-emerald-600 dark:text-emerald-400 font-bold">
                      <RotateCw className="w-3.5 h-3.5 animate-spin-slow" />
                      উত্তর দেখতে ক্লিক করুন (বা Space চাপুন)
                    </span>
                    <span className="text-[11px] font-mono">Front</span>
                  </div>
                </div>
              </div>

              {/* ---------------- BACK FACE ---------------- */}
              <div className="absolute inset-0 backface-hidden rotate-y-180 rounded-3xl p-6 sm:p-8 backdrop-blur-xl bg-gradient-to-br from-white via-emerald-50/20 to-teal-50/30 dark:from-slate-900 dark:via-slate-900/90 dark:to-emerald-950/20 ring-1 ring-emerald-500/40 shadow-lg flex flex-col justify-between overflow-y-auto">
                <div className="space-y-4">
                  <div className="flex items-center justify-between gap-2 border-b border-emerald-500/20 pb-2.5">
                    <div className="flex items-center gap-1.5">
                      <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
                      <span className="text-xs font-black text-emerald-700 dark:text-emerald-300">
                        {currentCard.topic}
                      </span>
                    </div>
                    <span className="px-2 py-0.5 rounded-md text-[10px] font-mono bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 font-bold">
                      {currentCard.month_bn} ২০২৬
                    </span>
                  </div>

                  {/* 1. Core Concept */}
                  <div className="p-3.5 rounded-2xl bg-emerald-500/10 dark:bg-emerald-500/10 ring-1 ring-emerald-500/20">
                    <div className="flex items-center gap-1.5 text-xs font-extrabold text-emerald-800 dark:text-emerald-300 mb-1">
                      <CheckCircle className="w-4 h-4 text-emerald-600 shrink-0" />
                      <span>সঠিক উত্তর ও মূল তথ্য:</span>
                    </div>
                    <div className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-medium">
                      <MathText text={currentCard.concept} />
                    </div>
                  </div>

                  {/* 2. Speed Hack */}
                  <div className="p-3.5 rounded-2xl bg-amber-500/10 dark:bg-amber-500/10 ring-1 ring-amber-500/20">
                    <div className="flex items-center gap-1.5 text-xs font-extrabold text-amber-800 dark:text-amber-300 mb-1">
                      <Zap className="w-4 h-4 text-amber-500 shrink-0" />
                      <span>শর্টকাট হ্যাক ও মেমোরি ট্রিক:</span>
                    </div>
                    <div className="text-xs text-slate-800 dark:text-slate-200 leading-relaxed font-medium">
                      <MathText text={currentCard.hack} />
                    </div>
                  </div>

                  {/* 3. Trap Shield */}
                  <div className="p-3.5 rounded-2xl bg-rose-500/10 dark:bg-rose-500/10 ring-1 ring-rose-500/20">
                    <div className="flex items-center gap-1.5 text-xs font-extrabold text-rose-800 dark:text-rose-300 mb-1">
                      <ShieldAlert className="w-4 h-4 text-rose-600 shrink-0" />
                      <span>পরীক্ষার অপশন ট্র্যাপ:</span>
                    </div>
                    <div className="text-xs text-slate-800 dark:text-slate-200 leading-relaxed font-medium">
                      <MathText text={currentCard.trap} />
                    </div>
                  </div>
                </div>

                {/* Flip Back hint */}
                <div className="pt-3 mt-3 border-t border-slate-200/60 dark:border-slate-800 flex items-center justify-between text-xs text-slate-500">
                  <span className="text-[11px] text-slate-500">কার্ডটি পুনরায় ঘোরাতে ক্লিক করুন</span>
                  <span className="text-[11px] font-mono text-emerald-600 dark:text-emerald-400 font-bold">Answer Back</span>
                </div>
              </div>

            </div>
          </div>

          {/* 5. CAROUSEL CONTROLS BAR */}
          <div className="flex items-center justify-between gap-2 pt-2">
            <button
              onClick={prevCard}
              className="px-4 py-2.5 rounded-2xl bg-white dark:bg-slate-800 ring-1 ring-slate-200 dark:ring-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-bold flex items-center gap-1 active:scale-95 transition-all cursor-pointer shadow-xs"
              title="পূর্ববর্তী (Left Arrow)"
            >
              <ChevronLeft className="w-4 h-4" />
              <span>পূর্ববর্তী</span>
            </button>

            {/* Quick Assessment Action Buttons */}
            <div className="flex items-center gap-2">
              <button
                onClick={markReview}
                className="px-3.5 py-2.5 rounded-2xl bg-rose-500/15 hover:bg-rose-500/25 text-rose-700 dark:text-rose-300 ring-1 ring-rose-500/30 text-xs font-black flex items-center gap-1.5 active:scale-95 transition-all cursor-pointer"
                title="মনে নেই (Key 1)"
              >
                <X className="w-4 h-4 text-rose-600" />
                <span className="hidden sm:inline">আবার প্র্যাকটিস</span>
              </button>

              <button
                onClick={() => setIsFlipped(!isFlipped)}
                className="px-4 py-2.5 rounded-2xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-black flex items-center gap-1.5 active:scale-95 transition-all cursor-pointer shadow-sm"
                title="কার্ড উল্টান (Space)"
              >
                <RotateCw className="w-3.5 h-3.5" />
                <span>{isFlipped ? 'প্রশ্ন দেখুন' : 'উত্তর দেখুন'}</span>
              </button>

              <button
                onClick={markMastered}
                className="px-3.5 py-2.5 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white ring-1 ring-emerald-600 text-xs font-black flex items-center gap-1.5 active:scale-95 transition-all cursor-pointer shadow-xs"
                title="সম্পূর্ণ আয়ত্ত (Key 2)"
              >
                <Check className="w-4 h-4" />
                <span className="hidden sm:inline">আয়ত্ত করেছি</span>
              </button>
            </div>

            <button
              onClick={nextCard}
              className="px-4 py-2.5 rounded-2xl bg-white dark:bg-slate-800 ring-1 ring-slate-200 dark:ring-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-bold flex items-center gap-1 active:scale-95 transition-all cursor-pointer shadow-xs"
              title="পরবর্তী (Right Arrow)"
            >
              <span>পরবর্তী</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      ) : (
        /* =========================================================================
           CHEAT SHEET / GRID REVISION MODE
           ========================================================================= */
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
          {cardsList.map((card, idx) => {
            const isMastered = masteredIds.has(card.id);
            return (
              <div
                key={card.id}
                className={`p-4 sm:p-5 rounded-3xl backdrop-blur-xl bg-white/90 dark:bg-slate-900/90 ring-1 transition-all flex flex-col justify-between ${
                  isMastered
                    ? 'ring-emerald-500/50 bg-emerald-500/5 dark:bg-emerald-950/10'
                    : 'ring-slate-200/80 dark:ring-slate-800/80 hover:ring-emerald-500/40'
                }`}
              >
                <div>
                  <div className="flex items-center justify-between gap-2 mb-2.5">
                    <div className="flex items-center gap-1.5 flex-wrap">
                      <span className="px-2 py-0.5 rounded-full text-[9px] font-black bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/30">
                        {card.month_bn} ২০২৬
                      </span>
                      <span className="px-2 py-0.5 rounded-md text-[9px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">
                        {card.category}
                      </span>
                    </div>

                    <button
                      onClick={(e) => toggleMastered(card.id, e)}
                      className={`p-1 rounded-lg transition-colors cursor-pointer ${
                        isMastered ? 'text-emerald-600 bg-emerald-500/15' : 'text-slate-400 hover:text-emerald-600'
                      }`}
                      title={isMastered ? 'আয়ত্ত তালিকা থেকে সরান' : 'আয়ত্ত হিসেবে যোগ করুন'}
                    >
                      <Check className="w-3.5 h-3.5" />
                    </button>
                  </div>

                  <h3 className="text-sm font-extrabold text-slate-900 dark:text-white mb-2 leading-snug">
                    {card.front}
                  </h3>

                  {/* Concept Capsule */}
                  <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 ring-1 ring-slate-200/60 dark:ring-slate-700/60 text-xs text-slate-700 dark:text-slate-300 leading-relaxed mb-2.5">
                    <span className="font-bold text-emerald-600 dark:text-emerald-400">সঠিক তথ্য: </span>
                    <MathText text={card.concept} />
                  </div>

                  {/* Hack & Trap */}
                  <div className="space-y-1.5 text-[11px]">
                    <div className="flex items-start gap-1.5 text-amber-800 dark:text-amber-300">
                      <Zap className="w-3.5 h-3.5 text-amber-500 shrink-0 mt-0.5" />
                      <span><strong>হ্যাক:</strong> {card.hack}</span>
                    </div>
                    <div className="flex items-start gap-1.5 text-rose-800 dark:text-rose-300">
                      <ShieldAlert className="w-3.5 h-3.5 text-rose-500 shrink-0 mt-0.5" />
                      <span><strong>ট্র্যাপ:</strong> {card.trap}</span>
                    </div>
                  </div>
                </div>

                <div className="flex items-center justify-between text-[10px] text-slate-400 pt-3 mt-3 border-t border-slate-100 dark:border-slate-800">
                  <span className="font-mono">#{idx + 1}</span>
                  <div className="flex items-center gap-1">
                    {card.exam_targets.map((t) => (
                      <span key={t} className="px-1.5 py-0.2 rounded bg-slate-100 dark:bg-slate-800 font-mono">
                        {t}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* 6. BOTTOM CHEAT TIPS BANNER */}
      <div className="mt-8 p-4 rounded-3xl backdrop-blur-xl bg-gradient-to-r from-emerald-500/10 via-teal-500/10 to-blue-500/10 ring-1 ring-emerald-500/25 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-emerald-600 text-white flex items-center justify-center shrink-0 shadow-md">
            <Award className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-xs sm:text-sm font-black text-slate-900 dark:text-white">
              ভর্তি পরীক্ষার সাম্প্রতিক সাধারণ জ্ঞানে ১০০% কমন কৌশল
            </h4>
            <p className="text-[11px] text-slate-600 dark:text-slate-400 mt-0.5">
              বিগত ভর্তি পরীক্ষার ধারা অনুযায়ী প্রতিটি মাসের জাতীয় মেগা প্রকল্প, নির্বাচন/সংবিধানের ধারা এবং নোবেল ২০২৬ থেকে সরাসরি প্রশ্ন আসে।
            </p>
          </div>
        </div>

        <button
          onClick={() => {
            setSelectedMonth('all');
            setSelectedCategory('সব ক্যাটাগরি');
            shuffleCards();
          }}
          className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shrink-0 active:scale-95 transition-all cursor-pointer shadow-xs flex items-center gap-1.5"
        >
          <Shuffle className="w-3.5 h-3.5" />
          <span>সম্পূর্ণ রিভিশন ড্রিল</span>
        </button>
      </div>

    </div>
  );
};

export default ActiveRecallView;
