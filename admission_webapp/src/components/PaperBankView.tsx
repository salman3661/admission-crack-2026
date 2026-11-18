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

const EXAM_LABELS: Record<string, string> = {
  du_ka: "ঢাকা বিশ্ববিদ্যালয় (DU 'Ka')",
  mat: 'মেডিকেল (MAT)',
  ru: 'রাজশাহী বিশ্ববিদ্যালয় (RU)',
  cu: 'চট্টগ্রাম বিশ্ববিদ্যালয় (CU)',
  ju: 'জাহাঙ্গীরনগর বিশ্ববিদ্যালয় (JU)',
  gst: 'জিএসটি গুচ্ছ (GST)',
  eng_bridge: 'ইঞ্জিনিয়ারিং ব্রিজ',
  other: 'অন্যান্য',
};

const EXAM_SHORT: Record<string, string> = {
  du_ka: "DU 'Ka'",
  mat: 'MAT',
  ru: 'RU',
  cu: 'CU',
  ju: 'JU',
  gst: 'GST',
  eng_bridge: 'Eng Bridge',
  other: 'অন্যান্য',
};

const SUBJECT_BN: Record<string, string> = {
  Physics: 'পদার্থবিজ্ঞান',
  Chemistry: 'রসায়ন',
  'Higher Math': 'উচ্চতর গণিত',
  Biology: 'জীববিজ্ঞান',
  English: 'ইংরেজি',
  Bangla: 'বাংলা',
  ICT: 'আইসিটি',
  GK: 'সাধারণ জ্ঞান',
};

