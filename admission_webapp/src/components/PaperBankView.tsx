import React, { useState, useMemo } from 'react';
import { FileJson, Play } from 'lucide-react';
import { BANK_INDEX, loadPaper, type Question, type SourceType } from '../lib/library';
import { DrillRunner } from './DrillRunner';
import { useSEO } from '../lib/seo';

interface PaperBankViewProps {
  title: string;
  description: string;
  path: string;
  defaultSourceType?: SourceType | 'all';
  activeTrack: 'varsity' | 'medical';
  selectedSubject: string;
}

export const PaperBankView: React.FC<PaperBankViewProps> = ({
  title,
  description,
  path,
  defaultSourceType = 'all',
  activeTrack,
  selectedSubject,
}) => {
  const [sourceFilter, setSourceFilter] = useState<SourceType | 'all'>(defaultSourceType);
  const [activeDrill, setActiveDrill] = useState<{ title: string; questions: Question[] } | null>(null);
  const [loadingPath, setLoadingPath] = useState<string | null>(null);

  useSEO({
    title: `${title} | Admission Crack 2026`,
    description,
    path,
  });

  const papers = useMemo(() => {
    const examKey = activeTrack === 'medical' ? 'mat' : 'du_ka';
    return BANK_INDEX.papers.filter((p) => {
      if (sourceFilter !== 'all' && !p.source_types.includes(sourceFilter)) return false;
      if (selectedSubject !== 'All' && !p.subjects.includes(selectedSubject)) return false;
      if (!p.exams.includes(examKey) && !p.exams.includes('other')) return false;
      return true;
    });
  }, [sourceFilter, selectedSubject, activeTrack]);

  const totalShown = useMemo(() => papers.reduce((a, b) => a + b.count, 0), [papers]);

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

  if (activeDrill) {
    return (
      <DrillRunner
        questions={activeDrill.questions}
        title={activeDrill.title}
        subtitle={`${activeDrill.questions.length}টি প্রশ্ন (অন-ডিমান্ড লোড)`}
        onBack={() => setActiveDrill(null)}
      />
    );
  }

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

      {papers.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-10 text-center text-sm text-slate-500">
          এই ফিল্টারে এখনো কোনো পেপার যোগ করা হয়নি। <code className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800">src/data/bank/</code> এ JSON ফাইল যোগ করে <code className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800">build-master-set.mjs</code> চালাও।
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
