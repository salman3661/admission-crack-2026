import React, { useState, useMemo, useEffect } from 'react';
import { FileJson, Play, Calendar, CheckCircle2 } from 'lucide-react';
import {
  BANK_INDEX,
  loadPaper,
  loadPapersByFilter,
  getSolvedQuestionsMap,
  type Question,
  type SourceType,
} from '../lib/library';
import { DrillRunner } from './DrillRunner';
import { useSEO } from '../lib/seo';
import type { WeekFilterType } from '../types';

interface PaperBankViewProps {
  title: string;
  description: string;
  path: string;
  defaultSourceType?: SourceType | 'all';
  activeTrack: 'varsity' | 'medical';
  selectedSubject: string;
  selectedWeek?: WeekFilterType;
  onSelectWeek?: (w: WeekFilterType) => void;
}

const WEEK_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9] as const;

export const PaperBankView: React.FC<PaperBankViewProps> = ({
  title,
  description,
  path,
  defaultSourceType = 'all',
  activeTrack,
  selectedSubject,
  selectedWeek = 'all',
  onSelectWeek,
}) => {
  const examKey = activeTrack === 'medical' ? 'mat' : 'du_ka';

  const papersForType = (st: SourceType | 'all') =>
    BANK_INDEX.papers.filter((p) => {
      if (st !== 'all' && !p.source_types.includes(st)) return false;
      if (selectedSubject !== 'All' && !p.subjects.includes(selectedSubject)) return false;
      if (!p.exams.includes(examKey) && !p.exams.includes('other')) return false;
      return true;
    });

  // Fix 1 & Fix 2: Route-specific source_type is used only if > 0 papers exist; otherwise fall back to 'all'
  const computeInitialSource = (routeType: SourceType | 'all'): SourceType | 'all' => {
    if (routeType === 'all') return 'all';
    const available = BANK_INDEX.papers.filter(
      (p) => p.source_types.includes(routeType) && (p.exams.includes(examKey) || p.exams.includes('other'))
    );
    return available.length > 0 ? routeType : 'all';
  };

  const [sourceFilter, setSourceFilter] = useState<SourceType | 'all'>(() =>
    computeInitialSource(defaultSourceType)
  );
  const [activeDrill, setActiveDrill] = useState<{ title: string; questions: Question[] } | null>(null);
  const [loadingPath, setLoadingPath] = useState<string | null>(null);

  useEffect(() => {
    setSourceFilter(computeInitialSource(defaultSourceType));
    setActiveDrill(null);
  }, [defaultSourceType, path, activeTrack]);

  useSEO({
    title: `${title} | Admission Crack 2026`,
    description,
    path,
  });

  const allTrackPapers = useMemo(() => papersForType('all'), [selectedSubject, examKey]);
  const allTrackQuestions = useMemo(
    () => allTrackPapers.reduce((a, b) => a + b.count, 0),
    [allTrackPapers]
  );

  const papers = useMemo(() => {
    const wkNum =
      selectedWeek && selectedWeek !== 'all' ? parseInt(selectedWeek.replace('week_', ''), 10) : null;
    return BANK_INDEX.papers.filter((p) => {
      if (sourceFilter !== 'all' && !p.source_types.includes(sourceFilter)) return false;
      if (selectedSubject !== 'All' && !p.subjects.includes(selectedSubject)) return false;
      if (!p.exams.includes(examKey) && !p.exams.includes('other')) return false;
      if (wkNum && Array.isArray(p.weeks) && p.weeks.length > 0 && !p.weeks.includes(wkNum)) return false;
      return true;
    });
  }, [sourceFilter, selectedSubject, examKey, selectedWeek]);

  const totalShown = useMemo(() => papers.reduce((a, b) => a + b.count, 0), [papers]);

  const solvedByWeek = useMemo(() => {
    const solved = getSolvedQuestionsMap();
    const counts: Record<number, number> = {};
    for (const v of Object.values(solved)) {
      if (v.week) counts[v.week] = (counts[v.week] || 0) + 1;
    }
    return counts;
  }, [activeDrill]);

  const handleOpenPaper = async (paperPath: string) => {
    setLoadingPath(paperPath);
    try {
      const qs = await loadPaper(paperPath);
      setActiveDrill({
        title: paperPath.replace(/^bank\//, '').replace(/\.json$/, '').replace(/\//g, ' · '),
        questions: qs,
      });
    } finally {
      setLoadingPath(null);
    }
  };

  const handleOpenWeekDrill = async (weekNum: number) => {
    const wkKey = `week_0${weekNum}` as WeekFilterType;
    if (onSelectWeek) onSelectWeek(wkKey);
    setLoadingPath(wkKey);
    try {
      const qs = await loadPapersByFilter({
        week: wkKey,
        subject: selectedSubject,
      });
      setActiveDrill({
        title: `Week 0${weekNum} — সাপ্তাহিক ড্রিল${selectedSubject !== 'All' ? ` (${selectedSubject})` : ''}`,
        questions: qs,
      });
    } finally {
      setLoadingPath(null);
    }
  };

  if (activeDrill) {
    return (
      <DrillRunner
        questions={activeDrill.questions}
        title={activeDrill.title}
        subtitle={`${activeDrill.questions.length}টি প্রশ্ন (অন-ডিমান্ড লোড)`}
        onBack={() => setActiveDrill(null)}
        bookmarkSource="bank"
      />
    );
  }

  const maxWeekCount = Math.max(
    180,
    ...WEEK_LIST.map((w) => BANK_INDEX.by_week[`week_0${w}`] || 0)
  );

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white">{title}</h1>
          <p className="text-xs text-slate-500 mt-1">
            {papers.length}টি পেপার ফাইল • মোট {totalShown}টি প্রশ্ন (ক্লিক করলেই কেবল ওই পেপারটি লোড হবে)
          </p>
        </div>

        <div className="flex flex-wrap gap-1.5">
          {(
            [
              ['all', 'সব ধরন'],
              ['past_paper', 'Past Paper'],
              ['weekly_solve', 'Weekly Solve'],
              ['paper_final', 'Paper Final'],
              ['subject_final', 'Subject Final'],
              ['model_test', 'Model Test'],
            ] as const
          ).map(([k, lbl]) => (
            <button
              key={k}
              onClick={() => setSourceFilter(k)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
                sourceFilter === k
                  ? 'bg-emerald-600 text-white'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-300'
              }`}
            >
              {lbl}
            </button>
          ))}
        </div>
      </div>

      {/* F21.A: Week-by-Week Drill Section (Week 01 - Week 09) */}
      {(path === '/weekly' || sourceFilter === 'weekly_solve' || selectedWeek !== 'all') && (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-2">
            <div>
              <h2 className="text-base font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
                <Calendar className="w-4 h-4 text-emerald-600" /> সপ্তাহভিত্তিক ড্রিল (Week 01 – Week 09)
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                যেকোনো সপ্তাহে ক্লিক করলে ওই সপ্তাহের সব প্রশ্ন ({selectedSubject === 'All' ? 'সব বিষয়' : selectedSubject}) ড্রিলে চালু হবে।
              </p>
            </div>
            {selectedWeek !== 'all' && onSelectWeek && (
              <button
                onClick={() => onSelectWeek('all')}
                className="px-3 py-1 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold text-slate-600 dark:text-slate-300 cursor-pointer"
              >
                সব সপ্তাহ দেখো
              </button>
            )}
          </div>

          <div className="grid sm:grid-cols-3 gap-2.5">
            {WEEK_LIST.map((w) => {
              const wkKey = `week_0${w}`;
              const count = BANK_INDEX.by_week[wkKey] || 0;
              const solved = solvedByWeek[w] || 0;
              const pct = Math.min(100, Math.round((count / maxWeekCount) * 100));
              const isSelected = selectedWeek === wkKey;
              return (
                <button
                  key={wkKey}
                  onClick={() => handleOpenWeekDrill(w)}
                  disabled={loadingPath === wkKey || count === 0}
                  className={`text-left p-3.5 rounded-2xl border transition-all cursor-pointer flex flex-col justify-between gap-2 ${
                    isSelected
                      ? 'bg-emerald-50/80 dark:bg-emerald-950/40 border-emerald-500 ring-1 ring-emerald-500/30'
                      : 'bg-slate-50/70 dark:bg-slate-800/50 border-slate-200/80 dark:border-slate-700/80 hover:border-emerald-400'
                  }`}
                >
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-xs font-extrabold text-slate-900 dark:text-white">
                      Week 0{w}
                    </span>
                    <span className="text-xs font-black text-emerald-600 dark:text-emerald-400 flex items-center gap-1">
                      {count} প্রশ্ন <CheckCircle2 className="w-3.5 h-3.5" />
                    </span>
                  </div>
                  <div className="h-1.5 w-full bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-emerald-500 to-teal-500 rounded-full"
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                  <div className="flex items-center justify-between text-[11px] text-slate-500">
                    <span>{solved > 0 ? `সমাধানকৃত: ${solved}/${count}` : 'ড্রিলের জন্য প্রস্তুত'}</span>
                    <span className="font-bold text-emerald-600 dark:text-emerald-400">
                      {loadingPath === wkKey ? 'লোড হচ্ছে...' : 'ড্রিল করো →'}
                    </span>
                  </div>
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* Fix 3: Honest Empty State with fallback button */}
      {papers.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-10 text-center space-y-3">
          <div className="text-base font-extrabold text-slate-800 dark:text-slate-100">
            এই ধরনের paper এখনো আসেনি।
          </div>
          <p className="text-xs text-slate-500 max-w-md mx-auto leading-relaxed">
            Paper Final / Subject Final / Model Test — coaching-এর paper যোগ করলে এখানে আসবে।
          </p>
          <div className="pt-1 flex flex-wrap items-center justify-center gap-3 text-xs font-bold text-slate-700 dark:text-slate-300">
            <span>
              এখনই যা আছে: {allTrackPapers.length}টি পেপার · {allTrackQuestions}টি প্রশ্ন
            </span>
            <button
              onClick={() => setSourceFilter('all')}
              className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold cursor-pointer"
            >
              সব ধরন দেখো
            </button>
          </div>
        </div>
      ) : (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
          {papers.map((p) => (
            <div
              key={p.path}
              className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 flex flex-col justify-between gap-3"
            >
              <div>
                <div className="flex items-center justify-between text-[11px] mb-1.5">
                  <span className="px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 font-bold text-slate-700 dark:text-slate-300">
                    {p.exams.join(', ').toUpperCase()}
                  </span>
                  <span className="text-emerald-600 font-extrabold">
                    {p.mcqs} MCQ {p.written > 0 ? `+ ${p.written} লিখিত` : ''}
                  </span>
                </div>
                <div className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-1.5">
                  <FileJson className="w-4 h-4 text-emerald-600 shrink-0" />
                  <span className="truncate">{p.subjects.join(', ')}</span>
                </div>
                <div className="text-[11px] text-slate-500 mt-1 truncate">{p.path}</div>
              </div>

              <button
                onClick={() => handleOpenPaper(p.path)}
                disabled={loadingPath === p.path}
                className="w-full py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
              >
                <Play className="w-3.5 h-3.5" />
                {loadingPath === p.path ? 'লোড হচ্ছে...' : 'প্র্যাকটিস শুরু করো'}
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
