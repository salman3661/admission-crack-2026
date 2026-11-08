import { ActiveRecallView } from './ActiveRecallView';
import React, { useState, useEffect, useMemo, useRef, useCallback } from 'react';
import { 
  RotateCw, 
  CheckCircle, 
  RotateCcw, 
  Shuffle, 
  Sparkles, 
  ChevronLeft, 
  ChevronRight,
  Flame, 
  ShieldAlert, 
  Zap, 
  Copy,
  Check
} from 'lucide-react';

import katex from 'katex';
import type { FlashcardItem, SubjectType, WeekFilterType, TrackType, AppMode } from '../types';
import { MathText, parseMarkdownTable } from './MathText';
import vaultItemsData from '../data/vault_items.json';

export interface FlashcardsViewProps {
  flashcards?: FlashcardItem[];
  selectedWeek?: WeekFilterType;
  onSelectWeek?: (week: WeekFilterType) => void;
  selectedSubject?: SubjectType;
  onSelectSubject?: (subject: SubjectType) => void;
  activeTrack?: TrackType;
  onSelectMode?: (mode: AppMode) => void;
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
  {
    id: 'recent_gk_monthly',
    title: '📅 Udvash Recent Monthly GK (Jan-Oct 2026)',
    icon: '📅',
    badge: '৮০ কার্ডস',
    color: 'from-teal-600 to-emerald-700',
    scope: 'উদ্ভাসের মান্থলি জিকে লেকচার ও পিডিএফ নোটস: ত্রয়োদশ নির্বাচন, পদ্মা ব্যারাজ, নোবেল ২০২৬ ও মেগা প্রজেক্টস',
  },
];

const CHAPTER_DISPLAY_NAMES: Record<string, string> = {
  'Vector': 'ভেক্টর (Vector)',
  'Dynamics': 'গতিবিদ্যা (Dynamics)',
  'Qualitative Analysis': 'গুণগত রসায়ন',
  'Matrix-Determinants': 'ম্যাট্রিক্স ও নির্ণায়ক',
  'Straight Lines': 'সরলরেখা (Straight Lines)',
  'Human Physiology (Circulation)': 'রক্ত ও সংবহন',
  'Human Physiology (Digestion)': 'পরিপাক ও শোষণ',
  'Work-Energy': 'কাজ, শক্তি ও ক্ষমতা',
  'Periodic Properties': 'পর্যায়বৃত্ত ধর্ম',
  'Chemical Changes (Equilibrium/pH)': 'রাসায়নিক পরিবর্তন (pH ও সাম্যাবস্থা)',
  'Cell & Structure': 'কোষ ও এর গঠন',
  'Circles': 'বৃত্ত (Circles)',
  'Trigonometry': 'ত্রিকোণমিতি (Trigonometry)',
  'Synonyms & Antonyms': 'Synonyms & Antonyms',
  'Appropriate Prepositions': 'Appropriate Prepositions',
  '1971 Liberation War & Bir Sreshtho Matrix': '১৯৭১ মুক্তিযুদ্ধ ও বীরশ্রেষ্ঠ ম্যাট্রিক্স',
  'Gravitation': 'মহাকর্ষ ও অভিকর্ষ',
  'Environmental Chem': 'পরিবেশ রসায়ন',
  'Complex Numbers': 'জটিল সংখ্যা',
  'Conics': 'কণিক (উপবৃত্ত, পরাবৃত্ত, অধিবৃত্ত)',
  'Plant Physiology': 'উদ্ভিদ শারীরতত্ত্ব',
  'Structural Properties of Matter': 'পদার্থের গাঠনিক ধর্ম',
  'Ideal Gas & Kinetic Theory': 'আদর্শ গ্যাস ও গতিতত্ত্ব',
  'Periodic Properties & Chemical Bonding': 'পর্যায়বৃত্ত ধর্ম ও বন্ধন',
  'Permutations & Combinations': 'বিন্যাস ও সমাবেশ',
  'Measures of Dispersion & Probability': 'সম্ভাবনা ও বিস্তার পরিমাপ',
  'Animal Diversity & Classification': 'প্রাণীর বিভিন্নতা ও শ্রেণিবিন্যাস',
  'Genetics & Evolution': 'জিনতত্ত্ব ও বিবর্তন',
  'Periodic Motion & SHM': 'পর্যায়বৃত্ত গতি ও সরল ছন্দিত স্পন্দন',
  'Waves & Sound': 'তরঙ্গ ও শব্দ',
  'Electrochemistry': 'তড়িৎ রসায়ন',
  'Polynomials & Equations': 'বহুপদী ও বহুপদী সমীকরণ',
  'Binomial Expansion': 'দ্বিপদী বিস্তৃতি',
  'Heat & Thermodynamics': 'তাপ ও তাপগতিবিদ্যা',
  'Calculus': 'ক্যালকুলাস',
  'Human Physiology (Excretion)': 'রেচন ও মানব শারীরতত্ত্ব',
  'স্থির তড়িৎ': 'স্থির তড়িৎ (Static Electricity)',
  'আধুনিক পদার্থবিজ্ঞান': 'আধুনিক পদার্থবিজ্ঞান (Modern Physics)',
  'জৈব রসায়ন': 'জৈব রসায়ন (Organic Chemistry)',
  'অন্তরীকরণ': 'অন্তরীকরণ (Calculus)',
  'নগ্নবীজী ও আবৃতবীজী উদ্ভিদ': 'নগ্নবীজী ও আবৃতবীজী উদ্ভিদ (Botany)',
  'সমন্বয় ও নিয়ন্ত্রণ': 'সমন্বয় ও নিয়ন্ত্রণ',
  'প্রাণীর আচরণ': 'প্রাণীর আচরণ (Animal Behavior)',
};

const toBengaliNumber = (num: number): string => {
  const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
  return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)]);
};

