import React from 'react';
import { 
  Play, 
  ArrowRight, 
  Layers, 
  Clock, 
  Zap, 
  BookOpen, 
  RotateCcw,
  Sparkles
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
  user,
  onOpenAuth,
  totalSlides,
  totalFlashcards,
  totalQuizzes,
  activeTrack = 'varsity',
  onSelectTrack,
}) => {
  const handleDeckNavigate = (targetMode: AppMode, subject: SubjectType) => {
    onSelectSubject(subject);
    onSelectMode(targetMode);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 py-5 pb-28">
      
      {/* 0. DUAL-TRACK SPRINT COUNTDOWN & ACTIVE SWITCHER */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
        {/* DU 'Ka' - Primary Target */}
        <div 
          onClick={() => onSelectTrack && onSelectTrack('varsity')}
          className={`p-4 rounded-3xl transition-all cursor-pointer border ${
            activeTrack === 'varsity'
              ? 'bg-blue-500/15 border-blue-500 ring-2 ring-blue-500 shadow-md'
              : 'bg-blue-500/5 border-blue-500/20 hover:border-blue-500/40 opacity-80 hover:opacity-100'
          } flex items-center justify-between group`}
        >
          <div className="flex items-center gap-3">
            <span className="text-2xl group-hover:scale-110 transition-transform">🎯</span>
            <div>
              <div className="flex items-center gap-1.5 flex-wrap">
                <span className="text-xs sm:text-sm font-black text-blue-900 dark:text-blue-200">
                  ঢাকা বিশ্ববিদ্যালয় 'ক' (DU 'Ka' - মেইন টার্গেট)
                </span>
                {activeTrack === 'varsity' && (
                  <span className="px-2 py-0.5 rounded-full text-[9px] font-black bg-blue-600 text-white shadow-xs">
                    ✓ সক্রিয় মেইন ট্র্যাক
                  </span>
                )}
              </div>
              <div className="text-[11px] text-zinc-600 dark:text-zinc-400 font-medium">
                বাকি আর মাত্র ২৫ দিন! (MCQ ৬০ + লিখিত ৪০ = ১০০ নম্বর | No-Calculator)
              </div>
            </div>
          </div>
          <span className={`px-2.5 py-1 rounded-xl text-white font-mono text-[11px] font-extrabold shrink-0 shadow-xs transition-colors ${
            activeTrack === 'varsity' ? 'bg-blue-600' : 'bg-zinc-500 group-hover:bg-blue-600'
          }`}>
            {activeTrack === 'varsity' ? 'Active' : 'সুইচ করুন'}
          </span>
        </div>

        {/* Medical - Secondary / Backup Target */}
        <div 
          onClick={() => onSelectTrack && onSelectTrack('medical')}
          className={`p-4 rounded-3xl transition-all cursor-pointer border ${
            activeTrack === 'medical'
              ? 'bg-rose-500/15 border-rose-500 ring-2 ring-rose-500 shadow-md'
              : 'bg-rose-500/5 border-rose-500/20 hover:border-rose-500/40 opacity-80 hover:opacity-100'
          } flex items-center justify-between group`}
        >
          <div className="flex items-center gap-3">
            <span className="text-2xl group-hover:scale-110 transition-transform">🩺</span>
            <div>
              <div className="flex items-center gap-1.5 flex-wrap">
                <span className="text-xs sm:text-sm font-black text-rose-900 dark:text-rose-200">
                  মেডিকেল ভর্তি পরীক্ষা (MAT 2026-27 - ব্যাকআপ)
                </span>
                {activeTrack === 'medical' && (
                  <span className="px-2 py-0.5 rounded-full text-[9px] font-black bg-rose-600 text-white shadow-xs">
                    ✓ সক্রিয় ট্র্যাক
                  </span>
                )}
              </div>
              <div className="text-[11px] text-zinc-600 dark:text-zinc-400 font-medium">
                বাকি আর মাত্র ১৫–২০ দিন! (Bio 30, Chem 25, Phys 20, Eng 15, GK 10)
              </div>
            </div>
          </div>
          <span className={`px-2.5 py-1 rounded-xl text-white font-mono text-[11px] font-extrabold shrink-0 shadow-xs transition-colors ${
            activeTrack === 'medical' ? 'bg-rose-600' : 'bg-zinc-500 group-hover:bg-rose-600'
          }`}>
            {activeTrack === 'medical' ? 'Active' : 'সুইচ করুন'}
          </span>
        </div>
      </div>

      {/* DUAL-TARGET SYNERGY STRATEGY CALLOUT */}
      <div className="mb-5 p-4 rounded-3xl bg-gradient-to-r from-blue-500/10 via-indigo-500/5 to-emerald-500/10 border border-blue-500/20 dark:border-blue-500/30 flex flex-col md:flex-row md:items-center justify-between gap-3 shadow-xs">
        <div className="flex items-start gap-3">
          <span className="text-2xl mt-0.5">💡</span>
          <div>
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-xs font-black text-zinc-900 dark:text-white uppercase tracking-wider">
                ডুয়াল-টার্গেট ৮০/২০ স্টাডি কৌশল:
              </span>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-600 text-white">
                মেইন টার্গেট: ঢাবি 'ক' (৭০% সময়)
              </span>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-600 text-white">
                সেকেন্ডারি এক্সাম: মেডিকেল (৩০% সময়)
              </span>
            </div>
            <p className="text-xs text-zinc-600 dark:text-zinc-300 mt-1 leading-relaxed">
              <strong>সিলেবাসের মিল নেই, কিন্তু কনফ্লিক্ট কেন নেই?</strong> ফিজিক্স ও কেমিস্ট্রি যদি ভার্সিটির জন্য ম্যাথসহ ডিপ প্রিপারেশন নাও, তবে মেডিকেলের ফিজিক্স ও কেমিস্ট্রি থিওরি পানির মতো সহজ লাগবে। আলাদা শুধু: মেডিকেলের <strong>বায়োলজি ছক (আজমল/হাসান)</strong> এবং <strong>ইংলিশ (১৫) + জিকে (১০)</strong>। দিনে মাত্র ১.৫–২ ঘণ্টা এই সেকশনে দিলে মূল ভার্সিটি প্রস্তুতিতে কোনো প্রভাব না ফেলেই মেডিকেলে টপ স্কোর সম্ভব!
            </p>
          </div>
        </div>
      </div>

      {/* 1. TOP 100 PARETO 80/20 COMMAND PILLARS (DYNAMICALLY TAILORED) */}
      <div className="mb-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        {activeTrack === 'varsity' ? (
          <>
            {/* Varsity Pillar 1: No-Calc Math */}
            <div 
              onClick={() => handleDeckNavigate('vault', 'Higher Math')}
              className="p-4 rounded-3xl bg-amber-500/10 dark:bg-amber-950/20 border border-amber-500/30 hover:border-amber-500 transition-all cursor-pointer group hover:scale-[1.02] shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xl">⚡</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500 text-white uppercase shadow-xs">
                    Calculation Fix
                  </span>
                </div>
                <h4 className="text-sm font-extrabold text-amber-900 dark:text-amber-200 group-hover:text-amber-700 dark:group-hover:text-amber-300 transition-colors">
                  নো-ক্যালকুলেটর স্পিড ম্যাথ
                </h4>
                <p className="text-[11px] text-zinc-600 dark:text-zinc-400 mt-1 leading-relaxed">
                  ভেক্টর ট্রিপলেট, আনুমানিক বর্গমূল ও লগ হ্যাক এবং ক্যালকুলেটরহীন দ্রাব্যতা ও বাফার pH।
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-amber-500/20 flex items-center justify-between text-[11px] font-bold text-amber-800 dark:text-amber-300">
                <span>ট্রিপলেট ও হ্যাক খুলুন</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Varsity Pillar 2: DU Written 40 Marks */}
            <div 
              onClick={() => handleDeckNavigate('predictor', 'Higher Math')}
              className="p-4 rounded-3xl bg-blue-500/10 dark:bg-blue-950/20 border border-blue-500/30 hover:border-blue-500 transition-all cursor-pointer group hover:scale-[1.02] shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xl">✍️</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-600 text-white uppercase shadow-xs">
                    Zero to 40 Marks
                  </span>
                </div>
                <h4 className="text-sm font-extrabold text-blue-900 dark:text-blue-200 group-hover:text-blue-700 dark:group-hover:text-blue-300 transition-colors">
                  ঢাবি লিখিত ৪০-মার্ক ড্রিল
                </h4>
                <p className="text-[11px] text-zinc-600 dark:text-zinc-400 mt-1 leading-relaxed">
                  ১৬টি টু-দ্য-পয়েন্ট সমস্যা (৪×২.৫) ও প্রতিটি সমস্যার স্টেপ-মার্কিং নম্বর বণ্টন রুব্রিক।
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-blue-500/20 flex items-center justify-between text-[11px] font-bold text-blue-800 dark:text-blue-300">
                <span>লিখিত সমস্যা ও রুব্রিক</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Varsity Pillar 3: Higher Math Shortcuts & Conics/Calculus */}
            <div 
              onClick={() => handleDeckNavigate('exam', 'Higher Math')}
              className="p-4 rounded-3xl bg-indigo-500/10 dark:bg-indigo-950/20 border border-indigo-500/30 hover:border-indigo-500 transition-all cursor-pointer group hover:scale-[1.02] shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xl">📐</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-indigo-600 text-white uppercase shadow-xs">
                    Math High-Yield
                  </span>
                </div>
                <h4 className="text-sm font-extrabold text-indigo-900 dark:text-indigo-200 group-hover:text-indigo-700 dark:group-hover:text-indigo-300 transition-colors">
                  উচ্চতর গণিত কোর ট্রিকস
                </h4>
                <p className="text-[11px] text-zinc-600 dark:text-zinc-400 mt-1 leading-relaxed">
                  লা হসপিটাল রুল, কনিকের স্পর্শক ও উপকেন্দ্র, ম্যাট্রিক্স নির্ণায়ক ও দ্রুত ইন্টিগ্রেশন।
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-indigo-500/20 flex items-center justify-between text-[11px] font-bold text-indigo-800 dark:text-indigo-300">
                <span>গণিত প্র্যাকটিস খুলুন</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Varsity Pillar 4: Medical Secondary Booster (Eng 15 + GK 10 + Bio Tables) */}
            <div 
              onClick={() => {
                if (onSelectTrack) onSelectTrack('medical');
                handleDeckNavigate('predictor', 'English');
              }}
              className="p-4 rounded-3xl bg-rose-500/10 dark:bg-rose-950/20 border border-rose-500/30 hover:border-rose-500 transition-all cursor-pointer group hover:scale-[1.02] shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xl">🩺</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-600 text-white uppercase shadow-xs">
                    Medical Booster
                  </span>
                </div>
                <h4 className="text-sm font-extrabold text-rose-900 dark:text-rose-200 group-hover:text-rose-700 dark:group-hover:text-rose-300 transition-colors">
                  মেডিকেল ব্যাকআপ বুস্টার
                </h4>
                <p className="text-[11px] text-zinc-600 dark:text-zinc-400 mt-1 leading-relaxed">
                  দিনে মাত্র ১ ঘণ্টা: ইংলিশ (১৫) + জিকে (১০) রেশিও ও জীববিজ্ঞান পাঠ্যবই ছক।
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-rose-500/20 flex items-center justify-between text-[11px] font-bold text-rose-800 dark:text-rose-300">
                <span>মেডিকেল ক্যাপসুল ওপেন করুন</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </div>
          </>
        ) : (
          <>
            {/* Medical Pillar 1: English (15) + GK (10) */}
            <div 
              onClick={() => handleDeckNavigate('predictor', 'English')}
              className="p-4 rounded-3xl bg-emerald-500/10 dark:bg-emerald-950/20 border border-emerald-500/30 hover:border-emerald-500 transition-all cursor-pointer group hover:scale-[1.02] shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xl">🇬🇧🇧🇩</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-600 text-white uppercase shadow-xs">
                    ২৫ / ২৫ টার্গেট
                  </span>
                </div>
                <h4 className="text-sm font-extrabold text-emerald-900 dark:text-emerald-200 group-hover:text-emerald-700 dark:group-hover:text-emerald-300 transition-colors">
                  ইংলিশ (১৫) + জিকে (১০) রেশিও
                </h4>
                <p className="text-[11px] text-zinc-600 dark:text-zinc-400 mt-1 leading-relaxed">
                  অফিসিয়াল MAT রেশিও: Prepositions, Vocab ও ১৯৭১ মুক্তিযুদ্ধ, সেক্টর, সংবিধান ও জাতিসংঘ।
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-emerald-500/20 flex items-center justify-between text-[11px] font-bold text-emerald-800 dark:text-emerald-300">
                <span>২৫ মার্কস স্পেশাল টেস্ট</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Medical Pillar 2: Biology Tables & Exceptions */}
            <div 
              onClick={() => handleDeckNavigate('flashcards', 'Biology')}
              className="p-4 rounded-3xl bg-rose-500/10 dark:bg-rose-950/20 border border-rose-500/30 hover:border-rose-500 transition-all cursor-pointer group hover:scale-[1.02] shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xl">🧬</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-600 text-white uppercase shadow-xs">
                    Bio 30 Marks
                  </span>
                </div>
                <h4 className="text-sm font-extrabold text-rose-900 dark:text-rose-200 group-hover:text-rose-700 dark:group-hover:text-rose-300 transition-colors">
                  আজমল ও হাসান স্যারের ছক
                </h4>
                <p className="text-[11px] text-zinc-600 dark:text-zinc-400 mt-1 leading-relaxed">
                  উদ্ভিদ ও প্রাণিবিজ্ঞান পাঠ্যবইয়ের সরাসরি ছক, বৈজ্ঞানিক নাম ও মেডিকেল ট্র্যাপ প্রতিরক্ষা।
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-rose-500/20 flex items-center justify-between text-[11px] font-bold text-rose-800 dark:text-rose-300">
                <span>ব্যতিক্রম ছক ও কার্ডস</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Medical Pillar 3: Chemistry Hazari Lines */}
            <div 
              onClick={() => handleDeckNavigate('flashcards', 'Chemistry')}
              className="p-4 rounded-3xl bg-purple-500/10 dark:bg-purple-950/20 border border-purple-500/30 hover:border-purple-500 transition-all cursor-pointer group hover:scale-[1.02] shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xl">🧪</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-purple-600 text-white uppercase shadow-xs">
                    Chem 25 Marks
                  </span>
                </div>
                <h4 className="text-sm font-extrabold text-purple-900 dark:text-purple-200 group-hover:text-purple-700 dark:group-hover:text-purple-300 transition-colors">
                  হাজারী-নাগ তথ্য ও ব্যতিক্রম
                </h4>
                <p className="text-[11px] text-zinc-600 dark:text-zinc-400 mt-1 leading-relaxed">
                  দ্রাব্যতা নীতি, কোয়ান্টাম সংখ্যা, বাফার দ্রবণ ও জৈব রসায়নের শনাক্তকারী পরীক্ষা।
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-purple-500/20 flex items-center justify-between text-[11px] font-bold text-purple-800 dark:text-purple-300">
                <span>কেমিস্ট্রি কার্ডস দেখুন</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Medical Pillar 4: Physics Units, Dimensions & Formulas */}
            <div 
              onClick={() => handleDeckNavigate('vault', 'Physics')}
              className="p-4 rounded-3xl bg-blue-500/10 dark:bg-blue-950/20 border border-blue-500/30 hover:border-blue-500 transition-all cursor-pointer group hover:scale-[1.02] shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xl">⚛️</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-600 text-white uppercase shadow-xs">
                    Phys 20 Marks
                  </span>
                </div>
                <h4 className="text-sm font-extrabold text-blue-900 dark:text-blue-200 group-hover:text-blue-700 dark:group-hover:text-blue-300 transition-colors">
                  ইসহাক স্যারের একক, মাত্রা ও সূত্র
                </h4>
                <p className="text-[11px] text-zinc-600 dark:text-zinc-400 mt-1 leading-relaxed">
                  ক্যালকুলেটরবিহীন সোজা সূত্র প্রয়োগ, ধ্রুবকের মান ও বহুল পুনরাবৃত্ত একক-মাত্রা।
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-blue-500/20 flex items-center justify-between text-[11px] font-bold text-blue-800 dark:text-blue-300">
                <span>ফিজিক্স ফর্মুলা ভল্ট</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </div>
          </>
        )}
      </div>

      {/* 2. SYLLABUS & CHAPTER SCOPE ROADMAP (TRANSPARENT BOUNDARIES) */}
      <div className="mb-6 p-5 rounded-3xl bg-white dark:bg-zinc-900 border border-zinc-200/90 dark:border-zinc-800 shadow-sm">
        <div className="flex items-center justify-between pb-3 border-b border-zinc-100 dark:border-zinc-800 mb-4 flex-wrap gap-2">
          <div className="flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-[#056839] dark:text-emerald-400" />
            <h3 className="text-base font-extrabold text-zinc-900 dark:text-white">
              সিলেবাস ও অধ্যায় কভারেজ ট্র্যাকার (Syllabus Scope Breakdown)
            </h3>
          </div>
          <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/40 text-[#056839] dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800">
            এইচএসসি সংক্ষিপ্ত সিলেবাস কোর
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5">
          <div className="p-3.5 rounded-2xl bg-zinc-50 dark:bg-zinc-800/50 border border-zinc-200/80 dark:border-zinc-700/80">
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-xs font-bold text-emerald-700 dark:text-emerald-400 font-mono">
                Week 01 Scope
              </span>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300">
                ভিত্তি অধ্যায়
              </span>
            </div>
            <p className="text-xs text-zinc-700 dark:text-zinc-300 leading-relaxed font-medium">
              ভেক্টর, গতিবিদ্যা, পরিমাণগত রসায়ন, সরলরেখা, রক্ত ও সংবহন, শ্বসন ও শ্বাসক্রিয়া।
            </p>
          </div>

          <div className="p-3.5 rounded-2xl bg-zinc-50 dark:bg-zinc-800/50 border border-zinc-200/80 dark:border-zinc-700/80">
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-xs font-bold text-blue-700 dark:text-blue-400 font-mono">
                Week 02 Scope
              </span>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-100 dark:bg-blue-950/60 text-blue-800 dark:text-blue-300">
                বলবিদ্যা ও বাফার
              </span>
            </div>
            <p className="text-xs text-zinc-700 dark:text-zinc-300 leading-relaxed font-medium">
              নিউটোনীয় বলবিদ্যা, পর্যায়বৃত্ত ধর্ম ও বন্ধন, রাসায়নিক পরিবর্তন (বাফার ও pH), বৃত্ত ও জটিল সংখ্যা, কোষ ও হাইড্রা।
            </p>
          </div>

          <div className="p-3.5 rounded-2xl bg-zinc-50 dark:bg-zinc-800/50 border border-zinc-200/80 dark:border-zinc-700/80">
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-xs font-bold text-amber-700 dark:text-amber-400 font-mono">
                Week 03 Scope
              </span>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-300">
                কণিক ও গুণগত
              </span>
            </div>
            <p className="text-xs text-zinc-700 dark:text-zinc-300 leading-relaxed font-medium">
              কাজ-শক্তি, মহাকর্ষ, গুণগত রসায়ন (Ksp ও কোয়ান্টাম), কণিক ও অসমতা, উদ্ভিদ শারীরতত্ত্ব ও প্রজনন।
            </p>
          </div>
        </div>
      </div>

      {/* 3. ORIGINAL WELCOME BANNER */}
      <div className="mb-5">
        <div className="bg-white dark:bg-zinc-900 rounded-3xl p-5 sm:p-6 border border-zinc-200/80 dark:border-zinc-800 shadow-sm relative overflow-hidden">
          <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div className="flex items-center gap-2 mb-2 flex-wrap">
                <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 flex items-center gap-1.5 shadow-xs">
                  <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                  Bangladesh Admission Core 2026
                </span>
                <span className={`inline-flex px-2.5 py-0.5 rounded-full text-xs font-bold border ${
                  activeTrack === 'medical'
                    ? 'bg-rose-500/10 text-rose-700 dark:text-rose-300 border-rose-500/20'
                    : 'bg-blue-500/10 text-blue-700 dark:text-blue-300 border-blue-500/20'
                }`}>
                  {activeTrack === 'medical' ? '🩺 মেডিকেল ট্র্যাক (Bio, Chem, Phys, Eng, GK)' : "🎯 ঢাবি 'ক' ট্র্যাক (Phys, Chem, Math, Bio)"}
                </span>
                <span className="hidden sm:inline-flex px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-700 dark:text-cyan-300 border border-cyan-500/20">
                  ⚡ {totalSlides}টি স্লাইড
                </span>
                <span className="inline-flex px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-700 dark:text-amber-300 border border-amber-500/20">
                  📚 {totalQuizzes}টি আইসোলেটেড MCQ
                </span>
                <button
                  onClick={() => onSelectMode('predictor')}
                  className="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full text-xs font-bold bg-amber-500 text-white shadow-xs hover:bg-amber-600 transition-all cursor-pointer"
                >
                  <Sparkles className="w-3 h-3 fill-current" />
                  <span>🔮 প্রেডিকশন ভল্ট ওপেন করুন</span>
                </button>
              </div>
              <h1 className="text-xl sm:text-2xl md:text-3xl font-extrabold text-zinc-900 dark:text-white tracking-tight leading-snug">
                {user.isLoggedIn && user.name ? `স্বাগতম, ${user.name}!` : 'ভর্তি প্রস্তুতি ২০২৬:'} {activeTrack === 'medical' ? 'মেডিকেল স্পেশাল পাঠ্যবই কোর ও ১৫ বছরের রিপিট' : "ঢাবি 'ক' স্পেশাল নো-ক্যালকুলেটর শর্টকাট ও কোর"}
              </h1>
              <p className="text-xs sm:text-sm text-zinc-600 dark:text-zinc-400 mt-1 max-w-2xl leading-relaxed">
                {activeTrack === 'medical'
                  ? 'গাজী আজমল, আবুল হাসান, হাজারী-নাগ ও ইসহাক স্যারের পাঠ্যবইয়ের দাগানো লাইন, ব্যতিক্রম ছক এবং বিগত ১৫ বছরের মেডিকেল (MAT) ও ডেন্টাল (DAT) এর নির্ভুল প্রশ্ন।'
                  : "ঢাকা বিশ্ববিদ্যালয়ের ১৫ বছরের প্রশ্নব্যাংক, কেতাব উদ্দীন স্যারের গণিত, হাজারী-নাগের রসায়ন ও ইসহাক স্যারের পদার্থবিজ্ঞানের ক্যালকুলেটরহীন দ্রুত সমাধান ও লিখিত সমস্যা।"}
              </p>
            </div>

            {/* User status or Google sign-in */}
            <div className="flex items-center gap-3 shrink-0">
              {user.isLoggedIn ? (
                <div 
                  onClick={onOpenAuth}
                  className="cursor-pointer p-2.5 sm:p-3 rounded-2xl bg-[#F6F8F6] dark:bg-zinc-800/80 border border-zinc-200/80 dark:border-zinc-700/80 flex items-center gap-3 hover:scale-102 transition-all shadow-xs"
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
                  className="py-2.5 px-4 rounded-2xl bg-white dark:bg-zinc-800 hover:bg-zinc-50 dark:hover:bg-zinc-700 text-zinc-800 dark:text-white text-xs font-bold border border-zinc-300 dark:border-zinc-700 shadow-xs flex items-center gap-2 transition-all hover:scale-105 active:scale-95 cursor-pointer"
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

      {/* 2. SPECIAL HERO CALLOUT: বারবার প্র্যাকটিস (MASTERY RE-TEST ENGINE) */}
      <div 
        onClick={() => handleDeckNavigate('exam', 'All')}
        className="mb-6 bg-gradient-to-r from-[#056839] via-[#008f5d] to-[#00B09B] rounded-3xl p-4 sm:p-5 text-white shadow-lg shadow-[#056839]/20 cursor-pointer hover:shadow-xl transition-all group border border-white/20"
      >
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-3.5">
            <div className="w-12 h-12 rounded-2xl bg-white/20 backdrop-blur-md flex items-center justify-center shrink-0 border border-white/30 group-hover:scale-110 transition-transform">
              <RotateCcw className="w-6 h-6 text-white animate-spin-slow" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-black uppercase tracking-wider bg-white/25 px-2.5 py-0.5 rounded-full border border-white/30">
                  🔥 Active Drill
                </span>
                <span className="text-xs text-white/90 font-medium">
                  Leitner 2-Strike Mastery
                </span>
              </div>
              <h3 className="text-lg sm:text-xl font-black mt-0.5">
                বারবার প্র্যাকটিস (Mastery Re-test Mode)
              </h3>
              <p className="text-xs sm:text-sm text-white/90">
                ভুল বা "Unsure" হলে প্রশ্নটি কিউতে থাকবে; পরপর <strong>২ বার সঠিক</strong> না দেওয়া পর্যন্ত অটো-রিপিট ড্রিল চলবে।
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 shrink-0">
            <span className="px-5 py-2.5 rounded-2xl bg-white text-[#056839] font-black text-xs sm:text-sm shadow-md group-hover:bg-white/95 flex items-center gap-1.5 transition-all">
              <span>মাস্টারি ড্রিল শুরু</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </span>
          </div>
        </div>
      </div>

      {/* 3. FOUR CORE BANGLADESH ADMISSION DECKS */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5 sm:gap-6">
        
        {/* CARD 1: Medical Precision Deck */}
        <div 
          className="bg-gradient-to-br from-[#E52D27] to-[#B31217] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 active:scale-[0.99] border border-white/20 relative group overflow-hidden"
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/15 pointer-events-none rounded-3xl" />

          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-white shadow-xs flex items-center gap-1.5 border border-white/25">
                <span className="w-2 h-2 rounded-full bg-white animate-ping" />
                🩺 Medical Precision
              </span>
              <span className="bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-semibold text-white/95 border border-white/20">
                MAT/DAT ১৫ বছর রিপিট
              </span>
            </div>
            <div className="bg-white/15 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5 border border-white/20">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              গাজী আজমল ও হাজারী-নাগ
            </div>
          </div>

          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-xs font-['Outfit']">
              Medical Precision Deck
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              গাজী আজমল ও হাজারী-নাগ স্যারের বইয়ের হুবহু লাইন, গুরুত্বপূর্ণ ছক ও মেডিকেল (MAT/DAT) বিগত ১৫ বছরের রিপিট প্রশ্ন সম্ভার।
            </p>
          </div>

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                ✎ 75 Questions
              </span>
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                🗂️ 60 Cards
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDeckNavigate('slides', 'Biology')}
                className="px-3 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs backdrop-blur-md border border-white/30 transition-all flex items-center gap-1 cursor-pointer"
              >
                <BookOpen className="w-3.5 h-3.5" />
                কনসেপ্ট
              </button>
              <button
                onClick={() => handleDeckNavigate('exam', 'Biology')}
                className="px-4 py-2 rounded-xl bg-white text-[#B31217] font-bold text-xs shadow-md hover:bg-white/95 transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                প্র্যাকটিস
              </button>
            </div>
          </div>
        </div>

        {/* CARD 2: DU 'Ka' Core Deck */}
        <div 
          className="bg-gradient-to-br from-[#00B09B] to-[#96C93D] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 active:scale-[0.99] border border-white/20 relative group overflow-hidden"
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/15 pointer-events-none rounded-3xl" />

          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-white shadow-xs flex items-center gap-1.5 border border-white/25">
                🏆 DU 'Ka' Core
              </span>
              <span className="bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-semibold text-white/95 border border-white/20">
                ১৫-২০ বছর PYQ
              </span>
            </div>
            <div className="bg-white/15 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5 border border-white/20">
              <span className="w-2 h-2 rounded-full bg-amber-300" />
              নো-ক্যালকুলেটর &lt; ৪৫ সে
            </div>
          </div>

          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-xs font-['Outfit']">
              DU 'Ka' Unit Core Deck
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিটের বিগত ১৫-২০ বছরের প্রশ্ন এবং ইসহাক ও কেতাব উদ্দীন স্যারের বইয়ের সরাসরি স্ট্যান্ডার্ড ম্যাথ।
            </p>
          </div>

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                ✎ 75 Questions
              </span>
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                🗂️ 50 Cards
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDeckNavigate('slides', 'Higher Math')}
                className="px-3 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs backdrop-blur-md border border-white/30 transition-all flex items-center gap-1 cursor-pointer"
              >
                <BookOpen className="w-3.5 h-3.5" />
                কনসেপ্ট
              </button>
              <button
                onClick={() => handleDeckNavigate('exam', 'Higher Math')}
                className="px-4 py-2 rounded-xl bg-white text-[#056839] font-bold text-xs shadow-md hover:bg-white/95 transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                প্র্যাকটিস
              </button>
            </div>
          </div>
        </div>

        {/* CARD 3: Varsity Core Deck (RU, JU, CU, GST) */}
        <div 
          className="bg-gradient-to-br from-[#0052D4] to-[#4364F7] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 active:scale-[0.99] border border-white/20 relative group overflow-hidden"
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/15 pointer-events-none rounded-3xl" />

          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-white shadow-xs flex items-center gap-1.5 border border-white/25">
                🏛️ Varsity Core
              </span>
              <span className="bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-semibold text-white/95 border border-white/20">
                RU • JU • CU • GST
              </span>
            </div>
            <div className="bg-white/15 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5 border border-white/20">
              <span className="w-2 h-2 rounded-full bg-cyan-300" />
              নিউমেরিক্যাল ভ্যারিয়েশন
            </div>
          </div>

          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-xs font-['Outfit']">
              Varsity Core Deck (RU, JU, CU, GST)
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              রাজশাহী, জাহাঙ্গীরনগর, চট্টগ্রাম ও গুচ্ছ বিশ্ববিদ্যালয়ের প্রশ্নব্যাংক প্যাটার্ন ও বারবার আসা সংখ্যাগত পরিবর্তনের পূর্ণাঙ্গ রি-টেস্ট।
            </p>
          </div>

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                ✎ 75 Questions
              </span>
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                🗂️ 50 Cards
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDeckNavigate('slides', 'Physics')}
                className="px-3 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs backdrop-blur-md border border-white/30 transition-all flex items-center gap-1 cursor-pointer"
              >
                <BookOpen className="w-3.5 h-3.5" />
                কনসেপ্ট
              </button>
              <button
                onClick={() => handleDeckNavigate('exam', 'Physics')}
                className="px-4 py-2 rounded-xl bg-white text-[#0052D4] font-bold text-xs shadow-md hover:bg-white/95 transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                প্র্যাকটিস
              </button>
            </div>
          </div>
        </div>

        {/* CARD 4: English & 1971 Liberation War GK Core Deck */}
        <div 
          className="bg-gradient-to-br from-[#8A2387] via-[#E94057] to-[#F27121] rounded-3xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 active:scale-[0.99] border border-white/20 relative group overflow-hidden"
        >
          <div className="absolute inset-0 bg-gradient-to-tr from-white/10 via-transparent to-white/15 pointer-events-none rounded-3xl" />

          <div className="flex items-center justify-between gap-2 mb-4 relative z-10 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-white shadow-xs flex items-center gap-1.5 border border-white/25">
                🇬🇧 English &amp; 🇧🇩 GK Core
              </span>
              <span className="bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-semibold text-white/95 border border-white/20">
                BCS • MAT • DU
              </span>
            </div>
            <div className="bg-white/15 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-white/90 flex items-center gap-1.5 border border-white/20">
              <span className="w-2 h-2 rounded-full bg-rose-300" />
              ১০০% নিশ্চিত মার্কস
            </div>
          </div>

          <div className="relative z-10 mb-5">
            <h2 className="text-2xl font-black tracking-tight text-white mb-2 drop-shadow-xs font-['Outfit']">
              English &amp; Liberation War GK Deck
            </h2>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              Appropriate Prepositions, বিসিএস ও মেডিকেলের রিপিটেড গ্রামার এবং ১৯৭১ মুক্তিযুদ্ধ ও বাংলাদেশ কোর জিকে অপরিহার্য তথ্যম্যাট্রিক্স।
            </p>
          </div>

          <div className="relative z-10 flex items-center justify-between pt-3 border-t border-white/20 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                ✎ 50 Questions
              </span>
              <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-xl text-xs font-bold text-white flex items-center gap-1 border border-white/20">
                🗂️ 90 Cards
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDeckNavigate('flashcards', 'English')}
                className="px-3 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs backdrop-blur-md border border-white/30 transition-all flex items-center gap-1 cursor-pointer"
              >
                <Layers className="w-3.5 h-3.5" />
                কার্ডস
              </button>
              <button
                onClick={() => handleDeckNavigate('exam', 'English')}
                className="px-4 py-2 rounded-xl bg-white text-[#8A2387] font-bold text-xs shadow-md hover:bg-white/95 transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                প্র্যাকটিস
              </button>
            </div>
          </div>
        </div>

      </div>

      {/* 4. QUICK LAUNCH SHORTCUTS & VAULT HIGHLIGHTS */}
      <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Shortcut 1: Calculator Free Vault */}
        <div 
          onClick={() => handleDeckNavigate('vault', 'All')}
          className="bg-white dark:bg-zinc-900 p-4 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 hover:border-[#056839]/50 shadow-xs cursor-pointer transition-all hover:-translate-y-0.5 group"
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
          className="bg-white dark:bg-zinc-900 p-4 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 hover:border-[#00B09B]/50 shadow-xs cursor-pointer transition-all hover:-translate-y-0.5 group"
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
                এক্টিভ রিকল ও স্পেসড রিপিটেশন
              </p>
            </div>
          </div>
        </div>

        {/* Shortcut 3: Real Test (-0.25) */}
        <div 
          onClick={() => handleDeckNavigate('exam', 'All')}
          className="bg-white dark:bg-zinc-900 p-4 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 hover:border-rose-500/50 shadow-xs cursor-pointer transition-all hover:-translate-y-0.5 group"
        >
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-rose-500/10 text-rose-600 dark:text-rose-400 group-hover:bg-rose-600 group-hover:text-white transition-colors">
              <Clock className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white flex items-center gap-1">
                {totalQuizzes}টি কোর টেস্ট (-০.২৫)
                <ArrowRight className="w-3.5 h-3.5 text-zinc-400 group-hover:translate-x-1 transition-transform" />
              </h3>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">
                ৪৫ সেকেন্ড টাইমার ও ট্র্যাপ ডিফেন্স
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
