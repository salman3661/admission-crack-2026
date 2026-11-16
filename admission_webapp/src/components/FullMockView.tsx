import React, { useState, useMemo, useEffect } from 'react';
import {
  Award,
  Timer,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  ArrowLeft,
  Zap,
  ShieldAlert,
  BookOpen,
  ChevronRight,
  ChevronLeft,
  Sparkles,
} from 'lucide-react';
import confetti from 'canvas-confetti';
import fullMockRaw from '../data/full_mock_bank.json';
import { MathText } from './MathText';
import type { FullMockBank, PredictorSet, TrackType } from '../types';

interface FullMockViewProps {
  activeTrack: TrackType;
}

const toBn = (num: number | string): string => {
  const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
  return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)] ?? d);
};

export const FullMockView: React.FC<FullMockViewProps> = ({ activeTrack }) => {
  const bank = fullMockRaw as unknown as FullMockBank;

  const mocks: PredictorSet[] = useMemo(() => {
    return activeTrack === 'medical' ? bank.medical_mocks || [] : bank.varsity_mocks || [];
  }, [bank, activeTrack]);

  const [activeMock, setActiveMock] = useState<PredictorSet | null>(null);
  const [examTab, setExamTab] = useState<'mcq' | 'written'>('mcq');
  const [currentIdx, setCurrentIdx] = useState(0);
  const [userAnswers, setUserAnswers] = useState<Record<number, number | null>>({});
  const [revealedWritten, setRevealedWritten] = useState<Record<number, boolean>>({});
  const [timeLeft, setTimeLeft] = useState(0);
  const [isFinished, setIsFinished] = useState(false);

  useEffect(() => {
    setActiveMock(null);
  }, [activeTrack]);

  const startMock = (mock: PredictorSet) => {
    setActiveMock(mock);
    setExamTab('mcq');
    setCurrentIdx(0);
    setUserAnswers({});
    setRevealedWritten({});
    setTimeLeft((mock.duration_minutes || 60) * 60);
    setIsFinished(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const finishMock = () => {
    setIsFinished(true);
    try {
      confetti({ particleCount: 90, spread: 75, origin: { y: 0.6 } });
    } catch {
      // ignore
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  useEffect(() => {
    if (!activeMock || isFinished) return;
    if (timeLeft <= 0) {
      finishMock();
      return;
    }
    const timer = setInterval(() => setTimeLeft((p) => p - 1), 1000);
    return () => clearInterval(timer);
  }, [activeMock, isFinished, timeLeft]);

  const questions = activeMock?.questions || [];
  const writtenProblems = activeMock?.written_problems || [];

  const stats = useMemo(() => {
    let correct = 0;
    let wrong = 0;
    let skipped = 0;
    questions.forEach((q, idx) => {
      const a = userAnswers[idx];
      if (a === undefined || a === null) skipped++;
      else if (a === q.ans) correct++;
      else wrong++;
    });
    const neg = activeMock?.negative_marking ?? 0.25;
    const score = Math.max(0, correct - wrong * neg);
    return { correct, wrong, skipped, score, total: questions.length };
  }, [questions, userAnswers, activeMock]);

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // =========================================================================
  // ACTIVE FULL MOCK EXAM SIMULATOR
  // =========================================================================
  if (activeMock) {
    const currentQ = questions[currentIdx];

    return (
      <div className="max-w-5xl mx-auto px-4 sm:px-6 py-5 pb-32 space-y-5">
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm flex flex-wrap items-center justify-between gap-3 sticky top-16 z-30">
          <div className="flex items-center gap-3 min-w-0">
            <button
              onClick={() => setActiveMock(null)}
              className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 cursor-pointer"
            >
              <ArrowLeft className="w-4 h-4" />
            </button>
            <div className="min-w-0">
              <div className="text-xs font-bold text-rose-600 dark:text-rose-400">
                Tier 4: Final Model Test
              </div>
              <h2 className="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white truncate">
                {activeMock.title}
              </h2>
            </div>
          </div>

          <div className="flex items-center gap-2.5">
            {!isFinished ? (
              <>
                <div
                  className={`px-3 py-1.5 rounded-xl font-mono text-xs sm:text-sm font-black flex items-center gap-1.5 border ${
                    timeLeft < 300
                      ? 'bg-rose-500/15 text-rose-600 border-rose-500/30 animate-pulse'
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-100 border-slate-200 dark:border-slate-700'
                  }`}
                >
                  <Timer className="w-4 h-4" /> {formatTimer(timeLeft)}
                </div>
                <button
                  onClick={finishMock}
                  className="px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs sm:text-sm font-bold shadow-sm cursor-pointer"
                >
                  সাবমিট করুন
                </button>
              </>
            ) : (
              <button
                onClick={() => startMock(activeMock)}
                className="px-4 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white text-xs sm:text-sm font-bold shadow-sm cursor-pointer"
              >
                পুনরায় পরীক্ষা দিন
              </button>
            )}
          </div>
        </div>

        {isFinished && (
          <div className="bg-gradient-to-br from-rose-500/10 via-amber-500/5 to-emerald-500/10 border border-rose-500/30 rounded-3xl p-5 sm:p-6 space-y-4">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 rounded-2xl bg-rose-600 text-white flex items-center justify-center shadow-md">
                <Award className="w-6 h-6" />
              </div>
              <div>
                <h3 className="text-lg sm:text-xl font-extrabold text-slate-900 dark:text-white">
                  ফাইনাল মডেল টেস্ট স্কোরকার্ড
                </h3>
                <p className="text-xs text-slate-600 dark:text-slate-400">
                  নেগেটিভ মার্কিং: -{activeMock.negative_marking ?? 0.25} প্রতি ভুল উত্তরে
                </p>
              </div>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
              <div className="bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200 dark:border-slate-800">
                <div className="text-[11px] font-bold text-slate-500">প্রাপ্ত MCQ নম্বর</div>
                <div className="text-xl font-black text-emerald-600 dark:text-emerald-400">
                  {stats.score.toFixed(2)} / {stats.total}
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
                <div className="text-[11px] font-bold text-slate-500">স্কিপড</div>
                <div className="text-xl font-black text-slate-600 dark:text-slate-300">
                  {toBn(stats.skipped)}টি
                </div>
              </div>
            </div>
          </div>
        )}

        {/* MCQ / Written Tabs */}
        <div className="flex items-center gap-2 bg-slate-100 dark:bg-slate-900 p-1.5 rounded-2xl border border-slate-200 dark:border-slate-800 w-fit">
          <button
            onClick={() => setExamTab('mcq')}
            className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-bold cursor-pointer ${
              examTab === 'mcq'
                ? 'bg-rose-600 text-white shadow-sm'
                : 'text-slate-600 dark:text-slate-400'
            }`}
          >
            📝 MCQ অংশ ({toBn(questions.length)}টি)
          </button>
          {writtenProblems.length > 0 && (
            <button
              onClick={() => setExamTab('written')}
              className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-bold cursor-pointer ${
                examTab === 'written'
                  ? 'bg-amber-600 text-white shadow-sm'
                  : 'text-slate-600 dark:text-slate-400'
              }`}
            >
              ✍️ লিখিত অংশ ({toBn(writtenProblems.length)}টি)
            </button>
          )}
        </div>

        {/* Active MCQ Runner */}
        {examTab === 'mcq' && !isFinished && currentQ && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
            <div className="lg:col-span-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-6 shadow-sm space-y-5">
              <div className="flex items-center justify-between gap-2 flex-wrap">
                <span className="px-2.5 py-1 rounded-lg bg-rose-500/10 text-rose-700 dark:text-rose-300 text-xs font-bold">
                  প্রশ্ন {toBn(currentIdx + 1)} / {toBn(questions.length)} • {currentQ.subject}
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
                  const sel = userAnswers[currentIdx] === oIdx;
                  return (
                    <button
                      key={oIdx}
                      onClick={() =>
                        setUserAnswers((p) => ({ ...p, [currentIdx]: sel ? null : oIdx }))
                      }
                      className={`w-full p-3.5 rounded-2xl border text-left flex items-center gap-3 cursor-pointer transition-all ${
                        sel
                          ? 'bg-rose-600/10 border-rose-600 text-rose-900 dark:text-rose-100 ring-1 ring-rose-600'
                          : 'bg-slate-50/80 dark:bg-slate-800/60 border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800'
                      }`}
                    >
                      <span
                        className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-black shrink-0 ${
                          sel
                            ? 'bg-rose-600 text-white'
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
                  disabled={currentIdx === 0}
                  onClick={() => setCurrentIdx((p) => Math.max(0, p - 1))}
                  className="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold disabled:opacity-40 flex items-center gap-1 cursor-pointer"
                >
                  <ChevronLeft className="w-4 h-4" /> পূর্ববর্তী
                </button>
                <button
                  disabled={currentIdx === questions.length - 1}
                  onClick={() => setCurrentIdx((p) => Math.min(questions.length - 1, p + 1))}
                  className="px-4 py-2 rounded-xl bg-rose-600 text-white text-xs font-bold disabled:opacity-40 flex items-center gap-1 cursor-pointer"
                >
                  পরবর্তী <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>

            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-4 shadow-sm h-fit">
              <div className="text-xs font-extrabold text-slate-700 dark:text-slate-200 mb-3">
                OMR নেভিগেটর ({toBn(Object.values(userAnswers).filter((v) => v !== null && v !== undefined).length)}/{toBn(questions.length)})
              </div>
              <div className="grid grid-cols-6 sm:grid-cols-8 lg:grid-cols-6 gap-1.5">
                {questions.map((_, idx) => {
                  const answered = userAnswers[idx] !== undefined && userAnswers[idx] !== null;
                  const active = idx === currentIdx;
                  return (
                    <button
                      key={idx}
                      onClick={() => setCurrentIdx(idx)}
                      className={`h-8 rounded-lg text-xs font-bold cursor-pointer ${
                        active
                          ? 'bg-rose-600 text-white ring-2 ring-rose-400'
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

        {/* MCQ Review */}
        {examTab === 'mcq' && isFinished && (
          <div className="space-y-4">
            {questions.map((q, idx) => {
              const ua = userAnswers[idx];
              const ok = ua === q.ans;
              const skip = ua === undefined || ua === null;
              return (
                <div
                  key={q.id || idx}
                  className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 space-y-3"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="text-sm sm:text-base font-bold text-slate-900 dark:text-white">
                      <span className="text-rose-600 mr-2">#{toBn(idx + 1)}</span>
                      <MathText content={q.q} />
                    </div>
                    <span
                      className={`px-2.5 py-1 rounded-lg text-[11px] font-bold shrink-0 flex items-center gap-1 ${
                        skip
                          ? 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                          : ok
                          ? 'bg-emerald-500/15 text-emerald-700 dark:text-emerald-300'
                          : 'bg-rose-500/15 text-rose-700 dark:text-rose-300'
                      }`}
                    >
                      {skip ? (
                        <>
                          <AlertTriangle className="w-3.5 h-3.5" /> স্কিপড
                        </>
                      ) : ok ? (
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
                      const picked = oIdx === ua;
                      return (
                        <div
                          key={oIdx}
                          className={`p-2.5 rounded-xl border text-xs sm:text-sm flex items-center gap-2 ${
                            right
                              ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-900 dark:text-emerald-200 font-bold'
                              : picked
                              ? 'bg-rose-500/15 border-rose-500/40 text-rose-900 dark:text-rose-200'
                              : 'bg-slate-50 dark:bg-slate-800/50 border-slate-200 dark:border-slate-700'
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
                        <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/70">
                          <strong>💡 ব্যাখ্যা:</strong> <MathText content={q.exp} />
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

        {/* Written Problems */}
        {examTab === 'written' && (
          <div className="space-y-4">
            {writtenProblems.map((wp, idx) => {
              const rev = !!revealedWritten[idx];
              return (
                <div
                  key={idx}
                  className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 space-y-3"
                >
                  <div className="flex items-center justify-between gap-2">
                    <span className="px-2.5 py-1 rounded-lg bg-amber-500/15 text-amber-700 dark:text-amber-300 text-xs font-extrabold">
                      লিখিত {toBn(idx + 1)} • {wp.subject}
                    </span>
                    <span className="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-xs font-bold">
                      নম্বর: {wp.marks}
                    </span>
                  </div>
                  <div className="text-sm sm:text-base font-bold text-slate-900 dark:text-white">
                    <MathText content={wp.problem} />
                  </div>
                  <button
                    onClick={() => setRevealedWritten((p) => ({ ...p, [idx]: !p[idx] }))}
                    className="px-3.5 py-1.5 rounded-xl bg-amber-500/15 text-amber-800 dark:text-amber-300 text-xs font-bold flex items-center gap-1.5 cursor-pointer"
                  >
                    <BookOpen className="w-3.5 h-3.5" />
                    {rev ? 'সমাধান লুকান' : 'সমাধান ও রুব্রিক দেখুন'}
                  </button>
                  {rev && (
                    <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 space-y-2 text-xs sm:text-sm">
                      <MathText content={wp.solution} />
                      {wp.rubric && (
                        <div className="pt-2 border-t border-emerald-500/20 text-[11px] font-bold">
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
  // FULL MOCK DIRECTORY VIEW
  // =========================================================================
  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 py-5 pb-32 space-y-5">
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-7 shadow-sm space-y-4">
        <div className="flex items-center gap-2 flex-wrap">
          <span className="px-3 py-1 rounded-full text-xs font-black bg-rose-500/15 text-rose-700 dark:text-rose-300 border border-rose-500/30 flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5" />
            Tier 4: Final Model Test
          </span>
          <span className="px-3 py-1 rounded-full text-xs font-bold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
            {activeTrack === 'medical'
              ? '🩺 মেডিকেল (MAT) ১০০ মার্কস ফুল-সিলেবাস মক'
              : "🎯 ঢাবি 'ক' ইউনিট ও ইঞ্জিনিয়ারিং ফুল-সিলেবাস মক"}
          </span>
        </div>

        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white tracking-tight">
            🏆 ফাইনাল মডেল টেস্ট (Full-Syllabus Master Mock)
          </h1>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1.5 max-w-3xl">
            মূল ভর্তি পরীক্ষার পরিবেশে পূর্ণাঙ্গ সিলেবাসের মাস্টার মক টেস্ট। প্রতিটি সেটে নির্দিষ্ট টাইমার, নেগেটিভ মার্কিং এবং সম্পূর্ণ ব্যাখ্যা ও লিখিত সমাধান সংযুক্ত রয়েছে।
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {mocks.map((mock) => (
          <div
            key={mock.id}
            className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 shadow-xs hover:shadow-md hover:border-rose-500/40 transition-all flex flex-col justify-between gap-4"
          >
            <div className="space-y-2.5">
              <div className="flex items-center justify-between gap-2 flex-wrap">
                <span className="px-2.5 py-1 rounded-lg bg-rose-500/10 text-rose-700 dark:text-rose-300 text-[11px] font-extrabold">
                  {mock.badge}
                </span>
                <span className="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-[11px] font-bold">
                  ⏱️ {toBn(mock.duration_minutes)} মিনিট
                </span>
              </div>

              <h3 className="text-base sm:text-lg font-extrabold text-slate-900 dark:text-white">
                {mock.title}
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                {mock.description}
              </p>

              <div className="flex flex-wrap gap-2 pt-1">
                <span className="px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 text-[11px] font-bold">
                  📝 {toBn((mock.questions || []).length)} MCQ
                </span>
                {(mock.written_problems || []).length > 0 && (
                  <span className="px-2.5 py-1 rounded-lg bg-amber-500/10 text-amber-700 dark:text-amber-300 text-[11px] font-bold">
                    ✍️ {toBn((mock.written_problems || []).length)} Written
                  </span>
                )}
                <span className="px-2.5 py-1 rounded-lg bg-purple-500/10 text-purple-700 dark:text-purple-300 text-[11px] font-bold">
                  🎯 মোট {toBn(mock.total_marks)} নম্বর
                </span>
              </div>
            </div>

            <button
              onClick={() => startMock(mock)}
              className="w-full py-2.5 rounded-2xl bg-gradient-to-r from-rose-600 to-orange-600 hover:from-rose-700 hover:to-orange-700 text-white text-xs sm:text-sm font-extrabold shadow-sm cursor-pointer active:scale-[0.99] transition-all"
            >
              ফাইনাল মক টেস্ট শুরু করুন →
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