function weekFilterToActiveNumber(filter?: WeekFilterType): 'all' | number {
  if (!filter || filter === 'all') return 'all';
  const match = filter.match(/week_0?(\d+)/);
  if (match) {
    const num = parseInt(match[1], 10);
    if (num >= 1 && num <= 7) return num;
  }
  return 'all';
}

function activeNumberToWeekFilter(num: 'all' | number): WeekFilterType {
  if (num === 'all') return 'all';
  return `week_${String(num).padStart(2, '0')}` as WeekFilterType;
}

interface UnifiedFlashcard {
  id: string;
  source: 'vault' | 'macro';
  deck_id?: string;
  deck_title?: string;
  week: number;
  week_id: string;
  subject: string;
  chapter: string;
  chapter_display: string;
  title: string;
  type: string;
  frontPrompt: string;
  back: string;
  formula?: string;
  concept?: string;
  hack?: string;
  trap?: string;
  headers?: string[];
  rows?: string[][];
  tags?: string[];
}

/** High-contrast KaTeX formula box with built-in copy button */
const FlashcardFormulaBox: React.FC<{ formula: string }> = ({ formula }) => {
  const [isCopied, setIsCopied] = useState(false);

  const handleCopy = (e: React.MouseEvent) => {
    e.stopPropagation();
    try {
      navigator.clipboard.writeText(formula);
      setIsCopied(true);
      setTimeout(() => setIsCopied(false), 2000);
    } catch {
      // ignore
    }
  };

  const parsedTable = useMemo(() => parseMarkdownTable(formula), [formula]);
  if (parsedTable) {
    return (
      <div className="w-full overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 shadow-xs my-2">
        <table className="w-full text-left border-collapse min-w-[280px]">
          <thead>
            <tr className="bg-slate-100 dark:bg-slate-800 text-xs font-semibold text-slate-700 dark:text-slate-200 border-b border-slate-200 dark:border-slate-700">
              {parsedTable.headers.map((h, i) => (
                <th key={i} className="py-2 px-3 text-xs font-semibold text-slate-700 dark:text-slate-200">
                  <MathText content={h} />
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {parsedTable.rows.map((row, rIdx) => (
              <tr key={rIdx} className="even:bg-slate-50/50 dark:even:bg-slate-800/30 border-b border-slate-100 dark:border-slate-800/60">
                {row.map((cell, cIdx) => (
                  <td key={cIdx} className="py-1.5 px-3 text-xs text-slate-800 dark:text-slate-100">
                    <MathText content={cell} />
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }

  const renderedHtml = useMemo(() => {
    let clean = formula.trim();
    if (clean.startsWith('$$') && clean.endsWith('$$')) {
      clean = clean.slice(2, -2).trim();
    } else if (clean.startsWith('$') && clean.endsWith('$')) {
      clean = clean.slice(1, -1).trim();
    }

    clean = clean.replace(/(?<!\\)\btimes\b/g, '\\times');
    clean = clean.replace(/(?<!\\)\bimplies\b/g, '\\implies');
    clean = clean.replace(/(?<!\\)\bapprox\b/g, '\\approx');
    clean = clean.replace(/\\textm\b|(?<!\\)\btextm\b/g, '\\text{m}');
    clean = clean.replace(/_\{([^\x00-\x7F]+)\}/g, '_{\\text{$1}}');
    clean = clean.replace(/\^\{([^\x00-\x7F]+)\}/g, '^{\\text{$1}}');

    try {
      return katex.renderToString(clean, {
        displayMode: true,
        throwOnError: false,
        strict: 'ignore',
      });
    } catch {
      return `<div class="font-mono text-rose-400 text-xs">${clean}</div>`;
    }
  }, [formula]);

  return (
    <div className="relative group bg-slate-900 dark:bg-slate-950 border border-slate-800 dark:border-slate-800/80 rounded-2xl p-3 sm:p-4 my-2.5 overflow-x-auto no-scrollbar shadow-inner text-center">
      <div 
        className="text-white text-sm sm:text-base inline-block max-w-full overflow-x-auto no-scrollbar py-1 leading-relaxed"
        dangerouslySetInnerHTML={{ __html: renderedHtml }}
      />
      <button
        type="button"
        onClick={handleCopy}
        className="absolute top-2 right-2 p-1.5 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-300 hover:text-white transition-all opacity-80 group-hover:opacity-100 flex items-center gap-1 text-[11px] font-mono cursor-pointer shadow-xs active:scale-95"
        title="সূত্র কপি করুন"
      >
        {isCopied ? (
          <>
            <Check className="w-3.5 h-3.5 text-emerald-400" />
            <span className="text-emerald-400 font-bold hidden sm:inline">কপি হয়েছে</span>
          </>
        ) : (
          <>
            <Copy className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">কপি</span>
          </>
        )}
      </button>
    </div>
  );
};

export const FlashcardsView: React.FC<FlashcardsViewProps> = ({
  flashcards = [],
  selectedWeek: propWeek,
  onSelectWeek,
  selectedSubject: propSubject,
  onSelectSubject,
  onSelectMode,
}) => {
  // Top-level View Mode: 'chapter' (অধ্যায়ভিত্তিক ডেক) vs 'macro' (⚡ অল-ইন-ওয়ান স্পেশাল ক্যাপসুল)
  const [activeTab, setActiveTab] = useState<'chapter' | 'macro'>('chapter');

  // Dynamic Filters for Chapter Deck Engine
  const [activeWeek, setActiveWeek] = useState<'all' | number>(() => {
    const parsed = weekFilterToActiveNumber(propWeek);
    return parsed !== 'all' ? parsed : 1; // Default to Week 1 for focused slide study
  });

  const [activeSubject, setActiveSubject] = useState<SubjectType>(() => {
    return propSubject && propSubject !== 'All' ? propSubject : 'All';
  });

  const [selectedChapter, setSelectedChapter] = useState<string>('all');
  const [selectedCardType, setSelectedCardType] = useState<string>('all');

  // Macro Deck Selection
  const [selectedMacroDeckId, setSelectedMacroDeckId] = useState<string>('du_speed');

  // Carousel & Leitner Mastery State
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

  // Touch Swipe Gesture State
  const touchStartX = useRef<number | null>(null);
  const touchStartY = useRef<number | null>(null);

  // Sync with prop changes from parent
  useEffect(() => {
    if (propWeek !== undefined) {
      const parsed = weekFilterToActiveNumber(propWeek);
      setActiveWeek(parsed !== 'all' ? parsed : 'all');
      setSelectedChapter('all');
    }
  }, [propWeek]);

  useEffect(() => {
    if (propSubject !== undefined) {
      setActiveSubject(propSubject);
      setSelectedChapter('all');
    }
  }, [propSubject]);

  // Persist mastered IDs
  useEffect(() => {
    try {
      localStorage.setItem('admission_flashcards_mastered', JSON.stringify(Array.from(masteredIds)));
    } catch (e) {
      console.error('Failed to save mastered flashcards', e);
    }
  }, [masteredIds]);

  // Build unified cards from vault_items.json
  const vaultCards: UnifiedFlashcard[] = useMemo(() => {
    const rawList = Array.isArray(vaultItemsData) ? vaultItemsData : [];
    return rawList.map((entry: any) => {
      const weekNum = typeof entry.week === 'number' ? entry.week : parseInt(entry.week, 10) || 1;
      const chapterName = entry.chapter || 'জেনারেল';
      const type = entry.type || 'core_formula';

      let prompt = '💡 এই টপিকের মূল সূত্র, প্রয়োগ ও সম্পর্ক মনে করার চেষ্টা করুন।';
      if (type === 'core_formula') {
        prompt = '💡 এই সূত্রের গাণিতিক সমীকরণ, রাশিগুলোর তাৎপর্য ও বিশেষ শর্ত মনে করার চেষ্টা করুন।';
      } else if (type === 'shortcut') {
        prompt = '⚡ ভর্তি পরীক্ষায় সময় বাঁচানোর নো-ক্যালকুলেটর শর্টকাট টেকনিক ও হ্যাক কী? মনে করার চেষ্টা করুন।';
      } else if (type === 'trap') {
        prompt = '⚠️ পরীক্ষার হলে এই সূত্রে শিক্ষার্থীরা সাধারণত কী ভুল করে এবং নেগেটিভ ট্র্যাপ কোথায়? মনে করার চেষ্টা করুন।';
      } else if (type === 'table') {
        prompt = '📊 এই তুলনামূলক ছকের গুরুত্বপূর্ণ মান, বৈশিষ্ট্য ও ব্যতিক্রম মনে করার চেষ্টা করুন।';
      }

      return {
        id: entry.id || `v_${Math.random()}`,
        source: 'vault' as const,
        week: weekNum,
        week_id: `week_${String(weekNum).padStart(2, '0')}`,
        subject: entry.subject || 'Physics',
        chapter: chapterName,
        chapter_display: CHAPTER_DISPLAY_NAMES[chapterName] || chapterName,
        title: entry.title || 'এডমিশন কার্ড',
        type,
        frontPrompt: prompt,
        back: entry.concept || entry.formula || '',
        formula: entry.formula,
        concept: entry.concept,
        hack: entry.hack,
        trap: entry.trap,
        headers: entry.headers,
        rows: entry.rows,
        tags: entry.tags,
      };
    });
  }, []);

  // Build unified cards from curated macro flashcards.json
  const macroCards: UnifiedFlashcard[] = useMemo(() => {
    return flashcards.map((fc) => {
      let weekNum = 1;
      if (fc.week_id) {
        const match = fc.week_id.match(/week_0?(\d+)/);
        if (match) weekNum = parseInt(match[1], 10);
      }

      return {
        id: fc.id,
        source: 'macro' as const,
        deck_id: fc.deck_id,
        deck_title: fc.deck_title,
        week: weekNum,
        week_id: fc.week_id || 'week_01',
        subject: fc.subject || 'All',
        chapter: fc.topic || 'স্পেশাল ডেক',
        chapter_display: fc.topic || 'স্পেশাল ডেক',
        title: fc.topic || 'ক্যাপসুল কার্ড',
        type: 'macro',
        frontPrompt: fc.front || 'এই প্রশ্নের উত্তর মনে করার চেষ্টা করুন:',
        back: fc.back || fc.concept || '',
        formula: fc.back?.includes('$') ? fc.back : undefined,
        concept: fc.concept || fc.back,
        hack: fc.hack,
        trap: fc.trap,
      };
    });
  }, [flashcards]);

  // Available subjects for the active week in Chapter mode
  const availableSubjectsForWeek = useMemo(() => {
    const weekCards = activeWeek === 'all' 
      ? vaultCards 
      : vaultCards.filter((c) => c.week === activeWeek);

    const counts: Record<string, number> = { All: weekCards.length };
    weekCards.forEach((c) => {
      counts[c.subject] = (counts[c.subject] || 0) + 1;
    });

    return counts;
  }, [vaultCards, activeWeek]);

  // Available chapters dynamically derived based on active week and active subject
  const availableChapters = useMemo(() => {
    let scoped = vaultCards;
    if (activeWeek !== 'all') {
      scoped = scoped.filter((c) => c.week === activeWeek);
    }
    if (activeSubject !== 'All') {
      scoped = scoped.filter((c) => c.subject === activeSubject);
    }

    const chapterMap = new Map<string, { display: string; count: number }>();
    scoped.forEach((c) => {
      if (c.chapter) {
        const existing = chapterMap.get(c.chapter);
        if (existing) {
          existing.count += 1;
        } else {
          chapterMap.set(c.chapter, {
            display: c.chapter_display,
            count: 1,
          });
        }
      }
    });

    return Array.from(chapterMap.entries())
      .map(([name, meta]) => ({ name, display: meta.display, count: meta.count }))
      .sort((a, b) => b.count - a.count);
  }, [vaultCards, activeWeek, activeSubject]);

  // Synchronize selectedChapter if it's no longer present
  useEffect(() => {
    if (selectedChapter !== 'all') {
      const exists = availableChapters.some((ch) => ch.name === selectedChapter);
      if (!exists) {
        setSelectedChapter('all');
      }
    }
  }, [availableChapters, selectedChapter]);

  // Compute active cards list based on current mode and filters
  const activeDeckCards = useMemo(() => {
    if (activeTab === 'macro') {
      if (selectedMacroDeckId === 'all') {
        return macroCards;
      }
      return macroCards.filter((c) => c.deck_id === selectedMacroDeckId);
    }

    // Chapter mode: Filter from vaultCards
    let filtered = vaultCards;
    if (activeWeek !== 'all') {
      filtered = filtered.filter((c) => c.week === activeWeek);
    }
    if (activeSubject !== 'All') {
      filtered = filtered.filter((c) => c.subject === activeSubject);
    }
    if (selectedChapter !== 'all') {
      filtered = filtered.filter((c) => c.chapter === selectedChapter);
    }
    if (selectedCardType !== 'all') {
      filtered = filtered.filter((c) => c.type === selectedCardType);
    }

    return filtered;
  }, [activeTab, selectedMacroDeckId, macroCards, vaultCards, activeWeek, activeSubject, selectedChapter, selectedCardType]);

  const [cardsList, setCardsList] = useState<UnifiedFlashcard[]>(activeDeckCards);

  // Sync cards list when activeDeckCards updates
  useEffect(() => {
    setCardsList(activeDeckCards);
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [activeDeckCards]);

  // Keyboard navigation & shortcuts
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes((e.target as HTMLElement).tagName)) return;

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

  const nextCard = useCallback(() => {
    setIsFlipped(false);
    setTimeout(() => {
      setCurrentIndex((prev) => (prev + 1 < cardsList.length ? prev + 1 : 0));
    }, 100);
  }, [cardsList.length]);

  const prevCard = useCallback(() => {
    setIsFlipped(false);
    setTimeout(() => {
      setCurrentIndex((prev) => (prev - 1 >= 0 ? prev - 1 : cardsList.length - 1));
    }, 100);
  }, [cardsList.length]);

  const markMastered = useCallback(() => {
    if (!cardsList[currentIndex]) return;
    setMasteredIds((prev) => new Set(prev).add(cardsList[currentIndex].id));
    nextCard();
  }, [cardsList, currentIndex, nextCard]);

  const markReview = useCallback(() => {
    if (!cardsList[currentIndex]) return;
    setMasteredIds((prev) => {
      const next = new Set(prev);
      next.delete(cardsList[currentIndex].id);
      return next;
    });
    nextCard();
  }, [cardsList, currentIndex, nextCard]);

  const shuffleCards = () => {
    setIsFlipped(false);
    setCardsList((prev) => [...prev].sort(() => Math.random() - 0.5));
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

  // Touch Swipe Handlers (Swipe left -> Next, Swipe right -> Prev)
  const handleTouchStart = (e: React.TouchEvent) => {
    touchStartX.current = e.touches[0].clientX;
    touchStartY.current = e.touches[0].clientY;
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    if (touchStartX.current === null || touchStartY.current === null) return;
    const deltaX = e.changedTouches[0].clientX - touchStartX.current;
    const deltaY = e.changedTouches[0].clientY - touchStartY.current;

    // Minimum swipe threshold of 45px and predominantly horizontal
    if (Math.abs(deltaX) > 45 && Math.abs(deltaX) > Math.abs(deltaY) * 1.5) {
      if (deltaX < 0) {
        nextCard();
      } else {
        prevCard();
      }
    }
    touchStartX.current = null;
    touchStartY.current = null;
  };

  // Deck progress stats
  const masteredCount = cardsList.filter((c) => masteredIds.has(c.id)).length;
  const progressPercent = cardsList.length > 0 
    ? Math.round((masteredCount / cardsList.length) * 100) 
    : 0;

  const currentCard: UnifiedFlashcard | undefined = cardsList[currentIndex] || cardsList[0];
  const isCurrentMastered = currentCard?.id ? masteredIds.has(currentCard.id) : false;

  // Compute progress for each macro deck
  const macroDeckProgressMap = useMemo(() => {
    const map: Record<string, { mastered: number; total: number }> = {};
    CURATED_DECKS.forEach((deck) => {
      if (deck.id === 'recent_gk_monthly') {
        try {
          const savedGK = localStorage.getItem('admission_monthly_gk_mastered');
          const count = savedGK ? JSON.parse(savedGK).length : 0;
          map[deck.id] = { mastered: count, total: 80 };
        } catch {
          map[deck.id] = { mastered: 0, total: 80 };
        }
        return;
      }
      const deckCards = macroCards.filter((c) => c.deck_id === deck.id);
      const m = deckCards.filter((c) => masteredIds.has(c.id)).length;
      map[deck.id] = { mastered: m, total: deckCards.length };
    });
    return map;
  }, [macroCards, masteredIds]);

  const handleWeekSelect = (w: 'all' | number) => {
    setActiveWeek(w);
    setSelectedChapter('all');
    if (onSelectWeek) {
      onSelectWeek(activeNumberToWeekFilter(w));
    }
  };

  const handleSubjectSelect = (sub: SubjectType) => {
    setActiveSubject(sub);
    setSelectedChapter('all');
    if (onSelectSubject) {
      onSelectSubject(sub);
    }
  };

  // Card type label badge
  const getCardTypeBadge = (type?: string) => {
    switch (type) {
      case 'core_formula':
        return { text: '💡 কোর ফর্মুলা', color: 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border-emerald-500/20' };
      case 'shortcut':
        return { text: '⚡ ৫-সেকেন্ড স্পিড হ্যাক', color: 'bg-amber-500/10 text-amber-700 dark:text-amber-300 border-amber-500/20' };
      case 'trap':
        return { text: '⚠️ নেগেটিভ ট্র্যাপ অ্যালার্ট', color: 'bg-rose-500/10 text-rose-700 dark:text-rose-300 border-rose-500/20' };
      case 'table':
        return { text: '📊 তুলনামূলক ছক', color: 'bg-blue-500/10 text-blue-700 dark:text-blue-300 border-blue-500/20' };
      case 'macro':
      default:
        return { text: '🎯 স্পেশাল ক্যাপসুল', color: 'bg-purple-500/10 text-purple-700 dark:text-purple-300 border-purple-500/20' };
    }
  };

  const currentTypeBadge = getCardTypeBadge(currentCard?.type);

  return (
    <div className="max-w-4xl mx-auto py-3 px-3 sm:px-5 flex flex-col items-center">
      
      {/* =========================================================================
          1. HEADER & DUAL MODE SEGMENTED TOGGLE
          [ 📖 অধ্যায়ভিত্তিক ডেক (Chapter Recall) ] vs [ ⚡ অল-ইন-ওয়ান স্পেশাল ক্যাপসুল ]
         ========================================================================= */}
      <div className="w-full mb-3">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 pb-2 border-b border-slate-200/80 dark:border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <span className="w-7 h-7 rounded-lg bg-gradient-to-tr from-[#056839] to-emerald-500 text-white flex items-center justify-center font-bold text-sm shadow-sm">
                🧠
              </span>
              <h1 className="text-base sm:text-lg font-black text-slate-900 dark:text-white">
                অ্যাক্টিভ রিকল স্লাইড ডেক (Active Recall Flashcards)
              </h1>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-mono font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20">
                {cardsList.length}টি কার্ড
              </span>
            </div>
          </div>

          {/* Mode Switcher Tabs */}
          <div className="flex items-center bg-slate-100 dark:bg-slate-800/80 p-1 rounded-2xl ring-1 ring-slate-200/80 dark:ring-slate-700/80 self-start sm:self-auto">
            <button
              onClick={() => setActiveTab('chapter')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeTab === 'chapter'
                  ? 'bg-white dark:bg-slate-900 text-[#056839] dark:text-emerald-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              📖 অধ্যায়ভিত্তিক ডেক
            </button>
            <button
              onClick={() => setActiveTab('macro')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeTab === 'macro'
                  ? 'bg-white dark:bg-slate-900 text-amber-600 dark:text-amber-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              ⚡ অল-ইন-ওয়ান স্পেশাল ক্যাপসুল
            </button>
          </div>
        </div>
      </div>

      {/* =========================================================================
          2. DYNAMIC HIERARCHY & FILTERING (UPPER FOLD)
         ========================================================================= */}
      {activeTab === 'chapter' ? (
        <div className="w-full bg-white dark:bg-slate-900/90 rounded-2xl p-3 sm:p-4 border border-slate-200/80 dark:border-slate-800 shadow-xs mb-3 space-y-2.5">
          
          {/* Level 1: Week Chips (Week 01 to Week 07 + All) */}
          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-1">
            <span className="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider shrink-0 mr-1 flex items-center gap-1">
              <span>📅</span> সপ্তাহ:
            </span>
            {[
              { id: 1, label: 'Week 01' },
              { id: 2, label: 'Week 02' },
              { id: 3, label: 'Week 03' },
              { id: 4, label: 'Week 04' },
              { id: 5, label: 'Week 05' },
              { id: 6, label: 'Week 06' },
              { id: 7, label: 'Week 07' },
              { id: 'all' as const, label: 'সব সপ্তাহ' },
            ].map((wk) => {
              const isActive = activeWeek === wk.id;
              return (
                <button
                  key={String(wk.id)}
                  onClick={() => handleWeekSelect(wk.id)}
                  className={`px-3 py-1 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer active:scale-95 ${
                    isActive
                      ? 'bg-[#056839] text-white shadow-xs ring-2 ring-[#056839]/30'
                      : 'bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                  }`}
                >
                  {wk.label}
                </button>
              );
            })}
          </div>

          {/* Level 2: Subject Pills */}
          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-1 pt-1 border-t border-slate-100 dark:border-slate-800/60">
            <span className="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider shrink-0 mr-1 flex items-center gap-1">
              <span>📚</span> বিষয়:
            </span>
            {[
              { id: 'All' as const, label: 'সব বিষয়', icon: '🌐' },
              { id: 'Physics' as const, label: 'পদার্থবিজ্ঞান', icon: '⚡' },
              { id: 'Chemistry' as const, label: 'রসায়ন', icon: '🧪' },
              { id: 'Higher Math' as const, label: 'উচ্চতর গণিত', icon: '📐' },
              { id: 'Biology' as const, label: 'জীববিজ্ঞান', icon: '🧬' },
              { id: 'English' as const, label: 'English', icon: '📖' },
              { id: 'GK' as const, label: 'সাধারণ জ্ঞান', icon: '🇧🇩' },
            ].map((sub) => {
              const count = availableSubjectsForWeek[sub.id] || 0;
              if (sub.id !== 'All' && count === 0) return null; // hide subjects with 0 cards for the week
              const isActive = activeSubject === sub.id;

              return (
                <button
                  key={sub.id}
                  onClick={() => handleSubjectSelect(sub.id)}
                  className={`px-3 py-1 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer flex items-center gap-1.5 active:scale-95 ${
                    isActive
                      ? 'bg-slate-900 text-white dark:bg-white dark:text-slate-900 shadow-xs'
                      : 'bg-slate-100 dark:bg-slate-800/80 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                  }`}
                >
                  <span>{sub.icon}</span>
                  <span>{sub.label}</span>
                  <span className={`text-[10px] px-1.5 py-0.2 rounded-md font-mono ${
                    isActive ? 'bg-white/20 text-white dark:bg-slate-900/20 dark:text-slate-900' : 'bg-slate-200/80 dark:bg-slate-700 text-slate-600 dark:text-slate-400'
                  }`}>
                    {count}
                  </span>
                </button>
              );
            })}
          </div>

          {/* Level 3: Dynamic Chapter Chips & Card Type Filters */}
          {availableChapters.length > 0 && (
            <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pt-1 border-t border-slate-100 dark:border-slate-800/60">
              <span className="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider shrink-0 mr-1 flex items-center gap-1">
                <span>📑</span> অধ্যায়:
              </span>
              <button
                onClick={() => setSelectedChapter('all')}
                className={`px-2.5 py-0.8 rounded-lg text-xs font-bold whitespace-nowrap transition-all cursor-pointer ${
                  selectedChapter === 'all'
                    ? 'bg-emerald-600 text-white shadow-xs'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-200'
                }`}
              >
                সকল অধ্যায় ({availableChapters.reduce((acc, c) => acc + c.count, 0)})
              </button>
              {availableChapters.map((ch) => {
                const isActive = selectedChapter === ch.name;
                return (
                  <button
                    key={ch.name}
                    onClick={() => setSelectedChapter(ch.name)}
                    className={`px-2.5 py-0.8 rounded-lg text-xs font-semibold whitespace-nowrap transition-all cursor-pointer flex items-center gap-1 ${
                      isActive
                        ? 'bg-emerald-600 text-white font-bold shadow-xs'
                        : 'bg-slate-100 dark:bg-slate-800/80 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                    }`}
                  >
                    <span>{ch.display}</span>
                    <span className="font-mono text-[10px] opacity-80">({ch.count})</span>
                  </button>
                );
              })}
            </div>
          )}

          {/* Level 4: Card Type Filter Chips */}
          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pt-1 border-t border-slate-100 dark:border-slate-800/60">
            <span className="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider shrink-0 mr-1 flex items-center gap-1">
              <span>🎯</span> ধরন:
            </span>
            {[
              { id: 'all', label: 'সব ধরন' },
              { id: 'core_formula', label: '💡 কোর ফর্মুলা' },
              { id: 'shortcut', label: '⚡ স্পিড হ্যাক' },
              { id: 'trap', label: '⚠️ ট্র্যাপ অ্যালার্ট' },
            ].map((typeItem) => {
              const isActive = selectedCardType === typeItem.id;
              return (
                <button
                  key={typeItem.id}
                  onClick={() => setSelectedCardType(typeItem.id)}
                  className={`px-2.5 py-0.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all cursor-pointer ${
                    isActive
                      ? 'bg-slate-800 text-white dark:bg-slate-200 dark:text-slate-900 font-bold shadow-xs'
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-700'
                  }`}
                >
                  {typeItem.label}
                </button>
              );
            })}
          </div>

        </div>

      ) : (
        /* Curated Macro Decks Bar */
        <div className="w-full bg-white dark:bg-slate-900/90 rounded-2xl p-3 border border-slate-200/80 dark:border-slate-800 shadow-xs mb-3">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2">
            {CURATED_DECKS.map((deck) => {
              const isActive = selectedMacroDeckId === deck.id;
              const progress = macroDeckProgressMap[deck.id] || { mastered: 0, total: 0 };
              const pct = progress.total > 0 ? Math.round((progress.mastered / progress.total) * 100) : 0;

              return (
                <button
                  key={deck.id}
                  onClick={() => setSelectedMacroDeckId(deck.id)}
                  className={`p-2.5 rounded-xl text-left transition-all border relative cursor-pointer ${
                    isActive
                      ? 'bg-emerald-50/50 dark:bg-emerald-950/20 border-[#056839] shadow-xs ring-2 ring-[#056839]/20'
                      : 'bg-slate-50/60 dark:bg-slate-800/40 border-slate-200/80 dark:border-slate-800 hover:bg-white dark:hover:bg-slate-800'
                  }`}
                >
                  <div className="flex items-center justify-between gap-1 mb-1">
                    <span className="text-base">{deck.icon}</span>
                    <span className="text-[10px] font-mono font-bold text-slate-500">
                      {progress.mastered}/{progress.total}
                    </span>
                  </div>
                  <div className="text-xs font-bold text-slate-900 dark:text-white line-clamp-1">
                    {deck.title}
                  </div>
                  {/* Micro progress bar */}
                  <div className="w-full bg-slate-200 dark:bg-slate-700 h-1 rounded-full overflow-hidden mt-1.5">
                    <div 
                      className="bg-gradient-to-r from-emerald-500 to-teal-500 h-full transition-all"
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                </button>
              );
            })}
          </div>

          <div className="mt-2 flex justify-end">
            <button
              onClick={() => setSelectedMacroDeckId('all')}
              className={`text-xs font-bold px-3 py-1 rounded-lg transition-all cursor-pointer ${
                selectedMacroDeckId === 'all'
                  ? 'bg-slate-800 text-white dark:bg-slate-200 dark:text-slate-900'
                  : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'
              }`}
            >
              🌐 সব স্পেশাল ডেক একসাথে ({macroCards.length} কার্ডস)
            </button>
          </div>
        </div>
      )}

      {activeTab === 'macro' && selectedMacroDeckId === 'recent_gk_monthly' ? (
        <div className="w-full">
          <ActiveRecallView onSelectMode={onSelectMode} />
        </div>
      ) : (
      <>
      {/* =========================================================================
          3. COMPACT STATS & UTILITY STRIP (UPPER FOLD)
         ========================================================================= */}
      <div className="w-full bg-white dark:bg-slate-900 rounded-2xl p-2.5 sm:p-3 border border-slate-200/80 dark:border-slate-800 shadow-xs mb-2 flex items-center justify-between gap-2 flex-wrap">
        {/* Left: Card Counter Badge */}
        <div className="flex items-center gap-2">
          <span className="px-3 py-1 rounded-xl bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-mono font-black text-xs sm:text-sm shadow-xs flex items-center gap-1.5">
            কার্ড: {toBengaliNumber(currentIndex + 1)} / {toBengaliNumber(cardsList.length || 1)}
          </span>
          <span className="text-xs font-semibold text-slate-500 dark:text-slate-400 hidden sm:inline truncate max-w-[200px]">
            {currentCard?.chapter_display || currentCard?.chapter}
          </span>
        </div>

        {/* Center: Micro Mastered Progress */}
        <div className="flex items-center gap-2 flex-1 max-w-[220px]">
          <Flame className="w-4 h-4 text-amber-500 shrink-0" />
          <div className="flex-1">
            <div className="flex items-center justify-between text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-0.5">
              <span>{toBengaliNumber(masteredCount)}/{toBengaliNumber(cardsList.length)} আয়ত্ত</span>
              <span className="font-mono text-[#056839] dark:text-emerald-400">{toBengaliNumber(progressPercent)}%</span>
            </div>
            <div className="w-full bg-slate-100 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden">
              <div 
                className="bg-gradient-to-r from-emerald-500 to-teal-500 h-full transition-all duration-300 rounded-full"
                style={{ width: `${progressPercent}%` }}
              />
            </div>
          </div>
        </div>

        {/* Right: Actions */}
        <div className="flex items-center gap-1.5">
          <button
            onClick={shuffleCards}
            className="flex items-center gap-1 px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 text-xs font-bold transition-all cursor-pointer"
            title="শাফল বা এলোমেলো করুন"
          >
            <Shuffle className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">শাফল</span>
          </button>
          <button
            onClick={resetCurrentDeckProgress}
            className="flex items-center gap-1 px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-200 text-xs font-bold transition-all cursor-pointer"
            title="এই ডেকের প্রোগ্রেস রিসেট করুন"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">রিসেট</span>
          </button>
        </div>
      </div>

      {/* =========================================================================
          4. PROMINENT ACTIVE FLASHCARD WITH TOUCH SWIPE (UPPER FOLD)
         ========================================================================= */}
      {cardsList.length === 0 ? (
        <div className="py-14 text-center max-w-md mx-auto px-4 bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 w-full my-4">
          <Sparkles className="w-10 h-10 text-slate-400 dark:text-slate-600 mx-auto mb-2 animate-pulse" />
          <h3 className="text-base font-bold text-slate-800 dark:text-slate-200">কোনো ফ্ল্যাশকার্ড পাওয়া যায়নি</h3>
          <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">দয়া করে অন্য কোনো সপ্তাহ বা অধ্যায় নির্বাচন করুন।</p>
          <button
            onClick={() => { setSelectedChapter('all'); setActiveSubject('All'); }}
            className="mt-4 px-4 py-1.5 rounded-xl bg-[#056839] text-white text-xs font-bold shadow-xs cursor-pointer"
          >
            সব কার্ড দেখুন
          </button>
        </div>
      ) : (
        <div 
          className="w-full my-1 select-none transition-all duration-300 cursor-pointer"
          onTouchStart={handleTouchStart}
          onTouchEnd={handleTouchEnd}
          onClick={() => setIsFlipped(!isFlipped)}
        >
          <div 
            className={`w-full rounded-3xl p-5 sm:p-7 border-2 transition-all duration-300 shadow-md flex flex-col justify-between min-h-[300px] sm:min-h-[340px] relative overflow-hidden ${
              isFlipped 
                ? 'bg-white dark:bg-slate-900 border-emerald-500/70 dark:border-emerald-500/60 shadow-emerald-500/5' 
                : 'bg-white dark:bg-slate-900 border-slate-200/90 dark:border-slate-800 hover:border-[#056839]/60'
            }`}
          >
            {/* Top Bar of the Card */}
            <div className="flex items-center justify-between gap-2 border-b border-slate-100 dark:border-slate-800 pb-3">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20">
                  {currentCard?.subject || 'ভর্তি পরীক্ষা'}
                </span>
                <span className="text-xs font-bold text-slate-600 dark:text-slate-300">
                  {currentCard?.chapter_display || currentCard?.chapter}
                </span>
                <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold border ${currentTypeBadge.color}`}>
                  {currentTypeBadge.text}
                </span>
              </div>

              <div className="flex items-center gap-2">
                {isCurrentMastered && (
                  <span className="flex items-center gap-1 text-[11px] font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-200 dark:border-emerald-500/20">
                    <CheckCircle className="w-3.5 h-3.5" /> আয়ত্ত
                  </span>
                )}
                {isFlipped ? (
                  <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 flex items-center gap-1">
                    <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
                    মাস্টার সল্যুশন
                  </span>
                ) : (
                  <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                    প্রশ্ন / রিকল কার্ড
                  </span>
                )}
              </div>
            </div>

            {/* Central Card Body */}
            <div className="min-h-[180px] sm:min-h-[200px] flex items-center justify-center p-3 sm:p-5 text-center w-full my-auto">
              {!isFlipped ? (
                /* FRONT: Topic Title & Active Recall Inquiry */
                <div className="w-full space-y-3">
                  <h2 className="text-lg sm:text-2xl font-black text-slate-900 dark:text-white leading-relaxed max-w-2xl mx-auto">
                    <MathText content={currentCard?.title} />
                  </h2>
                  <div className="p-3.5 sm:p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/80 max-w-xl mx-auto text-slate-700 dark:text-slate-300 font-medium text-xs sm:text-sm leading-relaxed">
                    <MathText content={currentCard?.frontPrompt} />
                  </div>
                </div>
              ) : (
                /* BACK: Formula Box, Core Concept, 5-Second Hack, and Trap Alerts */
                <div className="w-full space-y-3 text-left">
                  
                  {/* High-Contrast Formula Box if present */}
                  {currentCard?.formula && (
                    <div>
                      <div className="flex items-center gap-1.5 text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">
                        <span>📐 গাণিতিক সমীকরণ / সূত্র:</span>
                      </div>
                      <FlashcardFormulaBox formula={currentCard.formula} />
                    </div>
                  )}

                  {/* Core Concept & Explanation */}
                  {(currentCard?.concept || currentCard?.back) && (
                    <div className="p-3.5 sm:p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/80 text-slate-900 dark:text-slate-100 font-medium text-xs sm:text-sm leading-relaxed">
                      <div className="flex items-center gap-1.5 text-xs font-bold text-emerald-700 dark:text-emerald-400 mb-1">
                        <span className="text-amber-500">💡</span>
                        <span>কোর কনসেপ্ট ও সমাধান:</span>
                      </div>
                      <MathText content={currentCard?.concept || currentCard?.back} />
                    </div>
                  )}

                  {/* ⚡ 5-Second Hack if present */}
                  {currentCard?.hack && (
                    <div className="p-3.5 rounded-2xl bg-amber-500/10 dark:bg-amber-950/20 border border-amber-500/20 text-slate-900 dark:text-slate-100 text-xs sm:text-sm font-medium leading-relaxed">
                      <div className="flex items-center gap-1.5 text-xs font-bold text-amber-700 dark:text-amber-400 mb-1">
                        <Zap className="w-3.5 h-3.5 text-amber-500" />
                        <span>৫-সেকেন্ড স্পিড হ্যাক:</span>
                      </div>
                      <MathText content={currentCard.hack} />
                    </div>
                  )}

                  {/* ⚠️ Trap Alert if present */}
                  {currentCard?.trap && (
                    <div className="p-3.5 rounded-2xl bg-rose-500/10 dark:bg-rose-950/20 border border-rose-500/20 text-slate-900 dark:text-slate-100 text-xs sm:text-sm font-medium leading-relaxed">
                      <div className="flex items-center gap-1.5 text-xs font-bold text-rose-700 dark:text-rose-400 mb-1">
                        <ShieldAlert className="w-3.5 h-3.5 text-rose-500" />
                        <span>কমন নেগেটিভ ট্র্যাপ অ্যালার্ট:</span>
                      </div>
                      <MathText content={currentCard.trap} />
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Bottom Flip Prompt Indicator */}
            <div className="flex items-center justify-center gap-2 text-xs text-slate-400 dark:text-slate-500 font-bold border-t border-slate-100 dark:border-slate-800 pt-3">
              <RotateCw className="w-3.5 h-3.5 text-[#056839] dark:text-emerald-400" />
              <span>{isFlipped ? 'পুনরায় প্রশ্ন দেখতে ট্যাপ করুন' : 'কার্ডের সমাধান, ৫-সেকেন্ড হ্যাক ও ট্র্যাপ দেখতে ট্যাপ করুন'}</span>
            </div>
          </div>
        </div>
      )}

      {/* =========================================================================
          5. VISIBLE NEXT / PREV ARROWS & RESPONSE CONTROLS
         ========================================================================= */}
      <div className="w-full flex items-center justify-between gap-2 sm:gap-3 mt-3 max-w-2xl">
        {/* Left Arrow Button */}
        <button
          onClick={(e) => { e.stopPropagation(); prevCard(); }}
          className="p-3 sm:p-3.5 rounded-2xl bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200/80 dark:border-slate-800 shadow-sm transition-all active:scale-95 cursor-pointer flex items-center gap-1"
          title="পূর্ববর্তী কার্ড (ArrowLeft বা Swipe Right)"
        >
          <ChevronLeft className="w-5 h-5" />
          <span className="text-xs font-bold hidden sm:inline">পূর্ববর্তী</span>
        </button>

        {/* Central Spaced Repetition Response Controls */}
        <div className="flex items-center gap-2 sm:gap-3 flex-1 justify-center max-w-sm">
          <button
            onClick={(e) => { e.stopPropagation(); markReview(); }}
            className="flex-1 flex items-center justify-center gap-1.5 py-3 sm:py-3.5 px-3 rounded-2xl bg-rose-50 dark:bg-rose-950/30 hover:bg-rose-100 dark:hover:bg-rose-900/40 text-rose-700 dark:text-rose-300 border border-rose-200 dark:border-rose-900/60 text-xs sm:text-sm font-bold shadow-xs transition-all active:scale-95 cursor-pointer"
            title="আবার পড়ুন (কীবোর্ড ১ চাপুন)"
          >
            <RotateCcw className="w-4 h-4" />
            <span>আবার পড়ব [1]</span>
          </button>

          <button
            onClick={(e) => { e.stopPropagation(); markMastered(); }}
            className="flex-1 flex items-center justify-center gap-1.5 py-3 sm:py-3.5 px-3 rounded-2xl bg-gradient-to-r from-[#056839] to-emerald-600 hover:from-[#04522d] hover:to-emerald-700 text-white text-xs sm:text-sm font-bold shadow-md shadow-emerald-700/20 transition-all active:scale-95 cursor-pointer"
            title="মনে আছে (কীবোর্ড ২ চাপুন)"
          >
            <CheckCircle className="w-4 h-4" />
            <span>মনে আছে [2]</span>
          </button>
        </div>

        {/* Right Arrow Button */}
        <button
          onClick={(e) => { e.stopPropagation(); nextCard(); }}
          className="p-3 sm:p-3.5 rounded-2xl bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200/80 dark:border-slate-800 shadow-sm transition-all active:scale-95 cursor-pointer flex items-center gap-1"
          title="পরবর্তী কার্ড (ArrowRight বা Swipe Left)"
        >
          <span className="text-xs font-bold hidden sm:inline">পরবর্তী</span>
          <ChevronRight className="w-5 h-5" />
        </button>
      </div>

      {/* Touch Swipe and Keyboard Shortcuts Legend */}
      <div className="mt-3 text-[11px] text-slate-400 dark:text-slate-500 font-mono text-center flex items-center justify-center gap-3">
        <span>📱 মোবাইল সোয়াইপ (বাম/ডান)</span>
        <span className="hidden sm:inline">•</span>
        <span className="hidden sm:inline">[Space] উল্টান • [←] পূর্ববর্তী • [→] পরবর্তী • [1] আবার পড়ব • [2] মনে আছে</span>
      </div>

      </>
      )}
    </div>
  );
};

