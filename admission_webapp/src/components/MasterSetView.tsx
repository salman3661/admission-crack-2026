import React, { useState } from 'react';
import { Sparkles, Play, ShieldCheck, Info } from 'lucide-react';
import { BANK_INDEX, loadMasterSet, type Question } from '../lib/library';
import { DrillRunner } from './DrillRunner';
import backtestData from '../data/backtest.json';
import { useSEO } from '../lib/seo';

interface MasterSetViewProps {
  activeTrack: 'varsity' | 'medical';
}

export const MasterSetView: React.FC<MasterSetViewProps> = ({ activeTrack }) => {
  const [exam, setExam] = useState<'du_ka' | 'mat'>(activeTrack === 'medical' ? 'mat' : 'du_ka');
  const [activeSet, setActiveSet] = useState<{ label: string; questions: Question[] } | null>(null);
  const [loading, setLoading] = useState(false);

  useSEO({
    title: 'Master Sets (SET A / B / C) — Admission Crack 2026',
    description: 'LEARN→PREDICT→SELECT মডেলের ভিত্তিতে নির্বাচিত DU Ka ও MAT Master Set A, B এবং Wildcard Set C।',
    path: '/master-set',
  });

  const handleOpenSet = async (setKey: 'set_a' | 'set_b' | 'set_c', label: string) => {
    setLoading(true);
    try {
      const questions = await loadMasterSet(exam, setKey);
      setActiveSet({ label: `${exam === 'du_ka' ? 'DU Ka' : 'MAT'} — ${label}`, questions });
    } finally {
      setLoading(false);
    }
  };

  if (activeSet) {
    return (
      <DrillRunner
        questions={activeSet.questions}
        title={activeSet.label}
        subtitle={`${activeSet.questions.length}টি যাচাইকৃত প্রশ্ন • প্রোভেন্যান্সসহ`}
        onBack={() => setActiveSet(null)}
      />
    );
  }

  const sets = [
    {
      key: 'set_a' as const,
      title: 'SET-A · সর্বোচ্চ সম্ভাব্য',
      badge: 'Phase 1–2',
      count: exam === 'du_ka' ? BANK_INDEX.master_sets.du_ka_set_a : BANK_INDEX.master_sets.mat_set_a,
      desc: 'সর্বোচ্চ recency, yearsHit ও source_type weight অনুযায়ী নির্বাচিত মূল প্রশ্ন সেট।',
    },
    {
      key: 'set_b' as const,
      title: 'SET-B · দ্বিতীয় স্তর (০ Overlap)',
      badge: 'Phase 2',
      count: exam === 'du_ka' ? BANK_INDEX.master_sets.du_ka_set_b : BANK_INDEX.master_sets.mat_set_b,
      desc: 'SET-A এর সাথে একটিও প্রশ্ন shared নয় — দ্বিতীয় ধাপের পূর্ণাঙ্গ অনুশীলন।',
    },
    {
      key: 'set_c' as const,
      title: 'SET-C · Wildcard ও অন্যান্য ভার্সিটি',
      badge: 'Phase 4–5',
      count: exam === 'du_ka' ? BANK_INDEX.master_sets.du_ka_set_c : BANK_INDEX.master_sets.mat_set_c,
      desc: 'কম-সম্ভাব্য চ্যাপ্টার এবং RU/JU/CU/GST এর ওভারল্যাপিং সিলেবাসের প্রশ্ন।',
    },
  ];

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <Sparkles className="w-6 h-6 text-emerald-600" /> Master Sets (২৬–২৭ প্রেডিক্টর)
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            প্রতিটি প্রশ্ন আসল ব্যাংক থেকে নির্বাচিত — কোনো কৃত্রিম বা বানানো প্রশ্ন নেই।
          </p>
        </div>

        <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-2xl">
          <button
            onClick={() => setExam('du_ka')}
            className={`px-4 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              exam === 'du_ka' ? 'bg-emerald-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            DU 'Ka'
          </button>
          <button
            onClick={() => setExam('mat')}
            className={`px-4 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              exam === 'mat' ? 'bg-rose-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            MAT (MBBS)
          </button>
        </div>
      </div>

      {/* Backtest Credibility Card */}
      <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="flex items-start gap-3">
          <ShieldCheck className="w-6 h-6 text-emerald-600 shrink-0 mt-0.5" />
          <div>
            <div className="text-sm font-extrabold text-slate-900 dark:text-white">
              Leave-One-Year-Out Backtest (২০২১–২০২৪)
            </div>
            <div className="text-xs text-slate-500 mt-0.5">
              Top-8 চ্যাপ্টার কভারেজ: <strong>{backtestData.overall_top8_coverage_pct}%</strong> • #1 র‍্যাংক হিট: <strong>{backtestData.overall_rank1_hit_pct}%</strong> ({backtestData.total_test_questions}টি টেস্ট প্রশ্নে যাচাইকৃত)
            </div>
          </div>
        </div>
        <div className="text-[11px] text-amber-700 dark:text-amber-300 bg-amber-50 dark:bg-amber-950/40 px-3 py-2 rounded-xl flex items-center gap-1.5">
          <Info className="w-4 h-4 shrink-0" />
          টপিক-লেভেল মডেল; কোচিং মডেল টেস্ট যোগ হলে আরও নিখুঁত হয়।
        </div>
      </div>

      <div className="grid sm:grid-cols-3 gap-4">
        {sets.map((s) => (
          <div
            key={s.key}
            className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-3">
                <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300">
                  {s.badge}
                </span>
                <span className="text-xs font-black text-slate-700 dark:text-slate-300">{s.count} প্রশ্ন</span>
              </div>
              <h2 className="text-base font-extrabold text-slate-900 dark:text-white mb-2">{s.title}</h2>
              <p className="text-xs text-slate-500 leading-relaxed mb-5">{s.desc}</p>
            </div>

            <button
              onClick={() => handleOpenSet(s.key, s.title)}
              disabled={loading}
              className="w-full py-2.5 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
            >
              <Play className="w-3.5 h-3.5" /> ড্রিল শুরু করো
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
