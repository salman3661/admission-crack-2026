import React, { useState, useEffect, useRef } from 'react';
import { 
  Timer, 
  AlertCircle, 
  CheckCircle2, 
  XCircle, 
  MinusCircle, 
  RotateCcw, 
  Award, 
  Flame, 
  Clock, 
  ChevronRight, 
  ShieldAlert, 
  Play 
} from 'lucide-react';
import type { QuizQuestion, SubjectType, WeekFilterType } from '../types';
import { MathText } from './MathText';
import { saveExamAttempt, type ExamAttemptRecord } from '../lib/analytics';

interface ExamViewProps {
  quizzes: QuizQuestion[];
  selectedWeek: WeekFilterType;
  selectedSubject: SubjectType;
}

export const ExamView: React.FC<ExamViewProps> = ({
  quizzes,
  selectedWeek,
  selectedSubject,
}) => {
  // Filter questions
  const availableQuestions = quizzes.filter((q) => {
    const matchWeek = selectedWeek === 'all' || q.week_id === selectedWeek;
    const matchSubject = selectedSubject === 'All' || q.subject === selectedSubject;
    return matchWeek && matchSubject;
  });

  const [examStarted, setExamStarted] = useState(false);
  const [examFinished, setExamFinished] = useState(false);
  const [questionCount, setQuestionCount] = useState<number>(25);

  const [activeQuestions, setActiveQuestions] = useState<QuizQuestion[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<{ [qIndex: number]: number | null }>({});
  const [timeSpent, setTimeSpent] = useState<{ [qIndex: number]: number }>({});
  const [timeLeft, setTimeLeft] = useState(45);
  const [filterReview, setFilterReview] = useState<'all' | 'wrong'>('all');
  const hasSavedRef = useRef<boolean>(false);

  // Start exam session
  const startExam = (count: number) => {
    // Shuffle and pick `count`
    const shuffled = [...availableQuestions].sort(() => Math.random() - 0.5);
    const chosen = shuffled.slice(0, Math.min(count, shuffled.length));
    setActiveQuestions(chosen);
    setCurrentIndex(0);
    setSelectedAnswers({});
    setTimeSpent({});
    setTimeLeft(45);
    hasSavedRef.current = false;
    setExamStarted(true);
    setExamFinished(false);
  };

  // Record completed exam attempt to localStorage
  useEffect(() => {
    if (!examFinished || hasSavedRef.current || activeQuestions.length === 0) return;
    hasSavedRef.current = true;

    let correct = 0;
    let wrong = 0;
    let skipped = 0;
    const subjectCounts: { [subject: string]: { total: number; correct: number } } = {};

    activeQuestions.forEach((q, idx) => {
      const ans = selectedAnswers[idx];
      const subj = q.subject || 'General';
      if (!subjectCounts[subj]) {
        subjectCounts[subj] = { total: 0, correct: 0 };
      }
      if (ans === undefined || ans === null) {
        skipped++;
      } else if (ans === q.ans) {
        correct++;
        subjectCounts[subj].total += 1;
        subjectCounts[subj].correct += 1;
      } else {
        wrong++;
        subjectCounts[subj].total += 1;
      }
    });

    const score = correct * 1.0 - wrong * 0.25;
    const maxScore = activeQuestions.length * 1.0;
    const acc = correct + wrong > 0 ? Math.round((correct / (correct + wrong)) * 100) : 0;
    const totalSecs = Object.values(timeSpent).reduce((a, b) => a + b, 0);
    const avgSecs = activeQuestions.length > 0 ? Math.round(totalSecs / activeQuestions.length) : 0;

    const record: ExamAttemptRecord = {
      id: Date.now().toString(),
      timestamp: Date.now(),
      dateStr: new Date().toLocaleTimeString('bn-BD', { hour: '2-digit', minute: '2-digit' }),
      title: `${selectedWeek === 'all' ? 'All Weeks' : selectedWeek.toUpperCase()} • ${selectedSubject === 'All' ? 'সব বিষয়' : selectedSubject} টেস্ট`,
      totalQuestions: activeQuestions.length,
      correctCount: correct,
      wrongCount: wrong,
      skippedCount: skipped,
      totalScore: score,
      maxPossible: maxScore,
      accuracy: acc,
      avgTimePerQ: avgSecs,
      subjectCounts,
    };

    saveExamAttempt(record);
  }, [examFinished, activeQuestions, selectedAnswers, timeSpent, selectedWeek, selectedSubject]);

  // Timer countdown
  useEffect(() => {
    if (!examStarted || examFinished) return;

    if (timeLeft <= 0) {
      handleNext(null); // Auto-skip on timeout
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft((prev) => prev - 1);
      setTimeSpent((prev) => ({
        ...prev,
        [currentIndex]: (prev[currentIndex] || 0) + 1,
      }));
    }, 1000);

    return () => clearInterval(timer);
  }, [examStarted, examFinished, timeLeft, currentIndex]);

  // Keyboard shortcuts during exam
  useEffect(() => {
    if (!examStarted || examFinished) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (['1', 'a', 'A'].includes(e.key)) handleOptionSelect(0);
      else if (['2', 'b', 'B'].includes(e.key)) handleOptionSelect(1);
      else if (['3', 'c', 'C'].includes(e.key)) handleOptionSelect(2);
      else if (['4', 'd', 'D'].includes(e.key)) handleOptionSelect(3);
      else if (e.key === 'Enter') handleNext(selectedAnswers[currentIndex] ?? null);
      else if (['s', 'S'].includes(e.key)) handleNext(null);
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [examStarted, examFinished, currentIndex, selectedAnswers]);

  const handleOptionSelect = (optionIndex: number) => {
    setSelectedAnswers((prev) => ({
      ...prev,
      [currentIndex]: optionIndex,
    }));
  };

  const handleNext = (finalAnswer: number | null) => {
    setSelectedAnswers((prev) => ({
      ...prev,
      [currentIndex]: finalAnswer,
    }));

    if (currentIndex + 1 < activeQuestions.length) {
      setCurrentIndex((prev) => prev + 1);
      setTimeLeft(45);
    } else {
      setExamFinished(true);
    }
  };

  // Score Calculation
  let correctCount = 0;
  let wrongCount = 0;
  let skippedCount = 0;

  activeQuestions.forEach((q, idx) => {
    const ans = selectedAnswers[idx];
    if (ans === undefined || ans === null) {
      skippedCount++;
    } else if (ans === q.ans) {
      correctCount++;
    } else {
      wrongCount++;
    }
  });

  const totalScore = correctCount * 1.0 - wrongCount * 0.25;
  const maxPossible = activeQuestions.length * 1.0;
  const accuracy = correctCount + wrongCount > 0 ? Math.round((correctCount / (correctCount + wrongCount)) * 100) : 0;
  const totalSeconds = Object.values(timeSpent).reduce((a, b) => a + b, 0);
  const avgTimePerQ = activeQuestions.length > 0 ? Math.round(totalSeconds / activeQuestions.length) : 0;

  // Screen 1: Start Screen
  if (!examStarted) {
    const totalAvail = availableQuestions.length;
    return (
      <div className="max-w-xl mx-auto py-4 sm:py-6 px-3 text-center">
        <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-[#00B09B] via-[#056839] to-[#96C93D] p-0.5 mx-auto mb-3 shadow-md shadow-[#056839]/20">
          <div className="w-full h-full bg-white dark:bg-zinc-900 rounded-[14px] flex items-center justify-center">
            <Timer className="w-6 h-6 text-[#056839] dark:text-emerald-400" />
          </div>
        </div>
        <h2 className="text-xl sm:text-2xl font-black text-zinc-900 dark:text-white tracking-tight">
          🎯 এক্সাম ক্যাপসুল টেস্ট
        </h2>

        {/* Selected Scope Badge */}
        <div className="flex flex-wrap items-center justify-center gap-1.5 my-4">
          <span className="px-3 py-1 rounded-full bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 text-xs text-zinc-700 dark:text-zinc-300 font-semibold shadow-sm">
            সপ্তাহ: <strong className="text-[#056839] dark:text-emerald-400">{selectedWeek === 'all' ? 'All Weeks' : selectedWeek.toUpperCase()}</strong>
          </span>
          <span className="px-3 py-1 rounded-full bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 text-xs text-zinc-700 dark:text-zinc-300 font-semibold shadow-sm">
            বিষয়: <strong className="text-cyan-600 dark:text-cyan-400">{selectedSubject}</strong>
          </span>
          <span className="px-3 py-1 rounded-full bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 text-xs text-zinc-700 dark:text-zinc-300 font-semibold shadow-sm">
            উপলব্ধ: <strong className="text-amber-600 dark:text-amber-400">{totalAvail}টি</strong>
          </span>
        </div>

        {/* Question Count Selection Card */}
        <div className="bg-white dark:bg-zinc-900 p-4 sm:p-5 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 max-w-sm mx-auto mb-5 shadow-sm">
          <label className="block text-[11px] font-bold text-zinc-400 uppercase tracking-wider mb-2.5">
            প্রশ্নের সংখ্যা নির্বাচন করুন
          </label>
          <div className="grid grid-cols-4 gap-2">
            {[10, 25, 50, Math.min(100, totalAvail)].filter((v, i, a) => a.indexOf(v) === i && v <= totalAvail).map((cnt) => (
              <button
                key={cnt}
                onClick={() => setQuestionCount(cnt)}
                className={`py-2 rounded-xl text-xs sm:text-sm font-bold border transition-all ${
                  questionCount === cnt
                    ? 'bg-[#056839] text-white border-[#056839] shadow-sm scale-102'
                    : 'bg-zinc-50 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border-zinc-200 dark:border-zinc-700 hover:bg-zinc-100'
                }`}
              >
                {cnt} টি
              </button>
            ))}
          </div>
        </div>

        {/* Start Button */}
        <button
          onClick={() => startExam(questionCount)}
          disabled={totalAvail === 0}
          className="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#056839] hover:bg-[#044e2b] text-white font-bold text-sm sm:text-base shadow-lg shadow-[#056839]/25 transition-all disabled:opacity-40 active:scale-95"
        >
          <Play className="w-4 h-4 fill-current" />
          <span>ক্যাপসুল শুরু করুন ({questionCount}টি MCQ)</span>
        </button>
      </div>
    );
  }

  // Screen 2: Finished Exam Scorecard & Trap Defense
  if (examFinished) {
    const isPassing = totalScore >= maxPossible * 0.4;
    const reviewList = activeQuestions.filter((q, idx) => {
      if (filterReview === 'wrong') {
        const userAns = selectedAnswers[idx];
        return userAns === null || userAns === undefined || userAns !== q.ans;
      }
      return true;
    });

    return (
      <div className="max-w-3xl mx-auto py-6 px-3 sm:px-4">
        {/* Scorecard Hero */}
        <div className="bg-white dark:bg-zinc-900 p-5 sm:p-6 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 shadow-sm text-center relative overflow-hidden mb-6">
          <div className="flex items-center justify-center gap-2 mb-1.5">
            <Award className={`w-7 h-7 ${isPassing ? 'text-amber-500' : 'text-zinc-400'}`} />
            <h2 className="text-lg sm:text-xl font-black text-zinc-900 dark:text-white">
              {isPassing ? 'অভিনন্দন! চমৎকার পারফরম্যান্স' : 'পরীক্ষা সম্পন্ন হয়েছে'}
            </h2>
          </div>
          <p className="text-xs text-zinc-500 dark:text-zinc-400">
            ঢাবি 'ক' ইউনিট স্ট্যান্ডার্ড ফলাফল বিশ্লেষণ (+১.০ সঠিক, -০.২৫ ভুল) • গড় সময়: {avgTimePerQ}s / প্রশ্ন
          </p>

          {/* Big Score Display */}
          <div className="my-4">
            <span className="text-4xl sm:text-5xl font-black tracking-tight bg-gradient-to-r from-[#056839] via-[#00B09B] to-[#96C93D] bg-clip-text text-transparent font-['Outfit']">
              {totalScore.toFixed(2)}
            </span>
            <span className="text-base text-zinc-400 font-bold ml-1.5">/ {maxPossible.toFixed(1)}</span>
          </div>

          {/* Metric Stats Pills */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 max-w-xl mx-auto">
            <div className="p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/40 text-center">
              <span className="text-[11px] text-emerald-800 dark:text-emerald-300 font-medium">সঠিক উত্তর</span>
              <div className="text-lg font-bold text-emerald-600 dark:text-emerald-400 flex items-center justify-center gap-1 mt-0.5">
                <CheckCircle2 className="w-4 h-4" /> {correctCount}
              </div>
            </div>
            <div className="p-2.5 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800/40 text-center">
              <span className="text-[11px] text-rose-800 dark:text-rose-300 font-medium">ভুল (-০.২৫)</span>
              <div className="text-lg font-bold text-rose-600 dark:text-rose-400 flex items-center justify-center gap-1 mt-0.5">
                <XCircle className="w-4 h-4" /> {wrongCount}
              </div>
            </div>
            <div className="p-2.5 rounded-xl bg-zinc-50 dark:bg-zinc-800/60 border border-zinc-200 dark:border-zinc-700/60 text-center">
              <span className="text-[11px] text-zinc-600 dark:text-zinc-400 font-medium">স্কিপ / ফাঁকা</span>
              <div className="text-lg font-bold text-zinc-800 dark:text-zinc-200 flex items-center justify-center gap-1 mt-0.5">
                <MinusCircle className="w-4 h-4" /> {skippedCount}
              </div>
            </div>
            <div className="p-2.5 rounded-xl bg-[#056839]/10 dark:bg-[#056839]/20 border border-[#056839]/20 text-center">
              <span className="text-[11px] text-[#056839] dark:text-emerald-300 font-medium">নির্ভুলতা</span>
              <div className="text-lg font-bold text-[#056839] dark:text-emerald-400 flex items-center justify-center gap-1 mt-0.5">
                <Flame className="w-4 h-4" /> {accuracy}%
              </div>
            </div>
          </div>

          {/* Retake Button */}
          <div className="mt-6 flex justify-center gap-3">
            <button
              onClick={() => startExam(questionCount)}
              className="flex items-center gap-2 px-6 py-2.5 rounded-full bg-[#056839] hover:bg-[#044e2b] text-white font-bold text-sm shadow-md transition-all hover:scale-105 active:scale-95"
            >
              <RotateCcw className="w-4 h-4" />
              <span>পুনরায় পরীক্ষা দিন</span>
            </button>
            <button
              onClick={() => setExamStarted(false)}
              className="px-5 py-2.5 rounded-full bg-[#F6F8F6] dark:bg-[#1A261F] hover:bg-slate-200 dark:hover:bg-[#203026] text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-[#223328] text-sm font-semibold transition-all shadow-sm"
            >
              সেটিংস পরিবর্তন
            </button>
          </div>
        </div>

        {/* Trap Defense Section Header */}
        <div className="flex flex-wrap items-center justify-between pb-3 mb-4 border-b border-slate-200 dark:border-slate-800 gap-2">
          <div className="flex items-center gap-2">
            <ShieldAlert className="w-5 h-5 text-amber-500 dark:text-amber-400" />
            <h3 className="text-lg font-bold text-slate-900 dark:text-white">
              ট্র্যাপ ডিফেন্স রিভিউ (ফাঁদ বিশ্লেষণ ও সলিউশন)
            </h3>
          </div>
          <div className="flex items-center gap-1.5 bg-slate-100 dark:bg-slate-900 p-1 rounded-xl border border-slate-200 dark:border-slate-800">
            <button
              onClick={() => setFilterReview('all')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filterReview === 'all' 
                  ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-sm' 
                  : 'text-slate-600 dark:text-slate-400'
              }`}
            >
              সকল প্রশ্ন ({activeQuestions.length})
            </button>
            <button
              onClick={() => setFilterReview('wrong')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filterReview === 'wrong' 
                  ? 'bg-rose-100 dark:bg-rose-500/20 text-rose-800 dark:text-rose-300 font-bold' 
                  : 'text-slate-600 dark:text-slate-400'
              }`}
            >
              শুধু ভুল/স্কিপ ({wrongCount + skippedCount})
            </button>
          </div>
        </div>

        {/* Review Questions List */}
        <div className="space-y-4">
          {reviewList.map((q) => {
            const originalIndex = activeQuestions.indexOf(q);
            const userAns = selectedAnswers[originalIndex];
            const isCorrect = userAns === q.ans;
            const isSkipped = userAns === undefined || userAns === null;

            return (
              <div 
                key={q.id}
                className={`p-5 rounded-2xl border transition-all ${
                  isCorrect 
                    ? 'bg-white dark:bg-slate-900/60 border-emerald-200 dark:border-emerald-500/30 shadow-sm' 
                    : isSkipped 
                    ? 'bg-white dark:bg-slate-900/60 border-slate-200 dark:border-slate-800 shadow-sm' 
                    : 'bg-white dark:bg-slate-900/90 border-rose-300 dark:border-rose-500/40 shadow-sm'
                }`}
              >
                {/* Question Header */}
                <div className="flex items-start justify-between gap-3 mb-3">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                      Q{originalIndex + 1}
                    </span>
                    <span className="text-xs font-medium px-2 py-0.5 rounded bg-brand-50 dark:bg-brand-500/10 text-brand-700 dark:text-brand-300 border border-brand-200 dark:border-brand-500/20">
                      {q.subject}
                    </span>
                  </div>

                  {isCorrect ? (
                    <span className="flex items-center gap-1 text-xs font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-200 dark:border-emerald-500/20">
                      <CheckCircle2 className="w-3.5 h-3.5" /> +১.০ সঠিক
                    </span>
                  ) : isSkipped ? (
                    <span className="flex items-center gap-1 text-xs font-bold text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700">
                      <MinusCircle className="w-3.5 h-3.5" /> ০.০ স্কিপ
                    </span>
                  ) : (
                    <span className="flex items-center gap-1 text-xs font-bold text-rose-700 dark:text-rose-400 bg-rose-50 dark:bg-rose-500/10 px-2.5 py-1 rounded-lg border border-rose-200 dark:border-rose-500/20">
                      <XCircle className="w-3.5 h-3.5" /> -০.২৫ ভুল
                    </span>
                  )}
                </div>

                {/* Question Body */}
                <div className="text-base font-semibold text-slate-900 dark:text-white mb-4">
                  <MathText content={q.q} />
                </div>

                {/* Options Grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-4">
                  {q.opts.map((opt, optIdx) => {
                    const isSelected = userAns === optIdx;
                    const isRightOpt = q.ans === optIdx;

                    let optStyle = 'bg-slate-50 dark:bg-slate-800/40 border-slate-200 dark:border-slate-700/50 text-slate-800 dark:text-slate-300';
                    if (isRightOpt) {
                      optStyle = 'bg-emerald-50 dark:bg-emerald-500/15 border-emerald-300 dark:border-emerald-500/60 text-emerald-900 dark:text-emerald-200 font-semibold';
                    } else if (isSelected && !isRightOpt) {
                      optStyle = 'bg-rose-50 dark:bg-rose-500/15 border-rose-300 dark:border-rose-500/60 text-rose-900 dark:text-rose-200';
                    }

                    return (
                      <div
                        key={optIdx}
                        className={`p-3 rounded-xl border flex items-center gap-2.5 text-xs sm:text-sm ${optStyle}`}
                      >
                        <span className="w-5 h-5 rounded-md flex items-center justify-center font-bold text-xs bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 flex-shrink-0">
                          {String.fromCharCode(65 + optIdx)}
                        </span>
                        <div className="flex-1">
                          <MathText content={opt} />
                        </div>
                      </div>
                    );
                  })}
                </div>

                {/* Trap Defense Box */}
                <div className="bg-amber-50 dark:bg-amber-500/10 border border-amber-200 dark:border-amber-500/20 rounded-xl p-3 mb-2 flex items-start gap-2.5">
                  <AlertCircle className="w-4 h-4 text-amber-500 dark:text-amber-400 mt-0.5 flex-shrink-0" />
                  <div className="text-xs text-amber-900 dark:text-amber-200 leading-relaxed">
                    <strong className="text-amber-700 dark:text-amber-400 block mb-0.5 font-bold">ফাঁদ বিশ্লেষণ (Trap Insight):</strong>
                    {q.trap}
                  </div>
                </div>

                {/* Detailed Solution Box */}
                <div className="bg-slate-50 dark:bg-slate-800/50 rounded-xl p-3 text-xs text-slate-700 dark:text-slate-300 leading-relaxed border border-slate-200 dark:border-slate-700/50">
                  <strong className="text-brand-700 dark:text-brand-300 block mb-0.5">ব্যাখ্যা ও স্ট্যান্ডার্ড সমাধান:</strong>
                  <MathText content={q.exp} block />
                </div>
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  // Screen 3: Live Active Exam Question
  const currentQ = activeQuestions[currentIndex];
  const userSelected = selectedAnswers[currentIndex];
  const timerPercent = (timeLeft / 45) * 100;
  const isTimeCritical = timeLeft <= 10;

  return (
    <div className="max-w-2xl mx-auto py-4 px-3 sm:px-4">
      {/* Top Timer & Header */}
      <div className="flex items-center justify-between pb-3 mb-3 border-b border-zinc-200/80 dark:border-zinc-800">
        <div className="flex items-center gap-2">
          <span className="text-xs font-mono font-bold px-2.5 py-0.5 rounded-full bg-white dark:bg-zinc-900 text-[#056839] dark:text-emerald-400 border border-zinc-200 dark:border-zinc-800 shadow-sm">
            {currentIndex + 1} / {activeQuestions.length}
          </span>
          <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-800 shadow-sm">
            {currentQ.subject}
          </span>
        </div>

        {/* 45-Second Timer Pill */}
        <div className={`flex items-center gap-1.5 px-3 py-1 rounded-full border text-xs font-bold font-mono transition-all shadow-sm ${
          isTimeCritical 
            ? 'bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-800 text-rose-700 dark:text-rose-300 animate-pulse' 
            : 'bg-white dark:bg-zinc-900 border-zinc-200 dark:border-zinc-800 text-zinc-800 dark:text-zinc-200'
        }`}>
          <Clock className="w-3.5 h-3.5" />
          <span>{timeLeft}s</span>
        </div>
      </div>

      {/* Timer Progress Line */}
      <div className="w-full bg-zinc-200 dark:bg-zinc-800 h-1.5 rounded-full overflow-hidden mb-4">
        <div 
          className={`h-full transition-all duration-1000 ${
            isTimeCritical ? 'bg-rose-500' : 'bg-gradient-to-r from-[#00B09B] to-[#96C93D]'
          }`}
          style={{ width: `${timerPercent}%` }}
        />
      </div>

      {/* Question Card */}
      <div className="bg-white dark:bg-zinc-900 rounded-2xl p-4 sm:p-6 border border-zinc-200/80 dark:border-zinc-800 shadow-sm mb-4">
        <div className="text-sm sm:text-base font-bold text-zinc-900 dark:text-white leading-relaxed mb-4 overflow-x-auto no-scrollbar">
          <MathText content={currentQ.q} />
        </div>

        {/* Options */}
        <div className="space-y-2.5">
          {currentQ.opts.map((opt, optIdx) => {
            const isSelected = userSelected === optIdx;
            return (
              <button
                key={optIdx}
                onClick={() => handleOptionSelect(optIdx)}
                className={`w-full p-3 sm:p-3.5 rounded-xl border text-left flex items-center gap-3 transition-all text-xs sm:text-sm ${
                  isSelected
                    ? 'bg-[#056839]/10 dark:bg-[#056839]/25 border-[#056839] text-[#056839] dark:text-emerald-300 font-bold shadow-sm'
                    : 'bg-zinc-50 dark:bg-zinc-800/60 border-zinc-200 dark:border-zinc-800 text-zinc-800 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                }`}
              >
                <span className={`w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs flex-shrink-0 transition-all ${
                  isSelected 
                    ? 'bg-[#056839] text-white shadow-sm' 
                    : 'bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-700'
                }`}>
                  {String.fromCharCode(65 + optIdx)}
                </span>
                <div className="flex-1 leading-relaxed overflow-x-auto no-scrollbar">
                  <MathText content={opt} />
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* Action Footer */}
      <div className="flex items-center justify-between gap-3">
        <button
          onClick={() => handleNext(null)}
          className="px-4 py-2.5 rounded-full bg-white dark:bg-[#131E17] hover:bg-slate-100 dark:hover:bg-[#1A261F] text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 border border-slate-200/80 dark:border-[#1E2F24] text-xs sm:text-sm font-semibold shadow-sm transition-all"
        >
          স্কিপ করুন (S)
        </button>

        <span className="hidden sm:inline text-xs text-slate-500 dark:text-slate-400">
          <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-[#131E17] border border-slate-200 dark:border-[#1E2F24] text-slate-700 dark:text-slate-300">1-4</kbd> বিকল্প নির্বাচন | <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-[#131E17] border border-slate-200 dark:border-[#1E2F24] text-slate-700 dark:text-slate-300">Enter</kbd> পরবর্তী প্রশ্ন
        </span>

        <button
          onClick={() => handleNext(userSelected ?? null)}
          className="flex items-center gap-2 px-6 py-2.5 rounded-full bg-[#056839] hover:bg-[#044e2b] text-white text-xs sm:text-sm font-bold shadow-lg shadow-[#056839]/20 transition-all hover:scale-105 active:scale-95"
        >
          <span>{currentIndex + 1 === activeQuestions.length ? 'পরীক্ষা জমা দিন' : 'পরবর্তী প্রশ্ন'}</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
