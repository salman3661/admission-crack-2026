import type { TrackType } from '../types';

export interface SubjectStats {
  name: string;
  bn: string;
  solved: number;
  correct: number;
  accuracy: number;
  color: string;
  status: 'Mastered' | 'Strong' | 'Focus Needed' | 'পরীক্ষা বাকি';
}

export interface ExamAttemptRecord {
  id: string;
  timestamp: number;
  dateStr: string;
  title: string;
  totalQuestions: number;
  correctCount: number;
  wrongCount: number;
  skippedCount: number;
  totalScore: number;
  maxPossible: number;
  accuracy: number;
  avgTimePerQ: number;
  subjectCounts: {
    [subject: string]: {
      total: number;
      correct: number;
    };
  };
}

const STORAGE_KEY = 'admission_exam_history';

export function getExamHistory(): ExamAttemptRecord[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch (e) {
    console.error('Failed to parse exam history from localStorage', e);
    return [];
  }
}

export function saveExamAttempt(record: ExamAttemptRecord): void {
  if (typeof window === 'undefined') return;
  try {
    const existing = getExamHistory();
    const updated = [record, ...existing].slice(0, 50); // keep last 50 attempts
    localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
  } catch (e) {
    console.error('Failed to save exam record to localStorage', e);
  }
}

export function clearExamHistory(): void {
  if (typeof window === 'undefined') return;
  try {
    localStorage.removeItem(STORAGE_KEY);
  } catch (e) {
    console.error('Failed to clear exam history', e);
  }
}

export function computeAggregateStats(history: ExamAttemptRecord[], track: TrackType = 'varsity') {
  const attemptedCount = history.length;

  const subjectsConfig = track === 'medical'
    ? [
        { name: 'Biology', bn: 'জীববিজ্ঞান', color: 'bg-emerald-500' },
        { name: 'Chemistry', bn: 'রসায়ন', color: 'bg-amber-500' },
        { name: 'Physics', bn: 'পদার্থবিজ্ঞান', color: 'bg-cyan-500' },
        { name: 'English', bn: 'ইংরেজি', color: 'bg-blue-500' },
        { name: 'GK', bn: 'সাধারণ জ্ঞান', color: 'bg-purple-500' },
      ]
    : [
        { name: 'Physics', bn: 'পদার্থবিজ্ঞান', color: 'bg-cyan-500' },
        { name: 'Chemistry', bn: 'রসায়ন', color: 'bg-amber-500' },
        { name: 'Higher Math', bn: 'উচ্চতর গণিত', color: 'bg-rose-500' },
        { name: 'Biology', bn: 'জীববিজ্ঞান', color: 'bg-emerald-500' },
      ];

  if (attemptedCount === 0) {
    return {
      attemptedCount: 0,
      predictedRank: 'পরীক্ষার পর আনলক হবে',
      totalSolved: '০ টি',
      solvedCount: 0,
      overallAccuracy: '০%',
      accuracyNum: 0,
      avgTime: '--',
      subjects: subjectsConfig.map((cfg) => ({
        name: cfg.name,
        bn: cfg.bn,
        solved: 0,
        correct: 0,
        accuracy: 0,
        color: cfg.color,
        status: 'পরীক্ষা বাকি' as const,
      })),
      recentTests: [],
    };
  }

  let totalQuestionsAnswered = 0;
  let totalCorrect = 0;
  let totalTimeSum = 0;

  const subjectMap: Record<string, { total: number; correct: number }> = {};
  subjectsConfig.forEach((cfg) => {
    subjectMap[cfg.name] = { total: 0, correct: 0 };
  });

  history.forEach((h) => {
    const answeredInThis = h.correctCount + h.wrongCount;
    totalQuestionsAnswered += answeredInThis;
    totalCorrect += h.correctCount;
    totalTimeSum += h.avgTimePerQ;

    if (h.subjectCounts) {
      Object.entries(h.subjectCounts).forEach(([subj, data]) => {
        if (!subjectMap[subj]) {
          subjectMap[subj] = { total: 0, correct: 0 };
        }
        subjectMap[subj].total += data.total;
        subjectMap[subj].correct += data.correct;
      });
    }
  });

  const accuracyNum = totalQuestionsAnswered > 0 
    ? Math.round((totalCorrect / totalQuestionsAnswered) * 100) 
    : 0;

  const avgSeconds = Math.round(totalTimeSum / attemptedCount);

  // Dynamic merit rank estimation
  let predictedRank = '--';
  if (track === 'medical') {
    if (accuracyNum >= 90) {
      predictedRank = 'DMC / শীর্ষ মেডিকেল (#1 - #120)';
    } else if (accuracyNum >= 80) {
      predictedRank = 'শীর্ষ ৫ মেডিকেল (#125 - #550)';
    } else if (accuracyNum >= 70) {
      predictedRank = 'সরকারি মেডিকেল (#600 - #2200)';
    } else if (accuracyNum >= 55) {
      predictedRank = 'বিএমডিসি মেরিট ওয়েটিং';
    } else {
      predictedRank = 'পুনঃপ্রস্তুতি প্রয়োজন';
    }
  } else {
    if (accuracyNum >= 90) {
      predictedRank = 'ঢাবি শীর্ষ (#25 - #75)';
    } else if (accuracyNum >= 80) {
      predictedRank = "ঢাবি 'ক' মেরিট (#80 - #250)";
    } else if (accuracyNum >= 70) {
      predictedRank = "ঢাবি চয়েস লিস্ট (#260 - #650)";
    } else if (accuracyNum >= 55) {
      predictedRank = "ভার্সিটি গুচ্ছ মেরিট (#700 - #1800)";
    } else {
      predictedRank = '#2000+';
    }
  }

  const subjects: SubjectStats[] = subjectsConfig.map((cfg) => {
    const data = subjectMap[cfg.name] || { total: 0, correct: 0 };
    const acc = data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0;
    let status: SubjectStats['status'] = 'পরীক্ষা বাকি';
    if (data.total > 0) {
      if (acc >= 85) status = 'Mastered';
      else if (acc >= 70) status = 'Strong';
      else status = 'Focus Needed';
    }
    return {
      name: cfg.name,
      bn: cfg.bn,
      solved: data.total,
      correct: data.correct,
      accuracy: acc,
      color: cfg.color,
      status,
    };
  });

  const recentTests = history.slice(0, 5).map((h) => ({
    title: h.title,
    date: h.dateStr,
    score: `${h.totalScore.toFixed(2)}/${h.maxPossible.toFixed(0)}`,
    accuracy: `${h.accuracy}%`,
    time: `${h.avgTimePerQ} সে/প্রশ্ন`,
  }));

  // Bengali numeral converter
  const toBn = (n: number) => {
    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return String(n).replace(/\d/g, (d) => bnDigits[parseInt(d, 10)]);
  };

  return {
    attemptedCount,
    predictedRank,
    totalSolved: `${toBn(totalQuestionsAnswered)} টি`,
    solvedCount: totalQuestionsAnswered,
    overallAccuracy: `${toBn(accuracyNum)}%`,
    accuracyNum,
    avgTime: `${toBn(avgSeconds)} সে`,
    subjects,
    recentTests,
  };
}

