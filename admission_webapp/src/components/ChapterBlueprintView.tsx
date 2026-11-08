import React, { useState, useMemo, useEffect, useRef } from 'react';
import { 
  Layers, 
  ChevronDown, 
  ChevronUp, 
  CheckCircle2, 
  Zap, 
  RotateCcw, 
  Hash,
  Star,
  ShieldAlert,
  Flame,
  BookOpen,
  Clock,
  ArrowLeft,
  Calendar
} from 'lucide-react';
import { MathText } from './MathText';
import masterBlueprintRaw from '../data/master_chapter_blueprint.json';
import syntheticPredictorsRaw from '../data/chapter_synthetic_predictors.json';
import weeksDataRaw from '../data/weeks.json';
import weeklyExamsRaw from '../data/weekly_exams.json';
import type { 
  MasterChapterBlueprint, 
  ChapterSyntheticPredictors, 
  SyntheticPredictorQuestion,
  AppMode,
  WeekFilterType,
  SubjectType
} from '../types';

interface ChapterBlueprintViewProps {
  onSelectMode?: (mode: AppMode) => void;
  onSelectWeek?: (week: WeekFilterType) => void;
  onSelectSubject?: (subject: SubjectType) => void;
}

// 7-Week High-Yield Syllabus & Covered Chapters Tags
const WEEK_COVERED_CHAPTERS: Record<string, { badgeText: string; chaptersText: string }> = {
  'week_01': {
    badgeText: 'ভেক্টর + গতিবিদ্যা + পরিমাণগত রসায়ন + সরলরেখা + রক্ত ও শ্বসন',
    chaptersText: 'ভেক্টর ক্যালকুলাস, প্রাস, নদী-নৌকা, স্টয়কিওমেট্রি, সরলরেখা এবং মানব শারীরতত্ত্ব।'
  },
  'week_02': {
    badgeText: 'বলবিদ্যা + পর্যায়বৃত্ত ধর্ম + রাসায়নিক সাম্যাবস্থা + বৃত্ত + কোষ ও হাইড্রা',
    chaptersText: 'নিউটনিয়ান গতি, জড়তার ভ্রামক, d-ব্লক মৌল, বাফার ও pH, বৃত্ত, জটিল সংখ্যা ও কোষ অঙ্গাণু।'
  },
  'week_03': {
    badgeText: 'কাজ, শক্তি ও ক্ষমতা + অণুজীব + ত্রিকোণমিতি + মহাকর্ষ + গুণগত রসায়ন',
    chaptersText: 'কাজ, শক্তি ও ক্ষমতা, মহাকর্ষীয় বিভব ও মুক্তিবেগ, গুণগত দ্রাব্যতা ও Ksp, ত্রিকোণমিতি ও উদ্ভিদ শারীরতত্ত্ব।'
  },
  'week_04': {
    badgeText: 'পদার্থের গাঠনিক ধর্ম + আদর্শ গ্যাস + রাসায়নিক বন্ধন + বিন্যাস-সমাবেশ + জিনতত্ত্ব',
    chaptersText: 'পৃষ্ঠটান ও আরএমএস বেগ, ফাজানের নীতি ও সংকরায়ন, প্যাসকেলের সমাবেশ সূত্র ও মেন্ডেলীয় ব্যতিক্রম।'
  },
  'week_05': {
    badgeText: 'পর্যায়বৃত্ত গতি ও তরঙ্গ + তড়িৎ রসায়ন + বহুপদী ও দ্বিপদী + প্রাণীর বিভিন্নতা',
    chaptersText: 'সরল ছন্দিত স্পন্দন ও বিট, ফ্যারাডের সূত্র ও নার্নস্ট সেল, বহুপদীর মূলের প্রকৃতি ও প্রাণীর শ্রেণিবিন্যাস।'
  },
  'week_06': {
    badgeText: 'তাপ ও পর্যায়বৃত্ত গতি + পরিবেশ ও তড়িৎ রসায়ন + ত্রিকোণমিতি ও দ্বিপদী + পরিপাক ও রেচন',
    chaptersText: 'তাপগতিবিদ্যা ও SHM, ভ্যান ডার ওয়ালস ও নার্নস্ট সমীকরণ, ত্রিকোণমিতিক রূপান্তর ও মানব রেচন।'
  },
  'week_07': {
    badgeText: 'স্থির তড়িৎ + আধুনিক পদার্থবিজ্ঞান + জৈব রসায়ন + অন্তরীকরণ + মানব শারীরতত্ত্ব',
    chaptersText: 'স্থির তড়িৎ বিভব, ফটোইলেকট্রিক ও আপেক্ষিকতা, জৈব রসায়ন সমাণুতা, ক্যালকুলাস লিমিট ও সংবেদী অঙ্গ।'
  },
  'week_08': {
    badgeText: 'চল তড়িৎ + সেমিকন্ডাক্টর ও ইলেকট্রনিক্স + জৈব রসায়ন + যোগজীকরণ + কোষ ও এর গঠন',
    chaptersText: 'হুইটস্টোন ব্রিজ ও শান্ট, ট্রানজিস্টর (α, β) ও লজিক গেট, জৈব বিক্রিয়া ও সমাণুতা, নির্দিষ্ট যোগজ ও আবদ্ধ ক্ষেত্রফল, কোষ অঙ্গাণু ও জেনেটিক কোড।'
  }
};

