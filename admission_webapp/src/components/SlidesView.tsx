import React, { useState, useEffect, useRef } from 'react';
import { 
  ChevronLeft, 
  ChevronRight, 
  BookOpen, 
  Zap, 
  AlertTriangle, 
  CheckCircle2, 
  Compass, 
  Maximize2, 
  Minimize2 
} from 'lucide-react';
import type { SlideItem, SubjectType, WeekFilterType } from '../types';
import { MathText } from './MathText';

interface SlidesViewProps {
  slides: SlideItem[];
  selectedWeek: WeekFilterType;
  selectedSubject: SubjectType;
}

export const SlidesView: React.FC<SlidesViewProps> = ({
  slides,
  selectedWeek,
  selectedSubject,
}) => {
  // Filter slides
  const filteredSlides = slides.filter((slide) => {
    const matchWeek = selectedWeek === 'all' || slide.week_id === selectedWeek;
    const matchSubject = selectedSubject === 'All' || slide.subject === selectedSubject;
    return matchWeek && matchSubject;
  });

  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setCurrentIndex(0);
  }, [selectedWeek, selectedSubject]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight' || e.key === 'PageDown') {
        e.preventDefault();
        setCurrentIndex((prev) => Math.min(prev + 1, filteredSlides.length - 1));
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        setCurrentIndex((prev) => Math.max(prev - 1, 0));
      } else if (e.key === 'f' || e.key === 'F') {
        toggleFullscreen();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [filteredSlides.length]);

  const toggleFullscreen = () => {
    if (!containerRef.current) return;
    if (!document.fullscreenElement) {
      containerRef.current.requestFullscreen().then(() => setIsFullscreen(true)).catch(() => {});
    } else {
      document.exitFullscreen().then(() => setIsFullscreen(false)).catch(() => {});
    }
  };

  if (filteredSlides.length === 0) {
    return (
      <div className="py-16 text-center max-w-md mx-auto px-4">
        <Compass className="w-10 h-10 text-zinc-400 dark:text-zinc-600 mx-auto mb-2 animate-pulse" />
        <h3 className="text-base font-bold text-zinc-800 dark:text-zinc-200">কোনো ফর্মুলা ডেক পাওয়া যায়নি</h3>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-1">দয়া করে উপরে অন্য সপ্তাহ বা বিষয় নির্বাচন করুন।</p>
      </div>
    );
  }

  const currentSlide = filteredSlides[currentIndex];

  const getSubjectBadge = (subj: string) => {
    switch (subj) {
      case 'Physics': return 'bg-cyan-500/10 text-cyan-700 dark:text-cyan-400 border-cyan-500/20';
      case 'Chemistry': return 'bg-amber-500/10 text-amber-700 dark:text-amber-400 border-amber-500/20';
      case 'Higher Math': return 'bg-indigo-500/10 text-indigo-700 dark:text-indigo-400 border-indigo-500/20';
      case 'Biology': return 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border-emerald-500/20';
      default: return 'bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border-[#056839]/20';
    }
  };

  return (
    <div 
      ref={containerRef}
      className={`max-w-4xl mx-auto py-4 px-3 sm:px-4 ${isFullscreen ? 'bg-zinc-50 dark:bg-zinc-950 p-6 min-h-screen overflow-y-auto' : ''}`}
    >
      {/* Slide Navigation Stepper Header */}
      <div className="flex items-center justify-between gap-2 mb-3 bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 rounded-2xl p-3 shadow-sm">
        
        {/* Title & Badges */}
        <div className="overflow-hidden">
          <div className="flex items-center gap-1.5 mb-0.5">
            <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold border uppercase ${getSubjectBadge(currentSlide.subject)}`}>
              {currentSlide.subject}
            </span>
            <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-700">
              {currentSlide.week_id.replace('_', ' ').toUpperCase()}
            </span>
          </div>
          <h2 className="text-sm sm:text-base font-extrabold text-zinc-900 dark:text-white truncate">
            {currentSlide.title}
          </h2>
        </div>

        {/* Action Controls & Stepper */}
        <div className="flex items-center gap-1.5 shrink-0">
          <div className="text-xs font-mono font-bold text-zinc-700 dark:text-zinc-300 bg-zinc-100 dark:bg-zinc-800 px-2.5 py-1 rounded-xl border border-zinc-200 dark:border-zinc-700">
            <span className="text-[#056839] dark:text-emerald-400">{currentIndex + 1}</span> / {filteredSlides.length}
          </div>

          <button
            onClick={() => setCurrentIndex((prev) => Math.max(prev - 1, 0))}
            disabled={currentIndex === 0}
            className="p-1.5 rounded-xl bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-200 dark:hover:bg-zinc-700 disabled:opacity-30 disabled:pointer-events-none transition-colors border border-zinc-200 dark:border-zinc-700"
            title="পূর্ববর্তী"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>

          <button
            onClick={() => setCurrentIndex((prev) => Math.min(prev + 1, filteredSlides.length - 1))}
            disabled={currentIndex === filteredSlides.length - 1}
            className="p-1.5 rounded-xl bg-[#056839] text-white hover:bg-[#044e2b] disabled:opacity-30 disabled:pointer-events-none transition-colors shadow-sm"
            title="পরবর্তী"
          >
            <ChevronRight className="w-4 h-4" />
          </button>

          <button
            onClick={toggleFullscreen}
            className="p-1.5 rounded-xl bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white transition-colors border border-zinc-200 dark:border-zinc-700"
            title="ফুলস্ক্রিন (F)"
          >
            {isFullscreen ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {/* Progress Line */}
      <div className="w-full bg-zinc-200 dark:bg-zinc-800 h-1.5 rounded-full overflow-hidden mb-4">
        <div 
          className="bg-gradient-to-r from-[#00B09B] to-[#96C93D] h-full transition-all duration-300"
          style={{ width: `${((currentIndex + 1) / filteredSlides.length) * 100}%` }}
        />
      </div>

      {/* Simplified Soft Cards (One Focus at a Time) */}
      <div className="space-y-3.5">
        
        {/* Card 1: Core Formula Matrix */}
        <div className="bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 rounded-2xl p-4 sm:p-5 shadow-sm">
          <div className="flex items-center gap-2 mb-2 pb-2 border-b border-zinc-100 dark:border-zinc-800">
            <span className="p-1 rounded-lg bg-cyan-500/10 text-cyan-700 dark:text-cyan-400">
              <BookOpen className="w-4 h-4" />
            </span>
            <h3 className="text-xs sm:text-sm font-bold text-zinc-900 dark:text-white">
              কোর ফর্মুলা মেট্রিক্স (Core Matrix)
            </h3>
          </div>
          <div className="text-xs sm:text-sm leading-relaxed overflow-x-auto no-scrollbar">
            <MathText content={currentSlide.formula_matrix} block />
          </div>
        </div>

        {/* Card 2: 5-Second Hand Hacks */}
        <div className="bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 rounded-2xl p-4 sm:p-5 shadow-sm">
          <div className="flex items-center gap-2 mb-2 pb-2 border-b border-zinc-100 dark:border-zinc-800">
            <span className="p-1 rounded-lg bg-amber-500/10 text-amber-700 dark:text-amber-400">
              <Zap className="w-4 h-4" />
            </span>
            <h3 className="text-xs sm:text-sm font-bold text-zinc-900 dark:text-white">
              ৫-সেকেন্ড হ্যান্ড ক্যালকুলেশন হ্যাকস ও ছন্দ
            </h3>
          </div>
          <div className="text-xs sm:text-sm leading-relaxed overflow-x-auto no-scrollbar">
            <MathText content={currentSlide.hand_hacks} block />
          </div>
        </div>

        {/* Card 3: Student Traps */}
        <div className="bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 rounded-2xl p-4 sm:p-5 shadow-sm">
          <div className="flex items-center gap-2 mb-2 pb-2 border-b border-zinc-100 dark:border-zinc-800">
            <span className="p-1 rounded-lg bg-rose-500/10 text-rose-700 dark:text-rose-400">
              <AlertTriangle className="w-4 h-4" />
            </span>
            <h3 className="text-xs sm:text-sm font-bold text-rose-700 dark:text-rose-400">
              রেড অ্যালার্ট ট্র্যাপ (-০.২৫ ফাঁদ)
            </h3>
          </div>
          <div className="text-xs sm:text-sm leading-relaxed overflow-x-auto no-scrollbar">
            <MathText content={currentSlide.student_traps} block />
          </div>
        </div>

        {/* Card 4: Exam Capsule */}
        <div className="bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 rounded-2xl p-4 sm:p-5 shadow-sm">
          <div className="flex items-center gap-2 mb-2 pb-2 border-b border-zinc-100 dark:border-zinc-800">
            <span className="p-1 rounded-lg bg-emerald-500/10 text-emerald-700 dark:text-emerald-400">
              <CheckCircle2 className="w-4 h-4" />
            </span>
            <h3 className="text-xs sm:text-sm font-bold text-emerald-700 dark:text-emerald-400">
              লাস্ট নাইট এক্সাম ক্যাপসুল (হাই-ইল্ড পয়েন্ট)
            </h3>
          </div>
          <div className="text-xs sm:text-sm leading-relaxed overflow-x-auto no-scrollbar">
            <MathText content={currentSlide.exam_capsule} block />
          </div>
        </div>

      </div>

      {/* Stepper Footer */}
      <div className="flex items-center justify-between gap-3 mt-4 pt-3 border-t border-zinc-200/70 dark:border-zinc-800">
        <button
          onClick={() => setCurrentIndex((prev) => Math.max(prev - 1, 0))}
          disabled={currentIndex === 0}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 disabled:opacity-30 border border-zinc-200 dark:border-zinc-800 shadow-sm transition-all"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>পূর্ববর্তী স্লাইড</span>
        </button>

        <span className="text-[11px] text-zinc-400 dark:text-zinc-500 font-medium">
          স্লাইড {currentIndex + 1} / {filteredSlides.length}
        </span>

        <button
          onClick={() => setCurrentIndex((prev) => Math.min(prev + 1, filteredSlides.length - 1))}
          disabled={currentIndex === filteredSlides.length - 1}
          className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl text-xs font-bold bg-[#056839] hover:bg-[#044e2b] text-white disabled:opacity-30 shadow-sm transition-all"
        >
          <span>পরবর্তী স্লাইড</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
