import React, { useState, useEffect } from 'react';
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
    setExamStarted(true);
    setExamFinished(false);
  };

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
      <div className="max-w-2xl mx-auto py-12 px-4 text-center">
        <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-brand-600 to-indigo-600 p-0.5 mx-auto mb-4 shadow-xl shadow-brand-500/20">
          <div className="w-full h-full bg-slate-950 rounded-[14px] flex items-center justify-center">
            <Timer className="w-8 h-8 text-brand-400" />
          </div>
        </div>
        <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
          ঢাবি 'ক' ইউনিট রিয়েল এক্সাম মোড
        </h2>
        <p className="text-sm text-slate-400 mt-2 max-w-lg mx-auto">
          ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিটের স্ট্যান্ডার্ড নেগেটিভ মার্কিং (+১.০ সঠিক, -০.২৫ ভুল) এবং প্রতিটি প্রশ্নে ৪৫ সেকেন্ড সময়সীমা সহ বাস্তব পরীক্ষার অনুভূতি।
        </p>

        {/* Selected Scope Badge */}
        <div className="flex flex-wrap items-center justify-center gap-2 my-6">
          <span className="px-3 py-1 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300 font-semibold">
            সপ্তাহ: <strong className="text-brand-400">{selectedWeek === 'all' ? 'All Weeks' : selectedWeek.toUpperCase()}</strong>
          </span>
          <span className="px-3 py-1 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300 font-semibold">
            বিষয়: <strong className="text-cyan-400">{selectedSubject}</strong>
          </span>
          <span className="px-3 py-1 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300 font-semibold">
            উপলব্ধ প্রশ্ন: <strong className="text-amber-400">{totalAvail}টি</strong>
          </span>
        </div>

        {/* Question Count Selection */}
        <div className="bg-slate-900/80 p-6 rounded-2xl border border-slate-800 max-w-md mx-auto mb-8 shadow-xl">
          <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider mb-3">
            প্রশ্নের সংখ্যা নির্বাচন করুন
          </label>
          <div className="grid grid-cols-3 gap-2.5">
            {[10, 25, Math.min(50, totalAvail)].filter((v, i, a) => a.indexOf(v) === i && v <= totalAvail).map((cnt) => (
              <button
                key={cnt}
                onClick={() => setQuestionCount(cnt)}
                className={`py-2.5 rounded-xl text-sm font-bold border transition-all ${
                  questionCount === cnt
                    ? 'bg-brand-600 text-white border-brand-400 shadow-md shadow-brand-500/25'
                    : 'bg-slate-800/80 text-slate-300 border-slate-700/60 hover:bg-slate-800'
                }`}
              >
                {cnt} টি MCQ
              </button>
            ))}
          </div>
        </div>

        {/* Start Button */}
        <button
          onClick={() => startExam(questionCount)}
          disabled={totalAvail === 0}
          className="inline-flex items-center gap-2.5 px-8 py-3.5 rounded-2xl bg-gradient-to-r from-brand-600 via-indigo-600 to-cyan-500 hover:opacity-95 text-white font-bold text-base shadow-xl shadow-brand-500/25 transition-all disabled:opacity-40"
        >
          <Play className="w-5 h-5 fill-current" />
          <span>পরীক্ষা শুরু করুন ({questionCount}টি MCQ)</span>
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
      <div className="max-w-4xl mx-auto py-8 px-4">
        {/* Scorecard Hero */}
        <div className="bg-gradient-to-b from-slate-900 via-slate-900/95 to-slate-950 p-6 sm:p-8 rounded-3xl border border-slate-800 shadow-2xl text-center relative overflow-hidden mb-8">
          <div className="flex items-center justify-center gap-2 mb-2">
            <Award className={`w-8 h-8 ${isPassing ? 'text-amber-400' : 'text-slate-500'}`} />
            <h2 className="text-xl sm:text-2xl font-black text-white">
              {isPassing ? 'অভিনন্দন! চমৎকার পারফরম্যান্স' : 'পরীক্ষা সম্পন্ন হয়েছে'}
            </h2>
          </div>
          <p className="text-xs text-slate-400">
            ঢাবি 'ক' ইউনিট স্ট্যান্ডার্ড ফলাফল বিশ্লেষণ (+১.০ সঠিক, -০.২৫ ভুল) • গড় সময়: {avgTimePerQ}s / প্রশ্ন
          </p>

          {/* Big Score Display */}
          <div className="my-6">
            <span className="text-5xl sm:text-6xl font-black tracking-tight bg-gradient-to-r from-brand-400 via-cyan-300 to-emerald-400 bg-clip-text text-transparent font-['Outfit']">
              {totalScore.toFixed(2)}
            </span>
            <span className="text-lg text-slate-500 font-bold ml-2">/ {maxPossible.toFixed(1)}</span>
          </div>

          {/* Metric Stats Pills */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-2xl mx-auto">
            <div className="p-3 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 text-center">
              <span className="text-xs text-emerald-300 font-medium">সঠিক উত্তর</span>
              <div className="text-xl font-bold text-emerald-400 flex items-center justify-center gap-1 mt-0.5">
                <CheckCircle2 className="w-4 h-4" /> {correctCount}
              </div>
            </div>
            <div className="p-3 rounded-2xl bg-rose-500/10 border border-rose-500/20 text-center">
              <span className="text-xs text-rose-300 font-medium">ভুল উত্তর (-০.২৫)</span>
              <div className="text-xl font-bold text-rose-400 flex items-center justify-center gap-1 mt-0.5">
                <XCircle className="w-4 h-4" /> {wrongCount}
              </div>
            </div>
            <div className="p-3 rounded-2xl bg-slate-800/80 border border-slate-700/60 text-center">
              <span className="text-xs text-slate-400 font-medium">স্কিপ / ফাঁকা</span>
              <div className="text-xl font-bold text-slate-300 flex items-center justify-center gap-1 mt-0.5">
                <MinusCircle className="w-4 h-4" /> {skippedCount}
              </div>
            </div>
            <div className="p-3 rounded-2xl bg-brand-500/10 border border-brand-500/20 text-center">
              <span className="text-xs text-brand-300 font-medium">নির্ভুলতা (Accuracy)</span>
              <div className="text-xl font-bold text-brand-400 flex items-center justify-center gap-1 mt-0.5">
                <Flame className="w-4 h-4" /> {accuracy}%
              </div>
            </div>
          </div>

          {/* Retake Button */}
          <div className="mt-6 flex justify-center gap-3">
            <button
              onClick={() => startExam(questionCount)}
              className="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-500 text-white font-bold text-sm shadow-md transition-all"
            >
              <RotateCcw className="w-4 h-4" />
              <span>পুনরায় পরীক্ষা দিন</span>
            </button>
            <button
              onClick={() => setExamStarted(false)}
              className="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-semibold transition-all"
            >
              সেটিংস পরিবর্তন
            </button>
          </div>
        </div>

        {/* Trap Defense Section Header */}
        <div className="flex flex-wrap items-center justify-between pb-3 mb-4 border-b border-slate-800 gap-2">
          <div className="flex items-center gap-2">
            <ShieldAlert className="w-5 h-5 text-amber-400" />
            <h3 className="text-lg font-bold text-white">
              ট্র্যাপ ডিফেন্স রিভিউ (ফাঁদ বিশ্লেষণ ও সলিউশন)
            </h3>
          </div>
          <div className="flex items-center gap-1.5 bg-slate-900 p-1 rounded-xl border border-slate-800">
            <button
              onClick={() => setFilterReview('all')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filterReview === 'all' ? 'bg-slate-800 text-white' : 'text-slate-400'
              }`}
            >
              সকল প্রশ্ন ({activeQuestions.length})
            </button>
            <button
              onClick={() => setFilterReview('wrong')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filterReview === 'wrong' ? 'bg-rose-500/20 text-rose-300' : 'text-slate-400'
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
                    ? 'bg-slate-900/60 border-emerald-500/30' 
                    : isSkipped 
                    ? 'bg-slate-900/60 border-slate-800' 
                    : 'bg-slate-900/90 border-rose-500/40'
                }`}
              >
                {/* Question Header */}
                <div className="flex items-start justify-between gap-3 mb-3">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-800 text-slate-300">
                      Q{originalIndex + 1}
                    </span>
                    <span className="text-xs font-medium px-2 py-0.5 rounded bg-brand-500/10 text-brand-300 border border-brand-500/20">
                      {q.subject}
                    </span>
                  </div>

                  {isCorrect ? (
                    <span className="flex items-center gap-1 text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-500/20">
                      <CheckCircle2 className="w-3.5 h-3.5" /> +১.০ সঠিক
                    </span>
                  ) : isSkipped ? (
                    <span className="flex items-center gap-1 text-xs font-bold text-slate-400 bg-slate-800 px-2.5 py-1 rounded-lg">
                      <MinusCircle className="w-3.5 h-3.5" /> ০.০ স্কিপ
                    </span>
                  ) : (
                    <span className="flex items-center gap-1 text-xs font-bold text-rose-400 bg-rose-500/10 px-2.5 py-1 rounded-lg border border-rose-500/20">
                      <XCircle className="w-3.5 h-3.5" /> -০.২৫ ভুল
                    </span>
                  )}
                </div>

                {/* Question Body */}
                <div className="text-base font-semibold text-white mb-4">
                  <MathText content={q.q} />
                </div>

                {/* Options Grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-4">
                  {q.opts.map((opt, optIdx) => {
                    const isSelected = userAns === optIdx;
                    const isRightOpt = q.ans === optIdx;

                    let optStyle = 'bg-slate-800/40 border-slate-700/50 text-slate-300';
                    if (isRightOpt) {
                      optStyle = 'bg-emerald-500/15 border-emerald-500/60 text-emerald-200 font-semibold';
                    } else if (isSelected && !isRightOpt) {
                      optStyle = 'bg-rose-500/15 border-rose-500/60 text-rose-200';
                    }

                    return (
                      <div
                        key={optIdx}
                        className={`p-3 rounded-xl border flex items-center gap-2.5 text-xs sm:text-sm ${optStyle}`}
                      >
                        <span className="w-5 h-5 rounded-md flex items-center justify-center font-bold text-xs bg-slate-900 border border-slate-700 flex-shrink-0">
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
                <div className="bg-amber-500/10 border border-amber-500/20 rounded-xl p-3 mb-2 flex items-start gap-2.5">
                  <AlertCircle className="w-4 h-4 text-amber-400 mt-0.5 flex-shrink-0" />
                  <div className="text-xs text-amber-200 leading-relaxed">
                    <strong className="text-amber-400 block mb-0.5">ফাঁদ বিশ্লেষণ (Trap Insight):</strong>
                    {q.trap}
                  </div>
                </div>

                {/* Detailed Solution Box */}
                <div className="bg-slate-800/50 rounded-xl p-3 text-xs text-slate-300 leading-relaxed border border-slate-700/50">
                  <strong className="text-brand-300 block mb-0.5">ব্যাখ্যা ও স্ট্যান্ডার্ড সমাধান:</strong>
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
    <div className="max-w-3xl mx-auto py-6 px-4">
      {/* Top Timer & Header */}
      <div className="flex items-center justify-between pb-3 mb-4 border-b border-slate-800">
        <div className="flex items-center gap-2.5">
          <span className="text-xs font-mono font-bold px-3 py-1 rounded-xl bg-slate-900 text-brand-400 border border-slate-800">
            প্রশ্ন: {currentIndex + 1} / {activeQuestions.length}
          </span>
          <span className="text-xs font-semibold px-2.5 py-1 rounded-xl bg-slate-900 text-slate-300 border border-slate-800">
            {currentQ.subject}
          </span>
        </div>

        {/* 45-Second Timer Pill */}
        <div className={`flex items-center gap-2 px-3.5 py-1 rounded-xl border text-sm font-bold font-mono transition-all ${
          isTimeCritical 
            ? 'bg-rose-500/20 border-rose-500/50 text-rose-300 animate-pulse' 
            : 'bg-slate-900 border-slate-800 text-cyan-300'
        }`}>
          <Clock className="w-4 h-4" />
          <span>{timeLeft}s</span>
        </div>
      </div>

      {/* Timer Progress Line */}
      <div className="w-full bg-slate-900 h-1.5 rounded-full overflow-hidden mb-6">
        <div 
          className={`h-full transition-all duration-1000 ${
            isTimeCritical ? 'bg-rose-500' : 'bg-gradient-to-r from-brand-500 to-cyan-400'
          }`}
          style={{ width: `${timerPercent}%` }}
        />
      </div>

      {/* Question Card */}
      <div className="bg-slate-900/90 rounded-3xl p-6 sm:p-8 border border-slate-800 shadow-xl mb-6">
        <div className="text-lg sm:text-xl font-bold text-white leading-relaxed mb-6">
          <MathText content={currentQ.q} />
        </div>

        {/* Options (Keyboard 1, 2, 3, 4 / A, B, C, D) */}
        <div className="space-y-3">
          {currentQ.opts.map((opt, optIdx) => {
            const isSelected = userSelected === optIdx;
            return (
              <button
                key={optIdx}
                onClick={() => handleOptionSelect(optIdx)}
                className={`w-full p-4 rounded-2xl border text-left flex items-center gap-3.5 transition-all text-sm sm:text-base ${
                  isSelected
                    ? 'bg-brand-600/20 border-brand-500 text-white shadow-md shadow-brand-500/10'
                    : 'bg-slate-800/40 border-slate-700/50 text-slate-300 hover:bg-slate-800/80 hover:border-slate-600'
                }`}
              >
                <span className={`w-7 h-7 rounded-lg flex items-center justify-center font-bold text-xs flex-shrink-0 transition-all ${
                  isSelected 
                    ? 'bg-brand-500 text-white' 
                    : 'bg-slate-900 text-slate-400 border border-slate-700'
                }`}>
                  {String.fromCharCode(65 + optIdx)}
                </span>
                <div className="flex-1 leading-relaxed">
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
          className="px-4 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-slate-200 border border-slate-800 text-xs sm:text-sm font-semibold transition-all"
        >
          স্কিপ করুন (S)
        </button>

        <span className="hidden sm:inline text-xs text-slate-400">
          <kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">1-4</kbd> বিকল্প নির্বাচন | <kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">Enter</kbd> পরবর্তী প্রশ্ন
        </span>

        <button
          onClick={() => handleNext(userSelected ?? null)}
          className="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-500 text-white text-xs sm:text-sm font-bold shadow-lg shadow-brand-500/20 transition-all"
        >
          <span>{currentIndex + 1 === activeQuestions.length ? 'পরীক্ষা জমা দিন' : 'পরবর্তী প্রশ্ন'}</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
