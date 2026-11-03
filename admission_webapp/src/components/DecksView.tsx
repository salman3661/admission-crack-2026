import React, { useState } from 'react';
import { 
  Sparkles, 
  Play, 
  ArrowRight, 
  Layers, 
  Clock, 
  Zap,
  GraduationCap
} from 'lucide-react';
import type { AppMode, SubjectType, WeekFilterType, UserProfile } from '../types';

interface DecksViewProps {
  onSelectMode: (mode: AppMode) => void;
  onSelectSubject: (subject: SubjectType) => void;
  selectedWeek: WeekFilterType;
  onSelectWeek: (week: WeekFilterType) => void;
  user: UserProfile;
  onOpenAuth: () => void;
  totalSlides: number;
  totalFlashcards: number;
  totalQuizzes: number;
}

export const DecksView: React.FC<DecksViewProps> = ({
  onSelectMode,
  onSelectSubject,
  selectedWeek,
  onSelectWeek,
  user,
  onOpenAuth,
  totalSlides,
  totalFlashcards,
  totalQuizzes,
}) => {
  // Chorcha Segment Control filter tab
  const [activeSegment, setActiveSegment] = useState<'all' | 'exam' | 'varsity' | 'vault'>('all');

  const handleDeckClick = (targetMode: AppMode, subject: SubjectType) => {
    onSelectSubject(subject);
    onSelectMode(targetMode);
  };

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 py-6 pb-24">
      {/* Top Chorcha Aspirant Greeting & Live Banner */}
      <div className="mb-6">
        <div className="bg-white dark:bg-[#131E17] rounded-3xl p-5 sm:p-6 border border-slate-200/80 dark:border-[#1E2F24] shadow-sm relative overflow-hidden">
          {/* Subtle background glow */}
          <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-br from-[#056839]/10 via-[#00B09B]/5 to-transparent rounded-full blur-3xl pointer-events-none" />

          <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div className="flex items-center gap-2 mb-1.5">
                <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 flex items-center gap-1">
                  <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                  Chorcha Admission Deck 2026
                </span>
                <span className="hidden sm:inline-flex px-2 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-700 dark:text-amber-300 border border-amber-500/20">
                  🔥 লাইভ সেশন
                </span>
                <span className="hidden sm:inline-flex px-2 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-700 dark:text-cyan-300 border border-cyan-500/20">
                  📚 {totalSlides}টি স্লাইড ডেক
                </span>
              </div>
              <h1 className="text-xl sm:text-2xl font-extrabold text-slate-900 dark:text-white tracking-tight">
                {user.isLoggedIn ? `স্বাগতম, ${user.name}!` : 'স্বাগতম, ভর্তিযোদ্ধা!'} আজ তোমার টার্গেট DU 'Ka' ও মেডিকেল ক্র্যাক
              </h1>
              <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-2xl leading-relaxed">
                ক্যালকুলেটর-বিহীন শর্টকাট, -0.25 নেগেটিভ মার্কিং প্র্যাকটিস ও ১০০% এক্সপেক্টেড প্রশ্নের আধুনিক স্মার্ট ডেক।
              </p>
            </div>

            {/* Quick user status or Google sign-in trigger */}
            <div className="flex items-center gap-3">
              {user.isLoggedIn ? (
                <div 
                  onClick={onOpenAuth}
                  className="cursor-pointer p-3 rounded-2xl bg-[#F6F8F6] dark:bg-[#1A261F] border border-slate-200 dark:border-[#24352A] flex items-center gap-3 hover:scale-102 transition-all shadow-sm"
                >
                  <img
                    src={user.avatar}
                    alt={user.name}
                    className="w-10 h-10 rounded-xl object-cover ring-2 ring-[#056839]"
                  />
                  <div>
                    <div className="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1">
                      {user.name}
                      <span className="text-amber-500 font-mono">🔥{user.streakDays}d</span>
                    </div>
                    <div className="text-[11px] text-[#056839] dark:text-emerald-400 font-semibold">
                      {user.target.split(' ')[0]} • {user.accuracy}%
                    </div>
                  </div>
                </div>
              ) : (
                <button
                  onClick={onOpenAuth}
                  className="py-2.5 px-4 rounded-2xl bg-white dark:bg-[#1A261F] hover:bg-slate-50 dark:hover:bg-[#203026] text-slate-800 dark:text-white text-xs font-bold border border-slate-300 dark:border-[#2D4133] shadow-sm flex items-center gap-2 transition-all hover:scale-105 active:scale-95"
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
        </div>
      </div>

      {/* 3. CHORCHA PILL FILTERS & TABS:
          Replace flat text links with rounded pill segment controls:
          [ মডেল টেস্ট ]  [ ভার্সিটি ক্লাস্টার ]  [ ট্র্যাপ ও শর্টকাট ভল্ট ]
          Active pills get solid deep green/emerald background (bg-[#056839] text-white). */}
      <div className="flex items-center justify-between flex-wrap gap-3 mb-6">
        <div className="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none">
          <button
            onClick={() => setActiveSegment('all')}
            className={`px-4 py-2 rounded-full text-xs font-bold transition-all shadow-sm ${
              activeSegment === 'all'
                ? 'bg-[#056839] text-white shadow-[#056839]/25 shadow-md scale-102'
                : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
            }`}
          >
            সব ডেক
          </button>

          <button
            onClick={() => {
              setActiveSegment('exam');
              onSelectMode('exam');
            }}
            className={`px-4 py-2 rounded-full text-xs font-bold transition-all shadow-sm flex items-center gap-1.5 ${
              activeSegment === 'exam'
                ? 'bg-[#056839] text-white shadow-[#056839]/25 shadow-md scale-102'
                : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
            }`}
          >
            <Clock className="w-3.5 h-3.5" />
            মডেল টেস্ট
          </button>

          <button
            onClick={() => setActiveSegment('varsity')}
            className={`px-4 py-2 rounded-full text-xs font-bold transition-all shadow-sm flex items-center gap-1.5 ${
              activeSegment === 'varsity'
                ? 'bg-[#056839] text-white shadow-[#056839]/25 shadow-md scale-102'
                : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
            }`}
          >
            <GraduationCap className="w-3.5 h-3.5" />
            ভার্সিটি ক্লাস্টার
          </button>

          <button
            onClick={() => {
              setActiveSegment('vault');
              onSelectMode('vault');
            }}
            className={`px-4 py-2 rounded-full text-xs font-bold transition-all shadow-sm flex items-center gap-1.5 ${
              activeSegment === 'vault'
                ? 'bg-[#056839] text-white shadow-[#056839]/25 shadow-md scale-102'
                : 'bg-white dark:bg-[#131E17] text-slate-700 dark:text-slate-300 border border-slate-200/80 dark:border-[#1E2F24] hover:bg-slate-100 dark:hover:bg-[#1A261F]'
            }`}
          >
            <Zap className="w-3.5 h-3.5 text-amber-500" />
            ট্র্যাপ ও শর্টকাট ভল্ট
          </button>
        </div>

        {/* Week Pill Filter */}
        <div className="flex items-center gap-1.5 bg-white dark:bg-[#131E17] p-1 rounded-2xl border border-slate-200/80 dark:border-[#1E2F24] shadow-sm">
          <span className="text-[11px] font-semibold text-slate-400 pl-2 pr-1">সপ্তাহ:</span>
          {(['all', 'week_01', 'week_02', 'week_03'] as WeekFilterType[]).map((w) => (
            <button
              key={w}
              onClick={() => onSelectWeek(w)}
              className={`px-2.5 py-1 text-[11px] font-bold rounded-xl transition-all ${
                selectedWeek === w
                  ? 'bg-[#056839] text-white shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              {w === 'all' ? 'All' : w === 'week_01' ? 'W1' : w === 'week_02' ? 'W2' : 'W3'}
            </button>
          ))}
        </div>
      </div>

      {/* 2. CHORCHA-STYLE VIBRANT CARDS (GRID LAYOUT):
          2-column glossy cards featuring glass highlights:
          * Medical Deck: Crimson red gradient (from-[#E52D27] to-[#B31217]) with frosted glass badge & live counter.
          * Varsity 'Ka' Deck: Deep Emerald green gradient (from-[#00B09B] to-[#96C93D]).
          * Engineering Deck: Cobalt blue gradient (from-[#0052D4] to-[#4364F7]).
          * Special Expected Matrix: Vivid Violet/Magenta gradient (from-[#8A2387] to-[#E94057]). */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5 sm:gap-6">
        
        {/* CARD 1: Medical Deck (Crimson red) */}
        <div 
          className="glossy-card bg-gradient-to-br from-[#E52D27] to-[#B31217] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1.5 active:scale-[0.99] border border-white/20 relative group cursor-pointer"
          onClick={() => handleDeckClick('exam', 'Biology')}
        >
          {/* Subtle 3D glossy highlight */}
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/20 pointer-events-none rounded-3xl" />

          {/* Top Row: Frosted Badges & Live Counter */}
          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="frosted-glass px-3 py-1 rounded-full text-xs font-bold text-white shadow-sm flex items-center gap-1.5">
                <span className="w-2 h-2 rounded-full bg-white animate-ping" />
                ⚡ Live
              </span>
              <span className="frosted-glass px-2.5 py-1 rounded-full text-xs font-semibold text-white/95">
                🩺 মেডিকেল স্পেশাল
              </span>
            </div>

            {/* Live Counter */}
            <div className="frosted-glass px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              ১,৮৫০ জন লাইভ দিচ্ছে
            </div>
          </div>

          {/* Card Body */}
          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-sm font-['Outfit']">
              Medical Master Deck
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              উদ্ভিদ ও প্রাণিবিজ্ঞান, পরিমাণগত রসায়ন ও মুখস্থ-ভিত্তিক কনসেপ্টের নির্ভুল হ্যান্ডবুক। কোনো নেগেটিভ মার্কিং যেন না হয়!
            </p>
          </div>

          {/* Bottom Row: Exam/Card count pills & Action */}
          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20">
            <div className="flex items-center gap-2">
              <span className="frosted-glass px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1">
                ✎ 45 Questions
              </span>
              <span className="frosted-glass px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1">
                🗂️ 50 Cards
              </span>
            </div>

            <button
              onClick={(e) => {
                e.stopPropagation();
                handleDeckClick('exam', 'Biology');
              }}
              className="px-4 py-2 rounded-xl bg-white text-[#B31217] font-bold text-xs shadow-md hover:bg-white/90 transition-all flex items-center gap-1.5 group-hover:scale-105"
            >
              <Play className="w-3.5 h-3.5 fill-current" />
              টেস্ট শুরু
            </button>
          </div>
        </div>

        {/* CARD 2: Varsity 'Ka' Deck (Deep Emerald green) */}
        <div 
          className="glossy-card bg-gradient-to-br from-[#00B09B] to-[#96C93D] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1.5 active:scale-[0.99] border border-white/20 relative group cursor-pointer"
          onClick={() => handleDeckClick('exam', 'Higher Math')}
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/20 pointer-events-none rounded-3xl" />

          {/* Badges & Live Counter */}
          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="frosted-glass px-3 py-1 rounded-full text-xs font-bold text-white shadow-sm flex items-center gap-1.5">
                🏆 DU 1-100 Target
              </span>
              <span className="frosted-glass px-2.5 py-1 rounded-full text-xs font-semibold text-white/95">
                ⚡ নো ক্যালকুলেটর
              </span>
            </div>

            <div className="frosted-glass px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-amber-300" />
              ২,৩৪০ জন যুক্ত আছে
            </div>
          </div>

          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-sm font-['Outfit']">
              Varsity 'Ka' Unit Deck
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিটের জন্য ক্যালকুলেটর ছাড়া ১০ সেকেন্ডে ফিজিক্স ও উচ্চতর গণিত সমাধানের স্পিড প্র্যাকটিস।
            </p>
          </div>

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20">
            <div className="flex items-center gap-2">
              <span className="frosted-glass px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1">
                ✎ 60 Questions
              </span>
              <span className="frosted-glass px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1">
                🗂️ 65 Cards
              </span>
            </div>

            <button
              onClick={(e) => {
                e.stopPropagation();
                handleDeckClick('exam', 'Higher Math');
              }}
              className="px-4 py-2 rounded-xl bg-white text-[#00B09B] font-bold text-xs shadow-md hover:bg-white/90 transition-all flex items-center gap-1.5 group-hover:scale-105"
            >
              <Play className="w-3.5 h-3.5 fill-current" />
              মডেল টেস্ট
            </button>
          </div>
        </div>

        {/* CARD 3: Engineering Deck (Cobalt blue) */}
        <div 
          className="glossy-card bg-gradient-to-br from-[#0052D4] to-[#4364F7] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1.5 active:scale-[0.99] border border-white/20 relative group cursor-pointer"
          onClick={() => handleDeckClick('slides', 'Physics')}
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/20 pointer-events-none rounded-3xl" />

          {/* Badges & Live Counter */}
          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="frosted-glass px-3 py-1 rounded-full text-xs font-bold text-white shadow-sm flex items-center gap-1.5">
                📐 BUET & গুচ্ছ
              </span>
              <span className="frosted-glass px-2.5 py-1 rounded-full text-xs font-semibold text-white/95">
                🔥 হাই-কনসেপ্ট
              </span>
            </div>

            <div className="frosted-glass px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-cyan-300" />
              ৯৬০ জন লাইভ
            </div>
          </div>

          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-sm font-['Outfit']">
              Engineering Speed Deck
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              ভেক্টর ক্যালকুলাস, প্রাস, ঘূর্ণন গতিবিদ্যা ও জটিল সংখ্যার গভীরতম কনসেপ্ট এবং এডভান্সড সমস্যা সমাধান টেকনিক।
            </p>
          </div>

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20">
            <div className="flex items-center gap-2">
              <span className="frosted-glass px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1">
                ✎ 40 Questions
              </span>
              <span className="frosted-glass px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1">
                🗂️ 45 Cards
              </span>
            </div>

            <button
              onClick={(e) => {
                e.stopPropagation();
                handleDeckClick('slides', 'Physics');
              }}
              className="px-4 py-2 rounded-xl bg-white text-[#0052D4] font-bold text-xs shadow-md hover:bg-white/90 transition-all flex items-center gap-1.5 group-hover:scale-105"
            >
              <Zap className="w-3.5 h-3.5" />
              কনসেপ্ট ভিউ
            </button>
          </div>
        </div>

        {/* CARD 4: Special Expected Matrix (Vivid Violet/Magenta) */}
        <div 
          className="glossy-card bg-gradient-to-br from-[#8A2387] to-[#E94057] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1.5 active:scale-[0.99] border border-white/20 relative group cursor-pointer"
          onClick={() => handleDeckClick('slides', 'All')}
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/20 pointer-events-none rounded-3xl" />

          {/* Badges & Live Counter */}
          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="frosted-glass px-3 py-1 rounded-full text-xs font-bold text-white shadow-sm flex items-center gap-1.5">
                ⭐ ১০০% রিপিটেড
              </span>
              <span className="frosted-glass px-2.5 py-1 rounded-full text-xs font-semibold text-white/95">
                🎯 মোস্ট এক্সপেক্টেড
              </span>
            </div>

            <div className="frosted-glass px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-yellow-300" />
              ৩,১০০ জন রিভিশন দিচ্ছে
            </div>
          </div>

          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-sm font-['Outfit']">
              Special Expected Matrix
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              বিগত ২০ বছরের শীর্ষ ৫০টি ট্র্যাপ ও নিশ্চিত কমন আসা ফর্মুলা প্যাটার্ন। এই প্রশ্নগুলো ভুল করা মানেই মেরিট লিস্ট থেকে বাদ!
            </p>
          </div>

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20">
            <div className="flex items-center gap-2">
              <span className="frosted-glass px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1">
                ✎ 45 Questions
              </span>
              <span className="frosted-glass px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1">
                🗂️ 50 Cards
              </span>
            </div>

            <button
              onClick={(e) => {
                e.stopPropagation();
                handleDeckClick('slides', 'All');
              }}
              className="px-4 py-2 rounded-xl bg-white text-[#8A2387] font-bold text-xs shadow-md hover:bg-white/90 transition-all flex items-center gap-1.5 group-hover:scale-105"
            >
              <Sparkles className="w-3.5 h-3.5" />
              এক্সপেক্টেড ডেক
            </button>
          </div>
        </div>

      </div>

      {/* Quick Launch Shortcuts & Vault Highlights */}
      <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Shortcut 1: Calculator Free Vault */}
        <div 
          onClick={() => onSelectMode('vault')}
          className="bg-white dark:bg-[#131E17] p-4 rounded-2xl border border-slate-200/80 dark:border-[#1E2F24] hover:border-[#056839]/50 shadow-sm cursor-pointer transition-all hover:-translate-y-0.5 group"
        >
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 group-hover:bg-amber-500 group-hover:text-white transition-colors">
              <Zap className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-1">
                হ্যান্ড ক্যালকুলেশন ভল্ট
                <ArrowRight className="w-3.5 h-3.5 text-slate-400 group-hover:translate-x-1 transition-transform" />
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                √2, √3, লগ ও স্টয়কিওমেট্রি টেবিল
              </p>
            </div>
          </div>
        </div>

        {/* Shortcut 2: Smart Flashcards */}
        <div 
          onClick={() => onSelectMode('flashcards')}
          className="bg-white dark:bg-[#131E17] p-4 rounded-2xl border border-slate-200/80 dark:border-[#1E2F24] hover:border-[#00B09B]/50 shadow-sm cursor-pointer transition-all hover:-translate-y-0.5 group"
        >
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 group-hover:bg-emerald-600 group-hover:text-white transition-colors">
              <Layers className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-1">
                {totalFlashcards} স্মার্ট ফ্ল্যাশকার্ড
                <ArrowRight className="w-3.5 h-3.5 text-slate-400 group-hover:translate-x-1 transition-transform" />
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                একটিভ রিকল ও স্পেসড রিপিটেশন
              </p>
            </div>
          </div>
        </div>

        {/* Shortcut 3: DU Real Exam with Negative Marking */}
        <div 
          onClick={() => onSelectMode('exam')}
          className="bg-white dark:bg-[#131E17] p-4 rounded-2xl border border-slate-200/80 dark:border-[#1E2F24] hover:border-rose-500/50 shadow-sm cursor-pointer transition-all hover:-translate-y-0.5 group"
        >
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-rose-500/10 text-rose-600 dark:text-rose-400 group-hover:bg-rose-600 group-hover:text-white transition-colors">
              <Clock className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-1">
                {totalQuizzes} রিয়েল টেস্ট (-0.25)
                <ArrowRight className="w-3.5 h-3.5 text-slate-400 group-hover:translate-x-1 transition-transform" />
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                ৪৫ সেকেন্ড টাইমার ও ব্যাখ্যা
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
