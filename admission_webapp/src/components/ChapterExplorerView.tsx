import React, { useState, useMemo } from 'react';
import { Layers, Search, Play } from 'lucide-react';
import { BANK_INDEX, loadPapersByFilter, type Question } from '../lib/library';
import { DrillRunner } from './DrillRunner';
import { useSEO } from '../lib/seo';

interface ChapterExplorerViewProps {
  activeTrack: 'varsity' | 'medical';
}

export const ChapterExplorerView: React.FC<ChapterExplorerViewProps> = ({ activeTrack }) => {
  const [query, setQuery] = useState('');
  const [subject, setSubject] = useState('All');
  const [drill, setDrill] = useState<{ title: string; questions: Question[] } | null>(null);
  const [loading, setLoading] = useState(false);

  useSEO({
    title: 'Chapter Explorer (২৬–২৭ সম্ভাব্য প্রশ্নবণ্টন) | Admission Crack 2026',
    description: `${BANK_INDEX.chapters.length}টি অধ্যায়ের প্রশ্নসংখ্যা, কত বছরে এসেছে এবং ২৬–২৭ প্রত্যাশিত MCQ।`,
    path: '/chapters',
  });

  const subjects = useMemo(() => ['All', ...new Set(BANK_INDEX.chapters.map((c) => c.subject))], []);

  const chapters = useMemo(() => {
    const q = query.trim().toLowerCase();
    return BANK_INDEX.chapters
      .filter((c) => {
        if (subject !== 'All' && c.subject !== subject) return false;
        if (q && !c.chapter_name.toLowerCase().includes(q) && !c.chapter_id.toLowerCase().includes(q)) return false;
        return true;
      })
      .sort((a, b) => b.predicted_pct - a.predicted_pct || b.count - a.count);
  }, [query, subject]);

  const handleDrill = async (chapterId: string, chapterName: string) => {
    setLoading(true);
    try {
      const qs = await loadPapersByFilter({ chapterId });
      setDrill({ title: chapterName, questions: qs });
    } finally {
      setLoading(false);
    }
  };

  if (drill) {
    return <DrillRunner questions={drill.questions} title={drill.title} onBack={() => setDrill(null)} />;
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-6">
      <div>
        <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
          <Layers className="w-6 h-6 text-emerald-600" /> Chapter Explorer ({BANK_INDEX.chapters.length}টি অধ্যায়)
        </h1>
        <p className="text-xs text-slate-500 mt-1">
          প্রতিটি অধ্যায়ের প্রশ্নসংখ্যা, কত বছরে এসেছে ও {activeTrack === 'medical' ? 'MAT' : 'DU Ka'} ২৬–২৭ প্রত্যাশিত MCQ।
        </p>
      </div>

      <div className="flex flex-col sm:flex-row gap-3">
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="অধ্যায়ের নাম বা slug খুঁজুন..."
            className="w-full pl-10 pr-4 py-2.5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-xs"
          />
        </div>
        <div className="flex flex-wrap gap-1.5">
          {subjects.map((s) => (
            <button
              key={s}
              onClick={() => setSubject(s)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
                subject === s
                  ? 'bg-emerald-600 text-white'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-300'
              }`}
            >
              {s}
            </button>
          ))}
        </div>
      </div>

      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
        {chapters.map((c) => (
          <div
            key={`${c.subject}||${c.chapter_id}`}
            className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 flex flex-col justify-between gap-3"
          >
            <div>
              <div className="flex items-center justify-between text-[11px] mb-1.5">
                <span className="px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 font-bold">
                  {c.subject}
                </span>
                <span className="text-slate-500 font-semibold">{c.count} প্রশ্ন</span>
              </div>
              <h2 className="text-sm font-extrabold text-slate-900 dark:text-white leading-snug">{c.chapter_name}</h2>
              <div className="text-[11px] text-slate-500 mt-1.5">
                এসেছে: <strong>{c.years_hit}</strong> বছরে · <strong>{c.papers_hit}</strong> পেপারে
              </div>
              <div className="text-[11px] text-emerald-700 dark:text-emerald-400 font-bold mt-1">
                প্রত্যাশিত MCQ: {activeTrack === 'medical' ? c.expected_mcq_mat : c.expected_mcq_du_ka} ({c.predicted_pct}%)
              </div>
            </div>

            <button
              disabled={loading}
              onClick={() => handleDrill(c.chapter_id, c.chapter_name)}
              className="w-full py-2 rounded-xl bg-slate-900 dark:bg-emerald-600 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
            >
              <Play className="w-3.5 h-3.5" /> ড্রিল করো
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
