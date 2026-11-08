import React, { useState, useMemo, useCallback } from 'react';
import { 
  ArrowRight, 
  Zap, 
  Sparkles, 
  ChevronDown, 
  Layers, 
  Calendar, 
  CheckCircle2, 
  ShieldAlert, 
  Search, 
  X, 
  Filter 
} from 'lucide-react';
import { MathText } from './MathText';
import masterBlueprintRaw from '../data/master_chapter_blueprint.json';
import syntheticPredictorsRaw from '../data/chapter_synthetic_predictors.json';
import questionsRaw from '../data/questions.json';
import weeksRaw from '../data/weeks.json';
import recentGkRaw from '../data/recent_gk_monthly.json';
import sureShotEnglishRaw from '../data/sure_shot_english_predictors.json';
import { getExamHistory } from '../lib/analytics';
import type { 
  AppMode, 
  SubjectType, 
  WeekFilterType, 
  UserProfile, 
  TrackType, 
  MasterChapterBlueprint, 
  MasterMegaType, 
  ChapterSyntheticPredictors, 
  SyntheticPredictorQuestion, 
  QuizQuestion 
} from '../types';

interface DecksViewProps {
  onSelectMode: (mode: AppMode) => void;
  onSelectSubject: (subject: SubjectType) => void;
  selectedWeek: WeekFilterType;
  onSelectWeek: (week: WeekFilterType) => void;
  user: UserProfile;
  onOpenAuth: () => void;
  totalSlides: number;
  totalFlashcards: number;
  totalQuizzes: number;
  activeTrack?: TrackType;
  onSelectTrack?: (track: TrackType) => void;
}

// Bengali Numerals Converter
const toBn = (num: number | string): string => {
  const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
  return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)] ?? d);
};

// Subject Colors & Themes
const SUBJECT_THEMES: Record<string, {
  bg: string;
  activeBg: string;
  badge: string;
  border: string;
  accent: string;
  icon: string;
  labelBn: string;
}> = {
  'Physics': {
    bg: 'bg-cyan-500/10 text-cyan-700 dark:text-cyan-300 border-cyan-500/30',
    activeBg: 'bg-gradient-to-r from-cyan-600 to-blue-600 text-white border-cyan-600 shadow-cyan-500/25',
    badge: 'bg-cyan-50 dark:bg-cyan-950/50 text-cyan-700 dark:text-cyan-300 border-cyan-200 dark:border-cyan-800',
    border: 'border-cyan-500/30',
    accent: 'text-cyan-600 dark:text-cyan-400',
    icon: '⚡',
    labelBn: 'পদার্থবিজ্ঞান'
  },
  'Chemistry': {
    bg: 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border-emerald-500/30',
    activeBg: 'bg-gradient-to-r from-emerald-600 to-teal-600 text-white border-emerald-600 shadow-emerald-500/25',
    badge: 'bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800',
    border: 'border-emerald-500/30',
    accent: 'text-emerald-600 dark:text-emerald-400',
    icon: '🧪',
    labelBn: 'রসায়ন'
  },
  'Higher Math': {
    bg: 'bg-amber-500/10 text-amber-700 dark:text-amber-300 border-amber-500/30',
    activeBg: 'bg-gradient-to-r from-amber-600 to-orange-600 text-white border-amber-600 shadow-amber-500/25',
    badge: 'bg-amber-50 dark:bg-amber-950/50 text-amber-700 dark:text-amber-300 border-amber-200 dark:border-amber-800',
    border: 'border-amber-500/30',
    accent: 'text-amber-600 dark:text-amber-400',
    icon: '📐',
    labelBn: 'উচ্চতর গণিত'
  },
  'Biology': {
    bg: 'bg-rose-500/10 text-rose-700 dark:text-rose-300 border-rose-500/30',
    activeBg: 'bg-gradient-to-r from-rose-600 to-pink-600 text-white border-rose-600 shadow-rose-500/25',
    badge: 'bg-rose-50 dark:bg-rose-950/50 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-800',
    border: 'border-rose-500/30',
    accent: 'text-rose-600 dark:text-rose-400',
    icon: '🧬',
    labelBn: 'জীববিজ্ঞান'
  }
};

// ============================================================================
// MEMOIZED SUBCOMPONENT: MegaTypeItem
// ============================================================================
interface MegaTypeItemProps {
  type: MasterMegaType;
  isExpanded: boolean;
  onToggle: () => void;
}

