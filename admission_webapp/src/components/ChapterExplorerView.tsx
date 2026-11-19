import React, { useState, useMemo, useEffect } from 'react';
import {
  Layers,
  Search,
  Play,
  Sparkles,
  Calendar,
  ArrowLeft,
  GraduationCap,
  Stethoscope,
  TrendingUp,
  Sigma,
  Ruler,
  AlertTriangle,
  ChevronRight,
  Flame,
} from 'lucide-react';
import {
  BANK_INDEX,
  loadPapersByFilter,
  loadChapterQuestionsComplete,
  loadUnifiedMegaTypes,
  loadTopicQuestionsComplete,
  type UnifiedMegaTypeEntry,
  type Question,
} from '../lib/library';
import { buildCanonicalChapters, type CanonicalChapterGroup } from '../lib/chapterCatalog';
import { DrillRunner } from './DrillRunner';
import { MathText } from './MathText';
import { useSEO } from '../lib/seo';

interface ChapterExplorerViewProps {
  activeTrack: 'varsity' | 'medical';
  initialTab?: 'chapters' | 'topics' | 'weeks';
}

interface FormulaEntry {
  formula: string;
  count: number;
  years_hit: number;
  papers_hit: number;
  confidence: string;
  trap?: string;
}

interface FormulaChapterEntry {
  chapter: string;
  subject: string;
  subjects?: string[];
  formula_count: number;
  formulas: FormulaEntry[];
}

const normalizeName = (s: string) =>
  s
    .toLowerCase()
    .replace(/[\s\-_()[\].,:।]+/g, '')
    .trim();

