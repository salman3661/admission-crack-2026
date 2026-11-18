import React from 'react';
import {
  Target,
  Sparkles,
  BookX,
  BarChart3,
  ClipboardList,
  Layers,
  BookMarked,
  FileJson,
  Zap,
  Flame,
  ArrowRight,
  Clock,
} from 'lucide-react';
import { BANK_INDEX, getErrorLog, getMockTracker } from '../lib/library';
import { useSEO } from '../lib/seo';

export interface HomeHubViewProps {
  activeTrack: 'varsity' | 'medical';
  onNavigate: (path: string) => void;
}

export const HomeHubView: React.FC<HomeHubViewProps> = ({ activeTrack, onNavigate }) => {
  const isMedical = activeTrack === 'medical';
  const errorCount = getErrorLog().length;
  const dueCount = getErrorLog().filter((e) => new Date(e.retestDue).getTime() <= Date.now()).length;
  const mockCount = getMockTracker().length;

  useSEO({
    title: "Admission Crack 2026 | DU 'Ka' & Medical (MAT) Prep Engine",
    description: `${BANK_INDEX.total_questions}টি যাচাইকৃত প্রশ্ন, Master Set A/B/C, Real Exam Simulator, Mistake Book ও Weakness Radar — DU Ka ও MAT প্রস্তুতির সম্পূর্ণ ইঞ্জিন।`,
    path: '/',
  });

  const examMcqCount = isMedical
    ? (BANK_INDEX.by_exam.mat || 0) + (BANK_INDEX.by_exam.other || 0)
    : (BANK_INDEX.by_exam.du_ka || 0) + (BANK_INDEX.by_exam.other || 0);

  const cards = [
    {
      path: '/simulator',
      title: '🎯 Real Exam Simulator',
      badge: isMedical ? '৭৫ মি · ১০০ MCQ' : '৪৫+৪৫ মি · ৬০ MCQ + ৪০ লিখিত',
      desc: 'আসল পরীক্ষার টাইমার, −০.২৫ নেগেটিভ মার্কিং ও লিখিত খালি-সতর্কতাসহ পূর্ণাঙ্গ পরীক্ষা।',
      accent: 'from-emerald-600 to-teal-600 text-white',
      icon: Target,
      primary: true,
    },
    {
      path: '/master-set',
      title: '⚡ Master Sets (SET A / B / C)',
      badge: isMedical
        ? `${BANK_INDEX.master_sets.mat_set_a} + ${BANK_INDEX.master_sets.mat_set_b} + ${BANK_INDEX.master_sets.mat_set_c} প্রশ্ন`
        : `${BANK_INDEX.master_sets.du_ka_set_a} + ${BANK_INDEX.master_sets.du_ka_set_b} + ${BANK_INDEX.master_sets.du_ka_set_c} প্রশ্ন`,
      desc: 'LEARN→PREDICT→SELECT মডেলের ভিত্তিতে নির্বাচিত ২৬–২৭ এর সম্ভাব্য প্রশ্ন সেট।',
      accent: 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800',
      icon: Sparkles,
    },
    {
      path: '/mistake-book',
      title: '📕 Mistake Book (Error Log)',
      badge: dueCount > 0 ? `${dueCount}টি আজ Due` : `${errorCount}টি ভুল লগ`,
      desc: 'SM-2 ব্যবধানে (১ / ৩ / ৭ / ১৪ দিন) ভুল প্রশ্ন পুনরায় টেস্ট এবং কারণ লগ।',
      accent: 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800',
      icon: BookX,
    },
    {
      path: '/weakness-radar',
      title: '📊 Weakness Radar',
      badge: 'অধ্যায়ভিত্তিক ক্ষতি',
      desc: 'কোন অধ্যায়ে কত নম্বর হারিয়েছো তার চার্ট ও এক-ক্লিক দুর্বল অধ্যায় ড্রিল।',
      accent: 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800',
      icon: BarChart3,
    },
    {
      path: '/mock-tracker',
      title: '📋 Mock Tracker',
      badge: `${mockCount}টি মক সেভড`,
      desc: 'Paper Final, Subject Final ও Model Test 1–5 এর স্কোর ও Top-3 লসি চ্যাপ্টার।',
      accent: 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800',
      icon: ClipboardList,
    },
    {
      path: '/chapters',
      title: '🗂 Chapter Explorer',
      badge: `${BANK_INDEX.chapters.length}টি অধ্যায়`,
      desc: 'প্রতিটি অধ্যায়ের প্রশ্নসংখ্যা, কত বছরে এসেছে ও ২৬–২৭ প্রত্যাশিত MCQ।',
      accent: 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800',
      icon: Layers,
    },
    {
      path: '/bank',
      title: '📚 Paper Bank (অন-ডিমান্ড)',
      badge: `${BANK_INDEX.papers.length}টি পেপার · ${BANK_INDEX.total_questions} প্রশ্ন`,
      desc: 'Past Paper, Weekly Solve, Paper Final ও Model Test — শুধু খোলা পেপারই ডাউনলোড হবে।',
      accent: 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800',
      icon: FileJson,
    },
    {
      path: '/formulas',
      title: '📐 Formula Cards (লিখিত + MCQ)',
      badge: '৩৬৬ সূত্র কার্ড',
      desc: 'অধ্যায়ভিত্তিক সার্চ ও প্রিন্টযোগ্য সূত্র শিট — প্রতিদিন ৩০ মিনিট রিভিশন।',
      accent: 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800',
      icon: BookMarked,
    },
    {
      path: '/recall',
      title: '🧠 GK Monthly & English Recall',
      badge: 'MAT ২৫ নম্বর স্পেশাল',
      desc: 'মাসিক সাম্প্রতিক সাধারণ জ্ঞান ও ইংরেজি Sure-Shot প্র্যাকটিস ডেক।',
      accent: 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800',
      icon: Zap,
    },
  ];

  return (
    <div className="max-w-5xl mx-auto px-4 py-6 sm:py-8 space-y-6">
      {/* Hero Banner */}
      <div className="rounded-3xl bg-gradient-to-br from-[#056839] via-[#047857] to-[#0d9488] text-white p-6 sm:p-8 shadow-lg">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/15 text-xs font-bold mb-3">
              <Flame className="w-3.5 h-3.5 text-amber-300" />
              {isMedical ? 'মেডিকেল (MAT) · ১৮ ডিসেম্বর ২০২৬' : "ঢাবি 'ক' (DU Ka) · ১২ ডিসেম্বর ২০২৬"}
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
              টার্গেট ৭৮–৮০+ · প্র্যাকটিস ও প্রেডিকশন ইঞ্জিন
            </h1>
            <p className="text-xs sm:text-sm text-emerald-100 mt-1.5 max-w-xl">
              এক প্রস্তুতি, দুই পরীক্ষা — Physics, Chemistry ও Biology-র ~৭৫ নম্বর একই সিলেবাস থেকে।
            </p>
          </div>

          <div className="grid grid-cols-3 gap-2.5 text-center">
            <div className="bg-white/10 backdrop-blur-xs rounded-2xl px-3.5 py-2.5">
              <div className="text-lg sm:text-xl font-black">{BANK_INDEX.total_questions}</div>
              <div className="text-[10px] text-emerald-100">মোট প্রশ্ন</div>
            </div>
            <div className="bg-white/10 backdrop-blur-xs rounded-2xl px-3.5 py-2.5">
              <div className="text-lg sm:text-xl font-black">{examMcqCount}</div>
              <div className="text-[10px] text-emerald-100">{isMedical ? 'MAT পুল' : 'DU Ka পুল'}</div>
            </div>
            <div className="bg-white/10 backdrop-blur-xs rounded-2xl px-3.5 py-2.5">
              <div className="text-lg sm:text-xl font-black">{BANK_INDEX.chapters.length}</div>
              <div className="text-[10px] text-emerald-100">অধ্যায়</div>
            </div>
          </div>
        </div>

        <div className="mt-5 pt-4 border-t border-white/15 flex flex-wrap items-center gap-4 text-xs text-emerald-50">
          <span className="flex items-center gap-1">
            <Clock className="w-3.5 h-3.5" /> ৪৫ সেকেন্ড/প্রশ্ন
          </span>
          <span>• EV = 1.25P − 0.25 (২০%+ নিশ্চিত হলে দাগো)</span>
          <span>• লিখিত কখনো খালি নয়</span>
        </div>
      </div>

      {/* Feature Grid */}
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {cards.map((c) => {
          const Icon = c.icon;
          return (
            <button
              key={c.path}
              onClick={() => onNavigate(c.path)}
              className={`text-left rounded-3xl p-5 transition-all hover:scale-[1.01] active:scale-[0.99] cursor-pointer flex flex-col justify-between gap-4 ${
                c.primary ? `bg-gradient-to-br ${c.accent} shadow-md` : c.accent
              }`}
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <div
                    className={`w-9 h-9 rounded-xl flex items-center justify-center ${
                      c.primary ? 'bg-white/20 text-white' : 'bg-emerald-50 dark:bg-emerald-950/50 text-emerald-600'
                    }`}
                  >
                    <Icon className="w-5 h-5" />
                  </div>
                  <span
                    className={`px-2.5 py-0.5 rounded-full text-[11px] font-bold ${
                      c.primary ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
                    }`}
                  >
                    {c.badge}
                  </span>
                </div>
                <h2 className={`text-base font-extrabold mb-1 ${c.primary ? 'text-white' : 'text-slate-900 dark:text-white'}`}>
                  {c.title}
                </h2>
                <p className={`text-xs leading-relaxed ${c.primary ? 'text-emerald-50' : 'text-slate-500 dark:text-slate-400'}`}>
                  {c.desc}
                </p>
              </div>
              <div className={`flex items-center gap-1 text-xs font-bold ${c.primary ? 'text-white' : 'text-emerald-600 dark:text-emerald-400'}`}>
                শুরু করো <ArrowRight className="w-3.5 h-3.5" />
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
};
