import React, { useState, useMemo } from 'react';
import { Layers, Search, Play, Sparkles, Calendar } from 'lucide-react';
import { BANK_INDEX, loadPapersByFilter, type Question } from '../lib/library';
import { DrillRunner } from './DrillRunner';
import { useSEO } from '../lib/seo';

interface ChapterExplorerViewProps {
  activeTrack: 'varsity' | 'medical';
  initialTab?: 'chapters' | 'topics' | 'weeks';
}

export const ChapterExplorerView: React.FC<ChapterExplorerViewProps> = ({
  activeTrack,
  initialTab = 'chapters',
}) => {
  const [viewTab, setViewTab] = useState<'chapters' | 'topics' | 'weeks'>(initialTab);
  const [query, setQuery] = useState('');
  const [subject, setSubject] = useState('All');
  const [drill, setDrill] = useState<{ title: string; questions: Question[] } | null>(null);
  const [loading, setLoading] = useState(false);

  const megaEntries = useMemo(() => {
    const map = BANK_INDEX.by_mega_type || {};
    return Object.entries(map).map(([name, meta]) => ({
      name,
      ...meta,
    }));
  }, []);

  useSEO({
    title: 'Chapter & Topic Explorer (অধ্যায়, টপিক ও সপ্তাহভিত্তিক ড্রিল) | Admission Crack 2026',
    description: `${BANK_INDEX.chapters.length}টি অধ্যায় এবং ${megaEntries.length}টি টপিক (mega_type) ভিত্তিক প্রশ্নসংখ্যা, কত বছরে এসেছে এবং ২৬–২৭ প্রত্যাশিত MCQ।`,
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

  const filteredTopics = useMemo(() => {
    const q = query.trim().toLowerCase();
    return megaEntries
      .filter((t) => {
        if (subject !== 'All' && t.subject !== subject) return false;
        if (
          q &&
          !t.name.toLowerCase().includes(q) &&
          !String(t.chapter || '').toLowerCase().includes(q)
        ) {
          return false;
        }
        return true;
      })
      .sort((a, b) => b.count - a.count || b.years_hit - a.years_hit);
  }, [megaEntries, query, subject]);

  const handleDrillChapter = async (chapterId: string, chapterName: string) => {
    setLoading(true);
    try {
      const qs = await loadPapersByFilter({ chapterId });
      setDrill({ title: chapterName, questions: qs });
    } finally {
      setLoading(false);
    }
  };

  const handleDrillTopic = async (megaType: string) => {
    setLoading(true);
    try {
      const qs = await loadPapersByFilter({ megaType });
      setDrill({ title: megaType, questions: qs });
    } finally {
      setLoading(false);
    }
  };

  const handleDrillWeek = async (weekNum: number) => {
    setLoading(true);
    try {
      const wkKey = `week_0${weekNum}`;
      const qs = await loadPapersByFilter({
        week: wkKey,
        subject: subject !== 'All' ? subject : undefined,
      });
      setDrill({ title: `Week 0${weekNum} — সাপ্তাহিক ড্রিল`, questions: qs });
    } finally {
      setLoading(false);
    }
  };

  if (drill) {
    return (
      <DrillRunner
        questions={drill.questions}
        title={drill.title}
        subtitle={`${drill.questions.length}টি প্রশ্ন`}
        onBack={() => setDrill(null)}
        bookmarkSource="drill"
      />
    );
  }

  const maxTopicCount = Math.max(25, ...filteredTopics.map((t) => t.count));

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <Layers className="w-6 h-6 text-emerald-600" /> অধ্যায় · টপিক · সপ্তাহ ড্রিল
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            {BANK_INDEX.chapters.length}টি অধ্যায় • {megaEntries.length}টি টপিক (mega_type) • ৯টি সপ্তাহ — সরাসরি ড্রিল করো।
          </p>
        </div>

        {/* F21: 3-way Switcher (Chapters / Topics / Weeks) */}
        <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-2xl">
          <button
            onClick={() => setViewTab('chapters')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              viewTab === 'chapters' ? 'bg-emerald-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            🗂 অধ্যায় ({BANK_INDEX.chapters.length})
          </button>
          <button
            onClick={() => setViewTab('topics')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              viewTab === 'topics' ? 'bg-emerald-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            🧩 টপিক অনুযায়ী ({megaEntries.length})
          </button>
          <button
            onClick={() => setViewTab('weeks')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              viewTab === 'weeks' ? 'bg-emerald-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            📅 সপ্তাহভিত্তিক (৯)
          </button>
        </div>
      </div>

      <div className="flex flex-col sm:flex-row gap-3">
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder={
              viewTab === 'topics'
                ? 'টপিকের নাম (Type 1...) বা অধ্যায় খুঁজুন...'
                : 'অধ্যায়ের নাম বা slug খুঁজুন...'
            }
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

      {viewTab === 'chapters' && (
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
                <h2 className="text-sm font-extrabold text-slate-900 dark:text-white leading-snug">
                  {c.chapter_name}
                </h2>
                <div className="text-[11px] text-slate-500 mt-1.5">
                  এসেছে: <strong>{c.years_hit}</strong> বছরে · <strong>{c.papers_hit}</strong> পেপারে
                </div>
                <div className="text-[11px] text-emerald-700 dark:text-emerald-400 font-bold mt-1">
                  প্রত্যাশিত MCQ: {activeTrack === 'medical' ? c.expected_mcq_mat : c.expected_mcq_du_ka} (
                  {c.predicted_pct}%)
                </div>
              </div>

              <button
                disabled={loading}
                onClick={() => handleDrillChapter(c.chapter_id, c.chapter_name)}
                className="w-full py-2 rounded-xl bg-slate-900 dark:bg-emerald-600 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
              >
                <Play className="w-3.5 h-3.5" /> এই chapter ড্রিল করো
              </button>
            </div>
          ))}
        </div>
      )}

      {viewTab === 'topics' && (
        <div className="space-y-2.5">
          {filteredTopics.map((t) => {
            const barPct = Math.min(100, Math.round((t.count / maxTopicCount) * 100));
            return (
              <div
                key={t.name}
                className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3"
              >
                <div className="space-y-1 flex-1 min-w-0">
                  <div className="flex flex-wrap items-center gap-2 text-[11px]">
                    <span className="px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 font-bold">
                      {t.subject}
                    </span>
                    <span className="text-slate-500 font-semibold">{t.chapter}</span>
                    <span className="text-blue-600 dark:text-blue-400 font-bold">
                      {t.years_hit} বছরে এসেছে
                    </span>
                  </div>
                  <div className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-1.5">
                    <Sparkles className="w-3.5 h-3.5 text-amber-500 shrink-0" />
                    <span className="truncate">{t.name}</span>
                  </div>
                  <div className="flex items-center gap-2 pt-1 max-w-xs">
                    <div className="h-1.5 flex-1 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-emerald-500 rounded-full"
                        style={{ width: `${barPct}%` }}
                      />
                    </div>
                    <span className="text-[11px] font-bold text-slate-600 dark:text-slate-300">
                      {t.count} প্রশ্ন
                    </span>
                  </div>
                </div>

                <button
                  disabled={loading}
                  onClick={() => handleDrillTopic(t.name)}
                  className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer shrink-0 disabled:opacity-50"
                >
                  <Play className="w-3.5 h-3.5" /> ড্রিল করো
                </button>
              </div>
            );
          })}
        </div>
      )}

      {viewTab === 'weeks' && (
        <div className="grid sm:grid-cols-3 gap-3.5">
          {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((w) => {
            const wkKey = `week_0${w}`;
            const count = BANK_INDEX.by_week[wkKey] || 0;
            return (
              <div
                key={wkKey}
                className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 flex flex-col justify-between gap-3"
              >
                <div>
                  <div className="flex items-center justify-between text-xs mb-2">
                    <span className="font-extrabold text-slate-900 dark:text-white flex items-center gap-1.5">
                      <Calendar className="w-4 h-4 text-emerald-600" /> Week 0{w}
                    </span>
                    <span className="px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 font-black">
                      {count} প্রশ্ন ✅
                    </span>
                  </div>
                  <div className="h-2 w-full bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-emerald-500 rounded-full"
                      style={{ width: `${Math.min(100, Math.round((count / 180) * 100))}%` }}
                    />
                  </div>
                </div>
                <button
                  disabled={loading || count === 0}
                  onClick={() => handleDrillWeek(w)}
                  className="w-full py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
                >
                  <Play className="w-3.5 h-3.5" /> এই সপ্তাহ ড্রিল করো
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