const MegaTypeItem = React.memo<MegaTypeItemProps>(({ type, isExpanded, onToggle }) => {
  return (
    <div className="rounded-xl border border-slate-200/90 dark:border-slate-800/90 bg-white/70 dark:bg-slate-900/60 overflow-hidden transition-all duration-150">
      <button
        onClick={onToggle}
        className="w-full p-3 sm:p-3.5 flex items-center justify-between gap-3 text-left hover:bg-slate-50/70 dark:hover:bg-slate-800/50 transition-colors cursor-pointer"
      >
        <div className="flex items-center gap-2.5 flex-1 min-w-0">
          <span className="w-2 h-2 rounded-full bg-emerald-500 shrink-0" />
          <span className="text-xs sm:text-sm font-bold text-slate-800 dark:text-slate-100 truncate">
            {type.name}
          </span>
          <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-amber-500/30 shrink-0">
            {type.importance || '৫-স্টার'} • {toBn(type.repeat_frequency || 0)}টি রিপিট
          </span>
        </div>
        <ChevronDown className={`w-4 h-4 text-slate-400 transition-transform duration-200 shrink-0 ${isExpanded ? 'rotate-180' : ''}`} />
      </button>

      {isExpanded && (
        <div className="p-3.5 sm:p-4 pt-1 border-t border-slate-100 dark:border-slate-800/80 space-y-2.5 animate-in fade-in duration-150">
          {/* Core Rule / Formula */}
          {type.core_rule && (
            <div className="p-2.5 sm:p-3 rounded-lg bg-slate-50 dark:bg-slate-800/70 text-xs sm:text-sm text-slate-800 dark:text-slate-200 border border-slate-200/70 dark:border-slate-700/60 leading-relaxed font-sans">
              <span className="font-bold text-slate-900 dark:text-white mr-1.5">📌 কোর সূত্র ও নিয়ম:</span>
              <MathText content={type.core_rule} />
            </div>
          )}

          {/* High-Contrast Emerald Accent Speed Elimination Hack */}
          {type.speed_elimination && (
            <div className="flex items-start gap-2 p-2.5 rounded-lg bg-emerald-500/15 dark:bg-emerald-500/20 text-emerald-900 dark:text-emerald-200 border border-emerald-500/35 text-xs sm:text-sm leading-relaxed shadow-xs">
              <Zap className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0 mt-0.5" />
              <div>
                <span className="font-black text-emerald-800 dark:text-emerald-300 mr-1.5 uppercase tracking-wide text-[11px]">
                  ⚡ স্পিড এলিমিনেশন ট্রিক:
                </span>
                <MathText content={type.speed_elimination} />
              </div>
            </div>
          )}

          {/* Repeat Past Tags */}
          {type.past_tags && type.past_tags.length > 0 && (
            <div className="flex items-center gap-1.5 flex-wrap text-[10px] font-mono text-slate-500 dark:text-slate-400 pt-1">
              <span className="font-sans font-semibold text-slate-600 dark:text-slate-300">পূর্ববর্তী প্রশ্ন রেফারেন্স:</span>
              {type.past_tags.slice(0, 6).map((tag, i) => (
                <span key={i} className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
                  {tag}
                </span>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
});

MegaTypeItem.displayName = 'MegaTypeItem';

// ============================================================================
// MEMOIZED SUBCOMPONENT: ChapterCard
// ============================================================================
interface ChapterCardProps {
  chapter: MasterChapterBlueprint;
  predictorsCount: number;
  onLaunchPredictorDrill: (chapterId: string) => void;
}

const ChapterCard = React.memo<ChapterCardProps>(({
  chapter,
  predictorsCount,
  onLaunchPredictorDrill
}) => {
  const [isTypesExpanded, setIsTypesExpanded] = useState(false);
  const [expandedTypeIds, setExpandedTypeIds] = useState<Record<string, boolean>>({});

  const toggleType = useCallback((typeId: string) => {
    setExpandedTypeIds(prev => ({
      ...prev,
      [typeId]: !prev[typeId]
    }));
  }, []);

  const theme = SUBJECT_THEMES[chapter.subject] || SUBJECT_THEMES['Physics'];

  return (
    <div className="rounded-2xl border border-slate-200/90 dark:border-slate-800/90 bg-white/80 dark:bg-slate-900/80 backdrop-blur-xl p-4 sm:p-5 shadow-xs hover:shadow-md transition-all duration-200 flex flex-col justify-between group">
      <div>
        {/* Header Badges */}
        <div className="flex items-center justify-between gap-2 mb-2.5">
          <span className={`px-2.5 py-0.5 rounded-md text-[10px] font-extrabold uppercase tracking-wider border ${theme.badge}`}>
            {theme.icon} {theme.labelBn} • {chapter.paper}
          </span>
          <div className="flex items-center gap-1.5">
            <span className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border border-emerald-500/25">
              {toBn(predictorsCount)} MCQ ড্রিল
            </span>
            <span className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-amber-500/10 text-amber-700 dark:text-amber-300 border border-amber-500/25 flex items-center gap-1">
              <Sparkles className="w-3 h-3 text-amber-500" />
              {toBn(chapter.mega_types.length)} টাইপ
            </span>
          </div>
        </div>

        {/* Chapter Title */}
        <h3 className="text-base sm:text-lg font-black text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors mb-2">
          {chapter.title}
        </h3>

        {/* Mega Types Preview Pills */}
        <div className="flex flex-wrap gap-1.5 mb-3.5">
          {chapter.mega_types.slice(0, 3).map((t, idx) => (
            <span 
              key={idx} 
              className="px-2 py-0.5 rounded-md bg-slate-100/90 dark:bg-slate-800/90 text-slate-700 dark:text-slate-300 text-[11px] font-medium truncate max-w-[240px]"
              title={t.name}
            >
              • {t.name.split(':')[1]?.trim() || t.name}
            </span>
          ))}
          {chapter.mega_types.length > 3 && (
            <span className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-500 text-[10px] font-mono">
              +{toBn(chapter.mega_types.length - 3)} আরও
            </span>
          )}
        </div>
      </div>

      {/* Action Buttons */}
      <div className="space-y-2 pt-2 border-t border-slate-100 dark:border-slate-800/80">
        <div className="flex items-center gap-2">
          {/* Direct 1-Click Launch Predictor Drill */}
          <button
            onClick={() => onLaunchPredictorDrill(chapter.id)}
            className="flex-1 py-2.5 px-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs sm:text-sm font-bold shadow-xs hover:shadow-emerald-500/20 active:scale-95 transition-all flex items-center justify-center gap-1.5 cursor-pointer"
          >
            <Zap className="w-4 h-4 text-emerald-200 shrink-0" />
            <span>২০টি প্রেডিক্টর ড্রিল (১-ক্লিক শুরু)</span>
          </button>

          {/* Toggle Types Accordion */}
          <button
            onClick={() => setIsTypesExpanded(prev => !prev)}
            className="p-2.5 rounded-xl border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer shrink-0"
            title={isTypesExpanded ? "মেগা-টাইপ লুকান" : "সব মেগা-টাইপ বিস্তারিত দেখুন"}
          >
            <ChevronDown className={`w-4 h-4 transition-transform duration-200 ${isTypesExpanded ? 'rotate-180' : ''}`} />
          </button>
        </div>

        {/* Expandable Mega-Types list */}
        {isTypesExpanded && (
          <div className="pt-2 space-y-2 animate-in fade-in duration-200">
            <div className="text-[11px] font-bold text-slate-500 dark:text-slate-400 flex items-center justify-between">
              <span>অধ্যায়ের মেগা-টাইপ ও কোর সূত্র তালিকা:</span>
              <span className="font-mono">{toBn(chapter.mega_types.length)}টি টাইপ</span>
            </div>
            {chapter.mega_types.map(type => (
              <MegaTypeItem
                key={type.type_id}
                type={type}
                isExpanded={!!expandedTypeIds[type.type_id]}
                onToggle={() => toggleType(type.type_id)}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
});

ChapterCard.displayName = 'ChapterCard';

// ============================================================================
// MEMOIZED SUBCOMPONENT: WeekProgressCard
// ============================================================================
interface WeekProgressCardProps {
  weekId: string;
  name: string;
  badge: string;
  description: string;
  totalMCQs: number;
  totalTraps: number;
  solvedCount: number;
  accuracy: number;
  pendingTraps: number;
  onStartSpeedDrill: (weekId: string) => void;
}

const WeekProgressCard = React.memo<WeekProgressCardProps>(({
  weekId,
  name,
  badge,
  description,
  totalMCQs,
  totalTraps,
  solvedCount,
  accuracy,
  pendingTraps,
  onStartSpeedDrill
}) => {
  const percentSolved = totalMCQs > 0 ? Math.round((solvedCount / totalMCQs) * 100) : 0;

  return (
    <div className="rounded-2xl border border-slate-200/90 dark:border-slate-800/90 bg-white/80 dark:bg-slate-900/80 backdrop-blur-xl p-4 sm:p-5 shadow-xs hover:shadow-md transition-all duration-200 flex flex-col justify-between group">
      <div>
        {/* Top Badges */}
        <div className="flex items-center justify-between gap-2 mb-2">
          <span className="px-2.5 py-0.5 rounded-md text-[10px] font-black uppercase tracking-wider bg-emerald-500/15 text-emerald-800 dark:text-emerald-300 border border-emerald-500/30 flex items-center gap-1 font-mono">
            <Calendar className="w-3 h-3 text-emerald-600" />
            {name}
          </span>
          
          {/* Solved Status Pill */}
          <span className="text-[11px] font-mono font-bold text-slate-600 dark:text-slate-300">
            {toBn(solvedCount)} / {toBn(totalMCQs)} MCQ ({toBn(percentSolved)}%)
          </span>
        </div>

        {/* Week Syllabus Topics */}
        <h3 className="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors mb-1.5 leading-snug">
          {badge}
        </h3>

        <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mb-3.5 line-clamp-2">
          {description}
        </p>

        {/* Progress Bar */}
        <div className="w-full bg-slate-100 dark:bg-slate-800 rounded-full h-2 mb-3.5 overflow-hidden">
          <div 
            className="bg-gradient-to-r from-emerald-500 to-teal-500 h-2 rounded-full transition-all duration-500"
            style={{ width: `${Math.max(percentSolved, 4)}%` }}
          />
        </div>

        {/* Key Stats Row */}
        <div className="grid grid-cols-2 gap-2 mb-3.5">
          {/* Accuracy % */}
          <div className="p-2 rounded-xl bg-slate-50 dark:bg-slate-800/70 border border-slate-200/70 dark:border-slate-700/60">
            <div className="text-[10px] font-semibold text-slate-500 dark:text-slate-400">নির্ভুলতা (Accuracy)</div>
            <div className="text-sm font-black text-slate-900 dark:text-white font-mono mt-0.5 flex items-center gap-1">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500" />
              <span>{accuracy > 0 ? `${toBn(accuracy)}%` : '--'}</span>
            </div>
          </div>

          {/* Rose/Amber Badge for Pending Traps */}
          <div className="p-2 rounded-xl bg-amber-500/10 dark:bg-rose-500/15 border border-amber-500/25 dark:border-rose-500/30">
            <div className="text-[10px] font-semibold text-amber-900 dark:text-rose-200">
              পেন্ডিং ট্র্যাপ ({toBn(totalTraps)} মোট)
            </div>
            <div className="text-sm font-black text-amber-800 dark:text-rose-300 font-mono mt-0.5 flex items-center gap-1">
              <ShieldAlert className="w-3.5 h-3.5 text-amber-600 dark:text-rose-400" />
              <span>{toBn(pendingTraps)}টি ট্র্যাপ</span>
            </div>
          </div>
        </div>
      </div>

      {/* 1-Click to Start Weekly PCMB Speed Drill */}
      <button
        onClick={() => onStartSpeedDrill(weekId)}
        className="w-full py-2.5 px-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs sm:text-sm font-black shadow-xs hover:shadow-emerald-500/20 active:scale-95 transition-all flex items-center justify-center gap-2 cursor-pointer"
      >
        <Zap className="w-4 h-4 text-emerald-200" />
        <span>⚡ উইকলি স্পিড ড্রিল শুরু করুন</span>
      </button>
    </div>
  );
});

WeekProgressCard.displayName = 'WeekProgressCard';

// ============================================================================
// MEMOIZED SUBCOMPONENT: InlinePredictorDrill (Zero-lag inline interactive drill)
// ============================================================================
interface InlinePredictorDrillProps {
  chapter: MasterChapterBlueprint;
  predictors: SyntheticPredictorQuestion[];
  onClose: () => void;
}

const InlinePredictorDrill = React.memo<InlinePredictorDrillProps>(({
  chapter,
  predictors,
  onClose
}) => {
  const [currentIdx, setCurrentIdx] = useState(0);
  const [userAnswers, setUserAnswers] = useState<Record<string, string>>({});
  const [showOnlyTraps, setShowOnlyTraps] = useState(false);

  const displayedList = useMemo(() => {
    if (!showOnlyTraps) return predictors;
    return predictors.filter(q => {
      const ans = userAnswers[q.id];
      return ans && ans !== q.answer;
    });
  }, [predictors, showOnlyTraps, userAnswers]);

  const activeQ = displayedList[currentIdx] || displayedList[0];

  const handleSelectOption = (qId: string, optLetter: string) => {
    setUserAnswers(prev => ({ ...prev, [qId]: optLetter }));
  };

  const scoreStats = useMemo(() => {
    let answered = 0;
    let correct = 0;
    let wrong = 0;

    predictors.forEach(q => {
      const a = userAnswers[q.id];
      if (a) {
        answered++;
        if (a === q.answer) correct++;
        else wrong++;
      }
    });

    const accuracy = answered > 0 ? Math.round((correct / answered) * 100) : 0;
    return { answered, correct, wrong, total: predictors.length, accuracy };
  }, [predictors, userAnswers]);

  if (!activeQ) {
    return (
      <div className="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-center space-y-3">
        <p className="text-sm text-slate-600 dark:text-slate-400">কোনো ভুল ট্র্যাপ প্রশ্ন পাওয়া যায়নি।</p>
        <button
          onClick={() => setShowOnlyTraps(false)}
          className="px-4 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold"
        >
          সব ২০টি প্রশ্নে ফিরুন
        </button>
      </div>
    );
  }

  const optionLetters = ['A', 'B', 'C', 'D'];
  const userSelected = userAnswers[activeQ.id];
  const isAnswered = !!userSelected;

  return (
    <div className="rounded-3xl border border-emerald-500/40 bg-white/95 dark:bg-slate-900/95 backdrop-blur-2xl p-4 sm:p-6 shadow-xl space-y-4 animate-in fade-in zoom-in-95 duration-150">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 border border-emerald-500/30 uppercase">
              {chapter.subject} • ২০টি প্রেডিক্টর ড্রিল
            </span>
            <span className="text-xs text-slate-500 font-mono">
              প্রশ্ন {toBn(currentIdx + 1)} / {toBn(displayedList.length)}
            </span>
          </div>
          <h2 className="text-lg sm:text-xl font-black text-slate-900 dark:text-white">
            {chapter.title}
          </h2>
        </div>

        {/* Live Score Pill & Close */}
        <div className="flex items-center gap-2 self-start sm:self-auto">
          <div className="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 font-mono text-xs font-bold text-slate-700 dark:text-slate-300 flex items-center gap-2">
            <span>স্কোর: <strong className="text-emerald-600">{toBn(scoreStats.correct)}</strong>/{toBn(scoreStats.total)}</span>
            <span>•</span>
            <span>নির্ভুলতা: <strong className="text-cyan-600">{toBn(scoreStats.accuracy)}%</strong></span>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition-colors cursor-pointer"
            title="ড্রিল বন্ধ করুন"
          >
            <X className="w-5 h-5" />
          </button>
        </div>
      </div>

      {/* Quick Jump Question Dots */}
      <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
        {displayedList.map((q, idx) => {
          const ans = userAnswers[q.id];
          const isCorrect = ans === q.answer;
          const isCurrent = idx === currentIdx;

          let dotClass = 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border-slate-300 dark:border-slate-700';
          if (ans) {
            dotClass = isCorrect 
              ? 'bg-emerald-600 text-white border-emerald-600' 
              : 'bg-rose-600 text-white border-rose-600';
          }

          return (
            <button
              key={q.id}
              onClick={() => setCurrentIdx(idx)}
              className={`w-7 h-7 rounded-lg text-xs font-mono font-bold shrink-0 border transition-all cursor-pointer ${dotClass} ${
                isCurrent ? 'ring-2 ring-emerald-500 scale-105' : ''
              }`}
            >
              {idx + 1}
            </button>
          );
        })}
      </div>

      {/* Question Stem */}
      <div className="p-4 rounded-2xl bg-slate-50/80 dark:bg-slate-800/50 border border-slate-200/80 dark:border-slate-700/80 text-sm sm:text-base font-semibold text-slate-900 dark:text-white leading-relaxed">
        <MathText content={activeQ.stem} />
      </div>

      {/* 4 Options Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
        {activeQ.options.map((opt, i) => {
          const letter = optionLetters[i];
          const isSelected = userSelected === letter;
          const isCorrectAnswer = activeQ.answer === letter;
          const showFeedback = isAnswered;

          let optionStyle = 'bg-white dark:bg-slate-800/80 border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 hover:border-emerald-500';

          if (showFeedback) {
            if (isCorrectAnswer) {
              optionStyle = 'bg-emerald-500/20 text-emerald-900 dark:text-emerald-200 border-emerald-500 font-bold ring-1 ring-emerald-500';
            } else if (isSelected) {
              optionStyle = 'bg-rose-500/20 text-rose-900 dark:text-rose-200 border-rose-500 font-bold ring-1 ring-rose-500';
            } else {
              optionStyle = 'opacity-60 bg-slate-50 dark:bg-slate-900/50 border-slate-200 dark:border-slate-800 text-slate-500';
            }
          }

          return (
            <button
              key={i}
              onClick={() => handleSelectOption(activeQ.id, letter)}
              className={`p-3 sm:p-3.5 rounded-xl border text-left text-xs sm:text-sm font-medium transition-all flex items-start gap-2.5 cursor-pointer ${optionStyle}`}
            >
              <span className={`w-6 h-6 rounded-md font-mono text-xs font-bold flex items-center justify-center shrink-0 ${
                showFeedback && isCorrectAnswer 
                  ? 'bg-emerald-600 text-white' 
                  : showFeedback && isSelected 
                    ? 'bg-rose-600 text-white' 
                    : 'bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300'
              }`}>
                {letter}
              </span>
              <div className="flex-1 pt-0.5">
                <MathText content={opt} />
              </div>
            </button>
          );
        })}
      </div>

      {/* Feedback Accordion (Speed Hack & Trap Alert) */}
      {isAnswered && (
        <div className="space-y-2.5 pt-2 animate-in fade-in duration-150">
          {/* High-Contrast Emerald Accent for Speed Hack */}
          {activeQ.speed_hack && (
            <div className="flex items-start gap-2 p-3 rounded-xl bg-emerald-500/15 dark:bg-emerald-500/20 text-emerald-900 dark:text-emerald-200 border border-emerald-500/35 text-xs sm:text-sm leading-relaxed shadow-xs">
              <Zap className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0 mt-0.5" />
              <div>
                <span className="font-black text-emerald-800 dark:text-emerald-300 mr-1.5 uppercase text-[11px]">
                  ⚡ স্পিড এলিমিনেশন হ্যাক:
                </span>
                <MathText content={activeQ.speed_hack} />
              </div>
            </div>
          )}

          {/* Rose/Amber Badge for Trap Alert */}
          {activeQ.trap_alert && (
            <div className="flex items-start gap-2 p-3 rounded-xl bg-amber-500/15 dark:bg-rose-500/20 text-amber-950 dark:text-rose-200 border border-amber-500/30 dark:border-rose-500/40 text-xs sm:text-sm leading-relaxed shadow-xs">
              <ShieldAlert className="w-4 h-4 text-amber-600 dark:text-rose-400 shrink-0 mt-0.5" />
              <div>
                <span className="font-black text-amber-900 dark:text-rose-300 mr-1.5 uppercase text-[11px]">
                  ⚠️ ট্র্যাপ অ্যালার্ট (পরীক্ষায় যেভাবে ফাঁদে ফেলে):
                </span>
                <MathText content={activeQ.trap_alert} />
              </div>
            </div>
          )}

          {/* Full Step-by-Step Explanation */}
          {activeQ.explanation && (
            <div className="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed font-sans">
              <span className="font-bold text-slate-900 dark:text-white mr-1.5">📖 সম্পূর্ণ সমাধান:</span>
              <MathText content={activeQ.explanation} />
            </div>
          )}
        </div>
      )}

      {/* Navigation Controls */}
      <div className="flex items-center justify-between gap-2 pt-2 border-t border-slate-200 dark:border-slate-800">
        <button
          onClick={() => setCurrentIdx(prev => Math.max(0, prev - 1))}
          disabled={currentIdx === 0}
          className="px-3.5 py-2 rounded-xl border border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-700 dark:text-slate-300 disabled:opacity-40 cursor-pointer"
        >
          পূর্ববর্তী প্রশ্ন
        </button>

        <div className="flex items-center gap-2">
          <button
            onClick={() => setShowOnlyTraps(prev => !prev)}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold border transition-colors cursor-pointer flex items-center gap-1 ${
              showOnlyTraps
                ? 'bg-rose-600 text-white border-rose-600'
                : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700'
            }`}
          >
            <Filter className="w-3 h-3" />
            <span>শুধু ট্র্যাপ দেখুন</span>
          </button>

          <button
            onClick={() => setCurrentIdx(prev => Math.min(displayedList.length - 1, prev + 1))}
            disabled={currentIdx === displayedList.length - 1}
            className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-xs disabled:opacity-40 cursor-pointer"
          >
            পরবর্তী প্রশ্ন
          </button>
        </div>
      </div>
    </div>
  );
});

InlinePredictorDrill.displayName = 'InlinePredictorDrill';

// ============================================================================
// MAIN COMPONENT: DecksView
// ============================================================================
export const DecksView: React.FC<DecksViewProps> = ({
  onSelectMode,
  onSelectSubject,
  onSelectWeek,
  activeTrack = 'varsity',
  onSelectTrack,
}) => {
  // Top Workflow Switcher: 'chapter' vs 'weekly'
  const [activeWorkflow, setActiveWorkflow] = useState<'chapter' | 'weekly'>('chapter');

  // Chapter-wise view states
  const [selectedChapterSubject, setSelectedChapterSubject] = useState<'Physics' | 'Chemistry' | 'Higher Math' | 'Biology' | 'All'>('Physics');
  const [chapterSearchQuery, setChapterSearchQuery] = useState('');
  const [activeDrillChapterId, setActiveDrillChapterId] = useState<string | null>(null);

  // Tips expanded state
  const [isTipsExpanded, setIsTipsExpanded] = useState(false);

  // Load Chapter Blueprint & Synthetic Predictor Data
  const blueprintChapters = useMemo<MasterChapterBlueprint[]>(() => {
    return (masterBlueprintRaw as unknown as { chapters: MasterChapterBlueprint[] }).chapters || [];
  }, []);

  const syntheticChapters = useMemo<ChapterSyntheticPredictors[]>(() => {
    return (syntheticPredictorsRaw as unknown as { chapters: ChapterSyntheticPredictors[] }).chapters || [];
  }, []);

  // Map synthetic predictors by chapter_id for 0ms O(1) lookup
  const syntheticByChapterId = useMemo(() => {
    const map = new Map<string, SyntheticPredictorQuestion[]>();
    for (const ch of syntheticChapters) {
      map.set(ch.chapter_id, ch.predictors);
    }
    return map;
  }, [syntheticChapters]);

  // Filtered Chapters based on selected subject and search
  const filteredChapters = useMemo(() => {
    let list = blueprintChapters;
    if (selectedChapterSubject !== 'All') {
      list = list.filter(c => c.subject.toLowerCase() === selectedChapterSubject.toLowerCase());
    }
    if (chapterSearchQuery.trim()) {
      const q = chapterSearchQuery.toLowerCase().trim();
      list = list.filter(c => 
        c.title.toLowerCase().includes(q) ||
        c.subject.toLowerCase().includes(q) ||
        c.mega_types.some(t => t.name.toLowerCase().includes(q))
      );
    }
    return list;
  }, [blueprintChapters, selectedChapterSubject, chapterSearchQuery]);

  // Active drill chapter object & predictors
  const activeDrillChapter = useMemo(() => {
    if (!activeDrillChapterId) return null;
    return blueprintChapters.find(c => c.id === activeDrillChapterId) || null;
  }, [activeDrillChapterId, blueprintChapters]);

  const activeDrillPredictors = useMemo(() => {
    if (!activeDrillChapterId) return [];
    return syntheticByChapterId.get(activeDrillChapterId) || [];
  }, [activeDrillChapterId, syntheticByChapterId]);

  // 1-Click Launch Predictor Drill
  const handleLaunchPredictorDrill = useCallback((chapterId: string) => {
    setActiveDrillChapterId(chapterId);
    window.scrollTo({ top: 300, behavior: 'smooth' });
  }, []);

  const handleClosePredictorDrill = useCallback(() => {
    setActiveDrillChapterId(null);
  }, []);

  // --------------------------------------------------------------------------
  // WEEKLY PROGRESS & STATS ENGINE (Week 01 to Week 07)
  // --------------------------------------------------------------------------
  const questionsList = useMemo(() => questionsRaw as QuizQuestion[], []);
  
  // Sorted weeks 1 to 7
  const sortedWeeks = useMemo(() => {
    const weeks = [...(weeksRaw as Array<{
      id: string;
      name: string;
      badge: string;
      description: string;
      subjects: string[];
    }>)];

    return weeks.sort((a, b) => {
      const numA = parseInt(a.id.replace('week_', ''), 10) || 0;
      const numB = parseInt(b.id.replace('week_', ''), 10) || 0;
      return numA - numB;
    });
  }, []);

  // Compute live week stats
  const weeklyStatsMap = useMemo(() => {
    const map = new Map<string, {
      totalMCQs: number;
      totalTraps: number;
      solvedCount: number;
      accuracy: number;
      pendingTraps: number;
    }>();

    // Check user progress from exam history
    const examHistory = getExamHistory();
    const solvedByWeek: Record<string, { solved: number; correct: number }> = {};

    examHistory.forEach(record => {
      if (record.subjectCounts) {
        Object.keys(record.subjectCounts).forEach(() => {
          // general history presence
        });
      }
    });

    sortedWeeks.forEach(week => {
      const weekQuestions = questionsList.filter(q => q.week_id === week.id);
      const totalMCQs = weekQuestions.length;
      const totalTraps = weekQuestions.filter(q => !!(q.trap || q.trap_alert || q.trap_insight)).length;

      const progress = solvedByWeek[week.id] || { solved: 0, correct: 0 };
      const solvedCount = progress.solved;
      const accuracy = solvedCount > 0 ? Math.round((progress.correct / solvedCount) * 100) : 0;
      const pendingTraps = Math.max(0, totalTraps - solvedCount);

      map.set(week.id, {
        totalMCQs,
        totalTraps,
        solvedCount,
        accuracy,
        pendingTraps
      });
    });

    return map;
  }, [questionsList, sortedWeeks]);

  // 1-Click Launch Weekly PCMB Speed Drill
  const handleStartWeeklySpeedDrill = useCallback((weekId: string) => {
    try {
      sessionStorage.setItem('admission_autostart_exam', 'true');
    } catch {
      // ignore
    }
    onSelectWeek(weekId as WeekFilterType);
    onSelectSubject('All');
    onSelectMode('exam');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [onSelectWeek, onSelectSubject, onSelectMode]);

  const handleDeckNavigate = useCallback((targetMode: AppMode, subject: SubjectType = 'All') => {
    onSelectSubject(subject);
    onSelectMode(targetMode);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [onSelectSubject, onSelectMode]);

  return (
    <div className="max-w-6xl mx-auto px-3 sm:px-6 py-4 sm:py-6 pb-28 space-y-6">
      
      {/* =========================================================================
          1. DUAL-TARGET SPRINT TRACK SELECTOR (DU 'Ka' vs Medical MAT)
         ========================================================================= */}
      <div className="rounded-3xl backdrop-blur-xl bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80 shadow-xs overflow-hidden p-3.5 sm:p-5 transition-all">
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-3">
          {/* DU 'Ka' - Primary Target */}
          <div 
            onClick={() => onSelectTrack && onSelectTrack('varsity')}
            className={`p-3.5 sm:p-4 rounded-2xl transition-all cursor-pointer ring-1 ${
              activeTrack === 'varsity'
                ? 'bg-gradient-to-br from-emerald-500/15 via-teal-500/10 to-blue-500/10 ring-emerald-500 shadow-xs'
                : 'bg-slate-50/70 dark:bg-slate-800/50 ring-slate-200/80 dark:ring-slate-700/80 opacity-75 hover:opacity-100'
            } flex items-center justify-between group active:scale-[0.99]`}
          >
            <div className="flex items-center gap-3">
              <span className="text-2xl group-hover:scale-110 transition-transform">🎯</span>
              <div>
                <div className="flex items-center gap-1.5 flex-wrap">
                  <span className="text-xs sm:text-sm font-black text-slate-900 dark:text-white">
                    ঢাকা বিশ্ববিদ্যালয় 'ক' (DU 'Ka')
                  </span>
                  {activeTrack === 'varsity' && (
                    <span className="px-2 py-0.5 rounded-full text-[9px] font-black bg-emerald-600 text-white shadow-xs">
                      ✓ সক্রিয় মেইন ট্র্যাক
                    </span>
                  )}
                </div>
                <div className="text-[11px] text-slate-600 dark:text-slate-400 font-medium">
                  MCQ ৬০ + লিখিত ৪০ = ১০০ নম্বর • নো ক্যালকুলেটর
                </div>
              </div>
            </div>
            <span className={`px-2.5 py-1 rounded-xl text-white font-mono text-[11px] font-extrabold shrink-0 shadow-xs transition-colors ${
              activeTrack === 'varsity' ? 'bg-emerald-600' : 'bg-slate-500 group-hover:bg-emerald-600'
            }`}>
              {activeTrack === 'varsity' ? 'Active' : 'সুইচ'}
            </span>
          </div>

          {/* Medical MAT - Secondary / Backup Target */}
          <div 
            onClick={() => onSelectTrack && onSelectTrack('medical')}
            className={`p-3.5 sm:p-4 rounded-2xl transition-all cursor-pointer ring-1 ${
              activeTrack === 'medical'
                ? 'bg-gradient-to-br from-rose-500/15 via-red-500/10 to-pink-500/10 ring-rose-500 shadow-xs'
                : 'bg-slate-50/70 dark:bg-slate-800/50 ring-slate-200/80 dark:ring-slate-700/80 opacity-75 hover:opacity-100'
            } flex items-center justify-between group active:scale-[0.99]`}
          >
            <div className="flex items-center gap-3">
              <span className="text-2xl group-hover:scale-110 transition-transform">🩺</span>
              <div>
                <div className="flex items-center gap-1.5 flex-wrap">
                  <span className="text-xs sm:text-sm font-black text-slate-900 dark:text-white">
                    মেডিকেল ভর্তি পরীক্ষা (MAT 2026-27)
                  </span>
                  {activeTrack === 'medical' && (
                    <span className="px-2 py-0.5 rounded-full text-[9px] font-black bg-rose-600 text-white shadow-xs">
                      ✓ সক্রিয় ট্র্যাক
                    </span>
                  )}
                </div>
                <div className="text-[11px] text-slate-600 dark:text-slate-400 font-medium">
                  Bio 30, Chem 25, Phys 20, Eng 15, GK 10
                </div>
              </div>
            </div>
            <span className={`px-2.5 py-1 rounded-xl text-white font-mono text-[11px] font-extrabold shrink-0 shadow-xs transition-colors ${
              activeTrack === 'medical' ? 'bg-rose-600' : 'bg-slate-500 group-hover:bg-rose-600'
            }`}>
              {activeTrack === 'medical' ? 'Active' : 'সুইচ'}
            </span>
          </div>
        </div>

        {/* Collapsible Quick Tips */}
        <div className="border-t border-slate-200/70 dark:border-slate-800/70 pt-2">
          <button
            onClick={() => setIsTipsExpanded(!isTipsExpanded)}
            className="w-full flex items-center justify-between text-xs font-bold text-slate-700 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 transition-colors py-1 cursor-pointer"
          >
            <div className="flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-amber-500" />
              <span>💡 ডুয়াল-টার্গেট ৮০/২০ কৌশল ও টাইম ম্যানেজমেন্ট গাইডলাইন</span>
            </div>
            <ChevronDown className={`w-4 h-4 transition-transform duration-200 ${isTipsExpanded ? 'rotate-180' : ''}`} />
          </button>

          {isTipsExpanded && (
            <div className="mt-2.5 p-3 rounded-2xl bg-slate-50/80 dark:bg-slate-800/60 ring-1 ring-slate-200/80 dark:ring-slate-700/80 text-xs text-slate-600 dark:text-slate-300 leading-relaxed animate-in fade-in duration-200 space-y-1.5">
              <p>
                <strong>কেন কোনো কনফ্লিক্ট নেই?</strong> ফিজিক্স ও কেমিস্ট্রি যদি ভার্সিটির জন্য ম্যাথসহ ডিপ প্রিপারেশন নাও, তবে মেডিকেলের ফিজিক্স ও কেমিস্ট্রি থিওরি সরাসরি কমন পড়বে।
              </p>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1 font-medium text-[11px]">
                <div className="p-2 rounded-xl bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 ring-1 ring-emerald-500/20">
                  🎯 <strong>ভার্সিটি 'ক' (৭০% সময়):</strong> পদার্থ ও রসায়ন ম্যাথ, উচ্চতর গণিত শর্টকাট এবং লিখিত অংশের নিয়মিত খাতা চর্চা।
                </div>
                <div className="p-2 rounded-xl bg-rose-500/10 text-rose-800 dark:text-rose-300 ring-1 ring-rose-500/20">
                  🩺 <strong>মেডিকেল বুস্টার (৩০% সময়):</strong> দিনে ১.৫–২ ঘণ্টা বায়োলজি ছক (আজমল/হাসান) + ইংলিশ (১৫) + জিকে (১০)।
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* =========================================================================
          2. HIGH-CONTRAST TOP SEGMENTED PILL SWITCHER:
             [📂 চ্যাপ্টার-ভিত্তিক ব্লুপ্রিন্ট] vs [📅 সপ্তাহ-ভিত্তিক মাস্টারি (Week 01–07)]
         ========================================================================= */}
      <div className="p-1.5 rounded-2xl bg-white/90 dark:bg-slate-900/90 backdrop-blur-xl ring-2 ring-emerald-500/30 dark:ring-emerald-400/30 shadow-md flex items-center justify-between gap-1.5">
        <button
          onClick={() => setActiveWorkflow('chapter')}
          className={`flex-1 py-3 px-3 sm:px-5 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-2 cursor-pointer ${
            activeWorkflow === 'chapter'
              ? 'bg-gradient-to-r from-emerald-600 to-teal-600 text-white shadow-md ring-1 ring-emerald-400/50 scale-[1.01]'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100/70 dark:hover:bg-slate-800/70'
          }`}
        >
          <Layers className="w-4 h-4 text-emerald-200 shrink-0" />
          <span className="truncate">📂 অধ্যায়-ভিত্তিক ব্লুপ্রিন্ট (৩৪ চ্যাপ্টার)</span>
          <span className="hidden md:inline-block px-2 py-0.5 rounded-full text-[10px] bg-white/20 text-white font-mono">
            ৩৪ অধ্যায় • ৬৮০ প্রেডিক্টর
          </span>
        </button>

        <button
          onClick={() => setActiveWorkflow('weekly')}
          className={`flex-1 py-3 px-3 sm:px-5 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-2 cursor-pointer ${
            activeWorkflow === 'weekly'
              ? 'bg-gradient-to-r from-emerald-600 to-teal-600 text-white shadow-md ring-1 ring-emerald-400/50 scale-[1.01]'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100/70 dark:hover:bg-slate-800/70'
          }`}
        >
          <Calendar className="w-4 h-4 text-emerald-200 shrink-0" />
          <span className="truncate">📅 সপ্তাহ-ভিত্তিক মাস্টারি (Week 01 – 07)</span>
          <span className="hidden md:inline-block px-2 py-0.5 rounded-full text-[10px] bg-white/20 text-white font-mono">
            ৭টি উইকলি স্লট • ৭৫০ MCQ
          </span>
        </button>
      </div>

      {/* =========================================================================
          WORKFLOW 1: CHAPTER-WISE BLUEPRINT VIEW
         ========================================================================= */}
      {activeWorkflow === 'chapter' && (
        <div className="space-y-4">
          
          {/* Active Inline Predictor Drill (if open) */}
          {activeDrillChapter && (
            <InlinePredictorDrill
              chapter={activeDrillChapter}
              predictors={activeDrillPredictors}
              onClose={handleClosePredictorDrill}
            />
          )}

          {/* Smooth Horizontal Subject Selector Pills & Search */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            {/* Subject Pills: Physics, Chemistry, Higher Math, Biology, All */}
            <div className="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none">
              {[
                { id: 'Physics' as const, label: 'পদার্থবিজ্ঞান', sub: '১০ অধ্যায়', icon: '⚡' },
                { id: 'Chemistry' as const, label: 'রসায়ন', sub: '৮ অধ্যায়', icon: '🧪' },
                { id: 'Higher Math' as const, label: 'উচ্চতর গণিত', sub: '৮ অধ্যায়', icon: '📐' },
                { id: 'Biology' as const, label: 'জীববিজ্ঞান', sub: '৮ অধ্যায়', icon: '🧬' },
                { id: 'All' as const, label: 'সকল বিষয়', sub: '৩৪ অধ্যায়', icon: '🌟' },
              ].map(sub => {
                const isSelected = selectedChapterSubject === sub.id;
                const theme = SUBJECT_THEMES[sub.id] || { activeBg: 'bg-emerald-600 text-white' };

                return (
                  <button
                    key={sub.id}
                    onClick={() => setSelectedChapterSubject(sub.id)}
                    className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all shrink-0 border cursor-pointer flex items-center gap-1.5 ${
                      isSelected
                        ? `${theme.activeBg} shadow-sm border-transparent scale-[1.02]`
                        : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800'
                    }`}
                  >
                    <span>{sub.icon}</span>
                    <span>{sub.label}</span>
                    <span className={`text-[10px] px-1.5 py-0.2 rounded-md font-mono ${
                      isSelected ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                    }`}>
                      {sub.sub}
                    </span>
                  </button>
                );
              })}
            </div>

            {/* Quick Search */}
            <div className="relative min-w-[220px]">
              <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                value={chapterSearchQuery}
                onChange={(e) => setChapterSearchQuery(e.target.value)}
                placeholder="অধ্যায় বা টপিক খুঁজুন..."
                className="w-full pl-9 pr-3 py-1.5 rounded-xl text-xs bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-slate-900 dark:text-white"
              />
            </div>
          </div>

          {/* Section Summary Header */}
          <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-1 font-medium">
            <span>
              প্রদর্শিত হচ্ছে: <strong className="text-slate-800 dark:text-slate-200 font-bold">{toBn(filteredChapters.length)}টি অধ্যায়</strong> (২২,৮০৭+ প্রশ্ন অ্যানালাইসিস থেকে মেগা-টাইপ ও ৬৮০টি প্রেডিক্টর)
            </span>
            <span className="font-mono text-[11px] hidden sm:inline">
              ⚡ ১-ক্লিক ড্রিল লঞ্চার
            </span>
          </div>

          {/* Chapters Grid: All 34 Chapters with Mega-Types & 1-Click Launch */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {filteredChapters.map(chapter => {
              const predictors = syntheticByChapterId.get(chapter.id) || [];
              return (
                <ChapterCard
                  key={chapter.id}
                  chapter={chapter}
                  predictorsCount={predictors.length}
                  onLaunchPredictorDrill={handleLaunchPredictorDrill}
                />
              );
            })}
          </div>
        </div>
      )}

      {/* =========================================================================
          WORKFLOW 2: WEEKLY-WISE MASTERY PROGRESS CARDS (Week 01 to Week 07)
         ========================================================================= */}
      {activeWorkflow === 'weekly' && (
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 px-1">
            <div>
              <h2 className="text-base sm:text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <Calendar className="w-5 h-5 text-emerald-600" />
                <span>৭ সপ্তাহের ফুল সিলেবাস মাস্টারি ট্র্যাক (Week 01 – 07)</span>
              </h2>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-0.5">
                প্রতিটি সপ্তাহের সলভড স্ট্যাটাস, একুরেসি % এবং পেন্ডিং ট্র্যাপ ট্র্যাক করুন ও ১-ক্লিকে স্পিড ড্রিল শুরু করুন
              </p>
            </div>
            <span className="text-xs font-mono font-bold px-2.5 py-1 rounded-xl bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 border border-emerald-500/20 self-start sm:self-auto">
              মোট ৭৫০টি মাল্টি-স্ট্রিম MCQ
            </span>
          </div>

          {/* 7 Clean Responsive Weekly Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {sortedWeeks.map(week => {
              const stats = weeklyStatsMap.get(week.id) || {
                totalMCQs: 0,
                totalTraps: 0,
                solvedCount: 0,
                accuracy: 0,
                pendingTraps: 0
              };

              return (
                <WeekProgressCard
                  key={week.id}
                  weekId={week.id}
                  name={week.name}
                  badge={week.badge}
                  description={week.description}
                  totalMCQs={stats.totalMCQs}
                  totalTraps={stats.totalTraps}
                  solvedCount={stats.solvedCount}
                  accuracy={stats.accuracy}
                  pendingTraps={stats.pendingTraps}
                  onStartSpeedDrill={handleStartWeeklySpeedDrill}
                />
              );
            })}
          </div>
        </div>
      )}

      {/* =========================================================================
          3. EDTECH STREAM CARDS & SECONDARY ACCESS (Preserved & Enhanced)
         ========================================================================= */}
      <div className="pt-2">
        <div className="flex items-center justify-between gap-2 mb-3">
          <h2 className="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <Layers className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
            <span>এডমিশন কোর স্ট্রিম ও ডেডিকেটেড ডেক</span>
          </h2>
          <span className="text-[11px] font-semibold text-slate-500 dark:text-slate-400">
            রিয়েল PYQ, GK ও ইংলিশ প্রেডিক্টর
          </span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
          
          {/* Stream 1: Varsity 'Ka' Core */}
          <div 
            onClick={() => handleDeckNavigate('exam', 'All')}
            className="group p-4 sm:p-5 rounded-2xl backdrop-blur-xl bg-gradient-to-br from-emerald-500/10 via-emerald-600/5 to-teal-500/10 ring-1 ring-emerald-500/30 hover:ring-emerald-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-black bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/30">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping" />
                  🔴 Live 80/20
                </span>
                <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/20">
                  ২,৩৭৬+ MCQ
                </span>
              </div>
              <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors mb-1">
                ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট (DU 'Ka')
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                বিগত ১৫-২০ বছরের ঢাবি অরিজিনাল প্রশ্নব্যাংক, রিপিট প্যাটার্ন এবং নো-ক্যালকুলেটর ম্যাথ স্পিড ট্রিকস।
              </p>
            </div>
            <div className="flex items-center justify-between text-xs font-bold text-emerald-700 dark:text-emerald-400">
              <span>MCQ ৬০ + লিখিত ৪০ অনুশীলন</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Stream 2: Medical MAT */}
          <div 
            onClick={() => {
              onSelectTrack && onSelectTrack('medical');
              handleDeckNavigate('exam', 'All');
            }}
            className="group p-4 sm:p-5 rounded-2xl backdrop-blur-xl bg-gradient-to-br from-rose-500/10 via-red-600/5 to-pink-500/10 ring-1 ring-rose-500/30 hover:ring-rose-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-black bg-rose-500/15 text-rose-700 dark:text-rose-300 ring-1 ring-rose-500/30">
                  <span className="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping" />
                  🔴 Live 80/20
                </span>
                <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-rose-700 dark:text-rose-300 ring-1 ring-rose-500/20">
                  ১,৫৮৪+ প্রশ্ন
                </span>
              </div>
              <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-rose-600 dark:group-hover:text-rose-400 transition-colors mb-1">
                মেডিকেল ভর্তি পরীক্ষা (MAT 2026-27)
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                আজমল ও হাসান স্যারের বায়োলজি ছক, হাজারী স্যারের তথ্য কণিকা এবং বিগত মেডিকেল-ডেন্টাল PYQ।
              </p>
            </div>
            <div className="flex items-center justify-between text-xs font-bold text-rose-700 dark:text-rose-400">
              <span>Bio 30 • Chem 25 • Phys 20</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Stream 3: Trap Vault & Shortcuts */}
          <div 
            onClick={() => handleDeckNavigate('vault', 'All')}
            className="group p-4 sm:p-5 rounded-2xl backdrop-blur-xl bg-gradient-to-br from-amber-500/10 via-yellow-600/5 to-orange-500/10 ring-1 ring-amber-500/30 hover:ring-amber-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-black bg-amber-500/15 text-amber-700 dark:text-amber-300 ring-1 ring-amber-500/30">
                  🛡️ Trap Shield
                </span>
                <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-amber-700 dark:text-amber-300 ring-1 ring-amber-500/20">
                  ২০০+ শর্টকাট
                </span>
              </div>
              <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors mb-1">
                ১-সেকেন্ড ফর্মুলা ও ট্র্যাপ ডিফেন্স ভল্ট
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                দশমিক ভাগ, অনুপাত শর্টকাট, ত্রিকোণমিতি ডোমেন-রেঞ্জ ট্রিক এবং ঢাবি এক্সামিনারদের পছন্দের ট্র্যাপ হ্যাক।
              </p>
            </div>
            <div className="flex items-center justify-between text-xs font-bold text-amber-700 dark:text-amber-400">
              <span>ভল্ট এক্সপ্লোর করুন</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Stream 4: Udvash Recent Monthly GK 2026 */}
          <div 
            onClick={() => handleDeckNavigate('recall')}
            className="group p-4 sm:p-5 rounded-2xl backdrop-blur-xl bg-gradient-to-br from-teal-500/10 via-emerald-600/5 to-cyan-500/10 ring-1 ring-teal-500/30 hover:ring-teal-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-black bg-teal-500/15 text-teal-700 dark:text-teal-300 ring-1 ring-teal-500/30">
                  📅 উদ্ভাস মান্থলি জিকে ২০২৬
                </span>
                <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-teal-700 dark:text-teal-300 ring-1 ring-teal-500/20">
                  {(recentGkRaw as { total_cards?: number }).total_cards || 80} কার্ডস
                </span>
              </div>
              <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors mb-1">
                সাম্প্রতিক সাধারণ জ্ঞান (জানু–অক্টোবর ২০২৬)
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                ত্রয়োদশ নির্বাচন, পদ্মা ব্যারাজ, নোবেল ২০২৬, আসাম-বাংলাদেশ মিথানল ও মেগা প্রজেক্ট ট্র্যাপ ডিফেন্স।
              </p>
            </div>
            <div className="flex items-center justify-between text-xs font-bold text-teal-700 dark:text-teal-400">
              <span>অ্যাক্টিভ রিকল শুরু</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Stream 5: Sure-Shot English Predictors 2026 */}
          <div 
            onClick={() => handleDeckNavigate('recall')}
            className="group p-4 sm:p-5 rounded-2xl backdrop-blur-xl bg-gradient-to-br from-indigo-500/10 via-purple-600/5 to-blue-500/10 ring-1 ring-indigo-500/30 hover:ring-indigo-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-black bg-indigo-500/15 text-indigo-700 dark:text-indigo-300 ring-1 ring-indigo-500/30">
                  🇬🇧 শিওর-শট ইংলিশ ২০২৬
                </span>
                <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-indigo-700 dark:text-indigo-300 ring-1 ring-indigo-500/20">
                  {(sureShotEnglishRaw as { predictors?: unknown[] }).predictors?.length || 88} প্রেডিক্টর
                </span>
              </div>
              <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors mb-1">
                মেডিকেল ও ঢাবি শিওর-শট ইংলিশ ১৫ মার্কস
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                ৫টি মেগা ক্লাস্টার: Prepositions, Subject-Verb Agreement, Sentence Correction ও Vocabulary Traps।
              </p>
            </div>
            <div className="flex items-center justify-between text-xs font-bold text-indigo-700 dark:text-indigo-400">
              <span>ইংলিশ ডেক অনুশীলন</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Stream 6: Paper Final Predictor Sets */}
          <div 
            onClick={() => handleDeckNavigate('predictor')}
            className="group p-4 sm:p-5 rounded-2xl backdrop-blur-xl bg-gradient-to-br from-purple-500/10 via-violet-600/5 to-fuchsia-500/10 ring-1 ring-purple-500/30 hover:ring-purple-500 shadow-xs transition-all duration-200 cursor-pointer flex flex-col justify-between active:scale-[0.98]"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-black bg-purple-500/15 text-purple-700 dark:text-purple-300 ring-1 ring-purple-500/30">
                  🏆 ফুল পেপার ফাইনাল
                </span>
                <span className="px-2 py-0.5 rounded-lg text-[10px] font-mono font-bold bg-white/80 dark:bg-slate-800/80 text-purple-700 dark:text-purple-300 ring-1 ring-purple-500/20">
                  টাইমার এক্সাম
                </span>
              </div>
              <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors mb-1">
                মডেল টেস্ট ও এক্সপেক্টেড প্রশ্ন সেট
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-3">
                রিয়েল এক্সাম হলে বসে টাইমার ও নেগেটিভ মার্কিংসহ পূর্ণাঙ্গ পেপার ফাইনাল মডেল টেস্ট দিন।
              </p>
            </div>
            <div className="flex items-center justify-between text-xs font-bold text-purple-700 dark:text-purple-400">
              <span>সব সেট দেখুন</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

        </div>
      </div>

    </div>
  );
};
