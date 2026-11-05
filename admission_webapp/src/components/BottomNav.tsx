import React from 'react';
import { 
  Home, 
  BookOpen, 
  Zap, 
  BarChart3,
  Sparkles
} from 'lucide-react';
import type { AppMode } from '../types';

interface BottomNavProps {
  currentMode: AppMode;
  onSelectMode: (mode: AppMode) => void;
}

export const BottomNav: React.FC<BottomNavProps> = ({
  currentMode,
  onSelectMode,
}) => {
  const navItems: { id: AppMode; label: string; icon: React.ReactNode; isCenter?: boolean }[] = [
    {
      id: 'decks',
      label: 'হোম ডেক',
      icon: <Home className="w-[18px] h-[18px]" />,
    },
    {
      id: 'exam',
      label: 'প্রশ্নব্যাংক',
      icon: <BookOpen className="w-[18px] h-[18px]" />,
    },
    {
      id: 'predictor',
      label: 'প্রেডিকশন',
      icon: <Sparkles className="w-5 h-5" />,
      isCenter: true,
    },
    {
      id: 'vault',
      label: 'শর্টকাট ভল্ট',
      icon: <Zap className="w-[18px] h-[18px]" />,
    },
    {
      id: 'analytics',
      label: 'অ্যানালিটিক্স',
      icon: <BarChart3 className="w-[18px] h-[18px]" />,
    },
  ];

  return (
    <nav className="fixed bottom-0 inset-x-0 z-40 pointer-events-none pb-safe">
      <div className="pointer-events-auto max-w-lg mx-auto mb-2 sm:mb-3 px-3">
        <div className="backdrop-blur-2xl bg-white/85 dark:bg-slate-900/85 ring-1 ring-slate-200/90 dark:ring-slate-800/90 rounded-2xl sm:rounded-3xl shadow-[0_8px_32px_rgba(0,0,0,0.12)] dark:shadow-[0_8px_32px_rgba(0,0,0,0.5)] p-1.5 flex items-center justify-between gap-1 transition-all">
          {navItems.map((item) => {
            const isActive = currentMode === item.id;
            
            if (item.isCenter) {
              return (
                <button
                  key={item.id}
                  onClick={() => {
                    onSelectMode(item.id);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                  }}
                  className="flex-1 py-1 px-1 flex flex-col items-center justify-center relative active:scale-90 transition-transform duration-150 group cursor-pointer"
                  aria-label={item.label}
                >
                  <div className={`w-10 h-10 -mt-3 rounded-2xl flex items-center justify-center shadow-md transition-all duration-200 ${
                    isActive 
                      ? 'bg-gradient-to-tr from-amber-500 to-orange-500 text-white shadow-amber-500/30 scale-105 ring-2 ring-white dark:ring-slate-900' 
                      : 'bg-gradient-to-tr from-emerald-600 to-teal-500 text-white shadow-emerald-600/25 group-hover:scale-105'
                  }`}>
                    {item.icon}
                  </div>
                  <span className={`text-[10px] tracking-tight mt-0.5 leading-none font-bold whitespace-nowrap ${
                    isActive ? 'text-amber-600 dark:text-amber-400 font-extrabold' : 'text-slate-600 dark:text-slate-400'
                  }`}>
                    {item.label}
                  </span>
                  {isActive && (
                    <span className="w-1.5 h-1.5 rounded-full bg-amber-500 dark:bg-amber-400 mt-0.5 shadow-sm shadow-amber-500/50" />
                  )}
                </button>
              );
            }

            return (
              <button
                key={item.id}
                onClick={() => {
                  onSelectMode(item.id);
                  window.scrollTo({ top: 0, behavior: 'smooth' });
                }}
                className={`flex-1 py-1 px-1 flex flex-col items-center justify-center rounded-xl sm:rounded-2xl transition-all duration-150 relative active:scale-90 cursor-pointer ${
                  isActive
                    ? 'text-[#056839] dark:text-emerald-400 font-bold'
                    : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200'
                }`}
                aria-label={item.label}
              >
                {/* Active pill background aura with soft glass highlight */}
                {isActive && (
                  <span className="absolute inset-0 bg-emerald-500/10 dark:bg-emerald-500/20 ring-1 ring-emerald-500/20 dark:ring-emerald-400/20 rounded-xl sm:rounded-2xl -z-10 animate-in fade-in zoom-in-95 duration-100" />
                )}

                <div className={`transition-transform duration-150 ${isActive ? 'scale-110' : ''}`}>
                  {item.icon}
                </div>

                {/* Micro Label */}
                <span className="text-[10px] tracking-tight mt-0.5 leading-none font-semibold whitespace-nowrap">
                  {item.label}
                </span>

                {/* Active Indicator Dot */}
                {isActive && (
                  <span className="w-1 h-1 rounded-full bg-[#056839] dark:bg-emerald-400 mt-0.5 shadow-sm shadow-[#056839]/50" />
                )}
              </button>
            );
          })}
        </div>
      </div>
    </nav>
  );
};
