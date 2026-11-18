import React, { useState, useMemo } from 'react';
import { BarChart3, Play } from 'lucide-react';
import { getAttemptStats, loadPapersByFilter, type Question } from '../lib/library';
import { DrillRunner } from './DrillRunner';
import { useSEO } from '../lib/seo';

export const WeaknessRadarView: React.FC = () => {
  const [selectedSubject, setSelectedSubject] = useState<string>('All');
  const [drillState, setDrillState] = useState<{ title: string; questions: Question[] } | null>(null);
  const [loading, setLoading] = useState(false);

  useSEO({
    title: 'Weakness Radar — Marks Lost per Chapter | Admission Crack 2026',
    description: 'প্রতিটি বিষয় ও অধ্যায়ে কত নম্বর হারিয়েছো তার বিশ্লেষণ এবং সরাসরি দুর্বল অধ্যায় ড্রিল।',
    path: '/weakness-radar',
  });

  const stats = useMemo(() => Object.values(getAttemptStats()), []);
  const subjects = useMemo(() => ['All', ...new Set(stats.map((s) => s.subject))], [stats]);

  const filtered = useMemo(() => {
    return stats
      .filter((s) => selectedSubject === 'All' || s.subject === selectedSubject)
      .sort((a, b) => b.marksLost - a.marksLost);
  }, [stats, selectedSubject]);

  const maxLoss = Math.max(1, ...filtered.map((s) => s.marksLost));

  const handleDrillChapter = async (chapterId: string, chapterName: string) => {
    setLoading(true);
    try {
      const qs = await loadPapersByFilter({ chapterId });
      setDrillState({ title: `দুর্বল অধ্যায় ড্রিল: ${chapterName}`, questions: qs });
    } finally {
      setLoading(false);
    }
  };

  if (drillState) {
    return (
      <DrillRunner
        questions={drillState.questions}
        title={drillState.title}
        onBack={() => setDrillState(null)}
      />
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <BarChart3 className="w-6 h-6 text-amber-600" /> Weakness Radar
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            সবচেয়ে বেশি নম্বর হারানো অধ্যায়গুলো উপরে — যেকোনো অধ্যায়ে ক্লিক করে সরাসরি ড্রিল করো।
          </p>
        </div>

        <div className="flex flex-wrap gap-1.5">
          {subjects.map((s) => (
            <button
              key={s}
              onClick={() => setSelectedSubject(s)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
                selectedSubject === s
                  ? 'bg-emerald-600 text-white'
                  : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
              }`}
            >
              {s}
            </button>
          ))}
        </div>
      </div>

      {filtered.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-10 text-center text-sm text-slate-500">
          এখনো কোনো অনুশীলনের ডেটা নেই। ড্রিল বা সিমুলেটর শেষ করলে এখানে অধ্যায়ভিত্তিক দুর্বলতা দেখাবে।
        </div>
      ) : (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 space-y-3">
          {filtered.map((c) => {
            const acc = c.attempted ? Math.round((c.correct / c.attempted) * 100) : 0;
            const barPct = Math.min(100, Math.round((c.marksLost / maxLoss) * 100));
            return (
              <div
                key={`${c.subject}||${c.chapter_id}`}
                className="p-4 rounded-2xl border border-slate-100 dark:border-slate-800 hover:border-emerald-300 transition-all"
              >
                <div className="flex items-center justify-between gap-3 mb-2">
                  <div>
                    <div className="text-sm font-extrabold text-slate-900 dark:text-white">{c.chapter_name}</div>
                    <div className="text-xs text-slate-500">
                      {c.subject} • Attempted: {c.attempted} • Correct: {c.correct} ({acc}%)
                    </div>
                  </div>
                  <div className="flex items-center gap-3 shrink-0">
                    <span className="text-xs font-black text-rose-600">−{c.marksLost} নম্বর</span>
                    <button
                      disabled={loading}
                      onClick={() => handleDrillChapter(c.chapter_id, c.chapter_name)}
                      className="px-3 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1 cursor-pointer"
                    >
                      <Play className="w-3 h-3" /> ড্রিল
                    </button>
                  </div>
                </div>
                <div className="h-2 w-full bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                  <div className="h-full bg-gradient-to-r from-amber-500 to-rose-600 rounded-full" style={{ width: `${barPct}%` }} />
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
