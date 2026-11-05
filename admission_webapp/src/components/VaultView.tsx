/**
 * VaultView.tsx - Master Admission Formula & Trap Vault
 * Features:
 * - Dual Hierarchy: Level 1 (Weekly Selector W1-W7) + Level 2 (Dynamic Subject & Chapter Chips)
 * - 100% KaTeX Rendering with High-Contrast FormulaBox & copy button
 * - Segmented Card Types: All, Core Formulas, Speed Hacks, Trap Alerts
 * - Special Quick Tools responsive Bottom Sheet / Modal (Triplets, Logs, Stoichiometry)
 */

import React, { useState, useMemo, useEffect, useRef } from 'react';
import { 
  Search, 
  Copy, 
  Check, 
  ShieldAlert, 
  Sparkles, 
  X,
  BookOpen,
  Zap,
  SlidersHorizontal,
  Layers
} from 'lucide-react';
import katex from 'katex';
import type { VaultData, VaultEntry, SubjectType, WeekFilterType } from '../types';
import { MathText, parseMarkdownTable } from './MathText';

interface VaultViewProps {
  vault: VaultData;
  selectedWeek?: WeekFilterType;
  selectedSubject?: SubjectType;
}

type ActiveWeek = 'all' | 1 | 2 | 3 | 4 | 5 | 6 | 7;
type ActiveSubject = 'All' | 'Physics' | 'Chemistry' | 'Higher Math' | 'Biology' | 'English' | 'GK';
type ActiveCardType = 'all' | 'core_formula' | 'shortcut' | 'trap' | 'table' | 'quick_tools';

const WEEK_TABS: { id: ActiveWeek; label: string; weekNum?: number }[] = [
  { id: 'all', label: 'সব সপ্তাহ' },
  { id: 1, label: 'Week 01', weekNum: 1 },
  { id: 2, label: 'Week 02', weekNum: 2 },
  { id: 3, label: 'Week 03', weekNum: 3 },
  { id: 4, label: 'Week 04', weekNum: 4 },
  { id: 5, label: 'Week 05', weekNum: 5 },
  { id: 6, label: 'Week 06', weekNum: 6 },
  { id: 7, label: 'Week 07', weekNum: 7 },
];

const SUBJECT_OPTIONS: { id: ActiveSubject; label: string; icon: string; colorClass: string; activeClass: string }[] = [
  { 
    id: 'All', 
    label: 'সব বিষয়', 
    icon: '📚',
    colorClass: 'border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 bg-slate-50 dark:bg-slate-900/60',
    activeClass: 'bg-slate-900 text-white dark:bg-white dark:text-slate-900 border-transparent shadow-sm'
  },
  { 
    id: 'Physics', 
    label: 'পদার্থবিজ্ঞান', 
    icon: '⚡',
    colorClass: 'border-indigo-200 dark:border-indigo-900/60 text-indigo-700 dark:text-indigo-400 bg-indigo-50/60 dark:bg-indigo-950/20',
    activeClass: 'bg-indigo-600 text-white border-indigo-600 shadow-sm shadow-indigo-600/30'
  },
  { 
    id: 'Chemistry', 
    label: 'রসায়ন', 
    icon: '🧪',
    colorClass: 'border-teal-200 dark:border-teal-900/60 text-teal-700 dark:text-teal-400 bg-teal-50/60 dark:bg-teal-950/20',
    activeClass: 'bg-teal-600 text-white border-teal-600 shadow-sm shadow-teal-600/30'
  },
  { 
    id: 'Higher Math', 
    label: 'উচ্চতর গণিত', 
    icon: '📐',
    colorClass: 'border-purple-200 dark:border-purple-900/60 text-purple-700 dark:text-purple-400 bg-purple-50/60 dark:bg-purple-950/20',
    activeClass: 'bg-purple-600 text-white border-purple-600 shadow-sm shadow-purple-600/30'
  },
  { 
    id: 'Biology', 
    label: 'জীববিজ্ঞান', 
    icon: '🧬',
    colorClass: 'border-emerald-200 dark:border-emerald-900/60 text-emerald-700 dark:text-emerald-400 bg-emerald-50/60 dark:bg-emerald-950/20',
    activeClass: 'bg-[#056839] text-white border-[#056839] shadow-sm shadow-emerald-700/30'
  },
  { 
    id: 'English', 
    label: 'English', 
    icon: '📖',
    colorClass: 'border-sky-200 dark:border-sky-900/60 text-sky-700 dark:text-sky-400 bg-sky-50/60 dark:bg-sky-950/20',
    activeClass: 'bg-sky-600 text-white border-sky-600 shadow-sm shadow-sky-600/30'
  },
  { 
    id: 'GK', 
    label: 'সাধারণ জ্ঞান', 
    icon: '🇧🇩',
    colorClass: 'border-amber-200 dark:border-amber-900/60 text-amber-700 dark:text-amber-400 bg-amber-50/60 dark:bg-amber-950/20',
    activeClass: 'bg-amber-600 text-white border-amber-600 shadow-sm shadow-amber-600/30'
  },
];

function weekFilterToActive(filter?: WeekFilterType): ActiveWeek {
  if (filter && filter !== 'all') {
    const match = filter.match(/week_0?(\d+)/);
    if (match) {
      const num = parseInt(match[1], 10);
      if (num >= 1 && num <= 7) return num as ActiveWeek;
    }
  }
  // Default to latest active week (Week 06) so initial mount renders only ~20 cards instantly
  return 6;
}