export const ChapterBlueprintView: React.FC<ChapterBlueprintViewProps> = ({
  onSelectMode,
  onSelectWeek,
  onSelectSubject,
}) => {
  // Hash-aware Dual Workflow Mode: 'blueprint' (অধ্যায় ব্লুপ্রিন্ট) vs 'weekly' (উইকলি মাস্টারি)
  const getInitialWorkflowMode = (): 'blueprint' | 'weekly' => {
    try {
      const hash = window.location.hash.replace('#', '').toLowerCase();
      if (hash === 'weekly' || hash === 'weeks' || hash === 'weekly-mastery') return 'weekly';
    } catch {
      // fallback
    }
    return 'blueprint';
  };

  const [workflowMode, setWorkflowMode] = useState<'blueprint' | 'weekly'>(getInitialWorkflowMode);

  const handleWorkflowChange = (mode: 'blueprint' | 'weekly') => {
    setWorkflowMode(mode);
    try {
      window.history.replaceState(null, '', mode === 'weekly' ? '#weekly' : '#blueprint');
    } catch {
      // fallback
    }
  };

  // Synchronize hash changes
  useEffect(() => {
    const handleHashChange = () => {
      try {
        const hash = window.location.hash.replace('#', '').toLowerCase();
        if (hash === 'weekly' || hash === 'weeks' || hash === 'weekly-mastery') {
          setWorkflowMode('weekly');
        } else if (hash === 'blueprint') {
          setWorkflowMode('blueprint');
        }
      } catch {
        // fallback
      }
    };
    window.addEventListener('popstate', handleHashChange);
    window.addEventListener('hashchange', handleHashChange);
    return () => {
      window.removeEventListener('popstate', handleHashChange);
      window.removeEventListener('hashchange', handleHashChange);
    };
  }, []);

  // -------------------------------------------------------------
  // TAB 1 DATA: MASTER CHAPTER BLUEPRINT & SYNTHETIC PREDICTORS
  // -------------------------------------------------------------
  const blueprintChapters: MasterChapterBlueprint[] = useMemo(() => {
    return (masterBlueprintRaw as any).chapters || [];
  }, []);

  const syntheticChapters: ChapterSyntheticPredictors[] = useMemo(() => {
    return (syntheticPredictorsRaw as any).chapters || [];
  }, []);

  // Map synthetic predictors by chapter_id for instant O(1) lookup
  const syntheticByChapterId = useMemo(() => {
    const map = new Map<string, SyntheticPredictorQuestion[]>();
    for (const ch of syntheticChapters) {
      map.set(ch.chapter_id, ch.predictors);
    }
    return map;
  }, [syntheticChapters]);

  // Subject Selector State: 'Physics' | 'Chemistry' | 'Higher Math' | 'Biology'
  const [selectedSubject, setSelectedSubjectState] = useState<'Physics' | 'Chemistry' | 'Higher Math' | 'Biology'>('Physics');

  const handleSubjectChange = (subj: 'Physics' | 'Chemistry' | 'Higher Math' | 'Biology') => {
    setSelectedSubjectState(subj);
    onSelectSubject?.(subj as SubjectType);
  };

  // Chapters of selected subject
  const currentSubjectChapters = useMemo(() => {
    return blueprintChapters.filter(c => c.subject.toLowerCase() === selectedSubject.toLowerCase());
  }, [blueprintChapters, selectedSubject]);

  // Active Chapter ID
  const [selectedChapterId, setSelectedChapterId] = useState<string>('');

  // Synchronize active chapter when subject changes
  useEffect(() => {
    if (currentSubjectChapters.length > 0) {
      const exists = currentSubjectChapters.some(c => c.id === selectedChapterId);
      if (!exists) {
        setSelectedChapterId(currentSubjectChapters[0].id);
      }
    }
  }, [selectedSubject, currentSubjectChapters, selectedChapterId]);

  // Active chapter object
  const activeChapter = useMemo(() => {
    return currentSubjectChapters.find(c => c.id === selectedChapterId) || currentSubjectChapters[0];
  }, [currentSubjectChapters, selectedChapterId]);

  // Predictors for active chapter
  const activePredictors = useMemo(() => {
    if (!activeChapter) return [];
    return syntheticByChapterId.get(activeChapter.id) || [];
  }, [syntheticByChapterId, activeChapter]);

  // View Mode inside chapter: 'blueprint' | 'quiz'
  const [activeTab, setActiveTab] = useState<'blueprint' | 'quiz'>('blueprint');

  // Collapsible Type States
  const [expandedTypes, setExpandedTypes] = useState<Record<string, boolean>>({});

  const toggleTypeExpand = (typeId: string) => {
    setExpandedTypes(prev => ({
      ...prev,
      [typeId]: prev[typeId] === undefined ? false : !prev[typeId]
    }));
  };

  const expandAllTypes = () => {
    if (!activeChapter) return;
    const newState: Record<string, boolean> = {};
    activeChapter.mega_types.forEach(t => {
      newState[t.type_id] = true;
    });
    setExpandedTypes(newState);
  };

  const collapseAllTypes = () => {
    if (!activeChapter) return;
    const newState: Record<string, boolean> = {};
    activeChapter.mega_types.forEach(t => {
      newState[t.type_id] = false;
    });
    setExpandedTypes(newState);
  };

  // Section 2: Quiz Mode State
  const [userAnswers, setUserAnswers] = useState<Record<string, string>>({});
  const [revealedQuestions, setRevealedQuestions] = useState<Record<string, boolean>>({});
  const [showOnlyTraps, setShowOnlyTraps] = useState<boolean>(false);

  // Reset quiz on chapter change
  useEffect(() => {
    setUserAnswers({});
    setRevealedQuestions({});
    setShowOnlyTraps(false);
  }, [selectedChapterId]);

  const handleSelectOption = (qId: string, optionLetter: string) => {
    setUserAnswers(prev => ({ ...prev, [qId]: optionLetter }));
    setRevealedQuestions(prev => ({ ...prev, [qId]: true }));
  };

  const handleResetQuiz = () => {
    setUserAnswers({});
    setRevealedQuestions({});
    setShowOnlyTraps(false);
  };

  const handleRevealAll = () => {
    const allRev: Record<string, boolean> = {};
    activePredictors.forEach(q => {
      allRev[q.id] = true;
    });
    setRevealedQuestions(allRev);
  };

  // Calculate Quiz Score
  const scoreStats = useMemo(() => {
    let answered = 0;
    let correct = 0;
    let wrong = 0;

    activePredictors.forEach(q => {
      const ans = userAnswers[q.id];
      if (ans) {
        answered++;
        if (ans === q.answer) {
          correct++;
        } else {
          wrong++;
        }
      }
    });

    const total = activePredictors.length;
    const accuracy = answered > 0 ? Math.round((correct / answered) * 100) : 0;

    return { answered, correct, wrong, total, accuracy };
  }, [activePredictors, userAnswers]);

  // Filtered Predictors based on showOnlyTraps
  const displayedPredictors = useMemo(() => {
    if (!showOnlyTraps) return activePredictors;
    return activePredictors.filter(q => {
      const ans = userAnswers[q.id];
      return ans && ans !== q.answer;
    });
  }, [activePredictors, showOnlyTraps, userAnswers]);

  // -------------------------------------------------------------
  // TAB 2 DATA: WEEKLY EXAMS & MASTERY ENGINE (Week 01 – 08)
  // -------------------------------------------------------------
  const sortedWeeks = useMemo(() => {
    return [...(weeksDataRaw as any[])].sort((a, b) => a.id.localeCompare(b.id));
  }, []);

  const weeklyExamsMap = useMemo(() => {
    const map = new Map<string, any[]>();
    for (const q of (weeklyExamsRaw as any[])) {
      const list = map.get(q.week_id) || [];
      list.push(q);
      map.set(q.week_id, list);
    }
    return map;
  }, []);

  // User answers per week: { [weekId]: { [questionId]: 'A' | 'B' | 'C' | 'D' } }
  const [weeklyAnswers, setWeeklyAnswers] = useState<Record<string, Record<string, string>>>(() => {
    try {
      const raw = localStorage.getItem('admission_weekly_user_answers');
      if (raw) return JSON.parse(raw);
    } catch {}
    return {};
  });

  // Active Weekly Speed Drill week
  const [activeDrillWeekId, setActiveDrillWeekId] = useState<string | null>(null);
  const [weeklyRevealed, setWeeklyRevealed] = useState<Record<string, boolean>>({});
  const [weeklyShowOnlyTraps, setWeeklyShowOnlyTraps] = useState<boolean>(false);
  const drillSectionRef = useRef<HTMLDivElement>(null);

  const activeWeekQuestions = useMemo(() => {
    if (!activeDrillWeekId) return [];
    return weeklyExamsMap.get(activeDrillWeekId) || [];
  }, [activeDrillWeekId, weeklyExamsMap]);

  const activeWeekMeta = useMemo(() => {
    if (!activeDrillWeekId) return null;
    return sortedWeeks.find(w => w.id === activeDrillWeekId) || null;
  }, [activeDrillWeekId, sortedWeeks]);

  const handleStartWeeklyDrill = (weekId: string) => {
    setActiveDrillWeekId(weekId);
    setWeeklyShowOnlyTraps(false);
    onSelectWeek?.(weekId as WeekFilterType);
    setTimeout(() => {
      drillSectionRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 50);
  };

  const handleCloseWeeklyDrill = () => {
    setActiveDrillWeekId(null);
    setWeeklyShowOnlyTraps(false);
  };

  const handleSelectWeeklyOption = (qId: string, optionLetter: string) => {
    if (!activeDrillWeekId) return;
    setWeeklyAnswers(prev => {
      const updatedWeek = { ...(prev[activeDrillWeekId] || {}), [qId]: optionLetter };
      const updated = { ...prev, [activeDrillWeekId]: updatedWeek };
      try {
        localStorage.setItem('admission_weekly_user_answers', JSON.stringify(updated));
      } catch {}
      return updated;
    });
    setWeeklyRevealed(prev => ({ ...prev, [qId]: true }));
  };

  const handleResetWeeklyDrill = () => {
    if (!activeDrillWeekId) return;
    setWeeklyAnswers(prev => {
      const updated = { ...prev, [activeDrillWeekId]: {} };
      try {
        localStorage.setItem('admission_weekly_user_answers', JSON.stringify(updated));
      } catch {}
      return updated;
    });
    setWeeklyRevealed({});
    setWeeklyShowOnlyTraps(false);
  };

  const handleRevealAllWeekly = () => {
    const allRev: Record<string, boolean> = {};
    activeWeekQuestions.forEach(q => {
      allRev[q.id] = true;
    });
    setWeeklyRevealed(allRev);
  };

  // Helper to compute stats for a specific week
  const getWeekStats = (weekId: string) => {
    const questions = weeklyExamsMap.get(weekId) || [];
    const answers = weeklyAnswers[weekId] || {};
    let solved = 0;
    let correct = 0;
    let wrong = 0;

    const optionLetters = ['A', 'B', 'C', 'D'];
    questions.forEach(q => {
      const userAns = answers[q.id];
      if (userAns !== undefined) {
        solved++;
        const correctIdx = typeof q.correct_index === 'number' ? q.correct_index : (typeof q.ans === 'number' ? q.ans : 0);
        const correctLetter = optionLetters[correctIdx] || 'A';
        if (userAns === correctLetter) {
          correct++;
        } else {
          wrong++;
        }
      }
    });

    const total = questions.length;
    const accuracy = solved > 0 ? Math.round((correct / solved) * 100) : 0;
    const pendingTraps = Math.max(0, total - correct);
    const solvedPercent = total > 0 ? Math.round((solved / total) * 100) : 0;

    return { solved, correct, wrong, total, accuracy, pendingTraps, solvedPercent };
  };

  // Active drill stats
  const activeDrillStats = useMemo(() => {
    if (!activeDrillWeekId) return { total: 0, solved: 0, correct: 0, wrong: 0, accuracy: 0 };
    const stats = getWeekStats(activeDrillWeekId);
    return {
      total: stats.total,
      solved: stats.solved,
      correct: stats.correct,
      wrong: stats.wrong,
      accuracy: stats.accuracy
    };
  }, [activeDrillWeekId, weeklyAnswers, weeklyExamsMap]);

  // Questions displayed in active weekly speed drill
  const displayedWeeklyQuestions = useMemo(() => {
    if (!weeklyShowOnlyTraps) return activeWeekQuestions;
    const answers = activeDrillWeekId ? (weeklyAnswers[activeDrillWeekId] || {}) : {};
    const optionLetters = ['A', 'B', 'C', 'D'];
    return activeWeekQuestions.filter(q => {
      const ans = answers[q.id];
      if (!ans) return false;
      const correctIdx = typeof q.correct_index === 'number' ? q.correct_index : (typeof q.ans === 'number' ? q.ans : 0);
      return ans !== optionLetters[correctIdx];
    });
  }, [activeWeekQuestions, weeklyShowOnlyTraps, activeDrillWeekId, weeklyAnswers]);

  // Bengali Numerals Converter
  const toBn = (num: number | string) => {
    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)]);
  };

  // Subject themes
  const subjectThemes = {
    'Physics': {
      bg: 'bg-cyan-500/10 text-cyan-700 dark:text-cyan-300 border-cyan-500/30',
      activeBg: 'bg-cyan-600 text-white border-cyan-600 shadow-cyan-500/25',
      badge: 'bg-cyan-50 dark:bg-cyan-950/40 text-cyan-700 dark:text-cyan-300 border-cyan-200 dark:border-cyan-800'
    },
    'Chemistry': {
      bg: 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border-emerald-500/30',
      activeBg: 'bg-emerald-600 text-white border-emerald-600 shadow-emerald-500/25',
      badge: 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800'
    },
    'Higher Math': {
      bg: 'bg-amber-500/10 text-amber-700 dark:text-amber-300 border-amber-500/30',
      activeBg: 'bg-amber-600 text-white border-amber-600 shadow-amber-500/25',
      badge: 'bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 border-amber-200 dark:border-amber-800'
    },
    'Biology': {
      bg: 'bg-rose-500/10 text-rose-700 dark:text-rose-300 border-rose-500/30',
      activeBg: 'bg-rose-600 text-white border-rose-600 shadow-rose-500/25',
      badge: 'bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-800'
    }
  };

  const currentTheme = subjectThemes[selectedSubject];

  return (
    <div className="max-w-6xl mx-auto px-3 sm:px-6 py-4 sm:py-6 space-y-5">
      
      {/* 1. Header Banner */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-slate-900 via-slate-800 to-[#0A1F13] text-white p-5 sm:p-7 shadow-xl border border-slate-700/60">
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
            <Flame className="w-3.5 h-3.5 text-amber-400" />
            <span>মাস্টার কিউবি ডিপ অ্যানালাইসিস ও হাই-ইল্ড ব্লুপ্রিন্ট</span>
          </div>

          <h1 className="text-xl sm:text-3xl font-extrabold tracking-tight text-white flex flex-wrap items-center gap-2">
            <span>মাস্টার কিউবি টাইপ ক্লাস্টার ও প্রেডিক্টর টেস্ট</span>
            <span className="text-xs px-2.5 py-0.5 rounded-md bg-emerald-600 text-white font-mono">
              MAD & VAR
            </span>
          </h1>

          <p className="text-xs sm:text-sm text-slate-300 max-w-3xl leading-relaxed">
            মেডিকেল (MAD) ও ঢাকা বিশ্ববিদ্যালয়সহ ৯টি প্রধান বিশ্ববিদ্যালয় (VAR) এর ২২,৮০৭+ প্রশ্ন অ্যানালাইসিস করে সংকলিত ৪-৬টি মেগা-টাইপ, রিপিটেশন ফ্রিকোয়েন্সি, ৫-সেকেন্ড স্পিড এলিমিনেশন এবং আনসিন ২০টি প্রেডিক্টর টেস্ট।
          </p>

          <div className="flex flex-wrap items-center gap-3 pt-1 text-xs text-slate-300">
            <span className="flex items-center gap-1 bg-slate-800/80 px-2.5 py-1 rounded-md border border-slate-700">
              <Layers className="w-3.5 h-3.5 text-cyan-400" />
              ৩৪টি পূর্ণাঙ্গ অধ্যায়
            </span>
            <span className="flex items-center gap-1 bg-slate-800/80 px-2.5 py-1 rounded-md border border-slate-700">
              <Calendar className="w-3.5 h-3.5 text-amber-400" />
              Week 01 – 08 উইকলি মাস্টারি
            </span>
            <span className="flex items-center gap-1 bg-slate-800/80 px-2.5 py-1 rounded-md border border-slate-700">
              <Zap className="w-3.5 h-3.5 text-emerald-400" />
              ৭৫০টি উইকলি MCQ • ৬৮০টি প্রেডিক্টর
            </span>
          </div>
        </div>
      </div>

      {/* =========================================================================
          2. DUAL WORKFLOW TAB SWITCHER (HIGH-CONTRAST SEGMENTED CONTROL)
          [📂 অধ্যায়-ভিত্তিক ব্লুপ্রিন্ট (৩৪ চ্যাপ্টার)] | [📅 সপ্তাহ-ভিত্তিক মাস্টারি (Week 01 – 08)]
         ========================================================================= */}
      <div className="p-1.5 sm:p-2 rounded-2xl sm:rounded-3xl bg-slate-900/95 dark:bg-black/90 ring-2 ring-emerald-500/50 shadow-xl flex items-center gap-1.5 sm:gap-2">
        <button
          onClick={() => handleWorkflowChange('blueprint')}
          className={`flex-1 py-3 px-3 sm:px-6 rounded-xl sm:rounded-2xl font-black text-xs sm:text-sm transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer active:scale-95 ${
            workflowMode === 'blueprint'
              ? 'bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-700 text-white shadow-lg shadow-emerald-950/60 ring-1 ring-emerald-400/50 scale-[1.01]'
              : 'text-slate-300 hover:text-white hover:bg-slate-800/70'
          }`}
        >
          <span className="text-base sm:text-lg">📂</span>
          <span className="font-extrabold">অধ্যায়-ভিত্তিক ব্লুপ্রিন্ট</span>
          <span className={`text-[10px] sm:text-xs font-mono font-bold px-2 py-0.5 rounded-full ${
            workflowMode === 'blueprint' ? 'bg-white/20 text-white' : 'bg-slate-800 text-slate-300'
          }`}>
            ৩৪ চ্যাপ্টার
          </span>
        </button>

        <button
          onClick={() => handleWorkflowChange('weekly')}
          className={`flex-1 py-3 px-3 sm:px-6 rounded-xl sm:rounded-2xl font-black text-xs sm:text-sm transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer active:scale-95 ${
            workflowMode === 'weekly'
              ? 'bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-700 text-white shadow-lg shadow-emerald-950/60 ring-1 ring-emerald-400/50 scale-[1.01]'
              : 'text-slate-300 hover:text-white hover:bg-slate-800/70'
          }`}
        >
          <span className="text-base sm:text-lg">📅</span>
          <span className="font-extrabold">সপ্তাহ-ভিত্তিক মাস্টারি</span>
          <span className={`text-[10px] sm:text-xs font-mono font-bold px-2 py-0.5 rounded-full ${
            workflowMode === 'weekly' ? 'bg-amber-400/25 text-amber-200' : 'bg-slate-800 text-slate-300'
          }`}>
            Week 01 – 08
          </span>
        </button>
      </div>

      {/* =========================================================================
          WORKFLOW TAB 1: CHAPTER BLUEPRINT (PCMB 34 CHAPTERS + 20 PREDICTOR DRILLS)
         ========================================================================= */}
      {workflowMode === 'blueprint' && (
        <div className="space-y-5 animate-in fade-in duration-150">
          
          {/* PCMB Subject Selector */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            {[
              { key: 'Physics' as const, label: 'পদার্থবিজ্ঞান', sub: '১০টি অধ্যায় • ২০০ MCQ', icon: '⚡' },
              { key: 'Chemistry' as const, label: 'রসায়ন', sub: '৮টি অধ্যায় • ১৬০ MCQ', icon: '🧪' },
              { key: 'Higher Math' as const, label: 'উচ্চতর গণিত', sub: '৮টি অধ্যায় • ১৬০ MCQ', icon: '📐' },
              { key: 'Biology' as const, label: 'জীববিজ্ঞান', sub: '৮টি অধ্যায় • ১৬০ MCQ', icon: '🧬' }
            ].map(item => {
              const isSelected = selectedSubject === item.key;
              const theme = subjectThemes[item.key];
              return (
                <button
                  key={item.key}
                  onClick={() => handleSubjectChange(item.key)}
                  className={`p-3.5 rounded-2xl border text-left transition-all duration-200 flex flex-col justify-between cursor-pointer active:scale-[0.99] ${
                    isSelected
                      ? `${theme.activeBg} shadow-md scale-[1.01]`
                      : 'bg-white dark:bg-[#141E18] text-slate-700 dark:text-slate-200 border-slate-200 dark:border-[#223528] hover:border-slate-300 dark:hover:border-slate-600'
                  }`}
                >
                  <div className="flex items-center justify-between w-full">
                    <span className="text-xl">{item.icon}</span>
                    {isSelected && (
                      <CheckCircle2 className="w-4 h-4 text-white" />
                    )}
                  </div>
                  <div className="mt-2">
                    <div className={`font-bold text-sm sm:text-base ${isSelected ? 'text-white' : 'text-slate-900 dark:text-white'}`}>
                      {item.label}
                    </div>
                    <div className={`text-[11px] font-mono mt-0.5 ${isSelected ? 'text-white/80' : 'text-slate-500 dark:text-slate-400'}`}>
                      {item.sub}
                    </div>
                  </div>
                </button>
              );
            })}
          </div>

          {/* Horizontal Chapter Pills */}
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-1 font-medium">
              <span>অধ্যায় নির্বাচন করুন ({toBn(currentSubjectChapters.length)}টি অধ্যায়):</span>
              <span className="font-mono text-[11px]">
                {activeChapter?.paper || '১ম ও ২য় পত্র'}
              </span>
            </div>

            <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-thin scrollbar-thumb-slate-300 dark:scrollbar-thumb-slate-700">
              {currentSubjectChapters.map(ch => {
                const isSelected = ch.id === selectedChapterId;
                return (
                  <button
                    key={ch.id}
                    onClick={() => setSelectedChapterId(ch.id)}
                    className={`flex-shrink-0 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all border cursor-pointer ${
                      isSelected
                        ? 'bg-slate-900 dark:bg-emerald-600 text-white border-slate-900 dark:border-emerald-600 shadow-sm'
                        : 'bg-white dark:bg-[#141E18] text-slate-700 dark:text-slate-300 border-slate-200 dark:border-[#223528] hover:bg-slate-50 dark:hover:bg-[#1A261F]'
                    }`}
                  >
                    <div className="flex items-center gap-1.5">
                      <span>{ch.title.split('(')[0].trim()}</span>
                      <span className={`text-[10px] px-1.5 py-0.2 rounded-md ${
                        isSelected ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-[#1F2C24] text-slate-500 dark:text-slate-400'
                      }`}>
                        {toBn(ch.mega_types.length)}টি টাইপ
                      </span>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Active Chapter Overview Card & Section Switcher */}
          {activeChapter && (
            <div className="bg-white dark:bg-[#101A14] rounded-3xl border border-slate-200 dark:border-[#1E2D22] p-4 sm:p-6 shadow-sm space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 dark:border-[#1A291E] pb-4">
                <div>
                  <div className="flex items-center gap-2">
                    <span className={`text-xs px-2 py-0.5 rounded font-bold uppercase tracking-wider ${currentTheme.badge}`}>
                      {activeChapter.subject} • {activeChapter.paper}
                    </span>
                    <span className="text-xs text-slate-500 dark:text-slate-400 font-mono">
                      {toBn(activePredictors.length)} প্রেডিক্টর MCQ
                    </span>
                  </div>
                  <h2 className="text-lg sm:text-2xl font-black text-slate-900 dark:text-white mt-1">
                    {activeChapter.title}
                  </h2>
                </div>

                {/* Tab Buttons */}
                <div className="flex items-center bg-slate-100 dark:bg-[#18241D] p-1 rounded-xl self-start sm:self-auto">
                  <button
                    onClick={() => setActiveTab('blueprint')}
                    className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                      activeTab === 'blueprint'
                        ? 'bg-white dark:bg-[#23352A] text-slate-900 dark:text-white shadow-sm'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                    }`}
                  >
                    <Layers className="w-3.5 h-3.5 text-cyan-500" />
                    <span>মাস্টার কিউবি টাইপ ও রিপিট</span>
                  </button>
                  <button
                    onClick={() => setActiveTab('quiz')}
                    className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                      activeTab === 'quiz'
                        ? 'bg-emerald-600 text-white shadow-sm'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                    }`}
                  >
                    <Zap className="w-3.5 h-3.5 text-amber-300" />
                    <span>স্পেশাল ২০টি নমুনা টেস্ট</span>
                  </button>
                </div>
              </div>

              {/* Section 1: MASTER QB TYPE & REPEAT REFERENCE */}
              {activeTab === 'blueprint' && (
                <div className="space-y-4 pt-1">
                  <div className="flex items-center justify-between">
                    <div className="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                      <Star className="w-4 h-4 text-amber-500 fill-amber-500" />
                      <span>ক্লাস্টার্ড ডমিন্যান্ট মেগা-টাইপস ({toBn(activeChapter.mega_types.length)}টি টাইপ):</span>
                    </div>
                    <div className="flex items-center gap-2 text-xs">
                      <button
                        onClick={expandAllTypes}
                        className="text-slate-500 hover:text-emerald-600 dark:text-slate-400 dark:hover:text-emerald-400 font-medium cursor-pointer"
                      >
                        সব খুলুন
                      </button>
                      <span className="text-slate-300 dark:text-slate-700">|</span>
                      <button
                        onClick={collapseAllTypes}
                        className="text-slate-500 hover:text-emerald-600 dark:text-slate-400 dark:hover:text-emerald-400 font-medium cursor-pointer"
                      >
                        সব বন্ধ
                      </button>
                    </div>
                  </div>

                  <div className="space-y-3">
                    {activeChapter.mega_types.map((typeItem, idx) => {
                      const isExpanded = expandedTypes[typeItem.type_id] !== false;
                      const isFiveStar = typeItem.importance === '⭐⭐⭐⭐⭐';

                      return (
                        <div 
                          key={typeItem.type_id}
                          className={`rounded-2xl border transition-all duration-200 overflow-hidden ${
                            isFiveStar
                              ? 'border-amber-300/80 dark:border-amber-800/60 bg-gradient-to-r from-amber-500/5 via-transparent to-transparent dark:bg-amber-950/10'
                              : 'border-slate-200 dark:border-[#223528] bg-white dark:bg-[#131E17]'
                          }`}
                        >
                          <button
                            onClick={() => toggleTypeExpand(typeItem.type_id)}
                            className="w-full p-3.5 sm:p-4 text-left flex items-start sm:items-center justify-between gap-3 hover:bg-slate-50/80 dark:hover:bg-[#17251C] transition-colors cursor-pointer"
                          >
                            <div className="space-y-1.5 flex-1">
                              <div className="flex flex-wrap items-center gap-2">
                                <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-[#1F2F23] text-slate-700 dark:text-slate-300">
                                  #{toBn(idx + 1)}
                                </span>

                                <span className={`text-xs px-2 py-0.5 rounded-full font-bold flex items-center gap-1 ${
                                  isFiveStar
                                    ? 'bg-amber-500/15 text-amber-700 dark:text-amber-300 border border-amber-500/30'
                                    : 'bg-blue-500/15 text-blue-700 dark:text-blue-300 border border-blue-500/30'
                                }`}>
                                  {typeItem.stars}
                                  <span>({toBn(typeItem.repeat_frequency)}+ বার রিপিট)</span>
                                </span>

                                <div className="flex flex-wrap items-center gap-1">
                                  {typeItem.past_tags.map(tag => (
                                    <span 
                                      key={tag}
                                      className="text-[10px] font-mono font-semibold px-1.5 py-0.2 rounded bg-slate-100 dark:bg-[#1D2B21] text-slate-600 dark:text-slate-300"
                                    >
                                      {tag}
                                    </span>
                                  ))}
                                </div>
                              </div>

                              <h3 className="font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-1.5">
                                <MathText text={typeItem.name} />
                              </h3>
                            </div>

                            <div className="text-slate-400 p-1 rounded-md hover:bg-slate-200/60 dark:hover:bg-[#203125]">
                              {isExpanded ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
                            </div>
                          </button>

                          {isExpanded && (
                            <div className="p-3.5 sm:p-4 pt-0 border-t border-slate-100 dark:border-[#1E2E23] space-y-3 bg-slate-50/50 dark:bg-[#111A14]">
                              <div className="space-y-1.5 pt-2">
                                <div className="text-[11px] font-semibold text-slate-500 dark:text-slate-400 flex items-center gap-1">
                                  <Hash className="w-3 h-3 text-cyan-500" />
                                  <span>মাস্টার কিউবি এক্স্যাক্ট প্রশ্ন নম্বর রেফারেন্স:</span>
                                </div>
                                <div className="flex flex-wrap gap-1.5">
                                  {typeItem.qb_question_refs.map(ref => (
                                    <span 
                                      key={ref}
                                      className="text-[10px] font-mono font-bold px-2 py-0.5 rounded-md bg-white dark:bg-[#19271E] text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-[#273B2E] shadow-2xs"
                                    >
                                      {ref}
                                    </span>
                                  ))}
                                </div>
                              </div>

                              <div className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/25 space-y-1">
                                <div className="text-[11px] font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1.5">
                                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                                  <span>কোর রুল ও ফান্ডামেন্টাল সূত্র (Core Rule):</span>
                                </div>
                                <div className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed pl-5 font-medium">
                                  <MathText text={typeItem.core_rule} />
                                </div>
                              </div>

                              <div className="p-3 rounded-xl bg-amber-500/10 border border-amber-500/25 space-y-1">
                                <div className="text-[11px] font-bold text-amber-800 dark:text-amber-300 flex items-center gap-1.5">
                                  <Zap className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400 fill-amber-500" />
                                  <span>৫-সেকেন্ড স্পিড এলিমিনেশন ট্রিক (Speed Elimination):</span>
                                </div>
                                <div className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed pl-5 font-medium">
                                  <MathText text={typeItem.speed_elimination} />
                                </div>
                              </div>
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}

              {/* Section 2: SPECIAL 20 SYNTHETIC PREDICTORS QUIZ */}
              {activeTab === 'quiz' && (
                <div className="space-y-4 pt-1">
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-3.5 rounded-2xl bg-slate-50 dark:bg-[#16231A] border border-slate-200 dark:border-[#24372A]">
                    <div className="flex items-center gap-4 text-xs font-semibold">
                      <div>
                        <span className="text-slate-500 dark:text-slate-400">মোট প্রশ্ন: </span>
                        <span className="font-bold text-slate-900 dark:text-white font-mono">{toBn(scoreStats.total)}</span>
                      </div>
                      <div>
                        <span className="text-slate-500 dark:text-slate-400">উত্তর সম্পন্ন: </span>
                        <span className="font-bold text-blue-600 dark:text-blue-400 font-mono">{toBn(scoreStats.answered)}</span>
                      </div>
                      <div>
                        <span className="text-slate-500 dark:text-slate-400">সঠিক: </span>
                        <span className="font-bold text-emerald-600 dark:text-emerald-400 font-mono">{toBn(scoreStats.correct)}</span>
                      </div>
                      <div>
                        <span className="text-slate-500 dark:text-slate-400">ভুল: </span>
                        <span className="font-bold text-rose-600 dark:text-rose-400 font-mono">{toBn(scoreStats.wrong)}</span>
                      </div>
                      {scoreStats.answered > 0 && (
                        <div className="hidden sm:block">
                          <span className="text-slate-500 dark:text-slate-400">সঠিকতার হার: </span>
                          <span className="font-bold text-emerald-600 font-mono">{toBn(scoreStats.accuracy)}%</span>
                        </div>
                      )}
                    </div>

                    <div className="flex items-center gap-2 text-xs">
                      {scoreStats.wrong > 0 && (
                        <button
                          onClick={() => setShowOnlyTraps(!showOnlyTraps)}
                          className={`px-2.5 py-1 rounded-md font-semibold transition-all border cursor-pointer ${
                            showOnlyTraps
                              ? 'bg-rose-600 text-white border-rose-600'
                              : 'bg-white dark:bg-[#1D2B21] text-rose-600 dark:text-rose-400 border-rose-200 dark:border-rose-900/50 hover:bg-rose-50'
                          }`}
                        >
                          ভুল ট্র্যাপগুলো দেখো ({toBn(scoreStats.wrong)})
                        </button>
                      )}
                      <button
                        onClick={handleRevealAll}
                        className="px-2.5 py-1 rounded-md font-medium text-slate-600 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 cursor-pointer"
                      >
                        সব ব্যাখ্যা আনলক
                      </button>
                      <button
                        onClick={handleResetQuiz}
                        className="p-1 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer"
                        title="রিসেট টেস্ট"
                      >
                        <RotateCcw className="w-4 h-4" />
                      </button>
                    </div>
                  </div>

                  <div className="space-y-4">
                    {displayedPredictors.map((q, qIndex) => {
                      const userAnswer = userAnswers[q.id];
                      const isRevealed = revealedQuestions[q.id] || !!userAnswer;
                      const isAnswered = !!userAnswer;
                      const isCorrect = userAnswer === q.answer;

                      return (
                        <div
                          key={q.id}
                          className={`p-4 sm:p-5 rounded-2xl border transition-all duration-200 space-y-3 ${
                            isAnswered
                              ? isCorrect
                                ? 'bg-emerald-500/5 border-emerald-500/30'
                                : 'bg-rose-500/5 border-rose-500/30'
                              : 'bg-white dark:bg-[#141E18] border-slate-200 dark:border-[#223528]'
                          }`}
                        >
                          <div className="flex flex-wrap items-center justify-between gap-2">
                            <div className="flex items-center gap-2">
                              <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-[#1D2B21] text-slate-700 dark:text-slate-300">
                                Q{toBn(qIndex + 1)}
                              </span>
                              <span className="text-xs px-2 py-0.5 rounded font-semibold bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border border-emerald-500/20">
                                {q.type_ref}
                              </span>
                            </div>

                            <span className="text-[10px] font-mono text-slate-400">
                              {q.id}
                            </span>
                          </div>

                          <div className="text-sm sm:text-base font-medium text-slate-900 dark:text-white leading-relaxed">
                            <MathText text={q.stem} />
                          </div>

                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                            {q.options.map((optionText, optIdx) => {
                              const optionLetters = ['A', 'B', 'C', 'D'];
                              const currentLetter = optionLetters[optIdx];
                              const isOptionSelected = userAnswer === currentLetter;
                              const isOptionCorrect = q.answer === currentLetter;

                              let optionStyle = 'bg-white dark:bg-[#17241C] border-slate-200 dark:border-[#263A2D] text-slate-800 dark:text-slate-200 hover:border-slate-300 dark:hover:border-slate-500';

                              if (isRevealed) {
                                if (isOptionCorrect) {
                                  optionStyle = 'bg-emerald-600 text-white border-emerald-600 shadow-sm font-semibold';
                                } else if (isOptionSelected) {
                                  optionStyle = 'bg-rose-600 text-white border-rose-600 shadow-sm font-semibold';
                                } else {
                                  optionStyle = 'bg-slate-100/60 dark:bg-[#141E18]/60 text-slate-400 border-slate-200/60 dark:border-slate-800 line-through opacity-70';
                                }
                              } else if (isOptionSelected) {
                                optionStyle = 'bg-slate-900 text-white border-slate-900 dark:bg-emerald-600';
                              }

                              return (
                                <button
                                  key={optIdx}
                                  onClick={() => handleSelectOption(q.id, currentLetter)}
                                  className={`p-3 rounded-xl border text-left text-xs sm:text-sm transition-all flex items-start gap-2.5 cursor-pointer ${optionStyle}`}
                                >
                                  <span className={`w-5 h-5 flex-shrink-0 flex items-center justify-center rounded-md font-mono text-xs font-bold ${
                                    isRevealed && isOptionCorrect
                                      ? 'bg-white/20 text-white'
                                      : isOptionSelected
                                      ? 'bg-white/20 text-white'
                                      : 'bg-slate-100 dark:bg-[#203024] text-slate-600 dark:text-slate-300'
                                  }`}>
                                    {currentLetter}
                                  </span>
                                  <div className="flex-1 leading-snug">
                                    <MathText text={optionText} />
                                  </div>
                                </button>
                              );
                            })}
                          </div>

                          {isRevealed && (
                            <div className="pt-2 space-y-2 border-t border-slate-100 dark:border-[#1E2E23]">
                              <div className="p-3 rounded-xl bg-rose-500/10 border border-rose-500/25 space-y-1">
                                <div className="text-[11px] font-bold text-rose-800 dark:text-rose-300 flex items-center gap-1.5">
                                  <ShieldAlert className="w-3.5 h-3.5 text-rose-600 dark:text-rose-400" />
                                  <span>সাধারণ ছাত্রভ্রান্তি ও ফাঁদ (Trap Alert):</span>
                                </div>
                                <div className="text-xs text-slate-800 dark:text-slate-200 pl-5 font-medium">
                                  <MathText text={q.trap_alert} />
                                </div>
                              </div>

                              <div className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/25 space-y-1">
                                <div className="text-[11px] font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1.5">
                                  <Zap className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 fill-emerald-500" />
                                  <span>৫-সেকেন্ড স্পিড হ্যাক / অপশন এলিমিনেশন (Speed Hack):</span>
                                </div>
                                <div className="text-xs text-slate-800 dark:text-slate-200 pl-5 font-medium">
                                  <MathText text={q.speed_hack} />
                                </div>
                              </div>

                              {q.explanation && (
                                <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-[#16221A] text-xs text-slate-600 dark:text-slate-300 space-y-1">
                                  <span className="font-bold text-slate-700 dark:text-slate-200">ব্যাখ্যা: </span>
                                  <MathText text={q.explanation} />
                                </div>
                              )}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* =========================================================================
          WORKFLOW TAB 2: WEEKLY MASTERY (WEEK 01 – 07 DEDICATED CARDS & SPEED DRILLS)
         ========================================================================= */}
      {workflowMode === 'weekly' && (
        <div className="space-y-5 animate-in fade-in duration-150">
          
          {/* Subheader Information Banner */}
          <div className="rounded-3xl p-4 sm:p-5 bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800/80 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <div className="flex items-center gap-2 mb-1">
                <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/30 flex items-center gap-1">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping" />
                  সপ্তাহ-ভিত্তিক মাস্টারি রুটিন
                </span>
                <span className="text-[11px] font-mono text-slate-500 dark:text-slate-400">
                  Week 01 – 08 • ৭৫০টি হাই-ইল্ড MCQ
                </span>
              </div>
              <h2 className="text-base sm:text-lg font-black text-slate-900 dark:text-white">
                ৭ সপ্তাহের কমপ্লিট সিলেবাস ট্র্যাপ ডিফেন্স ও উইকলি স্পিড ড্রিল
              </h2>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-0.5">
                প্রতিটি সপ্তাহের কভার্ড অধ্যায়সমূহ রিভিশন দিন, পেন্ডিং ট্র্যাপ চেক করুন এবং সরাসরি উইকলি স্পিড ড্রিল শুরু করুন।
              </p>
            </div>

            <div className="flex items-center gap-2 self-start sm:self-auto shrink-0">
              <span className="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold text-slate-700 dark:text-slate-300 ring-1 ring-slate-200/70 dark:ring-slate-700 font-mono">
                ৭টি সপ্তাহ • ৭৫০ ট্র্যাপ
              </span>
            </div>
          </div>

          {/* ACTIVE WEEKLY SPEED DRILL CONTAINER (Shown when a week is selected) */}
          {activeDrillWeekId && (
            <div ref={drillSectionRef} className="rounded-3xl bg-white dark:bg-[#101A14] border-2 border-emerald-500/40 p-4 sm:p-6 shadow-xl space-y-4">
              {/* Drill Header */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 dark:border-[#1E2E23] pb-4">
                <div>
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="text-xs font-black px-2.5 py-0.5 rounded-full bg-emerald-600 text-white font-mono shadow-xs">
                      {activeWeekMeta?.name || activeDrillWeekId.toUpperCase()}
                    </span>
                    <span className="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border border-emerald-500/30">
                      ⚡ উইকলি স্পিড ড্রিল
                    </span>
                    <span className="text-xs font-mono text-slate-500 dark:text-slate-400">
                      {toBn(activeWeekQuestions.length)}টি প্রশ্ন
                    </span>
                  </div>
                  <h3 className="text-lg sm:text-xl font-black text-slate-900 dark:text-white mt-1.5 flex items-center gap-2">
                    <span>{WEEK_COVERED_CHAPTERS[activeDrillWeekId]?.badgeText || activeWeekMeta?.badge || 'উইকলি রিভিশন'}</span>
                  </h3>
                </div>

                <div className="flex items-center gap-2 self-start sm:self-auto shrink-0 flex-wrap">
                  {onSelectMode && onSelectWeek && (
                    <button
                      onClick={() => {
                        onSelectWeek(activeDrillWeekId as WeekFilterType);
                        onSelectSubject?.('All');
                        onSelectMode('exam');
                      }}
                      className="px-3.5 py-2 rounded-xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold shadow-xs transition-all flex items-center gap-1.5 cursor-pointer active:scale-95"
                      title="ফুল-স্ক্রিন টাইমড মক টেস্ট দিন"
                    >
                      <Clock className="w-3.5 h-3.5" />
                      <span>টাইমড এক্সামে যান</span>
                    </button>
                  )}
                  <button
                    onClick={handleCloseWeeklyDrill}
                    className="px-3.5 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold transition-all flex items-center gap-1 cursor-pointer active:scale-95"
                  >
                    <ArrowLeft className="w-3.5 h-3.5" />
                    <span>উইক তালিকায় ফিরুন</span>
                  </button>
                </div>
              </div>

              {/* Score & Controls Bar */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-3.5 rounded-2xl bg-slate-50 dark:bg-[#16231A] border border-slate-200 dark:border-[#24372A]">
                <div className="flex items-center gap-4 text-xs font-semibold flex-wrap">
                  <div>
                    <span className="text-slate-500 dark:text-slate-400">মোট প্রশ্ন: </span>
                    <span className="font-bold text-slate-900 dark:text-white font-mono">{toBn(activeDrillStats.total)}</span>
                  </div>
                  <div>
                    <span className="text-slate-500 dark:text-slate-400">উত্তর সম্পন্ন: </span>
                    <span className="font-bold text-blue-600 dark:text-blue-400 font-mono">{toBn(activeDrillStats.solved)}</span>
                  </div>
                  <div>
                    <span className="text-slate-500 dark:text-slate-400">সঠিক: </span>
                    <span className="font-bold text-emerald-600 dark:text-emerald-400 font-mono">{toBn(activeDrillStats.correct)}</span>
                  </div>
                  <div>
                    <span className="text-slate-500 dark:text-slate-400">ভুল: </span>
                    <span className="font-bold text-rose-600 dark:text-rose-400 font-mono">{toBn(activeDrillStats.wrong)}</span>
                  </div>
                  {activeDrillStats.solved > 0 && (
                    <div>
                      <span className="text-slate-500 dark:text-slate-400">সঠিকতার হার: </span>
                      <span className="font-bold text-emerald-600 font-mono">{toBn(activeDrillStats.accuracy)}%</span>
                    </div>
                  )}
                </div>

                <div className="flex items-center gap-2 text-xs flex-wrap">
                  {activeDrillStats.wrong > 0 && (
                    <button
                      onClick={() => setWeeklyShowOnlyTraps(!weeklyShowOnlyTraps)}
                      className={`px-2.5 py-1 rounded-lg font-semibold transition-all border cursor-pointer ${
                        weeklyShowOnlyTraps
                          ? 'bg-rose-600 text-white border-rose-600'
                          : 'bg-white dark:bg-[#1D2B21] text-rose-600 dark:text-rose-400 border-rose-200 dark:border-rose-900/50 hover:bg-rose-50'
                      }`}
                    >
                      ভুল ট্র্যাপগুলো দেখো ({toBn(activeDrillStats.wrong)})
                    </button>
                  )}
                  <button
                    onClick={handleRevealAllWeekly}
                    className="px-2.5 py-1 rounded-lg font-medium text-slate-600 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 cursor-pointer"
                  >
                    সব ব্যাখ্যা আনলক
                  </button>
                  <button
                    onClick={handleResetWeeklyDrill}
                    className="p-1 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer"
                    title="রিসেট টেস্ট"
                  >
                    <RotateCcw className="w-4 h-4" />
                  </button>
                </div>
              </div>

              {/* Weekly Questions List */}
              <div className="space-y-4">
                {displayedWeeklyQuestions.map((q, qIndex) => {
                  const normStem = (q.q || q.question || '').replace(/^\[(.*?)\]\s*/, '');
                  const origin = q.origin || (q.q || '').match(/^\[(.*?)\]/)?.[1] || 'DU Core';
                  const options: string[] = q.options || q.opts || [];
                  const correctIdx: number = typeof q.correct_index === 'number' ? q.correct_index : (typeof q.ans === 'number' ? q.ans : 0);
                  const optionLetters = ['A', 'B', 'C', 'D'];
                  const correctLetter = optionLetters[correctIdx] || 'A';
                  const userAnswer = activeDrillWeekId ? weeklyAnswers[activeDrillWeekId]?.[q.id] : undefined;
                  const isRevealed = weeklyRevealed[q.id] || !!userAnswer;
                  const isAnswered = !!userAnswer;
                  const isCorrect = userAnswer === correctLetter;
                  const trapAlert = q.trap_alert || q.trap_insight || q.trap || '';
                  const speedHack = q.speed_hack || '';
                  const explanation = q.explanation || q.exp || '';

                  return (
                    <div
                      key={q.id}
                      className={`p-4 sm:p-5 rounded-2xl border transition-all duration-200 space-y-3.5 ${
                        isAnswered
                          ? isCorrect
                            ? 'bg-emerald-500/5 border-emerald-500/30'
                            : 'bg-rose-500/5 border-rose-500/30'
                          : 'bg-white dark:bg-[#141E18] border-slate-200 dark:border-[#223528]'
                      }`}
                    >
                      <div className="flex flex-wrap items-center justify-between gap-2">
                        <div className="flex items-center gap-2 flex-wrap">
                          <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-[#1D2B21] text-slate-700 dark:text-slate-300">
                            Q{toBn(qIndex + 1)}
                          </span>
                          <span className="text-xs px-2.5 py-0.5 rounded-full font-bold bg-blue-500/10 text-blue-700 dark:text-blue-300 border border-blue-500/25">
                            {origin}
                          </span>
                          {q.chapter && (
                            <span className="text-xs px-2 py-0.5 rounded font-semibold bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border border-emerald-500/20">
                              {q.chapter}
                            </span>
                          )}
                        </div>
                        <span className="text-[10px] font-mono text-slate-400">
                          {q.id}
                        </span>
                      </div>

                      <div className="text-sm sm:text-base font-semibold text-slate-900 dark:text-white leading-relaxed">
                        <MathText text={normStem} />
                      </div>

                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                        {options.map((optText, optIdx) => {
                          const letter = optionLetters[optIdx];
                          const isSelected = userAnswer === letter;
                          const isThisCorrect = correctLetter === letter;

                          let optionStyle = 'bg-white dark:bg-[#17241C] border-slate-200 dark:border-[#263A2D] text-slate-800 dark:text-slate-200 hover:border-slate-300 dark:hover:border-slate-500';

                          if (isRevealed) {
                            if (isThisCorrect) {
                              optionStyle = 'bg-emerald-600 text-white border-emerald-600 shadow-sm font-semibold';
                            } else if (isSelected) {
                              optionStyle = 'bg-rose-600 text-white border-rose-600 shadow-sm font-semibold';
                            } else {
                              optionStyle = 'bg-slate-100/60 dark:bg-[#141E18]/60 text-slate-400 border-slate-200/60 dark:border-slate-800 line-through opacity-70';
                            }
                          } else if (isSelected) {
                            optionStyle = 'bg-slate-900 text-white border-slate-900 dark:bg-emerald-600';
                          }

                          return (
                            <button
                              key={optIdx}
                              onClick={() => handleSelectWeeklyOption(q.id, letter)}
                              className={`p-3 rounded-xl border text-left text-xs sm:text-sm transition-all flex items-start gap-2.5 cursor-pointer ${optionStyle}`}
                            >
                              <span className={`w-5 h-5 flex-shrink-0 flex items-center justify-center rounded-md font-mono text-xs font-bold ${
                                isRevealed && isThisCorrect
                                  ? 'bg-white/20 text-white'
                                  : isSelected
                                  ? 'bg-white/20 text-white'
                                  : 'bg-slate-100 dark:bg-[#203024] text-slate-600 dark:text-slate-300'
                              }`}>
                                {letter}
                              </span>
                              <div className="flex-1 leading-snug">
                                <MathText text={optText} />
                              </div>
                            </button>
                          );
                        })}
                      </div>

                      {isRevealed && (
                        <div className="pt-2 space-y-2.5 border-t border-slate-100 dark:border-[#1E2E23]">
                          {trapAlert && (
                            <div className="p-3 rounded-xl bg-rose-500/10 border border-rose-500/25 space-y-1">
                              <div className="text-[11px] font-bold text-rose-800 dark:text-rose-300 flex items-center gap-1.5">
                                <ShieldAlert className="w-3.5 h-3.5 text-rose-600 dark:text-rose-400" />
                                <span>সাধারণ ছাত্রভ্রান্তি ও ফাঁদ (Trap Alert):</span>
                              </div>
                              <div className="text-xs text-slate-800 dark:text-slate-200 pl-5 font-medium leading-relaxed">
                                <MathText text={trapAlert} />
                              </div>
                            </div>
                          )}

                          {speedHack && (
                            <div className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/25 space-y-1">
                              <div className="text-[11px] font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1.5">
                                <Zap className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 fill-emerald-500" />
                                <span>৫-সেকেন্ড স্পিড হ্যাক / অপশন এলিমিনেশন (Speed Hack):</span>
                              </div>
                              <div className="text-xs text-slate-800 dark:text-slate-200 pl-5 font-medium leading-relaxed">
                                <MathText text={speedHack} />
                              </div>
                            </div>
                          )}

                          {explanation && (
                            <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-[#16221A] text-xs text-slate-600 dark:text-slate-300 space-y-1">
                              <span className="font-bold text-slate-700 dark:text-slate-200">ব্যাখ্যা: </span>
                              <MathText text={explanation} />
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          {/* DEDICATED 7-WEEK CARDS GRID (Week 01 – Week 08) */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {sortedWeeks.map((week, wIdx) => {
              const weekInfo = WEEK_COVERED_CHAPTERS[week.id] || {
                badgeText: week.badge || 'উইকলি কোর সিলেবাস',
                chaptersText: week.description || ''
              };
              const stats = getWeekStats(week.id);
              const isActive = activeDrillWeekId === week.id;

              const weekIcons = ['🎯', '⚡', '🔬', '⚛️', '🧪', '📐', '🧬'];
              const icon = weekIcons[wIdx % weekIcons.length];

              return (
                <div
                  key={week.id}
                  className={`rounded-3xl p-5 border transition-all duration-200 flex flex-col justify-between space-y-4 ${
                    isActive
                      ? 'bg-emerald-500/10 border-emerald-500 shadow-md ring-2 ring-emerald-500/30'
                      : 'bg-white dark:bg-[#121B15] border-slate-200/90 dark:border-[#1E2E23] hover:border-emerald-500/60 dark:hover:border-emerald-500/60 shadow-sm'
                  }`}
                >
                  <div className="space-y-3">
                    {/* Week Top Badge Row */}
                    <div className="flex items-center justify-between gap-2">
                      <div className="flex items-center gap-2">
                        <span className="text-xl">{icon}</span>
                        <span className="text-sm font-black text-slate-900 dark:text-white font-mono uppercase tracking-wide">
                          {week.name}
                        </span>
                      </div>
                      <span className="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-slate-100 dark:bg-[#1C2A20] text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                        {toBn(stats.total)}টি MCQ
                      </span>
                    </div>

                    {/* Prominent Covered Chapters Tag */}
                    <div className="p-3 rounded-2xl bg-emerald-500/10 dark:bg-emerald-950/30 border border-emerald-500/25 space-y-1">
                      <div className="text-[11px] font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1.5">
                        <BookOpen className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                        <span>কভার্ড অধ্যায়সমূহ (Covered Chapters):</span>
                      </div>
                      <div className="text-xs font-bold text-slate-800 dark:text-slate-100 leading-snug">
                        {weekInfo.badgeText}
                      </div>
                    </div>

                    {/* Stats Metric Box: Solved Status, Accuracy %, Pending Trap Count */}
                    <div className="grid grid-cols-3 gap-2 pt-1">
                      {/* Solved Status */}
                      <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-[#18231C] border border-slate-200/80 dark:border-[#243529] text-center">
                        <div className="text-[10px] font-semibold text-slate-500 dark:text-slate-400">সমাধান</div>
                        <div className="text-xs sm:text-sm font-black text-slate-900 dark:text-white mt-0.5 font-mono">
                          {toBn(stats.solved)}/{toBn(stats.total)}
                        </div>
                        <div className="text-[9px] font-bold text-emerald-600 dark:text-emerald-400 font-mono">
                          {toBn(stats.solvedPercent)}%
                        </div>
                      </div>

                      {/* Accuracy % */}
                      <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-[#18231C] border border-slate-200/80 dark:border-[#243529] text-center">
                        <div className="text-[10px] font-semibold text-slate-500 dark:text-slate-400">সঠিকতা</div>
                        <div className={`text-xs sm:text-sm font-black mt-0.5 font-mono ${
                          stats.solved === 0
                            ? 'text-slate-400'
                            : stats.accuracy >= 80
                            ? 'text-emerald-600 dark:text-emerald-400'
                            : stats.accuracy >= 60
                            ? 'text-amber-500'
                            : 'text-rose-500'
                        }`}>
                          {stats.solved > 0 ? `${toBn(stats.accuracy)}%` : '--'}
                        </div>
                        <div className="text-[9px] text-slate-400">
                          {stats.solved > 0 ? 'নিখুঁত' : 'বাকি'}
                        </div>
                      </div>

                      {/* Pending Trap Count */}
                      <div className="p-2.5 rounded-xl bg-rose-500/10 dark:bg-rose-950/20 border border-rose-500/25 text-center">
                        <div className="text-[10px] font-semibold text-rose-700 dark:text-rose-300">পেন্ডিং ট্র্যাপ</div>
                        <div className="text-xs sm:text-sm font-black text-rose-600 dark:text-rose-400 mt-0.5 font-mono">
                          {toBn(stats.pendingTraps)}টি
                        </div>
                        <div className="text-[9px] font-bold text-rose-600 dark:text-rose-400">
                          বাকি আছে
                        </div>
                      </div>
                    </div>

                    {/* Progress Bar */}
                    <div className="w-full bg-slate-100 dark:bg-[#1E2B22] rounded-full h-1.5 overflow-hidden">
                      <div 
                        className="bg-gradient-to-r from-emerald-600 to-teal-500 h-1.5 rounded-full transition-all duration-300"
                        style={{ width: `${stats.solvedPercent}%` }}
                      />
                    </div>
                  </div>

                  {/* Direct Action Button: [⚡ উইকলি স্পিড ড্রিল শুরু করুন] */}
                  <div className="pt-2">
                    <button
                      onClick={() => handleStartWeeklyDrill(week.id)}
                      className={`w-full py-2.5 px-4 rounded-xl font-black text-xs sm:text-sm shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer active:scale-95 ${
                        isActive
                          ? 'bg-emerald-700 text-white shadow-emerald-900/40 ring-1 ring-emerald-400/50'
                          : 'bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-700 hover:from-emerald-500 hover:to-teal-600 text-white shadow-emerald-900/30'
                      }`}
                    >
                      <Zap className="w-4 h-4 text-amber-300 fill-amber-300" />
                      <span>⚡ উইকলি স্পিড ড্রিল শুরু করুন</span>
                    </button>
                  </div>
                </div>
              );
            })}
          </div>

        </div>
      )}

    </div>
  );
};

export default ChapterBlueprintView;
