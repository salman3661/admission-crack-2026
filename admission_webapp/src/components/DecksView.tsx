import React from 'react';
import { 
  Sparkles, 
  Play, 
  ArrowRight, 
  Layers, 
  Clock, 
  Zap,
  BookOpen
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
  user,
  onOpenAuth,
  totalSlides,
  totalFlashcards,
  totalQuizzes,
}) => {
  const handleDeckNavigate = (targetMode: AppMode, subject: SubjectType) => {
    onSelectSubject(subject);
    onSelectMode(targetMode);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 py-6 pb-28">
      
      {/* 1. TOP WELCOME BANNER */}
      <div className="mb-6">
        <div className="bg-white dark:bg-zinc-900 rounded-3xl p-5 sm:p-6 border border-zinc-200/80 dark:border-zinc-800 shadow-sm relative overflow-hidden">
          {/* Subtle background ambient glow */}
          <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-br from-[#056839]/10 via-[#00B09B]/5 to-transparent rounded-full blur-3xl pointer-events-none" />

          <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 flex items-center gap-1.5 shadow-sm">
                  <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                  Chorcha Admission Deck 2026
                </span>
                <span className="hidden sm:inline-flex px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-700 dark:text-amber-300 border border-amber-500/20">
                  🔥 লাইভ সেশন
                </span>
                <span className="hidden sm:inline-flex px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-700 dark:text-cyan-300 border border-cyan-500/20">
                  📚 {totalSlides}টি স্লাইড ডেক
                </span>
              </div>
              <h1 className="text-xl sm:text-2xl md:text-3xl font-extrabold text-zinc-900 dark:text-white tracking-tight leading-snug">
                {user.isLoggedIn && user.name ? `স্বাগতম, ${user.name}!` : 'স্বাগতম, ভর্তিযোদ্ধা!'} আজ তোমার টার্গেট DU 'Ka' ও মেডিকেল ক্র্যাক
              </h1>
              <p className="text-xs sm:text-sm text-zinc-600 dark:text-zinc-400 mt-1 max-w-2xl leading-relaxed">
                ক্যালকুলেটর-বিহীন শর্টকাট, -0.25 নেগেটিভ মার্কিং প্র্যাকটিস ও ১০০% এক্সপেক্টেড প্রশ্নের আধুনিক স্মার্ট ডেক।
              </p>
            </div>

            {/* User status or Google sign-in trigger */}
            <div className="flex items-center gap-3 shrink-0">
              {user.isLoggedIn ? (
                <div 
                  onClick={onOpenAuth}
                  className="cursor-pointer p-2.5 sm:p-3 rounded-2xl bg-[#F6F8F6] dark:bg-zinc-800/80 border border-zinc-200/80 dark:border-zinc-700/80 flex items-center gap-3 hover:scale-102 transition-all shadow-sm"
                >
                  <img
                    src={user.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(user.email || 'user')}`}
                    alt={user.name}
                    className="w-10 h-10 rounded-xl object-cover ring-2 ring-[#056839]"
                  />
                  <div>
                    <div className="text-xs font-bold text-zinc-900 dark:text-white flex items-center gap-1">
                      {user.name.split(' ')[0]}
                      <span className="text-amber-500 font-mono">🔥{user.streakDays}d</span>
                    </div>
                    <div className="text-[11px] text-[#056839] dark:text-emerald-400 font-semibold">
                      {user.target.split(' ')[0]}
                    </div>
                  </div>
                </div>
              ) : (
                <button
                  onClick={onOpenAuth}
                  className="py-2.5 px-4 rounded-2xl bg-white dark:bg-zinc-800 hover:bg-zinc-50 dark:hover:bg-zinc-700 text-zinc-800 dark:text-white text-xs font-bold border border-zinc-300 dark:border-zinc-700 shadow-sm flex items-center gap-2 transition-all hover:scale-105 active:scale-95"
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

      {/* 2. CHORCHA-STYLE VIBRANT CARDS (GRID LAYOUT) */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5 sm:gap-6">
        
        {/* CARD 1: Medical Master Deck (Crimson red) */}
        <div 
          className="bg-gradient-to-br from-[#E52D27] to-[#B31217] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 active:scale-[0.99] border border-white/20 relative group overflow-hidden"
        >
          {/* Subtle 3D glossy highlight */}
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/15 pointer-events-none rounded-3xl" />

          {/* Top Row: Frosted Badges & Live Counter */}
          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-white shadow-sm flex items-center gap-1.5 border border-white/25">
                <span className="w-2 h-2 rounded-full bg-white animate-ping" />
                ⚡ Live
              </span>
              <span className="bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-semibold text-white/95 border border-white/20">
                🩺 মেডিকেল স্পেশাল
              </span>
            </div>

            {/* Live Counter */}
            <div className="bg-white/15 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5 border border-white/20">
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

          {/* Bottom Row: Exam/Card count pills & Action Buttons */}
          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                ✎ 45 Questions
              </span>
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                🗂️ 50 Cards
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDeckNavigate('slides', 'Biology')}
                className="px-3 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs backdrop-blur-md border border-white/30 transition-all flex items-center gap-1"
                title="কনসেপ্ট স্লাইড দেখুন"
              >
                <BookOpen className="w-3.5 h-3.5" />
                কনসেপ্ট ভিউ
              </button>
              <button
                onClick={() => handleDeckNavigate('exam', 'Biology')}
                className="px-4 py-2 rounded-xl bg-white text-[#B31217] font-bold text-xs shadow-md hover:bg-white/95 transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95"
                title="মেডিকেল টেস্ট শুরু করুন"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                টেস্ট শুরু
              </button>
            </div>
          </div>
        </div>

        {/* CARD 2: Varsity 'Ka' Deck (Deep Emerald green) */}
        <div 
          className="bg-gradient-to-br from-[#00B09B] to-[#96C93D] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 active:scale-[0.99] border border-white/20 relative group overflow-hidden"
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/15 pointer-events-none rounded-3xl" />

          {/* Badges & Live Counter */}
          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-white shadow-sm flex items-center gap-1.5 border border-white/25">
                🏆 DU 1-100 Target
              </span>
              <span className="bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-semibold text-white/95 border border-white/20">
                ⚡ নো ক্যালকুলেটর
              </span>
            </div>

            <div className="bg-white/15 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5 border border-white/20">
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

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                ✎ 60 Questions
              </span>
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                🗂️ 65 Cards
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDeckNavigate('slides', 'Higher Math')}
                className="px-3 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs backdrop-blur-md border border-white/30 transition-all flex items-center gap-1"
                title="কনসেপ্ট স্লাইড দেখুন"
              >
                <BookOpen className="w-3.5 h-3.5" />
                কনসেপ্ট ভিউ
              </button>
              <button
                onClick={() => handleDeckNavigate('exam', 'Higher Math')}
                className="px-4 py-2 rounded-xl bg-white text-[#056839] font-bold text-xs shadow-md hover:bg-white/95 transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95"
                title="ঢাবি 'ক' ইউনিট টেস্ট শুরু করুন"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                টেস্ট শুরু
              </button>
            </div>
          </div>
        </div>

        {/* CARD 3: Engineering Deck (Cobalt blue) */}
        <div 
          className="bg-gradient-to-br from-[#0052D4] to-[#4364F7] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 active:scale-[0.99] border border-white/20 relative group overflow-hidden"
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/15 pointer-events-none rounded-3xl" />

          {/* Badges & Live Counter */}
          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-white shadow-sm flex items-center gap-1.5 border border-white/25">
                📐 BUET & গুচ্ছ
              </span>
              <span className="bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-semibold text-white/95 border border-white/20">
                🔥 হাই-কনসেপ্ট
              </span>
            </div>

            <div className="bg-white/15 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5 border border-white/20">
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

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                ✎ 40 Questions
              </span>
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                🗂️ 45 Cards
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDeckNavigate('slides', 'Physics')}
                className="px-3 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs backdrop-blur-md border border-white/30 transition-all flex items-center gap-1"
              >
                <BookOpen className="w-3.5 h-3.5" />
                কনসেপ্ট ভিউ
              </button>
              <button
                onClick={() => handleDeckNavigate('exam', 'Physics')}
                className="px-4 py-2 rounded-xl bg-white text-[#0052D4] font-bold text-xs shadow-md hover:bg-white/95 transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                টেস্ট শুরু
              </button>
            </div>
          </div>
        </div>

        {/* CARD 4: Special Expected Matrix (Vivid Violet/Magenta gradient) */}
        <div 
          className="bg-gradient-to-br from-[#8A2387] via-[#E94057] to-[#F27121] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 active:scale-[0.99] border border-white/20 relative group overflow-hidden"
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/15 pointer-events-none rounded-3xl" />

          {/* Badges & Live Counter */}
          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-white shadow-sm flex items-center gap-1.5 border border-white/25">
                🎯 ১০০% রিপিট
              </span>
              <span className="bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-semibold text-white/95 border border-white/20">
                ⚠️ ফাঁদ ব্রেকার
              </span>
            </div>

            <div className="bg-white/15 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5 border border-white/20">
              <span className="w-2 h-2 rounded-full bg-rose-300" />
              ১,৪২০ জন প্র্যাকটিস করছে
            </div>
          </div>

          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-sm font-['Outfit']">
              Special Expected Matrix
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              বিগত ২০ বছরের প্রশ্ন বিশ্লেষণ করে তৈরি সবচেয়ে বেশি রিপিট হওয়া ফর্মুলা ও ট্র্যাপের এক্সক্লুসিভ কালেকশন।
            </p>
          </div>

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                ✎ 45 Questions
              </span>
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                🗂️ 50 Cards
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDeckNavigate('slides', 'All')}
                className="px-3 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs backdrop-blur-md border border-white/30 transition-all flex items-center gap-1"
              >
                <BookOpen className="w-3.5 h-3.5" />
                কনসেপ্ট ভিউ
              </button>
              <button
                onClick={() => handleDeckNavigate('vault', 'All')}
                className="px-4 py-2 rounded-xl bg-white text-[#8A2387] font-bold text-xs shadow-md hover:bg-white/95 transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95"
              >
                <Sparkles className="w-3.5 h-3.5" />
                ভল্ট ওপেন
              </button>
            </div>
          </div>
        </div>

      </div>

      {/* 3. QUICK LAUNCH SHORTCUTS & VAULT HIGHLIGHTS */}
      <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Shortcut 1: Calculator Free Vault */}
        <div 
          onClick={() => handleDeckNavigate('vault', 'All')}
          className="bg-white dark:bg-zinc-900 p-4 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 hover:border-[#056839]/50 shadow-sm cursor-pointer transition-all hover:-translate-y-0.5 group"
        >
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 group-hover:bg-amber-500 group-hover:text-white transition-colors">
              <Zap className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white flex items-center gap-1">
                হ্যান্ড ক্যালকুলেশন ভল্ট
                <ArrowRight className="w-3.5 h-3.5 text-zinc-400 group-hover:translate-x-1 transition-transform" />
              </h3>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">
                √2, √3, লগ ও স্টয়কিওমেট্রি টেবিল
              </p>
            </div>
          </div>
        </div>

        {/* Shortcut 2: Smart Flashcards */}
        <div 
          onClick={() => handleDeckNavigate('flashcards', 'All')}
          className="bg-white dark:bg-zinc-900 p-4 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 hover:border-[#00B09B]/50 shadow-sm cursor-pointer transition-all hover:-translate-y-0.5 group"
        >
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 group-hover:bg-emerald-600 group-hover:text-white transition-colors">
              <Layers className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white flex items-center gap-1">
                {totalFlashcards} স্মার্ট ফ্ল্যাশকার্ড
                <ArrowRight className="w-3.5 h-3.5 text-zinc-400 group-hover:translate-x-1 transition-transform" />
              </h3>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">
                একটিভ রিকল ও স্পেসড রিপিটেশন
              </p>
            </div>
          </div>
        </div>

        {/* Shortcut 3: DU Real Exam with Negative Marking */}
        <div 
          onClick={() => handleDeckNavigate('exam', 'All')}
          className="bg-white dark:bg-zinc-900 p-4 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 hover:border-rose-500/50 shadow-sm cursor-pointer transition-all hover:-translate-y-0.5 group"
        >
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-rose-500/10 text-rose-600 dark:text-rose-400 group-hover:bg-rose-600 group-hover:text-white transition-colors">
              <Clock className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white flex items-center gap-1">
                {totalQuizzes} রিয়েল টেস্ট (-0.25)
                <ArrowRight className="w-3.5 h-3.5 text-zinc-400 group-hover:translate-x-1 transition-transform" />
              </h3>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">
                ৪৫ সেকেন্ড টাইমার ও ব্যাখ্যা
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
