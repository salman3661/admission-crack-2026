import React, { useState, useMemo, useEffect } from 'react';
import {
  BookOpen,
  Search,
  X,
  Zap,
  ShieldAlert,
  Timer,
  CheckCircle2,
  XCircle,
  Award,
  ArrowLeft,
  Flame,
  Play,
} from 'lucide-react';
import confetti from 'canvas-confetti';
import subjectFinalRaw from '../data/subject_final_bank.json';
import { MathText } from './MathText';
import type { SubjectFinalBank, QuizQuestion, TrackType, SubjectType } from '../types';

interface SubjectFinalViewProps {
  activeTrack: TrackType;
  selectedSubject: SubjectType;
  onSelectSubject: (subject: SubjectType) => void;
}

const toBn = (num: number | string): string => {
  const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
  return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)] ?? d);
};

export const SubjectFinalView: React.FC<SubjectFinalViewProps> = ({
  activeTrack,
  selectedSubject,
  onSelectSubject,
}) => {
  const bank = subjectFinalRaw as unknown as SubjectFinalBank;

  const trackQuestions: QuizQuestion[] = useMemo(() => {
    return activeTrack === 'medical' ? bank.medical || [] : bank.varsity || [];
  }, [bank, activeTrack]);

  const subjects: { id: SubjectType; label: string; icon: string }[] =
    activeTrack === 'medical'
      ? [
          { id: 'All', label: 'সব বিষয়', icon: '🌐' },
          { id: 'Biology', label: 'জীববিজ্ঞান', icon: '🧬' },
          { id: 'Chemistry', label: 'রসায়ন', icon: '🧪' },
          { id: 'Physics', label: 'পদার্থবিজ্ঞান', icon: '⚛️' },
          { id: 'English', label: 'ইংরেজি', icon: '🇬🇧' },
          { id: 'GK', label: 'সাধারণ জ্ঞান', icon: '🇧🇩' },
          { id: 'ICT', label: 'আইসিটি', icon: '💻' },
        ]
      : [
          { id: 'All', label: 'সব বিষয়', icon: '🌐' },
          { id: 'Physics', label: 'পদার্থবিজ্ঞান', icon: '⚛️' },
          { id: 'Chemistry', label: 'রসায়ন', icon: '🧪' },
          { id: 'Higher Math', label: 'উচ্চতর গণিত', icon: '📐' },
          { id: 'Biology', label: 'জীববিজ্ঞান', icon: '🧬' },
          { id: 'Bangla', label: 'বাংলা', icon: '📖' },
          { id: 'English', label: 'ইংরেজি', icon: '🇬🇧' },
          { id: 'GK', label: 'সাধারণ জ্ঞান', icon: '🇧🇩' },
          { id: 'ICT', label: 'আইসিটি', icon: '💻' },
        ];

  const [selectedChapter, setSelectedChapter] = useState<string>('All');
  const [searchQuery, setSearchQuery] = useState('');
  const [page, setPage] = useState(0);
  const pageSize = 15;

  // Inline answer reveal state for QB browsing
  const [revealedAnswers, setRevealedAnswers] = useState<Record<string, number>>({});

  // Timed Subject Final Model Test state
  const [isMockActive, setIsMockActive] = useState(false);
  const [mockQuestions, setMockQuestions] = useState<QuizQuestion[]>([]);
  const [mockIdx, setMockIdx] = useState(0);
  const [mockAnswers, setMockAnswers] = useState<Record<number, number | null>>({});
  const [mockTimeLeft, setMockTimeLeft] = useState(0);
  const [isMockFinished, setIsMockFinished] = useState(false);

  useEffect(() => {
    setSelectedChapter('All');
    setPage(0);
    setIsMockActive(false);
  }, [activeTrack, selectedSubject]);

  useEffect(() => {
    setPage(0);
  }, [selectedChapter, searchQuery]);

  // Extract chapters for current subject
  const availableChapters = useMemo(() => {
    const base =
      selectedSubject === 'All'
        ? trackQuestions
        : trackQuestions.filter((q) => q.subject === selectedSubject);
    const set = new Set<string>();
    base.forEach((q) => {
      if (q.chapter && q.chapter.trim()) set.add(q.chapter.trim());
    });
    return ['All', ...Array.from(set)];
  }, [trackQuestions, selectedSubject]);

  const filteredQuestions = useMemo(() => {
    return trackQuestions.filter((q) => {
      if (selectedSubject !== 'All' && q.subject !== selectedSubject) return false;
      if (selectedChapter !== 'All' && (q.chapter || '').trim() !== selectedChapter) return false;
      if (searchQuery.trim()) {
        const needle = searchQuery.toLowerCase();
        const hay = `${q.q} ${q.origin || ''} ${q.chapter || ''} ${q.du_repeat_tag || ''}`.toLowerCase();
        if (!hay.includes(needle)) return false;
      }
      return true;
    });
  }, [trackQuestions, selectedSubject, selectedChapter, searchQuery]);

  const totalPages = Math.max(1, Math.ceil(filteredQuestions.length / pageSize));
  const pagedQuestions = filteredQuestions.slice(page * pageSize, (page + 1) * pageSize);

  const startSubjectModelTest = (count: number) => {
    const pool = filteredQuestions.length > 0 ? filteredQuestions : trackQuestions;
    const shuffled = [...pool].sort(() => 0.5 - Math.random());
    const chosen = shuffled.slice(0, Math.min(count, shuffled.length));
    setMockQuestions(chosen);
    setMockIdx(0);
    setMockAnswers({});
    setMockTimeLeft(chosen.length * 60);
    setIsMockFinished(false);
    setIsMockActive(true);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const finishSubjectMock = () => {
    setIsMockFinished(true);
    try {
      confetti({ particleCount: 70, spread: 65, origin: { y: 0.6 } });
    } catch {
      // ignore
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  useEffect(() => {
    if (!isMockActive || isMockFinished) return;
    if (mockTimeLeft <= 0) {
      finishSubjectMock();
      return;
    }
    const timer = setInterval(() => setMockTimeLeft((p) => p - 1), 1000);
    return () => clearInterval(timer);
  }, [isMockActive, isMockFinished, mockTimeLeft]);

  const mockStats = useMemo(() => {
    let correct = 0;
    let wrong = 0;
    let skipped = 0;
    mockQuestions.forEach((q, i) => {
      const a = mockAnswers[i];
      if (a === undefined || a === null) skipped++;
      else if (a === q.ans) correct++;
      else wrong++;
    });
    const score = Math.max(0, correct - wrong * 0.25);
    return { correct, wrong, skipped, score };
  }, [mockQuestions, mockAnswers]);

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // =========================================================================
  // SUBJECT-WISE TIMED MODEL TEST VIEW
  // =========================================================================
  if (isMockActive) {
    const q = mockQuestions[mockIdx];
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-5 pb-28 space-y-5">
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm flex flex-wrap items-center justify-between gap-3 sticky top-16 z-30">
          <div className="flex items-center gap-3">
            <button
              onClick={() => setIsMockActive(false)}
              className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 cursor-pointer"
            >
              <ArrowLeft className="w-4 h-4" />
            </button>
            <div>
              <div className="text-xs font-bold text-teal-600 dark:text-teal-400">
                Tier 3: Subject-wise Final Model Test
              </div>
              <h2 className="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white">
                {selectedSubject === 'All' ? 'সমন্বিত বিষয় ফাইনাল' : selectedSubject} ({toBn(mockQuestions.length)} MCQ)
              </h2>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {!isMockFinished ? (
              <>
                <span className="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 font-mono text-xs font-black flex items-center gap-1.5">
                  <Timer className="w-4 h-4" /> {formatTimer(mockTimeLeft)}
                </span>
                <button
                  onClick={finishSubjectMock}
                  className="px-4 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold cursor-pointer"
                >
                  সাবমিট
                </button>
              </>
            ) : (
              <button
                onClick={() => setIsMockActive(false)}
                className="px-4 py-1.5 rounded-xl bg-teal-600 text-white text-xs font-bold cursor-pointer"
              >
                ব্যাংকে ফিরে যান
              </button>
            )}
          </div>
        </div>

        {isMockFinished ? (
          <div className="space-y-4">
            <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-3xl p-5 space-y-3">
              <div className="flex items-center gap-3">
                <Award className="w-8 h-8 text-emerald-600" />
                <div>
                  <h3 className="text-lg font-extrabold text-slate-900 dark:text-white">
                    স্কোর: {mockStats.score.toFixed(2)} / {mockQuestions.length}
                  </h3>
                  <p className="text-xs text-slate-600 dark:text-slate-400">
                    সঠিক: {toBn(mockStats.correct)} • ভুল: {toBn(mockStats.wrong)} • স্কিপড: {toBn(mockStats.skipped)}
                  </p>
                </div>
              </div>
            </div>

            {mockQuestions.map((mq, idx) => {
              const ua = mockAnswers[idx];
              const ok = ua === mq.ans;
              return (
                <div
                  key={mq.id || idx}
                  className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 space-y-2"
                >
                  <div className="text-sm font-bold text-slate-900 dark:text-white">
                    #{toBn(idx + 1)} <MathText content={mq.q} />
                  </div>
                  <div className="text-xs font-bold text-emerald-600 dark:text-emerald-400">
                    সঠিক উত্তর: <MathText content={mq.opts[mq.ans] || ''} />
                    {ua !== undefined && ua !== null && !ok && (
                      <span className="text-rose-500 ml-3">
                        (আপনার উত্তর: <MathText content={mq.opts[ua] || ''} />)
                      </span>
                    )}
                  </div>
                  {mq.exp && (
                    <div className="text-xs text-slate-600 dark:text-slate-400 bg-slate-50 dark:bg-slate-800/60 p-2.5 rounded-xl">
                      <MathText content={mq.exp} />
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        ) : (
          q && (
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-6 space-y-4">
              <div className="flex items-center justify-between text-xs font-bold text-slate-500">
                <span>
                  প্রশ্ন {toBn(mockIdx + 1)} / {toBn(mockQuestions.length)}
                </span>
                <span>{q.origin}</span>
              </div>
              <div className="text-base sm:text-lg font-bold text-slate-900 dark:text-white">
                <MathText content={q.q} />
              </div>
              <div className="space-y-2">
                {q.opts.map((opt, oIdx) => {
                  const sel = mockAnswers[mockIdx] === oIdx;
                  return (
                    <button
                      key={oIdx}
                      onClick={() => setMockAnswers((p) => ({ ...p, [mockIdx]: sel ? null : oIdx }))}
                      className={`w-full p-3 rounded-2xl border text-left flex items-center gap-3 cursor-pointer ${
                        sel
                          ? 'bg-teal-600/10 border-teal-600 text-teal-900 dark:text-teal-100'
                          : 'bg-slate-50 dark:bg-slate-800/60 border-slate-200 dark:border-slate-700'
                      }`}
                    >
                      <span className="w-7 h-7 rounded-lg bg-white dark:bg-slate-700 flex items-center justify-center text-xs font-black">
                        {['ক', 'খ', 'গ', 'ঘ'][oIdx]}
                      </span>
                      <MathText content={opt} />
                    </button>
                  );
                })}
              </div>
              <div className="flex justify-between pt-3 border-t border-slate-200 dark:border-slate-800">
                <button
                  disabled={mockIdx === 0}
                  onClick={() => setMockIdx((p) => Math.max(0, p - 1))}
                  className="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold disabled:opacity-40 cursor-pointer"
                >
                  পূর্ববর্তী
                </button>
                <button
                  disabled={mockIdx === mockQuestions.length - 1}
                  onClick={() => setMockIdx((p) => Math.min(mockQuestions.length - 1, p + 1))}
                  className="px-4 py-2 rounded-xl bg-teal-600 text-white text-xs font-bold disabled:opacity-40 cursor-pointer"
                >
                  পরবর্তী
                </button>
              </div>
            </div>
          )
        )}
      </div>
    );
  }

  // =========================================================================
  // SUBJECT-WISE & CHAPTER-WISE QB DIRECTORY
  // =========================================================================
  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 py-5 pb-28 space-y-6">
      {/* Header */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-7 shadow-sm space-y-4">
        <div className="flex items-center justify-between gap-3 flex-wrap">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="px-3 py-1 rounded-full text-xs font-black bg-teal-500/15 text-teal-700 dark:text-teal-300 border border-teal-500/30 flex items-center gap-1.5">
              <BookOpen className="w-3.5 h-3.5" />
              Tier 3: Subject-wise Final Model
            </span>
            <span className="px-3 py-1 rounded-full text-xs font-bold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
              {activeTrack === 'medical'
                ? `🩺 মেডিকেল MAT QB (${toBn(trackQuestions.length)} প্রশ্ন)`
                : `🎯 ভার্সিটি/DU QB (${toBn(trackQuestions.length)} প্রশ্ন)`}
            </span>
          </div>

          <button
            onClick={() => startSubjectModelTest(30)}
            disabled={filteredQuestions.length === 0}
            className="px-4 py-2 rounded-2xl bg-gradient-to-r from-teal-600 to-emerald-600 hover:from-teal-700 hover:to-emerald-700 text-white text-xs sm:text-sm font-extrabold shadow-sm flex items-center gap-1.5 cursor-pointer disabled:opacity-40"
          >
            <Play className="w-3.5 h-3.5 fill-current" />
            সাবজেক্ট ফাইনাল টেস্ট (৩০ MCQ)
          </button>
        </div>

        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white tracking-tight">
            📚 বিষয় ও অধ্যায়ভিত্তিক প্রশ্নব্যাংক (Subject-wise Final Bank)
          </h1>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1.5 max-w-3xl">
            ট্র্যাক অনুযায়ী সম্পূর্ণ আলাদা করা বিগত বছরের ভার্সিটি (DU 'Ka' / Engineering) ও মেডিকেল (MAT) প্রশ্নব্যাংক। অধ্যায় ফিল্টার করে সরাসরি প্র্যাকটিস বা টাইমড সাবজেক্ট ফাইনাল টেস্ট দিন।
          </p>
        </div>

        {/* Subject Pills */}
        <div className="pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
          {subjects.map((s) => (
            <button
              key={s.id}
              onClick={() => onSelectSubject(s.id)}
              className={`px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-1.5 whitespace-nowrap cursor-pointer transition-all ${
                selectedSubject === s.id
                  ? 'bg-teal-600 text-white shadow-xs'
                  : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
              }`}
            >
              <span>{s.icon}</span>
              <span>{s.label}</span>
            </button>
          ))}
        </div>

        {/* Chapter Filter & Search */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <select
            value={selectedChapter}
            onChange={(e) => setSelectedChapter(e.target.value)}
            className="w-full px-3.5 py-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs sm:text-sm font-bold text-slate-800 dark:text-slate-200"
          >
            {availableChapters.map((ch) => (
              <option key={ch} value={ch}>
                {ch === 'All' ? `সব অধ্যায় (${toBn(availableChapters.length - 1)}টি)` : ch}
              </option>
            ))}
          </select>

          <div className="relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="প্রশ্ন, অধ্যায় বা DU/MAT ট্যাগ খুঁজুন..."
              className="w-full pl-9 pr-9 py-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs sm:text-sm text-slate-800 dark:text-slate-200"
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 cursor-pointer"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Results Count + Pagination */}
      <div className="flex items-center justify-between text-xs font-bold text-slate-500 px-1">
        <span>মোট {toBn(filteredQuestions.length)}টি প্রশ্ন পাওয়া গেছে</span>
        <span>
          পৃষ্ঠা {toBn(page + 1)} / {toBn(totalPages)}
        </span>
      </div>

      {/* Question Cards */}
      <div className="space-y-4">
        {pagedQuestions.map((q, idx) => {
          const picked = revealedAnswers[q.id];
          const isAnswered = picked !== undefined;
          return (
            <div
              key={q.id || idx}
              className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 space-y-3 shadow-xs"
            >
              <div className="flex items-center justify-between gap-2 flex-wrap">
                <div className="flex items-center gap-1.5 flex-wrap">
                  <span className="px-2 py-0.5 rounded-md bg-teal-500/10 text-teal-700 dark:text-teal-300 text-[11px] font-bold">
                    {q.subject}
                  </span>
                  {q.chapter && (
                    <span className="px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-[11px] font-bold">
                      {q.chapter}
                    </span>
                  )}
                  {q.origin && (
                    <span className="px-2 py-0.5 rounded-md bg-blue-500/10 text-blue-700 dark:text-blue-300 text-[11px] font-bold">
                      {q.origin}
                    </span>
                  )}
                  {(q.du_repeat_tag || (q.repeat_count && q.repeat_count > 1)) && (
                    <span className="px-2 py-0.5 rounded-md bg-rose-500/10 text-rose-700 dark:text-rose-300 text-[11px] font-bold flex items-center gap-1">
                      <Flame className="w-3 h-3" />
                      {q.du_repeat_tag || `${toBn(q.repeat_count || 2)}x Repeat`}
                    </span>
                  )}
                </div>
              </div>

              <div className="text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-relaxed">
                <MathText content={q.q} />
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                {q.opts.map((opt, oIdx) => {
                  const isCorrect = oIdx === q.ans;
                  const isPicked = picked === oIdx;
                  return (
                    <button
                      key={oIdx}
                      onClick={() => setRevealedAnswers((p) => ({ ...p, [q.id]: oIdx }))}
                      className={`p-2.5 rounded-xl border text-left text-xs sm:text-sm flex items-center gap-2 cursor-pointer transition-all ${
                        isAnswered
                          ? isCorrect
                            ? 'bg-emerald-500/15 border-emerald-500/50 text-emerald-900 dark:text-emerald-200 font-bold'
                            : isPicked
                            ? 'bg-rose-500/15 border-rose-500/50 text-rose-900 dark:text-rose-200'
                            : 'bg-slate-50 dark:bg-slate-800/50 border-slate-200 dark:border-slate-700 opacity-75'
                          : 'bg-slate-50 dark:bg-slate-800/60 border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800'
                      }`}
                    >
                      <span className="font-black shrink-0">{['ক', 'খ', 'গ', 'ঘ'][oIdx]}.</span>
                      <span className="flex-1">
                        <MathText content={opt} />
                      </span>
                      {isAnswered && isCorrect && <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />}
                      {isAnswered && isPicked && !isCorrect && <XCircle className="w-4 h-4 text-rose-600 shrink-0" />}
                    </button>
                  );
                })}
              </div>

              {isAnswered && (q.exp || q.speed_hack || q.trap_alert || q.trap) && (
                <div className="pt-2 space-y-2 text-xs">
                  {q.exp && (
                    <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/70 text-slate-700 dark:text-slate-300">
                      <strong className="text-slate-900 dark:text-white mr-1">💡 ব্যাখ্যা:</strong>
                      <MathText content={q.exp} />
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

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-3 pt-2">
          <button
            disabled={page === 0}
            onClick={() => {
              setPage((p) => Math.max(0, p - 1));
              window.scrollTo({ top: 0, behavior: 'smooth' });
            }}
            className="px-4 py-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs font-bold disabled:opacity-40 cursor-pointer"
          >
            ← পূর্ববর্তী
          </button>
          <span className="text-xs font-bold text-slate-600 dark:text-slate-400">
            {toBn(page + 1)} / {toBn(totalPages)}
          </span>
          <button
            disabled={page >= totalPages - 1}
            onClick={() => {
              setPage((p) => Math.min(totalPages - 1, p + 1));
              window.scrollTo({ top: 0, behavior: 'smooth' });
            }}
            className="px-4 py-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs font-bold disabled:opacity-40 cursor-pointer"
          >
            পরবর্তী →
          </button>
        </div>
      )}
    </div>
  );
};
