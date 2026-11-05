import React, { useState, useRef, useEffect } from 'react';
import { 
  GraduationCap, 
  Sun, 
  Moon, 
  Flame, 
  LogOut, 
  Settings,
  Sparkles
} from 'lucide-react';
import type { AppMode, SubjectType, WeekFilterType, UserProfile, TrackType } from '../types';

interface NavbarProps {
  currentMode: AppMode;
  onSelectMode: (mode: AppMode) => void;
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
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Close dropdown on click outside
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

  // Level 1: Week Selector Pills
  const weeks: { id: WeekFilterType; label: string }[] = [
    { id: 'all', label: '📅 All' },
    { id: 'week_01', label: '1️⃣ Week 01' },
    { id: 'week_02', label: '2️⃣ Week 02' },
    { id: 'week_03', label: '3️⃣ Week 03' },
  ];

  // Subject Selector Horizontal Slider - Strictly isolated by Track
  const subjects: { label: SubjectType; bn: string; icon: string }[] = activeTrack === 'medical'
    ? [
        { label: 'All', bn: 'সব বিষয়', icon: '🌐' },
        { label: 'Biology', bn: 'বায়োলজি', icon: '🧬' },
        { label: 'Chemistry', bn: 'কেমিস্ট্রি', icon: '🧪' },
        { label: 'Physics', bn: 'ফিজিক্স', icon: '⚛️' },
        { label: 'English', bn: 'ইংরেজি', icon: '🇬🇧' },
        { label: 'GK', bn: 'সাধারণ জ্ঞান', icon: '🇧🇩' },
      ]
    : [
        { label: 'All', bn: 'সব বিষয়', icon: '🌐' },
        { label: 'Physics', bn: 'ফিজিক্স', icon: '⚛️' },
        { label: 'Chemistry', bn: 'কেমিস্ট্রি', icon: '🧪' },
        { label: 'Higher Math', bn: 'উচ্চতর গণিত', icon: '📐' },
        { label: 'Biology', bn: 'বায়োলজি', icon: '🧬' },
      ];

  // Condition: Only show Weekly filter and Subject pills when inside "প্রশ্নব্যাংক" or "ডেক" (or "slides")
  // Automatically hidden inside "প্রেডিকশন", "ভল্ট", "অ্যানালিটিক্স"
  const showFilters = currentMode === 'exam' || currentMode === 'decks' || currentMode === 'slides';

