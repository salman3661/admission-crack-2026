import React, { useState, useEffect, useMemo, useRef, useCallback } from 'react';
import { 
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
  Shuffle, 
  ArrowLeft,
  Calendar
} from 'lucide-react';
import { MathText } from './MathText';
import type { RecentGKCard, RecentGKMonthMeta, AppMode } from '../types';
import rawGkData from '../data/recent_gk_monthly.json';
import rawEnglishData from '../data/sure_shot_english_predictors.json';

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

interface EnglishPredictorItem {
  id: string;
  subject: string;
  cluster_id: string;
  cluster_name: string;
  cluster_name_bn: string;
  rule_id: string;
  rule_title: string;
  rule_formula: string;
  q: string;
  stem?: string;
  opts: string[];
  options?: string[];
  ans: number;
  correct_index?: number;
  exp: string;
  explanation?: string;
  speed_hack: string;
  trap_alert: string;
  trap?: string;
  exam_target: string;
  star_ranking: string;
  source?: string;
}

interface EnglishBlueprintData {
  metadata: {
    title: string;
    subtitle: string;
    total_predictors: number;
    clusters: string[];
  };
  predictors: EnglishPredictorItem[];
}

const gkData = rawGkData as MonthlyGKData;
const englishData = rawEnglishData as unknown as EnglishBlueprintData;

const GK_CATEGORIES = [
  'সব ক্যাটাগরি',
  'জাতীয় অর্জন ও প্রশাসন',
  'মেগা প্রকল্প ও অর্থনীতি',
  'আন্তর্জাতিক ও ভূরাজনীতি',
  'পুরস্কার ও সম্মেলন',
  'দিবস ও পরিবেশ',
  'ক্রীড়া ও রেকর্ড'
];

const ENGLISH_CLUSTERS = [
  { id: 'all', label: 'সব ক্লাস্টার' },
  { id: 'cluster_1_prepositions', label: 'Appropriate Prepositions' },
  { id: 'cluster_2_sva_verbs', label: 'Subject-Verb Agreement' },
  { id: 'cluster_3_sentence_correction', label: 'Sentence Correction' },
  { id: 'cluster_4_vocabulary_spelling', label: 'Vocab & Spelling Traps' },
  { id: 'cluster_5_pos_clauses', label: 'Parts of Speech & Clauses' },
  { id: 'cluster_medical_qb', label: 'MAT Direct Repeats' }
];

