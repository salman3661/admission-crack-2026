import React, { useState, useRef, useEffect } from 'react';
import {
  GraduationCap,
  Sun,
  Moon,
  LogOut,
  Settings,
  Sparkles,
  Layers,
  Target,
  Bookmark as BookmarkIcon,
  User,
  RefreshCw,
} from 'lucide-react';
import {
  BANK_INDEX,
  LocalStorageAdapter,
  getSolvedQuestionsMap,
  getMockTracker,
  getBookmarks,
  type SourceType,
} from '../lib/library';
import type { AppMode, SubjectType, WeekFilterType, UserProfile, TrackType } from '../types';

interface NavbarProps {
  currentMode: AppMode;
  onSelectMode: (mode: AppMode) => void;
  onNavigate?: (path: string) => void;
  selectedWeek: WeekFilterType;
  onSelectWeek: (week: WeekFilterType) => void;
  selectedSubject: SubjectType;
  onSelectSubject: (subject: SubjectType) => void;
  theme: 'dark' | 'light';
  onToggleTheme: () => void;
  user: UserProfile;
  onOpenAuth: () => void;
  onLogout: () => void;
  activeTrack: TrackType;
  onSelectTrack: (track: TrackType) => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentMode,
  onSelectMode,
  onNavigate,
  selectedWeek,
  onSelectWeek,
  selectedSubject,
  onSelectSubject,
  theme,
  onToggleTheme,
  user,
  onOpenAuth,
  onLogout,
  activeTrack,
  onSelectTrack,
}) => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const [syncLabel, setSyncLabel] = useState('স্থানীয় (এই ডিভাইসে)');
  const dropdownRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setIsDropdownOpen(false);
      }
    };
    if (isDropdownOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [isDropdownOpen]);

  // Level 1: Week Selector Pills with runtime counts from BANK_INDEX.by_week
  const weeks: { id: WeekFilterType; label: string; count: number }[] = [
    {
      id: 'all',
      label: '📅 All',
      count: Object.values(BANK_INDEX.by_week || {}).reduce((a, b) => a + b, 0),
    },
    { id: 'week_01', label: 'Week 01', count: BANK_INDEX.by_week.week_01 || 0 },
    { id: 'week_02', label: 'Week 02', count: BANK_INDEX.by_week.week_02 || 0 },
    { id: 'week_03', label: 'Week 03', count: BANK_INDEX.by_week.week_03 || 0 },
    { id: 'week_04', label: 'Week 04', count: BANK_INDEX.by_week.week_04 || 0 },
    { id: 'week_05', label: 'Week 05', count: BANK_INDEX.by_week.week_05 || 0 },
    { id: 'week_06', label: 'Week 06', count: BANK_INDEX.by_week.week_06 || 0 },
    { id: 'week_07', label: 'Week 07', count: BANK_INDEX.by_week.week_07 || 0 },
    { id: 'week_08', label: 'Week 08', count: BANK_INDEX.by_week.week_08 || 0 },
    { id: 'week_09', label: 'Week 09', count: BANK_INDEX.by_week.week_09 || 0 },
  ];

  const subjects: { label: SubjectType; bn: string; icon: string }[] =
    activeTrack === 'medical'
      ? [
          { label: 'All', bn: 'সব বিষয়', icon: '🌐' },
          { label: 'Biology', bn: 'বায়োলজি', icon: '🧬' },
          { label: 'Chemistry', bn: 'কেমিস্ট্রি', icon: '🧪' },
          { label: 'Physics', bn: 'ফিজিক্স', icon: '⚛️' },
          { label: 'English', bn: 'ইংরেজি', icon: '🇬🇧' },
          { label: 'GK', bn: 'সাধারণ জ্ঞান', icon: '🇧🇩' },
          { label: 'ICT', bn: 'আইসিটি', icon: '💻' },
        ]
      : [
          { label: 'All', bn: 'সব বিষয়', icon: '🌐' },
          { label: 'Physics', bn: 'ফিজিক্স', icon: '⚛️' },
          { label: 'Chemistry', bn: 'কেমিস্ট্রি', icon: '🧪' },
          { label: 'Higher Math', bn: 'উচ্চতর গণিত', icon: '📐' },
          { label: 'Biology', bn: 'বায়োলজি', icon: '🧬' },
          { label: 'Bangla', bn: 'বাংলা', icon: '📖' },
          { label: 'English', bn: 'ইংরেজি', icon: '🇬🇧' },
          { label: 'GK', bn: 'সাধারণ জ্ঞান', icon: '🇧🇩' },
          { label: 'ICT', bn: 'আইসিটি', icon: '💻' },
        ];

  const showFilters =
    currentMode === 'weekly' ||
    currentMode === 'exam' ||
    currentMode === 'subject_final' ||
    currentMode === 'decks' ||
    currentMode === 'slides' ||
    currentMode === 'flashcards' ||
    currentMode === 'vault';

  // Fix 4: Dynamic Tier badge counts from BANK_INDEX.papers (hide when 0)
  const countByType = (t: SourceType) =>
    BANK_INDEX.papers
      .filter((p) => p.source_types.includes(t))
      .reduce((n, p) => n + p.count, 0);

  const weeklyCount = countByType('weekly_solve');
  const pfCount = countByType('paper_final');
  const sfCount = countByType('subject_final');
  const mtCount = countByType('model_test');

  // Account corner live progress stats
  const solvedCount = Object.keys(getSolvedQuestionsMap()).length;
  const mcqPct = BANK_INDEX.total_mcqs
    ? Math.min(100, Math.round((solvedCount / BANK_INDEX.total_mcqs) * 100))
    : 0;
  const writtenCount = (() => {
    try {
      const raw = localStorage.getItem('ac_written_drafts_v1');
      return raw ? Object.values(JSON.parse(raw)).filter((v) => String(v || '').trim()).length : 0;
    } catch {
      return 0;
    }
  })();
  const writtenPct = BANK_INDEX.total_written
    ? Math.min(100, Math.round((writtenCount / BANK_INDEX.total_written) * 100))
    : 0;
  const mocks = getMockTracker();
  const pfTaken = mocks.filter((m) => /paper\s*final|pf/i.test(m.name)).length;
  const sfTaken = mocks.filter((m) => /subject\s*final|sf/i.test(m.name)).length;
  const mtTaken = mocks.filter((m) => /model\s*test|mt/i.test(m.name)).length;
  const bmCount = getBookmarks().length;

  const handleSyncNow = async () => {
    const st = await LocalStorageAdapter.get();
    await LocalStorageAdapter.put(st);
    setSyncLabel('এইমাত্র সিঙ্ক হয়েছে (স্থানীয়)');
  };

  return (
    <header className="sticky top-0 z-40 backdrop-blur-xl bg-white/85 dark:bg-slate-950/85 border-b border-slate-200/80 dark:border-slate-800/80 transition-colors duration-200">
      {/* 1. TOP BAR */}
      <div className="max-w-6xl mx-auto px-3 sm:px-4 h-14 flex items-center justify-between gap-1.5 sm:gap-2">
        {/* Logo */}
        <div
          onClick={() => onSelectMode('decks')}
          className="flex items-center gap-2 cursor-pointer group select-none shrink-0"
        >
          <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-[#056839] via-[#00B09B] to-[#96C93D] p-0.5 shadow-sm shadow-emerald-600/20 group-hover:scale-105 transition-transform shrink-0">
            <div className="w-full h-full bg-white dark:bg-slate-900 rounded-[10px] flex items-center justify-center">
              <GraduationCap className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
            </div>
          </div>

          <div className="flex items-center gap-1.5">
            <span className="text-sm sm:text-base font-extrabold tracking-tight text-slate-900 dark:text-white font-['Outfit'] whitespace-nowrap">
              Admission Crack
            </span>
            <span className="px-1.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border border-emerald-500/20 font-['Outfit']">
              2026
            </span>
          </div>
        </div>

        {/* Center: Track Switcher & Quick Feature Pills */}
        <div className="flex items-center gap-1.5 shrink-0">
          <div className="flex items-center bg-slate-100/90 dark:bg-slate-800/90 p-1 rounded-2xl border border-slate-200/90 dark:border-slate-700/80 shadow-xs">
            <button
              onClick={() => onSelectTrack('varsity')}
              className={`px-2.5 sm:px-3 py-1 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer active:scale-95 ${
                activeTrack === 'varsity'
                  ? 'bg-gradient-to-r from-emerald-600 to-teal-600 text-white shadow-sm shadow-emerald-600/30 ring-1 ring-emerald-400/40'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
              title="ভার্সিটি 'ক' ট্র্যাক (DU 'Ka')"
            >
              <span className="w-2 h-2 rounded-full bg-emerald-300 animate-pulse" />
              <span className="hidden sm:inline">ভার্সিটি 'ক'</span>
              <span className="sm:hidden text-[11px]">ভার্সিটি</span>
            </button>
            <button
              onClick={() => onSelectTrack('medical')}
              className={`px-2.5 sm:px-3 py-1 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer active:scale-95 ${
                activeTrack === 'medical'
                  ? 'bg-gradient-to-r from-rose-600 to-red-600 text-white shadow-sm shadow-rose-600/30 ring-1 ring-rose-400/40'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
              title="মেডিকেল ট্র্যাক (MAT)"
            >
              <span className="w-2 h-2 rounded-full bg-rose-300 animate-pulse" />
              <span className="hidden sm:inline">মেডিকেল</span>
              <span className="sm:hidden text-[11px]">মেডি</span>
            </button>
          </div>

          <button
            onClick={() => (onNavigate ? onNavigate('/matcher') : onSelectMode('decks'))}
            className="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all border cursor-pointer active:scale-95 bg-indigo-500/10 dark:bg-indigo-950/30 text-indigo-700 dark:text-indigo-300 border-indigo-300/60 dark:border-indigo-800/60 hover:bg-indigo-500/20"
            title="প্রশ্ন ম্যাচার (F17)"
          >
            <Target className="w-3.5 h-3.5" />
            <span>প্রশ্ন ম্যাচার</span>
          </button>

          <button
            onClick={() => onSelectMode('blueprint')}
            className={`hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all border cursor-pointer active:scale-95 ${
              currentMode === 'blueprint'
                ? 'bg-emerald-600 text-white border-emerald-700 shadow-sm'
                : 'bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-300 border-emerald-300/60 dark:border-emerald-800/60 hover:bg-emerald-500/20'
            }`}
            title="অধ্যায় ও টপিক ড্রিল"
          >
            <Layers className="w-3.5 h-3.5" />
            <span>অধ্যায় ও টপিক</span>
          </button>

          <button
            onClick={() => onSelectMode('predictor')}
            className={`hidden lg:flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all border cursor-pointer active:scale-95 ${
              currentMode === 'predictor'
                ? 'bg-amber-500 text-white border-amber-600 shadow-sm'
                : 'bg-amber-500/10 dark:bg-amber-950/30 text-amber-700 dark:text-amber-400 border-amber-300/60 dark:border-amber-800/60 hover:bg-amber-500/20'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5 fill-current" />
            <span>Master Sets</span>
          </button>

          <button
            onClick={() => (onNavigate ? onNavigate('/bookmarks') : onSelectMode('decks'))}
            className="hidden lg:flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all border cursor-pointer active:scale-95 bg-amber-500/10 dark:bg-amber-950/30 text-amber-700 dark:text-amber-300 border-amber-300/60 dark:border-amber-800/60"
            title="বুকমার্ক (F19)"
          >
            <BookmarkIcon className="w-3.5 h-3.5" />
            <span>বুকমার্ক ({bmCount})</span>
          </button>
        </div>

        {/* Right Controls: Theme Toggle + F18 Account Corner Dropdown */}
        <div className="flex items-center gap-1.5 shrink-0">
          <button
            onClick={onToggleTheme}
            className="p-2 rounded-xl bg-slate-100/80 dark:bg-slate-800/80 text-slate-700 dark:text-amber-400 hover:text-slate-900 dark:hover:text-amber-300 ring-1 ring-slate-200/80 dark:ring-slate-700 transition-all shadow-xs active:scale-95 cursor-pointer"
            title={theme === 'dark' ? 'লাইট মোড চালু করুন' : 'ডার্ক মোড চালু করুন'}
            aria-label="Toggle Theme"
          >
            {theme === 'dark' ? (
              <Sun className="w-4 h-4 text-amber-400" />
            ) : (
              <Moon className="w-4 h-4 text-slate-700" />
            )}
          </button>

          {/* F18: Account Corner Button & Dropdown Panel */}
          <div className="relative" ref={dropdownRef}>
            <button
              onClick={() => setIsDropdownOpen((prev) => !prev)}
              className="flex items-center gap-1.5 py-1 px-2.5 rounded-full bg-slate-100/90 dark:bg-slate-800/90 ring-1 ring-slate-200 dark:ring-slate-700 hover:ring-[#056839] dark:hover:ring-emerald-500/50 transition-all shadow-xs active:scale-95 cursor-pointer"
              title="অ্যাকাউন্ট ও প্রগতি (F18)"
            >
              <div className="w-6 h-6 rounded-full bg-emerald-600 text-white flex items-center justify-center text-xs font-extrabold">
                <User className="w-3.5 h-3.5" />
              </div>
              <span className="text-xs font-bold text-slate-800 dark:text-slate-200 max-w-[75px] truncate">
                {user.name ? user.name.split(' ')[0] : 'সালমান'}
              </span>
            </button>

            {isDropdownOpen && (
              <div className="absolute right-0 top-full mt-2 w-80 backdrop-blur-2xl bg-white/95 dark:bg-slate-900/95 rounded-3xl shadow-2xl ring-1 ring-slate-200 dark:ring-slate-800 p-4 z-50 space-y-3 text-xs">
                <div className="flex items-center justify-between pb-2 border-b border-slate-200 dark:border-slate-800">
                  <div>
                    <div className="font-extrabold text-sm text-slate-900 dark:text-white">
                      👤 {user.name || 'সালমান'} · {activeTrack === 'medical' ? 'MAT ২০২৬' : "ঢাবি 'ক' ২০২৬"}
                    </div>
                    <div className="text-[11px] text-slate-500">টার্গেট ৭৮–৮০+ · ২৫ দিনের রোডম্যাপ</div>
                  </div>
                </div>

                {/* Progress Bars */}
                <div className="space-y-2">
                  <div className="font-bold text-slate-700 dark:text-slate-200">📊 অগ্রগতি</div>
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5">
                      <span>MCQ</span>
                      <span className="font-bold">
                        {mcqPct}% ({solvedCount}/{BANK_INDEX.total_mcqs})
                      </span>
                    </div>
                    <div className="h-1.5 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                      <div className="h-full bg-emerald-500 rounded-full" style={{ width: `${mcqPct}%` }} />
                    </div>
                  </div>
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5">
                      <span>Written</span>
                      <span className="font-bold">
                        {writtenPct}% ({writtenCount}/{BANK_INDEX.total_written})
                      </span>
                    </div>
                    <div className="h-1.5 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                      <div className="h-full bg-purple-500 rounded-full" style={{ width: `${writtenPct}%` }} />
                    </div>
                  </div>
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5">
                      <span>Mock</span>
                      <span className="font-bold">{mocks.length}/7</span>
                    </div>
                    <div className="h-1.5 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-teal-500 rounded-full"
                        style={{ width: `${Math.min(100, Math.round((mocks.length / 7) * 100))}%` }}
                      />
                    </div>
                  </div>
                </div>

                {/* Exam Breakdown */}
                <div className="p-2.5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/70 dark:border-slate-700/70 space-y-1 text-[11px]">
                  <div className="font-extrabold text-slate-800 dark:text-slate-200">
                    🗓 কতগুলো exam দিয়েছে: {mocks.length} টি
                  </div>
                  <div className="flex justify-between text-slate-600 dark:text-slate-300">
                    <span>Paper Final 1–10</span>
                    <span className="font-bold">{pfTaken}/10 দিয়েছে</span>
                  </div>
                  <div className="flex justify-between text-slate-600 dark:text-slate-300">
                    <span>Subject Final 4টি</span>
                    <span className="font-bold">{sfTaken}/4 দিয়েছে</span>
                  </div>
                  <div className="flex justify-between text-slate-600 dark:text-slate-300">
                    <span>Model Test 1–5</span>
                    <span className="font-bold">{mtTaken}/5 দিয়েছে</span>
                  </div>
                </div>

                {/* Sync Status */}
                <div className="flex items-center justify-between text-[11px] text-slate-600 dark:text-slate-300 pt-1">
                  <span>🔄 সিঙ্ক: {syncLabel}</span>
                  <button
                    onClick={handleSyncNow}
                    className="px-2 py-1 rounded-lg bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 font-bold flex items-center gap-1 cursor-pointer"
                  >
                    <RefreshCw className="w-3 h-3" /> এখনই সিঙ্ক
                  </button>
                </div>

                {/* Quick Links */}
                <div className="grid grid-cols-2 gap-1.5 pt-2 border-t border-slate-200 dark:border-slate-800">
                  <button
                    onClick={() => {
                      setIsDropdownOpen(false);
                      if (onNavigate) onNavigate('/account');
                    }}
                    className="py-2 px-3 rounded-xl bg-emerald-600 text-white font-bold text-center cursor-pointer"
                  >
                    পূর্ণ অ্যাকাউন্ট পেজ
                  </button>
                  <button
                    onClick={() => {
                      setIsDropdownOpen(false);
                      if (onNavigate) onNavigate('/bookmarks');
                    }}
                    className="py-2 px-3 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-bold text-center cursor-pointer"
                  >
                    🔖 বুকমার্ক ({bmCount})
                  </button>
                </div>

                <div className="flex items-center justify-between pt-1">
                  <button
                    onClick={() => {
                      setIsDropdownOpen(false);
                      onOpenAuth();
                    }}
                    className="text-[11px] font-semibold text-slate-600 dark:text-slate-300 hover:underline flex items-center gap-1 cursor-pointer"
                  >
                    <Settings className="w-3.5 h-3.5" /> Google প্রোফাইল সেটিংস
                  </button>
                  {user.isLoggedIn && (
                    <button
                      onClick={() => {
                        setIsDropdownOpen(false);
                        onLogout();
                      }}
                      className="text-[11px] font-bold text-rose-600 flex items-center gap-1 cursor-pointer"
                    >
                      <LogOut className="w-3.5 h-3.5" /> সাইন আউট
                    </button>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* 1.5. 4-TIER ADMISSION ARCHITECTURE NAVIGATION STRIP (Fix 4: dynamic counts, no false hardcoded badges) */}
      <div className="bg-slate-50/90 dark:bg-slate-900/90 border-t border-slate-200/80 dark:border-slate-800/80">
        <div className="max-w-6xl mx-auto px-3 sm:px-4 py-1.5 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
          {[
            {
              id: 'weekly' as AppMode,
              label: 'Tier 1: Weekly Mode',
              count: weeklyCount,
              activeCls: 'bg-emerald-600 text-white shadow-xs',
            },
            {
              id: 'paper_final' as AppMode,
              label: 'Tier 2: Paper Final',
              count: pfCount,
              activeCls: 'bg-indigo-600 text-white shadow-xs',
            },
            {
              id: 'subject_final' as AppMode,
              label: 'Tier 3: Subject Final',
              count: sfCount,
              activeCls: 'bg-teal-600 text-white shadow-xs',
            },
            {
              id: 'full_mock' as AppMode,
              label: 'Tier 4: Final Model Test',
              count: mtCount,
              activeCls: 'bg-rose-600 text-white shadow-xs',
            },
          ].map((tier) => {
            const isActive = currentMode === tier.id;
            return (
              <button
                key={tier.id}
                onClick={() => onSelectMode(tier.id)}
                className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all whitespace-nowrap shrink-0 flex items-center gap-1.5 cursor-pointer active:scale-95 ${
                  isActive
                    ? tier.activeCls
                    : 'bg-white/90 dark:bg-slate-800/90 text-slate-700 dark:text-slate-300 ring-1 ring-slate-200/80 dark:ring-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>{tier.label}</span>
                {tier.count > 0 && (
                  <span
                    className={`px-1.5 py-0.5 rounded-md text-[10px] font-black ${
                      isActive
                        ? 'bg-white/20 text-white'
                        : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300'
                    }`}
                  >
                    {tier.count}
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* 2. LEVEL 1: WEEK SELECTOR (WITH RUNTIME QUESTION COUNTS) */}
      {showFilters && (
        <div className="backdrop-blur-md bg-slate-50/80 dark:bg-slate-900/80 border-t border-b border-slate-200/80 dark:border-slate-800/80 animate-in fade-in duration-150">
          <div className="max-w-6xl mx-auto px-3 py-1.5 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
            <span className="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider shrink-0 mr-1">
              সপ্তাহ:
            </span>
            {weeks.map((w) => {
              const isActive = selectedWeek === w.id;
              return (
                <button
                  key={w.id}
                  onClick={() => {
                    onSelectWeek(w.id);
                    if (currentMode !== 'weekly' && w.id !== 'all') {
                      onSelectMode('weekly');
                    }
                  }}
                  className={`px-3 py-1 text-xs font-bold rounded-xl transition-all whitespace-nowrap shrink-0 cursor-pointer active:scale-95 flex items-center gap-1 ${
                    isActive
                      ? 'bg-[#056839] text-white shadow-xs'
                      : 'bg-white/80 dark:bg-slate-800/80 text-slate-600 dark:text-slate-400 ring-1 ring-slate-200/80 dark:ring-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                  }`}
                >
                  <span>{w.label}</span>
                  <span className={`text-[10px] ${isActive ? 'text-emerald-100' : 'text-slate-400'}`}>
                    ({w.count})
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* 3. SUBJECT SELECTOR */}
      {showFilters && (
        <div className="backdrop-blur-md bg-white/70 dark:bg-slate-950/70 border-b border-slate-200/80 dark:border-slate-800/80 animate-in fade-in duration-150">
          <div className="max-w-6xl mx-auto px-3 py-1.5 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
            <span className="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider shrink-0 mr-1">
              বিষয়:
            </span>
            {subjects.map((subj) => {
              const isActive = selectedSubject === subj.label;
              return (
                <button
                  key={subj.label}
                  onClick={() => {
                    onSelectSubject(subj.label);
                    if (currentMode === 'decks' && subj.label !== 'All') {
                      onSelectMode('exam');
                    }
                  }}
                  className={`px-3 py-1 text-xs font-semibold rounded-xl transition-all whitespace-nowrap shrink-0 flex items-center gap-1.5 cursor-pointer active:scale-95 ${
                    isActive
                      ? 'bg-emerald-600/15 text-emerald-800 dark:text-emerald-300 ring-1 ring-emerald-500/40 font-bold shadow-xs'
                      : 'bg-slate-100/70 dark:bg-slate-800/70 text-slate-600 dark:text-slate-400 ring-1 ring-slate-200/80 dark:ring-slate-700 hover:bg-slate-200/60 dark:hover:bg-slate-700'
                  }`}
                >
                  <span>{subj.icon}</span>
                  <span>{subj.bn}</span>
                </button>
              );
            })}
          </div>
        </div>
      )}
    </header>
  );
};
