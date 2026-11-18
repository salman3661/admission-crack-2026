import React, { useState, useMemo, useEffect } from 'react';
import {
  FileText,
  Timer,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  Award,
  ArrowLeft,
  Zap,
  ShieldAlert,
  BookOpen,
  ChevronRight,
  ChevronLeft,
} from 'lucide-react';
import confetti from 'canvas-confetti';
import paperFinalRaw from '../data/paper_final_bank.json';
import { MathText } from './MathText';
import type { PaperFinalBank, PaperFinalTest, TrackType } from '../types';

interface PaperFinalViewProps {
  activeTrack: TrackType;
}

const toBn = (num: number | string): string => {
  const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
  return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)] ?? d);
};

export const PaperFinalView: React.FC<PaperFinalViewProps> = ({ activeTrack }) => {
  const bank = paperFinalRaw as unknown as PaperFinalBank;

  const [selectedSubject, setSelectedSubject] = useState<string>('All');
  const [selectedPaper, setSelectedPaper] = useState<string>('All');

  // Active exam session state
  const [activeTest, setActiveTest] = useState<PaperFinalTest | null>(null);
  const [examTab, setExamTab] = useState<'mcq' | 'written'>('mcq');
  const [currentMcqIdx, setCurrentMcqIdx] = useState(0);
  const [userAnswers, setUserAnswers] = useState<Record<number, number | null>>({});
  const [revealedWritten, setRevealedWritten] = useState<Record<number, boolean>>({});
  const [timeLeft, setTimeLeft] = useState(0);
  const [isFinished, setIsFinished] = useState(false);

  // Reset active test if track changes
  useEffect(() => {
    setActiveTest(null);
    setSelectedSubject('All');
    setSelectedPaper('All');
  }, [activeTrack]);

  useEffect(() => {
    window.dispatchEvent(new CustomEvent('ac-exam-focus', { detail: Boolean(activeTest) }));
    return () => {
      window.dispatchEvent(new CustomEvent('ac-exam-focus', { detail: false }));
    };
  }, [activeTest]);

  const trackTests = useMemo(() => {
    return (bank.tests || []).filter((t) => t.track === activeTrack);
  }, [bank.tests, activeTrack]);

  const filteredTests = useMemo(() => {
    return trackTests.filter((t) => {
      const matchSubj = selectedSubject === 'All' || t.subject === selectedSubject;
      const matchPaper = selectedPaper === 'All' || t.paper === selectedPaper;
      return matchSubj && matchPaper;
    });
  }, [trackTests, selectedSubject, selectedPaper]);

  const startTest = (test: PaperFinalTest) => {
    setActiveTest(test);
    setExamTab('mcq');
    setCurrentMcqIdx(0);
    setUserAnswers({});
    setRevealedWritten({});
    setTimeLeft((test.duration_minutes || 90) * 60);
    setIsFinished(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const finishTest = () => {
    setIsFinished(true);
    try {
      confetti({ particleCount: 70, spread: 65, origin: { y: 0.6 } });
    } catch {
      // ignore
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  useEffect(() => {
    if (!activeTest || isFinished) return;
    if (timeLeft <= 0) {
      finishTest();
      return;
    }
    const timer = setInterval(() => setTimeLeft((p) => p - 1), 1000);
    return () => clearInterval(timer);
  }, [activeTest, isFinished, timeLeft]);

  const stats = useMemo(() => {
    if (!activeTest) return { correct: 0, wrong: 0, skipped: 0, mcqScore: 0, totalMcqs: 0 };
    let correct = 0;
    let wrong = 0;
    let skipped = 0;
    activeTest.mcqs.forEach((q, idx) => {
      const ans = userAnswers[idx];
      if (ans === undefined || ans === null) skipped++;
      else if (ans === q.ans) correct++;
      else wrong++;
    });
    const neg = activeTest.negative_marking ?? 0.25;
    const mcqScore = Math.max(0, correct - wrong * neg);
    return { correct, wrong, skipped, mcqScore, totalMcqs: activeTest.mcqs.length };
  }, [activeTest, userAnswers]);

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const subjects =
    activeTrack === 'medical'
      ? ['All', 'Physics', 'Chemistry', 'Biology', 'English', 'GK', 'ICT']
      : ['All', 'Physics', 'Chemistry', 'Higher Math', 'Biology', 'Bangla', 'English', 'GK', 'ICT'];

  // =========================================================================
  // ACTIVE PAPER FINAL EXAM SIMULATOR
  // =========================================================================
  if (activeTest) {
    const currentQ = activeTest.mcqs[currentMcqIdx];

    return (
      <div className="max-w-5xl mx-auto px-4 sm:px-6 py-5 pb-32 space-y-5">
        {/* Top Sticky Exam Bar */}
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm flex flex-wrap items-center justify-between gap-3 sticky top-16 z-30">
          <div className="flex items-center gap-3 min-w-0">
            <button
              onClick={() => setActiveTest(null)}
              className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 cursor-pointer"
              title="পেপার ফাইনাল তালিকায় ফিরে যান"
            >
              <ArrowLeft className="w-4 h-4" />
            </button>
            <div className="min-w-0">
              <div className="text-xs font-bold text-indigo-600 dark:text-indigo-400">
                Tier 2: {activeTest.badge}
              </div>
              <h2 className="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white truncate">
                {activeTest.title}
              </h2>
            </div>
          </div>

          <div className="flex items-center gap-2.5">
            {!isFinished ? (
              <>
                <div
                  className={`px-3 py-1.5 rounded-xl font-mono text-xs sm:text-sm font-black flex items-center gap-1.5 border ${
                    timeLeft < 300
                      ? 'bg-rose-500/15 text-rose-600 dark:text-rose-400 border-rose-500/30 animate-pulse'
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-100 border-slate-200 dark:border-slate-700'
                  }`}
                >
                  <Timer className="w-4 h-4" />
                  {formatTimer(timeLeft)}
                </div>
                <button
                  onClick={finishTest}
                  className="px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs sm:text-sm font-bold shadow-sm cursor-pointer active:scale-95"
                >
                  সাবমিট করুন
                </button>
              </>
            ) : (
              <button
                onClick={() => startTest(activeTest)}
                className="px-4 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs sm:text-sm font-bold shadow-sm cursor-pointer"
              >
                পুনরায় পরীক্ষা দিন
              </button>
            )}
          </div>
        </div>

        {/* Scorecard after submit */}
        {isFinished && (
          <div className="bg-gradient-to-br from-emerald-500/10 via-teal-500/5 to-indigo-500/10 border border-emerald-500/30 rounded-3xl p-5 sm:p-6 space-y-4">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 rounded-2xl bg-emerald-600 text-white flex items-center justify-center shadow-md">
                <Award className="w-6 h-6" />
              </div>
              <div>
                <h3 className="text-lg sm:text-xl font-extrabold text-slate-900 dark:text-white">
                  পেপার ফাইনাল ফলাফল (MCQ স্কোরকার্ড)
                </h3>
                <p className="text-xs text-slate-600 dark:text-slate-400">
                  নেগেটিভ মার্কিং: -{activeTest.negative_marking} প্রতি ভুল উত্তরে
                  {activeTest.target_written > 0 && ' • নিচে ১৬টি লিখিত (Written) প্রশ্নের সমাধান ও রুব্রিক দেখুন'}
                </p>
              </div>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
              <div className="bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200 dark:border-slate-800">
                <div className="text-[11px] font-bold text-slate-500">প্রাপ্ত MCQ নম্বর</div>
                <div className="text-xl font-black text-emerald-600 dark:text-emerald-400">
                  {stats.mcqScore.toFixed(2)} / {stats.totalMcqs}
                </div>
              </div>
              <div className="bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200 dark:border-slate-800">
                <div className="text-[11px] font-bold text-slate-500">সঠিক উত্তর</div>
                <div className="text-xl font-black text-teal-600 dark:text-teal-400">
                  {toBn(stats.correct)}টি
                </div>
              </div>
              <div className="bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200 dark:border-slate-800">
                <div className="text-[11px] font-bold text-slate-500">ভুল উত্তর</div>
                <div className="text-xl font-black text-rose-600 dark:text-rose-400">
                  {toBn(stats.wrong)}টি
                </div>
              </div>
              <div className="bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200 dark:border-slate-800">
                <div className="text-[11px] font-bold text-slate-500">উত্তর করেননি</div>
                <div className="text-xl font-black text-slate-600 dark:text-slate-300">
                  {toBn(stats.skipped)}টি
                </div>
              </div>
            </div>
          </div>
        )}

        {/* MCQ vs Written Section Tabs */}
        <div className="flex items-center gap-2 bg-slate-100 dark:bg-slate-900 p-1.5 rounded-2xl border border-slate-200 dark:border-slate-800 w-fit">
          <button
            onClick={() => setExamTab('mcq')}
            className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer ${
              examTab === 'mcq'
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            📝 MCQ অংশ ({toBn(activeTest.mcqs.length)}টি • {toBn(activeTest.mcq_marks)} নম্বর)
          </button>
          {activeTest.written_questions.length > 0 && (
            <button
              onClick={() => setExamTab('written')}
              className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer ${
                examTab === 'written'
                  ? 'bg-amber-600 text-white shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              ✍️ লিখিত অংশ ({toBn(activeTest.written_questions.length)}টি × ২.৫ = {toBn(activeTest.written_marks)} নম্বর)
            </button>
          )}
        </div>

        {/* MCQ SECTION */}
        {examTab === 'mcq' && !isFinished && currentQ && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
            <div className="lg:col-span-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-6 shadow-sm space-y-5">
              <div className="flex items-center justify-between gap-2 flex-wrap">
                <span className="px-2.5 py-1 rounded-lg bg-indigo-500/10 text-indigo-700 dark:text-indigo-300 text-xs font-bold">
                  প্রশ্ন {toBn(currentMcqIdx + 1)} / {toBn(activeTest.mcqs.length)}
                </span>
                {currentQ.origin && (
                  <span className="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-[11px] font-bold">
                    {currentQ.origin}
                  </span>
                )}
              </div>

              <div className="text-base sm:text-lg font-bold text-slate-900 dark:text-white leading-relaxed">
                <MathText content={currentQ.q} />
              </div>

              <div className="space-y-2.5">
                {currentQ.opts.map((opt, oIdx) => {
                  const isSelected = userAnswers[currentMcqIdx] === oIdx;
                  return (
                    <button
                      key={oIdx}
                      onClick={() =>
                        setUserAnswers((prev) => ({
                          ...prev,
                          [currentMcqIdx]: prev[currentMcqIdx] === oIdx ? null : oIdx,
                        }))
                      }
                      className={`w-full p-3.5 rounded-2xl border text-left flex items-center gap-3 transition-all cursor-pointer ${
                        isSelected
                          ? 'bg-indigo-600/10 border-indigo-600 text-indigo-900 dark:text-indigo-100 ring-1 ring-indigo-600'
                          : 'bg-slate-50/80 dark:bg-slate-800/60 border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800'
                      }`}
                    >
                      <span
                        className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-black shrink-0 ${
                          isSelected
                            ? 'bg-indigo-600 text-white'
                            : 'bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-600'
                        }`}
                      >
                        {['ক', 'খ', 'গ', 'ঘ'][oIdx] ?? oIdx + 1}
                      </span>
                      <div className="text-sm sm:text-base font-medium flex-1">
                        <MathText content={opt} />
                      </div>
                    </button>
                  );
                })}
              </div>

              <div className="flex items-center justify-between pt-3 border-t border-slate-200 dark:border-slate-800">
                <button
                  disabled={currentMcqIdx === 0}
                  onClick={() => setCurrentMcqIdx((p) => Math.max(0, p - 1))}
                  className="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 text-xs font-bold disabled:opacity-40 flex items-center gap-1 cursor-pointer"
                >
                  <ChevronLeft className="w-4 h-4" /> পূর্ববর্তী
                </button>
                <button
                  disabled={currentMcqIdx === activeTest.mcqs.length - 1}
                  onClick={() => setCurrentMcqIdx((p) => Math.min(activeTest.mcqs.length - 1, p + 1))}
                  className="px-4 py-2 rounded-xl bg-indigo-600 text-white text-xs font-bold disabled:opacity-40 flex items-center gap-1 cursor-pointer"
                >
                  পরবর্তী <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Question Navigator Palette */}
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-4 shadow-sm h-fit">
              <div className="text-xs font-extrabold text-slate-700 dark:text-slate-200 mb-3">
                প্রশ্ন নেভিগেটর ({toBn(Object.values(userAnswers).filter((v) => v !== null && v !== undefined).length)}/{toBn(activeTest.mcqs.length)})
              </div>
              <div className="grid grid-cols-6 sm:grid-cols-8 lg:grid-cols-6 gap-1.5">
                {activeTest.mcqs.map((_, idx) => {
                  const answered = userAnswers[idx] !== undefined && userAnswers[idx] !== null;
                  const active = idx === currentMcqIdx;
                  return (
                    <button
                      key={idx}
                      onClick={() => setCurrentMcqIdx(idx)}
                      className={`h-8 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                        active
                          ? 'bg-indigo-600 text-white ring-2 ring-indigo-400'
                          : answered
                          ? 'bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 border border-emerald-500/40'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                      }`}
                    >
                      {idx + 1}
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* MCQ REVIEW AFTER FINISH */}
        {examTab === 'mcq' && isFinished && (
          <div className="space-y-4">
            {activeTest.mcqs.map((q, idx) => {
              const userAns = userAnswers[idx];
              const isCorrect = userAns === q.ans;
              const isSkipped = userAns === undefined || userAns === null;
              return (
                <div
                  key={q.id || idx}
                  className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 space-y-3"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="text-sm sm:text-base font-bold text-slate-900 dark:text-white">
                      <span className="text-indigo-600 dark:text-indigo-400 mr-2">#{toBn(idx + 1)}</span>
                      <MathText content={q.q} />
                    </div>
                    <span
                      className={`px-2.5 py-1 rounded-lg text-[11px] font-bold shrink-0 flex items-center gap-1 ${
                        isSkipped
                          ? 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                          : isCorrect
                          ? 'bg-emerald-500/15 text-emerald-700 dark:text-emerald-300'
                          : 'bg-rose-500/15 text-rose-700 dark:text-rose-300'
                      }`}
                    >
                      {isSkipped ? (
                        <>
                          <AlertTriangle className="w-3.5 h-3.5" /> স্কিপড
                        </>
                      ) : isCorrect ? (
                        <>
                          <CheckCircle2 className="w-3.5 h-3.5" /> সঠিক
                        </>
                      ) : (
                        <>
                          <XCircle className="w-3.5 h-3.5" /> ভুল
                        </>
                      )}
                    </span>
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    {q.opts.map((opt, oIdx) => {
                      const right = oIdx === q.ans;
                      const picked = oIdx === userAns;
                      return (
                        <div
                          key={oIdx}
                          className={`p-2.5 rounded-xl border text-xs sm:text-sm flex items-center gap-2 ${
                            right
                              ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-900 dark:text-emerald-200 font-bold'
                              : picked
                              ? 'bg-rose-500/15 border-rose-500/40 text-rose-900 dark:text-rose-200'
                              : 'bg-slate-50 dark:bg-slate-800/50 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300'
                          }`}
                        >
                          <span className="font-black">{['ক', 'খ', 'গ', 'ঘ'][oIdx]}.</span>
                          <MathText content={opt} />
                        </div>
                      );
                    })}
                  </div>

                  {(q.exp || q.speed_hack || q.trap_alert || q.trap) && (
                    <div className="pt-2 space-y-2 text-xs">
                      {q.exp && (
                        <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/70 text-slate-700 dark:text-slate-300">
                          <span className="font-bold text-slate-900 dark:text-white mr-1">💡 ব্যাখ্যা:</span>
                          <MathText content={q.exp} />
                        </div>
                      )}
                      {q.speed_hack && (
                        <div className="p-2.5 rounded-xl bg-emerald-500/10 text-emerald-800 dark:text-emerald-200 flex items-start gap-1.5">
                          <Zap className="w-3.5 h-3.5 shrink-0 mt-0.5" />
                          <span>
                            <strong>স্পিড হ্যাক:</strong> <MathText content={q.speed_hack} />
                          </span>
                        </div>
                      )}
                      {(q.trap_alert || q.trap) && (
                        <div className="p-2.5 rounded-xl bg-amber-500/10 text-amber-800 dark:text-amber-200 flex items-start gap-1.5">
                          <ShieldAlert className="w-3.5 h-3.5 shrink-0 mt-0.5" />
                          <span>
                            <strong>ট্র্যাপ অ্যালার্ট:</strong> <MathText content={q.trap_alert || q.trap} />
                          </span>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}

        {/* WRITTEN SECTION (16 Questions × 2.5 Marks) */}
        {examTab === 'written' && (
          <div className="space-y-4">
            {activeTest.written_questions.map((wp, idx) => {
              const revealed = !!revealedWritten[idx];
              return (
                <div
                  key={idx}
                  className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 space-y-3 shadow-xs"
                >
                  <div className="flex items-center justify-between gap-2">
                    <span className="px-2.5 py-1 rounded-lg bg-amber-500/15 text-amber-700 dark:text-amber-300 text-xs font-extrabold">
                      লিখিত প্রশ্ন {toBn(idx + 1)} / {toBn(activeTest.written_questions.length)}
                    </span>
                    <span className="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-bold">
                      নম্বর: ২.৫
                    </span>
                  </div>

                  <div className="text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-relaxed">
                    <MathText content={wp.problem} />
                  </div>

                  <button
                    onClick={() => setRevealedWritten((prev) => ({ ...prev, [idx]: !prev[idx] }))}
                    className="px-3.5 py-1.5 rounded-xl bg-amber-500/15 hover:bg-amber-500/25 text-amber-800 dark:text-amber-300 text-xs font-bold flex items-center gap-1.5 cursor-pointer"
                  >
                    <BookOpen className="w-3.5 h-3.5" />
                    {revealed ? 'সমাধান লুকান' : 'পূর্ণাঙ্গ সমাধান ও নম্বর বণ্টন দেখুন'}
                  </button>

                  {revealed && (
                    <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 space-y-2 text-xs sm:text-sm text-slate-800 dark:text-slate-200">
                      <div className="font-bold text-emerald-700 dark:text-emerald-300">✅ সমাধান:</div>
                      <MathText content={wp.solution} />
                      {wp.rubric && (
                        <div className="pt-2 border-t border-emerald-500/20 text-[11px] font-bold text-slate-600 dark:text-slate-400">
                          📊 রুব্রিক: {wp.rubric}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </div>
    );
  }

  // =========================================================================
  // PAPER FINAL DIRECTORY VIEW
  // =========================================================================
  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 py-5 pb-32 space-y-5">
      {/* Hero Banner */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-7 shadow-sm space-y-4">
        <div className="flex items-center gap-2 flex-wrap">
          <span className="px-3 py-1 rounded-full text-xs font-black bg-indigo-500/15 text-indigo-700 dark:text-indigo-300 border border-indigo-500/30 flex items-center gap-1.5">
            <FileText className="w-3.5 h-3.5" />
            Tier 2: Paper Final Section
          </span>
          <span className="px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border border-emerald-500/20">
            {activeTrack === 'medical' ? '🩺 মেডিকেল MAT স্ট্যান্ডার্ড' : "🎯 ভার্সিটি 'ক' (60 MCQ + 16 Written)"}
          </span>
        </div>

        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white tracking-tight">
            📄 পেপার ফাইনাল মডেল টেস্ট (Paper Final Bank)
          </h1>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1.5 max-w-3xl leading-relaxed">
            কলেজ ও কোচিং-স্ট্যান্ডার্ড ১ম ও ২য় পত্র পেপার ফাইনাল পরীক্ষা। প্রতিটি ভার্সিটি পেপার ফাইনালে ৬০টি MCQ ও ১৬টি লিখিত (২.৫ নম্বর করে) প্রশ্ন রয়েছে—উইকলি সলভ শিট থেকে সম্পূর্ণ আলাদা।
          </p>
        </div>

        {/* Filters */}
        <div className="pt-3 border-t border-slate-200 dark:border-slate-800 flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar">
            {subjects.map((s) => (
              <button
                key={s}
                onClick={() => setSelectedSubject(s)}
                className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer whitespace-nowrap ${
                  selectedSubject === s
                    ? 'bg-indigo-600 text-white shadow-xs'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                }`}
              >
                {s === 'All' ? 'সব বিষয়' : s}
              </button>
            ))}
          </div>

          <div className="flex items-center gap-1.5">
            {['All', '১ম পত্র', '২য় পত্র'].map((p) => (
              <button
                key={p}
                onClick={() => setSelectedPaper(p)}
                className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                  selectedPaper === p
                    ? 'bg-amber-600 text-white shadow-xs'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                }`}
              >
                {p === 'All' ? 'সব পত্র' : p}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Paper Final Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredTests.map((test) => (
          <div
            key={test.id}
            className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 shadow-xs hover:shadow-md hover:border-indigo-500/40 transition-all flex flex-col justify-between gap-4"
          >
            <div className="space-y-2.5">
              <div className="flex items-center justify-between gap-2">
                <span className="px-2.5 py-1 rounded-lg bg-indigo-500/10 text-indigo-700 dark:text-indigo-300 text-[11px] font-extrabold">
                  {test.badge}
                </span>
                <span className="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-[11px] font-bold">
                  ⏱️ {toBn(test.duration_minutes)} মিনিট
                </span>
              </div>

              <h3 className="text-base sm:text-lg font-extrabold text-slate-900 dark:text-white">
                {test.title}
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-400">{test.subtitle}</p>

              <div className="flex flex-wrap gap-2 pt-1">
                <span className="px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 text-[11px] font-bold">
                  📝 {toBn(test.target_mcqs)} MCQ
                </span>
                {test.target_written > 0 && (
                  <span className="px-2.5 py-1 rounded-lg bg-amber-500/10 text-amber-700 dark:text-amber-300 text-[11px] font-bold">
                    ✍️ {toBn(test.target_written)} Written (×২.৫)
                  </span>
                )}
                <span className="px-2.5 py-1 rounded-lg bg-purple-500/10 text-purple-700 dark:text-purple-300 text-[11px] font-bold">
                  🎯 মোট {toBn(test.total_marks)} নম্বর
                </span>
              </div>
            </div>

            <button
              onClick={() => startTest(test)}
              className="w-full py-2.5 rounded-2xl bg-gradient-to-r from-indigo-600 to-blue-600 hover:from-indigo-700 hover:to-blue-700 text-white text-xs sm:text-sm font-extrabold shadow-sm cursor-pointer active:scale-[0.99] transition-all"
            >
              পেপার ফাইনাল শুরু করুন →
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
