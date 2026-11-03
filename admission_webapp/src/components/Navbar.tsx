import React from 'react';
import { 
  GraduationCap, 
  Layers, 
  Sun, 
  Moon, 
  Flame, 
  Clock, 
  Zap, 
  Home, 
  Sparkles
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
}) => {
  const subjects: { label: SubjectType; bn: string }[] = [
    { label: 'All', bn: 'সব বিষয়' },
    { label: 'Physics', bn: 'পদার্থবিজ্ঞান' },
    { label: 'Chemistry', bn: 'রসায়ন' },
    { label: 'Higher Math', bn: 'উচ্চতর গণিত' },
    { label: 'Biology', bn: 'জীববিজ্ঞান' },
  ];

  return (
    <header className="sticky top-0 z-40 backdrop-blur-md bg-white/95 dark:bg-[#0D1410]/95 border-b border-slate-200/80 dark:border-[#1E2F24] transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Top Branding & Auth Row */}
        <div className="flex items-center justify-between py-3 gap-3">
          
          {/* Logo & Platform Name */}
          <div 
            onClick={() => onSelectMode('decks')}
            className="flex items-center gap-3 cursor-pointer group"
          >
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-[#056839] via-[#00B09B] to-[#96C93D] p-0.5 shadow-md shadow-[#056839]/20 group-hover:scale-105 transition-transform">
              <div className="w-full h-full bg-white dark:bg-[#131E17] rounded-[14px] flex items-center justify-center transition-colors">
                <GraduationCap className="w-5 h-5 text-[#056839] dark:text-emerald-400" />
              </div>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-lg font-bold tracking-tight text-slate-900 dark:text-white font-['Outfit']">
                  Admission Crack <span className="text-[#056839] dark:text-emerald-400 font-extrabold">2026</span>
                </h1>
                <span className="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20">
                  DU Ka & Medical
                </span>
              </div>
              <p className="text-[11px] text-slate-500 dark:text-slate-400 font-medium">
                Chorcha-Inspired Mobile First Deck
              </p>
            </div>
          </div>

          {/* Top-Right: Google Login + Week Selector + Theme Toggle */}
          <div className="flex items-center gap-2 sm:gap-3">
            
            {/* Google Login / User Profile Pill */}
            {user.isLoggedIn ? (
              <button
                onClick={onOpenAuth}
                className="flex items-center gap-2 p-1.5 pr-3 rounded-full bg-[#F6F8F6] dark:bg-[#1A261F] border border-slate-200 dark:border-[#223328] hover:border-[#056839] dark:hover:border-emerald-500/50 transition-all shadow-sm group"
                title="প্রোফাইল ও সেটিংস"
              >
                <div className="relative">
                  <img
                    src={user.avatar}
                    alt={user.name}
                    className="w-7 h-7 rounded-full object-cover ring-1 ring-[#056839]"
                  />
                  <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-emerald-500 ring-1 ring-white dark:ring-[#131E17]" />
                </div>
                <span className="text-xs font-bold text-slate-800 dark:text-white max-w-[80px] sm:max-w-none truncate">
                  {user.name.split(' ')[0]}
                </span>
                <span className="hidden sm:inline-flex items-center gap-0.5 text-[11px] font-bold text-amber-500 font-mono">
                  <Flame className="w-3.5 h-3.5 fill-current" />
                  {user.streakDays}d
                </span>
              </button>
            ) : (
              <button
                onClick={onOpenAuth}
                className="py-1.5 px-3 rounded-full bg-white dark:bg-[#1A261F] hover:bg-slate-50 dark:hover:bg-[#223429] border border-slate-300 dark:border-[#283C2F] text-slate-800 dark:text-white text-xs font-bold shadow-sm flex items-center gap-2 transition-all hover:scale-102 active:scale-98"
                title="Google দিয়ে লগইন করুন"
              >
                <svg className="w-4 h-4" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
                </svg>
                <span className="hidden xs:inline">Google</span> লগইন
              </button>
            )}

            {/* Week Selector Pills (Hidden on very small screens, visible on sm+) */}
            <div className="hidden md:flex items-center gap-1 bg-[#F6F8F6] dark:bg-[#131E17] p-1 rounded-full border border-slate-200 dark:border-[#1E2F24] shadow-inner">
              <span className="text-[11px] font-semibold text-slate-400 pl-2 pr-1 flex items-center gap-1">
                <Layers className="w-3 h-3" /> সপ্তাহ:
              </span>
              {(['all', 'week_01', 'week_02', 'week_03'] as WeekFilterType[]).map((w) => (
                <button
                  key={w}
                  onClick={() => onSelectWeek(w)}
                  className={`px-2.5 py-1 text-xs font-semibold rounded-full transition-all ${
                    selectedWeek === w
                      ? 'bg-[#056839] text-white shadow-sm'
                      : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                  }`}
                >
                  {w === 'all' ? 'All Weeks' : w === 'week_01' ? 'Week 01' : w === 'week_02' ? 'Week 02' : 'Week 03'}
                </button>
              ))}
            </div>

            {/* Sun/Moon Theme Toggle */}
            <button
              onClick={onToggleTheme}
              className="p-2 rounded-full bg-[#F6F8F6] dark:bg-[#1A261F] text-slate-700 dark:text-amber-400 hover:text-slate-900 dark:hover:text-amber-300 border border-slate-200 dark:border-[#1E2F24] transition-all shadow-sm hover:scale-105 active:scale-95"
              title={theme === 'dark' ? 'লাইট মোড চালু করুন' : 'ডার্ক মোড চালু করুন'}
              aria-label="Toggle Theme"
            >
              {theme === 'dark' ? (
                <Sun className="w-4 h-4 text-amber-400" />
              ) : (
                <Moon className="w-4 h-4 text-slate-700" />
              )}
            </button>
          </div>
        </div>

        {/* 3. CHORCHA PILL FILTERS & TABS:
            Replace flat text links with rounded pill segment controls:
            [ মডেল টেস্ট ]  [ ভার্সিটি ক্লাস্টার ]  [ ট্র্যাপ ও শর্টকাট ভল্ট ]
            Active pills get solid deep green/emerald background (bg-[#056839] text-white). */}
        <div className="flex flex-col md:flex-row md:items-center justify-between pb-3 pt-1 gap-2.5 border-t border-slate-200/70 dark:border-[#1E2F24]">
          
          {/* Chorcha Pill Segment Controls */}
          <div className="flex items-center gap-1.5 overflow-x-auto pb-1 md:pb-0 scrollbar-none">
            <button
              onClick={() => onSelectMode('decks')}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold transition-all whitespace-nowrap ${
                currentMode === 'decks'
                  ? 'bg-[#056839] text-white shadow-sm shadow-[#056839]/30 scale-102'
                  : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
              }`}
            >
              <Home className="w-3.5 h-3.5" />
              <span>ডেক ওভারভিউ</span>
            </button>

            <button
              onClick={() => onSelectMode('exam')}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold transition-all whitespace-nowrap ${
                currentMode === 'exam'
                  ? 'bg-[#056839] text-white shadow-sm shadow-[#056839]/30 scale-102'
                  : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
              }`}
            >
              <Clock className="w-3.5 h-3.5" />
              <span>মডেল টেস্ট</span>
              <span className={`text-[9px] px-1.5 py-0.2 rounded-full font-bold ${
                currentMode === 'exam' ? 'bg-white/20 text-white' : 'bg-rose-500/10 text-rose-600 dark:text-rose-400'
              }`}>
                -0.25
              </span>
            </button>

            <button
              onClick={() => onSelectMode('slides')}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold transition-all whitespace-nowrap ${
                currentMode === 'slides'
                  ? 'bg-[#056839] text-white shadow-sm shadow-[#056839]/30 scale-102'
                  : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
              }`}
            >
              <Sparkles className="w-3.5 h-3.5" />
              <span>ভার্সিটি ক্লাস্টার</span>
            </button>

            <button
              onClick={() => onSelectMode('vault')}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold transition-all whitespace-nowrap ${
                currentMode === 'vault'
                  ? 'bg-[#056839] text-white shadow-sm shadow-[#056839]/30 scale-102'
                  : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
              }`}
            >
              <Zap className="w-3.5 h-3.5 text-amber-500" />
              <span>ট্র্যাপ ও শর্টকাট ভল্ট</span>
            </button>
          </div>

          {/* Subject Filter Pills */}
          {currentMode !== 'vault' && currentMode !== 'analytics' && currentMode !== 'decks' && (
            <div className="flex items-center gap-1.5 overflow-x-auto pb-1 md:pb-0 scrollbar-none">
              {subjects.map((subj) => {
                const active = selectedSubject === subj.label;
                return (
                  <button
                    key={subj.label}
                    onClick={() => onSelectSubject(subj.label)}
                    className={`px-3 py-1 text-xs font-bold rounded-full transition-all whitespace-nowrap ${
                      active
                        ? 'bg-[#056839] text-white shadow-sm'
                        : 'bg-white dark:bg-[#131E17] text-slate-600 dark:text-slate-400 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
                    }`}
                  >
                    {subj.bn}
                  </button>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </header>
  );
};
