import React, { useState, useMemo, useEffect, useRef } from 'react';
import { 
  Search, 
  Copy, 
  Check, 
  ShieldAlert, 
  Sparkles, 
  X,
  ChevronDown,
  ChevronUp,
  BookOpen,
  Zap
} from 'lucide-react';
import type { VaultData, VaultEntry, SubjectType, WeekFilterType } from '../types';
import { MathText } from './MathText';

interface VaultViewProps {
  vault: VaultData;
  selectedWeek?: WeekFilterType;
  selectedSubject?: SubjectType;
}

type ActiveSubject = 'All' | 'Physics' | 'Chemistry' | 'Higher Math' | 'Biology' | 'English' | 'GK';
type ActiveCardType = 'all' | 'core_formula' | 'shortcut' | 'trap';

const SUBJECT_OPTIONS: { id: ActiveSubject; label: string; icon: string }[] = [
  { id: 'All', label: 'সব বিষয়', icon: '🌟' },
  { id: 'Physics', label: 'পদার্থবিজ্ঞান', icon: '⚛️' },
  { id: 'Chemistry', label: 'রসায়ন', icon: '🧪' },
  { id: 'Higher Math', label: 'উচ্চতর গণিত', icon: '📐' },
  { id: 'Biology', label: 'জীববিজ্ঞান', icon: '🧬' },
  { id: 'English', label: 'ইংরেজি', icon: '🇬🇧' },
  { id: 'GK', label: 'সাধারণ জ্ঞান', icon: '🇧🇩' },
];

