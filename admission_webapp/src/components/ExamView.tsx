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
  HelpCircle,
  Zap,
  Check
} from 'lucide-react';
import confetti from 'canvas-confetti';
import type { QuizQuestion, SubjectType, WeekFilterType } from '../types';
import { MathText } from './MathText';
import { saveExamAttempt, type ExamAttemptRecord } from '../lib/analytics';

interface ExamViewProps {
  quizzes: QuizQuestion[];
  selectedWeek: WeekFilterType;
  selectedSubject: SubjectType;
}

interface MasteryQueueItem {
  question: QuizQuestion;
  consecutiveCorrect: number; // 0, 1, or 2 (mastered)
  attempts: number;
  wrongCount: number;
  unsureCount: number;
  status: 'learning' | 'mastered';
}

export const ExamView: React.FC<ExamViewProps> = ({
  quizzes,
  selectedWeek,
  selectedSubject,
}) => {
  // Filter questions by week and subject
  const availableQuestions = quizzes.filter((q) => {
    const matchWeek = selectedWeek === 'all' || q.week_id === selectedWeek;
    const matchSubject = selectedSubject === 'All' || q.subject === selectedSubject;
    return matchWeek && matchSubject;
  });

  // Practice Mode: 'timed' (Timed Capsule Exam) or 'mastery' (বারবার প্র্যাকটিস - Mastery Re-test)
  const [practiceMode, setPracticeMode] = useState<'mastery' | 'timed'>('mastery');

  // Shared state
  const [sessionStarted, setSessionStarted] = useState(false);
  const [sessionFinished, setSessionFinished] = useState(false);
  const [questionCount, setQuestionCount] = useState<number>(25);

  // -------------------------------------------------------------
  // TIMED EXAM STATE
  // -------------------------------------------------------------
  const [timedQuestions, setTimedQuestions] = useState<QuizQuestion[]>([]);
  const [timedIndex, setTimedIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<{ [qIndex: number]: number | null }>({});
  const [timeSpent, setTimeSpent] = useState<{ [qIndex: number]: number }>({});
  const [timeLeft, setTimeLeft] = useState(45);
  const [filterReview, setFilterReview] = useState<'all' | 'wrong'>('all');
  const hasSavedRef = useRef<boolean>(false);

  // -------------------------------------------------------------
  // MASTERY RE-TEST STATE ("বারবার প্র্যাকটিস")
  // -------------------------------------------------------------
  const [masteryPool, setMasteryPool] = useState<MasteryQueueItem[]>([]);
  const [activeQueueIndices, setActiveQueueIndices] = useState<number[]>([]);
  const [currentQueuePos, setCurrentQueuePos] = useState<number>(0);
  const [masteryFeedback, setMasteryFeedback] = useState<{
    type: 'correct' | 'wrong' | 'unsure';
    userChoice: number | null;
    message: string;
  } | null>(null);
  const [autoAdvance, setAutoAdvance] = useState(true);
  const [totalRoundsAnswered, setTotalRoundsAnswered] = useState(0);
  const autoAdvanceTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Parse origin tag and clean question body
  const parseQuestionData = (q: QuizQuestion) => {
    let origin = q.origin;
    let cleanText = q.q;
    if (!origin) {
      const match = q.q.match(/^\[(.*?)\]\s*(.*)$/s);
      if (match) {
        origin = match[1];
        cleanText = match[2];
      } else {
        origin = "DU Core";
      }
    } else {
      cleanText = cleanText.replace(/^\[(.*?)\]\s*/, '');
    }
    return { origin, cleanText };
  };

  // Color style for origin badge
  const getOriginBadgeStyle = (origin: string) => {
    if (origin.includes('DU')) {
      return 'bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border-blue-200 dark:border-blue-800';
    } else if (origin.includes('MAT') || origin.includes('DAT') || origin.includes('Medical')) {
      return 'bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-800';
    } else if (origin.includes('RU') || origin.includes('JU') || origin.includes('CU') || origin.includes('GST')) {
      return 'bg-teal-50 dark:bg-teal-950/40 text-teal-700 dark:text-teal-300 border-teal-200 dark:border-teal-800';
    } else if (origin.includes('BCS') || origin.includes('1971') || origin.includes('Liberation War') || origin.includes('Core GK')) {
      return 'bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 border-amber-200 dark:border-amber-800';
    }
    return 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800';
  };

  const toBn = (num: number | string) => {
    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)]);
  };

  const getHotspotBadge = (q: QuizQuestion): string | null => {
    if (q.du_badge) return q.du_badge;
    if (q.du_topic && q.du_freq) {
      const icon = q.du_tier === 'super_hot' ? '🔥' : '⚡';
      const tierLabel = q.du_tier === 'super_hot' ? 'Super Hot' : 'Hot';
      return `${icon} ঢাবি ${tierLabel}: ${q.du_topic} (${toBn(q.du_freq)} বার)`;
    }
    const text = `${q.q} ${q.exp || ''} ${q.trap || ''} ${q.trap_insight || ''}`;
    if (/পর্ব|সিলোম|পরিফেরা|নিডারিয়া|প্লাটিহেলমিনথিস|নেমাটোডা|অ্যানিলিডা|আর্থ্রোপোডা|মলাস্কা|একাইনোডার্মাটা|কর্ডাটা|শিখা\s*কোষ/.test(text)) {
      return '🔥 ঢাবি Super Hot: ৯টি পর্বের বৈশিষ্ট্য (১৯ বার)';
    }
    if (/C3|C4|ক্যালভিন\s*চক্র|হ্যাচ\s*ও\s*স্ল্যাক|ক্র্যাঞ্জ|Kranz/.test(text)) {
      return '🔥 ঢাবি Super Hot: C3 ও C4 উদ্ভিদের পার্থক্য (১৭ বার)';
    }
    if (/করোটিক\s*স্নায়ু|অলফ্যাক্টরি|অপটিক|ভেগাস|ট্রাইজেমিনাল/.test(text)) {
      return '🔥 ঢাবি Super Hot: করোটিক স্নায়ু (১০ বার)';
    }
    if (/এন্ডোক্রাইন|অন্তঃক্ষরা|পিটুইটারি|থাইরয়েড|অ্যাড্রেনাল|ইনসুলিন|গ্লুকাগন/.test(text)) {
      return '🔥 ঢাবি Super Hot: এন্ডোক্রাইন গ্রন্থি (১৬ বার)';
    }
    if (/প্রোফেজ-১|লেপ্টোটিন|জাইগোটিন|প্যাকাইটিন|ডিপ্লোটিন|ডায়াকাইনেসিস|কায়াজমা|ক্রসিং\s*ওভার|সাইন্যাপসিস/.test(text)) {
      return '🔥 ঢাবি Super Hot: মায়োসিসের প্রোফেজ-১ (১২ বার)';
    }
    if (/জাইলেম|ফ্লোয়েম|ট্রাকিয়া|ভেসেল|সিভনল|ভাস্কুলার\s*বান্ডল/.test(text)) {
      return '🔥 ঢাবি Super Hot: জাইলেম ও ফ্লোয়েম (১১ বার)';
    }
    if (/হাইড্রা|নিডোসাইট|নেমাটোসিস্ট|মেসোগ্লিয়া|ইন্টারস্টিশিয়াল/.test(text)) {
      return '⚡ ঢাবি Hot: হাইড্রার কোষসমূহ (৯ বার)';
    }
    if (/হৃৎপিণ্ড|পেসমেকার|SAN|AVN|কার্ডিয়াক|বাইপাস|অ্যানজিওপ্লাস্টি/.test(text)) {
      return '⚡ ঢাবি Hot: হৃৎপিণ্ড ও রক্ত সংবহন (৯ বার)';
    }
    if (/মেন্ডেল|অসম্পূর্ণ\s*প্রকটতা|সমপ্রকটতা|লিথাল\s*জিন|এপিস্ট্যাসিস|দ্বৈত\s*প্রচ্ছন্ন/.test(text)) {
      return '⚡ ঢাবি Hot: মেন্ডেলের সূত্রের ব্যতিক্রম (৯ বার)';
    }
    if (/মাইটোকন্ড্রি|ক্রিস্টি|ATP\s*synthase/.test(text)) {
      return '⚡ ঢাবি Hot: মাইটোকন্ড্রিয়া (৮ বার)';
    }
    if (/DNA|RNA|ডাবল\s*হেলিক্স|শারগাফ|ট্রান্সক্রিপশন|ট্রান্সলেশন|জেনেটিক\s*কোড/.test(text)) {
      return '⚡ ঢাবি Hot: নিউক্লিক অ্যাসিড (৮ বার)';
    }
    if (/বর্তনী|তুল্য\s*রোধ|সার্কিট|অ্যাম্পিয়ার|রোধের\s*মান|হুইটস্টোন|তড়িচ্চালক/.test(text)) {
      return '⚡ ঢাবি হটস্পট: বর্তনী ও রোধের ম্যাথ';
    }
    if (/কার্বোক্যাটায়ন|ইলেকট্রোফাইল|নিউক্লিওফাইল|জৈব বিক্রিয়া|মারকনিকভ|বেনজিন|SN1|SN2|অ্যালকিন|ফ্রি\s*রেডিকেল/.test(text)) {
      return '⚡ ঢাবি হটস্পট: জৈব বিক্রিয়া মেকানিজম';
    }
    if (/লিমিট|ইন্টিগ্রেশন|ল['’]হপিটাল|\\lim|\\int|L['’]Hopital|যোজিত ফল/.test(text)) {
      return '⚡ ঢাবি হটস্পট: লিমিট ও ইন্টিগ্রেশন শর্টকাট';
    }
    return null;
  };

  const applyMiltonGoldenOrder = () => {
    const orderMap: Record<string, number> = {
      'Biology': 1,
      'Chemistry': 2,
      'Physics': 3,
      'Higher Math': 4,
    };
    const oldList = timedQuestions;
    const reordered = [...oldList].sort((a, b) => {
      const orderA = orderMap[a.subject] || 99;
      const orderB = orderMap[b.subject] || 99;
      return orderA - orderB;
    });
    const newAnswers: { [qIndex: number]: number | null } = {};
    const newSpent: { [qIndex: number]: number } = {};
    reordered.forEach((newQ, newIdx) => {
      const oldIdx = oldList.findIndex((q) => q.id === newQ.id);
      if (oldIdx !== -1 && selectedAnswers[oldIdx] !== undefined) {
        newAnswers[newIdx] = selectedAnswers[oldIdx];
      }
      if (oldIdx !== -1 && timeSpent[oldIdx] !== undefined) {
        newSpent[newIdx] = timeSpent[oldIdx];
      }
    });
    setTimedQuestions(reordered);
    setSelectedAnswers(newAnswers);
    setTimeSpent(newSpent);
    setTimedIndex(0);
  };

  // -------------------------------------------------------------
  // START SESSIONS
  // -------------------------------------------------------------
  const handleStartSession = (count: number, modeOverride?: 'mastery' | 'timed') => {
    const activeMode = modeOverride || practiceMode;
    if (modeOverride) {
      setPracticeMode(modeOverride);
    }
    const shuffled = [...availableQuestions].sort(() => Math.random() - 0.5);
    const chosen = shuffled.slice(0, Math.min(count, shuffled.length));

    // Dynamic shuffle of options array so correct answers distribute naturally across A, B, C, D
    const chosenWithShuffledOptions = chosen.map((q) => {
      const opts = [...(q.opts || q.options || [])];
      if (opts.length < 2) return q;
      const currentIdx = typeof q.ans === 'number' ? q.ans : (typeof q.correct_index === 'number' ? q.correct_index : 0);
      const correctVal = opts[currentIdx] ?? opts[0];
      const shuffledOpts = [...opts].sort(() => Math.random() - 0.5);
      const newAnsIdx = shuffledOpts.indexOf(correctVal);
      return {
        ...q,
        opts: shuffledOpts,
        options: shuffledOpts,
        ans: newAnsIdx,
        correct_index: newAnsIdx,
      };
    });

    if (activeMode === 'mastery') {
      const pool: MasteryQueueItem[] = chosenWithShuffledOptions.map((q) => ({
        question: q,
        consecutiveCorrect: 0,
        attempts: 0,
        wrongCount: 0,
        unsureCount: 0,
        status: 'learning',
      }));
      setMasteryPool(pool);
      // Active queue contains indices into pool
      setActiveQueueIndices(pool.map((_, i) => i));
      setCurrentQueuePos(0);
      setMasteryFeedback(null);
      setTotalRoundsAnswered(0);
    } else {
      setTimedQuestions(chosenWithShuffledOptions);
      setTimedIndex(0);
      setSelectedAnswers({});
      setTimeSpent({});
      setTimeLeft(45);
      hasSavedRef.current = false;
    }

    setSessionStarted(true);
    setSessionFinished(false);
  };

  // 1-Click Speed Drill Auto-Starter
  useEffect(() => {
    try {
      const autoStart = sessionStorage.getItem('admission_autostart_exam');
      if (autoStart === 'true') {
        sessionStorage.removeItem('admission_autostart_exam');
        if (availableQuestions.length > 0) {
          handleStartSession(Math.min(25, availableQuestions.length), 'mastery');
        }
      }
    } catch {
      // ignore
    }
  }, [availableQuestions]);

  // -------------------------------------------------------------
  // TIMED EXAM COUNTDOWN & AUTO-SKIP
  // -------------------------------------------------------------
  useEffect(() => {
    if (!sessionStarted || sessionFinished || practiceMode !== 'timed') return;

    if (timeLeft <= 0) {
      handleTimedNext(null); // Auto-skip on timeout
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft((prev) => prev - 1);
      setTimeSpent((prev) => ({
        ...prev,
        [timedIndex]: (prev[timedIndex] || 0) + 1,
      }));
    }, 1000);

    return () => clearInterval(timer);
  }, [sessionStarted, sessionFinished, timeLeft, timedIndex, practiceMode]);

  // Record completed timed exam to analytics
  useEffect(() => {
    if (!sessionFinished || hasSavedRef.current || timedQuestions.length === 0 || practiceMode !== 'timed') return;
    hasSavedRef.current = true;

    let correct = 0;
    let wrong = 0;
    let skipped = 0;
    const subjectCounts: { [subject: string]: { total: number; correct: number } } = {};

    timedQuestions.forEach((q, idx) => {
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
    const maxScore = timedQuestions.length * 1.0;
    const acc = correct + wrong > 0 ? Math.round((correct / (correct + wrong)) * 100) : 0;
    const totalSecs = Object.values(timeSpent).reduce((a, b) => a + b, 0);
    const avgSecs = timedQuestions.length > 0 ? Math.round(totalSecs / timedQuestions.length) : 0;

    const record: ExamAttemptRecord = {
      id: Date.now().toString(),
      timestamp: Date.now(),
      dateStr: new Date().toLocaleTimeString('bn-BD', { hour: '2-digit', minute: '2-digit' }),
      title: `${selectedWeek === 'all' ? 'All Weeks' : selectedWeek.toUpperCase()} • ${selectedSubject === 'All' ? 'সব বিষয়' : selectedSubject} টেস্ট`,
      totalQuestions: timedQuestions.length,
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
  }, [sessionFinished, timedQuestions, selectedAnswers, timeSpent, selectedWeek, selectedSubject, practiceMode]);

  const handleTimedOptionSelect = (optionIndex: number) => {
    setSelectedAnswers((prev) => ({
      ...prev,
      [timedIndex]: optionIndex,
    }));
  };

  const handleTimedNext = (finalAnswer: number | null) => {
    setSelectedAnswers((prev) => ({
      ...prev,
      [timedIndex]: finalAnswer,
    }));

    if (timedIndex + 1 < timedQuestions.length) {
      setTimedIndex((prev) => prev + 1);
      setTimeLeft(45);
    } else {
      setSessionFinished(true);
    }
  };

  // -------------------------------------------------------------
  // MASTERY DRILL LOGIC (LEITNER 2-STRIKE MASTERY ENGINE)
  // -------------------------------------------------------------
  const currentPoolIdx = activeQueueIndices[currentQueuePos];
  const currentMasteryItem = currentPoolIdx !== undefined ? masteryPool[currentPoolIdx] : null;

  const handleMasteryAnswer = (userChoice: number | null, isUnsure: boolean = false) => {
    if (!currentMasteryItem || masteryFeedback) return;

    if (autoAdvanceTimerRef.current) {
      clearTimeout(autoAdvanceTimerRef.current);
      autoAdvanceTimerRef.current = null;
    }

    const q = currentMasteryItem.question;
    const isCorrect = !isUnsure && userChoice !== null && userChoice === q.ans;
    setTotalRoundsAnswered((prev) => prev + 1);

    // Copy pool
    const newPool = [...masteryPool];
    const item = { ...newPool[currentPoolIdx] };
    item.attempts += 1;

    let feedbackMsg = '';
    let feedbackType: 'correct' | 'wrong' | 'unsure' = 'wrong';

    if (isUnsure) {
      item.unsureCount += 1;
      item.consecutiveCorrect = 0; // Reset streak
      feedbackType = 'unsure';
      feedbackMsg = '⚠️ সংশয় চিহ্নিত: সঠিক উত্তর দেখে নাও। প্রশ্নটি কিউতে রইল (পরপর ২ বার সঠিক করতে হবে)!';
    } else if (isCorrect) {
      item.consecutiveCorrect += 1;
      feedbackType = 'correct';

      if (item.consecutiveCorrect >= 2) {
        item.status = 'mastered';
        feedbackMsg = '🎉 মাস্টারড! পরপর ২ বার সঠিক উত্তর হয়েছে! 🏆';
        try {
          confetti({ particleCount: 35, spread: 50, origin: { y: 0.7 } });
        } catch {
          // ignore
        }
      } else {
        feedbackMsg = '✅ সঠিক উত্তর! আর ১ বার সঠিক করলে প্রশ্নটি মাস্টারড হবে।';
      }
    } else {
      item.wrongCount += 1;
      item.consecutiveCorrect = 0; // Reset streak
      feedbackType = 'wrong';
      feedbackMsg = '❌ ভুল উত্তর! সমাধানটি শিখে নাও। প্রশ্নটি কিউতে রইল (পরপর ২ বার সঠিক করতে হবে)!';
    }

    newPool[currentPoolIdx] = item;
    setMasteryPool(newPool);

    setMasteryFeedback({
      type: feedbackType,
      userChoice,
      message: feedbackMsg,
    });

    // Auto-advance if enabled and answer is correct
    if (autoAdvance && isCorrect) {
      autoAdvanceTimerRef.current = setTimeout(() => {
        handleMasteryNext(newPool);
      }, 500);
    }
  };

  const handleMasteryNext = (overridePool?: MasteryQueueItem[]) => {
    if (autoAdvanceTimerRef.current) {
      clearTimeout(autoAdvanceTimerRef.current);
      autoAdvanceTimerRef.current = null;
    }

    const activePool = overridePool || masteryPool;
    setMasteryFeedback(null);

    // Remaining unmastered indices in pool
    const unmastered = activePool
      .map((item, idx) => (item.status === 'learning' ? idx : -1))
      .filter((idx) => idx !== -1);

    if (unmastered.length === 0) {
      // All mastered!
      setSessionFinished(true);
      try {
        confetti({ particleCount: 100, spread: 80, origin: { y: 0.6 } });
      } catch {
        // ignore
      }
      return;
    }

    // Advance queue: if current item wasn't mastered, keep it in rotation
    let nextPos = currentQueuePos + 1;
    if (nextPos >= activeQueueIndices.length) {
      // Re-shuffle remaining unmastered indices for next rotation cycle
      const reRotated = [...unmastered].sort(() => Math.random() - 0.5);
      setActiveQueueIndices(reRotated);
      setCurrentQueuePos(0);
    } else {
      // Check if current position is still valid or unmastered
      if (activePool[activeQueueIndices[nextPos]]?.status === 'mastered') {
        // Find next unmastered in queue
        const remainingInCurrentQueue = activeQueueIndices
          .slice(nextPos)
          .filter((idx) => activePool[idx]?.status === 'learning');
        if (remainingInCurrentQueue.length > 0) {
          const nextIdx = remainingInCurrentQueue[0];
          setCurrentQueuePos(activeQueueIndices.indexOf(nextIdx));
        } else {
          setActiveQueueIndices([...unmastered].sort(() => Math.random() - 0.5));
          setCurrentQueuePos(0);
        }
      } else {
        setCurrentQueuePos(nextPos);
      }
    }
  };

  // -------------------------------------------------------------
  // FAST RECALL KEYBOARD SHORTCUTS
  // -------------------------------------------------------------
  useEffect(() => {
    if (!sessionStarted || sessionFinished) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      // Option choices 1-4 or A-D
      if (['1', 'a', 'A'].includes(e.key)) {
        if (practiceMode === 'mastery') handleMasteryAnswer(0);
        else handleTimedOptionSelect(0);
      } else if (['2', 'b', 'B'].includes(e.key)) {
        if (practiceMode === 'mastery') handleMasteryAnswer(1);
        else handleTimedOptionSelect(1);
      } else if (['3', 'c', 'C'].includes(e.key)) {
        if (practiceMode === 'mastery') handleMasteryAnswer(2);
        else handleTimedOptionSelect(2);
      } else if (['4', 'd', 'D'].includes(e.key)) {
        if (practiceMode === 'mastery') handleMasteryAnswer(3);
        else handleTimedOptionSelect(3);
      } else if (['u', 'U'].includes(e.key)) {
        if (practiceMode === 'mastery') handleMasteryAnswer(null, true);
      } else if (e.key === 'Enter' || e.code === 'Space') {
        if (practiceMode === 'mastery') {
          if (masteryFeedback) {
            e.preventDefault();
            handleMasteryNext();
          }
        } else {
          handleTimedNext(selectedAnswers[timedIndex] ?? null);
        }
      } else if (['s', 'S'].includes(e.key)) {
        if (practiceMode === 'timed') {
          handleTimedNext(null);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [
    sessionStarted, 
    sessionFinished, 
    practiceMode, 
    timedIndex, 
    selectedAnswers, 
    currentMasteryItem, 
    masteryFeedback, 
    currentQueuePos, 
    activeQueueIndices
  ]);

  // -------------------------------------------------------------
  // SCREEN 1: START SCREEN (MODERN EDTECH EXAM ROUTINE CARDS)
  // -------------------------------------------------------------
  if (!sessionStarted) {
    const totalAvail = availableQuestions.length;

    const getSubjectIcon = (subj: SubjectType) => {
      switch (subj) {
        case 'Physics': return '⚛️';
        case 'Chemistry': return '🧪';
        case 'Higher Math': return '📐';
        case 'Biology': return '🧬';
        case 'English': return '🇬🇧';
        case 'GK': return '🇧🇩';
        default: return '🎯';
      }
    };

    const getWeekDisplay = (w: WeekFilterType) => {
      if (w === 'all') return 'All-Week';
      return w.replace('_', '-').toUpperCase();
    };

    const routineSlots = [
      {
        id: 'slot_01',
        title: `${getWeekDisplay(selectedWeek)} ${selectedSubject === 'All' ? 'কোর' : selectedSubject} Slot-01: হাই-ইল্ড ক্যাপসুল`,
        badge: '✨ 80/20 High Yield',
        badgeColor: 'bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 ring-emerald-500/30',
        duration: 15,
        qCount: Math.min(12, totalAvail),
        marks: Math.min(12, totalAvail),
        desc: 'সবচেয়ে বেশি রিপিট হওয়া ১২টি কনসেপ্ট ও স্ট্যান্ডার্ড ঢাবি/মেডিকেল প্রশ্ন।'
      },
      {
        id: 'slot_02',
        title: `${getWeekDisplay(selectedWeek)} ${selectedSubject === 'All' ? 'কোর' : selectedSubject} Slot-02: ডিইউ রিপিট ড্রিল`,
        badge: '🔥 DU Repeat',
        badgeColor: 'bg-blue-500/15 text-blue-700 dark:text-blue-300 ring-blue-500/30',
        duration: 25,
        qCount: Math.min(25, totalAvail),
        marks: Math.min(25, totalAvail),
        desc: 'বিগত বছরের প্রশ্নভিত্তিক ২৫টি এক্সপেক্টেড ট্র্যাপ ও গতি অনুশীলনী।'
      },
      {
        id: 'slot_03',
        title: `${getWeekDisplay(selectedWeek)} ${selectedSubject === 'All' ? 'কোর' : selectedSubject} Slot-03: স্পিড অ্যান্ড ট্র্যাপ মক`,
        badge: '⚡ Trap Special',
        badgeColor: 'bg-amber-500/15 text-amber-700 dark:text-amber-300 ring-amber-500/30',
        duration: 45,
        qCount: Math.min(50, totalAvail),
        marks: Math.min(50, totalAvail),
        desc: 'নেগেটিভ মার্কিং এড়িয়ে ৫০টি প্রশ্নে সম্পূর্ণ পেপারের গতি ও দক্ষতা যাচাই।'
      },
    ].filter(slot => slot.qCount > 0);

    return (
      <div className="max-w-4xl mx-auto py-4 sm:py-6 px-3 sm:px-4 space-y-5">
        
        {/* Header Title with Glass Glow */}
        <div className="text-center max-w-xl mx-auto">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-500/20 text-xs font-bold mb-2">
            <span>{getSubjectIcon(selectedSubject)}</span>
            <span>{selectedSubject === 'All' ? 'সকল বিষয়' : selectedSubject} প্রশ্নব্যাংক</span>
          </div>

          <h2 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
            বাংলাদেশ এডমিশন কোর প্রশ্নব্যাংক ও স্লট রুটিন
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">
            বিগত ১৫–২০ বছরের ঢাবি ও মেডিকেল মূল প্রশ্ন, নো-ক্যালকুলেটর শর্টকাট এবং ট্র্যাপ অ্যানালাইসিস।
          </p>

          {/* Selected Scope Badges */}
          <div className="flex flex-wrap items-center justify-center gap-1.5 mt-3">
            <span className="px-3 py-1 rounded-full backdrop-blur-md bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800 text-xs text-slate-700 dark:text-slate-300 font-semibold shadow-xs">
              সপ্তাহ: <strong className="text-emerald-600 dark:text-emerald-400">{getWeekDisplay(selectedWeek)}</strong>
            </span>
            <span className="px-3 py-1 rounded-full backdrop-blur-md bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800 text-xs text-slate-700 dark:text-slate-300 font-semibold shadow-xs">
              বিষয়: <strong className="text-cyan-600 dark:text-cyan-400">{selectedSubject}</strong>
            </span>
            <span className="px-3 py-1 rounded-full backdrop-blur-md bg-white/80 dark:bg-slate-900/80 ring-1 ring-slate-200/80 dark:ring-slate-800 text-xs text-slate-700 dark:text-slate-300 font-semibold shadow-xs">
              উপলব্ধ প্রশ্ন: <strong className="text-amber-600 dark:text-amber-400">{totalAvail}টি</strong>
            </span>
          </div>
        </div>

        {/* =========================================================================
            MODERN EDTECH EXAM ROUTINE CARDS GRID
           ========================================================================= */}
        <div className="space-y-3.5">
          <div className="flex items-center justify-between text-xs font-bold text-slate-500 dark:text-slate-400 px-1">
            <span>🗓️ সিলেক্টেড উইক রুটিন স্লট</span>
            <span>{totalAvail}টি প্রশ্ন থেকে তৈরি</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5">
            {routineSlots.map((slot) => (
              <div 
                key={slot.id}
                className="group rounded-3xl backdrop-blur-xl bg-white/85 dark:bg-slate-900/85 ring-1 ring-slate-200/80 dark:ring-slate-800/80 hover:ring-emerald-500/50 dark:hover:ring-emerald-500/50 shadow-sm p-4 sm:p-5 flex flex-col justify-between transition-all duration-200"
              >
                <div>
                  {/* Card Header with Status Chip */}
                  <div className="flex items-center justify-between gap-2 mb-2.5">
                    <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold ring-1 ${slot.badgeColor}`}>
                      {slot.badge}
                    </span>
                    <span className="text-[11px] font-mono text-slate-500 flex items-center gap-1">
                      ⏱️ {slot.duration} মি.
                    </span>
                  </div>

                  {/* Slot Title */}
                  <div className="flex items-start gap-2 mb-2">
                    <span className="text-xl mt-0.5">{getSubjectIcon(selectedSubject)}</span>
                    <h3 className="text-sm font-extrabold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors leading-snug">
                      {slot.title}
                    </h3>
                  </div>

                  {/* Clean Metadata Row with Icons */}
                  <div className="flex items-center gap-2 text-[11px] font-medium text-slate-500 dark:text-slate-400 py-2 border-y border-slate-100 dark:border-slate-800/80 my-2">
                    <span className="flex items-center gap-1">
                      ⏱️ সময় ({slot.duration} মি.)
                    </span>
                    <span>•</span>
                    <span className="flex items-center gap-1">
                      📝 {slot.qCount}টি প্রশ্ন
                    </span>
                    <span>•</span>
                    <span className="flex items-center gap-1">
                      🎯 {slot.marks} মার্কস
                    </span>
                  </div>

                  <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed mb-4">
                    {slot.desc}
                  </p>
                </div>

                {/* Dual Call to Action Buttons */}
                <div className="grid grid-cols-2 gap-2 pt-2 border-t border-slate-100 dark:border-slate-800/80">
                  <button
                    onClick={() => handleStartSession(slot.qCount, 'mastery')}
                    className="py-2.5 px-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-xs transition-all flex items-center justify-center gap-1 active:scale-95 cursor-pointer"
                    title="বারবার প্র্যাকটিস ড্রিল (পরপর ২ বার সঠিক = মাস্টারড)"
                  >
                    <RotateCcw className="w-3.5 h-3.5" />
                    <span>প্র্যাকটিস শুরু</span>
                  </button>

                  <button
                    onClick={() => handleStartSession(slot.qCount, 'timed')}
                    className="py-2.5 px-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200 text-xs font-bold ring-1 ring-slate-200 dark:ring-slate-700 transition-all flex items-center justify-center gap-1 active:scale-95 cursor-pointer"
                    title="৪৫ সেকেন্ডের টাইমারসহ টাইমড এক্সাম"
                  >
                    <Timer className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                    <span>টাইমড টেস্ট</span>
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Quick Custom Count Launcher */}
        <div className="p-4 sm:p-5 rounded-3xl backdrop-blur-xl bg-white/70 dark:bg-slate-900/70 ring-1 ring-slate-200/80 dark:ring-slate-800/80 shadow-xs max-w-xl mx-auto text-center space-y-3">
          <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
            কাস্টম প্রশ্নের সংখ্যা নির্বাচন
          </div>
          <div className="flex items-center justify-center gap-2 flex-wrap">
            {[10, 25, 50, Math.min(100, totalAvail), totalAvail]
              .filter((v, i, a) => a.indexOf(v) === i && v <= totalAvail && v > 0)
              .map((cnt) => (
                <button
                  key={cnt}
                  onClick={() => setQuestionCount(cnt)}
                  className={`py-1.5 px-3 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                    questionCount === cnt
                      ? 'bg-[#056839] text-white shadow-xs scale-105'
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 ring-1 ring-slate-200 dark:ring-slate-700 hover:bg-slate-200 dark:hover:bg-slate-700'
                  }`}
                >
                  {cnt === totalAvail ? `সকল (${cnt})` : `${cnt} টি`}
                </button>
              ))}
          </div>

          <div className="flex items-center justify-center gap-2 pt-2">
            <button
              onClick={() => handleStartSession(questionCount, 'mastery')}
              disabled={totalAvail === 0}
              className="py-2.5 px-5 rounded-2xl bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold shadow-md shadow-[#056839]/20 transition-all flex items-center gap-1.5 active:scale-95 disabled:opacity-40 cursor-pointer"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>মাস্টারি ড্রিল ({Math.min(questionCount, totalAvail)}টি)</span>
            </button>
            <button
              onClick={() => handleStartSession(questionCount, 'timed')}
              disabled={totalAvail === 0}
              className="py-2.5 px-5 rounded-2xl bg-slate-900 dark:bg-slate-800 hover:bg-slate-800 text-white text-xs font-bold shadow-xs transition-all flex items-center gap-1.5 active:scale-95 disabled:opacity-40 cursor-pointer"
            >
              <Timer className="w-3.5 h-3.5 text-amber-400" />
              <span>টাইমড টেস্ট ({Math.min(questionCount, totalAvail)}টি)</span>
            </button>
          </div>
        </div>

      </div>
    );
  }

  // -------------------------------------------------------------
  // SCREEN 2A: FINISHED MASTERY SESSION SUMMARY
  // -------------------------------------------------------------
  if (sessionFinished && practiceMode === 'mastery') {
    const totalMastered = masteryPool.filter((i) => i.status === 'mastered').length;
    const totalWrongs = masteryPool.reduce((acc, i) => acc + i.wrongCount, 0);
    const totalUnsures = masteryPool.reduce((acc, i) => acc + i.unsureCount, 0);

    return (
      <div className="max-w-2xl mx-auto py-8 px-3 sm:px-4 text-center">
        <div className="bg-white dark:bg-zinc-900 p-6 sm:p-8 rounded-3xl border border-zinc-200/80 dark:border-zinc-800 shadow-sm relative overflow-hidden">
          <div className="w-14 h-14 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mx-auto mb-3 shadow-xs">
            <Award className="w-8 h-8" />
          </div>

          <h2 className="text-2xl font-black text-zinc-900 dark:text-white">
            🎉 মিশন সফল! সকল প্রশ্ন ১০০% মাস্টারড!
          </h2>
          <p className="text-xs sm:text-sm text-zinc-500 dark:text-zinc-400 mt-1">
            নির্বাচিত {totalMastered}টি প্রশ্নই তুমি পরপর ২ বার নির্ভুল উত্তর দিয়ে আয়ত্ত করেছো।
          </p>

          {/* Stats Grid */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 my-6 max-w-lg mx-auto">
            <div className="p-3 rounded-2xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/40 text-center">
              <span className="text-[11px] text-emerald-800 dark:text-emerald-300 font-semibold">মাস্টারড প্রশ্ন</span>
              <div className="text-xl font-black text-emerald-600 dark:text-emerald-400 mt-0.5">
                {totalMastered} / {masteryPool.length}
              </div>
            </div>
            <div className="p-3 rounded-2xl bg-zinc-50 dark:bg-zinc-800/60 border border-zinc-200 dark:border-zinc-700 text-center">
              <span className="text-[11px] text-zinc-600 dark:text-zinc-400 font-semibold">মোট ড্রিল রাউন্ড</span>
              <div className="text-xl font-black text-zinc-800 dark:text-zinc-200 mt-0.5">
                {totalRoundsAnswered} বার
              </div>
            </div>
            <div className="p-3 rounded-2xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800/40 text-center">
              <span className="text-[11px] text-rose-800 dark:text-rose-300 font-semibold">রি-টেস্টে ভুল</span>
              <div className="text-xl font-black text-rose-600 dark:text-rose-400 mt-0.5">
                {totalWrongs}
              </div>
            </div>
            <div className="p-3 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/40 text-center">
              <span className="text-[11px] text-amber-800 dark:text-amber-300 font-semibold">সংশয় চিহ্নিত</span>
              <div className="text-xl font-black text-amber-600 dark:text-amber-400 mt-0.5">
                {totalUnsures}
              </div>
            </div>
          </div>

          <div className="flex justify-center gap-3">
            <button
              onClick={() => handleStartSession(questionCount)}
              className="flex items-center gap-2 px-6 py-3 rounded-full bg-[#056839] hover:bg-[#044e2b] text-white font-bold text-sm shadow-md transition-all hover:scale-105 active:scale-95 cursor-pointer"
            >
              <RotateCcw className="w-4 h-4" />
              <span>আবার অনুশীলন করুন</span>
            </button>
            <button
              onClick={() => setSessionStarted(false)}
              className="px-5 py-3 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700 text-sm font-semibold transition-all hover:bg-zinc-200 cursor-pointer"
            >
              সেটিংস পরিবর্তন
            </button>
          </div>
        </div>
      </div>
    );
  }

  // -------------------------------------------------------------
  // SCREEN 2B: FINISHED TIMED EXAM SCORECARD & TRAP DEFENSE
  // -------------------------------------------------------------
  if (sessionFinished && practiceMode === 'timed') {
    let correctCount = 0;
    let wrongCount = 0;
    let skippedCount = 0;

    timedQuestions.forEach((q, idx) => {
      const ans = selectedAnswers[idx];
      if (ans === undefined || ans === null) skippedCount++;
      else if (ans === q.ans) correctCount++;
      else wrongCount++;
    });

    const totalScore = correctCount * 1.0 - wrongCount * 0.25;
    const maxPossible = timedQuestions.length * 1.0;
    const isPassing = totalScore >= maxPossible * 0.4;
    const accuracy = correctCount + wrongCount > 0 ? Math.round((correctCount / (correctCount + wrongCount)) * 100) : 0;
    const totalSeconds = Object.values(timeSpent).reduce((a, b) => a + b, 0);
    const avgTimePerQ = timedQuestions.length > 0 ? Math.round(totalSeconds / timedQuestions.length) : 0;

    const reviewList = timedQuestions.filter((q, idx) => {
      if (filterReview === 'wrong') {
        const userAns = selectedAnswers[idx];
        return userAns === null || userAns === undefined || userAns !== q.ans;
      }
      return true;
    });

    return (
      <div className="max-w-3xl mx-auto py-6 px-3 sm:px-4">
        {/* Scorecard Hero */}
        <div className="bg-white dark:bg-zinc-900 p-5 sm:p-6 rounded-3xl border border-zinc-200/80 dark:border-zinc-800 shadow-sm text-center relative overflow-hidden mb-6">
          <div className="flex items-center justify-center gap-2 mb-1.5">
            <Award className={`w-7 h-7 ${isPassing ? 'text-amber-500' : 'text-zinc-400'}`} />
            <h2 className="text-lg sm:text-xl font-black text-zinc-900 dark:text-white">
              {isPassing ? 'অভিনন্দন! চমৎকার প্রস্তুতি' : 'টাইমড টেস্ট সম্পন্ন হয়েছে'}
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

          <div className="mt-6 flex justify-center gap-3">
            <button
              onClick={() => handleStartSession(questionCount)}
              className="flex items-center gap-2 px-6 py-2.5 rounded-full bg-[#056839] hover:bg-[#044e2b] text-white font-bold text-sm shadow-md transition-all hover:scale-105 active:scale-95 cursor-pointer"
            >
              <RotateCcw className="w-4 h-4" />
              <span>পুনরায় পরীক্ষা দিন</span>
            </button>
            <button
              onClick={() => setSessionStarted(false)}
              className="px-5 py-2.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700 text-sm font-semibold transition-all hover:bg-zinc-200 cursor-pointer"
            >
              সেটিংস পরিবর্তন
            </button>
          </div>
        </div>

        {/* Trap Defense Section */}
        <div className="flex flex-wrap items-center justify-between pb-3 mb-4 border-b border-zinc-200 dark:border-zinc-800 gap-2">
          <div className="flex items-center gap-2">
            <ShieldAlert className="w-5 h-5 text-amber-500 dark:text-amber-400" />
            <h3 className="text-lg font-bold text-zinc-900 dark:text-white">
              ট্র্যাপ ডিফেন্স রিভিউ (ফাঁদ বিশ্লেষণ ও সলিউশন)
            </h3>
          </div>
          <div className="flex items-center gap-1.5 bg-zinc-100 dark:bg-zinc-900 p-1 rounded-xl border border-zinc-200 dark:border-zinc-800">
            <button
              onClick={() => setFilterReview('all')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filterReview === 'all' 
                  ? 'bg-white dark:bg-zinc-800 text-zinc-900 dark:text-white shadow-xs' 
                  : 'text-zinc-600 dark:text-zinc-400'
              }`}
            >
              সকল প্রশ্ন ({timedQuestions.length})
            </button>
            <button
              onClick={() => setFilterReview('wrong')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filterReview === 'wrong' 
                  ? 'bg-rose-100 dark:bg-rose-500/20 text-rose-800 dark:text-rose-300 font-bold' 
                  : 'text-zinc-600 dark:text-zinc-400'
              }`}
            >
              শুধু ভুল/স্কিপ ({wrongCount + skippedCount})
            </button>
          </div>
        </div>

        {/* Review Questions List */}
        <div className="space-y-4">
          {reviewList.map((q) => {
            const originalIndex = timedQuestions.indexOf(q);
            const userAns = selectedAnswers[originalIndex];
            const isCorrect = userAns === q.ans;
            const isSkipped = userAns === undefined || userAns === null;
            const { origin, cleanText } = parseQuestionData(q);

            return (
              <div 
                key={q.id}
                className={`p-4 sm:p-5 rounded-2xl border transition-all ${
                  isCorrect 
                    ? 'bg-white dark:bg-zinc-900/60 border-emerald-200 dark:border-emerald-500/30 shadow-xs' 
                    : isSkipped 
                    ? 'bg-white dark:bg-zinc-900/60 border-zinc-200 dark:border-zinc-800 shadow-xs' 
                    : 'bg-white dark:bg-zinc-900/90 border-rose-300 dark:border-rose-500/40 shadow-xs'
                }`}
              >
                <div className="flex items-start justify-between gap-3 mb-2.5">
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700">
                      প্রশ্ন: {originalIndex + 1} / {timedQuestions.length} টি
                    </span>
                    <span className={`text-[11px] font-bold px-2.5 py-0.5 rounded-full border ${getOriginBadgeStyle(origin)}`}>
                      📍 {origin}
                    </span>
                    <span className="text-xs font-medium px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-700">
                      {q.subject}
                    </span>
                    {q.expected_count !== undefined && q.expected_count !== null && (
                      <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 shadow-xs inline-flex items-center gap-1">
                        <span>🎯 প্রত্যাশিত ফ্রিকোয়েন্সি: {typeof q.expected_count === 'number' ? `${q.expected_count} বার` : q.expected_count}</span>
                      </span>
                    )}
                  </div>

                  {isCorrect ? (
                    <span className="flex items-center gap-1 text-xs font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2 py-0.5 rounded-lg border border-emerald-200 dark:border-emerald-500/20">
                      <CheckCircle2 className="w-3.5 h-3.5" /> +১.০ সঠিক
                    </span>
                  ) : isSkipped ? (
                    <span className="flex items-center gap-1 text-xs font-bold text-zinc-600 dark:text-zinc-400 bg-zinc-100 dark:bg-zinc-800 px-2 py-0.5 rounded-lg border border-zinc-200 dark:border-zinc-700">
                      <MinusCircle className="w-3.5 h-3.5" /> ০.০ স্কিপ
                    </span>
                  ) : (
                    <span className="flex items-center gap-1 text-xs font-bold text-rose-700 dark:text-rose-400 bg-rose-50 dark:bg-rose-500/10 px-2 py-0.5 rounded-lg border border-rose-200 dark:border-rose-500/20">
                      <XCircle className="w-3.5 h-3.5" /> -০.২৫ ভুল
                    </span>
                  )}
                </div>

                <div className="flex items-center gap-2 mb-2">
                  <span className="text-[11px] font-semibold px-2 py-0.5 rounded border bg-amber-50 text-amber-800 border-amber-200">
                    {(q as any).source || (q as any).source_tag || origin || "🎯 ২০২৬ প্রেডিক্টর"}
                  </span>
                </div>

                <div className="text-sm sm:text-base font-semibold text-zinc-900 dark:text-white mb-3">
                  <MathText content={cleanText} />
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-3">
                  {q.opts.map((opt, optIdx) => {
                    const isSelected = userAns === optIdx;
                    const isRightOpt = q.ans === optIdx;

                    let optStyle = 'bg-zinc-50 dark:bg-zinc-800/40 border-zinc-200 dark:border-zinc-700/50 text-zinc-800 dark:text-zinc-300';
                    if (isRightOpt) {
                      optStyle = 'bg-emerald-50 dark:bg-emerald-500/15 border-emerald-300 dark:border-emerald-500/60 text-emerald-900 dark:text-emerald-200 font-semibold';
                    } else if (isSelected && !isRightOpt) {
                      optStyle = 'bg-rose-50 dark:bg-rose-500/15 border-rose-300 dark:border-rose-500/60 text-rose-900 dark:text-rose-200';
                    }

                    return (
                      <div
                        key={optIdx}
                        className={`p-2.5 rounded-xl border flex items-center gap-2.5 text-xs sm:text-sm ${optStyle}`}
                      >
                        <span className="w-5 h-5 rounded-md flex items-center justify-center font-bold text-xs bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-700 text-zinc-700 dark:text-zinc-300 shrink-0">
                          {String.fromCharCode(65 + optIdx)}
                        </span>
                        <div className="flex-1">
                          <MathText content={opt} />
                        </div>
                      </div>
                    );
                  })}
                </div>

                {/* Speed Hack Section */}
                {q.speed_hack && (
                  <div className="bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-200 dark:border-emerald-500/20 rounded-xl p-2.5 mb-2 flex items-start gap-2">
                    <Zap className="w-4 h-4 text-emerald-600 dark:text-emerald-400 mt-0.5 shrink-0" />
                    <div className="text-xs text-emerald-950 dark:text-emerald-200 leading-relaxed">
                      <strong className="text-emerald-700 dark:text-emerald-400 font-bold mr-1">⚡ স্পিড হ্যাক:</strong>
                      <MathText content={q.speed_hack} />
                    </div>
                  </div>
                )}

                {/* Trap Defense Section (Strict Conditional Rendering) */}
                {(() => {
                  const trapAlert = (q.trap_alert || q.trap || '').trim();
                  const isBoilerplate = trapAlert.includes('পিত্তরসে কোনো পরিপাক এনজাইম থাকে না') && 
                    (!q.q.includes('পিত্ত') && !q.q.includes('যকৃৎ') && !q.q.includes('bile'));
                  if (!trapAlert || isBoilerplate) return null;
                  return (
                    <div className="bg-amber-50 dark:bg-amber-500/10 border border-amber-200 dark:border-amber-500/20 rounded-xl p-2.5 mb-2 flex items-start gap-2">
                      <AlertCircle className="w-4 h-4 text-amber-500 dark:text-amber-400 mt-0.5 shrink-0" />
                      <div className="text-xs text-amber-900 dark:text-amber-200 leading-relaxed">
                        <strong className="text-amber-700 dark:text-amber-400 font-bold mr-1">ফাঁদ বিশ্লেষণ:</strong>
                        <MathText content={trapAlert} />
                      </div>
                    </div>
                  );
                })()}

                <div className="bg-zinc-50 dark:bg-zinc-800/50 rounded-xl p-2.5 text-xs text-zinc-700 dark:text-zinc-300 leading-relaxed border border-zinc-200 dark:border-zinc-700/50">
                  <strong className="text-[#056839] dark:text-emerald-400 block mb-0.5">স্ট্যান্ডার্ড সমাধান ও ব্যাখ্যা:</strong>
                  <MathText content={q.exp} block />
                </div>
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  // -------------------------------------------------------------
  // SCREEN 3A: ACTIVE MASTERY DRILL QUESTION
  // -------------------------------------------------------------
  if (practiceMode === 'mastery' && currentMasteryItem) {
    const q = currentMasteryItem.question;
    const { origin, cleanText } = parseQuestionData(q);
    const consecutive = currentMasteryItem.consecutiveCorrect;
    const masteredCount = masteryPool.filter((i) => i.status === 'mastered').length;
    const remainingUnmastered = masteryPool.length - masteredCount;
    const progressPercent = Math.round((masteredCount / masteryPool.length) * 100);

    return (
      <div className="max-w-2xl mx-auto py-3 px-3 sm:px-4">
        {/* Top Sticky Recall Bar */}
        <div className="bg-white dark:bg-zinc-900 p-3 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 shadow-xs mb-3 flex items-center justify-between gap-3">
          {/* Left: Mastered progress */}
          <div className="flex items-center gap-2">
            <span className="w-8 h-8 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold text-xs">
              <Zap className="w-4 h-4" />
            </span>
            <div className="text-left">
              <div className="text-xs font-bold text-zinc-900 dark:text-white flex items-center gap-1.5">
                <span>মাস্টারড: {masteredCount} / {masteryPool.length}</span>
                <span className="text-[11px] font-mono text-emerald-600 dark:text-emerald-400 font-bold">({progressPercent}%)</span>
              </div>
              <div className="text-[11px] text-zinc-500 dark:text-zinc-400">
                বাকি কিউ: {remainingUnmastered}টি • ড্রিল রাউন্ড: #{totalRoundsAnswered + 1}
              </div>
            </div>
          </div>

          {/* Right: Auto Advance Toggle & Question Mastery Dots */}
          <div className="flex items-center gap-2">
            <button
              onClick={() => setAutoAdvance(!autoAdvance)}
              className={`px-2.5 py-1 rounded-full text-[11px] font-bold border transition-all cursor-pointer ${
                autoAdvance 
                  ? 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border-emerald-300 dark:border-emerald-700' 
                  : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-500 border-zinc-200 dark:border-zinc-700'
              }`}
              title="সঠিক উত্তর হলে ৩৫০ মিলিসেকেন্ডে অটোমেটিক পরের প্রশ্নে যাবে"
            >
              ⚡ ফাস্ট মোড: {autoAdvance ? 'ON' : 'OFF'}
            </button>
          </div>
        </div>

        {/* Progress Bar */}
        <div className="w-full bg-zinc-200 dark:bg-zinc-800 h-1.5 rounded-full overflow-hidden mb-3">
          <div 
            className="h-full bg-gradient-to-r from-[#00B09B] to-[#96C93D] transition-all duration-300"
            style={{ width: `${progressPercent}%` }}
          />
        </div>

        {/* Question Card (Compact Fast-Recall layout) */}
        <div className="bg-white dark:bg-zinc-900 rounded-3xl p-4 sm:p-5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm mb-3">
          {/* Card Origin & Status Header */}
          <div className="flex items-center justify-between gap-2 mb-2.5">
            <div className="flex items-center gap-1.5 flex-wrap">
              <span className="text-xs font-mono font-bold px-2.5 py-0.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700 shadow-xs">
                প্রশ্ন: {currentQueuePos + 1} / {activeQueueIndices.length} টি
              </span>
              <span className={`text-[11px] font-black px-2.5 py-0.5 rounded-full border shadow-xs ${getOriginBadgeStyle(origin)}`}>
                📍 {origin}
              </span>
              <span className="text-xs px-2.5 py-0.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-700 font-medium">
                {q.subject}
              </span>
              {q.expected_count !== undefined && q.expected_count !== null && (
                <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 shadow-xs inline-flex items-center gap-1">
                  <span>🎯 প্রত্যাশিত ফ্রিকোয়েন্সি: {typeof q.expected_count === 'number' ? `${q.expected_count} বার` : q.expected_count}</span>
                </span>
              )}
              {q.yield_stars && (
                <span className="text-xs px-2 py-0.5 rounded-full bg-amber-50 dark:bg-amber-950/40 text-amber-600 dark:text-amber-400 border border-amber-200 dark:border-amber-800 font-bold">
                  {'⭐️'.repeat(q.yield_stars)}
                </span>
              )}
            </div>

            {/* Mastery 2-Check Dots */}
            <div className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-zinc-100 dark:bg-zinc-800/80 border border-zinc-200 dark:border-zinc-700 text-xs font-bold">
              <span className="text-zinc-500 dark:text-zinc-400 text-[11px]">মাস্টারি:</span>
              <div className="flex items-center gap-1">
                <span className={`w-3 h-3 rounded-full border flex items-center justify-center transition-all ${
                  consecutive >= 1 
                    ? 'bg-emerald-500 border-emerald-500 text-white' 
                    : 'bg-transparent border-zinc-300 dark:border-zinc-600'
                }`}>
                  {consecutive >= 1 && <Check className="w-2.5 h-2.5 stroke-[3]" />}
                </span>
                <span className={`w-3 h-3 rounded-full border flex items-center justify-center transition-all ${
                  consecutive >= 2 
                    ? 'bg-emerald-500 border-emerald-500 text-white' 
                    : 'bg-transparent border-zinc-300 dark:border-zinc-600'
                }`}>
                  {consecutive >= 2 && <Check className="w-2.5 h-2.5 stroke-[3]" />}
                </span>
              </div>
              <span className="text-[11px] text-zinc-500 font-mono">({consecutive}/2)</span>
            </div>
          </div>

          {/* Recurring Hotspot Badge */}
          {(() => {
            const badge = getHotspotBadge(q);
            if (!badge) return null;
            return (
              <div className="mb-2.5">
                <span className="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold bg-amber-500/15 text-amber-800 dark:text-amber-300 border border-amber-500/30 inline-flex items-center gap-1 shadow-xs">
                  <Zap className="w-3.5 h-3.5 text-amber-500" />
                  {badge}
                </span>
              </div>
            );
          })()}

          {/* Question Text */}
          <div className="flex items-center gap-2 mb-2 flex-wrap">
            <span className="text-[11px] font-semibold px-2 py-0.5 rounded border bg-amber-50 text-amber-800 border-amber-200">
              {(q as any).source || (q as any).source_tag || origin || "🎯 ২০২৬ প্রেডিক্টর"}
            </span>
            {q.written_essential && (
              <span className="text-[11px] font-bold px-2 py-0.5 rounded border bg-violet-500/15 text-violet-700 dark:text-violet-300 border-violet-500/30">
                ✍️ Written Essential
              </span>
            )}
          </div>

          <div className="text-lg font-medium leading-relaxed text-zinc-900 dark:text-white mb-4 overflow-x-auto no-scrollbar">
            <MathText content={cleanText} />
          </div>

          {/* Options (Fast Click / Keyboard 1-4) */}
          <div className="space-y-2">
            {q.opts.map((opt, optIdx) => {
              const isSelected = masteryFeedback?.userChoice === optIdx;
              const isCorrectAnswer = q.ans === optIdx;

              let style = 'bg-zinc-50 dark:bg-zinc-800/60 border-zinc-200 dark:border-zinc-800 text-zinc-800 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800';

              if (masteryFeedback) {
                if (isCorrectAnswer) {
                  style = 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 font-bold';
                } else if (isSelected && !isCorrectAnswer) {
                  style = 'bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-900 dark:text-rose-200 font-bold';
                } else {
                  style = 'bg-zinc-50/50 dark:bg-zinc-800/30 border-zinc-200/50 dark:border-zinc-800/50 opacity-60';
                }
              }

              return (
                <button
                  key={optIdx}
                  onClick={() => handleMasteryAnswer(optIdx)}
                  disabled={masteryFeedback !== null}
                  className={`w-full text-base py-3 px-4 rounded-2xl border text-left flex items-center gap-3 transition-all cursor-pointer ${style}`}
                >
                  <span className={`w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 transition-all ${
                    masteryFeedback && isCorrectAnswer
                      ? 'bg-emerald-500 text-white'
                      : masteryFeedback && isSelected
                      ? 'bg-rose-500 text-white'
                      : 'bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700'
                  }`}>
                    {String.fromCharCode(65 + optIdx)}
                  </span>
                  <div className="flex-1 text-base leading-relaxed overflow-x-auto no-scrollbar">
                    <MathText content={opt} />
                  </div>
                </button>
              );
            })}
          </div>

          {/* Feedback & Solution Popup inside card when answered */}
          {masteryFeedback && (
            <div className="mt-3.5 pt-3 border-t border-zinc-200 dark:border-zinc-800 space-y-2 animate-in fade-in duration-200">
              {/* Status Message */}
              <div className={`p-2.5 rounded-xl border text-xs font-bold flex items-center justify-between ${
                masteryFeedback.type === 'correct'
                  ? 'bg-emerald-50 dark:bg-emerald-950/30 border-emerald-200 dark:border-emerald-800 text-emerald-800 dark:text-emerald-200'
                  : masteryFeedback.type === 'unsure'
                  ? 'bg-amber-50 dark:bg-amber-950/30 border-amber-200 dark:border-amber-800 text-amber-800 dark:text-amber-200'
                  : 'bg-rose-50 dark:bg-rose-950/30 border-rose-200 dark:border-rose-800 text-rose-800 dark:text-rose-200'
              }`}>
                <span>{masteryFeedback.message}</span>
                <span className="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-white dark:bg-zinc-900 border">
                  Space / Enter ⏎
                </span>
              </div>

              {/* Speed Hack */}
              {q.speed_hack && (
                <div className="bg-emerald-50/70 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-800/40 rounded-xl p-3 text-sm md:text-base leading-relaxed text-emerald-950 dark:text-emerald-200 flex items-start gap-2">
                  <Zap className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0 mt-0.5" />
                  <div>
                    <strong className="text-emerald-700 dark:text-emerald-400 font-bold mr-1">⚡ স্পিড হ্যাক:</strong>
                    <MathText content={q.speed_hack} />
                  </div>
                </div>
              )}

              {/* Trap Insight (Strict Conditional Rendering) */}
              {(() => {
                const currentTrap = (q.trap_alert || q.trap || '').trim();
                const isBoilerplate = currentTrap.includes('পিত্তরসে কোনো পরিপাক এনজাইম থাকে না') && 
                  (!q.q.includes('পিত্ত') && !q.q.includes('যকৃৎ') && !q.q.includes('bile'));
                if (!currentTrap || isBoilerplate) return null;
                return (
                  <div className="bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200 dark:border-amber-800/40 rounded-xl p-3 text-sm md:text-base leading-relaxed text-amber-900 dark:text-amber-200 flex items-start gap-2">
                    <AlertCircle className="w-4 h-4 text-amber-500 shrink-0 mt-0.5" />
                    <div>
                      <strong className="text-amber-700 dark:text-amber-400 font-bold mr-1">ফাঁদ বিশ্লেষণ:</strong>
                      <MathText content={currentTrap} />
                    </div>
                  </div>
                );
              })()}

              {/* Detailed Explanation */}
              <div className="bg-zinc-50 dark:bg-zinc-800/50 rounded-xl p-3 text-sm md:text-base text-zinc-700 dark:text-zinc-300 leading-relaxed border border-zinc-200 dark:border-zinc-700/60">
                <strong className="text-[#056839] dark:text-emerald-400 block mb-0.5 font-bold">স্ট্যান্ডার্ড সমাধান:</strong>
                <MathText content={q.exp} block />
              </div>
            </div>
          )}
        </div>

        {/* Action Bottom Bar */}
        <div className="flex items-center justify-between gap-2.5">
          {/* Unsure / Doubt Button */}
          <button
            onClick={() => handleMasteryAnswer(null, true)}
            disabled={masteryFeedback !== null}
            className="flex items-center gap-1.5 px-4 py-2.5 rounded-full bg-amber-50 dark:bg-amber-950/30 hover:bg-amber-100 dark:hover:bg-amber-900/40 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-700/60 text-xs sm:text-sm font-bold shadow-xs transition-all disabled:opacity-40 cursor-pointer"
            title="সংশয় চিহ্নিত করলে প্রশ্নটি কিউতে থাকবে যাতে ২ বার নির্ভুল উত্তর দেওয়া যায়"
          >
            <HelpCircle className="w-4 h-4" />
            <span>সংশয় / Unsure (U)</span>
          </button>

          {/* Micro Helper */}
          <span className="hidden sm:inline text-xs text-zinc-400 font-mono">
            <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700">1-4</kbd> বিকল্প | <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700">U</kbd> সংশয় | <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700">Space</kbd> পরবর্তী
          </span>

          {/* Next Button */}
          <button
            onClick={() => handleMasteryNext()}
            disabled={masteryFeedback === null}
            className="flex items-center gap-2 px-6 py-2.5 rounded-full bg-[#056839] hover:bg-[#044e2b] text-white text-xs sm:text-sm font-bold shadow-md shadow-[#056839]/20 transition-all disabled:opacity-40 active:scale-95 cursor-pointer"
          >
            <span>পরবর্তী প্রশ্ন</span>
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    );
  }

  // -------------------------------------------------------------
  // SCREEN 3B: ACTIVE TIMED EXAM QUESTION
  // -------------------------------------------------------------
  const currentTimedQ = timedQuestions[timedIndex];
  const userSelected = selectedAnswers[timedIndex];
  const timerPercent = (timeLeft / 45) * 100;
  const isTimeCritical = timeLeft <= 10;
  const { origin: timedOrigin, cleanText: timedCleanText } = currentTimedQ ? parseQuestionData(currentTimedQ) : { origin: "DU Core", cleanText: "" };
  const timedHotspot = currentTimedQ ? getHotspotBadge(currentTimedQ) : null;

  return (
    <div className="max-w-2xl mx-auto py-3 px-3 sm:px-4">
      {/* Milton Khandokar Golden Order 1-Click Action */}
      <div className="flex items-center justify-between gap-2 mb-2">
        <button
          onClick={applyMiltonGoldenOrder}
          title="বায়োলজি ➔ রসায়ন ➔ পদার্থ ➔ গণিত ক্রমানুসারে সাজান"
          className="w-full py-1.5 px-3 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-800 text-[11px] sm:text-xs font-bold transition-all flex items-center justify-center gap-1.5 shadow-xs cursor-pointer"
        >
          <span>⚡ মিল্টন স্যারের গোল্ডেন অর্ডার: বায়োলজি ➔ রসায়ন ➔ পদার্থ ➔ গণিত</span>
        </button>
      </div>

      {/* Top Timer & Header */}
      <div className="flex items-center justify-between pb-3 mb-2.5 border-b border-zinc-200/80 dark:border-zinc-800">
        <div className="flex items-center gap-2 flex-wrap">
          <span className="text-xs font-mono font-bold px-2.5 py-0.5 rounded-full bg-white dark:bg-zinc-900 text-[#056839] dark:text-emerald-400 border border-zinc-200 dark:border-zinc-800 shadow-xs">
            প্রশ্ন: {timedIndex + 1} / {timedQuestions.length} টি
          </span>
          <span className={`text-[11px] font-bold px-2.5 py-0.5 rounded-full border shadow-xs ${getOriginBadgeStyle(timedOrigin)}`}>
            📍 {timedOrigin}
          </span>
          <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-800 shadow-xs">
            {currentTimedQ.subject}
          </span>
          {currentTimedQ.expected_count !== undefined && currentTimedQ.expected_count !== null && (
            <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 shadow-xs inline-flex items-center gap-1">
              <span>🎯 প্রত্যাশিত ফ্রিকোয়েন্সি: {typeof currentTimedQ.expected_count === 'number' ? `${currentTimedQ.expected_count} বার` : currentTimedQ.expected_count}</span>
            </span>
          )}
          {currentTimedQ.written_essential && (
            <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-violet-500/15 text-violet-700 dark:text-violet-300 border border-violet-500/30 shadow-xs inline-flex items-center gap-1">
              ✍️ Written Essential
            </span>
          )}
        </div>

        {/* 45-Second Timer Pill */}
        <div className={`flex items-center gap-1.5 px-3 py-1 rounded-full border text-xs font-bold font-mono transition-all shadow-xs ${
          isTimeCritical 
            ? 'bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-800 text-rose-700 dark:text-rose-300 animate-pulse' 
            : 'bg-white dark:bg-zinc-900 border-zinc-200 dark:border-zinc-800 text-zinc-800 dark:text-zinc-200'
        }`}>
          <Clock className="w-3.5 h-3.5" />
          <span>{timeLeft}s</span>
        </div>
      </div>

      {/* Timer Progress Line */}
      <div className="w-full bg-zinc-200 dark:bg-zinc-800 h-1.5 rounded-full overflow-hidden mb-3">
        <div 
          className={`h-full transition-all duration-1000 ${
            isTimeCritical ? 'bg-rose-500' : 'bg-gradient-to-r from-[#00B09B] to-[#96C93D]'
          }`}
          style={{ width: `${timerPercent}%` }}
        />
      </div>

      {/* Question Card */}
      <div className="bg-white dark:bg-zinc-900 rounded-3xl p-4 sm:p-5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm mb-3">
        {timedHotspot && (
          <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-700 text-xs font-bold mb-2.5 shadow-xs">
            <span>{timedHotspot}</span>
          </div>
        )}
        <div className="flex items-center gap-2 mb-2">
          <span className="text-[11px] font-semibold px-2 py-0.5 rounded border bg-amber-50 text-amber-800 border-amber-200">
            {(currentTimedQ as any).source || (currentTimedQ as any).source_tag || timedOrigin || "🎯 ২০২৬ প্রেডিক্টর"}
          </span>
        </div>

        <div className="text-lg font-medium leading-relaxed text-zinc-900 dark:text-white mb-4 overflow-x-auto no-scrollbar">
          <MathText content={timedCleanText} />
        </div>

        {/* Options */}
        <div className="space-y-2">
          {currentTimedQ.opts.map((opt, optIdx) => {
            const isSelected = userSelected === optIdx;
            return (
              <button
                key={optIdx}
                onClick={() => handleTimedOptionSelect(optIdx)}
                className={`w-full text-base py-3 px-4 rounded-2xl border text-left flex items-center gap-3 transition-all cursor-pointer ${
                  isSelected
                    ? 'bg-[#056839]/10 dark:bg-[#056839]/25 border-[#056839] text-[#056839] dark:text-emerald-300 font-bold shadow-xs'
                    : 'bg-zinc-50 dark:bg-zinc-800/60 border-zinc-200 dark:border-zinc-800 text-zinc-800 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                }`}
              >
                <span className={`w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 transition-all ${
                  isSelected 
                    ? 'bg-[#056839] text-white shadow-xs' 
                    : 'bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-700'
                }`}>
                  {String.fromCharCode(65 + optIdx)}
                </span>
                <div className="flex-1 text-base leading-relaxed overflow-x-auto no-scrollbar">
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
          onClick={() => handleTimedNext(null)}
          className="px-4 py-2.5 rounded-full bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-800 text-xs sm:text-sm font-semibold shadow-xs transition-all cursor-pointer"
        >
          স্কিপ করুন (S)
        </button>

        <span className="hidden sm:inline text-xs text-zinc-500 dark:text-zinc-400 font-mono">
          <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-700">1-4</kbd> বিকল্প | <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-700">Enter</kbd> পরবর্তী প্রশ্ন
        </span>

        <button
          onClick={() => handleTimedNext(userSelected ?? null)}
          className="flex items-center gap-2 px-6 py-2.5 rounded-full bg-[#056839] hover:bg-[#044e2b] text-white text-xs sm:text-sm font-bold shadow-lg shadow-[#056839]/20 transition-all hover:scale-105 active:scale-95 cursor-pointer"
        >
          <span>{timedIndex + 1 === timedQuestions.length ? 'পরীক্ষা জমা দিন' : 'পরবর্তী প্রশ্ন'}</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