/** Extract dimension & unit snippets from chapter questions and formulas */
function extractDimensionsAndUnits(questions: Question[], formulas: FormulaEntry[]): string[] {
  const results = new Set<string>();
  const dimPattern = /(\[?\s*M\s*\^?\{?-?\d*\}?\s*L\s*\^?\{?-?\d*\}?\s*T\s*\^?\{?-?\d*\}?[^\n।,;]*\]?)/gi;

  for (const q of questions) {
    const combined = `${q.question || ''}\n${q.explanation || ''}\n${q.trap || ''}`;
    const lines = combined.split(/\r?\n|।/);
    for (const rawLine of lines) {
      const line = rawLine.trim();
      if (!line || line.length > 160) continue;
      if (
        line.includes('মাত্রা') ||
        line.includes('একক') ||
        /\[M\s*L/i.test(line) ||
        /ML\^?\{?-?\d/i.test(line)
      ) {
        results.add(line);
      }
      if (results.size >= 12) break;
    }
    if (results.size >= 12) break;
  }

  for (const f of formulas) {
    if (dimPattern.test(f.formula) || (f.trap && (f.trap.includes('মাত্রা') || f.trap.includes('একক')))) {
      results.add(`$${f.formula}$`);
    }
    if (results.size >= 15) break;
  }

  return Array.from(results).slice(0, 12);
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

  // Selected Chapter Hub state
  const [selectedChapter, setSelectedChapter] = useState<CanonicalChapterGroup | null>(null);
  const [chapterQuestions, setChapterQuestions] = useState<Question[]>([]);
  const [chapterCategories, setChapterCategories] = useState<{
    varsity: Question[];
    mat: Question[];
    predictor: Question[];
  }>({ varsity: [], mat: [], predictor: [] });
  const [chapterLoading, setChapterLoading] = useState(false);
  const [formulaChapters, setFormulaChapters] = useState<FormulaChapterEntry[] | null>(null);

  const [onlyHighYield, setOnlyHighYield] = useState(false);
  const [unifiedMegaEntries, setUnifiedMegaEntries] = useState<UnifiedMegaTypeEntry[] | null>(null);

  const canonicalChapters = useMemo(() => buildCanonicalChapters(), []);

  const megaEntries = useMemo(() => {
    if (unifiedMegaEntries) return unifiedMegaEntries;
    const map = BANK_INDEX.by_mega_type || {};
    return Object.entries(map).map(([name, meta]) => ({
      name,
      subject: meta.subject as UnifiedMegaTypeEntry['subject'],
      chapter: meta.chapter,
      count: meta.count,
      years_hit: meta.years_hit,
      isHighYield: meta.years_hit >= 3 || meta.count >= 8,
    }));
  }, [unifiedMegaEntries]);

  useEffect(() => {
    if (viewTab !== 'topics' || unifiedMegaEntries) return;
    let cancelled = false;
    loadUnifiedMegaTypes().then((list) => {
      if (!cancelled) setUnifiedMegaEntries(list);
    });
    return () => {
      cancelled = true;
    };
  }, [viewTab, unifiedMegaEntries]);

  useSEO({
    title: 'Chapter & Topic Explorer (অধ্যায়, টপিক ও সপ্তাহভিত্তিক ড্রিল) | Admission Crack 2026',
    description: `${canonicalChapters.length}টি সুবিন্যস্ত অধ্যায় এবং ${megaEntries.length}টি টপিক (mega_type) ভিত্তিক প্রশ্নসংখ্যা, Varsity/MAT/Predictor ড্রিল এবং সূত্র ও মাত্রা এক নজরে।`,
    path: '/chapters',
  });

  // Load ALL chapter questions (bank + paper final + subject final + full mock + master + synthetic predictors + varsity/medical banks) + formulas.json
  useEffect(() => {
    if (!selectedChapter) return;
    let cancelled = false;
    setChapterLoading(true);
    setChapterQuestions([]);
    setChapterCategories({ varsity: [], mat: [], predictor: [] });

    Promise.all([
      loadChapterQuestionsComplete(
        selectedChapter.merged_chapter_ids,
        selectedChapter.chapter_name,
        selectedChapter.subject,
        selectedChapter.match_keywords
      ),
      formulaChapters
        ? Promise.resolve(formulaChapters)
        : import('../data/formulas.json').then((m) => (m.default?.chapters || m.chapters || []) as FormulaChapterEntry[]),
    ])
      .then(([res, fChapters]) => {
        if (cancelled) return;
        setChapterQuestions(res.all);
        setChapterCategories({ varsity: res.varsity, mat: res.mat, predictor: res.predictor });
        if (!formulaChapters) {
          setFormulaChapters(fChapters);
        }
      })
      .finally(() => {
        if (!cancelled) setChapterLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, [selectedChapter, formulaChapters]);

  const subjects = useMemo(() => ['All', ...new Set(canonicalChapters.map((c) => c.subject))], [canonicalChapters]);

  const chapters = useMemo(() => {
    const q = query.trim().toLowerCase();
    return canonicalChapters.filter((c) => {
      if (subject !== 'All' && c.subject !== subject) return false;
      if (
        q &&
        !c.chapter_name.toLowerCase().includes(q) &&
        !c.match_keywords.some((kw) => kw.toLowerCase().includes(q))
      ) {
        return false;
      }
      return true;
    });
  }, [canonicalChapters, query, subject]);

  const filteredTopics = useMemo(() => {
    const q = query.trim().toLowerCase();
    return megaEntries
      .filter((t) => {
        if (subject !== 'All' && t.subject !== subject) return false;
        if (onlyHighYield && !t.isHighYield) return false;
        if (
          q &&
          !t.name.toLowerCase().includes(q) &&
          !String(t.chapter || '').toLowerCase().includes(q)
        ) {
          return false;
        }
        return true;
      })
      .sort((a, b) => (b.years_hit * 3 + b.count) - (a.years_hit * 3 + a.count));
  }, [megaEntries, query, subject, onlyHighYield]);

  // Group selected chapter questions by mega_type (Important Patterns)
  const chapterPatterns = useMemo(() => {
    const map = new Map<string, Question[]>();
    for (const q of chapterQuestions) {
      const mt = String(q.mega_type || '').trim();
      if (!mt) continue;
      const arr = map.get(mt) || [];
      arr.push(q);
      map.set(mt, arr);
    }
    return Array.from(map.entries())
      .map(([name, qs]) => ({
        name,
        questions: qs,
        yearsHit: Math.max(0, ...qs.map((q) => q.years_hit || 0)),
      }))
      .sort((a, b) => (b.yearsHit * 2 + b.questions.length) - (a.yearsHit * 2 + a.questions.length));
  }, [chapterQuestions]);

  // Match formulas for selected chapter
  const matchedFormulas = useMemo(() => {
    if (!selectedChapter || !formulaChapters) return [];
    const targetName = normalizeName(selectedChapter.chapter_name);
    const matched = formulaChapters.find(
      (fc) =>
        normalizeName(fc.chapter) === targetName &&
        (fc.subject === selectedChapter.subject || fc.subjects?.includes(selectedChapter.subject))
    ) || formulaChapters.find((fc) => normalizeName(fc.chapter).includes(targetName) || targetName.includes(normalizeName(fc.chapter)));

    return matched?.formulas || [];
  }, [selectedChapter, formulaChapters]);

  const dimensionsAndUnits = useMemo(
    () => extractDimensionsAndUnits(chapterQuestions, matchedFormulas),
    [chapterQuestions, matchedFormulas]
  );

  const uniqueTraps = useMemo(() => {
    const set = new Set<string>();
    for (const f of matchedFormulas) {
      if (f.trap && f.trap.trim()) set.add(f.trap.trim());
    }
    for (const q of chapterQuestions) {
      if (q.trap && q.trap.trim() && set.size < 8) set.add(q.trap.trim());
    }
    return Array.from(set).slice(0, 6);
  }, [matchedFormulas, chapterQuestions]);

  const handleDrillTopic = async (megaType: string) => {
    setLoading(true);
    try {
      const qs = await loadTopicQuestionsComplete(megaType);
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

  // Chapter Hub View (when a chapter grid box is clicked)
  if (selectedChapter) {
    return (
      <div className="max-w-5xl mx-auto px-4 py-6 space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <button
            onClick={() => setSelectedChapter(null)}
            className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-800 cursor-pointer"
          >
            <ArrowLeft className="w-4 h-4" /> সকল অধ্যায় (Grid)
          </button>

          <div className="flex items-center gap-2 text-xs font-bold">
            <span className="px-2.5 py-1 rounded-full bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300">
              {selectedChapter.subject}
            </span>
            <span className="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
              মোট {chapterLoading ? '...' : chapterQuestions.length || selectedChapter.count}টি প্রশ্ন • {selectedChapter.years_hit} বছর
            </span>
          </div>
        </div>

        {/* Chapter Hero */}
        <div className="bg-gradient-to-br from-emerald-500/10 via-teal-500/5 to-indigo-500/10 border border-emerald-500/20 rounded-3xl p-5 sm:p-6">
          <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">
            {selectedChapter.chapter_name}
          </h1>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1">
            প্রত্যাশিত MCQ: <strong className="text-emerald-600 dark:text-emerald-400">{activeTrack === 'medical' ? selectedChapter.expected_mcq_mat : selectedChapter.expected_mcq_du_ka}</strong> ({selectedChapter.predicted_pct}%) • নিচে ৩টি ক্যাটাগরি থেকে ড্রিল শুরু করুন অথবা এক নজরে সূত্র ও মাত্রা দেখুন।
          </p>
        </div>

        {/* 3 Categories: Varsity / MAT / Predictor */}
        <div>
          <h2 className="text-sm font-extrabold text-slate-800 dark:text-slate-200 mb-3 flex items-center gap-2">
            <Layers className="w-4 h-4 text-emerald-600" /> ৩টি ক্যাটাগরিতে অনুশীলন
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3.5">
            {/* Varsity */}
            <div className="bg-white dark:bg-slate-900 border border-indigo-200 dark:border-indigo-900/50 rounded-2xl p-4 flex flex-col justify-between gap-3 shadow-sm">
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="w-9 h-9 rounded-xl bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 flex items-center justify-center">
                    <GraduationCap className="w-5 h-5" />
                  </span>
                  <span className="text-xs font-black px-2.5 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300">
                    {chapterLoading ? '...' : `${chapterCategories.varsity.length} প্রশ্ন`}
                  </span>
                </div>
                <h3 className="text-base font-extrabold text-slate-900 dark:text-white">Varsity (DU / RU / CU / GST)</h3>
                <p className="text-[11px] text-slate-500 mt-1">বিশ্ববিদ্যালয় ভর্তি পরীক্ষার বিগত ও মডেল প্রশ্ন</p>
              </div>
              <button
                disabled={chapterLoading || chapterCategories.varsity.length === 0}
                onClick={() =>
                  setDrill({
                    title: `${selectedChapter.chapter_name} — Varsity`,
                    questions: chapterCategories.varsity,
                  })
                }
                className="w-full py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-40"
              >
                <Play className="w-3.5 h-3.5" /> Varsity ড্রিল
              </button>
            </div>

            {/* MAT */}
            <div className="bg-white dark:bg-slate-900 border border-rose-200 dark:border-rose-900/50 rounded-2xl p-4 flex flex-col justify-between gap-3 shadow-sm">
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="w-9 h-9 rounded-xl bg-rose-500/10 text-rose-600 dark:text-rose-400 flex items-center justify-center">
                    <Stethoscope className="w-5 h-5" />
                  </span>
                  <span className="text-xs font-black px-2.5 py-0.5 rounded-full bg-rose-50 dark:bg-rose-950/60 text-rose-700 dark:text-rose-300">
                    {chapterLoading ? '...' : `${chapterCategories.mat.length} প্রশ্ন`}
                  </span>
                </div>
                <h3 className="text-base font-extrabold text-slate-900 dark:text-white">MAT (Medical)</h3>
                <p className="text-[11px] text-slate-500 mt-1">মেডিকেল ও ডেন্টাল ভর্তি পরীক্ষার প্রশ্নাবলি</p>
              </div>
              <button
                disabled={chapterLoading || chapterCategories.mat.length === 0}
                onClick={() =>
                  setDrill({
                    title: `${selectedChapter.chapter_name} — MAT`,
                    questions: chapterCategories.mat,
                  })
                }
                className="w-full py-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-40"
              >
                <Play className="w-3.5 h-3.5" /> MAT ড্রিল
              </button>
            </div>

            {/* Predictor */}
            <div className="bg-white dark:bg-slate-900 border border-amber-200 dark:border-amber-900/50 rounded-2xl p-4 flex flex-col justify-between gap-3 shadow-sm">
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="w-9 h-9 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 flex items-center justify-center">
                    <TrendingUp className="w-5 h-5" />
                  </span>
                  <span className="text-xs font-black px-2.5 py-0.5 rounded-full bg-amber-50 dark:bg-amber-950/60 text-amber-700 dark:text-amber-300">
                    {chapterLoading ? '...' : `${chapterCategories.predictor.length} প্রশ্ন`}
                  </span>
                </div>
                <h3 className="text-base font-extrabold text-slate-900 dark:text-white">Predictor (২৬–২৭)</h3>
                <p className="text-[11px] text-slate-500 mt-1">বারবার আসা ও হাই-ইয়েল্ড সম্ভাব্য প্রশ্ন</p>
              </div>
              <button
                disabled={chapterLoading || chapterCategories.predictor.length === 0}
                onClick={() =>
                  setDrill({
                    title: `${selectedChapter.chapter_name} — Predictor`,
                    questions: chapterCategories.predictor,
                  })
                }
                className="w-full py-2.5 rounded-xl bg-amber-600 hover:bg-amber-700 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-40"
              >
                <Play className="w-3.5 h-3.5" /> Predictor ড্রিল
              </button>
            </div>
          </div>

          {chapterQuestions.length > 0 && (
            <button
              onClick={() =>
                setDrill({
                  title: `${selectedChapter.chapter_name} — সব প্রশ্ন`,
                  questions: chapterQuestions,
                })
              }
              className="mt-3 w-full py-2.5 rounded-xl bg-slate-900 dark:bg-emerald-600 hover:opacity-95 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Play className="w-3.5 h-3.5" /> এই অধ্যায়ের সব প্রশ্ন একসাথে ড্রিল ({chapterQuestions.length}টি)
            </button>
          )}
        </div>

        {/* Important Patterns in this Chapter */}
        {!chapterLoading && chapterPatterns.length > 0 && (
          <div className="bg-white dark:bg-slate-900 border border-amber-200/80 dark:border-amber-900/40 rounded-3xl p-5 space-y-3">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <h2 className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
                <Flame className="w-4 h-4 text-amber-500" /> এই অধ্যায়ের গুরুত্বপূর্ণ প্যাটার্ন (Important Patterns)
              </h2>
              <span className="text-[11px] font-bold text-amber-700 dark:text-amber-300">
                {chapterPatterns.length}টি প্যাটার্ন
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              {chapterPatterns.slice(0, 12).map((pat) => {
                const isHot = pat.yearsHit >= 3 || pat.questions.length >= 4;
                return (
                  <div
                    key={pat.name}
                    className="p-3 rounded-2xl bg-amber-50/50 dark:bg-amber-950/20 border border-amber-200/70 dark:border-amber-900/40 flex items-center justify-between gap-2.5"
                  >
                    <div className="min-w-0 flex-1 space-y-1">
                      <div className="flex items-center gap-1.5 text-[10px] font-bold">
                        {isHot && (
                          <span className="px-1.5 py-0.5 rounded bg-amber-500 text-white">🔥 হাই-ইয়েল্ড</span>
                        )}
                        <span className="text-slate-600 dark:text-slate-300">{pat.questions.length} প্রশ্ন</span>
                        {pat.yearsHit > 0 && (
                          <span className="text-blue-600 dark:text-blue-400">• {pat.yearsHit} বছর</span>
                        )}
                      </div>
                      <div className="text-xs font-extrabold text-slate-900 dark:text-white truncate">
                        {pat.name}
                      </div>
                    </div>
                    <button
                      onClick={() =>
                        setDrill({
                          title: `${selectedChapter.chapter_name} — ${pat.name}`,
                          questions: pat.questions,
                        })
                      }
                      className="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-700 text-white text-[11px] font-bold shrink-0 cursor-pointer flex items-center gap-1"
                    >
                      <Play className="w-3 h-3" /> ড্রিল
                    </button>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* At-a-Glance Dimensions & Units (মাত্রা ও একক) */}
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 space-y-3">
          <h2 className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <Ruler className="w-4 h-4 text-cyan-600" /> মাত্রা ও একক এক নজরে (Dimensions & Units)
          </h2>
          {chapterLoading ? (
            <p className="text-xs text-slate-500">লোড হচ্ছে...</p>
          ) : dimensionsAndUnits.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              {dimensionsAndUnits.map((item, idx) => (
                <div
                  key={idx}
                  className="p-3 rounded-xl bg-cyan-50/60 dark:bg-cyan-950/20 border border-cyan-200/70 dark:border-cyan-900/40 text-xs text-slate-800 dark:text-slate-200 leading-relaxed"
                >
                  <MathText content={item} />
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-slate-500">
              এই অধ্যায়ে আলাদা মাত্রা/একক তথ্য নেই — নিচের সূত্রগুলো দেখুন।
            </p>
          )}
        </div>

        {/* At-a-Glance Formulas (সূত্র এক নজরে) */}
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 space-y-3">
          <div className="flex items-center justify-between">
            <h2 className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
              <Sigma className="w-4 h-4 text-emerald-600" /> অধ্যায়ের গুরুত্বপূর্ণ সূত্র এক নজরে
            </h2>
            <span className="text-[11px] font-bold text-slate-500">
              {matchedFormulas.length}টি সূত্র
            </span>
          </div>

          {chapterLoading ? (
            <p className="text-xs text-slate-500">সূত্র লোড হচ্ছে...</p>
          ) : matchedFormulas.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2.5">
              {matchedFormulas.slice(0, 18).map((f, idx) => (
                <div
                  key={idx}
                  className="p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/70 border border-slate-200 dark:border-slate-700/80 flex flex-col justify-between gap-1.5"
                >
                  <div className="text-sm font-bold text-slate-900 dark:text-white overflow-x-auto">
                    <MathText content={`$${f.formula}$`} />
                  </div>
                  <div className="flex items-center justify-between text-[10px] text-slate-500 font-semibold">
                    <span>{f.years_hit} বছর এসেছে</span>
                    <span className="px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-700 dark:text-emerald-300">
                      ×{f.count}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-slate-500">এই অধ্যায়ের জন্য সংরক্ষিত সূত্র এখনো যুক্ত হয়নি।</p>
          )}
        </div>

        {/* Common Traps */}
        {uniqueTraps.length > 0 && (
          <div className="bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200 dark:border-amber-900/40 rounded-3xl p-5 space-y-2.5">
            <h2 className="text-sm font-extrabold text-amber-900 dark:text-amber-300 flex items-center gap-2">
              <AlertTriangle className="w-4 h-4" /> পরীক্ষার সাধারণ ভুল (Common Traps)
            </h2>
            <ul className="space-y-1.5 text-xs text-slate-700 dark:text-slate-300">
              {uniqueTraps.map((t, i) => (
                <li key={i} className="flex items-start gap-2">
                  <span className="text-amber-600 font-black">•</span>
                  <div className="flex-1">
                    <MathText content={t} />
                  </div>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
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
            যেকোনো অধ্যায় বক্সে ক্লিক করলে Varsity / MAT / Predictor ৩ ক্যাটাগরি এবং সূত্র ও মাত্রা এক নজরে পাবেন।
          </p>
        </div>

        {/* 3-way Switcher (Chapters / Topics / Weeks) */}
        <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-2xl">
          <button
            onClick={() => setViewTab('chapters')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              viewTab === 'chapters' ? 'bg-emerald-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            🗂 অধ্যায় গ্রিড ({canonicalChapters.length})
          </button>
          <button
            onClick={() => setViewTab('topics')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              viewTab === 'topics' ? 'bg-emerald-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            🧩 টপিক ({megaEntries.length})
          </button>
          <button
            onClick={() => setViewTab('weeks')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              viewTab === 'weeks' ? 'bg-emerald-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            📅 সপ্তাহ (৯)
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
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
          {chapters.map((c) => (
            <button
              key={c.key}
              onClick={() => setSelectedChapter(c)}
              className="group text-left bg-white dark:bg-slate-900 hover:border-emerald-500 dark:hover:border-emerald-500 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 flex flex-col justify-between gap-3 transition-all shadow-sm hover:shadow-md cursor-pointer"
            >
              <div className="space-y-1.5">
                <div className="flex items-center justify-between gap-1 text-[10px]">
                  <span className="px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 font-bold truncate">
                    {c.subject}
                  </span>
                  <span className="px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-bold shrink-0">
                    {c.paper}
                  </span>
                </div>
                <h2 className="text-xs sm:text-sm font-extrabold text-slate-900 dark:text-white leading-snug line-clamp-2 group-hover:text-emerald-600 dark:group-hover:text-emerald-400">
                  {c.chapter_name}
                </h2>
              </div>

              <div className="pt-2 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between text-[10px] font-bold">
                <span className="text-emerald-700 dark:text-emerald-400">
                  {c.count}+ Q • MCQ: {activeTrack === 'medical' ? c.expected_mcq_mat : c.expected_mcq_du_ka}
                </span>
                <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-emerald-500 group-hover:translate-x-0.5 transition-transform" />
              </div>
            </button>
          ))}
        </div>
      )}

      {viewTab === 'topics' && (
        <div className="space-y-3">
          <div className="flex flex-wrap items-center justify-between gap-2 bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200/80 dark:border-amber-900/40 rounded-2xl px-4 py-2.5">
            <span className="text-xs font-bold text-amber-900 dark:text-amber-200 flex items-center gap-1.5">
              <Flame className="w-4 h-4 text-amber-500" />
              সবচেয়ে বেশি আসা প্যাটার্ন সবার আগে সাজানো আছে ({filteredTopics.length}টি প্যাটার্ন)
            </span>
            <button
              onClick={() => setOnlyHighYield((v) => !v)}
              className={`px-3 py-1 rounded-xl text-xs font-bold cursor-pointer transition-colors ${
                onlyHighYield
                  ? 'bg-amber-600 text-white'
                  : 'bg-white dark:bg-slate-900 text-amber-700 dark:text-amber-300 border border-amber-300 dark:border-amber-800'
              }`}
            >
              {onlyHighYield ? '🔥 শুধু হাই-ইয়েল্ড (চালু)' : '🔥 শুধু হাই-ইয়েল্ড দেখাও'}
            </button>
          </div>
          {filteredTopics.map((t) => {
            const barPct = Math.min(100, Math.round((t.count / maxTopicCount) * 100));
            return (
              <div
                key={t.name}
                className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3"
              >
                <div className="space-y-1 flex-1 min-w-0">
                  <div className="flex flex-wrap items-center gap-2 text-[11px]">
                    {t.isHighYield && (
                      <span className="px-2 py-0.5 rounded-full bg-amber-500 text-white font-black">
                        🔥 হাই-ইয়েল্ড
                      </span>
                    )}
                    <span className="px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 font-bold">
                      {t.subject}
                    </span>
                    <span className="text-slate-500 font-semibold">{t.chapter}</span>
                    {t.years_hit > 0 && (
                      <span className="text-blue-600 dark:text-blue-400 font-bold">
                        {t.years_hit} বছরে এসেছে
                      </span>
                    )}
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