export const VaultView: React.FC<VaultViewProps> = ({ 
  vault, 
  selectedWeek: _selectedWeek = 'all', 
  selectedSubject: propSubject = 'All' 
}) => {
  void _selectedWeek;
  const [searchQuery, setSearchQuery] = useState('');
  const [activeSubject, setActiveSubject] = useState<ActiveSubject>(
    propSubject !== 'All' ? propSubject : 'All'
  );

  // Sync with propSubject changes when navigating from Decks or Navbar
  useEffect(() => {
    if (propSubject) {
      setActiveSubject(propSubject);
      setSelectedChapter('all');
    }
  }, [propSubject]);
  const [selectedChapter, setSelectedChapter] = useState<string>('all');
  const [selectedCardType, setSelectedCardType] = useState<ActiveCardType>('all');
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [expandedChapters, setExpandedChapters] = useState<Record<string, boolean>>({});
  const [showQuickTools, setShowQuickTools] = useState(true);
  const [quickToolTab, setQuickToolTab] = useState<'triplets' | 'quick_math' | 'fractions'>('triplets');
  const [displayLimit, setDisplayLimit] = useState(20);
  const sentinelRef = useRef<HTMLDivElement | null>(null);

  const entries: VaultEntry[] = useMemo(() => vault.entries || [], [vault.entries]);

  const copyToClipboard = (id: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleSubjectChange = (subject: ActiveSubject) => {
    setActiveSubject(subject);
    setSelectedChapter('all');
  };

  // Derive available chapters based on selected subject
  const availableChapters = useMemo(() => {
    const relevant = activeSubject === 'All'
      ? entries
      : entries.filter((e) => e.subject === activeSubject);
    
    const chapterMap = new Map<string, number>();
    relevant.forEach((e) => {
      const count = chapterMap.get(e.chapter) || 0;
      chapterMap.set(e.chapter, count + 1);
    });

    return Array.from(chapterMap.entries()).map(([chapter, count]) => ({
      name: chapter,
      count
    }));
  }, [entries, activeSubject]);

  // Filter entries based on Subject, Chapter, Card Type, and Search Query
  const filteredEntries = useMemo(() => {
    const q = searchQuery.toLowerCase().trim();

    return entries.filter((item) => {
      // Subject filter
      if (activeSubject !== 'All' && item.subject !== activeSubject) return false;

      // Chapter filter
      if (selectedChapter !== 'all' && item.chapter !== selectedChapter) return false;

      // Card Type filter
      if (selectedCardType !== 'all' && item.type !== selectedCardType) return false;

      // Search Query filter
      if (q) {
        const inTitle = item.title?.toLowerCase().includes(q) ?? false;
        const inFormula = item.formula?.toLowerCase().includes(q) ?? false;
        const inConcept = item.concept?.toLowerCase().includes(q) ?? false;
        const inHack = item.hack?.toLowerCase().includes(q) ?? false;
        const inTrap = item.trap?.toLowerCase().includes(q) ?? false;
        const inChapter = item.chapter?.toLowerCase().includes(q) ?? false;
        const inTags = item.tags ? item.tags.some((t) => t.toLowerCase().includes(q)) : false;
        if (!inTitle && !inFormula && !inConcept && !inHack && !inTrap && !inChapter && !inTags) {
          return false;
        }
      }

      return true;
    });
  }, [entries, activeSubject, selectedChapter, selectedCardType, searchQuery]);

  // Reset display limit on filter/search change
  useEffect(() => {
    setDisplayLimit(20);
  }, [searchQuery, activeSubject, selectedChapter, selectedCardType]);

  // Infinite scroll trigger
  useEffect(() => {
    if (!sentinelRef.current) return;
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          setDisplayLimit((prev) => {
            if (prev < filteredEntries.length) return prev + 20;
            return prev;
          });
        }
      },
      { rootMargin: '200px' }
    );
    observer.observe(sentinelRef.current);
    return () => observer.disconnect();
  }, [filteredEntries.length]);

  // Sliced entries for mobile DOM performance (shows full when filtered)
  const displayedEntries = useMemo(() => {
    if (selectedChapter !== 'all' || selectedCardType !== 'all' || searchQuery) {
      return filteredEntries;
    }
    return filteredEntries.slice(0, displayLimit);
  }, [filteredEntries, displayLimit, selectedChapter, selectedCardType, searchQuery]);

  // Group sliced entries by chapter
  const groupedByChapter = useMemo(() => {
    const map = new Map<string, VaultEntry[]>();
    displayedEntries.forEach((item) => {
      const list = map.get(item.chapter) || [];
      list.push(item);
      map.set(item.chapter, list);
    });
    return map;
  }, [displayedEntries]);

  // Counts for Card Types
  const typeCounts = useMemo(() => {
    const subjectScoped = activeSubject === 'All'
      ? entries
      : entries.filter((e) => e.subject === activeSubject);
    const chapterScoped = selectedChapter === 'all'
      ? subjectScoped
      : subjectScoped.filter((e) => e.chapter === selectedChapter);

    return {
      all: chapterScoped.length,
      core_formula: chapterScoped.filter((e) => e.type === 'core_formula').length,
      shortcut: chapterScoped.filter((e) => e.type === 'shortcut').length,
      trap: chapterScoped.filter((e) => e.type === 'trap').length,
    };
  }, [entries, activeSubject, selectedChapter]);

  const toggleChapter = (chapter: string) => {
    setExpandedChapters((prev) => ({
      ...prev,
      [chapter]: prev[chapter] === undefined ? false : !prev[chapter]
    }));
  };

  const isChapterExpanded = (chapter: string) => {
    if (selectedChapter !== 'all' && selectedChapter === chapter) return true;
    return expandedChapters[chapter] !== false; // Default to expanded
  };

  // Legacy quick tools filter
  const q = searchQuery.toLowerCase().trim();
  const filteredTriplets = (vault.triplets || []).filter((t) => 
    (!q || t.sides.toLowerCase().includes(q) || t.result.toLowerCase().includes(q) || t.app.toLowerCase().includes(q))
  );
  const filteredQuickMath = (vault.quick_math || []).filter((m) =>
    (!q || m.type.toLowerCase().includes(q) || m.item.toLowerCase().includes(q))
  );
  const filteredFractions = (vault.magic_fractions || []).filter((f) =>
    (!q || f.compound.toLowerCase().includes(q) || f.mw.toLowerCase().includes(q) || f.trick.toLowerCase().includes(q))
  );

  return (
    <div className="max-w-5xl mx-auto py-5 px-3 sm:px-5">
      
      {/* 1. HEADER & SEARCH */}
      <div className="mb-6">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-3 mb-4">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <span className="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 flex items-center gap-1">
                <Sparkles className="w-3 h-3 text-[#056839] dark:text-emerald-400" />
                অ্যাডমিশন ফর্মুলা ও ট্র্যাপ ভল্ট
              </span>
              <span className="text-xs font-mono font-bold text-zinc-500 dark:text-zinc-400">
                {entries.length}টি এন্ট্রি • ২৯টি অধ্যায়
              </span>
            </div>
            <h1 className="text-xl sm:text-2xl font-black text-zinc-900 dark:text-white tracking-tight">
              চ্যাপ্টারওয়াইজ ফর্মুলা, হ্যাক ও নেগেটিভ মার্কিং ট্র্যাপ
            </h1>
          </div>

          {/* Quick Tools Toggle Button */}
          <button
            onClick={() => setShowQuickTools(!showQuickTools)}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-xl text-xs font-bold transition-all border shrink-0 ${
              showQuickTools
                ? 'bg-amber-500 text-white border-amber-600 shadow-sm'
                : 'bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 border-zinc-200/80 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-800'
            }`}
          >
            <Zap className="w-3.5 h-3.5" />
            <span>স্পেশাল টুলস (Triplets & Roots)</span>
          </button>
        </div>

        {/* Real-time Search Bar */}
        <div className="relative mb-4">
          <Search className="w-4 h-4 text-zinc-400 absolute left-3.5 top-3.5 pointer-events-none" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="সূত্র, শর্টকাট, অধ্যায় বা ট্র্যাপ দিয়ে সাথে সাথে খুঁজুন (e.g. লব্ধি, pH, দ্বিপদী, ট্রিপলেট)..."
            className="w-full bg-white dark:bg-zinc-900 border border-zinc-200/90 dark:border-zinc-800 rounded-2xl pl-10 pr-9 py-2.5 text-xs sm:text-sm text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-[#056839] focus:ring-2 focus:ring-[#056839]/20 transition-all shadow-sm"
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery('')}
              className="absolute right-3.5 top-3 text-zinc-400 hover:text-zinc-700 dark:hover:text-white transition-colors"
              title="মুছে ফেলুন"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>

        {/* 2. SUBJECT FILTER PILLS */}
        <div className="mb-3">
          <div className="text-[11px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500 mb-2">
            বিষয় নির্বাচন করুন
          </div>
          <div className="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1">
            {SUBJECT_OPTIONS.map((sub) => {
              const isActive = activeSubject === sub.id;
              const subCount = sub.id === 'All' 
                ? entries.length 
                : entries.filter((e) => e.subject === sub.id).length;
              return (
                <button
                  key={sub.id}
                  onClick={() => handleSubjectChange(sub.id)}
                  className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold transition-all whitespace-nowrap shrink-0 shadow-xs cursor-pointer ${
                    isActive
                      ? 'bg-[#056839] text-white scale-[1.02] ring-2 ring-[#056839]/30'
                      : 'bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 border border-zinc-200/80 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                  }`}
                >
                  <span>{sub.icon}</span>
                  <span>{sub.label}</span>
                  <span className={`text-[10px] font-mono px-1.5 py-0.2 rounded-full font-bold ${
                    isActive ? 'bg-white/20 text-white' : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-500'
                  }`}>
                    {subCount}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* 3. CHAPTER SELECTOR PILLS */}
        {availableChapters.length > 0 && (
          <div className="mb-3">
            <div className="text-[11px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500 mb-2">
              অধ্যায় ফিল্টার ({availableChapters.length}টি অধ্যায়)
            </div>
            <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-1">
              <button
                onClick={() => setSelectedChapter('all')}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap shrink-0 transition-all cursor-pointer ${
                  selectedChapter === 'all'
                    ? 'bg-emerald-600 text-white font-bold shadow-xs'
                    : 'bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 border border-zinc-200/80 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                }`}
              >
                <span>সব অধ্যায়</span>
                <span className="text-[10px] font-mono opacity-80">
                  ({typeCounts.all})
                </span>
              </button>

              {availableChapters.map((chap) => {
                const isActive = selectedChapter === chap.name;
                return (
                  <button
                    key={chap.name}
                    onClick={() => setSelectedChapter(chap.name)}
                    className={`flex items-center gap-1 px-3 py-1.5 rounded-xl text-xs whitespace-nowrap shrink-0 transition-all cursor-pointer ${
                      isActive
                        ? 'bg-emerald-600 text-white font-bold shadow-xs'
                        : 'bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 border border-zinc-200/80 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                    }`}
                  >
                    <span>{chap.name}</span>
                    <span className="text-[10px] font-mono opacity-70">
                      ({chap.count})
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* 4. CARD TYPE TABS */}
        <div className="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1 border-b border-zinc-200/70 dark:border-zinc-800/80 pt-1">
          <button
            onClick={() => setSelectedCardType('all')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all border-b-2 cursor-pointer ${
              selectedCardType === 'all'
                ? 'border-[#056839] text-[#056839] dark:text-emerald-400 bg-[#056839]/5'
                : 'border-transparent text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200'
            }`}
          >
            <span>🌐 সব ধরণ</span>
            <span className="text-[10px] font-mono px-1.5 py-0.2 rounded-full bg-zinc-100 dark:bg-zinc-800">
              {typeCounts.all}
            </span>
          </button>

          <button
            onClick={() => setSelectedCardType('core_formula')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all border-b-2 cursor-pointer ${
              selectedCardType === 'core_formula'
                ? 'border-indigo-600 text-indigo-600 dark:text-indigo-400 bg-indigo-50/50 dark:bg-indigo-950/20'
                : 'border-transparent text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200'
            }`}
          >
            <span>📐 কোর সূত্রাবলী</span>
            <span className="text-[10px] font-mono px-1.5 py-0.2 rounded-full bg-zinc-100 dark:bg-zinc-800">
              {typeCounts.core_formula}
            </span>
          </button>

          <button
            onClick={() => setSelectedCardType('shortcut')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all border-b-2 cursor-pointer ${
              selectedCardType === 'shortcut'
                ? 'border-amber-500 text-amber-600 dark:text-amber-400 bg-amber-50/50 dark:bg-amber-950/20'
                : 'border-transparent text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200'
            }`}
          >
            <span>⚡ নো-ক্যালকুলেটর শর্টকাট</span>
            <span className="text-[10px] font-mono px-1.5 py-0.2 rounded-full bg-zinc-100 dark:bg-zinc-800">
              {typeCounts.shortcut}
            </span>
          </button>

          <button
            onClick={() => setSelectedCardType('trap')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all border-b-2 cursor-pointer ${
              selectedCardType === 'trap'
                ? 'border-rose-600 text-rose-600 dark:text-rose-400 bg-rose-50/50 dark:bg-rose-950/20'
                : 'border-transparent text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200'
            }`}
          >
            <span>⚠️ ট্র্যাপ এলার্ট</span>
            <span className="text-[10px] font-mono px-1.5 py-0.2 rounded-full bg-zinc-100 dark:bg-zinc-800">
              {typeCounts.trap}
            </span>
          </button>
        </div>
      </div>

      {/* 5. SPECIAL QUICK TOOLS SECTION (Triplets, Roots & Fractions) */}
      {showQuickTools && (
        <div className="mb-6 p-4 rounded-3xl bg-amber-50/50 dark:bg-amber-950/20 border border-amber-200/80 dark:border-amber-900/40 shadow-sm animate-fadeIn">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-2">
              <Zap className="w-4 h-4 text-amber-600 dark:text-amber-400" />
              <h3 className="text-sm font-bold text-amber-900 dark:text-amber-200">
                স্পেশাল কুইক টুলস ও নো-ক্যালকুলেটর টেবিল
              </h3>
            </div>
            <div className="flex items-center gap-1">
              <button
                onClick={() => setQuickToolTab('triplets')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-colors ${
                  quickToolTab === 'triplets'
                    ? 'bg-amber-600 text-white'
                    : 'bg-white dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300'
                }`}
              >
                📐 পিথাগোরিয়ান ট্রিপলেট ({filteredTriplets.length})
              </button>
              <button
                onClick={() => setQuickToolTab('quick_math')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-colors ${
                  quickToolTab === 'quick_math'
                    ? 'bg-amber-600 text-white'
                    : 'bg-white dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300'
                }`}
              >
                ⚡ রুট ও লগ হ্যাক ({filteredQuickMath.length})
              </button>
              <button
                onClick={() => setQuickToolTab('fractions')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-colors ${
                  quickToolTab === 'fractions'
                    ? 'bg-amber-600 text-white'
                    : 'bg-white dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300'
                }`}
              >
                🧪 স্টয়কিওমেট্রি ফ্র্যাকশন ({filteredFractions.length})
              </button>
            </div>
          </div>

          {quickToolTab === 'triplets' && (
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5">
              {filteredTriplets.map((item, idx) => (
                <div key={idx} className="bg-white dark:bg-zinc-900 rounded-2xl p-3 border border-amber-200/60 dark:border-amber-900/30 shadow-xs flex flex-col justify-between">
                  <div>
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-mono font-bold text-xs text-cyan-700 dark:text-cyan-400">{item.sides}</span>
                      <span className="px-2 py-0.5 rounded-full bg-cyan-50 dark:bg-cyan-950/30 text-cyan-700 dark:text-cyan-400 text-[10px] font-mono font-bold">
                        মান: {item.result}
                      </span>
                    </div>
                    <div className="text-[11px] text-zinc-600 dark:text-zinc-400">
                      <MathText content={item.app} />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}

          {quickToolTab === 'quick_math' && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
              {filteredQuickMath.map((item, idx) => (
                <div key={idx} className="bg-white dark:bg-zinc-900 rounded-2xl p-3 border border-amber-200/60 dark:border-amber-900/30 shadow-xs flex items-center justify-between gap-2">
                  <div className="flex-1 text-xs font-medium text-zinc-800 dark:text-zinc-200">
                    <span className="text-[10px] font-bold px-1.5 py-0.5 rounded-md bg-amber-500/10 text-amber-700 dark:text-amber-400 mr-1.5">
                      {item.type}
                    </span>
                    <MathText content={item.item} />
                  </div>
                </div>
              ))}
            </div>
          )}

          {quickToolTab === 'fractions' && (
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5">
              {filteredFractions.map((item, idx) => (
                <div key={idx} className="bg-white dark:bg-zinc-900 rounded-2xl p-3 border border-amber-200/60 dark:border-amber-900/30 shadow-xs">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-xs text-emerald-700 dark:text-emerald-400">
                      <MathText content={item.compound} />
                    </span>
                    <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-300">
                      M = {item.mw}
                    </span>
                  </div>
                  <div className="text-[11px] text-zinc-600 dark:text-zinc-400">
                    <MathText content={item.trick} />
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* 6. MAIN CONTENT: CHAPTER ACCORDION / LIST */}
      {filteredEntries.length === 0 ? (
        <div className="py-16 text-center max-w-md mx-auto px-4 bg-white dark:bg-zinc-900 rounded-3xl border border-zinc-200/80 dark:border-zinc-800 shadow-sm">
          <BookOpen className="w-10 h-10 text-zinc-400 dark:text-zinc-600 mx-auto mb-2 animate-bounce" />
          <h3 className="text-base font-bold text-zinc-800 dark:text-zinc-200">কোনো সূত্র বা ট্র্যাপ পাওয়া যায়নি</h3>
          <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-1 mb-4">
            আপনার ফিল্টার বা সার্চ কীওয়ার্ডের সাথে মিলছে না। ফিল্টার পরিবর্তন করে আবার চেষ্টা করুন।
          </p>
          <button
            onClick={() => {
              setSearchQuery('');
              setActiveSubject('All');
              setSelectedChapter('all');
              setSelectedCardType('all');
            }}
            className="px-4 py-2 rounded-xl bg-[#056839] text-white text-xs font-bold hover:bg-[#044e2b] transition-all shadow-xs"
          >
            ফিল্টার রিসেট করুন
          </button>
        </div>
      ) : (
        <div className="space-y-6">
          {/* Active Filter Bar & Card Counter */}
          <div className="bg-white dark:bg-zinc-900 px-4 py-3 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 flex items-center justify-between gap-3 flex-wrap shadow-xs">
            <div className="flex items-center gap-2 flex-wrap text-xs font-semibold text-zinc-600 dark:text-zinc-400">
              <span>ফিল্টার করা মোট কার্ড:</span>
              <span className="font-extrabold text-[#056839] dark:text-emerald-400 font-mono text-sm">
                {filteredEntries.length}টি
              </span>
              {selectedChapter !== 'all' && (
                <span className="px-2.5 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/40 text-[#056839] dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800 text-[11px] font-bold flex items-center gap-1">
                  <span>অধ্যায়:</span> {selectedChapter}
                  <button 
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
                  <span>ধরণ:</span> 
                  {selectedCardType === 'core_formula' ? 'কোর সূত্রাবলী' : selectedCardType === 'shortcut' ? 'নো-ক্যালকুলেটর শর্টকাট' : 'ট্র্যাপ এলার্ট'}
                  <button 
                    onClick={() => setSelectedCardType('all')} 
                    className="ml-1 hover:text-rose-600 cursor-pointer text-xs"
                    title="ধরণ ফিল্টার মুছুন"
                  >
                    ×
                  </button>
                </span>
              )}
            </div>

            {(selectedChapter !== 'all' || selectedCardType !== 'all' || activeSubject !== 'All' || searchQuery) && (
              <button
                onClick={() => {
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
          {Array.from(groupedByChapter.entries()).map(([chapterName, chapterEntries]) => {
            const isExpanded = isChapterExpanded(chapterName);
            const chapterSubject = chapterEntries[0]?.subject || activeSubject;

            return (
              <div 
                key={chapterName}
                className="bg-white dark:bg-zinc-900 rounded-3xl border border-zinc-200/80 dark:border-zinc-800 shadow-sm overflow-hidden transition-all"
              >
                {/* Chapter Header / Accordion Trigger */}
                <div 
                  onClick={() => toggleChapter(chapterName)}
                  className="p-4 sm:p-5 flex items-center justify-between cursor-pointer hover:bg-zinc-50/70 dark:hover:bg-zinc-800/40 border-b border-zinc-100 dark:border-zinc-800/80 transition-colors select-none"
                >
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold text-sm shrink-0">
                      {chapterSubject === 'Physics' ? '⚛️' : chapterSubject === 'Chemistry' ? '🧪' : chapterSubject === 'Higher Math' ? '📐' : chapterSubject === 'Biology' ? '🧬' : chapterSubject === 'English' ? '🇬🇧' : '🇧🇩'}
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <h2 className="text-sm sm:text-base font-extrabold text-zinc-900 dark:text-white">
                          {chapterName}
                        </h2>
                        <span className="text-[11px] font-semibold text-zinc-400">
                          ({chapterEntries.length}টি কার্ড)
                        </span>
                      </div>
                      <div className="text-[11px] text-zinc-500 dark:text-zinc-400 flex items-center gap-2 mt-0.5">
                        <span>{chapterSubject}</span>
                        <span>•</span>
                        <span>
                          {chapterEntries.filter(e => e.type === 'core_formula').length} সূত্র
                        </span>
                        <span>•</span>
                        <span>
                          {chapterEntries.filter(e => e.type === 'shortcut').length} শর্টকাট
                        </span>
                        <span>•</span>
                        <span className="text-rose-500 font-medium">
                          {chapterEntries.filter(e => e.type === 'trap').length} ট্র্যাপ
                        </span>
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    <span className="text-xs font-semibold text-zinc-400 hidden sm:inline">
                      {isExpanded ? 'সংকুচিত করুন' : 'বিস্তৃত করুন'}
                    </span>
                    <div className="p-1.5 rounded-lg bg-zinc-100 dark:bg-zinc-800 text-zinc-500">
                      {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                    </div>
                  </div>
                </div>

                {/* Chapter Cards Grid */}
                {isExpanded && (
                  <div className="p-4 sm:p-5 grid grid-cols-1 md:grid-cols-2 gap-4">
                    {chapterEntries.map((item) => {
                      const isTrap = item.type === 'trap';
                      const isShortcut = item.type === 'shortcut';
                      const isCopied = copiedId === item.id;

                      return (
                        <div
                          key={item.id}
                          className={`rounded-2xl p-4 sm:p-5 border transition-all flex flex-col justify-between shadow-xs hover:shadow-md ${
                            isTrap
                              ? 'bg-rose-50/20 dark:bg-rose-950/10 border-rose-200/80 dark:border-rose-900/30'
                              : isShortcut
                              ? 'bg-amber-50/15 dark:bg-amber-950/10 border-amber-200/70 dark:border-amber-900/30'
                              : 'bg-white dark:bg-zinc-900/90 border-zinc-200/80 dark:border-zinc-800'
                          }`}
                        >
                          <div>
                            {/* Card Top: Badges + Copy */}
                            <div className="flex items-center justify-between mb-2.5 gap-2">
                              <div className="flex items-center gap-1.5 flex-wrap">
                                {item.type === 'core_formula' && (
                                  <span className="text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-700 dark:text-indigo-300 border border-indigo-500/20 flex items-center gap-1">
                                    <span>📐</span> কোর সূত্র
                                  </span>
                                )}
                                {item.type === 'shortcut' && (
                                  <span className="text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-amber-500/10 text-amber-700 dark:text-amber-400 border border-amber-500/20 flex items-center gap-1">
                                    <Zap className="w-3 h-3 text-amber-500" /> ৫-সেকেন্ড হ্যাক
                                  </span>
                                )}
                                {item.type === 'trap' && (
                                  <span className="text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-rose-500/10 text-rose-700 dark:text-rose-400 border border-rose-500/20 flex items-center gap-1">
                                    <ShieldAlert className="w-3 h-3 text-rose-500" /> নেগেটিভ ট্র্যাপ
                                  </span>
                                )}
                                <span className="text-[10px] font-medium text-zinc-400">
                                  #{item.id}
                                </span>
                              </div>

                              <button
                                onClick={() => copyToClipboard(item.id, `${item.title}\n${item.formula}\n${item.concept}`)}
                                className="flex items-center gap-1 text-[11px] font-medium text-zinc-400 hover:text-zinc-800 dark:hover:text-white transition-colors p-1 rounded-md hover:bg-zinc-100 dark:hover:bg-zinc-800"
                                title="কপি করুন"
                              >
                                {isCopied ? (
                                  <span className="flex items-center gap-1 text-emerald-600 font-bold">
                                    <Check className="w-3.5 h-3.5" /> কপি হয়েছে
                                  </span>
                                ) : (
                                  <span className="flex items-center gap-1">
                                    <Copy className="w-3.5 h-3.5" /> কপি
                                  </span>
                                )}
                              </button>
                            </div>

                            {/* Card Title */}
                            <h3 className="text-sm font-extrabold text-zinc-900 dark:text-white mb-2 leading-snug">
                              {item.title}
                            </h3>

                            {/* Formula Box (High-priority display with Crisp Solid White Math Contrast) */}
                            {item.formula && (
                              <div className="my-3 bg-zinc-950 dark:bg-black text-white border border-zinc-800 p-4 rounded-2xl font-mono text-xs sm:text-sm overflow-x-auto no-scrollbar shadow-inner formula-container math-renderer">
                                <MathText content={item.formula} block className="text-white" />
                              </div>
                            )}

                            {/* Core Concept Box */}
                            {item.concept && (
                              <div className="text-xs text-zinc-700 dark:text-zinc-300 leading-relaxed mb-2.5">
                                <strong className="text-zinc-900 dark:text-white font-bold block mb-0.5">
                                  💡 মূল ধারণা:
                                </strong>
                                <MathText content={item.concept} />
                              </div>
                            )}

                            {/* Shortcut / 5-Second Hack Box */}
                            {item.hack && (
                              <div className="bg-amber-500/10 dark:bg-amber-950/30 p-2.5 rounded-xl border border-amber-500/20 text-xs text-amber-900 dark:text-amber-200 leading-relaxed mb-2 overflow-x-auto no-scrollbar">
                                <strong className="text-amber-700 dark:text-amber-400 font-bold flex items-center gap-1 mb-0.5">
                                  <Zap className="w-3 h-3 text-amber-500" /> ৫-সেকেন্ড হ্যাক:
                                </strong>
                                <MathText content={item.hack} />
                              </div>
                            )}

                            {/* Negative Marking Trap Box */}
                            {item.trap && (
                              <div className="bg-rose-500/10 dark:bg-rose-950/30 p-2.5 rounded-xl border border-rose-500/20 text-xs text-rose-900 dark:text-rose-200 leading-relaxed mb-2 overflow-x-auto no-scrollbar">
                                <strong className="text-rose-700 dark:text-rose-400 font-bold flex items-center gap-1 mb-0.5">
                                  <ShieldAlert className="w-3.5 h-3.5 text-rose-500" /> যেখানে ভুল হয় (Trap Alert):
                                </strong>
                                <MathText content={item.trap} />
                              </div>
                            )}
                          </div>

                          {/* Card Footer: Tags */}
                          {item.tags && item.tags.length > 0 && (
                            <div className="flex items-center gap-1.5 flex-wrap pt-2.5 mt-2 border-t border-zinc-100 dark:border-zinc-800/80">
                              {item.tags.map((tag, tIdx) => (
                                <span
                                  key={tIdx}
                                  onClick={() => setSearchQuery(tag)}
                                  className="text-[10px] font-medium px-2 py-0.5 rounded-md bg-zinc-100 dark:bg-zinc-800 text-zinc-500 hover:text-zinc-900 dark:hover:text-white cursor-pointer transition-colors"
                                >
                                  #{tag}
                                </span>
                              ))}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}

          {/* Smooth Pagination / Lazy Loading Trigger for Mobile Instant Performance */}
          {filteredEntries.length > displayLimit && (
            <div className="pt-4 pb-2 text-center">
              <button
                onClick={() => setDisplayLimit((prev) => prev + 20)}
                className="w-full py-3.5 px-4 rounded-2xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-slate-800 text-sm font-bold text-[#056839] dark:text-emerald-400 hover:bg-slate-50 dark:hover:bg-zinc-800 shadow-sm flex items-center justify-center gap-2 cursor-pointer transition-all active:scale-[0.99]"
              >
                <span>আরও ২০টি কার্ড লোড করুন ▾</span>
                <span className="text-xs text-zinc-400 font-mono">({Math.min(displayLimit, filteredEntries.length)} / {filteredEntries.length} প্রদর্শিত)</span>
              </button>
            </div>
          )}

          {/* Sentinel for infinite scroll trigger */}
          <div ref={sentinelRef} className="h-4 w-full" />
        </div>
      )}

    </div>
  );
};
