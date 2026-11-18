import React, { useState, useEffect, useMemo } from 'react';
import {
  CheckCircle2,
  XCircle,
  Clock,
  ChevronLeft,
  ChevronRight,
  AlertTriangle,
  BookOpen,
  Sparkles,
  FileText,
  RotateCcw,
} from 'lucide-react';
import { MathText } from './MathText';
import {
  type Question,
  getShuffledOptions,
  addErrorLogEntry,
  recordAttemptStat,
} from '../lib/library';

interface DrillRunnerProps {
  questions: Question[];
  title: string;
  subtitle?: string;
  onBack?: () => void;
  softTimerSec?: number;
}

const OPTION_LABELS = ['ক', 'খ', 'গ', 'ঘ', 'ঙ'];

export const DrillRunner: React.FC<DrillRunnerProps> = ({
  questions,
  title,
  subtitle,
  onBack,
  softTimerSec = 45,
}) => {
  const [idx, setIdx] = useState(0);
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [writtenDrafts, setWrittenDrafts] = useState<Record<string, string>>(() => {
    try {
      const raw = localStorage.getItem('ac_written_drafts_v1');
      return raw ? JSON.parse(raw) : {};
    } catch {
      return {};
    }
  });
  const [revealedWritten, setRevealedWritten] = useState<Record<string, boolean>>({});
  const [elapsed, setElapsed] = useState(0);
  const [showSummary, setShowSummary] = useState(false);

  const q = questions[idx];

  useEffect(() => {
    setElapsed(0);
    if (!q || showSummary) return;
    const t = setInterval(() => setElapsed((s) => s + 1), 1000);
    return () => clearInterval(t);
  }, [idx, q?.id, showSummary]);

  const shuffled = useMemo(() => {
    if (!q) return { options: [], correctIndex: null, order: [] };
    return getShuffledOptions(q);
  }, [q]);

  if (!questions.length) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-12 text-center">
        <p className="text-slate-500 dark:text-slate-400">এই সেটে কোনো প্রশ্ন পাওয়া যায়নি।</p>
        {onBack && (
          <button
            onClick={onBack}
            className="mt-4 px-4 py-2 rounded-xl bg-emerald-600 text-white text-sm font-bold cursor-pointer"
          >
            ফিরে যাও
          </button>
        )}
      </div>
    );
  }

  const handleSelectOption = (shuffledOptIdx: number) => {
    if (!q || q.is_written || answers[q.id] !== undefined) return;
    setAnswers((prev) => ({ ...prev, [q.id]: shuffledOptIdx }));
    const isCorrect = shuffledOptIdx === shuffled.correctIndex;
    recordAttemptStat(q, isCorrect, 0.25);
    if (!isCorrect) {
      addErrorLogEntry(q, shuffled.order[shuffledOptIdx] ?? shuffledOptIdx);
    }
  };

  const handleWrittenChange = (qid: string, val: string) => {
    const next = { ...writtenDrafts, [qid]: val };
    setWrittenDrafts(next);
    try {
      localStorage.setItem('ac_written_drafts_v1', JSON.stringify(next));
    } catch {
      // ignore
    }
  };

  const mcqQuestions = questions.filter((x) => !x.is_written && x.options.length > 0);
  const answeredMcqs = mcqQuestions.filter((x) => answers[x.id] !== undefined);
  const correctMcqs = mcqQuestions.filter((x) => {
    const a = answers[x.id];
    if (a === undefined) return false;
    const sh = getShuffledOptions(x);
    return a === sh.correctIndex;
  });
  const wrongMcqs = answeredMcqs.length - correctMcqs.length;
  const netScore = +(correctMcqs.length - wrongMcqs * 0.25).toFixed(2);

  if (showSummary) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-8">
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-xl font-extrabold text-slate-900 dark:text-white">{title} — ফলাফল</h2>
              <p className="text-xs text-slate-500 mt-1">ভুলগুলো স্বয়ংক্রিয়ভাবে Mistake Book-এ যুক্ত হয়েছে</p>
            </div>
            <button
              onClick={() => {
                setAnswers({});
                setIdx(0);
                setShowSummary(false);
              }}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold cursor-pointer"
            >
              <RotateCcw className="w-3.5 h-3.5" /> আবার দাও
            </button>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-6">
            <div className="p-4 rounded-2xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/40">
              <div className="text-xs text-emerald-700 dark:text-emerald-400 font-bold">সঠিক</div>
              <div className="text-2xl font-black text-emerald-700 dark:text-emerald-300">{correctMcqs.length}</div>
            </div>
            <div className="p-4 rounded-2xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800/40">
              <div className="text-xs text-rose-700 dark:text-rose-400 font-bold">ভুল (−০.২৫)</div>
              <div className="text-2xl font-black text-rose-700 dark:text-rose-300">{wrongMcqs}</div>
            </div>
            <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
              <div className="text-xs text-slate-600 dark:text-slate-400 font-bold">নেট স্কোর</div>
              <div className="text-2xl font-black text-slate-900 dark:text-white">{netScore}</div>
            </div>
            <div className="p-4 rounded-2xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800/40">
              <div className="text-xs text-blue-700 dark:text-blue-400 font-bold">Accuracy</div>
              <div className="text-2xl font-black text-blue-700 dark:text-blue-300">
                {answeredMcqs.length ? Math.round((correctMcqs.length / answeredMcqs.length) * 100) : 0}%
              </div>
            </div>
          </div>

          {onBack && (
            <button
              onClick={onBack}
              className="w-full py-3 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm cursor-pointer"
            >
              তালিকায় ফিরে যাও
            </button>
          )}
        </div>
      </div>
    );
  }

  const selectedOpt = answers[q.id];
  const isAnswered = selectedOpt !== undefined;
  const overTime = !q.is_written && elapsed > softTimerSec;

  return (
    <div className="max-w-3xl mx-auto px-3 sm:px-4 py-6">
      {/* Header */}
      <div className="flex items-center justify-between gap-3 mb-4">
        <div className="flex items-center gap-2 min-w-0">
          {onBack && (
            <button
              onClick={onBack}
              className="p-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:bg-slate-50 cursor-pointer shrink-0"
              title="ফিরে যাও"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
          )}
          <div className="min-w-0">
            <h1 className="text-base sm:text-lg font-extrabold text-slate-900 dark:text-white truncate">{title}</h1>
            {subtitle && <p className="text-xs text-slate-500 truncate">{subtitle}</p>}
          </div>
        </div>

        <div className="flex items-center gap-2 shrink-0">
          <span
            className={`flex items-center gap-1 px-2.5 py-1 rounded-xl text-xs font-bold border ${
              overTime
                ? 'bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 border-amber-300'
                : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-800'
            }`}
          >
            <Clock className="w-3.5 h-3.5" />
            {elapsed}s {!q.is_written && `/ ${softTimerSec}s`}
          </span>
          <span className="px-2.5 py-1 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 text-xs font-extrabold border border-emerald-200 dark:border-emerald-800/50">
            {idx + 1} / {questions.length}
          </span>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="h-1.5 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden mb-5">
        <div
          className="h-full bg-gradient-to-r from-emerald-500 to-teal-500 transition-all duration-300"
          style={{ width: `${((idx + 1) / questions.length) * 100}%` }}
        />
      </div>

      {/* Question Card */}
      <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/90 dark:border-slate-800 p-5 sm:p-7 shadow-sm">
        {/* F13: Provenance / Theory of the question */}
        <div className="flex flex-wrap items-center gap-1.5 mb-4 text-[11px]">
          <span className="px-2.5 py-0.5 rounded-full font-bold bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border border-emerald-200/70 dark:border-emerald-800/60">
            📌 {q.subject} · {q.chapter_name}
          </span>
          <span className="px-2.5 py-0.5 rounded-full font-semibold bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
            উৎস: {q.source_name}
            {q.exam_year ? ` (${q.exam_year})` : ''}
          </span>
          {q.years_hit && (
            <span className="px-2.5 py-0.5 rounded-full font-semibold bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300">
              এসেছে: {q.years_hit}টি বছরে{q.papers_hit ? `, ${q.papers_hit}টি paper-এ` : ''}
            </span>
          )}
          {q.likelihood_pct !== undefined && q.likelihood_pct > 0 && (
            <span className="px-2.5 py-0.5 rounded-full font-semibold bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300">
              সম্ভাবনা: {q.likelihood_pct}%
            </span>
          )}
          {q.is_written && (
            <span className="px-2.5 py-0.5 rounded-full font-extrabold bg-purple-100 dark:bg-purple-950/50 text-purple-700 dark:text-purple-300">
              ✍️ লিখিত ({q.marks} নম্বর)
            </span>
          )}
        </div>

        {q.mega_type && (
          <div className="text-xs text-slate-500 dark:text-slate-400 mb-2 font-medium flex items-center gap-1">
            <Sparkles className="w-3.5 h-3.5 text-amber-500" />
            {q.mega_type}
          </div>
        )}

        {/* Question Stem */}
        <div className="text-base sm:text-lg font-semibold text-slate-900 dark:text-white mb-6 leading-relaxed">
          <MathText content={q.question} block />
        </div>

        {/* Rule 7: Written card when options: [] or is_written */}
        {q.is_written || shuffled.options.length === 0 ? (
          <div className="space-y-4">
            <div className="p-3.5 rounded-2xl bg-purple-50/70 dark:bg-purple-950/20 border border-purple-200 dark:border-purple-800/40 text-xs text-purple-800 dark:text-purple-200 flex items-start gap-2">
              <FileText className="w-4 h-4 shrink-0 mt-0.5" />
              <div>
                <strong>সিলেবাস স্টাইলে লিখো:</strong> সূত্র → কাজ → উত্তর। লিখিত প্রশ্নে নেগেটিভ মার্কিং নেই, আংশিক নম্বর (partial credit) আছে — তাই খালি রাখবে না।
              </div>
            </div>

            <textarea
              value={writtenDrafts[q.id] || ''}
              onChange={(e) => handleWrittenChange(q.id, e.target.value)}
              rows={5}
              placeholder="এখানে তোমার সমাধান বা মূল সূত্র ও ধাপগুলো লিখে রাখো..."
              className="w-full rounded-2xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800/60 p-4 text-sm text-slate-800 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-emerald-500"
            />

            <button
              onClick={() => setRevealedWritten((p) => ({ ...p, [q.id]: !p[q.id] }))}
              className="px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold cursor-pointer"
            >
              {revealedWritten[q.id] ? 'মডেল উত্তর লুকাও' : 'মডেল উত্তর ও ব্যাখ্যা দেখো'}
            </button>

            {revealedWritten[q.id] && (
              <div className="p-4 rounded-2xl bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/50 text-sm">
                <div className="font-bold text-emerald-800 dark:text-emerald-300 mb-1.5 flex items-center gap-1.5">
                  <BookOpen className="w-4 h-4" /> মডেল উত্তর
                </div>
                <MathText content={q.explanation || 'ব্যাখ্যা যুক্ত করা হয়নি।'} block />
              </div>
            )}
          </div>
        ) : (
          /* MCQ Options (Session-Stable Shuffled) */
          <div className="space-y-2.5">
            {shuffled.options.map((opt, i) => {
              const isSelected = selectedOpt === i;
              const isCorrectOpt = shuffled.correctIndex === i;

              let btnClass =
                'bg-slate-50 dark:bg-slate-800/60 border-slate-200 dark:border-slate-700/80 hover:border-emerald-400 hover:bg-emerald-50/40 dark:hover:bg-emerald-950/20 text-slate-800 dark:text-slate-100';
              if (isAnswered) {
                if (isCorrectOpt) {
                  btnClass =
                    'bg-emerald-50 dark:bg-emerald-950/50 border-emerald-500 text-emerald-900 dark:text-emerald-100 ring-1 ring-emerald-500/40';
                } else if (isSelected && !isCorrectOpt) {
                  btnClass =
                    'bg-rose-50 dark:bg-rose-950/50 border-rose-500 text-rose-900 dark:text-rose-100 ring-1 ring-rose-500/40';
                } else {
                  btnClass = 'bg-slate-50/60 dark:bg-slate-900 border-slate-200/60 dark:border-slate-800 opacity-60';
                }
              }

              return (
                <button
                  key={i}
                  disabled={isAnswered}
                  onClick={() => handleSelectOption(i)}
                  className={`w-full text-left p-3.5 sm:p-4 rounded-2xl border transition-all flex items-start gap-3 cursor-pointer disabled:cursor-default ${btnClass}`}
                >
                  <span className="w-7 h-7 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 flex items-center justify-center text-xs font-extrabold shrink-0">
                    {OPTION_LABELS[i] || i + 1}
                  </span>
                  <div className="flex-1 text-sm sm:text-base pt-0.5">
                    <MathText content={opt} />
                  </div>
                  {isAnswered && isCorrectOpt && <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0 mt-0.5" />}
                  {isAnswered && isSelected && !isCorrectOpt && <XCircle className="w-5 h-5 text-rose-600 shrink-0 mt-0.5" />}
                </button>
              );
            })}
          </div>
        )}

        {/* Explanation + Trap after MCQ answer */}
        {isAnswered && !q.is_written && (
          <div className="mt-5 space-y-3">
            {q.explanation && (
              <div className="p-4 rounded-2xl bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/50 text-sm">
                <div className="font-bold text-emerald-800 dark:text-emerald-300 mb-1 flex items-center gap-1.5">
                  <BookOpen className="w-4 h-4" /> ব্যাখ্যা
                </div>
                <MathText content={q.explanation} block />
              </div>
            )}
            {q.trap && (
              <div className="p-4 rounded-2xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/50 text-sm">
                <div className="font-bold text-amber-800 dark:text-amber-300 mb-1 flex items-center gap-1.5">
                  <AlertTriangle className="w-4 h-4" /> সাধারণ ফাঁদ (Trap Alert)
                </div>
                <MathText content={q.trap} block />
              </div>
            )}
          </div>
        )}

        {/* Navigation Footer */}
        <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between gap-3">
          <button
            onClick={() => setIdx((i) => Math.max(0, i - 1))}
            disabled={idx === 0}
            className="flex items-center gap-1 px-4 py-2.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold disabled:opacity-40 cursor-pointer"
          >
            <ChevronLeft className="w-4 h-4" /> আগেরটি
          </button>

          {idx < questions.length - 1 ? (
            <button
              onClick={() => setIdx((i) => Math.min(questions.length - 1, i + 1))}
              className="flex items-center gap-1 px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold cursor-pointer"
            >
              পরেরটি <ChevronRight className="w-4 h-4" />
            </button>
          ) : (
            <button
              onClick={() => setShowSummary(true)}
              className="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold cursor-pointer"
            >
              ফলাফল দেখো
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
