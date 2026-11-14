import React, { useState, useMemo } from 'react';
import { 
  Sparkles, 
  Award, 
  Timer, 
  CheckCircle2, 
  XCircle, 
  AlertTriangle, 
  ChevronRight, 
  Layers,
  FileText
} from 'lucide-react';
import confetti from 'canvas-confetti';
import type { QuizQuestion, TrackType, SubjectType, PredictorSet } from '../types';
import { MathText } from './MathText';

interface PredictorViewProps {
  activeTrack: TrackType;
  questions: QuizQuestion[];
  predictorSets: PredictorSet[];
  onSelectTrack?: (track: TrackType) => void;
}

export const PredictorView: React.FC<PredictorViewProps> = ({
  activeTrack,
  questions,
  predictorSets,
}) => {
  // Sets filtered by track
  const currentSets = useMemo(() => {
    return predictorSets.filter((s) => (s.track || '').toLowerCase() === activeTrack.toLowerCase());
  }, [predictorSets, activeTrack]);

  // Weekly Prediction Slot Tabs State: 'week_01' | 'week_02' | 'week_03' | 'week_04' | 'week_05' | 'week_06' | 'week_07' | 'sets'
  const [activeTab, setActiveTab] = useState<'weekly' | 'sets'>('weekly');
  const [selectedWeekTab, setSelectedWeekTab] = useState<'week_01' | 'week_02' | 'week_03' | 'week_04' | 'week_05' | 'week_06' | 'week_07' | 'week_08'>('week_08');
  const [currentSlotIndex, setCurrentSlotIndex] = useState<number>(0);
  const pageSize = 12; // 10 to 15 questions per slot page

  // Star Filter & Subject Filter
  const [selectedStar, setSelectedStar] = useState<number | 'all'>('all');
  const [selectedSubject, setSelectedSubject] = useState<SubjectType>('All');

  // Reset slot pagination on filter or tab change
  React.useEffect(() => {
    setCurrentSlotIndex(0);
  }, [selectedWeekTab, selectedStar, selectedSubject, activeTrack, activeTab]);

  // Bengali numerals converter
  const toBn = (num: number) => {
    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)]);
  };

  // Interactive Exam Simulation State
  const [activeExamSet, setActiveExamSet] = useState<PredictorSet | null>(null);
  const [examQuestions, setExamQuestions] = useState<QuizQuestion[]>([]);
  const [currentExamIndex, setCurrentExamIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState<{ [qIndex: number]: number | null }>({});
  const [timeLeft, setTimeLeft] = useState<number>(60 * 60);
  const [isExamFinished, setIsExamFinished] = useState(false);
  const [examTab, setExamTab] = useState<'mcq' | 'written'>('mcq');

  // Single Question Explorer answer state
  const [revealedQuestions, setRevealedQuestions] = useState<{ [id: string]: number }>({});

  // Hotspot detection helper
  const getHotspotBadge = (q: QuizQuestion): string | null => {
    if (q.du_badge) return q.du_badge;
    if (q.du_topic && q.du_freq) {
      const icon = q.du_tier === 'super_hot' ? '🔥' : '⚡';
      const tierLabel = q.du_tier === 'super_hot' ? 'Super Hot' : 'Hot';
      return `${icon} ঢাবি ${tierLabel}: ${q.du_topic} (${toBn(q.du_freq)} বার)`;
    }
    const text = (q.q + ' ' + (q.exp || '')).toLowerCase();
    if (text.includes('পর্ব') || text.includes('সিলোম') || text.includes('পরিফেরা') || text.includes('নিডারিয়া') || text.includes('প্লাটিহেলমিনথিস') || text.includes('নেমাটোডা') || text.includes('অ্যানিলিডা') || text.includes('আর্থ্রোপোডা') || text.includes('মলাস্কা') || text.includes('একাইনোডার্মাটা') || text.includes('কর্ডাটা') || text.includes('শিখা কোষ')) {
      return '🔥 ঢাবি Super Hot: ৯টি পর্বের বৈশিষ্ট্য (১৯ বার)';
    }
    if (text.includes('c3') || text.includes('c4') || text.includes('ক্যালভিন') || text.includes('হ্যাচ ও স্ল্যাক') || text.includes('ক্র্যাঞ্জ') || text.includes('kranz')) {
      return '🔥 ঢাবি Super Hot: C3 ও C4 উদ্ভিদের পার্থক্য (১৭ বার)';
    }
    if (text.includes('করোটিক স্নায়ু') || text.includes('অলফ্যাক্টরি') || text.includes('অপটিক') || text.includes('ভেগাস') || text.includes('ট্রাইজেমিনাল')) {
      return '🔥 ঢাবি Super Hot: করোটিক স্নায়ু (১০ বার)';
    }
    if (text.includes('এন্ডোক্রাইন') || text.includes('অন্তঃক্ষরা') || text.includes('পিটুইটারি') || text.includes('থাইরয়েড') || text.includes('অ্যাড্রেনাল') || text.includes('ইনসুলিন') || text.includes('গ্লুকাগন')) {
      return '🔥 ঢাবি Super Hot: এন্ডোক্রাইন গ্রন্থি (১৬ বার)';
    }
    if (text.includes('প্রোফেজ-১') || text.includes('লেপ্টোটিন') || text.includes('জাইগোটিন') || text.includes('প্যাকাইটিন') || text.includes('ডিপ্লোটিন') || text.includes('ডায়াকাইনেসিস') || text.includes('কায়াজমা') || text.includes('ক্রসিং ওভার') || text.includes('সাইন্যাপসিস')) {
      return '🔥 ঢাবি Super Hot: মায়োসিসের প্রোফেজ-১ (১২ বার)';
    }
    if (text.includes('জাইলেম') || text.includes('ফ্লোয়েম') || text.includes('ট্রাকিয়া') || text.includes('ভেসেল') || text.includes('সিভনল') || text.includes('ভাস্কুলার বান্ডল')) {
      return '🔥 ঢাবি Super Hot: জাইলেম ও ফ্লোয়েম (১১ বার)';
    }
    if (text.includes('হাইড্রা') || text.includes('নিডোসাইট') || text.includes('নেমাটোসিস্ট') || text.includes('মেসোগ্লিয়া') || text.includes('ইন্টারস্টিশিয়াল')) {
      return '⚡ ঢাবি Hot: হাইড্রার কোষসমূহ (৯ বার)';
    }
    if (text.includes('হৃৎপিণ্ড') || text.includes('পেসমেকার') || text.includes('san') || text.includes('avn') || text.includes('কার্ডিয়াক') || text.includes('বাইপাস') || text.includes('অ্যানজিওপ্লাস্টি')) {
      return '⚡ ঢাবি Hot: হৃৎপিণ্ড ও রক্ত সংবহন (৯ বার)';
    }
    if (text.includes('মেন্ডেল') || text.includes('অসম্পূর্ণ প্রকটতা') || text.includes('সমপ্রকটতা') || text.includes('লিথাল জিন') || text.includes('এপিস্ট্যাসিস') || text.includes('দ্বৈত প্রচ্ছন্ন')) {
      return '⚡ ঢাবি Hot: মেন্ডেলের সূত্রের ব্যতিক্রম (৯ বার)';
    }
    if (text.includes('মাইটোকন্ড্রি') || text.includes('ক্রিস্টি') || text.includes('atp synthase')) {
      return '⚡ ঢাবি Hot: মাইটোকন্ড্রিয়া (৮ বার)';
    }
    if (text.includes('dna') || text.includes('rna') || text.includes('ডাবল হেলিক্স') || text.includes('শারগাফ') || text.includes('ট্রান্সক্রিপশন') || text.includes('ট্রান্সলেশন') || text.includes('জেনেটিক কোড')) {
      return '⚡ ঢাবি Hot: নিউক্লিক অ্যাসিড (৮ বার)';
    }
    if (text.includes('বর্তনী') || text.includes('রোধ') || text.includes('তুল্যরোধ') || text.includes('সার্কিট') || text.includes('কার্শফ') || text.includes('রোধের')) {
      return '⚡ ঢাবি হটস্পট: বর্তনী ও রোধের ম্যাথ';
    }
    if (text.includes('মেকানিজম') || text.includes('ইলেকট্রোফাইল') || text.includes('কার্বোক্যাটায়ন') || text.includes('মারকভনিকভ') || text.includes('হাকেল') || text.includes('জৈব বিক্রিয়া')) {
      return '⚡ ঢাবি হটস্পট: জৈব বিক্রিয়া মেকানিজম';
    }
    if (text.includes('লিমিট') || text.includes('ল’হসপিটাল') || text.includes('l\'hopital') || text.includes('ইন্টিগ্রেশন') || text.includes('যোগজ') || text.includes('অন্তরীকরণ') || text.includes('e^x')) {
      return '⚡ ঢাবি হটস্পট: লিমিট ও ইন্টিগ্রেশন শর্টকাট';
    }
    if (text.includes('নার্নস্ট') || text.includes('কোষ বিভব') || text.includes('ফ্যারাডে') || text.includes('তড়িৎদ্বার')) {
      return '⚡ ঢাবি হটস্পট: তড়িৎ রসায়ন ও নার্নস্ট সমীকরণ';
    }
    if (text.includes('দোলনকাল') || text.includes('স্প্রিং') || text.includes('অর্ধায়ু') || text.includes('তেজস্ক্রিয়')) {
      return '⚡ ইঞ্জিনিয়ারিং ব্রিজ: SHM ও তেজস্ক্রিয়তা স্পিড হ্যাক';
    }
    if (text.includes('ফাজান') || text.includes('পোলারায়ন') || text.includes('সংকরায়ন') || text.includes('vsepr') || text.includes('বন্ধন কোণ')) {
      return '⚡ ঢাবি হটস্পট: ফাজানের নীতি ও সংকরায়ন';
    }
    if (text.includes('বুদ্বুদ') || text.includes('হ্রদের') || text.includes('পৃষ্ঠটান') || text.includes('ইয়ং') || text.includes('সান্দ্রতা')) {
      return '⚡ ইঞ্জিনিয়ারিং ব্রিজ: পদার্থের গাঠনিক ধর্ম ও গ্যাস সূত্র';
    }
    if (text.includes('বিন্যাস') || text.includes('সমাবেশ') || text.includes('ভেদাঙ্ক') || text.includes('পরিমিত ব্যবধান')) {
      return '⚡ ঢাবি হটস্পট: বিন্যাস-সমাবেশ ও বিস্তার পরিমাপ';
    }
    return null;
  };

  // Milton Khandokar Golden Order Sequence
  const applyMiltonGoldenOrder = () => {
    if (examQuestions.length === 0) return;
    const goldenOrder = ['Biology', 'Chemistry', 'Physics', 'Higher Math'];
    const reordered = [...examQuestions].sort((a, b) => {
      const idxA = goldenOrder.indexOf(a.subject);
      const idxB = goldenOrder.indexOf(b.subject);
      if (idxA !== -1 && idxB !== -1) return idxA - idxB;
      if (idxA !== -1) return -1;
      if (idxB !== -1) return 1;
      return 0;
    });
    const newAnswers: { [qIndex: number]: number | null } = {};
    reordered.forEach((newQ, newIdx) => {
      const oldIdx = examQuestions.findIndex((q) => q.id === newQ.id);
      if (oldIdx !== -1 && userAnswers[oldIdx] !== undefined) {
        newAnswers[newIdx] = userAnswers[oldIdx];
      }
    });
    setExamQuestions(reordered);
    setUserAnswers(newAnswers);
    setCurrentExamIndex(0);
  };

  // Questions filtered strictly for the active weekly tab
  const currentWeekQuestions = useMemo(() => {
    return questions.filter((q) => {
      const qTrack = (q.track || '').toLowerCase();
      const aTrack = activeTrack.toLowerCase();
      const matchTrack = !q.track || qTrack === aTrack;

      const qWeekId = (q.week_id || '').toLowerCase();
      const qWeek = q.week !== undefined && q.week !== null ? String(q.week).toLowerCase() : '';
      const selWeek = selectedWeekTab.toLowerCase();
      const selWeekNum = selectedWeekTab.replace('week_0', '').replace('week_', '');

      const matchWeek = 
        qWeekId === selWeek || 
        qWeek === selWeek || 
        qWeek === selWeekNum ||
        (typeof q.week === 'number' && selWeek === `week_${String(q.week).padStart(2, '0')}`);

      const matchStar = selectedStar === 'all' || (q.yield_stars || 4) === selectedStar;
      const matchSubject = selectedSubject === 'All' || q.subject === selectedSubject;
      return matchTrack && matchWeek && matchStar && matchSubject;
    });
  }, [questions, activeTrack, selectedWeekTab, selectedStar, selectedSubject]);

  // Total slots calculation (10 to 15 questions per slot/page)
  const totalSlots = Math.max(1, Math.ceil(currentWeekQuestions.length / pageSize));

  // Current slot slice
  const slotQuestions = useMemo(() => {
    const start = currentSlotIndex * pageSize;
    return currentWeekQuestions.slice(start, start + pageSize);
  }, [currentWeekQuestions, currentSlotIndex, pageSize]);

  // Answered counter in current slot
  const slotAnsweredCount = useMemo(() => {
    return slotQuestions.filter((q) => revealedQuestions[q.id] !== undefined).length;
  }, [slotQuestions, revealedQuestions]);

  // Track-isolated subjects list
  const trackSubjects: { label: SubjectType; bn: string; icon: string }[] = useMemo(() => {
    if (activeTrack === 'medical') {
      return [
        { label: 'All', bn: 'সব বিষয়', icon: '🌐' },
        { label: 'Biology', bn: 'বায়োলজি', icon: '🧬' },
        { label: 'Chemistry', bn: 'কেমিস্ট্রি', icon: '🧪' },
        { label: 'Physics', bn: 'ফিজিক্স', icon: '⚛️' },
        { label: 'English', bn: 'ইংরেজি', icon: '🇬🇧' },
        { label: 'GK', bn: 'সাধারণ জ্ঞান', icon: '🇧🇩' },
      ];
    } else {
      return [
        { label: 'All', bn: 'সব বিষয়', icon: '🌐' },
        { label: 'Physics', bn: 'ফিজিক্স', icon: '⚛️' },
        { label: 'Chemistry', bn: 'কেমিস্ট্রি', icon: '🧪' },
        { label: 'Higher Math', bn: 'উচ্চতর গণিত', icon: '📐' },
        { label: 'Biology', bn: 'বায়োলজি', icon: '🧬' },
      ];
    }
  }, [activeTrack]);

  // Launch a curated prediction exam
  const handleStartSetExam = (set: PredictorSet) => {
    let chosen: QuizQuestion[] = [];
    if (set.questions && set.questions.length > 0) {
      chosen = [...set.questions];
    } else if (set.question_ids && set.question_ids.length > 0) {
      const qMap = new Map(questions.map((q) => [q.id, q]));
      chosen = set.question_ids
        .map((qid) => qMap.get(qid))
        .filter((q): q is QuizQuestion => Boolean(q));
    }

    if (chosen.length === 0) {
      let pool = questions.filter((q) => {
        const qTrack = (q.track || '').toLowerCase();
        const aTrack = activeTrack.toLowerCase();
        const matchTrack = !q.track || qTrack === aTrack;

        if (set.week_id || set.week) {
          const selWeek = (set.week_id || '').toLowerCase();
          const selWeekNum = set.week !== undefined ? String(set.week) : '';
          const qWeekId = (q.week_id || '').toLowerCase();
          const qWeek = q.week !== undefined && q.week !== null ? String(q.week).toLowerCase() : '';
          const matchWeek = 
            (selWeek && (qWeekId === selWeek || qWeek === selWeek)) ||
            (selWeekNum && (qWeek === selWeekNum || qWeekId.endsWith(selWeekNum.padStart(2, '0'))));
          if (!matchWeek) return false;
        }
        return matchTrack;
      });

      if (set.subjects && set.subjects.length > 0) {
        pool = pool.filter((q) => set.subjects.includes(q.subject));
      }
      const shuffled = [...pool].sort(() => 0.5 - Math.random());
      const count = Math.min(set.target_mcqs || pool.length, pool.length);
      chosen = shuffled.slice(0, count);
    }

    setExamQuestions(chosen);
    setActiveExamSet(set);
    setCurrentExamIndex(0);
    setUserAnswers({});
    setTimeLeft(set.duration_minutes * 60);
    setIsExamFinished(false);
    setExamTab('mcq');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Timer countdown
  React.useEffect(() => {
    if (!activeExamSet || isExamFinished) return;
    if (timeLeft <= 0) {
      handleFinishExam();
      return;
    }
    const timer = setInterval(() => {
      setTimeLeft((prev) => prev - 1);
    }, 1000);
    return () => clearInterval(timer);
  }, [activeExamSet, isExamFinished, timeLeft]);

  // Finish exam & trigger celebration
  const handleFinishExam = () => {
    setIsExamFinished(true);
    try {
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 },
      });
    } catch {
      // fallback
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Calculate score
  const examStats = useMemo(() => {
    let correct = 0;
    let wrong = 0;
    let unattempted = 0;

    examQuestions.forEach((q, idx) => {
      const ans = userAnswers[idx];
      if (ans === undefined || ans === null) {
        unattempted++;
      } else if (ans === q.ans) {
        correct++;
      } else {
        wrong++;
      }
    });

    const neg = activeExamSet?.negative_marking || 0.25;
    const finalScore = Math.max(0, correct * 1 - wrong * neg);
    const maxScore = examQuestions.length;
    const percentage = maxScore > 0 ? (finalScore / maxScore) * 100 : 0;

    return { correct, wrong, unattempted, finalScore, maxScore, percentage };
  }, [examQuestions, userAnswers, activeExamSet]);

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 py-5 pb-28">
      
      {/* 1. TOP HERO HEADER (CLEAN SOLID, NO BLUR/GPU ARTIFACTS) */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-7 shadow-sm mb-6 space-y-4">
        <div>
          <div className="flex items-center gap-2 mb-2 flex-wrap">
            <span className="px-2.5 py-0.5 rounded-full text-xs font-black bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 flex items-center gap-1.5 shadow-xs">
              <Sparkles className="w-3.5 h-3.5 text-amber-500" />
              Predictive High-Yield Engine 2026
            </span>
            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-500/10 text-blue-700 dark:text-blue-300 border border-blue-500/20">
              ⭐️ 1-5 Star Probability Matrix
            </span>
            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border border-emerald-500/20">
              {activeTrack === 'medical' ? '🩺 মেডিকেল ট্র্যাক' : "🎯 ভার্সিটি 'ক' ট্র্যাক"}
            </span>
          </div>

          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white tracking-tight">
            🔮 প্রেডিকশন ভল্ট: পেপার ফাইনাল ও মডেল সেট
          </h1>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1.5 max-w-2xl leading-relaxed">
            বিগত ১৫ বছরের মেডিকেল ও ঢাবি ভর্তি পরীক্ষার প্রশ্ন পুনরাবৃত্তির হার (Recurrence Weightage) এবং উইকলি কোচিং ট্রেন্ড অনুযায়ী কিউরেটেড মাস্টার প্রেডিকশন সেট ও হাই-ইল্ড স্টার ব্যাংক।
          </p>
        </div>

        {/* Clean Horizontal Weekly / Slot-Based Navigation Tabs */}
        {!activeExamSet && (
          <div className="pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3 flex-wrap">
            <div className="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1 w-full sm:w-auto">
              <button
                onClick={() => {
                  setActiveTab('weekly');
                  setSelectedWeekTab('week_01');
                  setCurrentSlotIndex(0);
                }}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'weekly' && selectedWeekTab === 'week_01'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>🎯</span>
                <span>Week 1: High Yield Core</span>
              </button>

              <button
                onClick={() => {
                  setActiveTab('weekly');
                  setSelectedWeekTab('week_02');
                  setCurrentSlotIndex(0);
                }}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'weekly' && selectedWeekTab === 'week_02'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>🔥</span>
                <span>Week 2: DU Repeat Vault</span>
              </button>

              <button
                onClick={() => {
                  setActiveTab('weekly');
                  setSelectedWeekTab('week_03');
                  setCurrentSlotIndex(0);
                }}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'weekly' && selectedWeekTab === 'week_03'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>⚡</span>
                <span>Week 3: Trap & Speed Special</span>
              </button>

              <button
                onClick={() => {
                  setActiveTab('weekly');
                  setSelectedWeekTab('week_04');
                  setCurrentSlotIndex(0);
                }}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'weekly' && selectedWeekTab === 'week_04'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>🎯</span>
                <span>Week 4: 80/20 Multi-Stream</span>
              </button>

              <button
                onClick={() => {
                  setActiveTab('weekly');
                  setSelectedWeekTab('week_05');
                  setCurrentSlotIndex(0);
                }}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'weekly' && selectedWeekTab === 'week_05'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>🔮</span>
                <span>Week 5: 80/20 Multi-Stream</span>
              </button>

              <button
                onClick={() => {
                  setActiveTab('weekly');
                  setSelectedWeekTab('week_06');
                  setCurrentSlotIndex(0);
                }}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'weekly' && selectedWeekTab === 'week_06'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>🚀</span>
                <span>Week 6: 80/20 Multi-Stream</span>
              </button>

              <button
                onClick={() => {
                  setActiveTab('weekly');
                  setSelectedWeekTab('week_07');
                  setCurrentSlotIndex(0);
                }}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'weekly' && selectedWeekTab === 'week_07'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>👑</span>
                <span>Week 7: Tri-Stream Pattern</span>
              </button>

              <button
                onClick={() => {
                  setActiveTab('weekly');
                  setSelectedWeekTab('week_08');
                  setCurrentSlotIndex(0);
                }}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'weekly' && selectedWeekTab === 'week_08'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <span>⚡</span>
                <span>Week 8: PCMB Master Core</span>
              </button>

              <button
                onClick={() => setActiveTab('sets')}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer whitespace-nowrap shrink-0 shadow-xs ${
                  activeTab === 'sets'
                    ? 'bg-[#056839] text-white ring-2 ring-[#056839]/30 scale-[1.02]'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
              >
                <Layers className="w-3.5 h-3.5" />
                <span>মডেল টেস্ট পেপার ({currentSets.length}টি সেট)</span>
              </button>
            </div>

            <div className="text-xs font-semibold text-slate-500 dark:text-slate-400">
              ট্র্যাক: <span className="font-bold text-[#056839] dark:text-emerald-400">{activeTrack === 'medical' ? 'মেডিকেল' : "ভার্সিটি 'ক'"}</span>
            </div>
          </div>
        )}
      </div>

      {/* =========================================================================
          VIEW A: ACTIVE TIMED EXAM SIMULATION
         ========================================================================= */}
      {activeExamSet && (
        <div className="bg-white dark:bg-zinc-900 rounded-3xl border border-zinc-200/90 dark:border-zinc-800 p-5 sm:p-7 shadow-sm mb-6 animate-in fade-in duration-200">
          
          {/* Exam Header */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-5 border-b border-zinc-200 dark:border-zinc-800">
            <div>
              <div className="flex items-center gap-2 mb-1">
                <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20">
                  {activeExamSet.badge}
                </span>
                <span className="text-xs font-semibold text-zinc-500">
                  {activeExamSet.total_marks} Marks • নেগেটিভ {activeExamSet.negative_marking}
                </span>
              </div>
              <h2 className="text-lg sm:text-xl font-extrabold text-zinc-900 dark:text-white">
                {activeExamSet.title}
              </h2>
            </div>

            <div className="flex items-center gap-3">
              {/* Countdown Timer */}
              {!isExamFinished && (
                <div className={`flex items-center gap-2 px-3 py-1.5 rounded-2xl font-mono text-sm font-bold border shadow-xs ${
                  timeLeft < 300 
                    ? 'bg-rose-50 dark:bg-rose-950/40 text-rose-600 border-rose-300 animate-pulse'
                    : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-200 border-zinc-300 dark:border-zinc-700'
                }`}>
                  <Timer className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
                  <span>{formatTimer(timeLeft)}</span>
                </div>
              )}

              {/* Finish Exam Button */}
              {!isExamFinished ? (
                <button
                  onClick={handleFinishExam}
                  className="px-4 py-1.5 rounded-2xl bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold shadow-sm transition-all active:scale-95 cursor-pointer"
                >
                  পরীক্ষা জমা দিন
                </button>
              ) : (
                <button
                  onClick={() => setActiveExamSet(null)}
                  className="px-4 py-1.5 rounded-2xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold shadow-sm transition-all active:scale-95 cursor-pointer"
                >
                  সেট তালিকা দেখুন
                </button>
              )}
            </div>
          </div>

          {/* Exam Mode Toggle: MCQ vs Written Section (if Varsity) */}
          {activeExamSet.written_included && (
            <div className="flex items-center gap-2 mt-4">
              <button
                onClick={() => setExamTab('mcq')}
                className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                  examTab === 'mcq'
                    ? 'bg-blue-600 text-white'
                    : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400'
                }`}
              >
                ১. এমসিকিউ সেকশন ({examQuestions.length}টি)
              </button>
              <button
                onClick={() => setExamTab('written')}
                className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                  examTab === 'written'
                    ? 'bg-emerald-600 text-white'
                    : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400'
                }`}
              >
                ২. ঢাবি লিখিত সেকশন ({activeExamSet.written_problems?.length || 4}টি সমস্যা)
              </button>
            </div>
          )}

          {/* Result Card when exam finished */}
          {isExamFinished && (
            <div className="my-6 p-5 rounded-2xl bg-gradient-to-r from-emerald-50 via-teal-50 to-cyan-50 dark:from-emerald-950/30 dark:via-teal-950/20 dark:to-zinc-900 border border-emerald-200 dark:border-emerald-800">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <Award className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
                    <span className="text-xs font-bold text-emerald-800 dark:text-emerald-300 uppercase tracking-wider">
                      ফাইনাল স্কোর কার্ড
                    </span>
                  </div>
                  <h3 className="text-xl font-black text-zinc-900 dark:text-white">
                    প্রাপ্ত স্কোর: {examStats.finalScore.toFixed(2)} / {examStats.maxScore}
                  </h3>
                  <p className="text-xs text-zinc-600 dark:text-zinc-400 mt-0.5">
                    সঠিক: <span className="font-bold text-emerald-600">{examStats.correct}</span> | ভুল: <span className="font-bold text-rose-600">{examStats.wrong}</span> | উত্তরহীন: <span className="font-bold text-zinc-500">{examStats.unattempted}</span>
                  </p>
                </div>

                <div className="bg-white dark:bg-zinc-800 p-3 rounded-xl border border-zinc-200 dark:border-zinc-700 text-center min-w-[140px]">
                  <div className="text-[11px] font-semibold text-zinc-400">সম্ভাব্য মেরিট রেঞ্জ</div>
                  <div className="text-base font-extrabold text-[#056839] dark:text-emerald-400">
                    {examStats.percentage >= 80 ? 'শীর্ষ ১ - ৫০০' : examStats.percentage >= 65 ? 'শীর্ষ ১০০০ - ২৫০০' : 'মেরিট অপেক্ষমাণ'}
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* ==================== TAB 1: MCQ SECTION ==================== */}
          {examTab === 'mcq' && (
            <div className="mt-6">
              {/* Milton Khandokar Golden Order 1-Click Action */}
              <div className="flex items-center justify-between gap-2 mb-4">
                <button
                  onClick={applyMiltonGoldenOrder}
                  title="বায়োলজি ➔ রসায়ন ➔ পদার্থ ➔ গণিত ক্রমানুসারে সাজান"
                  className="w-full sm:w-auto py-2 px-4 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-800 text-xs font-bold transition-all flex items-center justify-center gap-1.5 shadow-xs cursor-pointer"
                >
                  <span>⚡ মিল্টন স্যারের গোল্ডেন অর্ডার: বায়োলজি ➔ রসায়ন ➔ পদার্থ ➔ গণিত</span>
                </button>
              </div>

              {/* Question Navigation Palette */}
              <div className="flex items-center gap-1.5 overflow-x-auto pb-3 mb-6 no-scrollbar">
                {examQuestions.map((_, i) => {
                  const isCurrent = currentExamIndex === i;
                  const isAnswered = userAnswers[i] !== undefined && userAnswers[i] !== null;
                  return (
                    <button
                      key={i}
                      onClick={() => setCurrentExamIndex(i)}
                      className={`w-8 h-8 rounded-xl text-xs font-bold shrink-0 transition-all ${
                        isCurrent
                          ? 'ring-2 ring-[#056839] bg-[#056839] text-white'
                          : isAnswered
                          ? 'bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-700'
                          : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-700'
                      }`}
                    >
                      {i + 1}
                    </button>
                  );
                })}
              </div>

              {/* Current Question Body */}
              {examQuestions[currentExamIndex] && (
                <div className="p-5 rounded-2xl bg-zinc-50 dark:bg-zinc-800/50 border border-zinc-200/80 dark:border-zinc-700/80">
                  {/* Hotspot Badge if matching */}
                  {getHotspotBadge(examQuestions[currentExamIndex]) && (
                    <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-700 text-xs font-bold mb-3 shadow-xs">
                      <span>{getHotspotBadge(examQuestions[currentExamIndex])}</span>
                    </div>
                  )}

                  <div className="flex items-center justify-between gap-3 mb-3 flex-wrap">
                    <div className="flex items-center gap-2 flex-wrap">
                      <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 shadow-xs font-mono">
                        প্রশ্ন: {currentExamIndex + 1} / {examQuestions.length} টি • {examQuestions[currentExamIndex].subject}
                      </span>
                      {((examQuestions[currentExamIndex] as any).is_du_repeated || (examQuestions[currentExamIndex] as any).source_tag?.includes('DU Most Repeated') || examQuestions[currentExamIndex].tag?.includes('DU Repeat')) && (
                        <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full border bg-amber-500/15 text-amber-700 dark:text-amber-300 border-amber-500/30 flex items-center gap-1">
                          🔥 DU Most Repeated
                        </span>
                      )}
                      {examQuestions[currentExamIndex].written_essential && (
                        <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full border bg-violet-500/15 text-violet-700 dark:text-violet-300 border-violet-500/30 flex items-center gap-1">
                          ✍️ Written Essential
                        </span>
                      )}
                      {((examQuestions[currentExamIndex] as any).is_du_speed_hack || (examQuestions[currentExamIndex] as any).source_tag?.includes('DU Speed-Hack') || examQuestions[currentExamIndex].speed_hack) && (
                        <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full border bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 border-emerald-500/30 flex items-center gap-1">
                          ⚡ DU Speed-Hack
                        </span>
                      )}
                      {examQuestions[currentExamIndex].expected_count !== undefined && examQuestions[currentExamIndex].expected_count !== null && (
                        <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 shadow-xs inline-flex items-center gap-1">
                          <span>🎯 প্রত্যাশিত ফ্রিকোয়েন্সি: {typeof examQuestions[currentExamIndex].expected_count === 'number' ? `${examQuestions[currentExamIndex].expected_count} বার` : examQuestions[currentExamIndex].expected_count}</span>
                        </span>
                      )}
                    </div>

                    <span className="text-amber-500 text-xs font-bold">
                      {'⭐️'.repeat(examQuestions[currentExamIndex].yield_stars || 4)} {examQuestions[currentExamIndex].probability || '95% Yield'}
                    </span>
                  </div>

                  <h3 className="text-base sm:text-lg font-bold text-zinc-900 dark:text-white mb-5 leading-relaxed">
                    <MathText content={examQuestions[currentExamIndex].q} />
                  </h3>

                  {/* Options */}
                  <div className="space-y-2.5">
                    {examQuestions[currentExamIndex].opts.map((opt, optIdx) => {
                      const isSelected = userAnswers[currentExamIndex] === optIdx;
                      const isCorrect = isExamFinished && examQuestions[currentExamIndex].ans === optIdx;
                      const isWrongSelected = isExamFinished && isSelected && !isCorrect;

                      return (
                        <button
                          key={optIdx}
                          disabled={isExamFinished}
                          onClick={() => {
                            setUserAnswers((prev) => ({
                              ...prev,
                              [currentExamIndex]: optIdx,
                            }));
                          }}
                          className={`w-full p-3.5 rounded-xl border text-left text-sm font-semibold transition-all flex items-center justify-between gap-3 ${
                            isCorrect
                              ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-800 dark:text-emerald-200 font-bold'
                              : isWrongSelected
                              ? 'bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-800 dark:text-rose-200 font-bold'
                              : isSelected
                              ? 'bg-emerald-50 dark:bg-emerald-950/30 border-[#056839] text-zinc-900 dark:text-white font-bold ring-1 ring-[#056839]'
                              : 'bg-white dark:bg-zinc-800/80 border-zinc-200 dark:border-zinc-700 text-zinc-700 dark:text-zinc-300 hover:border-zinc-400 dark:hover:border-zinc-600'
                          }`}
                        >
                          <div className="flex items-center gap-3">
                            <span className="w-6 h-6 rounded-lg bg-zinc-100 dark:bg-zinc-700 text-zinc-700 dark:text-zinc-300 flex items-center justify-center text-xs font-bold shrink-0">
                              {String.fromCharCode(65 + optIdx)}
                            </span>
                            <MathText content={opt} />
                          </div>

                          {isCorrect && <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />}
                          {isWrongSelected && <XCircle className="w-5 h-5 text-rose-600 shrink-0" />}
                        </button>
                      );
                    })}
                  </div>

                  {/* Review Explanation (when exam is finished) */}
                  {isExamFinished && (
                    <div className="mt-5 p-4 rounded-xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-700 text-xs text-zinc-700 dark:text-zinc-300 space-y-2">
                      <div className="font-bold text-[#056839] dark:text-emerald-400">
                        ব্যাখ্যা ও সমাধান:
                      </div>
                      <MathText content={examQuestions[currentExamIndex].exp} />

                      {examQuestions[currentExamIndex].speed_hack && (
                        <div className="mt-2 pt-2 border-t border-zinc-100 dark:border-zinc-800 text-emerald-700 dark:text-emerald-400 flex items-start gap-1.5">
                          <span className="shrink-0">⚡</span>
                          <span><strong>স্পিড হ্যাক:</strong> <MathText content={examQuestions[currentExamIndex].speed_hack} /></span>
                        </div>
                      )}

                      {/* Strict Conditional Trap Alert */}
                      {(() => {
                        const currentQ = examQuestions[currentExamIndex];
                        const trapAlert = (currentQ.trap_alert || currentQ.trap || '').trim();
                        const isBoilerplate = trapAlert.includes('পিত্তরসে কোনো পরিপাক এনজাইম থাকে না') && 
                          (!currentQ.q.includes('পিত্ত') && !currentQ.q.includes('যকৃৎ') && !currentQ.q.includes('bile'));
                        if (!trapAlert || isBoilerplate) return null;
                        return (
                          <div className="mt-2 pt-2 border-t border-zinc-100 dark:border-zinc-800 text-amber-700 dark:text-amber-400 flex items-start gap-1.5">
                            <AlertTriangle className="w-4 h-4 shrink-0 text-amber-500" />
                            <span><strong>ট্র্যাপ সতর্কতা:</strong> <MathText content={trapAlert} /></span>
                          </div>
                        );
                      })()}

                      {examQuestions[currentExamIndex].source_book && (
                        <div className="text-[11px] text-zinc-400 font-semibold">
                          উৎস: {examQuestions[currentExamIndex].source_book}
                        </div>
                      )}
                    </div>
                  )}

                  {/* Question Navigator Controls */}
                  <div className="flex items-center justify-between gap-3 mt-6">
                    <button
                      disabled={currentExamIndex === 0}
                      onClick={() => setCurrentExamIndex((prev) => Math.max(0, prev - 1))}
                      className="px-4 py-2 rounded-xl bg-white dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 text-xs font-bold disabled:opacity-40"
                    >
                      পূর্ববর্তী প্রশ্ন
                    </button>

                    <button
                      disabled={currentExamIndex === examQuestions.length - 1}
                      onClick={() => setCurrentExamIndex((prev) => Math.min(examQuestions.length - 1, prev + 1))}
                      className="px-4 py-2 rounded-xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold disabled:opacity-40"
                    >
                      পরবর্তী প্রশ্ন
                    </button>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* ==================== TAB 2: WRITTEN SECTION (40 MARKS, 4 SUBJECT BLOCKS) ==================== */}
          {examTab === 'written' && activeExamSet.written_problems && (
            <div className="mt-6 space-y-8">
              <div className="p-4 rounded-2xl bg-blue-50/60 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800 text-xs text-blue-900 dark:text-blue-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <span>
                  <strong>ঢাকা বিশ্ববিদ্যালয় 'ক' লিখিত অংশ (DU 40-Mark Written Engine):</strong> ৪টি বিষয় (পদার্থ, রসায়ন, গণিত, জীববিজ্ঞান) × ৪টি সমস্যা (২.৫ নম্বর) = মোট ১৬টি সমস্যা (৪০ নম্বর)।
                </span>
                <span className="font-mono font-bold bg-blue-600 text-white px-2 py-0.5 rounded-lg shrink-0 text-[11px]">
                  মোট মান: ৪০.০
                </span>
              </div>

              {/* Render by 4 Distinct Subject Blocks */}
              {(['Physics', 'Chemistry', 'Higher Math', 'Biology'] as SubjectType[]).map((subjName) => {
                const problems = (activeExamSet.written_problems || []).filter((wp) => wp.subject === subjName);
                if (problems.length === 0) return null;

                const subjectTitles: { [key: string]: { bn: string; icon: string } } = {
                  Physics: { bn: 'পদার্থবিজ্ঞান', icon: '⚛️' },
                  Chemistry: { bn: 'রসায়ন', icon: '🧪' },
                  'Higher Math': { bn: 'উচ্চতর গণিত', icon: '📐' },
                  Biology: { bn: 'জীববিজ্ঞান', icon: '🧬' },
                };

                return (
                  <div key={subjName} className="space-y-4">
                    <div className="flex items-center justify-between pb-2 border-b border-zinc-200 dark:border-zinc-800">
                      <div className="flex items-center gap-2">
                        <span className="text-lg">{subjectTitles[subjName]?.icon || '📝'}</span>
                        <h3 className="text-base font-extrabold text-zinc-900 dark:text-white">
                          {subjectTitles[subjName]?.bn || subjName} লিখিত অংশ
                        </h3>
                      </div>
                      <span className="text-xs font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/50 px-2.5 py-0.5 rounded-full border border-emerald-200 dark:border-emerald-800">
                        ১০.০ নম্বর (৪ × ২.৫)
                      </span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {problems.map((wp, pIdx) => (
                        <div key={pIdx} className="p-4 sm:p-5 rounded-2xl bg-zinc-50 dark:bg-zinc-800/40 border border-zinc-200 dark:border-zinc-700 flex flex-col justify-between">
                          <div>
                            <div className="flex items-center justify-between gap-2 mb-2">
                              <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-blue-100 dark:bg-blue-950/60 text-blue-800 dark:text-blue-300">
                                সমস্যা {pIdx + 1} • {wp.subject}
                              </span>
                              <span className="text-xs font-bold text-zinc-500 font-mono">
                                মান: {wp.marks}
                              </span>
                            </div>

                            <div className="text-sm font-semibold text-zinc-900 dark:text-white my-3">
                              <MathText content={wp.problem} />
                            </div>
                          </div>

                          <details className="mt-3 group border-t border-zinc-200/80 dark:border-zinc-700/80 pt-3">
                            <summary className="cursor-pointer text-xs font-bold text-[#056839] dark:text-emerald-400 hover:underline list-none flex items-center gap-1.5">
                              <FileText className="w-3.5 h-3.5" />
                              <span>মডেল সমাধান ও স্টেপ-মার্কিং রুব্রিক (নম্বর বণ্টন) ▾</span>
                            </summary>
                            <div className="mt-2.5 p-3 rounded-xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-700 text-xs text-zinc-700 dark:text-zinc-300 leading-relaxed space-y-2">
                              <div>
                                <strong className="text-zinc-900 dark:text-white block mb-1">মডেল সমাধান:</strong>
                                <MathText content={wp.solution} />
                              </div>
                              {wp.rubric && (
                                <div className="pt-2 border-t border-zinc-100 dark:border-zinc-800 text-emerald-800 dark:text-emerald-300">
                                  <strong className="block mb-0.5 text-emerald-700 dark:text-emerald-400 font-bold">
                                    📋 নম্বর বণ্টন রুব্রিক:
                                  </strong>
                                  <span>{wp.rubric}</span>
                                </div>
                              )}
                            </div>
                          </details>
                        </div>
                      ))}
                    </div>
                  </div>
                );
              })}
            </div>
          )}

        </div>
      )}

      {/* =========================================================================
          VIEW B: MASTER PREDICTION SET CARDS (Sets List)
         ========================================================================= */}
      {!activeExamSet && activeTab === 'sets' && (
        <div className="space-y-4">
          <div className="flex items-center justify-between gap-2 mb-2">
            <h2 className="text-lg font-extrabold text-zinc-900 dark:text-white flex items-center gap-2">
              <Award className="w-5 h-5 text-amber-500" />
              <span>{activeTrack === 'medical' ? 'মেডিকেল পেপার ফাইনাল ও মডেল সেট' : "ঢাকা বিশ্ববিদ্যালয় 'ক' পেপার ফাইনাল ও মডেল সেট"}</span>
            </h2>
            <span className="text-xs text-zinc-500">
              {currentSets.length}টি স্পেশাল সেট
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {currentSets.map((set) => (
              <div 
                key={set.id}
                className="group rounded-3xl backdrop-blur-xl bg-white/85 dark:bg-slate-900/85 ring-1 ring-slate-200/80 dark:ring-slate-800/80 hover:ring-emerald-500/50 dark:hover:ring-emerald-500/50 shadow-sm p-5 flex flex-col justify-between transition-all duration-200"
              >
                <div>
                  <div className="flex items-center justify-between gap-2 mb-3">
                    <div className="flex items-center gap-1.5 flex-wrap">
                      <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/20">
                        {set.badge}
                      </span>
                      <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-500/10 text-amber-700 dark:text-amber-300 ring-1 ring-amber-500/20">
                        ✨ 80/20 High Yield
                      </span>
                    </div>
                    <span className="text-xs font-semibold text-slate-500 flex items-center gap-1 font-mono">
                      ⏱️ {set.duration_minutes} মিনিট
                    </span>
                  </div>

                  <div className="flex items-start gap-2.5 mb-2">
                    <span className="text-2xl mt-0.5 shrink-0">
                      {activeTrack === 'medical' ? '🩺' : '🎯'}
                    </span>
                    <h3 className="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors leading-snug">
                      {set.title}
                    </h3>
                  </div>

                  <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mb-3">
                    {set.description}
                  </p>

                  {set.syllabus_scope && (
                    <div className="mb-3.5 p-2.5 rounded-2xl bg-slate-50/80 dark:bg-slate-800/60 ring-1 ring-slate-200/80 dark:ring-slate-700/80 text-[11px] leading-relaxed text-slate-700 dark:text-slate-300">
                      <strong className="block text-emerald-700 dark:text-emerald-400 font-bold mb-0.5">📚 সিলেবাস ও অধ্যায় কাভারেজ:</strong>
                      <span>{set.syllabus_scope}</span>
                    </div>
                  )}

                  {/* Clean Metadata Row with Icons */}
                  <div className="flex items-center gap-2 text-xs font-semibold text-slate-600 dark:text-slate-300 py-2.5 border-y border-slate-100 dark:border-slate-800/80 my-2">
                    <span className="flex items-center gap-1">
                      ⏱️ সময় ({set.duration_minutes} মি.)
                    </span>
                    <span>•</span>
                    <span className="flex items-center gap-1">
                      📝 {set.target_mcqs}টি প্রশ্ন
                    </span>
                    <span>•</span>
                    <span className="flex items-center gap-1">
                      🎯 {set.total_marks} মার্কস
                    </span>
                  </div>
                </div>

                <div className="pt-2">
                  <button
                    onClick={() => handleStartSetExam(set)}
                    className="w-full py-2.5 rounded-2xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold shadow-md shadow-[#056839]/20 transition-all flex items-center justify-center gap-2 active:scale-95 cursor-pointer"
                  >
                    <span>পরীক্ষা শুরু করুন</span>
                    <ChevronRight className="w-4 h-4" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* =========================================================================
          VIEW C: WEEKLY / SLOT-BASED PREDICTION SETS (FOCUSED 10-15 QUESTIONS/PAGE)
         ========================================================================= */}
      {!activeExamSet && activeTab === 'weekly' && (
        <div className="space-y-5">
          {/* Filters Bar: Star Rating & Isolated Subjects */}
          <div className="bg-white dark:bg-zinc-900 p-4 rounded-2xl border border-zinc-200/90 dark:border-zinc-800 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xs">
            {/* Star Filter Pills */}
            <div className="flex items-center gap-1.5 overflow-x-auto w-full sm:w-auto no-scrollbar">
              <span className="text-xs font-bold text-zinc-400 uppercase tracking-wider shrink-0 mr-1">
                স্টার স্কোর:
              </span>
              {[
                { id: 'all' as const, label: '🌟 অল' },
                { id: 5, label: '⭐️⭐️⭐️⭐️⭐️ (৫-স্টার)' },
                { id: 4, label: '⭐️⭐️⭐️⭐️ (৪-স্টার)' },
              ].map((st) => (
                <button
                  key={st.id}
                  onClick={() => setSelectedStar(st.id)}
                  className={`px-3 py-1 rounded-full text-xs font-bold transition-all shrink-0 cursor-pointer ${
                    selectedStar === st.id
                      ? 'bg-amber-500 text-white shadow-xs'
                      : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200 dark:hover:bg-zinc-700'
                  }`}
                >
                  {st.label}
                </button>
              ))}
            </div>

            {/* Subject Filter Pills (Strictly isolated by track) */}
            <div className="flex items-center gap-1.5 overflow-x-auto w-full sm:w-auto no-scrollbar">
              {trackSubjects.map((sb) => (
                <button
                  key={sb.label}
                  onClick={() => setSelectedSubject(sb.label)}
                  className={`px-2.5 py-1 rounded-full text-xs font-semibold transition-all shrink-0 flex items-center gap-1 cursor-pointer ${
                    selectedSubject === sb.label
                      ? 'bg-[#056839] text-white font-bold shadow-xs'
                      : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200 dark:hover:bg-zinc-700'
                  }`}
                >
                  <span>{sb.icon}</span>
                  <span>{sb.bn}</span>
                </button>
              ))}
            </div>
          </div>

          {/* Slot Segment Navigation Bar */}
          <div className="bg-white dark:bg-zinc-900 p-4 rounded-2xl border border-zinc-200/90 dark:border-zinc-800 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3">
            <div>
              <div className="flex items-center gap-2">
                <span className="text-sm font-extrabold text-zinc-900 dark:text-white">
                  {selectedWeekTab === 'week_01'
                    ? '🎯 Week 1: High Yield Core'
                    : selectedWeekTab === 'week_02'
                    ? '🔥 Week 2: DU Repeat Vault'
                    : selectedWeekTab === 'week_03'
                    ? '⚡ Week 3: Trap & Speed Special'
                    : selectedWeekTab === 'week_04'
                    ? '🎯 Week 4: 80/20 Multi-Stream'
                    : selectedWeekTab === 'week_05'
                    ? '🔮 Week 5: 80/20 Multi-Stream Pattern'
                    : selectedWeekTab === 'week_06'
                    ? '🚀 Week 6: 80/20 Multi-Stream'
                    : selectedWeekTab === 'week_07'
                    ? '👑 Week 7: Tri-Stream Pattern'
                    : '⚡ Week 8: PCMB Master Core'}
                </span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/40 text-[#056839] dark:text-emerald-400 font-mono font-bold border border-emerald-200 dark:border-emerald-800">
                  মোট {toBn(currentWeekQuestions.length)}টি প্রশ্ন
                </span>
              </div>
              <div className="text-[11px] text-zinc-500 dark:text-zinc-400 mt-0.5">
                প্রতি স্লটে ১২টি করে ফোকাসড প্রশ্ন • এক নজরে গভীর অনুশীলন
              </div>
            </div>

            {/* Quick Slot Jump Pills */}
            <div className="flex items-center gap-1.5 overflow-x-auto max-w-full no-scrollbar pb-1">
              {Array.from({ length: totalSlots }).map((_, sIdx) => {
                const isActive = currentSlotIndex === sIdx;
                return (
                  <button
                    key={sIdx}
                    onClick={() => {
                      setCurrentSlotIndex(sIdx);
                      window.scrollTo({ top: 220, behavior: 'smooth' });
                    }}
                    className={`px-3 py-1 rounded-xl text-xs font-bold transition-all shrink-0 cursor-pointer ${
                      isActive
                        ? 'bg-[#056839] text-white shadow-xs scale-105'
                        : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200 dark:hover:bg-zinc-700'
                    }`}
                  >
                    স্লট {toBn(sIdx + 1)}
                  </button>
                );
              })}
            </div>
          </div>

          {/* MODERN EDTECH EXAM ROUTINE CARD FOR ACTIVE SLOT */}
          {slotQuestions.length > 0 && (
            <div className="rounded-3xl backdrop-blur-xl bg-gradient-to-br from-white/90 via-slate-50/80 to-emerald-50/30 dark:from-slate-900/90 dark:via-slate-900/80 dark:to-emerald-950/20 ring-1 ring-slate-200/80 dark:ring-slate-800/80 hover:ring-emerald-500/50 p-4 sm:p-5 shadow-sm transition-all flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <div className="flex items-center gap-2 mb-2 flex-wrap">
                  <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/30">
                    ✨ 80/20 High Yield
                  </span>
                  <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-blue-500/10 text-blue-700 dark:text-blue-300 ring-1 ring-blue-500/20">
                    🔥 DU Repeat
                  </span>
                  <span className="text-xs text-slate-500 dark:text-slate-400 font-mono">
                    স্লট {toBn(currentSlotIndex + 1)} / {toBn(totalSlots)}
                  </span>
                </div>

                <div className="flex items-center gap-2 mb-1.5">
                  <span className="text-2xl">
                    {selectedSubject === 'Physics' ? '⚛️' : selectedSubject === 'Chemistry' ? '🧪' : selectedSubject === 'Higher Math' ? '📐' : selectedSubject === 'Biology' ? '🧬' : '🎯'}
                  </span>
                  <h3 className="text-base sm:text-lg font-extrabold text-slate-900 dark:text-white">
                    {selectedWeekTab.toUpperCase()} {selectedSubject === 'All' ? (activeTrack === 'medical' ? 'Medical Core' : 'Varsity Core') : selectedSubject} Slot-{toBn(currentSlotIndex + 1)}
                  </h3>
                </div>

                {/* Clean Metadata Row with Icons */}
                <div className="flex items-center gap-2 text-xs font-semibold text-slate-600 dark:text-slate-300">
                  <span className="flex items-center gap-1">
                    ⏱️ সময় (১৫ মি.)
                  </span>
                  <span>|</span>
                  <span className="flex items-center gap-1">
                    📝 {toBn(slotQuestions.length)}টি প্রশ্ন
                  </span>
                  <span>|</span>
                  <span className="flex items-center gap-1">
                    🎯 {toBn(slotQuestions.length)} মার্কস
                  </span>
                </div>
              </div>

              {/* Call to Action Buttons */}
              <div className="flex items-center gap-2 shrink-0">
                <button
                  onClick={() => {
                    const fakeSet: PredictorSet = {
                      id: `slot_${selectedWeekTab}_${currentSlotIndex}`,
                      title: `${selectedWeekTab.toUpperCase()} ${selectedSubject === 'All' ? (activeTrack === 'medical' ? 'Medical Core' : 'Varsity Core') : selectedSubject} Slot-${toBn(currentSlotIndex + 1)}`,
                      badge: '✨ 80/20 High Yield',
                      duration_minutes: 15,
                      target_mcqs: slotQuestions.length,
                      total_marks: slotQuestions.length,
                      negative_marking: 0.25,
                      subjects: [selectedSubject === 'All' ? (activeTrack === 'medical' ? 'Biology' : 'Physics') : selectedSubject],
                      track: activeTrack,
                      description: '১২টি হাই-ইল্ড ফোকাসড প্রশ্ন প্র্যাকটিস ড্রিল',
                      questions: slotQuestions,
                      question_ids: slotQuestions.map((q) => q.id),
                    };
                    handleStartSetExam(fakeSet);
                  }}
                  className="px-4 py-2.5 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-md shadow-emerald-600/20 transition-all flex items-center gap-1.5 active:scale-95 cursor-pointer"
                >
                  <Sparkles className="w-4 h-4 fill-current" />
                  <span>প্র্যাকটিস শুরু করুন</span>
                </button>

                <button
                  onClick={() => {
                    const fakeSet: PredictorSet = {
                      id: `timed_slot_${selectedWeekTab}_${currentSlotIndex}`,
                      title: `${selectedWeekTab.toUpperCase()} ${selectedSubject === 'All' ? (activeTrack === 'medical' ? 'Medical Core' : 'Varsity Core') : selectedSubject} Slot-${toBn(currentSlotIndex + 1)} (Timed)`,
                      badge: '⏱️ Timed Test',
                      duration_minutes: 15,
                      target_mcqs: slotQuestions.length,
                      total_marks: slotQuestions.length,
                      negative_marking: 0.25,
                      subjects: [selectedSubject === 'All' ? (activeTrack === 'medical' ? 'Biology' : 'Physics') : selectedSubject],
                      track: activeTrack,
                      description: 'টাইমড টেস্ট ক্যাপসুল',
                      questions: slotQuestions,
                      question_ids: slotQuestions.map((q) => q.id),
                    };
                    handleStartSetExam(fakeSet);
                  }}
                  className="px-4 py-2.5 rounded-2xl bg-slate-900 dark:bg-slate-800 hover:bg-slate-800 text-white text-xs font-bold shadow-xs transition-all flex items-center gap-1.5 ring-1 ring-slate-700 active:scale-95 cursor-pointer"
                >
                  <Timer className="w-4 h-4 text-amber-400" />
                  <span>টাইমড টেস্ট</span>
                </button>
              </div>
            </div>
          )}

          {/* Current Slot Questions (10-15 per page) */}
          {slotQuestions.length === 0 ? (
            <div className="bg-white dark:bg-zinc-900 rounded-3xl p-8 border border-zinc-200/90 dark:border-zinc-800 text-center space-y-3">
              <span className="text-3xl">🔍</span>
              <h3 className="text-sm font-bold text-zinc-800 dark:text-zinc-200">
                এই ফিল্টারে কোনো প্রশ্ন পাওয়া যায়নি
              </h3>
              <p className="text-xs text-zinc-500">বিষয় বা স্টার ফিল্টার রিসেট করে আবার চেষ্টা করুন।</p>
              <button
                onClick={() => {
                  setSelectedStar('all');
                  setSelectedSubject('All');
                }}
                className="px-4 py-1.5 rounded-xl bg-[#056839] text-white text-xs font-bold"
              >
                ফিল্টার রিসেট
              </button>
            </div>
          ) : (
            <div className="space-y-4">
              {slotQuestions.map((q, idx) => {
                const globalIndex = currentSlotIndex * pageSize + idx + 1;
                const userChoice = revealedQuestions[q.id];
                const isAnswered = userChoice !== undefined;
                const isCorrect = isAnswered && userChoice === q.ans;
                const hotspot = getHotspotBadge(q);

                return (
                  <div 
                    key={q.id || idx}
                    className="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-zinc-200/90 dark:border-zinc-800 shadow-sm transition-all"
                  >
                    {hotspot && (
                      <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-700 text-xs font-bold mb-3 shadow-xs">
                        <span>{hotspot}</span>
                      </div>
                    )}

                    <div className="flex items-center justify-between gap-3 mb-2.5 flex-wrap">
                      <div className="flex items-center gap-2">
                        <span className="w-6 h-6 rounded-lg bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 flex items-center justify-center text-xs font-mono font-bold shrink-0">
                          {toBn(globalIndex)}
                        </span>
                        <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20">
                          {q.subject}
                        </span>
                        {q.written_essential && (
                          <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-violet-500/15 text-violet-700 dark:text-violet-300 border border-violet-500/30">
                            ✍️ Written Essential
                          </span>
                        )}
                        {q.chapter && (
                          <span className="px-2 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-50 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-300 border border-emerald-500/20">
                            {q.chapter}
                          </span>
                        )}
                        {q.tag && (
                          <span className="px-2 py-0.5 rounded-full text-[11px] font-semibold bg-blue-500/10 text-blue-700 dark:text-blue-300 border border-blue-500/20">
                            {q.tag}
                          </span>
                        )}
                        {((q as any).is_du_repeated || (q as any).source_tag?.includes('DU Most Repeated') || q.tag?.includes('DU Repeat')) && (
                          <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-amber-500/15 text-amber-700 dark:text-amber-300 border border-amber-500/30">
                            🔥 DU Most Repeated
                          </span>
                        )}
                        {((q as any).is_du_speed_hack || (q as any).source_tag?.includes('DU Speed-Hack') || q.speed_hack) && (
                          <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 border border-emerald-500/30">
                            ⚡ DU Speed-Hack
                          </span>
                        )}
                        {q.expected_count !== undefined && q.expected_count !== null && (
                          <span className="text-[11px] font-bold px-2 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 shadow-xs inline-flex items-center gap-1">
                            <span>🎯 প্রত্যাশিত ফ্রিকোয়েন্সি: {typeof q.expected_count === 'number' ? `${q.expected_count} বার` : q.expected_count}</span>
                          </span>
                        )}
                      </div>

                      <div className="flex items-center gap-2 text-xs font-bold text-amber-500">
                        <span>{'⭐️'.repeat(q.yield_stars || 4)}</span>
                        <span className="text-zinc-500 font-mono text-[11px]">({q.probability || 'High-Yield'})</span>
                      </div>
                    </div>

                    <h3 className="text-sm sm:text-base font-bold text-zinc-900 dark:text-white mb-4 leading-relaxed">
                      <MathText content={q.q} />
                    </h3>

                    {/* Options */}
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-3">
                      {q.opts.map((opt, optIdx) => {
                        const isChoice = userChoice === optIdx;
                        const isRealAns = isAnswered && q.ans === optIdx;

                        return (
                          <button
                            key={optIdx}
                            onClick={() => {
                              setRevealedQuestions((prev) => ({
                                ...prev,
                                [q.id]: optIdx,
                              }));
                            }}
                            className={`p-2.5 rounded-xl border text-left text-xs font-semibold transition-all flex items-center justify-between gap-2 cursor-pointer ${
                              isRealAns
                                ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-800 dark:text-emerald-200 font-bold'
                                : isChoice && !isRealAns
                                ? 'bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-800 dark:text-rose-200 font-bold'
                                : 'bg-zinc-50 dark:bg-zinc-800/60 border-zinc-200/80 dark:border-zinc-700/80 hover:bg-zinc-100 dark:hover:bg-zinc-700 text-zinc-700 dark:text-zinc-300'
                            }`}
                          >
                            <div className="flex items-center gap-2">
                              <span className="w-5 h-5 rounded-md bg-zinc-200/70 dark:bg-zinc-700 text-zinc-700 dark:text-zinc-300 flex items-center justify-center text-[10px] font-bold shrink-0">
                                {String.fromCharCode(65 + optIdx)}
                              </span>
                              <MathText content={opt} />
                            </div>

                            {isRealAns && <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />}
                            {isChoice && !isRealAns && <XCircle className="w-4 h-4 text-rose-600 shrink-0" />}
                          </button>
                        );
                      })}
                    </div>

                    {/* Explanation card (Strict Conditional Trap Alert) */}
                    {isAnswered && (
                      <div className="mt-3 p-3.5 rounded-xl bg-zinc-50 dark:bg-zinc-800/50 border border-zinc-200/80 dark:border-zinc-700/80 text-xs text-zinc-700 dark:text-zinc-300 space-y-1.5 animate-in fade-in duration-150">
                        <div className="font-bold text-[#056839] dark:text-emerald-400">
                          {isCorrect ? '✓ সঠিক উত্তর!' : '✗ ভুল উত্তর!'} সঠিক অপশন: {String.fromCharCode(65 + q.ans)}
                        </div>
                        <MathText content={q.exp} />

                        {q.speed_hack && (
                          <div className="pt-2 text-emerald-700 dark:text-emerald-400 flex items-start gap-1.5 border-t border-zinc-200/70 dark:border-zinc-700/70">
                            <span className="shrink-0 mt-0.5">⚡</span>
                            <span><strong className="font-bold">স্পিড হ্যাক:</strong> <MathText content={q.speed_hack} /></span>
                          </div>
                        )}

                        {/* Strict conditional rendering: ONLY if genuine trap exists */}
                        {(() => {
                          const trapAlert = (q.trap_alert || q.trap || '').trim();
                          const isBoilerplate = trapAlert.includes('পিত্তরসে কোনো পরিপাক এনজাইম থাকে না') && 
                            (!q.q.includes('পিত্ত') && !q.q.includes('যকৃৎ') && !q.q.includes('bile'));
                          if (!trapAlert || isBoilerplate) return null;
                          return (
                            <div className="pt-2 text-amber-700 dark:text-amber-400 flex items-start gap-1.5 border-t border-zinc-200/70 dark:border-zinc-700/70">
                              <AlertTriangle className="w-3.5 h-3.5 shrink-0 text-amber-500 mt-0.5" />
                              <span><strong className="font-bold">ট্র্যাপ সতর্কতা:</strong> <MathText content={trapAlert} /></span>
                            </div>
                          );
                        })()}

                        {q.source_book && (
                          <div className="text-[10px] text-zinc-400 font-semibold pt-1">
                            উৎস: {q.source_book}
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          )}

          {/* Sticky Bottom Navigation Bar for Slot Progress & Slot Switching */}
          <div className="sticky bottom-4 z-40 bg-white/95 dark:bg-zinc-900/95 backdrop-blur-md border border-zinc-200/90 dark:border-zinc-800 shadow-xl rounded-2xl p-3 sm:p-4 flex items-center justify-between gap-3 max-w-4xl mx-auto mt-6">
            {/* Progress counter */}
            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold text-xs shrink-0">
                ✓
              </div>
              <div>
                <div className="text-xs sm:text-sm font-extrabold text-zinc-900 dark:text-white">
                  {toBn(slotAnsweredCount)} / {toBn(slotQuestions.length)} সম্পন্ন
                </div>
                <div className="text-[10px] text-zinc-500 dark:text-zinc-400 font-medium">
                  স্লট {toBn(currentSlotIndex + 1)} / {toBn(totalSlots)} (মোট {toBn(currentWeekQuestions.length)}টি প্রশ্ন)
                </div>
              </div>
            </div>

            {/* Previous / Next Slot Navigation Buttons */}
            <div className="flex items-center gap-2">
              <button
                disabled={currentSlotIndex === 0}
                onClick={() => {
                  setCurrentSlotIndex((prev) => Math.max(0, prev - 1));
                  window.scrollTo({ top: 220, behavior: 'smooth' });
                }}
                className="px-3.5 py-2 rounded-xl text-xs font-bold transition-all border border-zinc-200 dark:border-zinc-700 bg-white dark:bg-zinc-800 text-zinc-700 dark:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-700 disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer"
              >
                পূর্ববর্তী স্লট
              </button>

              <button
                onClick={() => {
                  if (currentSlotIndex < totalSlots - 1) {
                    setCurrentSlotIndex((prev) => prev + 1);
                    window.scrollTo({ top: 220, behavior: 'smooth' });
                  } else {
                    // Advance to next week or trigger confetti
                    if (selectedWeekTab === 'week_01') {
                      setSelectedWeekTab('week_02');
                      setCurrentSlotIndex(0);
                      window.scrollTo({ top: 220, behavior: 'smooth' });
                    } else if (selectedWeekTab === 'week_02') {
                      setSelectedWeekTab('week_03');
                      setCurrentSlotIndex(0);
                      window.scrollTo({ top: 220, behavior: 'smooth' });
                    } else if (selectedWeekTab === 'week_03') {
                      setSelectedWeekTab('week_05');
                      setCurrentSlotIndex(0);
                      window.scrollTo({ top: 220, behavior: 'smooth' });
                    } else if (selectedWeekTab === 'week_05') {
                      setSelectedWeekTab('week_06');
                      setCurrentSlotIndex(0);
                      window.scrollTo({ top: 220, behavior: 'smooth' });
                    } else if (selectedWeekTab === 'week_06') {
                      setSelectedWeekTab('week_07');
                      setCurrentSlotIndex(0);
                      window.scrollTo({ top: 220, behavior: 'smooth' });
                    } else if (selectedWeekTab === 'week_07') {
                      setSelectedWeekTab('week_08');
                      setCurrentSlotIndex(0);
                      window.scrollTo({ top: 220, behavior: 'smooth' });
                    } else {
                      try {
                        confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
                      } catch {}
                    }
                  }
                }}
                className="px-4 py-2 rounded-xl text-xs font-bold transition-all bg-[#056839] hover:bg-[#044e2b] text-white shadow-sm cursor-pointer flex items-center gap-1.5"
              >
                <span>
                  {currentSlotIndex < totalSlots - 1
                    ? 'পরবর্তী স্লট'
                    : selectedWeekTab !== 'week_08'
                    ? 'পরবর্তী উইক স্লট ➔'
                    : 'উইক সম্পন্ন 🎉'}
                </span>
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
};

export const PredictionView = PredictorView;
export default PredictorView;
