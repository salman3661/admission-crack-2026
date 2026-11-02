import React from 'react';
import { 
  Presentation, 
  Sparkles, 
  Timer, 
  Zap, 
  GraduationCap, 
  Layers 
} from 'lucide-react';
import type { AppMode, SubjectType, WeekFilterType } from '../types';

interface NavbarProps {
  currentMode: AppMode;
  onSelectMode: (mode: AppMode) => void;
  selectedWeek: WeekFilterType;
  onSelectWeek: (week: WeekFilterType) => void;
  selectedSubject: SubjectType;
  onSelectSubject: (subject: SubjectType) => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentMode,
  onSelectMode,
  selectedWeek,
  onSelectWeek,
  selectedSubject,
  onSelectSubject,
}) => {
  const subjects: { label: SubjectType }[] = [
    { label: 'All' },
    { label: 'Physics' },
    { label: 'Chemistry' },
    { label: 'Higher Math' },
    { label: 'Biology' },
  ];

  const modes: { id: AppMode; label: string; icon: React.ReactNode; badge?: string }[] = [
    { id: 'slides', label: 'স্লাইড ডেক', icon: <Presentation className="w-4 h-4" /> },
    { id: 'flashcards', label: 'স্মার্ট ফ্ল্যাশকার্ড', icon: <Sparkles className="w-4 h-4" /> },
    { id: 'exam', label: 'ঢাবি রিয়েল এক্সাম', icon: <Timer className="w-4 h-4" />, badge: '-0.25' },
    { id: 'vault', label: 'গ্লোবাল ভল্ট', icon: <Zap className="w-4 h-4 text-amber-400" /> },
  ];

  return (
    <header className="sticky top-0 z-50 backdrop-blur-md bg-slate-950/85 border-b border-slate-800/80">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Top Branding Row */}
        <div className="flex flex-wrap items-center justify-between py-3 gap-3">
          {/* Logo & Tag */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 via-indigo-600 to-cyan-500 p-0.5 shadow-lg shadow-brand-500/20">
              <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
                <GraduationCap className="w-5 h-5 text-brand-400" />
              </div>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-lg font-bold tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-300 bg-clip-text text-transparent font-['Outfit']">
                  Admission Crack <span className="text-brand-400 font-extrabold">2026</span>
                </h1>
                <span className="hidden sm:inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-brand-500/10 text-brand-300 border border-brand-500/20">
                  DU Ka & Medical
                </span>
              </div>
              <p className="text-xs text-slate-400 font-medium">
                Rank 1–100 Active-Recall Revision Platform
              </p>
            </div>
          </div>

          {/* Week Selector Dropdown / Pills */}
          <div className="flex items-center gap-2 bg-slate-900/90 p-1 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs font-medium text-slate-400 pl-2 pr-1 flex items-center gap-1">
              <Layers className="w-3.5 h-3.5 text-slate-400" /> সপ্তাহ:
            </span>
            {(['all', 'week_01', 'week_02'] as WeekFilterType[]).map((w) => (
              <button
                key={w}
                onClick={() => onSelectWeek(w)}
                className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                  selectedWeek === w
                    ? 'bg-gradient-to-r from-brand-600 to-indigo-600 text-white shadow-md shadow-brand-500/25'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
                }`}
              >
                {w === 'all' ? 'All Weeks' : w === 'week_01' ? 'Week 01' : 'Week 02'}
              </button>
            ))}
          </div>
        </div>

        {/* Navigation & Filter Row */}
        <div className="flex flex-col md:flex-row md:items-center justify-between pb-3 pt-1 gap-3 border-t border-slate-800/40">
          {/* Mode Switcher Tabs */}
          <div className="flex items-center gap-1.5 overflow-x-auto pb-1 md:pb-0 scrollbar-none">
            {modes.map((mode) => {
              const active = currentMode === mode.id;
              return (
                <button
                  key={mode.id}
                  onClick={() => onSelectMode(mode.id)}
                  className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all whitespace-nowrap ${
                    active
                      ? 'bg-slate-800 text-white border border-brand-500/40 shadow-sm shadow-brand-500/10'
                      : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900 border border-transparent'
                  }`}
                >
                  <span className={active ? 'text-brand-400' : 'text-slate-500'}>
                    {mode.icon}
                  </span>
                  <span>{mode.label}</span>
                  {mode.badge && (
                    <span className="text-[10px] font-bold px-1.5 py-0.2 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30">
                      {mode.badge}
                    </span>
                  )}
                </button>
              );
            })}
          </div>

          {/* Subject Filter Pills */}
          {currentMode !== 'vault' && (
            <div className="flex items-center gap-1.5 overflow-x-auto scrollbar-none">
              {subjects.map((subj) => {
                const active = selectedSubject === subj.label;
                return (
                  <button
                    key={subj.label}
                    onClick={() => onSelectSubject(subj.label)}
                    className={`px-3 py-1 text-xs font-medium rounded-lg transition-all border whitespace-nowrap ${
                      active
                        ? 'bg-slate-800 text-brand-300 border-brand-500/50 shadow-sm'
                        : 'bg-slate-900/60 text-slate-400 border-slate-800 hover:bg-slate-800/50 hover:text-slate-200'
                    }`}
                  >
                    {subj.label === 'All' ? 'সব বিষয়' : subj.label}
                  </button>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </header>
  );
};
