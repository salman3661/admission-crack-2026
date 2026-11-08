import React, { useState, useMemo, useEffect } from 'react';
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
  Flame
} from 'lucide-react';
import { MathText } from './MathText';
import masterBlueprintRaw from '../data/master_chapter_blueprint.json';
import syntheticPredictorsRaw from '../data/chapter_synthetic_predictors.json';
import type { 
  MasterChapterBlueprint, 
  ChapterSyntheticPredictors, 
  SyntheticPredictorQuestion 
} from '../types';

export const ChapterBlueprintView: React.FC = () => {
  // Load data
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
  const [selectedSubject, setSelectedSubject] = useState<'Physics' | 'Chemistry' | 'Higher Math' | 'Biology'>('Physics');

  // Chapters of selected subject
  const currentSubjectChapters = useMemo(() => {
    return blueprintChapters.filter(c => c.subject.toLowerCase() === selectedSubject.toLowerCase());
  }, [blueprintChapters, selectedSubject]);

  // Active Chapter ID
  const [selectedChapterId, setSelectedChapterId] = useState<string>('');

  // Synchronize active chapter when subject changes
  useEffect(() => {
    if (currentSubjectChapters.length > 0) {
      // Keep selected if valid, otherwise pick first
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

  // View Mode: 'all' | 'blueprint' | 'predictors'
  const [activeTab, setActiveTab] = useState<'blueprint' | 'quiz'>('blueprint');

  // Section 1 Collapsible Type States (expanded by default for fast scan)
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
    // Auto reveal feedback on click for instant active recall
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

  // Bengali Numerals Converter
  const toBn = (num: number | string) => {
    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return num.toString().replace(/\d/g, (d) => bnDigits[parseInt(d, 10)]);
  };

  // Subject pill styling
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
    <div className="max-w-6xl mx-auto px-3 sm:px-6 py-6 space-y-6">
      {/* 1. Header Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-slate-900 via-slate-800 to-[#0A1F13] text-white p-5 sm:p-7 shadow-xl border border-slate-700/60">
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

          <div className="flex flex-wrap items-center gap-3 pt-2 text-xs text-slate-300">
            <span className="flex items-center gap-1 bg-slate-800/80 px-2.5 py-1 rounded-md border border-slate-700">
              <Layers className="w-3.5 h-3.5 text-cyan-400" />
              ৩৪টি পূর্ণাঙ্গ অধ্যায়
            </span>
            <span className="flex items-center gap-1 bg-slate-800/80 px-2.5 py-1 rounded-md border border-slate-700">
              <Star className="w-3.5 h-3.5 text-amber-400 fill-amber-400" />
              ৫-স্টার মেগা-রিপিট রেফারেন্স
            </span>
            <span className="flex items-center gap-1 bg-slate-800/80 px-2.5 py-1 rounded-md border border-slate-700">
              <Zap className="w-3.5 h-3.5 text-emerald-400" />
              ৬৮০টি সম্পূর্ণ ফ্রেশ প্রেডিক্টর MCQ
            </span>
          </div>
        </div>
      </div>

      {/* 2. PCMB Subject Selector */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
        {[
          { key: 'Physics', label: 'পদার্থবিজ্ঞান', sub: '১০টি অধ্যায় • ২০০ MCQ', icon: '⚡' },
          { key: 'Chemistry', label: 'রসায়ন', sub: '৮টি অধ্যায় • ১৬০ MCQ', icon: '🧪' },
          { key: 'Higher Math', label: 'উচ্চতর গণিত', sub: '৮টি অধ্যায় • ১৬০ MCQ', icon: '📐' },
          { key: 'Biology', label: 'জীববিজ্ঞান', sub: '৮টি অধ্যায় • ১৬০ MCQ', icon: '🧬' }
        ].map(item => {
          const isSelected = selectedSubject === item.key;
          const theme = subjectThemes[item.key as keyof typeof subjectThemes];
          return (
            <button
              key={item.key}
              onClick={() => setSelectedSubject(item.key as any)}
              className={`p-3.5 rounded-xl border text-left transition-all duration-200 flex flex-col justify-between ${
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

      {/* 3. Horizontal Chapter Pills */}
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
                className={`flex-shrink-0 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all border ${
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

      {/* 4. Active Chapter Overview Card & Section Switcher */}
      {activeChapter && (
        <div className="bg-white dark:bg-[#101A14] rounded-2xl border border-slate-200 dark:border-[#1E2D22] p-4 sm:p-6 shadow-sm space-y-4">
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
                className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all ${
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
                className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all ${
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
                    className="text-slate-500 hover:text-emerald-600 dark:text-slate-400 dark:hover:text-emerald-400 font-medium"
                  >
                    সব খুলুন
                  </button>
                  <span className="text-slate-300 dark:text-slate-700">|</span>
                  <button
                    onClick={collapseAllTypes}
                    className="text-slate-500 hover:text-emerald-600 dark:text-slate-400 dark:hover:text-emerald-400 font-medium"
                  >
                    সব বন্ধ
                  </button>
                </div>
              </div>

              <div className="space-y-3">
                {activeChapter.mega_types.map((typeItem, idx) => {
                  const isExpanded = expandedTypes[typeItem.type_id] !== false; // expanded by default
                  const isFiveStar = typeItem.importance === '⭐⭐⭐⭐⭐';

                  return (
                    <div 
                      key={typeItem.type_id}
                      className={`rounded-xl border transition-all duration-200 overflow-hidden ${
                        isFiveStar
                          ? 'border-amber-300/80 dark:border-amber-800/60 bg-gradient-to-r from-amber-500/5 via-transparent to-transparent dark:bg-amber-950/10'
                          : 'border-slate-200 dark:border-[#223528] bg-white dark:bg-[#131E17]'
                      }`}
                    >
                      {/* Collapsible Card Header */}
                      <button
                        onClick={() => toggleTypeExpand(typeItem.type_id)}
                        className="w-full p-3.5 sm:p-4 text-left flex items-start sm:items-center justify-between gap-3 hover:bg-slate-50/80 dark:hover:bg-[#17251C] transition-colors"
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

                            {/* Past University Tags */}
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

                      {/* Collapsible Content */}
                      {isExpanded && (
                        <div className="p-3.5 sm:p-4 pt-0 border-t border-slate-100 dark:border-[#1E2E23] space-y-3 bg-slate-50/50 dark:bg-[#111A14]">
                          {/* Exact Master QB Question References */}
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

                          {/* Core Rule */}
                          <div className="p-3 rounded-lg bg-emerald-500/10 border border-emerald-500/25 space-y-1">
                            <div className="text-[11px] font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1.5">
                              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                              <span>কোর রুল ও ফান্ডামেন্টাল সূত্র (Core Rule):</span>
                            </div>
                            <div className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed pl-5 font-medium">
                              <MathText text={typeItem.core_rule} />
                            </div>
                          </div>

                          {/* 5-Second Speed Elimination */}
                          <div className="p-3 rounded-lg bg-amber-500/10 border border-amber-500/25 space-y-1">
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
              {/* Score & Controls Bar */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-3.5 rounded-xl bg-slate-50 dark:bg-[#16231A] border border-slate-200 dark:border-[#24372A]">
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
                      className={`px-2.5 py-1 rounded-md font-semibold transition-all border ${
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
                    className="px-2.5 py-1 rounded-md font-medium text-slate-600 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400"
                  >
                    সব ব্যাখ্যা আনলক
                  </button>
                  <button
                    onClick={handleResetQuiz}
                    className="p-1 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
                    title="রিসেট টেস্ট"
                  >
                    <RotateCcw className="w-4 h-4" />
                  </button>
                </div>
              </div>

              {/* Questions List */}
              <div className="space-y-4">
                {displayedPredictors.map((q, qIndex) => {
                  const userAnswer = userAnswers[q.id];
                  const isRevealed = revealedQuestions[q.id] || !!userAnswer;
                  const isAnswered = !!userAnswer;
                  const isCorrect = userAnswer === q.answer;

                  return (
                    <div
                      key={q.id}
                      className={`p-4 sm:p-5 rounded-xl border transition-all duration-200 space-y-3 ${
                        isAnswered
                          ? isCorrect
                            ? 'bg-emerald-500/5 border-emerald-500/30'
                            : 'bg-rose-500/5 border-rose-500/30'
                          : 'bg-white dark:bg-[#141E18] border-slate-200 dark:border-[#223528]'
                      }`}
                    >
                      {/* Question Header: Number & Type Reference */}
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

                      {/* Question Stem */}
                      <div className="text-sm sm:text-base font-medium text-slate-900 dark:text-white leading-relaxed">
                        <MathText text={q.stem} />
                      </div>

                      {/* 4 Options Grid */}
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
                              className={`p-3 rounded-xl border text-left text-xs sm:text-sm transition-all flex items-start gap-2.5 ${optionStyle}`}
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

                      {/* Instant Feedback & Trap Alert Breakdown */}
                      {isRevealed && (
                        <div className="pt-2 space-y-2 border-t border-slate-100 dark:border-[#1E2E23]">
                          {/* Trap Alert */}
                          <div className="p-3 rounded-lg bg-rose-500/10 border border-rose-500/25 space-y-1">
                            <div className="text-[11px] font-bold text-rose-800 dark:text-rose-300 flex items-center gap-1.5">
                              <ShieldAlert className="w-3.5 h-3.5 text-rose-600 dark:text-rose-400" />
                              <span>সাধারণ ছাত্রভ্রান্তি ও ফাঁদ (Trap Alert):</span>
                            </div>
                            <div className="text-xs text-slate-800 dark:text-slate-200 pl-5 font-medium">
                              <MathText text={q.trap_alert} />
                            </div>
                          </div>

                          {/* Speed Hack */}
                          <div className="p-3 rounded-lg bg-emerald-500/10 border border-emerald-500/25 space-y-1">
                            <div className="text-[11px] font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1.5">
                              <Zap className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 fill-emerald-500" />
                              <span>৫-সেকেন্ড স্পিড হ্যাক / অপশন এলিমিনেশন (Speed Hack):</span>
                            </div>
                            <div className="text-xs text-slate-800 dark:text-slate-200 pl-5 font-medium">
                              <MathText text={q.speed_hack} />
                            </div>
                          </div>

                          {/* Detailed Explanation */}
                          {q.explanation && (
                            <div className="p-2.5 rounded-lg bg-slate-50 dark:bg-[#16221A] text-xs text-slate-600 dark:text-slate-300 space-y-1">
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
  );
};

export default ChapterBlueprintView;
