import React, { useState, useMemo } from 'react';
import {
  Target,
  Search,
  AlertTriangle,
  BookOpen,
  Play,
  PlusCircle,
  Download,
  Star,
  Sparkles,
} from 'lucide-react';
import {
  BANK_INDEX,
  loadAllBankQuestions,
  loadPapersByFilter,
  addUserQuestion,
  getUserAddedQuestions,
  toggleBookmark,
  isBookmarked,
  type Question,
  type CanonicalSubject,
} from '../lib/library';
import { MathText } from './MathText';
import { DrillRunner } from './DrillRunner';
import { useSEO } from '../lib/seo';

// 1. Normalize as specified in 06-NEW-FEATURES.md (F17)
export function normForMatch(s: string): string {
  return String(s || '')
    .replace(/\\\[|\\\]|\$+/g, '') // LaTeX delimiters
    .replace(/[০-৯]/g, (d) => String('০১২৩৪৫৬৭৮৯'.indexOf(d))) // Bengali -> English digits
    .replace(/[^\w\sঀ-৿]/g, ' ') // strip punctuation
    .replace(/\s+/g, ' ')
    .toLowerCase()
    .trim();
}

// 2. Token shingles (3-gram, with 1-gram fallback for short queries)
export function shingles(text: string, k = 3): Set<string> {
  const w = normForMatch(text).split(' ').filter(Boolean);
  const out = new Set<string>();
  if (w.length < k) {
    w.forEach((tok) => out.add(tok));
    return out;
  }
  for (let i = 0; i + k <= w.length; i++) {
    out.add(w.slice(i, i + k).join(' '));
  }
  w.forEach((tok) => {
    if (tok.length > 2) out.add(`w:${tok}`);
  });
  return out;
}

export function jaccard(a: Set<string>, b: Set<string>): number {
  if (a.size === 0 || b.size === 0) return 0;
  let inter = 0;
  for (const x of a) if (b.has(x)) inter++;
  const uni = a.size + b.size - inter;
  return uni === 0 ? 0 : inter / uni;
}

// Memoized shingle cache across the session
const shingleMemo = new Map<string, { norm: string; set: Set<string> }>();

function getQuestionShingle(q: Question): { norm: string; set: Set<string> } {
  let cached = shingleMemo.get(q.id);
  if (!cached) {
    const full = `${q.question} ${(q.options || []).join(' ')}`;
    cached = {
      norm: normForMatch(q.question),
      set: shingles(full, 3),
    };
    shingleMemo.set(q.id, cached);
  }
  return cached;
}

interface MatchCandidate {
  question: Question;
  score: number;
  verdict: 'exact' | 'similar' | 'topic';
  yearsHit: number;
  papersHit: number;
  predictedPct: number;
}

