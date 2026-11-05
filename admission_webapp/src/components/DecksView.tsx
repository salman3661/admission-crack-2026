import React, { useState } from 'react';
import { 
  ArrowRight, 
  Clock, 
  Zap, 
  BookOpen, 
  RotateCcw,
  Sparkles,
  ChevronDown,
  Layers,
  Award,
  ShieldCheck,
  GraduationCap
} from 'lucide-react';
import type { AppMode, SubjectType, WeekFilterType, UserProfile, TrackType } from '../types';

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
  activeTrack?: TrackType;
  onSelectTrack?: (track: TrackType) => void;
}

export const DecksView: React.FC<DecksViewProps> = ({
  onSelectMode,
  onSelectSubject,
  activeTrack = 'varsity',
  onSelectTrack,
}) => {
  // Segmented control pills: 'all' | 'model' | 'weekly' | 'subject' | 'vault'
  const [activeSegment, setActiveSegment] = useState<'all' | 'model' | 'weekly' | 'subject' | 'vault'>('all');
  const [isTipsExpanded, setIsTipsExpanded] = useState(false);

  const handleDeckNavigate = (targetMode: AppMode, subject: SubjectType = 'All') => {
    onSelectSubject(subject);
    onSelectMode(targetMode);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="max-w-6xl mx-auto px-3 sm:px-6 py-4 sm:py-6 pb-28 space-y-5">
      
      {/* =========================================================================
          1. SEGMENTED CONTROL PILLS
          [ মডেল টেস্ট | উইকলি স্লট | বিষয় ভিত্তিক | ভল্ট শর্টকাট ]
         ========================================================================= */}
      <div className="flex items-center justify-between gap-1.5 overflow-x-auto no-scrollbar p-1.5 rounded-2xl backdrop-blur-xl bg-white/70 dark:bg-slate-900/70 ring-1 ring-slate-200/80 dark:ring-slate-800/80 shadow-xs">
        {[
          { id: 'all' as const, label: '🌟 অল স্ট্রিম ডেক' },
          { id: 'model' as const, label: '🏆 মডেল টেস্ট' },
          { id: 'weekly' as const, label: '📅 উইকলি স্লট' },
          { id: 'subject' as const, label: '📚 বিষয় ভিত্তিক' },
          { id: 'vault' as const, label: '⚡ ভল্ট শর্টকাট' },
        ].map((pill) => {
          const isActive = activeSegment === pill.id;
          return (
            <button
              key={pill.id}
              onClick={() => setActiveSegment(pill.id)}
              className={`flex-1 min-w-max px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all whitespace-nowrap active:scale-95 cursor-pointer ${
                isActive
                  ? 'bg-gradient-to-r from-emerald-600 to-teal-600 text-white shadow-sm ring-1 ring-emerald-500/40'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-100/60 dark:hover:bg-slate-800/60'
              }`}
            >
              {pill.label}
            </button>
          );
        })}
      </div>

      {/* =========================================================================
          2. COMPACT DUAL-TARGET STUDY BANNER WITH COLLAPSIBLE QUICK TIPS
         ========================================================================= */}
      <div className="rounded-3xl backdrop-blur-xl bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80 shadow-sm overflow-hidden p-4 sm:p-5 transition-all">
        {/* Dual Sprint Track Selector Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-3.5">
          {/* DU 'Ka' - Primary Target */}
          <div 
            onClick={() => onSelectTrack && onSelectTrack('varsity')}
            className={`p-3.5 sm:p-4 rounded-2xl transition-all cursor-pointer ring-1 ${
              activeTrack === 'varsity'
                ? 'bg-gradient-to-br from-emerald-500/15 via-teal-500/10 to-blue-500/10 ring-emerald-500 stream-glow-varsity shadow-xs'
                : 'bg-slate-50/70 dark:bg-slate-800/50 ring-slate-200/80 dark:ring-slate-700/80 opacity-75 hover:opacity-100'
            } flex items-center justify-between group active:scale-[0.99]`}
          >
            <div className="flex items-center gap-3">
              <span className="text-2xl group-hover:scale-110 transition-transform">🎯</span>
              <div>
                <div className="flex items-center gap-1.5 flex-wrap">
                  <span className="text-xs sm:text-sm font-black text-slate-900 dark:text-white">
                    ঢাকা বিশ্ববিদ্যালয় 'ক' (DU 'Ka')
                  </span>
                  {activeTrack === 'varsity' && (
                    <span className="px-2 py-0.5 rounded-full text-[9px] font-black bg-emerald-600 text-white shadow-xs">
                      ✓ সক্রিয় মেইন ট্র্যাক
                    </span>
                  )}
                </div>
                <div className="text-[11px] text-slate-600 dark:text-slate-400 font-medium">
                  MCQ ৬০ + লিখিত ৪০ = ১০০ নম্বর • নো ক্যালকুলেটর
                </div>
              </div>
            </div>
            <span className={`px-2.5 py-1 rounded-xl text-white font-mono text-[11px] font-extrabold shrink-0 shadow-xs transition-colors ${
              activeTrack === 'varsity' ? 'bg-emerald-600' : 'bg-slate-500 group-hover:bg-emerald-600'
            }`}>
              {activeTrack === 'varsity' ? 'Active' : 'সুইচ'}
            </span>
          </div>

          {/* Medical MAT - Secondary / Backup Target */}
          <div 
            onClick={() => onSelectTrack && onSelectTrack('medical')}
            className={`p-3.5 sm:p-4 rounded-2xl transition-all cursor-pointer ring-1 ${
              activeTrack === 'medical'
                ? 'bg-gradient-to-br from-rose-500/15 via-crimson-500/10 to-pink-500/10 ring-rose-500 stream-glow-medical shadow-xs'
                : 'bg-slate-50/70 dark:bg-slate-800/50 ring-slate-200/80 dark:ring-slate-700/80 opacity-75 hover:opacity-100'
            } flex items-center justify-between group active:scale-[0.99]`}
          >
            <div className="flex items-center gap-3">
              <span className="text-2xl group-hover:scale-110 transition-transform">🩺</span>
              <div>
                <div className="flex items-center gap-1.5 flex-wrap">
                  <span className="text-xs sm:text-sm font-black text-slate-900 dark:text-white">
                    মেডিকেল ভর্তি পরীক্ষা (MAT 2026-27)
                  </span>
                  {activeTrack === 'medical' && (
                    <span className="px-2 py-0.5 rounded-full text-[9px] font-black bg-rose-600 text-white shadow-xs">
                      ✓ সক্রিয় ট্র্যাক
                    </span>
                  )}
                </div>
                <div className="text-[11px] text-slate-600 dark:text-slate-400 font-medium">
                  Bio 30, Chem 25, Phys 20, Eng 15, GK 10
                </div>
              </div>
            </div>
            <span className={`px-2.5 py-1 rounded-xl text-white font-mono text-[11px] font-extrabold shrink-0 shadow-xs transition-colors ${
              activeTrack === 'medical' ? 'bg-rose-600' : 'bg-slate-500 group-hover:bg-rose-600'
            }`}>
              {activeTrack === 'medical' ? 'Active' : 'সুইচ'}
            </span>
          </div>
        </div>

        {/* Collapsible Quick Tips Bar */}
        <div className="border-t border-slate-200/70 dark:border-slate-800/70 pt-2.5">
          <button
            onClick={() => setIsTipsExpanded(!isTipsExpanded)}
            className="w-full flex items-center justify-between text-xs font-bold text-slate-700 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 transition-colors py-1 cursor-pointer"
          >
            <div className="flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-amber-500" />
              <span>💡 ডুয়াল-টার্গেট ৮০/২০ কৌশল ও টাইম ম্যানেজমেন্ট গাইডলাইন</span>
            </div>
            <ChevronDown className={`w-4 h-4 transition-transform duration-200 ${isTipsExpanded ? 'rotate-180' : ''}`} />
          </button>

          {isTipsExpanded && (
            <div className="mt-2.5 p-3 rounded-2xl bg-slate-50/80 dark:bg-slate-800/60 ring-1 ring-slate-200/80 dark:ring-slate-700/80 text-xs text-slate-600 dark:text-slate-300 leading-relaxed animate-in fade-in duration-200 space-y-1.5">
              <p>
                <strong>কেন কোনো কনফ্লিক্ট নেই?</strong> ফিজিক্স ও কেমিস্ট্রি যদি ভার্সিটির জন্য ম্যাথসহ ডিপ প্রিপারেশন নাও, তবে মেডিকেলের ফিজিক্স ও কেমিস্ট্রি থিওরি সরাসরি কমন পড়বে।
              </p>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1 font-medium text-[11px]">
                <div className="p-2 rounded-xl bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 ring-1 ring-emerald-500/20">
                  🎯 <strong>ভার্সিটি 'ক' (৭০% সময়):</strong> পদার্থ ও রসায়ন ম্যাথ, উচ্চতর গণিত শর্টকাট এবং লিখিত অংশের নিয়মিত খাতা চর্চা।
                </div>
                <div className="p-2 rounded-xl bg-rose-500/10 text-rose-800 dark:text-rose-300 ring-1 ring-rose-500/20">
                  🩺 <strong>মেডিকেল বুস্টার (৩০% সময়):</strong> দিনে ১.৫–২ ঘণ্টা বায়োলজি ছক (আজমল/হাসান) + ইংলিশ (১৫) + জিকে (১০)।
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* =========================================================================
          3. SLEEK 2x3 GRID OF INTERACTIVE STREAM CARDS (Aesthetic Edtech Layout)
         ========================================================================= */}
      {(activeSegment === 'all' || activeSegment === 'weekly') && (
        <div>
          <div className="flex items-center justify-between gap-2 mb-3">
            <h2 className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
              <Layers className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
              <span>এডমিশন কোর স্ট্রিম কার্ডস (2026 Edition)</span>
            </h2>
            <span className="text-[11px] font-semibold text-slate-500 dark:text-slate-400">
              ৬টি ইন্টারেক্টিভ স্ট্রিম
            </span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
            
            {/* Stream 1: Varsity 'Ka' Core */}
            <div 
              onClick={() => handleDeckNavigate('exam', 'All')}
              className="group p-5 rounded-3xl backdrop-blur-xl bg-gradient-to-br from-emerald-500/10 via-emerald-600/5 to-teal-500/10 ring-1 ring-emerald-500/30 hover:ring-emerald-500 stream-glow-varsity shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/30">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping" />
                    🔴 Live 80/20
                  </span>
                  <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/20">
                    ২,৩৭৬+ MCQ
                  </span>
                </div>

                <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-emerald-600 to-teal-500 text-white flex items-center justify-center text-xl shadow-md shadow-emerald-600/25 mb-3 group-hover:scale-105 transition-transform">
                  🎯
                </div>

                <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors mb-1.5">
                  ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট (DU 'Ka')
                </h3>

                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                  বিগত ১৫-২০ বছরের ঢাবি অরিজিনাল প্রশ্নব্যাংক, রিপিট প্যাটার্ন এবং নো-ক্যালকুলেটর ম্যাথ স্পিড ট্রিকস।
                </p>
              </div>

              <div>
                <div className="p-2 rounded-xl bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 text-[11px] font-semibold mb-3 flex items-center gap-1.5">
                  <ShieldCheck className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                  <span>MCQ ৬০ + লিখিত ৪০ • ১০০ মার্কস কমপ্লিট</span>
                </div>
                <div className="flex items-center justify-between text-xs font-bold text-emerald-700 dark:text-emerald-400">
                  <span>অনুশীলন শুরু করুন</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </div>

            {/* Stream 2: Medical MAT */}
            <div 
              onClick={() => {
                onSelectTrack && onSelectTrack('medical');
                handleDeckNavigate('exam', 'All');
              }}
              className="group p-5 rounded-3xl backdrop-blur-xl bg-gradient-to-br from-rose-500/10 via-red-600/5 to-pink-500/10 ring-1 ring-rose-500/30 hover:ring-rose-500 stream-glow-medical shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-rose-500/15 text-rose-700 dark:text-rose-300 ring-1 ring-rose-500/30">
                    <span className="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping" />
                    🔴 Live 80/20
                  </span>
                  <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-rose-700 dark:text-rose-300 ring-1 ring-rose-500/20">
                    ১,৫৮৪+ প্রশ্ন
                  </span>
                </div>

                <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-rose-600 to-pink-600 text-white flex items-center justify-center text-xl shadow-md shadow-rose-600/25 mb-3 group-hover:scale-105 transition-transform">
                  🩺
                </div>

                <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-rose-600 dark:group-hover:text-rose-400 transition-colors mb-1.5">
                  মেডিকেল ভর্তি পরীক্ষা (MAT 2026-27)
                </h3>

                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                  আজমল ও হাসান স্যারের বায়োলজি ছক, হাজারী স্যারের তথ্য কণিকা এবং বিগত মেডিকেল-ডেন্টাল PYQ।
                </p>
              </div>

              <div>
                <div className="p-2 rounded-xl bg-rose-500/10 text-rose-800 dark:text-rose-300 text-[11px] font-semibold mb-3 flex items-center gap-1.5">
                  <Award className="w-3.5 h-3.5 text-rose-600 shrink-0" />
                  <span>Bio 30 • Chem 25 • Phys 20 • Eng 15 • GK 10</span>
                </div>
                <div className="flex items-center justify-between text-xs font-bold text-rose-700 dark:text-rose-400">
                  <span>মেডিকেল ড্রিল শুরু</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </div>

            {/* Stream 3: Engineering Bridge & Math Speed */}
            <div 
              onClick={() => handleDeckNavigate('vault', 'Higher Math')}
              className="group p-5 rounded-3xl backdrop-blur-xl bg-gradient-to-br from-cyan-500/10 via-indigo-600/5 to-blue-500/10 ring-1 ring-cyan-500/30 hover:ring-cyan-500 stream-glow-engineering shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-cyan-500/15 text-cyan-700 dark:text-cyan-300 ring-1 ring-cyan-500/30">
                    ⚡ BUET/CKRUET Bridge
                  </span>
                  <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-cyan-700 dark:text-cyan-300 ring-1 ring-cyan-500/20">
                    হাই-স্পিড হ্যাক
                  </span>
                </div>

                <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-cyan-600 to-indigo-600 text-white flex items-center justify-center text-xl shadow-md shadow-cyan-600/25 mb-3 group-hover:scale-105 transition-transform">
                  📐
                </div>

                <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-cyan-600 dark:group-hover:text-cyan-400 transition-colors mb-1.5">
                  ইঞ্জিনিয়ারিং ব্রিজ ও স্পিড হ্যাক
                </h3>

                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                  ক্যালকুলাস শর্টকাট (ল'হসপিটাল/ইন্টিগ্রেশন ট্রিক), কনিক্স ফর্মুলা এবং মেকানিক্স প্রবলেম সলভিং।
                </p>
              </div>

              <div>
                <div className="p-2 rounded-xl bg-cyan-500/10 text-cyan-800 dark:text-cyan-300 text-[11px] font-semibold mb-3 flex items-center gap-1.5">
                  <Zap className="w-3.5 h-3.5 text-cyan-600 shrink-0" />
                  <span>ক্যালকুলাস • কনিক্স • মেকানিক্স স্পিড হ্যাক</span>
                </div>
                <div className="flex items-center justify-between text-xs font-bold text-cyan-700 dark:text-cyan-400">
                  <span>ম্যাথ ভল্ট এক্সপ্লোর</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </div>

            {/* Stream 4: DU Written Blueprint */}
            <div 
              onClick={() => handleDeckNavigate('predictor', 'All')}
              className="group p-5 rounded-3xl backdrop-blur-xl bg-gradient-to-br from-purple-500/10 via-indigo-600/5 to-violet-500/10 ring-1 ring-purple-500/30 hover:ring-purple-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-purple-500/15 text-purple-700 dark:text-purple-300 ring-1 ring-purple-500/30">
                    ✍️ Written Blueprint
                  </span>
                  <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-purple-700 dark:text-purple-300 ring-1 ring-purple-500/20">
                    ৪০/৪০ টার্গেট
                  </span>
                </div>

                <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-purple-600 to-indigo-600 text-white flex items-center justify-center text-xl shadow-md shadow-purple-600/25 mb-3 group-hover:scale-105 transition-transform">
                  📝
                </div>

                <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors mb-1.5">
                  ঢাবি লিখিত ৪০ মার্কস মাস্টারক্লাস
                </h3>

                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                  বক্স সাইজ লিমিটেশন, স্টেপ-বাই-স্টেপ পার্শিয়াল মার্কিং রুব্রিক এবং স্যাম্পল খাতা সমাধান।
                </p>
              </div>

              <div>
                <div className="p-2 rounded-xl bg-purple-500/10 text-purple-800 dark:text-purple-300 text-[11px] font-semibold mb-3 flex items-center gap-1.5">
                  <GraduationCap className="w-3.5 h-3.5 text-purple-600 shrink-0" />
                  <span>পার্শিয়াল মার্কিং রুব্রিক ও ঢাবি খাতা সলিউশন</span>
                </div>
                <div className="flex items-center justify-between text-xs font-bold text-purple-700 dark:text-purple-400">
                  <span>লিখিত প্রবলেম দেখুন</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </div>

            {/* Stream 5: 1-Second Formula Vault & Trap Defense */}
            <div 
              onClick={() => handleDeckNavigate('vault', 'All')}
              className="group p-5 rounded-3xl backdrop-blur-xl bg-gradient-to-br from-amber-500/10 via-yellow-600/5 to-orange-500/10 ring-1 ring-amber-500/30 hover:ring-amber-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-amber-500/15 text-amber-700 dark:text-amber-300 ring-1 ring-amber-500/30">
                    🛡️ Trap Shield
                  </span>
                  <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-amber-700 dark:text-amber-300 ring-1 ring-amber-500/20">
                    ২০০+ শর্টকাট
                  </span>
                </div>

                <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-500 to-orange-500 text-white flex items-center justify-center text-xl shadow-md shadow-amber-500/25 mb-3 group-hover:scale-105 transition-transform">
                  ⚡
                </div>

                <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors mb-1.5">
                  ১-সেকেন্ড ফর্মুলা ও ট্র্যাপ ডিফেন্স
                </h3>

                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                  দশমিক ভাগ, অনুপাত শর্টকাট, ত্রিকোণমিতি ডোমেন-রেঞ্জ ট্রিক এবং ঢাবি এক্সামিনারদের পছন্দের ট্র্যাপ হ্যাক।
                </p>
              </div>

              <div>
                <div className="p-2 rounded-xl bg-amber-500/10 text-amber-800 dark:text-amber-300 text-[11px] font-semibold mb-3 flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5 text-amber-600 shrink-0" />
                  <span>দশমিক ভাগ • অনুপাত শর্টকাট • হটস্পট</span>
                </div>
                <div className="flex items-center justify-between text-xs font-bold text-amber-700 dark:text-amber-400">
                  <span>ভল্ট ওপেন করুন</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </div>

            {/* Stream 6: Leitner 2-Strike Mastery Engine */}
            <div 
              onClick={() => handleDeckNavigate('exam', 'All')}
              className="group p-5 rounded-3xl backdrop-blur-xl bg-gradient-to-br from-emerald-500/10 via-teal-600/5 to-cyan-500/10 ring-1 ring-emerald-500/30 hover:ring-emerald-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/30">
                    🔄 ২-স্ট্রাইক ইঞ্জিন
                  </span>
                  <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/20">
                    ১০০% রিটেনশন
                  </span>
                </div>

                <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-emerald-600 to-teal-500 text-white flex items-center justify-center text-xl shadow-md shadow-emerald-600/25 mb-3 group-hover:scale-105 transition-transform">
                  🔁
                </div>

                <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors mb-1.5">
                  বারবার প্র্যাকটিস (Mastery Re-test)
                </h3>

                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                  ভুল হলে প্রশ্নটি স্বয়ংক্রিয় কিউতে ফিরে আসে। পরপর ২ বার সঠিক উত্তর না দেওয়া পর্যন্ত ঘুরতে থাকে।
                </p>
              </div>

              <div>
                <div className="p-2 rounded-xl bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 text-[11px] font-semibold mb-3 flex items-center gap-1.5">
                  <RotateCcw className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                  <span>ভুল হলে কিউতে রিপিট • ফুল মাস্টারি ড্রিল</span>
                </div>
                <div className="flex items-center justify-between text-xs font-bold text-emerald-700 dark:text-emerald-400">
                  <span>মাস্টারি ড্রিল শুরু</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </div>

          </div>
        </div>
      )}

      {/* =========================================================================
          4. MODEL TESTS & PREDICTOR SETS (When 'model' is selected)
         ========================================================================= */}
      {(activeSegment === 'model' || activeSegment === 'all') && (
        <div className="rounded-3xl backdrop-blur-xl bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80 p-5 shadow-sm">
          <div className="flex items-center justify-between gap-2 mb-4">
            <div>
              <h2 className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
                <Award className="w-4 h-4 text-amber-500" />
                <span>মডেল টেস্ট ও পেপার ফাইনাল এক্সাম</span>
              </h2>
              <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
                রিয়েল এক্সাম হলে বসে টাইমার ও নেগেটিভ মার্কিংসহ পূর্ণাঙ্গ মডেল টেস্ট দিন
              </p>
            </div>
            <button
              onClick={() => handleDeckNavigate('predictor')}
              className="px-3 py-1.5 rounded-xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold shadow-xs flex items-center gap-1 active:scale-95 transition-all cursor-pointer"
            >
              <span>সব সেট</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
            {/* Model Card 1 */}
            <div 
              onClick={() => handleDeckNavigate('predictor')}
              className="p-4 rounded-2xl bg-slate-50/70 dark:bg-slate-800/50 ring-1 ring-slate-200/80 dark:ring-slate-700/80 hover:ring-emerald-500 transition-all cursor-pointer group flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-2">
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/20">
                    🔥 DU Model 01
                  </span>
                  <span className="text-[11px] text-slate-500 flex items-center gap-1 font-mono">
                    <Clock className="w-3 h-3" /> ৪৫ মিনিট
                  </span>
                </div>
                <h4 className="text-sm font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors mb-1">
                  ঢাকা বিশ্ববিদ্যালয় পূর্ণাঙ্গ পেপার ফাইনাল সেট
                </h4>
                <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed mb-3">
                  ৬০টি এমসিকিউ (বায়োলজি, রসায়ন, পদার্থ, উচ্চতর গণিত) + লিখিত অংশ।
                </p>
              </div>
              <div className="flex items-center justify-between text-xs font-bold text-emerald-700 dark:text-emerald-400 pt-2 border-t border-slate-200/60 dark:border-slate-700/60">
                <span>৬০ মার্কস MCQ + লিখিত</span>
                <span className="flex items-center gap-1">টেস্ট দিন <ArrowRight className="w-3.5 h-3.5" /></span>
              </div>
            </div>

            {/* Model Card 2 */}
            <div 
              onClick={() => handleDeckNavigate('predictor')}
              className="p-4 rounded-2xl bg-slate-50/70 dark:bg-slate-800/50 ring-1 ring-slate-200/80 dark:ring-slate-700/80 hover:ring-rose-500 transition-all cursor-pointer group flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-2">
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-500/10 text-rose-700 dark:text-rose-300 ring-1 ring-rose-500/20">
                    🩺 MAT Model 01
                  </span>
                  <span className="text-[11px] text-slate-500 flex items-center gap-1 font-mono">
                    <Clock className="w-3 h-3" /> ৬০ মিনিট
                  </span>
                </div>
                <h4 className="text-sm font-bold text-slate-900 dark:text-white group-hover:text-rose-600 dark:group-hover:text-rose-400 transition-colors mb-1">
                  মেডিকেল ভর্তি পরীক্ষা ১০০ মার্কস মডেল টেস্ট
                </h4>
                <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed mb-3">
                  ১০০টি প্রশ্ন (বায়োলজি ৩০, কেমিস্ট্রি ২৫, ফিজিক্স ২০, ইংলিশ ১৫, জিকে ১০)।
                </p>
              </div>
              <div className="flex items-center justify-between text-xs font-bold text-rose-700 dark:text-rose-400 pt-2 border-t border-slate-200/60 dark:border-slate-700/60">
                <span>১০০ মার্কস থিওরি</span>
                <span className="flex items-center gap-1">টেস্ট দিন <ArrowRight className="w-3.5 h-3.5" /></span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* =========================================================================
          5. SUBJECT-BASED CARDS (When 'subject' or 'all' is active)
         ========================================================================= */}
      {(activeSegment === 'subject' || activeSegment === 'all') && (
        <div className="rounded-3xl backdrop-blur-xl bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80 p-5 shadow-sm">
          <div className="flex items-center justify-between gap-2 mb-4">
            <div>
              <h2 className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-cyan-600 dark:text-cyan-400" />
                <span>বিষয় ভিত্তিক স্পেশাল ড্রিল (Subject-Wise)</span>
              </h2>
              <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
                দুর্বল বিষয় চিহ্নিত করে বিষয়ভিত্তিক গভীর অনুশীলন করুন
              </p>
            </div>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
            {[
              { label: 'Physics' as const, bn: 'পদার্থবিজ্ঞান', icon: '⚛️', count: '৭৫০+ MCQ', color: 'from-blue-500/10 to-indigo-500/10 ring-blue-500/30 text-blue-700 dark:text-blue-300' },
              { label: 'Chemistry' as const, bn: 'রসায়ন', icon: '🧪', count: '৭২০+ MCQ', color: 'from-emerald-500/10 to-teal-500/10 ring-emerald-500/30 text-emerald-700 dark:text-emerald-300' },
              { label: 'Higher Math' as const, bn: 'উচ্চতর গণিত', icon: '📐', count: '৬৫০+ MCQ', color: 'from-cyan-500/10 to-blue-500/10 ring-cyan-500/30 text-cyan-700 dark:text-cyan-300' },
              { label: 'Biology' as const, bn: 'জীববিজ্ঞান', icon: '🧬', count: '৮৫০+ MCQ', color: 'from-rose-500/10 to-pink-500/10 ring-rose-500/30 text-rose-700 dark:text-rose-300' },
              { label: 'English' as const, bn: 'ইংরেজি', icon: '🇬🇧', count: '৩৫০+ MCQ', color: 'from-amber-500/10 to-orange-500/10 ring-amber-500/30 text-amber-700 dark:text-amber-300' },
              { label: 'GK' as const, bn: 'সাধারণ জ্ঞান', icon: '🇧🇩', count: '৩০০+ MCQ', color: 'from-teal-500/10 to-emerald-500/10 ring-teal-500/30 text-teal-700 dark:text-teal-300' },
            ].map((s) => (
              <button
                key={s.label}
                onClick={() => handleDeckNavigate('exam', s.label)}
                className={`p-3.5 rounded-2xl bg-gradient-to-br ${s.color} ring-1 text-left transition-all hover:scale-[1.02] active:scale-95 cursor-pointer shadow-xs`}
              >
                <div className="text-2xl mb-2">{s.icon}</div>
                <div className="text-xs font-black truncate">{s.bn}</div>
                <div className="text-[10px] opacity-80 font-mono mt-0.5">{s.count}</div>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* =========================================================================
          6. VAULT SHORTCUTS (When 'vault' is selected)
         ========================================================================= */}
      {(activeSegment === 'vault' || activeSegment === 'all') && (
        <div className="rounded-3xl backdrop-blur-xl bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80 p-5 shadow-sm">
          <div className="flex items-center justify-between gap-2 mb-3">
            <div>
              <h2 className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
                <Zap className="w-4 h-4 text-amber-500" />
                <span>১-সেকেন্ড ফর্মুলা ও নো-ক্যালকুলেটর ভল্ট শর্টকাট</span>
              </h2>
              <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
                ক্যালকুলেটর ছাড়া দশমিকের ভাগ ও অনুপাত ট্রিকস
              </p>
            </div>
            <button
              onClick={() => handleDeckNavigate('vault')}
              className="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold shadow-xs flex items-center gap-1 active:scale-95 transition-all cursor-pointer"
            >
              <span>ভল্ট এক্সপ্লোর</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            <div 
              onClick={() => handleDeckNavigate('vault', 'Higher Math')}
              className="p-3.5 rounded-2xl bg-amber-500/10 ring-1 ring-amber-500/30 hover:ring-amber-500 cursor-pointer transition-all active:scale-95"
            >
              <div className="text-xs font-black text-amber-900 dark:text-amber-200 mb-1">
                ⚡ নো-ক্যালকুলেটর স্পিড ম্যাথ
              </div>
              <div className="text-[11px] text-slate-600 dark:text-slate-300">
                1/7 = 0.1428, 1/8 = 0.125, √2 = 1.414, √3 = 1.732 দশমিক টেবিল।
              </div>
            </div>

            <div 
              onClick={() => handleDeckNavigate('vault', 'Physics')}
              className="p-3.5 rounded-2xl bg-cyan-500/10 ring-1 ring-cyan-500/30 hover:ring-cyan-500 cursor-pointer transition-all active:scale-95"
            >
              <div className="text-xs font-black text-cyan-900 dark:text-cyan-200 mb-1">
                ⚛️ ফিজিক্স স্প্রিং ও সমান্তরাল অনুপাত
              </div>
              <div className="text-[11px] text-slate-600 dark:text-slate-300">
                তুল্য রোধ, ধারকত্ব এবং SHM দোলনকালের 1-সেকেন্ড স্পিড ফর্মুলা।
              </div>
            </div>

            <div 
              onClick={() => handleDeckNavigate('vault', 'Chemistry')}
              className="p-3.5 rounded-2xl bg-emerald-500/10 ring-1 ring-emerald-500/30 hover:ring-emerald-500 cursor-pointer transition-all active:scale-95"
            >
              <div className="text-xs font-black text-emerald-900 dark:text-emerald-200 mb-1">
                🧪 কেমিস্ট্রি pH ও সংকরায়ন ট্রিকস
              </div>
              <div className="text-[11px] text-slate-600 dark:text-slate-300">
                লগ টেবিল ছাড়া 3 সেকেন্ডে তীব্র ও মৃদু এসিড-ক্ষারকের pH নির্ণয়।
              </div>
            </div>
          </div>
        </div>
      )}

    </div>
  );
};
