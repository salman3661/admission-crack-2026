import React, { useState } from 'react';
import { DecksView } from './DecksView';
import type { QuizQuestion, AppMode, SubjectType, WeekFilterType, UserProfile, TrackType } from '../types';
import { MathText } from './MathText';
import { 
  CheckCircle2, 
  XCircle, 
  ChevronLeft, 
  ChevronRight, 
  Zap
} from 'lucide-react';

export interface QuestionDeckViewProps {
  questions?: QuizQuestion[];
  initialIndex?: number;
  onSelectMode?: (mode: AppMode) => void;
  onSelectSubject?: (subject: SubjectType) => void;
  selectedWeek?: WeekFilterType;
  onSelectWeek?: (week: WeekFilterType) => void;
  user?: UserProfile;
  onOpenAuth?: () => void;
  totalSlides?: number;
  totalFlashcards?: number;
  totalQuizzes?: number;
  activeTrack?: TrackType;
  onSelectTrack?: (track: TrackType) => void;
}

export const QuestionDeckCard: React.FC<{
  question: QuizQuestion;
  index: number;
  total: number;
  onNext?: () => void;
  onPrev?: () => void;
}> = ({ question: q, index, total, onNext, onPrev }) => {
  const [selectedOpt, setSelectedOpt] = useState<number | null>(null);

  const isAnswered = selectedOpt !== null;
  const isCorrect = isAnswered && selectedOpt === q.ans;

  return (
    <div className="bg-white dark:bg-zinc-900 rounded-3xl p-5 sm:p-6 border border-zinc-200/80 dark:border-zinc-800 shadow-sm max-w-3xl mx-auto space-y-4">
      {/* Top Header with Index Counter and Dynamic Frequency Meta Badge */}
      <div className="flex items-center justify-between gap-2 pb-3 border-b border-zinc-100 dark:border-zinc-800/80 flex-wrap">
        <div className="flex items-center gap-2 flex-wrap">
          {/* Index Counter */}
          <span className="text-xs font-mono font-bold px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 shadow-xs">
            প্রশ্ন: {index + 1} / {total} টি
          </span>

          {/* Dynamic Meta Badge Tracking Expected Exam Frequency */}
          {q.expected_count !== undefined && q.expected_count !== null && (
            <span className="text-[11px] font-bold px-2.5 py-1 rounded-full bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 shadow-xs inline-flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse" />
              <span>🎯 প্রত্যাশিত ফ্রিকোয়েন্সি: {typeof q.expected_count === 'number' ? `${q.expected_count} বার` : q.expected_count}</span>
            </span>
          )}

          {q.origin && (
            <span className="text-[11px] font-bold px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 shadow-xs">
              📍 {q.origin}
            </span>
          )}

          <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-700">
            {q.subject}
          </span>
        </div>

        {q.yield_stars && (
          <div className="flex items-center gap-1 text-xs font-bold text-amber-500">
            <span>{'⭐️'.repeat(q.yield_stars)}</span>
            <span className="text-zinc-500 font-mono text-[11px]">({q.probability || 'High-Yield'})</span>
          </div>
        )}
      </div>

      {/* Question Text */}
      <div className="text-base sm:text-lg font-bold text-zinc-900 dark:text-white leading-relaxed">
        <MathText content={q.q} />
      </div>

      {/* Options List */}
      <div className="space-y-2.5">
        {q.opts.map((opt, optIdx) => {
          const isSelected = selectedOpt === optIdx;
          const isRightAnswer = isAnswered && q.ans === optIdx;
          const isWrongChoice = isAnswered && isSelected && !isRightAnswer;

          let style = 'bg-zinc-50 dark:bg-zinc-800/60 border-zinc-200 dark:border-zinc-800 text-zinc-800 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800';
          if (isRightAnswer) {
            style = 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 font-bold';
          } else if (isWrongChoice) {
            style = 'bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-900 dark:text-rose-200 font-bold';
          }

          return (
            <button
              key={optIdx}
              onClick={() => setSelectedOpt(optIdx)}
              className={`w-full p-3 rounded-2xl border text-left flex items-center justify-between gap-3 text-sm transition-all cursor-pointer ${style}`}
            >
              <div className="flex items-center gap-2.5 flex-1">
                <span className={`w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 ${
                  isRightAnswer
                    ? 'bg-emerald-600 text-white'
                    : isWrongChoice
                    ? 'bg-rose-600 text-white'
                    : 'bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-700 text-zinc-700 dark:text-zinc-300'
                }`}>
                  {String.fromCharCode(65 + optIdx)}
                </span>
                <MathText content={opt} />
              </div>

              {isRightAnswer && <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />}
              {isWrongChoice && <XCircle className="w-4 h-4 text-rose-600 shrink-0" />}
            </button>
          );
        })}
      </div>

      {/* Explanation & Trap Box */}
      {isAnswered && (
        <div className="p-4 rounded-2xl bg-zinc-50 dark:bg-zinc-800/50 border border-zinc-200/80 dark:border-zinc-700/80 text-xs sm:text-sm text-zinc-700 dark:text-zinc-300 space-y-2 animate-in fade-in duration-150">
          <div className="font-bold text-emerald-700 dark:text-emerald-400">
            {isCorrect ? '✅ সঠিক উত্তর!' : '❌ ভুল উত্তর!'} সঠিক বিকল্প: {String.fromCharCode(65 + q.ans)}
          </div>
          <MathText content={q.exp} />

          {(q.trap_alert || q.trap) && (
            <div className="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-900 dark:text-amber-200 text-xs flex items-start gap-1.5 mt-2">
              <Zap className="w-4 h-4 text-amber-500 shrink-0 mt-0.5" />
              <span><strong>ট্র্যাপ সতর্কতা:</strong> {q.trap_alert || q.trap}</span>
            </div>
          )}
        </div>
      )}

      {/* Navigation Buttons */}
      <div className="flex items-center justify-between pt-2">
        <button
          onClick={onPrev}
          disabled={!onPrev || index === 0}
          className="px-4 py-2 rounded-xl bg-zinc-100 dark:bg-zinc-800 hover:bg-zinc-200 dark:hover:bg-zinc-700 text-xs font-bold disabled:opacity-40 flex items-center gap-1 transition-all cursor-pointer"
        >
          <ChevronLeft className="w-4 h-4" />
          পূর্ববর্তী প্রশ্ন
        </button>

        <button
          onClick={onNext}
          disabled={!onNext || index === total - 1}
          className="px-4 py-2 rounded-xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold disabled:opacity-40 flex items-center gap-1 transition-all cursor-pointer"
        >
          পরবর্তী প্রশ্ন
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

export const DeckView: React.FC<QuestionDeckViewProps> = (props) => {
  const { questions, initialIndex = 0, ...decksProps } = props;
  const [currentIndex, setCurrentIndex] = useState(initialIndex);

  // If questions are provided, render interactive question deck
  if (questions && questions.length > 0) {
    const currentQ = questions[currentIndex] || questions[0];
    return (
      <div className="max-w-4xl mx-auto px-3 sm:px-6 py-6 pb-28 space-y-5">
        <QuestionDeckCard
          question={currentQ}
          index={currentIndex}
          total={questions.length}
          onPrev={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
          onNext={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
        />
      </div>
    );
  }

  // Otherwise delegate to DecksView
  return <DecksView {...(decksProps as React.ComponentProps<typeof DecksView>)} />;
};

export default DeckView;
export { DecksView };