export const QuestionMatcherView: React.FC = () => {
  const [inputText, setInputText] = useState('');
  const [searching, setSearching] = useState(false);
  const [matches, setMatches] = useState<MatchCandidate[] | null>(null);
  const [drill, setDrill] = useState<{ title: string; questions: Question[] } | null>(null);
  const [, setBmTick] = useState(0);

  // Add-to-bank form state when question is new
  const [showAddForm, setShowAddForm] = useState(false);
  const [newSubj, setNewSubj] = useState<CanonicalSubject>('Physics');
  const [newChap, setNewChap] = useState('ভেক্টর');
  const [newSource, setNewSource] = useState('Coaching Practice 2026');
  const [newExp, setNewExp] = useState('');
  const [userAddedList, setUserAddedList] = useState<Question[]>(() => getUserAddedQuestions());

  useSEO({
    title: '🎯 প্রশ্ন ম্যাচার (Practice-Question Matcher) | Admission Crack 2026',
    description:
      'কোচিং বা প্র্যাকটিস শিটের যেকোনো প্রশ্ন পেস্ট করে যাচাই করো এটি ঢাবি ক বা মেডিকেলে আগে কতবার ও কত বছরে এসেছে।',
    path: '/matcher',
  });

  const chapterMetaMap = useMemo(() => {
    const m = new Map<string, { years_hit: number; papers_hit: number; predicted_pct: number; count: number }>();
    for (const c of BANK_INDEX.chapters) {
      m.set(`${c.subject}||${c.chapter_id}`, {
        years_hit: c.years_hit,
        papers_hit: c.papers_hit,
        predicted_pct: c.predicted_pct,
        count: c.count,
      });
    }
    return m;
  }, []);

  const handleSearch = async (overrideText?: string) => {
    const raw = (overrideText ?? inputText).trim();
    if (!raw) return;
    setSearching(true);
    try {
      const bank = await loadAllBankQuestions();
      const qNorm = normForMatch(raw);
      const qShingles = shingles(raw, 3);
      const qWords = new Set(qNorm.split(' ').filter((w) => w.length > 2));

      const scored: MatchCandidate[] = [];
      for (const item of bank) {
        const { norm, set } = getQuestionShingle(item);
        let score = 0;
        if (norm && qNorm && (norm === qNorm || norm.includes(qNorm) || qNorm.includes(norm))) {
          const lenRatio = Math.min(norm.length, qNorm.length) / Math.max(norm.length, qNorm.length);
          score = Math.max(0.97, lenRatio);
        } else {
          const jac = jaccard(qShingles, set);
          let wordHits = 0;
          if (qWords.size > 0) {
            for (const w of qWords) if (norm.includes(w)) wordHits++;
          }
          const wordRecall = qWords.size > 0 ? wordHits / qWords.size : 0;
          score = Math.min(0.96, Math.max(jac, jac * 0.55 + wordRecall * 0.45));
        }

        if (score > 0.08) {
          const cm = chapterMetaMap.get(`${item.subject}||${item.chapter_id}`);
          const yearsHit = item.years_hit || cm?.years_hit || (item.exam_year ? 1 : 3);
          const papersHit = item.papers_hit || cm?.papers_hit || (item.appears_in?.length || 1);
          const predictedPct = item.likelihood_pct || cm?.predicted_pct || 0;
          scored.push({
            question: item,
            score,
            verdict: score >= 0.97 ? 'exact' : score >= 0.8 ? 'similar' : 'topic',
            yearsHit,
            papersHit,
            predictedPct,
          });
        }
      }

      scored.sort((a, b) => b.score - a.score || b.yearsHit - a.yearsHit);
      setMatches(scored.slice(0, 5));
    } finally {
      setSearching(false);
    }
  };

  const handleLoadSample = async () => {
    const bank = await loadAllBankQuestions();
    const sample = bank.find((q) => q.subject === 'Physics' && q.trap && q.explanation) || bank[0];
    if (sample) {
      setInputText(sample.question);
      handleSearch(sample.question);
    }
  };

  const handleDrillChapter = async (chapterId: string, chapterName: string) => {
    setSearching(true);
    try {
      const qs = await loadPapersByFilter({ chapterId });
      setDrill({ title: `${chapterName} — সব ব্যাংক প্রশ্ন`, questions: qs });
    } finally {
      setSearching(false);
    }
  };

  const handleSaveUserQuestion = () => {
    if (!inputText.trim()) return;
    const newQ: Question = {
      id: `user_${Date.now()}`,
      source_type: 'paper_final',
      source_name: newSource.trim() || 'User Coaching Paper',
      exam: 'du_ka',
      exam_year: 2026,
      exam_date: new Date().toISOString().slice(0, 10),
      subject: newSubj,
      chapter_id: newChap.trim().toLowerCase().replace(/\s+/g, '_') || 'unclassified',
      chapter_name: newChap.trim() || 'অনির্ধারিত',
      question: inputText.trim(),
      options: [],
      correct_index: null,
      explanation: newExp.trim(),
      trap: '',
      is_written: true,
      marks: 1,
      duration_sec: 45,
    };
    const next = addUserQuestion(newQ);
    setUserAddedList(next);
    setShowAddForm(false);
  };

  const handleExportUserQuestions = () => {
    const dateStr = new Date().toISOString().slice(0, 10);
    const blob = new Blob([JSON.stringify(userAddedList, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `user_added_${dateStr}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  if (drill) {
    return (
      <DrillRunner
        questions={drill.questions}
        title={drill.title}
        subtitle={`${drill.questions.length}টি যাচাইকৃত প্রশ্ন`}
        onBack={() => setDrill(null)}
        bookmarkSource="matcher"
      />
    );
  }

  const topMatch = matches?.[0] || null;

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <Target className="w-6 h-6 text-emerald-600" /> 🎯 প্রশ্ন ম্যাচার — "এই প্রশ্ন কতটুকু কমন?"
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            কোচিং বা মডেল টেস্টের প্রশ্ন পেস্ট করো — ব্যাংকের {BANK_INDEX.total_questions}টি যাচাইকৃত প্রশ্নের সাথে মিলিয়ে কমনতা, বছর ও ট্র্যাপ দেখো।
          </p>
        </div>

        <button
          onClick={handleLoadSample}
          className="px-3.5 py-2 rounded-xl bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 text-xs font-bold cursor-pointer flex items-center gap-1.5"
        >
          <Sparkles className="w-3.5 h-3.5" /> নমুনা প্রশ্ন দিয়ে দেখো
        </button>
      </div>

      {/* Input Card */}
      <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-6 space-y-4 shadow-xs">
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          rows={4}
          placeholder="coaching-এর প্রশ্ন এখানে paste করো (LaTeX সহ, অথবা ৪টি অপশনসহ)..."
          className="w-full rounded-2xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800/60 p-4 text-sm text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-emerald-500"
        />

        <div className="flex flex-wrap items-center justify-between gap-3">
          <span className="text-[11px] text-slate-500">
            অ্যালগরিদম: ৩-গ্রাম টোকেন শিংগল + জ্যাকার্ড সাদৃশ্য (১০০% অফলাইন ও ডিটারমিনিস্টিক, কোনো AI নয়)
          </span>
          <div className="flex items-center gap-2">
            {inputText && (
              <button
                onClick={() => {
                  setInputText('');
                  setMatches(null);
                }}
                className="px-3.5 py-2.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold text-slate-600 dark:text-slate-300 cursor-pointer"
              >
                মুছে ফেলো
              </button>
            )}
            <button
              onClick={() => handleSearch()}
              disabled={searching || !inputText.trim()}
              className="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
            >
              <Search className="w-4 h-4" /> {searching ? 'খোঁজা হচ্ছে...' : 'মিল খুঁজো'}
            </button>
          </div>
        </div>
      </div>

      {/* Match Results */}
      {matches !== null && (
        <div className="space-y-4">
          {!topMatch || topMatch.score < 0.8 ? (
            <div className="bg-white dark:bg-slate-900 rounded-3xl border-2 border-rose-300 dark:border-rose-800/70 p-5 sm:p-6 space-y-4">
              <div className="flex items-center justify-between gap-2">
                <span className="px-3 py-1 rounded-full bg-rose-100 dark:bg-rose-950/60 text-rose-700 dark:text-rose-300 text-xs font-extrabold">
                  🔴 নতুন প্রশ্ন — ব্যাংকে হুবহু নেই
                </span>
                <button
                  onClick={() => setShowAddForm((p) => !p)}
                  className="px-3 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1 cursor-pointer"
                >
                  <PlusCircle className="w-3.5 h-3.5" /> এটা ব্যাংকে যোগ করো
                </button>
              </div>

              {topMatch && (
                <div className="p-4 rounded-2xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/50 space-y-2">
                  <div className="text-xs font-bold text-amber-900 dark:text-amber-200">
                    ⚠️ এটা নতুন হতে পারে, কিন্তু কাছাকাছি টপিক ও অধ্যায় ব্যাংকে আছে ({Math.round(topMatch.score * 100)}% টপিক মিল):
                  </div>
                  <div className="text-sm font-extrabold text-slate-900 dark:text-white">
                    {topMatch.question.subject} · {topMatch.question.chapter_name}
                    {topMatch.question.mega_type ? ` · ${topMatch.question.mega_type}` : ''}
                  </div>
                  <div className="text-xs text-slate-600 dark:text-slate-300">
                    কমনতা: {topMatch.yearsHit} বছরে · {topMatch.papersHit}টি পেপারে এসেছে
                  </div>
                  <button
                    onClick={() =>
                      handleDrillChapter(topMatch.question.chapter_id, topMatch.question.chapter_name)
                    }
                    className="mt-1 px-4 py-2 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-bold inline-flex items-center gap-1.5 cursor-pointer"
                  >
                    <Play className="w-3.5 h-3.5" /> এই chapter-এর সব প্রশ্ন দেখো
                  </button>
                </div>
              )}

              {showAddForm && (
                <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3">
                  <div className="text-xs font-extrabold text-slate-800 dark:text-slate-200">
                    তোমার নিজের কাগজ থেকে ব্যাংকে সংরক্ষণ করো (স্থানীয় স্টোরেজে সেভ হবে ও JSON এক্সপোর্ট করা যাবে):
                  </div>
                  <div className="grid sm:grid-cols-3 gap-2.5">
                    <select
                      value={newSubj}
                      onChange={(e) => setNewSubj(e.target.value as CanonicalSubject)}
                      className="px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-xs font-bold"
                    >
                      {(['Physics', 'Chemistry', 'Higher Math', 'Biology', 'English', 'GK'] as const).map((s) => (
                        <option key={s} value={s}>
                          {s}
                        </option>
                      ))}
                    </select>
                    <input
                      type="text"
                      value={newChap}
                      onChange={(e) => setNewChap(e.target.value)}
                      placeholder="অধ্যায়ের নাম (যেমন: ভেক্টর)"
                      className="px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-xs"
                    />
                    <input
                      type="text"
                      value={newSource}
                      onChange={(e) => setNewSource(e.target.value)}
                      placeholder="উৎস (যেমন: Paper Final 01)"
                      className="px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-xs"
                    />
                  </div>
                  <textarea
                    value={newExp}
                    onChange={(e) => setNewExp(e.target.value)}
                    rows={2}
                    placeholder="সমাধান বা নোট (ঐচ্ছিক)..."
                    className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-xs"
                  />
                  <button
                    onClick={handleSaveUserQuestion}
                    className="px-4 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold cursor-pointer"
                  >
                    সেভ করো
                  </button>
                </div>
              )}
            </div>
          ) : null}

          {matches.map((m) => {
            const q = m.question;
            const pct = Math.round(m.score * 100);
            const commonBar = Math.min(100, Math.round((m.yearsHit / 10) * 100));
            const bm = isBookmarked(q.id);

            return (
              <div
                key={q.id}
                className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-6 space-y-4 shadow-xs"
              >
                <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-100 dark:border-slate-800">
                  <div className="flex flex-wrap items-center gap-2">
                    {m.verdict === 'exact' ? (
                      <span className="px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300 text-xs font-extrabold">
                        ✅ EXACT MATCH — {q.source_name} {q.exam_year ? `(${q.exam_year})` : ''}
                      </span>
                    ) : m.verdict === 'similar' ? (
                      <span className="px-3 py-1 rounded-full bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-300 text-xs font-extrabold">
                        🟡 SIMILAR ({pct}% মিল) — {q.source_name} {q.exam_year ? `(${q.exam_year})` : ''}
                      </span>
                    ) : (
                      <span className="px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-bold">
                        টপিক মিল ({pct}%) — {q.source_name}
                      </span>
                    )}
                  </div>

                  <button
                    onClick={() => {
                      toggleBookmark(q, 'matcher');
                      setBmTick((t) => t + 1);
                    }}
                    className={`p-2 rounded-xl border cursor-pointer ${
                      bm
                        ? 'bg-amber-50 dark:bg-amber-950/50 border-amber-300 text-amber-500'
                        : 'bg-slate-50 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-400'
                    }`}
                    title="বুকমার্ক করো"
                  >
                    <Star className={`w-4 h-4 ${bm ? 'fill-current' : ''}`} />
                  </button>
                </div>

                {/* Commonness & Metadata */}
                <div className="grid sm:grid-cols-2 gap-3 text-xs bg-slate-50 dark:bg-slate-800/50 p-3.5 rounded-2xl">
                  <div className="space-y-1.5">
                    <div className="flex items-center justify-between font-bold text-slate-700 dark:text-slate-200">
                      <span>কমনতা স্কোর:</span>
                      <span className="text-emerald-600 dark:text-emerald-400">
                        {m.yearsHit}/{m.papersHit} ({m.yearsHit} বছরে, {m.papersHit} paper-এ)
                      </span>
                    </div>
                    <div className="h-2 w-full bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-emerald-500 rounded-full"
                        style={{ width: `${commonBar}%` }}
                      />
                    </div>
                  </div>
                  <div className="space-y-1 text-slate-600 dark:text-slate-300">
                    <div>
                      <strong>Chapter:</strong> {q.subject} · {q.chapter_name}
                    </div>
                    {q.mega_type && (
                      <div className="truncate">
                        <strong>Topic:</strong> {q.mega_type}
                      </div>
                    )}
                    {m.predictedPct > 0 && (
                      <div className="text-emerald-600 dark:text-emerald-400 font-bold">
                        ২৬–২৭ সম্ভাবনা: {m.predictedPct}%
                      </div>
                    )}
                  </div>
                </div>

                {/* Question Text */}
                <div className="text-sm sm:text-base font-semibold text-slate-900 dark:text-white">
                  <MathText content={q.question} block />
                </div>

                {/* Trap & Explanation */}
                {q.trap && (
                  <div className="p-3.5 rounded-2xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/50 text-xs">
                    <div className="font-bold text-amber-800 dark:text-amber-300 mb-1 flex items-center gap-1">
                      <AlertTriangle className="w-3.5 h-3.5" /> 🚨 ট্র্যাপ:
                    </div>
                    <MathText content={q.trap} block />
                  </div>
                )}

                {q.explanation && (
                  <div className="p-3.5 rounded-2xl bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/50 text-xs">
                    <div className="font-bold text-emerald-800 dark:text-emerald-300 mb-1 flex items-center gap-1">
                      <BookOpen className="w-3.5 h-3.5" /> 📖 সমাধান:
                    </div>
                    <MathText content={q.explanation} block />
                  </div>
                )}

                <div className="pt-1 flex flex-wrap items-center gap-2">
                  <button
                    onClick={() => handleDrillChapter(q.chapter_id, q.chapter_name)}
                    className="px-4 py-2 rounded-xl bg-slate-900 dark:bg-emerald-600 text-white text-xs font-bold flex items-center gap-1.5 cursor-pointer"
                  >
                    <Play className="w-3.5 h-3.5" /> এই chapter-এর সব প্রশ্ন দেখো
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* User Added Questions Footer */}
      {userAddedList.length > 0 && (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 flex flex-wrap items-center justify-between gap-3">
          <div>
            <div className="text-sm font-extrabold text-slate-900 dark:text-white">
              তোমার সংরক্ষিত নতুন প্রশ্ন: {userAddedList.length}টি
            </div>
            <div className="text-xs text-slate-500">
              JSON হিসেবে এক্সপোর্ট করে <code className="px-1 rounded bg-slate-100 dark:bg-slate-800">src/data/bank/du_ka/past_paper/</code> এ যোগ করতে পারো।
            </div>
          </div>
          <button
            onClick={handleExportUserQuestions}
            className="px-4 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1.5 cursor-pointer"
          >
            <Download className="w-3.5 h-3.5" /> JSON এক্সপোর্ট করো
          </button>
        </div>
      )}
    </div>
  );
};
