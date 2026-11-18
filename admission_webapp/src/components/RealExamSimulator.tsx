import React, { useState, useEffect, useMemo } from 'react';
import {
  Clock,
  Play,
  AlertTriangle,
  CheckCircle2,
  Award,
  Save,
  ShieldAlert,
  ChevronRight,
  ChevronLeft,
} from 'lucide-react';
import { MathText } from './MathText';
import {
  type Question,
  loadMasterSet,
  loadPapersByFilter,
  getShuffledOptions,
  addErrorLogEntry,
  recordAttemptStat,
  saveMockTrackerEntry,
} from '../lib/library';
import { useSEO } from '../lib/seo';

interface RealExamSimulatorProps {
  activeTrack: 'varsity' | 'medical';
  onOpenMockTracker?: () => void;
}

type SimPhase = 'setup' | 'mcq' | 'break' | 'written' | 'result';

const DU_SUBJECTS = ['Physics', 'Chemistry', 'Higher Math', 'Biology'] as const;
const MAT_SUBJECTS = ['Biology', 'Chemistry', 'Physics', 'English', 'GK'] as const;
const OPTION_LABELS = ['ক', 'খ', 'গ', 'ঘ', 'ঙ'];

export const RealExamSimulator: React.FC<RealExamSimulatorProps> = ({ activeTrack, onOpenMockTracker }) => {
  const [examMode, setExamMode] = useState<'du_ka' | 'mat'>(activeTrack === 'medical' ? 'mat' : 'du_ka');
  const [setChoice, setSetChoice] = useState<'set_a' | 'set_b'>('set_a');
  const [phase, setPhase] = useState<SimPhase>('setup');
  const [loading, setLoading] = useState(false);

  const [mcqPool, setMcqPool] = useState<Question[]>([]);
  const [writtenPool, setWrittenPool] = useState<Question[]>([]);
  const [mcqIdx, setMcqIdx] = useState(0);
  const [mcqAnswers, setMcqAnswers] = useState<Record<string, number>>({});
  const [lowConfFlags, setLowConfFlags] = useState<Record<string, boolean>>({});
  const [writtenDrafts, setWrittenDrafts] = useState<Record<string, string>>({});
  const [writtenSelfMarks, setWrittenSelfMarks] = useState<Record<string, number>>({});

  const [mcqSecondsLeft, setMcqSecondsLeft] = useState(45 * 60);
  const [writtenSecondsLeft, setWrittenSecondsLeft] = useState(45 * 60);
  const [mcqTimeUsedMin, setMcqTimeUsedMin] = useState(0);
  const [writtenTimeUsedMin, setWrittenTimeUsedMin] = useState(0);
  const [savedToTracker, setSavedToTracker] = useState(false);
  const [blankWarning, setBlankWarning] = useState(false);

  useSEO({
    title: 'Real Exam Simulator — DU Ka & MAT | Admission Crack 2026',
    description: 'আসল পরীক্ষার টাইমার ও নেগেটিভ মার্কিং (−০.২৫) সহ DU Ka (৬০ MCQ + ৪০ লিখিত) এবং MAT (১০০ MCQ) পূর্ণাঙ্গ সিমুলেটর।',
    path: '/simulator',
  });

  useEffect(() => {
    const isRunning = phase !== 'setup';
    window.dispatchEvent(new CustomEvent('ac-exam-focus', { detail: isRunning }));
    return () => {
      window.dispatchEvent(new CustomEvent('ac-exam-focus', { detail: false }));
    };
  }, [phase]);

  useEffect(() => {
    if (phase !== 'mcq') return;
    const t = setInterval(() => {
      setMcqSecondsLeft((s) => {
        if (s <= 1) {
          clearInterval(t);
          finishMcqPhase(examMode === 'du_ka' ? 45 : 75);
          return 0;
        }
        return s - 1;
      });
    }, 1000);
    return () => clearInterval(t);
  }, [phase, examMode]);

  useEffect(() => {
    if (phase !== 'written') return;
    const t = setInterval(() => {
      setWrittenSecondsLeft((s) => {
        if (s <= 1) {
          clearInterval(t);
          finishExam(45);
          return 0;
        }
        return s - 1;
      });
    }, 1000);
    return () => clearInterval(t);
  }, [phase]);

  const startSimulator = async () => {
    setLoading(true);
    setSavedToTracker(false);
    setBlankWarning(false);
    setMcqAnswers({});
    setLowConfFlags({});
    setWrittenDrafts({});
    setWrittenSelfMarks({});
    setMcqIdx(0);

    try {
      const mcqs = await loadMasterSet(examMode, setChoice);
      setMcqPool(mcqs);

      if (examMode === 'du_ka') {
        const allDu = await loadPapersByFilter({ exam: 'du_ka' });
        const realWritten = allDu.filter((q) => q.is_written || q.options.length === 0).slice(0, 12);
        setWrittenPool(realWritten);
        setMcqSecondsLeft(45 * 60);
        setWrittenSecondsLeft(45 * 60);
      } else {
        setWrittenPool([]);
        setMcqSecondsLeft(75 * 60);
      }
      setPhase('mcq');
    } finally {
      setLoading(false);
    }
  };

  const finishMcqPhase = (forcedMin?: number) => {
    const totalMin = examMode === 'du_ka' ? 45 : 75;
    const used = forcedMin ?? Math.max(1, Math.round((totalMin * 60 - mcqSecondsLeft) / 60));
    setMcqTimeUsedMin(used);

    // Record attempts & errors
    for (const q of mcqPool) {
      const ans = mcqAnswers[q.id];
      if (ans === undefined) continue;
      const sh = getShuffledOptions(q);
      const ok = ans === sh.correctIndex;
      recordAttemptStat(q, ok, 0.25);
      if (!ok) {
        addErrorLogEntry(q, sh.order[ans] ?? ans, 'Real Exam Simulator ভুল');
      }
    }

    if (examMode === 'du_ka') {
      setPhase('break');
    } else {
      setPhase('result');
    }
  };

  const finishExam = (forcedWrittenMin?: number) => {
    if (examMode === 'du_ka' && writtenPool.length > 0 && forcedWrittenMin === undefined) {
      const blanks = writtenPool.filter((w) => !(writtenDrafts[w.id] || '').trim()).length;
      if (blanks > 0 && !blankWarning) {
        setBlankWarning(true);
        return;
      }
    }
    const used = forcedWrittenMin ?? Math.max(1, Math.round((45 * 60 - writtenSecondsLeft) / 60));
    setWrittenTimeUsedMin(used);
    setPhase('result');
  };

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  };

  const currentMcq = mcqPool[mcqIdx];
  const currentShuffled = useMemo(() => {
    if (!currentMcq) return { options: [], correctIndex: null, order: [] };
    return getShuffledOptions(currentMcq);
  }, [currentMcq]);

  // Compute scorecard
  const scorecard = useMemo(() => {
    const subjects = examMode === 'du_ka' ? [...DU_SUBJECTS] : [...MAT_SUBJECTS];
    const perSubj: Record<string, { correct: number; wrong: number; skipped: number; mcqNet: number; written: number }> = {};
    for (const s of subjects) {
      perSubj[s] = { correct: 0, wrong: 0, skipped: 0, mcqNet: 0, written: 0 };
    }
    const chapLoss: Record<string, { name: string; loss: number }> = {};

    for (const q of mcqPool) {
      const s = perSubj[q.subject] || (perSubj[q.subject] = { correct: 0, wrong: 0, skipped: 0, mcqNet: 0, written: 0 });
      const ans = mcqAnswers[q.id];
      if (ans === undefined) {
        s.skipped++;
        chapLoss[q.chapter_id] = {
          name: q.chapter_name,
          loss: (chapLoss[q.chapter_id]?.loss || 0) + 1,
        };
        continue;
      }
      const sh = getShuffledOptions(q);
      if (ans === sh.correctIndex) {
        s.correct++;
        s.mcqNet += 1;
      } else {
        s.wrong++;
        s.mcqNet = +(s.mcqNet - 0.25).toFixed(2);
        chapLoss[q.chapter_id] = {
          name: q.chapter_name,
          loss: +( (chapLoss[q.chapter_id]?.loss || 0) + 1.25 ).toFixed(2),
        };
      }
    }

    let writtenTotal = 0;
    for (const w of writtenPool) {
      const m = Number(writtenSelfMarks[w.id] || 0);
      writtenTotal += m;
      if (perSubj[w.subject]) perSubj[w.subject].written += m;
    }

    const totalCorrect = Object.values(perSubj).reduce((a, b) => a + b.correct, 0);
    const totalWrong = Object.values(perSubj).reduce((a, b) => a + b.wrong, 0);
    const totalMcqNet = +Object.values(perSubj).reduce((a, b) => a + b.mcqNet, 0).toFixed(2);
    const attempted = totalCorrect + totalWrong;
    const accuracy = attempted ? Math.round((totalCorrect / attempted) * 100) : 0;
    const grandTotal = +(totalMcqNet + writtenTotal).toFixed(2);
    const top3Lossy = Object.values(chapLoss)
      .sort((a, b) => b.loss - a.loss)
      .slice(0, 3)
      .map((c) => `${c.name} (-${c.loss})`);
    const writtenBlankCount = writtenPool.filter((w) => !(writtenDrafts[w.id] || '').trim()).length;

    return { perSubj, totalCorrect, totalWrong, totalMcqNet, writtenTotal, grandTotal, accuracy, top3Lossy, writtenBlankCount };
  }, [examMode, mcqPool, mcqAnswers, writtenPool, writtenSelfMarks, writtenDrafts]);

  const handleSaveToTracker = () => {
    const p = scorecard.perSubj;
    saveMockTrackerEntry({
      id: `sim_${Date.now()}`,
      date: new Date().toISOString().slice(0, 10),
      name: `${examMode === 'du_ka' ? 'DU Ka' : 'MAT'} Simulator (${setChoice.toUpperCase()})`,
      exam: examMode,
      Physics_MCQ: p.Physics?.mcqNet || 0,
      Physics_Written: p.Physics?.written || 0,
      Chem_MCQ: p.Chemistry?.mcqNet || 0,
      Chem_Written: p.Chemistry?.written || 0,
      Math_MCQ: p['Higher Math']?.mcqNet || 0,
      Math_Written: p['Higher Math']?.written || 0,
      Bio_MCQ: p.Biology?.mcqNet || 0,
      Bio_Written: p.Biology?.written || 0,
      MCQ_total: scorecard.totalMcqNet,
      Written_total: scorecard.writtenTotal,
      GRAND_TOTAL: scorecard.grandTotal,
      accuracy_pct: scorecard.accuracy,
      time_MCQ_used: mcqTimeUsedMin,
      time_written_used: writtenTimeUsedMin,
      written_blank_count: scorecard.writtenBlankCount,
      top3_lossy_chapter: scorecard.top3Lossy.join(' | '),
      next48h_fix: 'Top-3 লসি চ্যাপ্টার ড্রিল',
    });
    setSavedToTracker(true);
  };

  if (phase === 'setup') {
    return (
      <div className="max-w-3xl mx-auto px-4 py-8">
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 shadow-sm">
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white mb-2">
            🎯 Real Exam Simulator
          </h1>
          <p className="text-sm text-slate-600 dark:text-slate-400 mb-6">
            আসল পরীক্ষার কাঠামো, টাইমার ও নেগেটিভ মার্কিং (−০.২৫) সহ পূর্ণাঙ্গ পরীক্ষা। ভুল উত্তর সরাসরি Mistake Book-এ যুক্ত হবে।
          </p>

          <div className="grid sm:grid-cols-2 gap-3 mb-5">
            <button
              onClick={() => setExamMode('du_ka')}
              className={`p-4 rounded-2xl border text-left transition-all cursor-pointer ${
                examMode === 'du_ka'
                  ? 'border-emerald-500 bg-emerald-50/70 dark:bg-emerald-950/30 ring-1 ring-emerald-500'
                  : 'border-slate-200 dark:border-slate-800'
              }`}
            >
              <div className="font-extrabold text-slate-900 dark:text-white">DU 'Ka' (Science Unit)</div>
              <div className="text-xs text-slate-500 mt-1">৬০ MCQ (৪৫ মিনিট) + ৪০ লিখিত (৪৫ মিনিট) • ১২ ডিসে</div>
            </button>

            <button
              onClick={() => setExamMode('mat')}
              className={`p-4 rounded-2xl border text-left transition-all cursor-pointer ${
                examMode === 'mat'
                  ? 'border-rose-500 bg-rose-50/70 dark:bg-rose-950/30 ring-1 ring-rose-500'
                  : 'border-slate-200 dark:border-slate-800'
              }`}
            >
              <div className="font-extrabold text-slate-900 dark:text-white">MAT (MBBS)</div>
              <div className="text-xs text-slate-500 mt-1">১০০ MCQ (৭৫ মিনিট) • Bio ৩০, Chem ২৫, Phys ২০, Eng ১৫, GK ১০</div>
            </button>
          </div>

          <div className="mb-6">
            <label className="block text-xs font-bold text-slate-600 dark:text-slate-400 mb-2">প্রশ্ন সেট বেছে নাও</label>
            <div className="flex gap-2">
              {(['set_a', 'set_b'] as const).map((s) => (
                <button
                  key={s}
                  onClick={() => setSetChoice(s)}
                  className={`px-4 py-2 rounded-xl text-xs font-bold border cursor-pointer ${
                    setChoice === s
                      ? 'bg-slate-900 dark:bg-white text-white dark:text-slate-900 border-transparent'
                      : 'border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300'
                  }`}
                >
                  {s === 'set_a' ? 'Master SET-A (সবচেয়ে সম্ভাব্য)' : 'Master SET-B (দ্বিতীয় স্তর)'}
                </button>
              ))}
            </div>
          </div>

          <div className="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/40 text-xs text-amber-900 dark:text-amber-200 mb-6 space-y-1">
            <div className="font-bold">⚡ Exam-Hall Rules (EV = 1.25P − 0.25):</div>
            <div>১. ২০% এর বেশি নিশ্চিত হলে তবেই MCQ দাগো; নইলে ফাঁকা রাখো।</div>
            <div>২. কোনো ক্যালকুলেটর বা ফোন নয়।</div>
            <div>৩. লিখিত অংশ কখনো খালি রাখবে না — আংশিক নম্বর আছে।</div>
          </div>

          <button
            onClick={startSimulator}
            disabled={loading}
            className="w-full py-3.5 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50"
          >
            <Play className="w-4 h-4" />
            {loading ? 'প্রশ্ন লোড হচ্ছে...' : 'পরীক্ষা শুরু করো'}
          </button>
        </div>
      </div>
    );
  }

  if (phase === 'mcq' && currentMcq) {
    const selected = mcqAnswers[currentMcq.id];
    return (
      <div className="max-w-3xl mx-auto px-4 py-6">
        <div className="flex items-center justify-between gap-3 mb-4 bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200 dark:border-slate-800 sticky top-16 z-20 shadow-xs">
          <div className="text-xs font-extrabold text-slate-700 dark:text-slate-200">
            MCQ ধাপ • প্রশ্ন {mcqIdx + 1}/{mcqPool.length} ({currentMcq.subject})
          </div>
          <div className="flex items-center gap-2">
            <span className={`flex items-center gap-1 px-2.5 py-1 rounded-xl text-xs font-black ${mcqSecondsLeft < 300 ? 'bg-rose-100 text-rose-700' : 'bg-slate-100 dark:bg-slate-800'}`}>
              <Clock className="w-3.5 h-3.5" /> {formatTimer(mcqSecondsLeft)}
            </span>
            <button
              onClick={() => finishMcqPhase()}
              className="px-3 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold cursor-pointer"
            >
              MCQ জমা দাও
            </button>
          </div>
        </div>

        {/* F12 Attempt Strategy Helper */}
        <div className="mb-4 p-3 rounded-2xl bg-blue-50/70 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800/40 flex items-center justify-between gap-2 text-xs">
          <span className="text-blue-800 dark:text-blue-200 font-medium">
            💡 <strong>EV = 1.25P − 0.25:</strong> ২০%+ নিশ্চিত না হলে দাগবে না।
          </span>
          <button
            onClick={() => setLowConfFlags((p) => ({ ...p, [currentMcq.id]: !p[currentMcq.id] }))}
            className={`px-2.5 py-1 rounded-lg font-bold shrink-0 cursor-pointer ${
              lowConfFlags[currentMcq.id]
                ? 'bg-amber-500 text-white'
                : 'bg-white dark:bg-slate-800 border border-blue-200 dark:border-slate-700 text-blue-700 dark:text-blue-300'
            }`}
          >
            {lowConfFlags[currentMcq.id] ? '⚠ <20% চিহ্নিত' : '<20% নিশ্চিত মার্ক'}
          </button>
        </div>

        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-7">
          <div className="text-xs text-slate-500 mb-3">
            📌 {currentMcq.chapter_name} · {currentMcq.source_name}
          </div>
          <div className="text-base sm:text-lg font-semibold mb-5">
            <MathText content={currentMcq.question} block />
          </div>

          <div className="space-y-2.5">
            {currentShuffled.options.map((opt, i) => (
              <button
                key={i}
                onClick={() => setMcqAnswers((p) => ({ ...p, [currentMcq.id]: i }))}
                className={`w-full text-left p-3.5 rounded-2xl border flex items-start gap-3 cursor-pointer transition-all ${
                  selected === i
                    ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 ring-1 ring-emerald-500'
                    : 'border-slate-200 dark:border-slate-700 hover:border-emerald-400'
                }`}
              >
                <span className="w-7 h-7 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-center text-xs font-extrabold shrink-0">
                  {OPTION_LABELS[i] || i + 1}
                </span>
                <div className="flex-1 text-sm pt-0.5">
                  <MathText content={opt} />
                </div>
              </button>
            ))}
          </div>

          <div className="mt-6 flex items-center justify-between">
            <button
              onClick={() => setMcqIdx((i) => Math.max(0, i - 1))}
              disabled={mcqIdx === 0}
              className="flex items-center gap-1 px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold disabled:opacity-40 cursor-pointer"
            >
              <ChevronLeft className="w-4 h-4" /> আগেরটি
            </button>
            <button
              onClick={() => {
                setMcqAnswers((p) => {
                  const n = { ...p };
                  delete n[currentMcq.id];
                  return n;
                });
              }}
              className="text-xs text-slate-500 hover:text-rose-600 font-semibold cursor-pointer"
            >
              উত্তর মুছো (Skip)
            </button>
            <button
              onClick={() => setMcqIdx((i) => Math.min(mcqPool.length - 1, i + 1))}
              disabled={mcqIdx === mcqPool.length - 1}
              className="flex items-center gap-1 px-4 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold disabled:opacity-40 cursor-pointer"
            >
              পরেরটি <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (phase === 'break') {
    return (
      <div className="max-w-xl mx-auto px-4 py-12 text-center">
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-8">
          <CheckCircle2 className="w-12 h-12 text-emerald-500 mx-auto mb-3" />
          <h2 className="text-xl font-extrabold mb-2">MCQ ধাপ শেষ!</h2>
          <p className="text-sm text-slate-600 dark:text-slate-400 mb-6">
            তুমি {mcqTimeUsedMin} মিনিটে MCQ শেষ করেছো। এবার ৪৫ মিনিটের লিখিত (৪০ নম্বর) পরীক্ষা। মনে রেখো: লিখিত প্রশ্নে নেগেটিভ মার্কিং নেই, আংশিক নম্বর আছে।
          </p>
          <button
            onClick={() => setPhase('written')}
            className="px-6 py-3 rounded-2xl bg-emerald-600 text-white font-bold text-sm cursor-pointer"
          >
            লিখিত পরীক্ষা শুরু করো (৪৫ মিনিট)
          </button>
        </div>
      </div>
    );
  }

  if (phase === 'written') {
    return (
      <div className="max-w-3xl mx-auto px-4 py-6">
        <div className="flex items-center justify-between gap-3 mb-4 bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200 dark:border-slate-800 sticky top-16 z-20">
          <div className="text-xs font-extrabold">✍️ লিখিত ধাপ ({writtenPool.length} প্রশ্ন)</div>
          <div className="flex items-center gap-2">
            <span className="flex items-center gap-1 px-2.5 py-1 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-black">
              <Clock className="w-3.5 h-3.5" /> {formatTimer(writtenSecondsLeft)}
            </span>
            <button
              onClick={() => finishExam()}
              className="px-3 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold cursor-pointer"
            >
              চূড়ান্ত জমা দাও
            </button>
          </div>
        </div>

        {blankWarning && (
          <div className="mb-4 p-4 rounded-2xl bg-rose-50 dark:bg-rose-950/40 border border-rose-300 text-xs text-rose-800 dark:text-rose-200 flex items-center justify-between gap-3">
            <div className="flex items-center gap-2">
              <ShieldAlert className="w-5 h-5 shrink-0" />
              <span>তুমি কিছু লিখিত প্রশ্ন খালি রেখেছো! আংশিক নম্বর পেতে অন্তত মূল সূত্রটি লেখো, অথবা আবার জমা দাও।</span>
            </div>
            <button
              onClick={() => finishExam(Math.max(1, Math.round((45 * 60 - writtenSecondsLeft) / 60)))}
              className="px-3 py-1.5 rounded-xl bg-rose-600 text-white font-bold shrink-0 cursor-pointer"
            >
              তবুও জমা দাও
            </button>
          </div>
        )}

        <div className="space-y-4">
          {writtenPool.map((w, i) => (
            <div key={w.id} className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5">
              <div className="flex items-center justify-between text-xs text-slate-500 mb-2">
                <span>প্রশ্ন #{i + 1} · {w.subject} · {w.chapter_name}</span>
                <span className="font-bold text-purple-600">{w.marks} নম্বর</span>
              </div>
              <div className="text-sm font-semibold mb-3">
                <MathText content={w.question} block />
              </div>
              <textarea
                rows={3}
                value={writtenDrafts[w.id] || ''}
                onChange={(e) => setWrittenDrafts((p) => ({ ...p, [w.id]: e.target.value }))}
                placeholder="সূত্র → কাজ → উত্তর (সিলেবাস স্টাইলে লিখো)..."
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 p-3 text-sm mb-3"
              />
              <div className="flex items-center justify-between gap-2 text-xs">
                <span className="text-slate-500">স্ব-মূল্যায়ন (আংশিক নম্বর):</span>
                <input
                  type="number"
                  min={0}
                  max={w.marks}
                  step={0.5}
                  value={writtenSelfMarks[w.id] ?? ''}
                  onChange={(e) => setWrittenSelfMarks((p) => ({ ...p, [w.id]: Number(e.target.value) }))}
                  placeholder={`0 - ${w.marks}`}
                  className="w-24 px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-right font-bold"
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  // RESULT SCORECARD
  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 shadow-sm">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <div className="w-11 h-11 rounded-2xl bg-emerald-100 dark:bg-emerald-950/50 flex items-center justify-center text-emerald-600">
              <Award className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-extrabold">স্কোরকার্ড — {examMode === 'du_ka' ? 'DU Ka' : 'MAT'}</h2>
              <p className="text-xs text-slate-500">MCQ সময়: {mcqTimeUsedMin} মি · Accuracy: {scorecard.accuracy}%</p>
            </div>
          </div>
          <div className="text-right">
            <div className="text-3xl font-black text-emerald-600">{scorecard.grandTotal}</div>
            <div className="text-xs text-slate-500">মোট ১০০ এর মধ্যে</div>
          </div>
        </div>

        <div className="overflow-x-auto mb-6">
          <table className="w-full text-xs text-left border-collapse">
            <thead>
              <tr className="border-b border-slate-200 dark:border-slate-800 text-slate-500">
                <th className="py-2">বিষয়</th>
                <th className="py-2">সঠিক</th>
                <th className="py-2">ভুল</th>
                <th className="py-2">MCQ নেট</th>
                {examMode === 'du_ka' && <th className="py-2">লিখিত</th>}
              </tr>
            </thead>
            <tbody>
              {Object.entries(scorecard.perSubj).map(([subj, d]) => (
                <tr key={subj} className="border-b border-slate-100 dark:border-slate-800/60">
                  <td className="py-2.5 font-bold">{subj}</td>
                  <td className="py-2.5 text-emerald-600 font-bold">{d.correct}</td>
                  <td className="py-2.5 text-rose-600 font-bold">{d.wrong}</td>
                  <td className="py-2.5 font-bold">{d.mcqNet}</td>
                  {examMode === 'du_ka' && <td className="py-2.5 font-bold">{d.written}</td>}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {scorecard.top3Lossy.length > 0 && (
          <div className="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/40 text-xs mb-6">
            <div className="font-bold text-amber-800 dark:text-amber-300 mb-1 flex items-center gap-1.5">
              <AlertTriangle className="w-4 h-4" /> Top-3 সবচেয়ে বেশি নম্বর হারানো Chapter:
            </div>
            <div>{scorecard.top3Lossy.join(' • ')}</div>
          </div>
        )}

        <div className="flex flex-wrap gap-3">
          <button
            onClick={handleSaveToTracker}
            disabled={savedToTracker}
            className="flex-1 py-3 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center justify-center gap-2 cursor-pointer disabled:opacity-60"
          >
            <Save className="w-4 h-4" />
            {savedToTracker ? 'Mock Tracker-এ সেভ হয়েছে ✓' : 'Mock Tracker-এ সেভ করো'}
          </button>
          {onOpenMockTracker && (
            <button
              onClick={onOpenMockTracker}
              className="py-3 px-4 rounded-2xl bg-slate-100 dark:bg-slate-800 text-xs font-bold cursor-pointer"
            >
              Mock Tracker দেখো
            </button>
          )}
          <button
            onClick={() => setPhase('setup')}
            className="py-3 px-4 rounded-2xl border border-slate-200 dark:border-slate-700 text-xs font-bold cursor-pointer"
          >
            আবার দাও
          </button>
        </div>
      </div>
    </div>
  );
};