const VARSITY_EXAMS = new Set(['du_ka', 'ru', 'cu', 'ju', 'gst', 'eng_bridge', 'other']);
const MEDICAL_EXAMS = new Set(['mat', 'other']);

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
  const [examFilter, setExamFilter] = useState<string>('track');

  const matchesExam = (exams: string[], filter: string) => {
    if (filter === 'all') return true;
    if (filter === 'track') {
      const allowed = activeTrack === 'medical' ? MEDICAL_EXAMS : VARSITY_EXAMS;
      return exams.some((e) => allowed.has(e));
    }
    return exams.includes(filter);
  };

  const papersForType = (st: SourceType | 'all') =>
    BANK_INDEX.papers.filter((p) => {
      if (st !== 'all' && !p.source_types.includes(st)) return false;
      if (selectedSubject !== 'All' && !p.subjects.includes(selectedSubject)) return false;
      if (!matchesExam(p.exams, examFilter)) return false;
      return true;
    });

  // Route-specific source_type is used only if > 0 papers exist; otherwise fall back to 'all'
  const computeInitialSource = (routeType: SourceType | 'all'): SourceType | 'all' => {
    if (routeType === 'all') return 'all';
    const available = BANK_INDEX.papers.filter(
      (p) => p.source_types.includes(routeType) && matchesExam(p.exams, 'track')
    );
    return available.length > 0 ? routeType : 'all';
  };

  const [sourceFilter, setSourceFilter] = useState<SourceType | 'all'>(() =>
    computeInitialSource(defaultSourceType)
  );
  const [activeDrill, setActiveDrill] = useState<{ title: string; questions: Question[] } | null>(null);
  const [loadingPath, setLoadingPath] = useState<string | null>(null);

  useEffect(() => {
    const initial = computeInitialSource(defaultSourceType);
    const hasMatches = BANK_INDEX.papers.some(
      (p) =>
        (initial === 'all' || p.source_types.includes(initial)) &&
        (selectedSubject === 'All' || p.subjects.includes(selectedSubject)) &&
        matchesExam(p.exams, 'track')
    );
    setSourceFilter(hasMatches ? initial : 'all');
    setExamFilter('track');
    setActiveDrill(null);
  }, [defaultSourceType, path, activeTrack, selectedSubject]);

  useSEO({
    title: `${title} | Admission Crack 2026`,
    description,
    path,
  });

  const allTrackPapers = useMemo(() => papersForType('all'), [selectedSubject, examFilter, activeTrack]);
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
      if (!matchesExam(p.exams, examFilter)) return false;
      if (wkNum && Array.isArray(p.weeks) && p.weeks.length > 0 && !p.weeks.includes(wkNum)) return false;
      return true;
    });
  }, [sourceFilter, selectedSubject, examFilter, activeTrack, selectedWeek]);

  const totalShown = useMemo(() => papers.reduce((a, b) => a + b.count, 0), [papers]);

  const groupedByExam = useMemo(() => {
    const order = activeTrack === 'medical'
      ? ['mat', 'other', 'du_ka', 'ru', 'cu', 'ju', 'gst', 'eng_bridge']
      : ['du_ka', 'ru', 'cu', 'ju', 'gst', 'eng_bridge', 'other', 'mat'];
    const map = new Map<string, typeof papers>();
    for (const p of papers) {
      const key = p.exams[0] || 'other';
      if (!map.has(key)) map.set(key, []);
      map.get(key)!.push(p);
    }
    return [...map.entries()].sort((a, b) => {
      const ia = order.indexOf(a[0]);
      const ib = order.indexOf(b[0]);
      return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib);
    });
  }, [papers, activeTrack]);

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
      let qs = await loadPaper(paperPath);
      const wkNum =
        selectedWeek && selectedWeek !== 'all' ? parseInt(selectedWeek.replace('week_', ''), 10) : null;
      if (wkNum) qs = qs.filter((q) => q.week === wkNum);
      if (selectedSubject !== 'All') qs = qs.filter((q) => q.subject === selectedSubject);
      const wkBadge = wkNum ? ` · Week 0${wkNum}` : '';
      const subjBadge = selectedSubject !== 'All' ? ` · ${SUBJECT_BN[selectedSubject] || selectedSubject}` : '';
      setActiveDrill({
        title: `${paperPath.replace(/^bank\//, '').replace(/\.json$/, '').replace(/\//g, ' · ')}${wkBadge}${subjBadge}`,
        questions: qs,
      });
    } finally {
      setLoadingPath(null);
    }
  };

  const handleOpenFilteredDrill = async () => {
    setLoadingPath('__filtered__');
    try {
      const qs = await loadPapersByFilter({
        week: selectedWeek !== 'all' ? selectedWeek : undefined,
        subject: selectedSubject !== 'All' ? selectedSubject : undefined,
        sourceType: sourceFilter,
        exam: examFilter !== 'track' && examFilter !== 'all' ? examFilter : undefined,
      });
      const wkLabel = selectedWeek !== 'all' ? `Week 0${selectedWeek.replace('week_', '')}` : '';
      const subjLabel = selectedSubject !== 'All' ? SUBJECT_BN[selectedSubject] || selectedSubject : 'সব বিষয়';
      setActiveDrill({
        title: `${[wkLabel, subjLabel].filter(Boolean).join(' · ')} — ফিল্টার্ড ড্রিল`,
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
        title: `Week 0${weekNum} — সাপ্তাহিক ড্রিল${selectedSubject !== 'All' ? ` (${SUBJECT_BN[selectedSubject] || selectedSubject})` : ''}`,
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

      {/* Active Week / Subject Filter Banner */}
      {(selectedWeek !== 'all' || selectedSubject !== 'All') && (
        <div className="bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800/60 rounded-2xl p-4 flex flex-wrap items-center justify-between gap-3">
          <div className="text-xs font-bold text-emerald-900 dark:text-emerald-200 flex flex-wrap items-center gap-2">
            <span>সক্রিয় ফিল্টার:</span>
            {selectedWeek !== 'all' && (
              <span className="px-2.5 py-1 rounded-lg bg-emerald-600 text-white">
                Week 0{selectedWeek.replace('week_', '')}
              </span>
            )}
            {selectedSubject !== 'All' && (
              <span className="px-2.5 py-1 rounded-lg bg-slate-900 dark:bg-white text-white dark:text-slate-900">
                {SUBJECT_BN[selectedSubject] || selectedSubject}
              </span>
            )}
          </div>
          <div className="flex items-center gap-2">
            {selectedWeek !== 'all' && onSelectWeek && (
              <button
                onClick={() => onSelectWeek('all')}
                className="px-3 py-1.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-600 dark:text-slate-300 cursor-pointer"
              >
                সব সপ্তাহ দেখো
              </button>
            )}
            <button
              onClick={handleOpenFilteredDrill}
              disabled={loadingPath === '__filtered__'}
              className="px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
            >
              <Play className="w-3.5 h-3.5" />
              {loadingPath === '__filtered__' ? 'লোড হচ্ছে...' : 'এই ফিল্টারের সব প্রশ্ন ড্রিল করো'}
            </button>
          </div>
        </div>
      )}

      {/* Exam Filter Pills */}
      <div className="flex flex-wrap gap-1.5">
        {(
          [
            ['track', activeTrack === 'medical' ? 'মেডিকেল ট্র্যাক' : 'সকল ভার্সিটি'],
            ['all', `সব পরীক্ষা (${BANK_INDEX.total_questions})`],
            ...Object.entries(BANK_INDEX.by_exam).map(([k, cnt]) => [k, `${EXAM_SHORT[k] || k} (${cnt})`]),
          ] as [string, string][]
        ).map(([k, lbl]) => (
          <button
            key={k}
            onClick={() => setExamFilter(k)}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold cursor-pointer transition-colors ${
              examFilter === k
                ? 'bg-slate-900 dark:bg-white text-white dark:text-slate-900'
                : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-300 hover:border-emerald-400'
            }`}
          >
            {lbl}
          </button>
        ))}
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

      {/* Honest Empty State with fallback button */}
      {papers.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-10 text-center space-y-3">
          <div className="text-base font-extrabold text-slate-800 dark:text-slate-100">
            এই ফিল্টারে কোনো পেপার পাওয়া যায়নি।
          </div>
          <div className="pt-1 flex flex-wrap items-center justify-center gap-3 text-xs font-bold text-slate-700 dark:text-slate-300">
            <span>
              মোট উপলব্ধ: {allTrackPapers.length}টি পেপার · {allTrackQuestions}টি প্রশ্ন
            </span>
            <button
              onClick={() => {
                setSourceFilter('all');
                setExamFilter('all');
              }}
              className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold cursor-pointer"
            >
              সব ধরন ও পরীক্ষা দেখো
            </button>
          </div>
        </div>
      ) : (
        <div className="space-y-6">
          {groupedByExam.map(([examKey, examPapers]) => {
            const groupTotal = examPapers.reduce((a, b) => a + b.count, 0);
            return (
              <section key={examKey} className="space-y-3">
                <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                  <h2 className="text-base font-extrabold text-slate-900 dark:text-white">
                    {EXAM_LABELS[examKey] || examKey.toUpperCase()}
                  </h2>
                  <span className="text-xs font-bold text-emerald-600 dark:text-emerald-400">
                    {examPapers.length}টি ফাইল · {groupTotal}টি প্রশ্ন
                  </span>
                </div>
                <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
                  {examPapers.map((p) => {
                    const subjLabel = p.subjects.map((s) => SUBJECT_BN[s] || s).join(', ');
                    const srcLabel = p.source_types
                      .map((st) => (st === 'weekly_solve' ? 'Weekly Solve' : 'Past Paper'))
                      .join(', ');
                    return (
                      <div
                        key={p.path}
                        className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 flex flex-col justify-between gap-3 hover:border-emerald-400/70 transition-colors"
                      >
                        <div>
                          <div className="flex items-center justify-between text-[11px] mb-1.5">
                            <span className="px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 font-bold text-slate-700 dark:text-slate-300">
                              {EXAM_SHORT[examKey] || examKey.toUpperCase()} · {srcLabel}
                            </span>
                            <span className="text-emerald-600 font-extrabold">
                              {p.mcqs} MCQ {p.written > 0 ? `+ ${p.written} লিখিত` : ''}
                            </span>
                          </div>
                          <div className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-1.5">
                            <FileJson className="w-4 h-4 text-emerald-600 shrink-0" />
                            <span className="truncate">{subjLabel}</span>
                          </div>
                          {Array.isArray(p.weeks) && p.weeks.length > 0 && (
                            <div className="text-[11px] text-slate-500 mt-1">
                              সপ্তাহ: {p.weeks.map((w) => `W-0${w}`).join(', ')}
                            </div>
                          )}
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
                    );
                  })}
                </div>
              </section>
            );
          })}
        </div>
      )}
    </div>
  );
};