const ActiveRecallViewComponent: React.FC<ActiveRecallViewProps> = ({
  onSelectMode,
  initialMonth = 'all'
}) => {
  // Main Segment Switcher: 'gk' vs 'english'
  const [deckType, setDeckType] = useState<'gk' | 'english'>('gk');

  // Shared View Mode: 'card' vs 'grid'
  const [viewMode, setViewMode] = useState<'card' | 'grid'>('card');
  const [searchQuery, setSearchQuery] = useState<string>('');

  // --------------------------------------------------------------------------
  // GK DECK STATES
  // --------------------------------------------------------------------------
  const [selectedMonth, setSelectedMonth] = useState<string>(initialMonth);
  const [selectedCategory, setSelectedCategory] = useState<string>('সব ক্যাটাগরি');
  const [gkCurrentIndex, setGkCurrentIndex] = useState(0);
  const [gkIsFlipped, setGkIsFlipped] = useState(false);
  const sliderRef = useRef<HTMLDivElement>(null);

  // GK Leitner persistence
  const [masteredGkIds, setMasteredGkIds] = useState<Set<string>>(() => {
    try {
      const saved = localStorage.getItem('admission_monthly_gk_mastered');
      return saved ? new Set(JSON.parse(saved)) : new Set();
    } catch {
      return new Set();
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('admission_monthly_gk_mastered', JSON.stringify(Array.from(masteredGkIds)));
    } catch (e) {
      console.error('Failed to save mastered GK cards', e);
    }
  }, [masteredGkIds]);

  const filteredGkCards = useMemo(() => {
    let pool: RecentGKCard[] = [];
    if (selectedMonth === 'all') {
      pool = gkData.cards;
    } else {
      pool = gkData.data[selectedMonth] || [];
    }

    if (selectedCategory !== 'সব ক্যাটাগরি') {
      pool = pool.filter((c) => c.category === selectedCategory);
    }

    if (searchQuery.trim() && deckType === 'gk') {
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
  }, [selectedMonth, selectedCategory, searchQuery, deckType]);

  const [gkCardsList, setGkCardsList] = useState<RecentGKCard[]>(filteredGkCards);

  useEffect(() => {
    setGkCardsList(filteredGkCards);
    setGkCurrentIndex(0);
    setGkIsFlipped(false);
  }, [filteredGkCards]);

  // --------------------------------------------------------------------------
  // ENGLISH PREDICTOR DECK STATES
  // --------------------------------------------------------------------------
  const [selectedEnglishCluster, setSelectedEnglishCluster] = useState<string>('all');
  const [engCurrentIndex, setEngCurrentIndex] = useState(0);
  const [engIsFlipped, setEngIsFlipped] = useState(false);
  const [userSelectedOption, setUserSelectedOption] = useState<number | null>(null);

  // English Leitner persistence
  const [masteredEngIds, setMasteredEngIds] = useState<Set<string>>(() => {
    try {
      const saved = localStorage.getItem('admission_english_mastered');
      return saved ? new Set(JSON.parse(saved)) : new Set();
    } catch {
      return new Set();
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('admission_english_mastered', JSON.stringify(Array.from(masteredEngIds)));
    } catch (e) {
      console.error('Failed to save mastered English cards', e);
    }
  }, [masteredEngIds]);

  const filteredEnglishPredictors = useMemo(() => {
    let list = englishData.predictors || [];

    if (selectedEnglishCluster !== 'all') {
      list = list.filter((p) => p.cluster_id === selectedEnglishCluster);
    }

    if (searchQuery.trim() && deckType === 'english') {
      const q = searchQuery.toLowerCase().trim();
      list = list.filter(
        (p) =>
          p.q.toLowerCase().includes(q) ||
          p.rule_title.toLowerCase().includes(q) ||
          p.rule_formula.toLowerCase().includes(q) ||
          p.speed_hack.toLowerCase().includes(q) ||
          p.trap_alert.toLowerCase().includes(q)
      );
    }

    return list;
  }, [selectedEnglishCluster, searchQuery, deckType]);

  const [engList, setEngList] = useState<EnglishPredictorItem[]>(filteredEnglishPredictors);

  useEffect(() => {
    setEngList(filteredEnglishPredictors);
    setEngCurrentIndex(0);
    setEngIsFlipped(false);
    setUserSelectedOption(null);
  }, [filteredEnglishPredictors]);

  // --------------------------------------------------------------------------
  // NAVIGATION HANDLERS (Keyboard support)
  // --------------------------------------------------------------------------
  const nextGkCard = useCallback(() => {
    setGkIsFlipped(false);
    setTimeout(() => {
      setGkCurrentIndex((prev) => (prev + 1 < gkCardsList.length ? prev + 1 : 0));
    }, 120);
  }, [gkCardsList.length]);

  const prevGkCard = useCallback(() => {
    setGkIsFlipped(false);
    setTimeout(() => {
      setGkCurrentIndex((prev) => (prev - 1 >= 0 ? prev - 1 : gkCardsList.length - 1));
    }, 120);
  }, [gkCardsList.length]);

  const shuffleGkCards = useCallback(() => {
    setGkIsFlipped(false);
    const shuffled = [...gkCardsList].sort(() => Math.random() - 0.5);
    setGkCardsList(shuffled);
    setGkCurrentIndex(0);
  }, [gkCardsList]);

  const nextEngCard = useCallback(() => {
    setEngIsFlipped(false);
    setUserSelectedOption(null);
    setTimeout(() => {
      setEngCurrentIndex((prev) => (prev + 1 < engList.length ? prev + 1 : 0));
    }, 120);
  }, [engList.length]);

  const prevEngCard = useCallback(() => {
    setEngIsFlipped(false);
    setUserSelectedOption(null);
    setTimeout(() => {
      setEngCurrentIndex((prev) => (prev - 1 >= 0 ? prev - 1 : engList.length - 1));
    }, 120);
  }, [engList.length]);

  const shuffleEngCards = useCallback(() => {
    setEngIsFlipped(false);
    setUserSelectedOption(null);
    const shuffled = [...engList].sort(() => Math.random() - 0.5);
    setEngList(shuffled);
    setEngCurrentIndex(0);
  }, [engList]);

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement).tagName)) return;

      if (e.code === 'Space') {
        e.preventDefault();
        if (deckType === 'gk') setGkIsFlipped((prev) => !prev);
        else setEngIsFlipped((prev) => !prev);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        if (deckType === 'gk') nextGkCard();
        else nextEngCard();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        if (deckType === 'gk') prevGkCard();
        else prevEngCard();
      } else if (e.key.toLowerCase() === 's') {
        if (deckType === 'gk') shuffleGkCards();
        else shuffleEngCards();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [deckType, nextGkCard, nextEngCard, prevGkCard, prevEngCard, shuffleGkCards, shuffleEngCards]);

  const currentGkCard: RecentGKCard | undefined = gkCardsList[gkCurrentIndex];
  const isCurrentGkMastered = currentGkCard ? masteredGkIds.has(currentGkCard.id) : false;

  const toggleGkMastered = (id: string, e?: React.MouseEvent) => {
    if (e) e.stopPropagation();
    setMasteredGkIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const currentEngCard: EnglishPredictorItem | undefined = engList[engCurrentIndex];
  const isCurrentEngMastered = currentEngCard ? masteredEngIds.has(currentEngCard.id) : false;

  const toggleEngMastered = (id: string, e?: React.MouseEvent) => {
    if (e) e.stopPropagation();
    setMasteredEngIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const scrollSlider = (direction: 'left' | 'right') => {
    if (sliderRef.current) {
      const amount = direction === 'left' ? -220 : 220;
      sliderRef.current.scrollBy({ left: amount, behavior: 'smooth' });
    }
  };

  const gkMasteredCount = useMemo(() => {
    return gkCardsList.filter((c) => masteredGkIds.has(c.id)).length;
  }, [gkCardsList, masteredGkIds]);

  const engMasteredCount = useMemo(() => {
    return engList.filter((c) => masteredEngIds.has(c.id)).length;
  }, [engList, masteredEngIds]);

  return (
    <div className="max-w-5xl mx-auto px-3 sm:px-4 py-4 sm:py-6 space-y-5">
      
      {/* 1. TOP HEADER & BREADCRUMB */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
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
              GK & ENGLISH DUAL MASTERY DECK
            </span>
          </div>

          <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white flex items-center gap-2">
            <span>{deckType === 'gk' ? '📅 সাম্প্রতিক সাধারণ জ্ঞান (Recent GK 2026)' : '🇬🇧 শিওর-শট ইংলিশ প্রেডিক্টর (Sure-Shot English)'}</span>
          </h1>
          <p className="text-xs text-slate-600 dark:text-slate-400 mt-0.5">
            {deckType === 'gk'
              ? 'উদ্ভাসের মান্থলি জিকে লেকচার ও নোটের ৮০টি কার্ড: ত্রয়োদশ নির্বাচন, নোবেল ২০২৬ ও মেগা প্রজেক্ট'
              : 'মেডিকেল ১৫-মার্কস ও ঢাবি নিশ্চিত কমন ৮৮টি প্রেডিক্টর: ৫টি কোর ক্লাস্টার, স্পিড হ্যাক ও ট্র্যাপ ডিফেন্স'}
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
              {deckType === 'gk' 
                ? `${masteredGkIds.size} / ${gkData.total_cards} (${Math.round((masteredGkIds.size / gkData.total_cards) * 100)}%)`
                : `${masteredEngIds.size} / ${englishData.metadata.total_predictors} (${Math.round((masteredEngIds.size / englishData.metadata.total_predictors) * 100)}%)`}
            </div>
          </div>
        </div>
      </div>

      {/* 2. DUAL DECK SEGMENTED PILL SWITCHER */}
      <div className="p-1 rounded-2xl bg-white/90 dark:bg-slate-900/90 ring-1 ring-slate-200/90 dark:ring-slate-800/90 shadow-xs flex items-center gap-1">
        <button
          onClick={() => {
            setDeckType('gk');
            setSearchQuery('');
          }}
          className={`flex-1 py-2.5 px-3 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-2 cursor-pointer ${
            deckType === 'gk'
              ? 'bg-gradient-to-r from-emerald-600 to-teal-600 text-white shadow-xs'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
          }`}
        >
          <span>🇧🇩 সাম্প্রতিক সাধারণ জ্ঞান</span>
          <span className={`px-2 py-0.5 rounded-full text-[10px] font-mono ${deckType === 'gk' ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'}`}>
            {gkData.total_cards} কার্ডস
          </span>
        </button>

        <button
          onClick={() => {
            setDeckType('english');
            setSearchQuery('');
          }}
          className={`flex-1 py-2.5 px-3 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-2 cursor-pointer ${
            deckType === 'english'
              ? 'bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-xs'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
          }`}
        >
          <span>🇬🇧 শিওর-শট ইংলিশ প্রেডিক্টর</span>
          <span className={`px-2 py-0.5 rounded-full text-[10px] font-mono ${deckType === 'english' ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'}`}>
            {englishData.metadata.total_predictors} প্রশ্ন
          </span>
        </button>
      </div>

      {/* 3. TABS BAR (Month Slider for GK, Cluster Pills for English) */}
      {deckType === 'gk' ? (
        <div className="relative group">
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
      ) : (
        /* English Clusters Bar */
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
          {ENGLISH_CLUSTERS.map((cl) => {
            const isSelected = selectedEnglishCluster === cl.id;
            return (
              <button
                key={cl.id}
                onClick={() => setSelectedEnglishCluster(cl.id)}
                className={`px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 transition-all cursor-pointer border ${
                  isSelected
                    ? 'bg-purple-600 text-white border-purple-600 shadow-xs'
                    : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
              >
                {cl.label}
              </button>
            );
          })}
        </div>
      )}

      {/* 4. SEARCH & VIEW MODE CONTROLS */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-2.5">
        {/* Categories if GK */}
        {deckType === 'gk' ? (
          <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
            {GK_CATEGORIES.map((cat) => (
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
        ) : (
          <div className="text-xs text-slate-500 dark:text-slate-400 font-medium">
            ক্লাস্টারভিত্তিক মোট <strong className="text-purple-600 dark:text-purple-400 font-bold">{engList.length}টি</strong> নিশ্চিত প্রশ্ন
          </div>
        )}

        {/* Search & Toggle view */}
        <div className="flex items-center gap-2">
          <div className="relative flex-1 sm:w-48">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder={deckType === 'gk' ? "টপিক বা তথ্য খুঁজুন..." : "নিয়ম বা প্রশ্ন খুঁজুন..."}
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
            >
              <LayoutGrid className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">গ্রিড ভিউ</span>
            </button>
          </div>
        </div>
      </div>

      {/* 5. MAIN DISPLAY (GK vs ENGLISH) */}
      {deckType === 'gk' ? (
        /* GK DISPLAY */
        gkCardsList.length === 0 ? (
          <div className="p-12 text-center rounded-3xl bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80">
            <HelpCircle className="w-10 h-10 text-slate-400 mx-auto mb-2" />
            <h3 className="text-base font-bold text-slate-800 dark:text-slate-200">কোনো ফ্ল্যাশকার্ড পাওয়া যায়নি</h3>
          </div>
        ) : viewMode === 'card' && currentGkCard ? (
          <div className="space-y-4">
            <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-1 font-medium">
              <span className="px-2 py-0.5 rounded-lg bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 font-mono font-bold text-[11px]">
                কার্ড {gkCurrentIndex + 1} / {gkCardsList.length} • {currentGkCard.month_bn} ২০২৬
              </span>
              <span className="text-[11px] font-mono text-emerald-600 font-bold">
                {gkMasteredCount} আয়ত্ত
              </span>
            </div>

            <div
              onClick={() => setGkIsFlipped(!gkIsFlipped)}
              className="p-6 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm cursor-pointer min-h-[300px] flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    {currentGkCard.category}
                  </span>
                  <button
                    onClick={(e) => toggleGkMastered(currentGkCard.id, e)}
                    className={`p-1.5 rounded-xl border transition-colors ${
                      isCurrentGkMastered 
                        ? 'bg-emerald-600 text-white border-emerald-600' 
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-400 border-slate-200 dark:border-slate-700'
                    }`}
                  >
                    <CheckCircle className="w-4 h-4" />
                  </button>
                </div>
                <h3 className="text-base sm:text-lg font-black text-slate-900 dark:text-white mb-3">
                  {currentGkCard.front}
                </h3>
                {gkIsFlipped && (
                  <div className="space-y-2.5 pt-3 border-t border-slate-100 dark:border-slate-800 animate-in fade-in duration-150">
                    <p className="text-xs sm:text-sm text-slate-700 dark:text-slate-200 leading-relaxed font-semibold">
                      {currentGkCard.back}
                    </p>
                    {currentGkCard.hack && (
                      <div className="flex items-start gap-1.5 p-2 rounded-lg bg-emerald-500/15 text-emerald-900 dark:text-emerald-200 text-xs border border-emerald-500/30">
                        <Zap className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                        <span><strong>স্পিড হ্যাক:</strong> {currentGkCard.hack}</span>
                      </div>
                    )}
                    {currentGkCard.trap && (
                      <div className="flex items-start gap-1.5 p-2 rounded-lg bg-amber-500/15 text-amber-900 dark:text-rose-200 text-xs border border-amber-500/30">
                        <ShieldAlert className="w-3.5 h-3.5 text-amber-600 shrink-0 mt-0.5" />
                        <span><strong>ট্র্যাপ অ্যালার্ট:</strong> {currentGkCard.trap}</span>
                      </div>
                    )}
                  </div>
                )}
              </div>
              <div className="text-[11px] text-slate-400 text-center pt-3 border-t border-slate-100 dark:border-slate-800">
                {gkIsFlipped ? 'পরবর্তী কার্ডে যেতে ডান তীর বা পরবর্তী বাটনে চাপ দিন' : 'উত্তর ও ট্র্যাপ ডিফেন্স দেখতে ক্লিক করুন'}
              </div>
            </div>

            <div className="flex items-center justify-between gap-2 pt-2">
              <button
                onClick={prevGkCard}
                className="px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-700 dark:text-slate-300 cursor-pointer"
              >
                পূর্ববর্তী
              </button>
              <button
                onClick={nextGkCard}
                className="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold cursor-pointer shadow-xs"
              >
                পরবর্তী কার্ড
              </button>
            </div>
          </div>
        ) : (
          /* GK Grid View */
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
            {gkCardsList.map((card) => (
              <div
                key={card.id}
                className="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-[10px] font-bold text-emerald-600 dark:text-emerald-400">{card.month_bn} ২০২৬</span>
                    <button
                      onClick={() => toggleGkMastered(card.id)}
                      className={`p-1 rounded-md ${masteredGkIds.has(card.id) ? 'text-emerald-600' : 'text-slate-300'}`}
                    >
                      <CheckCircle className="w-3.5 h-3.5" />
                    </button>
                  </div>
                  <h4 className="text-xs font-bold text-slate-900 dark:text-white mb-2">{card.front}</h4>
                  <p className="text-[11px] text-slate-600 dark:text-slate-300 mb-2">{card.back}</p>
                </div>
                {card.hack && (
                  <div className="text-[10px] p-1.5 rounded bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 font-medium">
                    ⚡ {card.hack}
                  </div>
                )}
              </div>
            ))}
          </div>
        )
      ) : (
        /* =========================================================================
           ENGLISH PREDICTOR DECK DISPLAY
           ========================================================================= */
        engList.length === 0 ? (
          <div className="p-12 text-center rounded-3xl bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80">
            <HelpCircle className="w-10 h-10 text-slate-400 mx-auto mb-2" />
            <h3 className="text-base font-bold text-slate-800 dark:text-slate-200">কোনো ইংলিশ প্রশ্ন পাওয়া যায়নি</h3>
          </div>
        ) : viewMode === 'card' && currentEngCard ? (
          <div className="space-y-4">
            <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-1 font-medium">
              <span className="px-2 py-0.5 rounded-lg bg-purple-500/10 text-purple-700 dark:text-purple-300 font-mono font-bold text-[11px]">
                প্রশ্ন {engCurrentIndex + 1} / {engList.length} • {currentEngCard.cluster_name_bn || currentEngCard.cluster_name}
              </span>
              <span className="text-[11px] font-mono text-purple-600 font-bold">
                {engMasteredCount} আয়ত্ত
              </span>
            </div>

            <div className="p-5 sm:p-6 rounded-3xl bg-white dark:bg-slate-900 border border-purple-500/30 shadow-md flex flex-col justify-between space-y-4">
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="px-2.5 py-0.5 rounded-md text-[10px] font-mono font-bold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                    🎯 {currentEngCard.exam_target} • {currentEngCard.star_ranking}
                  </span>
                  <button
                    onClick={(e) => toggleEngMastered(currentEngCard.id, e)}
                    className={`p-1.5 rounded-xl border transition-colors ${
                      isCurrentEngMastered 
                        ? 'bg-purple-600 text-white border-purple-600' 
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-400 border-slate-200 dark:border-slate-700'
                    }`}
                  >
                    <CheckCircle className="w-4 h-4" />
                  </button>
                </div>

                <div className="p-3.5 rounded-2xl bg-slate-50/80 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/80 text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-relaxed mb-3.5">
                  <MathText content={currentEngCard.q} />
                </div>

                {/* 4 Options Grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                  {(currentEngCard.options || currentEngCard.opts).map((opt, idx) => {
                    const letters = ['A', 'B', 'C', 'D'];
                    const isSelected = userSelectedOption === idx;
                    const isCorrect = idx === currentEngCard.ans;
                    const showFeedback = engIsFlipped || userSelectedOption !== null;

                    let optClass = 'bg-white dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 hover:border-purple-500';
                    if (showFeedback) {
                      if (isCorrect) {
                        optClass = 'bg-emerald-500/20 text-emerald-900 dark:text-emerald-200 border-emerald-500 font-bold';
                      } else if (isSelected) {
                        optClass = 'bg-rose-500/20 text-rose-900 dark:text-rose-200 border-rose-500 font-bold';
                      } else {
                        optClass = 'opacity-50 border-slate-200 dark:border-slate-800';
                      }
                    }

                    return (
                      <button
                        key={idx}
                        onClick={() => {
                          setUserSelectedOption(idx);
                          setEngIsFlipped(true);
                        }}
                        className={`p-3 rounded-xl border text-left text-xs sm:text-sm font-medium transition-all flex items-center gap-2.5 cursor-pointer ${optClass}`}
                      >
                        <span className="w-6 h-6 rounded-md bg-slate-100 dark:bg-slate-700 font-mono text-xs font-bold flex items-center justify-center shrink-0">
                          {letters[idx]}
                        </span>
                        <span>{opt}</span>
                      </button>
                    );
                  })}
                </div>

                {/* Flipped Content / Explanations */}
                {engIsFlipped && (
                  <div className="mt-4 space-y-2.5 pt-3 border-t border-slate-100 dark:border-slate-800 animate-in fade-in duration-150">
                    {/* Emerald Speed Hack */}
                    {currentEngCard.speed_hack && (
                      <div className="flex items-start gap-2 p-2.5 rounded-xl bg-emerald-500/15 text-emerald-900 dark:text-emerald-200 text-xs sm:text-sm border border-emerald-500/30">
                        <Zap className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                        <div>
                          <strong className="text-emerald-800 dark:text-emerald-300 mr-1 uppercase text-[11px]">⚡ স্পিড হ্যাক:</strong>
                          <MathText content={currentEngCard.speed_hack} />
                        </div>
                      </div>
                    )}

                    {/* Rose/Amber Trap Alert */}
                    {currentEngCard.trap_alert && (
                      <div className="flex items-start gap-2 p-2.5 rounded-xl bg-amber-500/15 text-amber-950 dark:text-rose-200 text-xs sm:text-sm border border-amber-500/30">
                        <ShieldAlert className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
                        <div>
                          <strong className="text-amber-900 dark:text-rose-300 mr-1 uppercase text-[11px]">⚠️ ট্র্যাপ অ্যালার্ট:</strong>
                          <MathText content={currentEngCard.trap_alert} />
                        </div>
                      </div>
                    )}

                    {/* Explanation */}
                    {currentEngCard.exp && (
                      <div className="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
                        <strong className="text-slate-900 dark:text-white mr-1">📖 ব্যাখ্যা ও নিয়ম:</strong>
                        <MathText content={currentEngCard.exp} />
                      </div>
                    )}
                  </div>
                )}
              </div>

              {/* Navigation Controls */}
              <div className="flex items-center justify-between gap-2 pt-2 border-t border-slate-100 dark:border-slate-800">
                <button
                  onClick={prevEngCard}
                  className="px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-700 dark:text-slate-300 cursor-pointer"
                >
                  পূর্ববর্তী প্রশ্ন
                </button>
                <button
                  onClick={() => setEngIsFlipped(!engIsFlipped)}
                  className="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-bold cursor-pointer"
                >
                  {engIsFlipped ? 'উত্তর লুকান' : 'ব্যাখ্যা দেখুন'}
                </button>
                <button
                  onClick={nextEngCard}
                  className="px-5 py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold cursor-pointer shadow-xs"
                >
                  পরবর্তী প্রশ্ন
                </button>
              </div>
            </div>
          </div>
        ) : (
          /* English Grid View */
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
            {engList.map((q) => (
              <div
                key={q.id}
                className="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-[10px] font-bold text-purple-600 dark:text-purple-400 font-mono">{q.exam_target}</span>
                    <button
                      onClick={() => toggleEngMastered(q.id)}
                      className={`p-1 rounded-md ${masteredEngIds.has(q.id) ? 'text-purple-600' : 'text-slate-300'}`}
                    >
                      <CheckCircle className="w-3.5 h-3.5" />
                    </button>
                  </div>
                  <h4 className="text-xs font-bold text-slate-900 dark:text-white mb-2 leading-snug">{q.q}</h4>
                  <div className="text-[11px] font-medium text-emerald-700 dark:text-emerald-400 mb-2">
                    ✓ সঠিক উত্তর: {q.options ? q.options[q.ans] : q.opts[q.ans]}
                  </div>
                </div>
                {q.speed_hack && (
                  <div className="text-[10px] p-1.5 rounded bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 font-medium">
                    ⚡ {q.speed_hack}
                  </div>
                )}
              </div>
            ))}
          </div>
        )
      )}

      {/* 6. BOTTOM CHEAT TIPS BANNER */}
      <div className="mt-8 p-4 rounded-3xl backdrop-blur-xl bg-gradient-to-r from-emerald-500/10 via-teal-500/10 to-purple-500/10 ring-1 ring-emerald-500/25 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-emerald-600 text-white flex items-center justify-center shrink-0 shadow-md">
            <Award className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-xs sm:text-sm font-black text-slate-900 dark:text-white">
              মেডিকেল ও ভার্সিটি ২৫-মার্কস নন-সায়েন্স বুস্টার স্ট্র্যাটেজি
            </h4>
            <p className="text-[11px] text-slate-600 dark:text-slate-400 mt-0.5">
              মেডিকেলে ইংলিশ ১৫ + জিকে ১০ = ২৫ নম্বর। প্রতিদিন ২০ মিনিট অ্যাক্টিভ রিকলে রিভিশন দিলে নিশ্চিত ফুল মার্কস নিশ্চিত হয়।
            </p>
          </div>
        </div>

        <button
          onClick={() => {
            if (deckType === 'gk') shuffleGkCards();
            else shuffleEngCards();
          }}
          className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shrink-0 active:scale-95 transition-all cursor-pointer shadow-xs flex items-center gap-1.5"
        >
          <Shuffle className="w-3.5 h-3.5" />
          <span>র‌্যান্ডম রিভিশন ড্রিল</span>
        </button>
      </div>

    </div>
  );
};

export const ActiveRecallView = React.memo(ActiveRecallViewComponent);
export default ActiveRecallView;
