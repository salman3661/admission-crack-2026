import React, { useState, useEffect, useRef } from 'react';
import { 
  ChevronLeft, 
  ChevronRight, 
  Maximize2, 
  Minimize2, 
  BookOpen, 
  Zap, 
  AlertTriangle, 
  CheckCircle2, 
  Compass, 
  ListFilter 
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

  // Reset index when filters change
  useEffect(() => {
    setCurrentIndex(0);
  }, [selectedWeek, selectedSubject]);

  // Keyboard navigation
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
      <div className="py-20 text-center">
        <Compass className="w-12 h-12 text-slate-600 mx-auto mb-3 animate-pulse" />
        <h3 className="text-lg font-bold text-slate-300">কোনো স্লাইড পাওয়া যায়নি</h3>
        <p className="text-sm text-slate-500 mt-1">দয়া করে ফিল্টার পরিবর্তন করে পুনরায় চেষ্টা করুন।</p>
      </div>
    );
  }

  const currentSlide = filteredSlides[currentIndex];

  const getSubjectColor = (subj: string) => {
    switch (subj) {
      case 'Physics': return 'from-cyan-500/20 to-blue-500/10 text-cyan-400 border-cyan-500/30';
      case 'Chemistry': return 'from-amber-500/20 to-orange-500/10 text-amber-400 border-amber-500/30';
      case 'Higher Math': return 'from-indigo-500/20 to-violet-500/10 text-indigo-400 border-indigo-500/30';
      case 'Biology': return 'from-emerald-500/20 to-teal-500/10 text-emerald-400 border-emerald-500/30';
      default: return 'from-brand-500/20 to-blue-500/10 text-brand-400 border-brand-500/30';
    }
  };

  return (
    <div 
      ref={containerRef}
      className={`flex flex-col ${isFullscreen ? 'bg-slate-950 p-6 min-h-screen overflow-y-auto' : 'max-w-6xl mx-auto py-6 px-4'}`}
    >
      {/* Top Slide Control Header */}
      <div className="flex flex-wrap items-center justify-between pb-4 gap-3 border-b border-slate-800">
        <div className="flex items-center gap-3">
          <span className={`px-2.5 py-1 rounded-lg text-xs font-bold border uppercase tracking-wider bg-gradient-to-r ${getSubjectColor(currentSlide.subject)}`}>
            {currentSlide.subject}
          </span>
          <span className="text-xs font-semibold px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">
            {currentSlide.week_id.replace('_', ' ').toUpperCase()}
          </span>
          <h2 className="text-base sm:text-lg font-bold text-white tracking-wide">
            {currentSlide.title}
          </h2>
        </div>

        {/* Counter & Action Controls */}
        <div className="flex items-center gap-2">
          <div className="text-xs font-mono text-slate-400 bg-slate-900 px-2.5 py-1 rounded-lg border border-slate-800">
            <span className="text-brand-400 font-bold">{currentIndex + 1}</span> / {filteredSlides.length}
          </div>

          {/* Quick jump select */}
          <div className="relative">
            <select
              value={currentIndex}
              onChange={(e) => setCurrentIndex(Number(e.target.value))}
              aria-label="স্লাইড নির্বাচন করুন"
              className="appearance-none bg-slate-900 text-slate-300 text-xs px-2.5 py-1.5 pr-7 rounded-lg border border-slate-800 hover:border-slate-700 cursor-pointer focus:outline-none"
            >
              {filteredSlides.map((s, idx) => (
                <option key={s.id} value={idx}>
                  {idx + 1}. {s.title}
                </option>
              ))}
            </select>
            <ListFilter className="w-3.5 h-3.5 text-slate-400 absolute right-2 top-2.5 pointer-events-none" />
          </div>

          {/* Fullscreen Button */}
          <button
            onClick={toggleFullscreen}
            className="p-1.5 rounded-lg bg-slate-900 text-slate-400 hover:text-white hover:bg-slate-800 border border-slate-800 transition-all"
            title="ফুলস্ক্রিন মোড (F)"
          >
            {isFullscreen ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-slate-900 h-1.5 rounded-full overflow-hidden my-3">
        <div 
          className="bg-gradient-to-r from-brand-500 via-indigo-500 to-cyan-400 h-full transition-all duration-300"
          style={{ width: `${((currentIndex + 1) / filteredSlides.length) * 100}%` }}
        />
      </div>

      {/* Main Slide Card Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 my-2">
        {/* Card 1: Core Formula Matrix */}
        <div className="bg-slate-900/90 rounded-2xl p-5 border border-cyan-500/30 shadow-lg shadow-cyan-950/20 relative overflow-hidden group hover:border-cyan-500/50 transition-all">
          <div className="absolute top-0 right-0 w-32 h-32 bg-cyan-500/5 rounded-full blur-2xl pointer-events-none" />
          <div className="flex items-center gap-2 mb-3">
            <span className="p-1.5 rounded-lg bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
              <BookOpen className="w-4 h-4" />
            </span>
            <h3 className="text-sm font-bold text-cyan-300 tracking-wide">
              কোর ফর্মুলা ও মাস্টার রুলস (Core Matrix)
            </h3>
          </div>
          <div className="text-sm">
            <MathText content={currentSlide.formula_matrix} block />
          </div>
        </div>

        {/* Card 2: 5-Second Hand Calculation Hacks */}
        <div className="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 shadow-lg shadow-amber-950/20 relative overflow-hidden group hover:border-amber-500/50 transition-all">
          <div className="absolute top-0 right-0 w-32 h-32 bg-amber-500/5 rounded-full blur-2xl pointer-events-none" />
          <div className="flex items-center gap-2 mb-3">
            <span className="p-1.5 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/20">
              <Zap className="w-4 h-4" />
            </span>
            <h3 className="text-sm font-bold text-amber-300 tracking-wide">
              ৫-সেকেন্ড হ্যান্ড ক্যালকুলেশন হ্যাকস ও ছন্দ
            </h3>
          </div>
          <div className="text-sm">
            <MathText content={currentSlide.hand_hacks} block />
          </div>
        </div>

        {/* Card 3: Red Alert Student Traps */}
        <div className="bg-slate-900/90 rounded-2xl p-5 border border-rose-500/30 shadow-lg shadow-rose-950/20 relative overflow-hidden group hover:border-rose-500/50 transition-all">
          <div className="absolute top-0 right-0 w-32 h-32 bg-rose-500/5 rounded-full blur-2xl pointer-events-none" />
          <div className="flex items-center gap-2 mb-3">
            <span className="p-1.5 rounded-lg bg-rose-500/10 text-rose-400 border border-rose-500/20">
              <AlertTriangle className="w-4 h-4" />
            </span>
            <h3 className="text-sm font-bold text-rose-300 tracking-wide">
              রেড অ্যালার্ট ট্র্যাপ ও নেগেটিভ মার্কিং ফাঁদ
            </h3>
          </div>
          <div className="text-sm">
            <MathText content={currentSlide.student_traps} block />
          </div>
        </div>

        {/* Card 4: Last Night Exam Capsule */}
        <div className="bg-slate-900/90 rounded-2xl p-5 border border-emerald-500/30 shadow-lg shadow-emerald-950/20 relative overflow-hidden group hover:border-emerald-500/50 transition-all">
          <div className="absolute top-0 right-0 w-32 h-32 bg-emerald-500/5 rounded-full blur-2xl pointer-events-none" />
          <div className="flex items-center gap-2 mb-3">
            <span className="p-1.5 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              <CheckCircle2 className="w-4 h-4" />
            </span>
            <h3 className="text-sm font-bold text-emerald-300 tracking-wide">
              লাস্ট নাইট এক্সাম ক্যাপসুল (হাই-ইল্ড পয়েন্ট)
            </h3>
          </div>
          <div className="text-sm">
            <MathText content={currentSlide.exam_capsule} block />
          </div>
        </div>
      </div>

      {/* Slide Navigation Footer Bar */}
      <div className="flex items-center justify-between pt-4 mt-2 border-t border-slate-800">
        <button
          onClick={() => setCurrentIndex((prev) => Math.max(prev - 1, 0))}
          disabled={currentIndex === 0}
          className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-slate-900 text-slate-300 hover:text-white hover:bg-slate-800 disabled:opacity-40 disabled:pointer-events-none border border-slate-800 transition-all"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>পূর্ববর্তী স্লাইড</span>
        </button>

        <span className="hidden sm:inline text-xs text-slate-500 font-medium">
          কীবোর্ডের <kbd className="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">←</kbd> ও <kbd className="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">→</kbd> কী ব্যবহার করুন
        </span>

        <button
          onClick={() => setCurrentIndex((prev) => Math.min(prev + 1, filteredSlides.length - 1))}
          disabled={currentIndex === filteredSlides.length - 1}
          className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-brand-600 hover:bg-brand-500 text-white disabled:opacity-40 disabled:pointer-events-none shadow-md shadow-brand-500/20 transition-all"
        >
          <span>পরবর্তী স্লাইড</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
