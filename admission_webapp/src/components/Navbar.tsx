import React, { useState, useRef, useEffect } from 'react';
import { 
  GraduationCap, 
  Sun, 
  Moon, 
  Flame, 
  LogOut, 
  Clock, 
  Home, 
  Sparkles,
  Zap,
  Layers,
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

  const weeks: { id: WeekFilterType; label: string }[] = [
    { id: 'all', label: 'All Weeks' },
    { id: 'week_01', label: 'Week 01' },
    { id: 'week_02', label: 'Week 02' },
    { id: 'week_03', label: 'Week 03' },
  ];

  const subjects: { label: SubjectType; bn: string }[] = [
    { label: 'All', bn: 'সব বিষয়' },
    { label: 'Physics', bn: 'পদার্থবিজ্ঞান' },
    { label: 'Chemistry', bn: 'রসায়ন' },
    { label: 'Higher Math', bn: 'উচ্চতর গণিত' },
    { label: 'Biology', bn: 'জীববিজ্ঞান' },
  ];

  return (
    <header className="sticky top-0 z-40 backdrop-blur-md bg-white/95 dark:bg-[#0D1410]/95 border-b border-slate-200/80 dark:border-[#1E2F24] transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-3 sm:px-6">
        
        {/* ROW 1: Ultra-Compact Single Row Header */}
        <div className="flex items-center justify-between h-14 gap-3">
          
          {/* Logo & '2026' Badge */}
          <div 
            onClick={() => onSelectMode('decks')}
            className="flex items-center gap-2.5 cursor-pointer group select-none shrink-0"
          >
            <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-[#056839] via-[#00B09B] to-[#96C93D] p-0.5 shadow-sm group-hover:scale-105 transition-transform">
              <div className="w-full h-full bg-white dark:bg-[#131E17] rounded-[10px] flex items-center justify-center">
                <GraduationCap className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
              </div>
            </div>
            
            <div className="flex items-center gap-2">
              <span className="text-base font-extrabold tracking-tight text-slate-900 dark:text-white font-['Outfit']">
                Admission Crack
              </span>
              <span className="px-2 py-0.5 rounded-full text-[11px] font-black bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 font-['Outfit']">
                2026
              </span>
            </div>
          </div>

          {/* Right Controls: Dark Mode Toggle + User Avatar with Sign Out Dropdown */}
          <div className="flex items-center gap-2 shrink-0">
            
            {/* Theme Toggle Button */}
            <button
              onClick={onToggleTheme}
              className="p-2 rounded-full bg-[#F6F8F6] dark:bg-[#1A261F] text-slate-700 dark:text-amber-400 hover:text-slate-900 dark:hover:text-amber-300 border border-slate-200 dark:border-[#1E2F24] transition-all shadow-sm active:scale-95"
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
                  className="flex items-center gap-2 p-1 pr-2.5 rounded-full bg-[#F6F8F6] dark:bg-[#1A261F] border border-slate-200 dark:border-[#223328] hover:border-[#056839] dark:hover:border-emerald-500/50 transition-all shadow-sm active:scale-95"
                  title="প্রোফাইল মেনু"
                >
                  <div className="relative">
                    <img
                      src={user.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(user.email || 'user')}`}
                      alt={user.name}
                      className="w-7 h-7 rounded-full object-cover ring-1 ring-[#056839]"
                    />
                    <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-emerald-500 ring-1 ring-white dark:ring-[#131E17]" />
                  </div>
                  <span className="text-xs font-bold text-slate-800 dark:text-white max-w-[70px] sm:max-w-none truncate">
                    {user.name.split(' ')[0] || 'শিক্ষার্থী'}
                  </span>
                  {user.streakDays > 0 && (
                    <span className="hidden sm:inline-flex items-center gap-0.5 text-[11px] font-bold text-amber-500 font-mono">
                      <Flame className="w-3 h-3 fill-current" />
                      {user.streakDays}d
                    </span>
                  )}
                </button>

                {/* Clean Sign Out Dropdown Menu */}
                {isDropdownOpen && (
                  <div className="absolute right-0 top-full mt-2 w-64 bg-white dark:bg-[#131E17] rounded-2xl shadow-2xl border border-slate-200/90 dark:border-[#1E2F24] p-3 z-50 animate-in fade-in zoom-in-95 duration-150">
                    <div className="flex items-center gap-3 p-2 bg-[#F6F8F6] dark:bg-[#1A261F] rounded-xl mb-2.5 border border-slate-200/60 dark:border-[#24352A]">
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

                    <div className="h-px bg-slate-200 dark:bg-[#1E2F24] my-1" />

                    <button
                      onClick={() => {
                        setIsDropdownOpen(false);
                        onOpenAuth();
                      }}
                      className="w-full px-3 py-2 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-[#1A261F] rounded-xl flex items-center gap-2 transition-colors text-left"
                    >
                      <Settings className="w-4 h-4 text-slate-500" />
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
                className="py-1.5 px-3 rounded-full bg-white dark:bg-[#1A261F] hover:bg-slate-50 dark:hover:bg-[#223429] border border-slate-300 dark:border-[#283C2F] text-slate-800 dark:text-white text-xs font-bold shadow-sm flex items-center gap-1.5 transition-all active:scale-95"
                title="Google দিয়ে সাইন ইন করুন"
              >
                <svg className="w-4 h-4" viewBox="0 0 24 24">
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

        {/* ROW 2: Compact Filter Bar (Mode Tabs + Weekly Pills + Subject Pills) */}
        <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-2 border-t border-slate-200/70 dark:border-[#1E2F24]">
          
          {/* Chorcha Primary Mode Pills */}
          <button
            onClick={() => onSelectMode('decks')}
            className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold transition-all whitespace-nowrap shrink-0 ${
              currentMode === 'decks'
                ? 'bg-[#056839] text-white shadow-sm'
                : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
            }`}
          >
            <Home className="w-3.5 h-3.5" />
            <span>ডেক</span>
          </button>

          <button
            onClick={() => onSelectMode('exam')}
            className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold transition-all whitespace-nowrap shrink-0 ${
              currentMode === 'exam'
                ? 'bg-[#056839] text-white shadow-sm'
                : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
            }`}
          >
            <Clock className="w-3.5 h-3.5" />
            <span>মডেল টেস্ট</span>
          </button>

          <button
            onClick={() => onSelectMode('slides')}
            className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold transition-all whitespace-nowrap shrink-0 ${
              currentMode === 'slides'
                ? 'bg-[#056839] text-white shadow-sm'
                : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>স্লাইডস</span>
          </button>

          <button
            onClick={() => onSelectMode('vault')}
            className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold transition-all whitespace-nowrap shrink-0 ${
              currentMode === 'vault'
                ? 'bg-[#056839] text-white shadow-sm'
                : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
            }`}
          >
            <Zap className="w-3.5 h-3.5 text-amber-500" />
            <span>শর্টকাট ভল্ট</span>
          </button>

          {/* Vertical Separator */}
          <div className="h-4 w-px bg-slate-300 dark:bg-[#1E2F24] shrink-0 mx-1" />

          {/* Weekly Filter Pills */}
          <span className="text-[11px] font-semibold text-slate-400 shrink-0 flex items-center gap-1 pl-1">
            <Layers className="w-3 h-3" /> সপ্তাহ:
          </span>
          {weeks.map((w) => (
            <button
              key={w.id}
              onClick={() => onSelectWeek(w.id)}
              className={`px-2.5 py-1 text-xs font-semibold rounded-full transition-all whitespace-nowrap shrink-0 ${
                selectedWeek === w.id
                  ? 'bg-[#056839] text-white shadow-sm'
                  : 'bg-white dark:bg-[#131E17] text-slate-600 dark:text-slate-400 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
              }`}
            >
              {w.label}
            </button>
          ))}

          {/* Subject Filter Pills (Visible when in exam, slides, or flashcards) */}
          {currentMode !== 'vault' && currentMode !== 'analytics' && (
            <>
              <div className="h-4 w-px bg-slate-300 dark:bg-[#1E2F24] shrink-0 mx-1" />
              {subjects.map((subj) => {
                const active = selectedSubject === subj.label;
                return (
                  <button
                    key={subj.label}
                    onClick={() => onSelectSubject(subj.label)}
                    className={`px-2.5 py-1 text-xs font-semibold rounded-full transition-all whitespace-nowrap shrink-0 ${
                      active
                        ? 'bg-[#056839] text-white shadow-sm'
                        : 'bg-white dark:bg-[#131E17] text-slate-600 dark:text-slate-400 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
                    }`}
                  >
                    {subj.bn}
                  </button>
                );
              })}
            </>
          )}
        </div>
      </div>
    </header>
  );
};