/** Clean, mobile-responsive HTML table for comparative matrices & biological tables */
export const StructuredTableView: React.FC<{
  headers: string[];
  rows: string[][];
  onCopy?: () => void;
  isCopied?: boolean;
}> = ({ headers, rows, onCopy, isCopied }) => {
  return (
    <div className="relative group my-3">
      <div 
        className="w-full overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 shadow-xs"
        style={{ WebkitOverflowScrolling: 'touch' }}
      >
        <table className="w-full text-left border-collapse min-w-[280px]">
          <thead>
            <tr className="bg-slate-100 dark:bg-slate-800 text-xs font-semibold text-slate-700 dark:text-slate-200 border-b border-slate-200 dark:border-slate-700">
              {headers.map((h, i) => (
                <th key={i} className="py-2.5 px-3 text-xs font-semibold text-slate-700 dark:text-slate-200 border-b border-slate-200 dark:border-slate-700">
                  <MathText content={h} />
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, rIdx) => (
              <tr 
                key={rIdx} 
                className="even:bg-slate-50/50 dark:even:bg-slate-800/30 border-b border-slate-100 dark:border-slate-800/60 transition-colors"
              >
                {row.map((cell, cIdx) => (
                  <td 
                    key={cIdx} 
                    className="py-2 px-3 text-xs text-slate-800 dark:text-slate-100 border-b border-slate-100 dark:border-slate-800/60 leading-relaxed font-normal"
                  >
                    <MathText content={cell} />
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {onCopy && (
        <button
          type="button"
          onClick={onCopy}
          className="absolute top-2 right-2 p-1.5 rounded-lg bg-slate-200/90 dark:bg-slate-800/90 hover:bg-slate-300 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition-all opacity-0 group-hover:opacity-100 flex items-center gap-1 text-[11px] font-mono cursor-pointer shadow-xs active:scale-95 z-10"
          title="ছক কপি করুন"
        >
          {isCopied ? (
            <>
              <Check className="w-3.5 h-3.5 text-emerald-500" />
              <span className="text-emerald-500 font-bold hidden sm:inline">কপি হয়েছে</span>
            </>
          ) : (
            <>
              <Copy className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">কপি</span>
            </>
          )}
        </button>
      )}
    </div>
  );
};

/** High-contrast KaTeX formula box with built-in copy and error protection */
const FormulaBox: React.FC<{
  formula: string;
  onCopy: () => void;
  isCopied: boolean;
}> = ({ formula, onCopy, isCopied }) => {
  const parsedTable = useMemo(() => parseMarkdownTable(formula), [formula]);
  if (parsedTable) {
    return (
      <StructuredTableView
        headers={parsedTable.headers}
        rows={parsedTable.rows}
        onCopy={onCopy}
        isCopied={isCopied}
      />
    );
  }

  const renderedHtml = useMemo(() => {
    let clean = formula.trim();
    if (clean.startsWith('$$') && clean.endsWith('$$')) {
      clean = clean.slice(2, -2).trim();
    } else if (clean.startsWith('$') && clean.endsWith('$')) {
      clean = clean.slice(1, -1).trim();
    }

    // Auto-fix missing backslashes & unicode subscripts
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
    <div className="relative group bg-slate-900 dark:bg-slate-950 border border-slate-800 dark:border-slate-800/80 rounded-xl p-3 sm:p-4 my-3 overflow-x-auto no-scrollbar shadow-inner text-center">
      <div 
        className="text-white text-sm sm:text-base inline-block max-w-full overflow-x-auto no-scrollbar py-1"
        dangerouslySetInnerHTML={{ __html: renderedHtml }}
      />
      <button
        type="button"
        onClick={onCopy}
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

export const VaultView: React.FC<VaultViewProps> = ({ 
  vault, 
  selectedWeek: propWeek, 
  selectedSubject: propSubject 
}) => {
  const [activeWeek, setActiveWeek] = useState<ActiveWeek>(() => weekFilterToActive(propWeek));
  const [activeSubject, setActiveSubject] = useState<ActiveSubject>(
    propSubject && propSubject !== 'All' ? propSubject : 'All'
  );
  const [selectedChapter, setSelectedChapter] = useState<string>('all');
  const [selectedCardType, setSelectedCardType] = useState<ActiveCardType>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [showQuickToolsModal, setShowQuickToolsModal] = useState(false);
  const [quickToolTab, setQuickToolTab] = useState<'triplets' | 'quick_math' | 'fractions' | 'w4_bridge' | 'w5_bridge' | 'w6_bridge' | 'w7_matrix'>('triplets');
  const [visibleCount, setVisibleCount] = useState<number>(15);
  const chapterScrollRef = useRef<HTMLDivElement | null>(null);
  const sentinelRef = useRef<HTMLDivElement | null>(null);

  // Sync with prop changes from parent
  useEffect(() => {
    if (propWeek !== undefined) {
      setActiveWeek(weekFilterToActive(propWeek));
      setSelectedChapter('all');
    }
  }, [propWeek]);

  useEffect(() => {
    if (propSubject !== undefined) {
      setActiveSubject(propSubject);
      setSelectedChapter('all');
    }
  }, [propSubject]);

  // Reset visibleCount to 15 whenever filters change
  useEffect(() => {
    setVisibleCount(15);
  }, [activeWeek, activeSubject, selectedChapter, selectedCardType, searchQuery]);

  // Close Quick Tools Modal on ESC key
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && showQuickToolsModal) {
        setShowQuickToolsModal(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [showQuickToolsModal]);


  const entries: VaultEntry[] = useMemo(() => vault.entries || [], [vault.entries]);

  // Week-level item counts
  const weekCounts = useMemo(() => {
    const counts: Record<string | number, number> = { all: entries.length };
    entries.forEach((e) => {
      const w = e.week;
      if (w !== undefined) {
        counts[w] = (counts[w] || 0) + 1;
      }
    });
    return counts;
  }, [entries]);

  // Entries filtered by Active Week
  const weekScopedEntries = useMemo(() => {
    if (activeWeek === 'all') return entries;
    return entries.filter((e) => e.week === activeWeek);
  }, [entries, activeWeek]);

  // Subject-level counts for the active week
  const subjectCounts = useMemo(() => {
    const counts: Record<string, number> = { All: weekScopedEntries.length };
    weekScopedEntries.forEach((e) => {
      counts[e.subject] = (counts[e.subject] || 0) + 1;
    });
    return counts;
  }, [weekScopedEntries]);

  // Entries filtered by Active Week AND Active Subject
  const subjectScopedEntries = useMemo(() => {
    if (activeSubject === 'All') return weekScopedEntries;
    return weekScopedEntries.filter((e) => e.subject === activeSubject);
  }, [weekScopedEntries, activeSubject]);

  // Available chapters dynamically derived based on active week and active subject
  const availableChapters = useMemo(() => {
    const chapterMap = new Map<string, number>();
    subjectScopedEntries.forEach((e) => {
      if (e.chapter) {
        chapterMap.set(e.chapter, (chapterMap.get(e.chapter) || 0) + 1);
      }
    });

    return Array.from(chapterMap.entries())
      .map(([name, count]) => ({ name, count }))
      .sort((a, b) => a.name.localeCompare(b.name, 'bn'));
  }, [subjectScopedEntries]);

  // Card type counts under current week, subject, and chapter
  const typeCounts = useMemo(() => {
    const base = selectedChapter === 'all'
      ? subjectScopedEntries
      : subjectScopedEntries.filter((e) => e.chapter === selectedChapter);

    const qToolsCount = (vault.triplets?.length || 0) + (vault.quick_math?.length || 0) + (vault.magic_fractions?.length || 0);

    return {
      all: base.length,
      core_formula: base.filter((e) => e.type === 'core_formula').length,
      shortcut: base.filter((e) => e.type === 'shortcut').length,
      trap: base.filter((e) => e.type === 'trap').length,
      quick_tools: qToolsCount,
    };
  }, [subjectScopedEntries, selectedChapter, vault]);

  // Final filtered entries
  const filteredEntries = useMemo(() => {
    const q = searchQuery.toLowerCase().trim();

    return subjectScopedEntries.filter((item) => {
      // Chapter filter
      if (selectedChapter !== 'all' && item.chapter !== selectedChapter) return false;

      // Card Type filter
      if (selectedCardType !== 'all' && selectedCardType !== 'quick_tools' && item.type !== selectedCardType) return false;

      // Search Query filter
      if (q) {
        const inTitle = item.title?.toLowerCase().includes(q) ?? false;
        const inFormula = item.formula?.toLowerCase().includes(q) ?? false;
        const inConcept = item.concept?.toLowerCase().includes(q) ?? false;
        const inHack = item.hack?.toLowerCase().includes(q) ?? false;
        const inTrap = item.trap?.toLowerCase().includes(q) ?? false;
        const inChapter = item.chapter?.toLowerCase().includes(q) ?? false;
        const inTags = item.tags?.some((t) => t.toLowerCase().includes(q)) ?? false;

        if (!inTitle && !inFormula && !inConcept && !inHack && !inTrap && !inChapter && !inTags) {
          return false;
        }
      }

      return true;
    });
  }, [subjectScopedEntries, selectedChapter, selectedCardType, searchQuery]);

  const copyToClipboard = (id: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleWeekChange = (w: ActiveWeek) => {
    setActiveWeek(w);
    setSelectedChapter('all');
  };

  const handleSubjectChange = (sub: ActiveSubject) => {
    setActiveSubject(sub);
    setSelectedChapter('all');
  };

  // Sliced array for virtualized chunked lazy loading (strictly limits DOM KaTeX nodes)
  const displayedCards = useMemo(() => {
    return filteredEntries.slice(0, visibleCount);
  }, [filteredEntries, visibleCount]);

  // Group ONLY the currently displayed cards by chapter
  const groupedDisplayedCards = useMemo(() => {
    const map = new Map<string, VaultEntry[]>();
    displayedCards.forEach((entry) => {
      const list = map.get(entry.chapter) || [];
      list.push(entry);
      map.set(entry.chapter, list);
    });
    return map;
  }, [displayedCards]);

  // Infinite scroll trigger via IntersectionObserver
  useEffect(() => {
    const sentinel = sentinelRef.current;
    if (!sentinel) return;

    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          setVisibleCount((prev) => {
            if (prev < filteredEntries.length) {
              return Math.min(prev + 15, filteredEntries.length);
            }
            return prev;
          });
        }
      },
      { rootMargin: '300px' }
    );

    observer.observe(sentinel);
    return () => observer.disconnect();
  }, [filteredEntries.length]);


  // Legacy quick tools filter
  const qTool = searchQuery.toLowerCase().trim();
  const filteredTriplets = (vault.triplets || []).filter((t) => 
    (!qTool || t.sides.toLowerCase().includes(qTool) || t.result.toLowerCase().includes(qTool) || t.app.toLowerCase().includes(qTool))
  );
  const filteredQuickMath = (vault.quick_math || []).filter((m) =>
    (!qTool || m.type.toLowerCase().includes(qTool) || m.item.toLowerCase().includes(qTool))
  );
  const filteredFractions = (vault.magic_fractions || []).filter((f) =>
    (!qTool || f.compound.toLowerCase().includes(qTool) || f.mw.toLowerCase().includes(qTool) || f.trick.toLowerCase().includes(qTool))
  );

  // Dedicated Interactive Quick Tools View (Triplets, Roots, Log, Fractions, Bridge Hacks)
  const renderQuickToolsView = () => (
    <div className="bg-white dark:bg-slate-900 rounded-3xl p-5 sm:p-6 border border-slate-200/90 dark:border-slate-800 shadow-sm space-y-5 animate-in fade-in duration-200">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200/80 dark:border-slate-800/80">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-2xl bg-gradient-to-tr from-amber-500 to-orange-500 text-white shadow-md shadow-amber-500/25">
            <Zap className="w-5 h-5 fill-current" />
          </div>
          <div>
            <h3 className="text-base sm:text-lg font-black text-slate-900 dark:text-white">
              ⚡ স্পেশাল কুইক রেফারেন্স টেবিল ও নো-ক্যালকুলেটর ভল্ট
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              ভর্তি পরীক্ষায় ক্যালকুলেটর ছাড়া চোখের পলকে সমস্যা সমাধানের চার্ট ও শর্টকাট ম্যাট্রিক্স
            </p>
          </div>
        </div>
        <button
          type="button"
          onClick={() => setSelectedCardType('all')}
          className="text-xs font-bold text-slate-500 hover:text-slate-900 dark:hover:text-white underline cursor-pointer shrink-0 self-start sm:self-auto"
        >
          অধ্যায় সূত্রে ফিরে যান
        </button>
      </div>

      {/* Sub-tool navigation tabs */}
      <div className="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1">
        {[
          { id: 'triplets' as const, label: `📐 পিথাগোরিয়ান ট্রিপলেট (${filteredTriplets.length})` },
          { id: 'quick_math' as const, label: `⚡ রুট ও লগ হ্যাক (${filteredQuickMath.length})` },
          { id: 'fractions' as const, label: `🧪 স্টয়কিওমেট্রি ফ্র্যাকশন (${filteredFractions.length})` },
          { id: 'w4_bridge' as const, label: '🎯 Week 04 ব্রিজ' },
          { id: 'w5_bridge' as const, label: '🔮 Week 05 ব্রিজ' },
          { id: 'w6_bridge' as const, label: '🚀 Week 06 ব্রিজ' },
          { id: 'w7_matrix' as const, label: '👑 Week 07 ব্রিজ' },
        ].map((tab) => (
          <button
            key={tab.id}
            type="button"
            onClick={() => setQuickToolTab(tab.id)}
            className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer ${
              quickToolTab === tab.id
                ? 'bg-amber-600 text-white shadow-xs'
                : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Quick Tools Content */}
      <div className="space-y-4 pt-1">
        {quickToolTab === 'triplets' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {filteredTriplets.map((item, idx) => (
              <div key={idx} className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60 flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-mono font-bold text-sm text-sky-700 dark:text-sky-400">{item.sides}</span>
                    <span className="px-2.5 py-0.5 rounded-full bg-sky-100 dark:bg-sky-950/50 text-sky-700 dark:text-sky-300 text-[11px] font-mono font-bold">
                      মান: {item.result}
                    </span>
                  </div>
                  <div className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                    <MathText content={item.app} />
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {quickToolTab === 'quick_math' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {filteredQuickMath.map((item, idx) => (
              <div key={idx} className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60 flex items-center justify-between gap-3">
                <div className="flex-1 text-xs sm:text-sm font-medium text-slate-800 dark:text-slate-200">
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-amber-500/10 text-amber-700 dark:text-amber-400 mr-2">
                    {item.type}
                  </span>
                  <MathText content={item.item} />
                </div>
              </div>
            ))}
          </div>
        )}

        {quickToolTab === 'fractions' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {filteredFractions.map((item, idx) => (
              <div key={idx} className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
                <div className="flex items-center justify-between mb-2">
                  <span className="font-bold text-xs sm:text-sm text-teal-700 dark:text-teal-400">
                    <MathText content={item.compound} />
                  </span>
                  <span className="font-mono text-xs px-2.5 py-0.5 rounded-full bg-slate-200/80 dark:bg-slate-700 text-slate-700 dark:text-slate-300 font-bold">
                    M: {item.mw}
                  </span>
                </div>
                <div className="text-xs text-slate-600 dark:text-slate-300">
                  <MathText content={item.trick} />
                </div>
              </div>
            ))}
          </div>
        )}

        {quickToolTab === 'w4_bridge' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-indigo-600 dark:text-indigo-400">হ্রদের গভীরতা হ্যাক (বুদ্বুদ)</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">১০.৩৩ মিটার</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="ব্যাস বা ব্যাসার্ধ $n$ গুণ হলে: $h = (n^3 - 1) \times 10.33\text{ m}$<br />আয়তন $n$ গুণ হলে: $h = (n - 1) \times 10.33\text{ m}$" />
              </div>
            </div>

            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-teal-600 dark:text-teal-400">সংকরায়ন দ্রুত গণনা</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">H মান</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="$H = \frac{1}{2}(V + M - C + A)$<br />$H=2 \implies sp, \quad H=3 \implies sp^2, \quad H=4 \implies sp^3, \quad H=5 \implies sp^3d$" />
              </div>
            </div>

            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-purple-600 dark:text-purple-400">কর্ণের সংখ্যা ও হাত মেলানো</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">nCr হ্যাক</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="কর্ণের সংখ্যা: $\frac{n(n-3)}{2}$ (১২ বাহুর কর্ণ = ৫৪টি)<br />করমর্দন সংখ্যা: $\frac{n(n-1)}{2}$ (১০ জনের করমর্দন = ৪৫টি)" />
              </div>
            </div>

            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-emerald-600 dark:text-emerald-400">মেন্ডেলের ব্যতিক্রম অনুপাত</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">জিনতত্ত্ব</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="পরিপূরক জিন: ৯:৭<br />এপিস্ট্যাসিস (প্রকট): ১২:৩:১<br />এপিস্ট্যাসিস (দ্বৈত প্রচ্ছন্ন): ৯:৭<br />লিথাল জিন: ২:১" />
              </div>
            </div>
          </div>
        )}

        {quickToolTab === 'w5_bridge' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-indigo-600 dark:text-indigo-400">সরল ছন্দিত গতিতে শক্তি</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">সরণ x</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="$E_k = E_p \implies x = \pm \frac{A}{\sqrt{2}}$<br />$E_k = 3E_p \implies x = \pm \frac{A}{2}$<br />$E_p = 3E_k \implies x = \pm \frac{\sqrt{3}}{2}A$" />
              </div>
            </div>

            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-teal-600 dark:text-teal-400">ফ্যারাডের মানসিক গণনা</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">৯৬৫০০ কুলম্ব</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="$1\text{ F} = 96500\text{ C} \implies \text{দেয় } \frac{\text{মোলার ভর}}{\text{যোজ্যতা}}\text{ গ্রাম}$<br />$1\text{ F} \implies \text{Al}: 9\text{ g}, \quad \text{Cu}: 31.75\text{ g}, \quad \text{Ag}: 108\text{ g}$" />
              </div>
            </div>
          </div>
        )}

        {quickToolTab === 'w6_bridge' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-indigo-600 dark:text-indigo-400">ত্রুটিপূর্ণ থার্মোমিটার হ্যাক</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">অনুপাত</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="$\frac{X - \text{ice}}{\text{steam} - \text{ice}} = \frac{C}{100}$<br />বরফ $4^\circ\text{C}$, বাষ্প $96^\circ\text{C}$ হলে ৫০ পাঠের সঠিক মান ঠিক $50^\circ\text{C}$!" />
              </div>
            </div>

            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-purple-600 dark:text-purple-400">লব হরের অন্তরক ইন্টিগ্রেশন</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">১ সেকেন্ড</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="$\int \frac{f'(x)}{f(x)} dx = \ln|f(x)| + c$<br />$\int \frac{f'(x)}{\sqrt{f(x)}} dx = 2\sqrt{f(x)} + c$" />
              </div>
            </div>
          </div>
        )}

        {quickToolTab === 'w7_matrix' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-indigo-600 dark:text-indigo-400">ফটোইলেক্ট্রিক ১২৪০০ ফর্মুলা</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">eV মান</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="$E = \frac{12400}{\lambda(\text{\AA})}\text{ eV}$<br />নিবৃত্তি বিভব $V_s$ এর ভোল্ট মান সংখ্যাগতভাবে $K_{\max}(\text{eV})$ এর সমান!" />
              </div>
            </div>

            <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-4 border border-slate-200/80 dark:border-slate-700/60">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-bold text-xs text-teal-600 dark:text-teal-400">কার্বোক্যাটায়ন স্থায়িত্ব ক্রম</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">জৈব রসায়ন</span>
              </div>
              <div className="text-xs text-slate-600 dark:text-slate-300">
                <MathText content="ক্যাটায়ন ও মুক্ত মূলক: $3^\circ > 2^\circ > 1^\circ > \text{CH}_3^+$<br />কার্বানায়ন: $\text{CH}_3^- > 1^\circ > 2^\circ > 3^\circ$" />
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );

  return (
    <div className="max-w-6xl mx-auto py-5 px-3 sm:px-6">
      
      {/* 1. APP-LIKE HEADER */}
      <div className="mb-6 space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div className="flex items-center gap-2 mb-1.5 flex-wrap">
              <span className="px-3 py-1 rounded-full text-[11px] font-extrabold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-[#056839] dark:text-emerald-400" />
                মাস্টার অ্যাডমিশন ভল্ট
              </span>
              <span className="text-xs font-mono font-bold text-slate-500 dark:text-slate-400">
                {entries.length}টি হাই-ইল্ড সূত্র ও ট্র্যাপ • ৭টি সপ্তাহ
              </span>
            </div>
            <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
              চ্যাপ্টারওয়াইজ সূত্র, ৫-সেকেন্ড হ্যাক ও ট্র্যাপ ম্যাট্রিক্স
            </h1>
          </div>

          {/* Quick Tools Launch Button */}
          <button
            type="button"
            onClick={() => {
              if (selectedCardType === 'quick_tools') {
                setSelectedCardType('all');
              } else {
                setSelectedCardType('quick_tools');
                window.scrollTo({ top: 160, behavior: 'smooth' });
              }
            }}
            className={`flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer shrink-0 active:scale-95 ${
              selectedCardType === 'quick_tools'
                ? 'bg-amber-600 text-white ring-2 ring-amber-400 shadow-sm'
                : 'bg-amber-500 hover:bg-amber-600 text-white shadow-sm shadow-amber-500/25'
            }`}
          >
            <Zap className="w-4 h-4 fill-current" />
            <span>{selectedCardType === 'quick_tools' ? '✓ কুইক টেবিল খোলা আছে' : 'স্পেশাল টুলস (Triplets & Roots)'}</span>
          </button>
        </div>

        {/* Real-time Search Input */}
        <div className="relative">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5 pointer-events-none" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="সূত্র, শর্টকাট, অধ্যায় বা ট্র্যাপ খুঁজুন (যেমন: লব্ধি, pH, দ্বিপদী, ত্রিকোণমিতি, কণিক)..."
            className="w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl pl-10 pr-9 py-2.5 text-xs sm:text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-[#056839] focus:ring-2 focus:ring-[#056839]/20 transition-all shadow-xs"
          />
          {searchQuery && (
            <button
              type="button"
              onClick={() => setSearchQuery('')}
              className="absolute right-3.5 top-3 text-slate-400 hover:text-slate-700 dark:hover:text-white transition-colors cursor-pointer"
              title="মুছে ফেলুন"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>

        {/* 2. LEVEL 1: WEEKLY SELECTOR TABS */}
        <div className="space-y-1.5">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1">
              <Layers className="w-3 h-3" /> সপ্তাহ নির্বাচন (Weekly Hierarchy)
            </span>
            {activeWeek !== 'all' && (
              <button
                type="button"
                onClick={() => handleWeekChange('all')}
                className="text-[11px] font-bold text-[#056839] dark:text-emerald-400 hover:underline cursor-pointer"
              >
                সব সপ্তাহ দেখুন
              </button>
            )}
          </div>

          <div className="flex items-center gap-2 overflow-x-auto no-scrollbar scroll-smooth pb-1 -mx-1 px-1">
            {WEEK_TABS.map((w) => {
              const isActive = activeWeek === w.id;
              const count = weekCounts[w.id] || 0;
              return (
                <button
                  key={w.id}
                  type="button"
                  onClick={() => handleWeekChange(w.id)}
                  className={`min-h-[42px] px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 shrink-0 transition-all cursor-pointer active:scale-95 border ${
                    isActive
                      ? 'bg-[#056839] text-white border-[#056839] shadow-sm shadow-emerald-700/30'
                      : 'bg-white dark:bg-slate-900 border-slate-200/90 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
                  }`}
                >
                  <span>{w.label}</span>
                  <span className={`text-[10px] font-mono px-1.5 py-0.5 rounded-full ${
                    isActive 
                      ? 'bg-white/20 text-white' 
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400'
                  }`}>
                    {count}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* 3. LEVEL 2A: SUBJECT FILTER CHIPS */}
        <div className="space-y-1.5">
          <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1">
            <SlidersHorizontal className="w-3 h-3" /> বিষয় নির্বাচন (Subject Filter)
          </div>
          <div className="flex items-center gap-2 overflow-x-auto no-scrollbar scroll-smooth pb-1 -mx-1 px-1">
            {SUBJECT_OPTIONS.map((sub) => {
              const isActive = activeSubject === sub.id;
              const subCount = subjectCounts[sub.id] || 0;

              // Hide subject if it has 0 entries in the current week (unless it's 'All')
              if (sub.id !== 'All' && subCount === 0) return null;

              return (
                <button
                  key={sub.id}
                  type="button"
                  onClick={() => handleSubjectChange(sub.id)}
                  className={`min-h-[42px] px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 shrink-0 transition-all cursor-pointer active:scale-95 border ${
                    isActive
                      ? sub.activeClass
                      : `${sub.colorClass} hover:opacity-90`
                  }`}
                >
                  <span>{sub.icon}</span>
                  <span>{sub.label}</span>
                  <span className={`text-[10px] font-mono px-1.5 py-0.5 rounded-full ${
                    isActive
                      ? 'bg-white/25 text-white'
                      : 'bg-black/5 dark:bg-white/10'
                  }`}>
                    {subCount}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* 4. LEVEL 2B: CHAPTER SWIPEABLE CHIPS */}
        {availableChapters.length > 0 && (
          <div className="space-y-1.5">
            <div className="flex items-center justify-between text-[11px] font-bold text-slate-400 dark:text-slate-500">
              <span className="uppercase tracking-wider flex items-center gap-1">
                <BookOpen className="w-3 h-3" /> অধ্যায় নির্বাচন ({availableChapters.length}টি অধ্যায়)
              </span>
              {selectedChapter !== 'all' && (
                <button
                  type="button"
                  onClick={() => setSelectedChapter('all')}
                  className="text-[#056839] dark:text-emerald-400 hover:underline cursor-pointer"
                >
                  সব অধ্যায় দেখুন
                </button>
              )}
            </div>

            <div 
              ref={chapterScrollRef}
              className="flex items-center gap-2 overflow-x-auto no-scrollbar scroll-smooth pb-1.5 -mx-1 px-1"
            >
              <button
                type="button"
                onClick={() => setSelectedChapter('all')}
                className={`min-h-[44px] px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer active:scale-95 border ${
                  selectedChapter === 'all'
                    ? 'bg-[#056839] text-white border-[#056839] shadow-sm shadow-emerald-700/30'
                    : 'bg-white dark:bg-slate-900 border-slate-200/90 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
              >
                <span>সব অধ্যায়</span>
                <span className={`ml-1.5 text-[10px] font-mono px-1.5 py-0.5 rounded-full ${
                  selectedChapter === 'all' ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                }`}>
                  {subjectScopedEntries.length}
                </span>
              </button>

              {availableChapters.map((ch) => {
                const isActive = selectedChapter === ch.name;
                return (
                  <button
                    key={ch.name}
                    type="button"
                    onClick={() => setSelectedChapter(ch.name)}
                    className={`min-h-[44px] px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold shrink-0 transition-all cursor-pointer active:scale-95 border flex items-center gap-2 ${
                      isActive
                        ? 'bg-emerald-600 text-white border-emerald-600 shadow-sm shadow-emerald-600/30 font-bold'
                        : 'bg-white dark:bg-slate-900 border-slate-200/90 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
                    }`}
                  >
                    <span>{ch.name}</span>
                    <span className={`text-[10px] font-mono px-1.5 py-0.5 rounded-full ${
                      isActive ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                    }`}>
                      {ch.count}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* 5. CARD DISPLAY TYPE SEGMENTED BAR */}
        <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-900 p-1.5 rounded-2xl border border-slate-200/80 dark:border-slate-800 overflow-x-auto no-scrollbar">
          <button
            type="button"
            onClick={() => setSelectedCardType('all')}
            className={`min-h-[40px] flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer shrink-0 ${
              selectedCardType === 'all'
                ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            <span>সব ধরন</span>
            <span className="text-[10px] font-mono px-1.5 py-0.5 rounded-full bg-slate-200/70 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300">
              {typeCounts.all}
            </span>
          </button>

          <button
            type="button"
            onClick={() => setSelectedCardType('core_formula')}
            className={`min-h-[40px] flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer shrink-0 ${
              selectedCardType === 'core_formula'
                ? 'bg-white dark:bg-slate-800 text-indigo-600 dark:text-indigo-400 shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-indigo-600 dark:hover:text-indigo-400'
            }`}
          >
            <span>📐 কোর সূত্রাবলী</span>
            <span className="text-[10px] font-mono px-1.5 py-0.5 rounded-full bg-indigo-100 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300">
              {typeCounts.core_formula}
            </span>
          </button>

          <button
            type="button"
            onClick={() => setSelectedCardType('shortcut')}
            className={`min-h-[40px] flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer shrink-0 ${
              selectedCardType === 'shortcut'
                ? 'bg-white dark:bg-slate-800 text-emerald-600 dark:text-emerald-400 shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-emerald-600 dark:hover:text-emerald-400'
            }`}
          >
            <span>⚡ নো-ক্যালকুলেটর হ্যাক</span>
            <span className="text-[10px] font-mono px-1.5 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300">
              {typeCounts.shortcut}
            </span>
          </button>

          <button
            type="button"
            onClick={() => setSelectedCardType('trap')}
            className={`min-h-[40px] flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer shrink-0 ${
              selectedCardType === 'trap'
                ? 'bg-white dark:bg-slate-800 text-rose-600 dark:text-rose-400 shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-rose-600 dark:hover:text-rose-400'
            }`}
          >
            <span>⚠️ ট্র্যাপ অ্যালার্ট</span>
            <span className="text-[10px] font-mono px-1.5 py-0.5 rounded-full bg-rose-100 dark:bg-rose-950/60 text-rose-700 dark:text-rose-300">
              {typeCounts.trap}
            </span>
          </button>

          <button
            type="button"
            onClick={() => setSelectedCardType('quick_tools')}
            className={`min-h-[40px] flex items-center justify-center gap-1.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer shrink-0 ${
              selectedCardType === 'quick_tools'
                ? 'bg-amber-500 text-white shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-amber-600 dark:hover:text-amber-400'
            }`}
          >
            <Zap className="w-3.5 h-3.5 fill-current" />
            <span>⚡ কুইক রেফারেন্স টেবিল</span>
            <span className={`text-[10px] font-mono px-1.5 py-0.5 rounded-full ${
              selectedCardType === 'quick_tools'
                ? 'bg-white/20 text-white'
                : 'bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-200'
            }`}>
              {typeCounts.quick_tools}
            </span>
          </button>
        </div>
      </div>

      {/* 6. MAIN CONTENT AREA */}
      {selectedCardType === 'quick_tools' ? (
        renderQuickToolsView()
      ) : filteredEntries.length === 0 ? (
        <div className="py-14 sm:py-16 text-center max-w-md mx-auto px-4 bg-white/80 dark:bg-slate-900/80 rounded-3xl border border-slate-200/80 dark:border-slate-800 shadow-xs backdrop-blur-md">
          <BookOpen className="w-12 h-12 text-slate-300 dark:text-slate-600 mx-auto mb-3 animate-pulse" />
          <h3 className="text-base font-bold text-slate-800 dark:text-slate-200">
            {selectedChapter !== 'all' ? `"${selectedChapter}" অধ্যায়ে কোনো সূত্র বা ট্র্যাপ পাওয়া যায়নি` : 'কোনো সূত্র বা ট্র্যাপ পাওয়া যায়নি'}
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 mb-5 leading-relaxed">
            {selectedChapter !== 'all'
              ? 'এই অধ্যায়ের জন্য নির্বাচিত ধরনের কোনো কার্ড নেই। "সব ধরন" নির্বাচন করুন অথবা অন্য অধ্যায় বেছে নিন।'
              : 'আপনার ফিল্টার বা সার্চ কীওয়ার্ডের সাথে মিলছে না। ফিল্টার রিসেট করে আবার চেষ্টা করুন।'}
          </p>
          <div className="flex items-center justify-center gap-2 flex-wrap">
            {selectedCardType !== 'all' && (
              <button
                type="button"
                onClick={() => setSelectedCardType('all')}
                className="px-4 py-2 rounded-xl bg-emerald-600 text-white text-xs sm:text-sm font-bold hover:bg-emerald-700 transition-all shadow-xs cursor-pointer active:scale-95"
              >
                সব ধরন দেখুন
              </button>
            )}
            {selectedChapter !== 'all' && (
              <button
                type="button"
                onClick={() => setSelectedChapter('all')}
                className="px-4 py-2 rounded-xl bg-indigo-600 text-white text-xs sm:text-sm font-bold hover:bg-indigo-700 transition-all shadow-xs cursor-pointer active:scale-95"
              >
                সব অধ্যায় দেখুন
              </button>
            )}
            <button
              type="button"
              onClick={() => {
                setSearchQuery('');
                setActiveWeek('all');
                setActiveSubject('All');
                setSelectedChapter('all');
                setSelectedCardType('all');
              }}
              className="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs sm:text-sm font-bold hover:bg-slate-200 dark:hover:bg-slate-700 transition-all shadow-xs cursor-pointer active:scale-95"
            >
              সব ফিল্টার রিসেট
            </button>
          </div>
        </div>
      ) : (
        <div className="space-y-6">
          {/* Active Filter Summary Bar */}
          <div className="bg-white dark:bg-slate-900 px-4 py-3 rounded-2xl border border-slate-200/80 dark:border-slate-800 flex items-center justify-between gap-3 flex-wrap shadow-xs">
            <div className="flex items-center gap-2 flex-wrap text-xs font-semibold text-slate-600 dark:text-slate-400">
              <span>মোট কার্ড:</span>
              <span className="font-extrabold text-[#056839] dark:text-emerald-400 font-mono text-sm">
                {filteredEntries.length}টি
              </span>
              
              {activeWeek !== 'all' && (
                <span className="px-2.5 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/40 text-[#056839] dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800 text-[11px] font-bold flex items-center gap-1">
                  <span>Week 0{activeWeek}</span>
                  <button 
                    type="button"
                    onClick={() => handleWeekChange('all')} 
                    className="ml-1 hover:text-rose-600 cursor-pointer text-xs"
                    title="সপ্তাহ ফিল্টার মুছুন"
                  >
                    ×
                  </button>
                </span>
              )}

              {selectedChapter !== 'all' && (
                <span className="px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 text-[11px] font-bold flex items-center gap-1">
                  <span>{selectedChapter}</span>
                  <button 
                    type="button"
                    onClick={() => setSelectedChapter('all')} 
                    className="ml-1 hover:text-rose-600 cursor-pointer text-xs"
                    title="অধ্যায় ফিল্টার মুছুন"
                  >
                    ×
                  </button>
                </span>
              )}

              {selectedCardType !== 'all' && (
                <span className="px-2.5 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 text-[11px] font-bold flex items-center gap-1">
                  <span>{selectedCardType === 'core_formula' ? 'কোর সূত্রাবলী' : selectedCardType === 'shortcut' ? 'নো-ক্যালকুলেটর হ্যাক' : 'ট্র্যাপ অ্যালার্ট'}</span>
                  <button 
                    type="button"
                    onClick={() => setSelectedCardType('all')} 
                    className="ml-1 hover:text-rose-600 cursor-pointer text-xs"
                    title="ধরণ ফিল্টার মুছুন"
                  >
                    ×
                  </button>
                </span>
              )}
            </div>

            {(activeWeek !== 'all' || selectedChapter !== 'all' || selectedCardType !== 'all' || activeSubject !== 'All' || searchQuery) && (
              <button
                type="button"
                onClick={() => {
                  setActiveWeek('all');
                  setSelectedChapter('all');
                  setSelectedCardType('all');
                  setActiveSubject('All');
                  setSearchQuery('');
                }}
                className="text-xs font-bold text-rose-600 hover:text-rose-700 dark:text-rose-400 cursor-pointer underline flex items-center gap-1"
              >
                <span>সব ফিল্টার রিসেট</span>
              </button>
            )}
          </div>

          {/* Grouped Chapter Sections (Only rendering displayedCards chunk) */}
          {Array.from(groupedDisplayedCards.entries()).map(([chapterName, chapterItems]) => {
            if (chapterItems.length === 0) return null;
            const totalInChapter = filteredEntries.filter((e) => e.chapter === chapterName).length;

            return (
              <div key={chapterName} className="space-y-3.5">
                {/* Chapter Section Title */}
                <div className="flex items-center justify-between pb-1.5 border-b border-slate-200/80 dark:border-slate-800">
                  <div className="flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-full bg-[#056839] dark:bg-emerald-400" />
                    <h2 className="text-base sm:text-lg font-black text-slate-900 dark:text-white">
                      {chapterName}
                    </h2>
                    <span className="text-xs font-mono font-bold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">
                      {chapterItems.length < totalInChapter ? `${chapterItems.length}/${totalInChapter}টি` : `${totalInChapter}টি`}
                    </span>
                  </div>
                </div>

                {/* Cards Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {chapterItems.map((item) => {
                    const isCopied = copiedId === item.id;
                    const cardTypeBadge = item.type === 'core_formula'
                      ? { label: '📐 কোর সূত্রাবলী', class: 'bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border-indigo-200 dark:border-indigo-800' }
                      : item.type === 'shortcut'
                      ? { label: '⚡ নো-ক্যালকুলেটর হ্যাক', class: 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800' }
                      : { label: '⚠️ ট্র্যাপ অ্যালার্ট', class: 'bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-800' };

                    return (
                      <div 
                        key={item.id}
                        className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/60 rounded-2xl shadow-xs hover:shadow-md transition-all p-4 sm:p-5 flex flex-col justify-between"
                      >
                        <div>
                          {/* Card Top Meta Badges */}
                          <div className="flex items-center justify-between gap-2 mb-2.5 flex-wrap">
                            <div className="flex items-center gap-1.5 flex-wrap">
                              <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-600 dark:text-slate-300">
                                Week 0{item.week}
                              </span>
                              <span className="text-[10px] font-extrabold px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-600 dark:text-slate-300">
                                {item.subject}
                              </span>
                            </div>
                            <span className={`text-[10px] font-extrabold px-2.5 py-0.5 rounded-full border ${cardTypeBadge.class}`}>
                              {cardTypeBadge.label}
                            </span>
                          </div>

                          {/* Card Title */}
                          <h3 className="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2 leading-snug">
                            {item.title}
                          </h3>

                          {/* KaTeX High-Contrast Formula Box */}
                          {item.formula && (
                            <FormulaBox
                              formula={item.formula}
                              onCopy={() => copyToClipboard(item.id, item.formula)}
                              isCopied={isCopied}
                            />
                          )}

                          {/* Core Concept Box */}
                          {item.concept && (
                            <div className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed mb-3">
                              <strong className="text-slate-900 dark:text-white font-bold block mb-1">
                                💡 মূল ধারণা:
                              </strong>
                              <MathText content={item.concept} />
                            </div>
                          )}

                          {/* Shortcut / Speed Hack Box */}
                          {item.hack && (
                            <div className="bg-emerald-500/10 dark:bg-emerald-950/30 p-3 rounded-xl border border-emerald-500/20 text-xs text-emerald-950 dark:text-emerald-200 leading-relaxed mb-2.5 overflow-x-auto no-scrollbar">
                              <strong className="text-emerald-700 dark:text-emerald-400 font-bold flex items-center gap-1 mb-1">
                                <Zap className="w-3.5 h-3.5 text-emerald-500 fill-current" /> ৫-সেকেন্ড নো-ক্যালকুলেটর হ্যাক:
                              </strong>
                              <MathText content={item.hack} />
                            </div>
                          )}

                          {/* Negative Marking Trap Box */}
                          {item.trap && (
                            <div className="bg-rose-500/10 dark:bg-rose-950/30 p-3 rounded-xl border border-rose-500/25 text-xs text-rose-950 dark:text-rose-200 leading-relaxed mb-2 overflow-x-auto no-scrollbar">
                              <strong className="text-rose-700 dark:text-rose-400 font-bold flex items-center gap-1.5 mb-1">
                                <ShieldAlert className="w-4 h-4 text-rose-500 shrink-0" /> ⚠️ সতর্কতা / যেখানে ভুল হয় (Trap Alert):
                              </strong>
                              <MathText content={item.trap} />
                            </div>
                          )}
                        </div>

                        {/* Card Tags Footer */}
                        {item.tags && item.tags.length > 0 && (
                          <div className="flex items-center gap-1.5 flex-wrap pt-3 mt-2 border-t border-slate-100 dark:border-slate-700/60">
                            {item.tags.map((tag, tIdx) => (
                              <button
                                key={tIdx}
                                type="button"
                                onClick={() => setSearchQuery(tag)}
                                className="text-[10px] font-medium px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer transition-colors"
                              >
                                #{tag}
                              </button>
                            ))}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })}

          {/* Smooth Pagination / Load More Button */}
          {visibleCount < filteredEntries.length && (
            <div className="pt-4 pb-2 text-center">
              <button
                type="button"
                onClick={() => setVisibleCount((prev) => Math.min(prev + 15, filteredEntries.length))}
                className="w-full py-3.5 px-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-sm font-bold text-[#056839] dark:text-emerald-400 hover:bg-slate-50 dark:hover:bg-slate-800/80 shadow-xs flex items-center justify-center gap-2 cursor-pointer transition-all active:scale-[0.99]"
              >
                <span>আরো ১৫টি কার্ড লোড করুন</span>
                <span className="text-xs text-slate-400 font-mono">
                  (বাকি: {filteredEntries.length - visibleCount}টি)
                </span>
              </button>
            </div>
          )}

          {/* Sentinel for auto scroll trigger */}
          <div ref={sentinelRef} className="h-4 w-full" />
        </div>
      )}

      {/* 7. SPECIAL QUICK TOOLS MODAL / BOTTOM SHEET */}
      {showQuickToolsModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 bg-black/60 backdrop-blur-xs animate-fadeIn">
          <div 
            className="bg-white dark:bg-slate-900 w-full max-w-4xl max-h-[90vh] rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 flex flex-col overflow-hidden animate-slideUp"
            role="dialog"
            aria-modal="true"
          >
            {/* Modal Header */}
            <div className="p-4 sm:p-5 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3 bg-amber-500/10 dark:bg-amber-950/20">
              <div className="flex items-center gap-2.5">
                <div className="p-2 rounded-xl bg-amber-500 text-white shadow-xs">
                  <Zap className="w-5 h-5 fill-current" />
                </div>
                <div>
                  <h3 className="text-base sm:text-lg font-black text-slate-900 dark:text-white">
                    স্পেশাল কুইক টুলস ও নো-ক্যালকুলেটর ভল্ট
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400">
                    ভর্তি পরীক্ষায় ক্যালকুলেটর ছাড়া চোখের পলকে সমস্যা সমাধানের চার্ট
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setShowQuickToolsModal(false)}
                className="p-2 rounded-xl hover:bg-slate-200 dark:hover:bg-slate-800 text-slate-500 dark:text-slate-400 transition-colors cursor-pointer"
                title="বন্ধ করুন (ESC)"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Modal Tabs */}
            <div className="p-3 border-b border-slate-200 dark:border-slate-800 flex items-center gap-2 overflow-x-auto no-scrollbar bg-slate-50 dark:bg-slate-900/50">
              <button
                type="button"
                onClick={() => setQuickToolTab('triplets')}
                className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer ${
                  quickToolTab === 'triplets'
                    ? 'bg-amber-600 text-white shadow-xs'
                    : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                📐 পিথাগোরিয়ান ট্রিপলেট ({filteredTriplets.length})
              </button>
              <button
                type="button"
                onClick={() => setQuickToolTab('quick_math')}
                className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer ${
                  quickToolTab === 'quick_math'
                    ? 'bg-amber-600 text-white shadow-xs'
                    : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                ⚡ রুট ও লগ হ্যাক ({filteredQuickMath.length})
              </button>
              <button
                type="button"
                onClick={() => setQuickToolTab('fractions')}
                className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer ${
                  quickToolTab === 'fractions'
                    ? 'bg-amber-600 text-white shadow-xs'
                    : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                🧪 স্টয়কিওমেট্রি ফ্র্যাকশন ({filteredFractions.length})
              </button>
              <button
                type="button"
                onClick={() => setQuickToolTab('w4_bridge')}
                className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer ${
                  quickToolTab === 'w4_bridge'
                    ? 'bg-amber-600 text-white shadow-xs'
                    : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                🎯 Week 04 ব্রিজ
              </button>
              <button
                type="button"
                onClick={() => setQuickToolTab('w5_bridge')}
                className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer ${
                  quickToolTab === 'w5_bridge'
                    ? 'bg-amber-600 text-white shadow-xs'
                    : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                🔮 Week 05 ব্রিজ
              </button>
              <button
                type="button"
                onClick={() => setQuickToolTab('w6_bridge')}
                className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer ${
                  quickToolTab === 'w6_bridge'
                    ? 'bg-amber-600 text-white shadow-xs'
                    : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                🚀 Week 06 ব্রিজ
              </button>
              <button
                type="button"
                onClick={() => setQuickToolTab('w7_matrix')}
                className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shrink-0 transition-all cursor-pointer ${
                  quickToolTab === 'w7_matrix'
                    ? 'bg-amber-600 text-white shadow-xs'
                    : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                👑 Week 07 ব্রিজ
              </button>
            </div>

            {/* Modal Body */}
            <div className="p-4 sm:p-6 overflow-y-auto max-h-[60vh] space-y-4">
              {quickToolTab === 'triplets' && (
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                  {filteredTriplets.map((item, idx) => (
                    <div key={idx} className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60 flex flex-col justify-between">
                      <div>
                        <div className="flex items-center justify-between mb-1.5">
                          <span className="font-mono font-bold text-sm text-sky-700 dark:text-sky-400">{item.sides}</span>
                          <span className="px-2 py-0.5 rounded-full bg-sky-100 dark:bg-sky-950/50 text-sky-700 dark:text-sky-300 text-[11px] font-mono font-bold">
                            মান: {item.result}
                          </span>
                        </div>
                        <div className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                          <MathText content={item.app} />
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}

              {quickToolTab === 'quick_math' && (
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {filteredQuickMath.map((item, idx) => (
                    <div key={idx} className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60 flex items-center justify-between gap-3">
                      <div className="flex-1 text-xs sm:text-sm font-medium text-slate-800 dark:text-slate-200">
                        <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-amber-500/10 text-amber-700 dark:text-amber-400 mr-2">
                          {item.type}
                        </span>
                        <MathText content={item.item} />
                      </div>
                    </div>
                  ))}
                </div>
              )}

              {quickToolTab === 'fractions' && (
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                  {filteredFractions.map((item, idx) => (
                    <div key={idx} className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                      <div className="flex items-center justify-between mb-1.5">
                        <span className="font-bold text-xs sm:text-sm text-teal-700 dark:text-teal-400">
                          <MathText content={item.compound} />
                        </span>
                        <span className="font-mono text-xs px-2 py-0.5 rounded bg-slate-200/80 dark:bg-slate-700 text-slate-700 dark:text-slate-300 font-bold">
                          M: {item.mw}
                        </span>
                      </div>
                      <div className="text-xs text-slate-600 dark:text-slate-300">
                        <MathText content={item.trick} />
                      </div>
                    </div>
                  ))}
                </div>
              )}

              {quickToolTab === 'w4_bridge' && (
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-indigo-600 dark:text-indigo-400">হ্রদের গভীরতা হ্যাক (বুদ্বুদ)</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">১০.৩৩ মিটার</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="ব্যাস বা ব্যাসার্ধ $n$ গুণ হলে: $h = (n^3 - 1) \times 10.33\text{ m}$<br />আয়তন $n$ গুণ হলে: $h = (n - 1) \times 10.33\text{ m}$" />
                    </div>
                  </div>

                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-teal-600 dark:text-teal-400">সংকরায়ন দ্রুত গণনা</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">H মান</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="$H = \frac{1}{2}(V + M - C + A)$<br />$H=2 \implies sp, \quad H=3 \implies sp^2, \quad H=4 \implies sp^3, \quad H=5 \implies sp^3d$" />
                    </div>
                  </div>

                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-purple-600 dark:text-purple-400">কর্ণের সংখ্যা ও হাত মেলানো</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">nCr হ্যাক</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="কর্ণের সংখ্যা: $\frac{n(n-3)}{2}$ (১২ বাহুর কর্ণ = ৫৪টি)<br />করমর্দন সংখ্যা: $\frac{n(n-1)}{2}$ (১০ জনের করমর্দন = ৪৫টি)" />
                    </div>
                  </div>

                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-emerald-600 dark:text-emerald-400">মেন্ডেলের ব্যতিক্রম অনুপাত</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">জিনতত্ত্ব</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="পরিপূরক জিন: ৯:৭<br />এপিস্ট্যাসিস (প্রকট): ১২:৩:১<br />এপিস্ট্যাসিস (দ্বৈত প্রচ্ছন্ন): ৯:৭<br />লিথাল জিন: ২:১" />
                    </div>
                  </div>
                </div>
              )}

              {quickToolTab === 'w5_bridge' && (
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-indigo-600 dark:text-indigo-400">সরল ছন্দিত গতিতে শক্তি</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">সরণ x</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="$E_k = E_p \implies x = \pm \frac{A}{\sqrt{2}}$<br />$E_k = 3E_p \implies x = \pm \frac{A}{2}$<br />$E_p = 3E_k \implies x = \pm \frac{\sqrt{3}}{2}A$" />
                    </div>
                  </div>

                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-teal-600 dark:text-teal-400">ফ্যারাডের মানসিক গণনা</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">৯৬৫০০ কুলম্ব</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="$1\text{ F} = 96500\text{ C} \implies \text{দেয় } \frac{\text{মোলার ভর}}{\text{যোজ্যতা}}\text{ গ্রাম}$<br />$1\text{ F} \implies \text{Al}: 9\text{ g}, \quad \text{Cu}: 31.75\text{ g}, \quad \text{Ag}: 108\text{ g}$" />
                    </div>
                  </div>
                </div>
              )}

              {quickToolTab === 'w6_bridge' && (
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-indigo-600 dark:text-indigo-400">ত্রুটিপূর্ণ থার্মোমিটার হ্যাক</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">অনুপাত</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="$\frac{X - \text{ice}}{\text{steam} - \text{ice}} = \frac{C}{100}$<br />বরফ $4^\circ\text{C}$, বাষ্প $96^\circ\text{C}$ হলে ৫০ পাঠের সঠিক মান ঠিক $50^\circ\text{C}$!" />
                    </div>
                  </div>

                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-purple-600 dark:text-purple-400">লব হরের অন্তরক ইন্টিগ্রেশন</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">১ সেকেন্ড</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="$\int \frac{f'(x)}{f(x)} dx = \ln|f(x)| + c$<br />$\int \frac{f'(x)}{\sqrt{f(x)}} dx = 2\sqrt{f(x)} + c$" />
                    </div>
                  </div>
                </div>
              )}

              {quickToolTab === 'w7_matrix' && (
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-indigo-600 dark:text-indigo-400">ফটোইলেক্ট্রিক ১২৪০০ ফর্মুলা</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">eV মান</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="$E = \frac{12400}{\lambda(\text{\AA})}\text{ eV}$<br />নিবৃত্তি বিভব $V_s$ এর ভোল্ট মান সংখ্যাগতভাবে $K_{\max}(\text{eV})$ এর সমান!" />
                    </div>
                  </div>

                  <div className="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/60">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-bold text-xs text-teal-600 dark:text-teal-400">কার্বোক্যাটায়ন স্থায়িত্ব ক্রম</span>
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300">জৈব রসায়ন</span>
                    </div>
                    <div className="text-xs text-slate-600 dark:text-slate-300">
                      <MathText content="ক্যাটায়ন ও মুক্ত মূলক: $3^\circ > 2^\circ > 1^\circ > \text{CH}_3^+$<br />কার্বানায়ন: $\text{CH}_3^- > 1^\circ > 2^\circ > 3^\circ$" />
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* Modal Footer */}
            <div className="p-3.5 border-t border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900/50 flex justify-end">
              <button
                type="button"
                onClick={() => setShowQuickToolsModal(false)}
                className="px-4 py-2 rounded-xl bg-slate-800 dark:bg-slate-700 hover:bg-slate-900 text-white text-xs font-bold transition-all cursor-pointer shadow-xs active:scale-95"
              >
                বন্ধ করুন
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
};