  return (
    <header className="sticky top-0 z-40 backdrop-blur-none md:backdrop-blur-md bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 transition-colors duration-200">
      
      {/* 1. TOP BAR (COMPACT H-14, SINGLE-LINE ALIGNED) */}
      <div className="max-w-6xl mx-auto px-3 sm:px-4 h-14 flex items-center justify-between gap-1.5 sm:gap-2">
        
        {/* Logo & 2026 Badge (Clicking opens Home Decks) */}
        <div 
          onClick={() => onSelectMode('decks')}
          className="flex items-center gap-1.5 cursor-pointer group select-none shrink-0"
        >
          <div className="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-gradient-to-tr from-[#056839] via-[#00B09B] to-[#96C93D] p-0.5 shadow-sm group-hover:scale-105 transition-transform shrink-0">
            <div className="w-full h-full bg-white dark:bg-slate-900 rounded-[9px] sm:rounded-[10px] flex items-center justify-center">
              <GraduationCap className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-[#056839] dark:text-emerald-400" />
            </div>
          </div>
          
          <div className="flex items-center gap-1">
            <span className="text-xs sm:text-base font-extrabold tracking-tight text-slate-900 dark:text-white font-['Outfit'] whitespace-nowrap">
              Admission Crack
            </span>
            <span className="hidden sm:inline-block px-1.5 py-0.5 rounded-full text-[10px] sm:text-[11px] font-black bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 font-['Outfit']">
              2026
            </span>
          </div>
        </div>

        {/* Center: Track Switcher & Predictor Vault Pill */}
        <div className="flex items-center gap-1.5 shrink-0">
          {/* Track Switcher */}
          <div className="flex items-center bg-slate-100 dark:bg-slate-800 p-0.5 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-xs">
            <button
              onClick={() => onSelectTrack('varsity')}
              className={`px-2 sm:px-2.5 py-1 rounded-xl text-xs font-bold transition-all flex items-center gap-1 cursor-pointer ${
                activeTrack === 'varsity'
                  ? 'bg-blue-600 text-white shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
              title="ভার্সিটি 'ক' ট্র্যাক"
            >
              <span>🎯</span>
              <span className="hidden sm:inline">ভার্সিটি 'ক'</span>
              <span className="sm:hidden text-[11px]">ভার্সিটি</span>
            </button>
            <button
              onClick={() => onSelectTrack('medical')}
              className={`px-2 sm:px-2.5 py-1 rounded-xl text-xs font-bold transition-all flex items-center gap-1 cursor-pointer ${
                activeTrack === 'medical'
                  ? 'bg-rose-600 text-white shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
              title="মেডিকেল ট্র্যাক"
            >
              <span>🩺</span>
              <span className="hidden sm:inline">মেডিকেল</span>
              <span className="sm:hidden text-[11px]">মেডি</span>
            </button>
          </div>

          {/* Quick Predictor Vault Button */}
          <button
            onClick={() => onSelectMode('predictor')}
            className={`hidden md:flex items-center gap-1.5 px-3 py-1 rounded-xl text-xs font-bold transition-all border cursor-pointer ${
              currentMode === 'predictor'
                ? 'bg-amber-500 text-white border-amber-600 shadow-sm'
                : 'bg-amber-50 dark:bg-amber-950/30 text-amber-700 dark:text-amber-400 border-amber-200 dark:border-amber-800/60 hover:bg-amber-100'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5 fill-current" />
            <span>প্রেডিকশন ভল্ট</span>
          </button>
        </div>

        {/* Right Controls: Theme Toggle + User Avatar with Dropdown */}
        <div className="flex items-center gap-1.5 shrink-0">
          
          {/* Theme Toggle Button */}
          <button
            onClick={onToggleTheme}
            className="p-1.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-amber-400 hover:text-slate-900 dark:hover:text-amber-300 border border-slate-200 dark:border-slate-700 transition-all shadow-sm active:scale-95 cursor-pointer"
            title={theme === 'dark' ? 'লাইট মোড চালু করুন' : 'ডার্ক মোড চালু করুন'}
            aria-label="Toggle Theme"
          >
            {theme === 'dark' ? (
              <Sun className="w-4 h-4 text-amber-400" />
            ) : (
              <Moon className="w-4 h-4 text-slate-700" />
            )}
          </button>

          {/* User Profile Avatar with Dropdown */}
          {user.isLoggedIn ? (
            <div className="relative" ref={dropdownRef}>
              <button
                onClick={() => setIsDropdownOpen((prev) => !prev)}
                className="flex items-center gap-1 p-1 pr-2 rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:border-[#056839] dark:hover:border-emerald-500/50 transition-all shadow-sm active:scale-95 cursor-pointer"
                title="প্রোফাইল মেনু"
              >
                <div className="relative">
                  <img
                    src={user.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(user.email || 'user')}`}
                    alt={user.name}
                    className="w-6 h-6 rounded-full object-cover ring-1 ring-[#056839]"
                  />
                  <span className="absolute bottom-0 right-0 w-1.5 h-1.5 rounded-full bg-emerald-500 ring-1 ring-white dark:ring-slate-900" />
                </div>
                <span className="text-xs font-bold text-slate-800 dark:text-slate-200 max-w-[55px] sm:max-w-[70px] truncate">
                  {user.name.split(' ')[0] || 'শিক্ষার্থী'}
                </span>
                {user.streakDays > 0 && (
                  <span className="hidden sm:inline-flex items-center gap-0.5 text-[10px] font-bold text-amber-500 font-mono">
                    <Flame className="w-3 h-3 fill-current" />
                    {user.streakDays}d
                  </span>
                )}
              </button>

              {/* Clean Sign Out Dropdown Menu */}
              {isDropdownOpen && (
                <div className="absolute right-0 top-full mt-2 w-64 bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 p-3 z-50 animate-in fade-in zoom-in-95 duration-150">
                  <div className="flex items-center gap-3 p-2 bg-slate-50 dark:bg-slate-800/60 rounded-xl mb-2 border border-slate-200/60 dark:border-slate-700/60">
                    <img
                      src={user.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(user.email || 'user')}`}
                      alt={user.name}
                      className="w-10 h-10 rounded-xl object-cover ring-1 ring-[#056839]"
                    />
                    <div className="overflow-hidden flex-1">
                      <div className="text-xs font-bold text-slate-900 dark:text-white truncate">
                        {user.name}
                      </div>
                      <div className="text-[11px] text-slate-500 dark:text-slate-400 truncate">
                        {user.email}
                      </div>
                    </div>
                  </div>

                  <div className="px-2 py-1 mb-2">
                    <div className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider">টার্গেট</div>
                    <div className="text-xs font-bold text-[#056839] dark:text-emerald-400 truncate">
                      {user.target}
                    </div>
                  </div>

                  <div className="h-px bg-slate-200 dark:bg-slate-800 my-1" />

                  <button
                    onClick={() => {
                      setIsDropdownOpen(false);
                      onOpenAuth();
                    }}
                    className="w-full px-3 py-2 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl flex items-center gap-2 transition-colors text-left cursor-pointer"
                  >
                    <Settings className="w-4 h-4 text-slate-500" />
                    <span>প্রোফাইল সেটিংস</span>
                  </button>

                  <button
                    onClick={() => {
                      setIsDropdownOpen(false);
                      onLogout();
                    }}
                    className="w-full px-3 py-2 text-xs font-bold text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 rounded-xl flex items-center gap-2 transition-colors text-left cursor-pointer"
                  >
                    <LogOut className="w-4 h-4" />
                    <span>সাইন আউট (Sign Out)</span>
                  </button>
                </div>
              )}
            </div>
          ) : (
            <button
              onClick={onOpenAuth}
              className="py-1 px-2.5 rounded-full bg-white dark:bg-slate-800 hover:bg-slate-50 dark:hover:bg-slate-700 border border-slate-300 dark:border-slate-700 text-slate-800 dark:text-white text-xs font-bold shadow-sm flex items-center gap-1.5 transition-all active:scale-95 cursor-pointer"
              title="Google দিয়ে সাইন ইন করুন"
            >
              <svg className="w-3.5 h-3.5" viewBox="0 0 24 24">
                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
              </svg>
              <span className="hidden xs:inline">Google</span>
              <span>লগইন</span>
            </button>
          )}
        </div>
      </div>

      {/* 2. LEVEL 1: WEEK SELECTOR (ONLY SHOWN INSIDE "প্রশ্নব্যাংক" OR "ডেক") */}
      {showFilters && (
        <div className="bg-slate-50 dark:bg-slate-900/90 border-t border-b border-slate-200 dark:border-slate-800 animate-in fade-in duration-150">
          <div className="max-w-6xl mx-auto px-3 py-1 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
            <span className="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider shrink-0 mr-1">
              সপ্তাহ:
            </span>
            {weeks.map((w) => {
              const isActive = selectedWeek === w.id;
              return (
                <button
                  key={w.id}
                  onClick={() => onSelectWeek(w.id)}
                  className={`px-3 py-1 text-xs font-bold rounded-full transition-all whitespace-nowrap shrink-0 cursor-pointer ${
                    isActive
                      ? 'bg-[#056839] text-white shadow-sm'
                      : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                  }`}
                >
                  {w.label}
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* 3. SUBJECT SELECTOR (ONLY SHOWN INSIDE "প্রশ্নব্যাংক" OR "ডেক") */}
      {showFilters && (
        <div className="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 animate-in fade-in duration-150">
          <div className="max-w-6xl mx-auto px-3 py-1 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
            <span className="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider shrink-0 mr-1">
              বিষয়:
            </span>
            {subjects.map((subj) => {
              const isActive = selectedSubject === subj.label;
              return (
                <button
                  key={subj.label}
                  onClick={() => onSelectSubject(subj.label)}
                  className={`px-3 py-1 text-xs font-semibold rounded-full transition-all whitespace-nowrap shrink-0 flex items-center gap-1 cursor-pointer ${
                    isActive
                      ? 'bg-emerald-600/15 text-emerald-800 dark:text-emerald-300 border border-emerald-500/40 font-bold'
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-700 hover:bg-slate-200/60 dark:hover:bg-slate-700'
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
