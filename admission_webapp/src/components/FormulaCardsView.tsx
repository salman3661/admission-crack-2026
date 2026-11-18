import React, { useState, useEffect, useMemo } from 'react';
import {
  BookMarked,
  Search,
  Printer,
  AlertTriangle,
  Star,
  Play,
  Sparkles,
  FileText,
} from 'lucide-react';
import { MathText } from './MathText';
import { DrillRunner } from './DrillRunner';
import { loadPapersByFilter, type Question } from '../lib/library';
import { useSEO } from '../lib/seo';

interface ExtractedFormula {
  formula: string;
  count: number;
  years_hit: number;
  papers_hit: number;
  confidence: 'high' | 'medium' | 'low';
  trap: string | null;
  question_ids: string[];
}

interface FormulaChapterCard {
  chapter: string;
  subject: string;
  subjects: string[];
  question_count: number;
  years_hit: number;
  papers_hit: number;
  predicted_pct: number;
  difficulty: 'easy' | 'medium' | 'hard';
  possible: boolean;
  formula_count: number;
  formulas: ExtractedFormula[];
  traps: string[];
  trap_count: number;
}

interface FormulasPayload {
  generated_at: string;
  total_math_expressions: number;
  chapters_with_formulas: number;
  total_formulas: number;
  stats: {
    easy_chapters: number;
    possible_chapters: number;
    high_confidence_formulas: number;
    traps_collected: number;
  };
  chapters: FormulaChapterCard[];
}

const FORMULA_BM_KEY = 'ac_formula_bookmarks_v1';
const FORMULA_NOTES_KEY = 'ac_formula_notes_v1';

