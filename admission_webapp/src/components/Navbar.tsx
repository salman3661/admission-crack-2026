import React, { useState, useRef, useEffect } from 'react';
import { 
  GraduationCap, 
  Sun, 
  Moon, 
  Flame, 
  LogOut, 
  Settings
} from 'lucide-react';
import type { AppMode, SubjectType, WeekFilterType, UserProfile } from '../types';

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

  // Subject Selector Horizontal Slider
  const subjects: { label: SubjectType; bn: string; icon: string }[] = [
    { label: 'All', bn: 'সব বিষয়', icon: '🌐' },
    { label: 'Physics', bn: 'ফিজিক্স', icon: '⚛️' },
    { label: 'Chemistry', bn: 'কেমিস্ট্রি', icon: '🧪' },
    { label: 'Higher Math', bn: 'ম্যাথ', icon: '📐' },
    { label: 'Biology', bn: 'বায়োলজি', icon: '🧬' },
  ];

  // Level 2: Section / Category Submenu
  const categories: { id: AppMode; label: string }[] = [
    { id: 'slides', label: '⚡ কোর ফর্মুলা' },
    { id: 'flashcards', label: '💡 শর্টকাট ভল্ট' },
    { id: 'vault', label: '⚠️ ট্র্যাপ ক্যাপসুল' },
    { id: 'exam', label: '📝 মডেল টেস্ট' },
  ];

  return (
    <header className="sticky top-0 z-40 backdrop-blur-md bg-white/95 dark:bg-[#0D1410]/95 border-b border-zinc-200/80 dark:border-zinc-800 transition-colors duration-200">
      
      {/* 1. TOP BAR (MINIMALIST) */}
      <div className="max-w-6xl mx-auto px-4 h-13 flex items-center justify-between">
        
        {/* Logo & 2026 Badge (No dummy text) */}
        <div 
          onClick={() => onSelectMode('slides')}
          className="flex items-center gap-2 cursor-pointer group select-none"
        >
          <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-[#056839] via-[#00B09B] to-[#96C93D] p-0.5 shadow-sm group-hover:scale-105 transition-transform">
            <div className="w-full h-full bg-white dark:bg-zinc-900 rounded-[10px] flex items-center justify-center">
              <GraduationCap className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
            </div>
          </div>
          
          <div className="flex items-center gap-1.5">
            <span className="text-base font-extrabold tracking-tight text-zinc-900 dark:text-white font-['Outfit']">
              Admission Crack
            </span>
            <span className="px-2 py-0.5 rounded-full text-[11px] font-black bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 font-['Outfit']">
              2026
            </span>
          </div>
        </div>

        {/* Right Controls: Theme Toggle + User Avatar with Dropdown */}
        <div className="flex items-center gap-2 shrink-0">
          
          {/* Theme Toggle Button */}
          <button
            onClick={onToggleTheme}
            className="p-1.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-amber-400 hover:text-zinc-900 dark:hover:text-amber-300 border border-zinc-200 dark:border-zinc-700 transition-all shadow-sm active:scale-95"
            title={theme === 'dark' ? 'লাইট মোড চালু করুন' : 'ডার্ক মোড চালু করুন'}
            aria-label="Toggle Theme"
          >
            {theme === 'dark' ? (
              <Sun className="w-4 h-4 text-amber-400" />
            ) : (
              <Moon className="w-4 h-4 text-zinc-700" />
            )}
          </button>

          {/* User Profile Avatar with Dropdown */}
          {user.isLoggedIn ? (
            <div className="relative" ref={dropdownRef}>
              <button
                onClick={() => setIsDropdownOpen((prev) => !prev)}
                className="flex items-center gap-1.5 p-1 pr-2 rounded-full bg-zinc-100 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 hover:border-[#056839] dark:hover:border-emerald-500/50 transition-all shadow-sm active:scale-95"
                title="প্রোফাইল মেনু"
              >
                <div className="relative">
                  <img
                    src={user.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(user.email || 'user')}`}
                    alt={user.name}
                    className="w-6 h-6 rounded-full object-cover ring-1 ring-[#056839]"
                  />
                  <span className="absolute bottom-0 right-0 w-1.5 h-1.5 rounded-full bg-emerald-500 ring-1 ring-white dark:ring-zinc-900" />
                </div>
                <span className="text-xs font-bold text-zinc-800 dark:text-zinc-200 max-w-[65px] truncate">
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
                <div className="absolute right-0 top-full mt-2 w-64 bg-white dark:bg-zinc-900 rounded-2xl shadow-2xl border border-zinc-200 dark:border-zinc-800 p-3 z-50 animate-in fade-in zoom-in-95 duration-150">
                  <div className="flex items-center gap-3 p-2 bg-zinc-50 dark:bg-zinc-800/60 rounded-xl mb-2 border border-zinc-200/60 dark:border-zinc-700/60">
                    <img
                      src={user.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(user.email || 'user')}`}
                      alt={user.name}
                      className="w-10 h-10 rounded-xl object-cover ring-1 ring-[#056839]"
                    />
                    <div className="overflow-hidden flex-1">
                      <div className="text-xs font-bold text-zinc-900 dark:text-white truncate">
                        {user.name}
                      </div>
                      <div className="text-[11px] text-zinc-500 dark:text-zinc-400 truncate">
                        {user.email}
                      </div>
                    </div>
                  </div>

                  <div className="px-2 py-1 mb-2">
                    <div className="text-[10px] font-semibold text-zinc-400 uppercase tracking-wider">টার্গেট</div>
                    <div className="text-xs font-bold text-[#056839] dark:text-emerald-400 truncate">
                      {user.target}
                    </div>
                  </div>

                  <div className="h-px bg-zinc-200 dark:bg-zinc-800 my-1" />

                  <button
                    onClick={() => {
                      setIsDropdownOpen(false);
                      onOpenAuth();
                    }}
                    className="w-full px-3 py-2 text-xs font-semibold text-zinc-700 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 rounded-xl flex items-center gap-2 transition-colors text-left"
                  >
                    <Settings className="w-4 h-4 text-zinc-500" />
                    <span>প্রোফাইল সেটিংস</span>
                  </button>

                  <button
                    onClick={() => {
                      setIsDropdownOpen(false);
                      onLogout();
                    }}
                    className="w-full px-3 py-2 text-xs font-bold text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 rounded-xl flex items-center gap-2 transition-colors text-left"
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
              className="py-1 px-2.5 rounded-full bg-white dark:bg-zinc-900 hover:bg-zinc-50 dark:hover:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 text-zinc-800 dark:text-white text-xs font-bold shadow-sm flex items-center gap-1.5 transition-all active:scale-95"
              title="Google দিয়ে সাইন ইন করুন"
            >
              <svg className="w-3.5 h-3.5" viewBox="0 0 24 24">
                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
              </svg>
              <span>Google লগইন</span>
            </button>
          )}
        </div>
      </div>

      {/* 2. LEVEL 1: WEEK SELECTOR (HORIZONTAL SLICK PILLS) */}
      <div className="bg-zinc-50/70 dark:bg-zinc-950/40 border-t border-b border-zinc-200/60 dark:border-zinc-800/60">
        <div className="max-w-6xl mx-auto px-3 py-1 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
          <span className="text-[11px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-wider shrink-0 mr-1">
            সপ্তাহ:
          </span>
          {weeks.map((w) => {
            const isActive = selectedWeek === w.id;
            return (
              <button
                key={w.id}
                onClick={() => onSelectWeek(w.id)}
                className={`px-3 py-1 text-xs font-bold rounded-full transition-all whitespace-nowrap shrink-0 ${
                  isActive
                    ? 'bg-[#056839] text-white shadow-sm scale-[1.02]'
                    : 'bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                }`}
              >
                {w.label}
              </button>
            );
          })}
        </div>
      </div>

      {/* 3. SUBJECT SELECTOR (CLEAN HORIZONTAL SLIDER) */}
      <div className="bg-white/80 dark:bg-zinc-950/60 border-b border-zinc-200/60 dark:border-zinc-800/60">
        <div className="max-w-6xl mx-auto px-3 py-1 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
          <span className="text-[11px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-wider shrink-0 mr-1">
            বিষয়:
          </span>
          {subjects.map((subj) => {
            const isActive = selectedSubject === subj.label;
            return (
              <button
                key={subj.label}
                onClick={() => onSelectSubject(subj.label)}
                className={`px-3 py-1 text-xs font-semibold rounded-full transition-all whitespace-nowrap shrink-0 flex items-center gap-1 ${
                  isActive
                    ? 'bg-emerald-600/15 text-emerald-800 dark:text-emerald-300 border border-emerald-500/40 font-bold'
                    : 'bg-zinc-100/80 dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 border border-zinc-200/80 dark:border-zinc-800 hover:bg-zinc-200/60 dark:hover:bg-zinc-800'
                }`}
              >
                <span>{subj.icon}</span>
                <span>{subj.bn}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* 4. LEVEL 2: SECTION / CATEGORY SUBMENU */}
      <div className="bg-white dark:bg-zinc-950">
        <div className="max-w-6xl mx-auto px-3 py-1.5 flex items-center gap-2 overflow-x-auto no-scrollbar">
          {categories.map((cat) => {
            const isActive = currentMode === cat.id;
            return (
              <button
                key={cat.id}
                onClick={() => onSelectMode(cat.id)}
                className={`px-3.5 py-1.5 text-xs font-bold rounded-xl transition-all whitespace-nowrap shrink-0 ${
                  isActive
                    ? 'bg-[#056839] text-white shadow-sm scale-[1.02]'
                    : 'bg-zinc-100 dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 border border-zinc-200/80 dark:border-zinc-800 hover:bg-zinc-200/80 dark:hover:bg-zinc-800'
                }`}
              >
                {cat.label}
              </button>
            );
          })}
        </div>
      </div>

    </header>
  );
};