export const FormulaCardsView: React.FC = () => {
  const [payload, setPayload] = useState<FormulasPayload | null>(null);
  const [loading, setLoading] = useState(true);
  const [subject, setSubject] = useState('All');
  const [query, setQuery] = useState('');
  const [onlyPossible, setOnlyPossible] = useState(false);
  const [onlyTraps, setOnlyTraps] = useState(false);
  const [onlyEasy, setOnlyEasy] = useState(false);
  const [onlyBookmarked, setOnlyBookmarked] = useState(false);

  const [bookmarkedChapters, setBookmarkedChapters] = useState<Record<string, boolean>>(() => {
    try {
      const raw = localStorage.getItem(FORMULA_BM_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch {
      return {};
    }
  });
  const [notes, setNotes] = useState<Record<string, string>>(() => {
    try {
      const raw = localStorage.getItem(FORMULA_NOTES_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch {
      return {};
    }
  });
  const [openNoteKey, setOpenNoteKey] = useState<string | null>(null);
  const [drill, setDrill] = useState<{ title: string; questions: Question[] } | null>(null);
  const [drillLoading, setDrillLoading] = useState<string | null>(null);

  useSEO({
    title: '📐 সূত্র কার্ড — সবকিছু এক জায়গায় (Unified Formula + Trap) | Admission Crack 2026',
    description:
      'ব্যাংকের প্রশ্ন ও সমাধান থেকে সংগৃহীত সকল LaTeX সূত্র, সাধারণ ফাঁদ (Trap), কমনতা ও সংযুক্ত প্রশ্ন ড্রিল।',
    path: '/formulas',
  });

  useEffect(() => {
    import('../data/formulas.json').then((mod) => {
      const data = mod.default as unknown as FormulasPayload;
      if (data && Array.isArray(data.chapters)) {
        setPayload(data);
      }
      setLoading(false);
    });
  }, []);

  const chapters = payload?.chapters || [];

  const subjects = useMemo(
    () => ['All', 'Physics', 'Chemistry', 'Higher Math', 'Biology'],
    []
  );

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return chapters.filter((c) => {
      if (subject !== 'All' && c.subject !== subject && !c.subjects?.includes(subject)) return false;
      if (onlyPossible && !c.possible) return false;
      if (onlyTraps && c.trap_count === 0) return false;
      if (onlyEasy && c.difficulty !== 'easy') return false;
      if (onlyBookmarked && !bookmarkedChapters[c.chapter]) return false;
      if (q) {
        const inChap = c.chapter.toLowerCase().includes(q);
        const inForm = c.formulas.some((f) => f.formula.toLowerCase().includes(q));
        const inTrap = c.traps.some((t) => t.toLowerCase().includes(q));
        if (!inChap && !inForm && !inTrap) return false;
      }
      return true;
    });
  }, [chapters, subject, query, onlyPossible, onlyTraps, onlyEasy, onlyBookmarked, bookmarkedChapters]);

  const toggleChapterBookmark = (chap: string) => {
    const next = { ...bookmarkedChapters, [chap]: !bookmarkedChapters[chap] };
    setBookmarkedChapters(next);
    try {
      localStorage.setItem(FORMULA_BM_KEY, JSON.stringify(next));
    } catch {
      // ignore
    }
  };

  const saveChapterNote = (chap: string, val: string) => {
    const next = { ...notes, [chap]: val };
    setNotes(next);
    try {
      localStorage.setItem(FORMULA_NOTES_KEY, JSON.stringify(next));
    } catch {
      // ignore
    }
  };

  const handleOpenFormulaQuestions = async (c: FormulaChapterCard) => {
    setDrillLoading(c.chapter);
    try {
      const qids = [...new Set(c.formulas.flatMap((f) => f.question_ids))];
      const qs = await loadPapersByFilter({ questionIds: qids });
      setDrill({
        title: `📐 ${c.chapter} — সূত্র সংযুক্ত প্রশ্ন`,
        questions: qs,
      });
    } finally {
      setDrillLoading(null);
    }
  };

  if (drill) {
    return (
      <DrillRunner
        questions={drill.questions}
        title={drill.title}
        subtitle={`${drill.questions.length}টি সংযুক্ত প্রশ্ন`}
        onBack={() => setDrill(null)}
        bookmarkSource="formula"
      />
    );
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3 print:hidden">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <BookMarked className="w-6 h-6 text-emerald-600" /> 📐 সূত্র কার্ড — সবকিছু এক জায়গায়
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            {payload
              ? `${payload.chapters_with_formulas}টি অধ্যায় • ${payload.total_formulas}টি সূত্র • ${payload.stats.traps_collected}টি ট্র্যাপ (লিখিত ৪০ নম্বরের প্রস্তুতির জন্য)`
              : 'প্রতিদিন ৩০ মিনিট লিখিত ও MCQ সূত্র রিভিশনের জন্য।'}
          </p>
        </div>

        <button
          onClick={() => window.print()}
          className="px-4 py-2 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-bold flex items-center gap-1.5 cursor-pointer"
        >
          <Printer className="w-4 h-4" /> প্রিন্ট করো
        </button>
      </div>

      {/* Search & Subject Filter */}
      <div className="flex flex-col sm:flex-row gap-3 print:hidden">
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="সূত্র খুঁজো (যেমন: frac, sin, pH, কনিক্স, ভেক্টর)..."
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
              {s === 'All' ? 'সব বিষয়' : s}
            </button>
          ))}
        </div>
      </div>

      {/* F20 Quick Filter Pills */}
      <div className="flex flex-wrap gap-2 print:hidden">
        <button
          onClick={() => setOnlyPossible((p) => !p)}
          className={`px-3 py-1.5 rounded-xl text-xs font-bold border cursor-pointer flex items-center gap-1 ${
            onlyPossible
              ? 'bg-amber-500 text-white border-amber-600'
              : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300'
          }`}
        >
          <Sparkles className="w-3.5 h-3.5" /> শুধু বারবার আসা ⭐ ({payload?.stats.possible_chapters || 0})
        </button>

        <button
          onClick={() => setOnlyTraps((p) => !p)}
          className={`px-3 py-1.5 rounded-xl text-xs font-bold border cursor-pointer flex items-center gap-1 ${
            onlyTraps
              ? 'bg-rose-600 text-white border-rose-700'
              : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300'
          }`}
        >
          <AlertTriangle className="w-3.5 h-3.5" /> শুধু ট্র্যাপ আছে 🚨
        </button>

        <button
          onClick={() => setOnlyEasy((p) => !p)}
          className={`px-3 py-1.5 rounded-xl text-xs font-bold border cursor-pointer flex items-center gap-1 ${
            onlyEasy
              ? 'bg-emerald-600 text-white border-emerald-700'
              : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300'
          }`}
        >
          🟢 শুধু EASY ({payload?.stats.easy_chapters || 0})
        </button>

        <button
          onClick={() => setOnlyBookmarked((p) => !p)}
          className={`px-3 py-1.5 rounded-xl text-xs font-bold border cursor-pointer flex items-center gap-1 ${
            onlyBookmarked
              ? 'bg-indigo-600 text-white border-indigo-700'
              : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300'
          }`}
        >
          <Star className="w-3.5 h-3.5" /> বুকমার্ক করা সূত্র
        </button>
      </div>

      {loading ? (
        <div className="p-10 text-center text-sm text-slate-500">সূত্র কার্ড লোড হচ্ছে...</div>
      ) : filtered.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-10 text-center text-sm text-slate-500">
          এই ফিল্টারে কোনো সূত্র পাওয়া যায়নি।
        </div>
      ) : (
        <div className="grid sm:grid-cols-2 gap-4">
          {filtered.map((c) => {
            const diffBadge =
              c.difficulty === 'easy'
                ? { label: '🟢 EASY — মূল বিষয়', cls: 'bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800' }
                : c.difficulty === 'medium'
                  ? { label: '🟡 MEDIUM', cls: 'bg-amber-50 dark:bg-amber-950/50 text-amber-700 dark:text-amber-300 border-amber-200 dark:border-amber-800' }
                  : { label: '🔴 HARD', cls: 'bg-rose-50 dark:bg-rose-950/50 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-800' };

            const isBm = Boolean(bookmarkedChapters[c.chapter]);
            const linkedQids = [...new Set(c.formulas.flatMap((f) => f.question_ids))];

            return (
              <div
                key={c.chapter}
                className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 flex flex-col justify-between gap-4 break-inside-avoid shadow-xs"
              >
                <div className="space-y-3">
                  {/* Top Badges + Star */}
                  <div className="flex items-start justify-between gap-2">
                    <div className="flex flex-wrap items-center gap-1.5 text-[11px]">
                      <span className={`px-2.5 py-0.5 rounded-full font-extrabold border ${diffBadge.cls}`}>
                        {diffBadge.label}
                      </span>
                      {c.possible && (
                        <span className="px-2.5 py-0.5 rounded-full font-extrabold bg-amber-500 text-white">
                          ⭐ POSSIBLE
                        </span>
                      )}
                      <span className="px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-bold">
                        {c.subject}
                      </span>
                    </div>

                    <button
                      onClick={() => toggleChapterBookmark(c.chapter)}
                      className={`p-1.5 rounded-xl border cursor-pointer ${
                        isBm
                          ? 'bg-amber-50 dark:bg-amber-950/50 border-amber-300 text-amber-500'
                          : 'bg-slate-50 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-400'
                      }`}
                      title="সূত্র বুকমার্ক"
                    >
                      <Star className={`w-4 h-4 ${isBm ? 'fill-current' : ''}`} />
                    </button>
                  </div>

                  {/* Chapter Title */}
                  <h2 className="text-base font-extrabold text-slate-900 dark:text-white">
                    {c.chapter}
                  </h2>

                  {/* Grouped Formulas Box */}
                  <div className="rounded-2xl bg-slate-50 dark:bg-slate-800/70 border border-slate-200/80 dark:border-slate-700/70 p-3.5 space-y-2 max-h-60 overflow-y-auto">
                    {c.formulas.slice(0, 8).map((f, idx) => (
                      <div
                        key={idx}
                        className="flex items-start justify-between gap-2 pb-2 last:pb-0 border-b last:border-b-0 border-slate-200/60 dark:border-slate-700/50 text-xs sm:text-sm"
                      >
                        <div className="overflow-x-auto">
                          <MathText content={`$${f.formula}$`} />
                        </div>
                        {f.count > 1 && (
                          <span className="px-1.5 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 text-[10px] font-bold shrink-0">
                            ×{f.count}
                          </span>
                        )}
                      </div>
                    ))}
                  </div>

                  {/* Trap Section */}
                  {c.traps.length > 0 && (
                    <div className="rounded-2xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/50 p-3 text-xs text-amber-900 dark:text-amber-200 space-y-1">
                      <div className="font-extrabold flex items-center gap-1 text-amber-800 dark:text-amber-300">
                        <AlertTriangle className="w-3.5 h-3.5 shrink-0" /> 🚨 ট্র্যাপ (সতর্কতা):
                      </div>
                      <div className="leading-relaxed">
                        <MathText content={c.traps[0]} />
                      </div>
                    </div>
                  )}

                  {/* Commonness Stats */}
                  <div className="text-[11px] text-slate-500 flex flex-wrap items-center gap-2">
                    <span>
                      📊 কমনতা: <strong>{c.years_hit}</strong> বছরে · <strong>{c.papers_hit}</strong> paper
                    </span>
                    {c.predicted_pct > 0 && (
                      <span className="text-emerald-600 dark:text-emerald-400 font-bold">
                        • ২৬–২৭ সম্ভাবনা: {c.predicted_pct}%
                      </span>
                    )}
                  </div>

                  {/* User Note */}
                  {(openNoteKey === c.chapter || notes[c.chapter]) && (
                    <div className="pt-1">
                      <textarea
                        value={notes[c.chapter] || ''}
                        onChange={(e) => saveChapterNote(c.chapter, e.target.value)}
                        rows={2}
                        placeholder="এই সূত্রের শর্ত বা নিজের নোট লিখে রাখো..."
                        className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 p-2.5 text-xs"
                      />
                    </div>
                  )}
                </div>

                {/* Action Buttons */}
                <div className="pt-2 border-t border-slate-100 dark:border-slate-800 flex flex-wrap items-center gap-2 print:hidden">
                  <button
                    onClick={() => handleOpenFormulaQuestions(c)}
                    disabled={drillLoading === c.chapter || linkedQids.length === 0}
                    className="flex-1 py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
                  >
                    <Play className="w-3.5 h-3.5" />
                    {drillLoading === c.chapter
                      ? 'লোড হচ্ছে...'
                      : `যে প্রশ্নে এসেছে (${c.question_count})`}
                  </button>

                  <button
                    onClick={() => toggleChapterBookmark(c.chapter)}
                    className="py-2 px-3 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-bold cursor-pointer"
                  >
                    {isBm ? '★ বুকমার্কড' : '☆ বুকমার্ক'}
                  </button>

                  <button
                    onClick={() => setOpenNoteKey((k) => (k === c.chapter ? null : c.chapter))}
                    className="py-2 px-3 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-bold flex items-center gap-1 cursor-pointer"
                  >
                    <FileText className="w-3.5 h-3.5" /> নোট
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
