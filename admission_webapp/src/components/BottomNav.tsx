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
  const navItems: { id: AppMode; label: string; icon: React.ReactNode }[] = [
    {
      id: 'decks',
      label: '🏠 ডেক',
      icon: <Home className="w-4 h-4" />,
    },
    {
      id: 'exam',
      label: '📚 প্রশ্নব্যাংক',
      icon: <BookOpen className="w-4 h-4" />,
    },
    {
      id: 'predictor',
      label: '🔮 প্রেডিকশন',
      icon: <Sparkles className="w-4 h-4" />,
    },
    {
      id: 'vault',
      label: '⚡ ভল্ট',
      icon: <Zap className="w-4 h-4" />,
    },
    {
      id: 'analytics',
      label: '📊 অ্যানালিটিক্স',
      icon: <BarChart3 className="w-4 h-4" />,
    },
  ];

  return (
    <nav className="fixed bottom-0 inset-x-0 z-40 pointer-events-none pb-safe">
      <div className="pointer-events-auto max-w-md mx-auto sm:mb-2">
        <div className="backdrop-blur-none md:backdrop-blur-xl bg-white dark:bg-slate-900 border-t sm:border border-slate-200 dark:border-slate-800 sm:rounded-2xl shadow-[0_-4px_20px_rgba(0,0,0,0.06)] dark:shadow-[0_-4px_20px_rgba(0,0,0,0.4)] px-1.5 py-1 flex items-center justify-around transition-all">
          {navItems.map((item) => {
            const isActive = currentMode === item.id;
            
            return (
              <button
                key={item.id}
                onClick={() => {
                  onSelectMode(item.id);
                  window.scrollTo({ top: 0, behavior: 'smooth' });
                }}
                className={`flex-1 py-1 px-1 flex flex-col items-center justify-center rounded-xl transition-all duration-150 relative active:scale-95 ${
                  isActive
                    ? 'text-[#056839] dark:text-emerald-400 font-bold'
                    : 'text-zinc-500 dark:text-zinc-400 hover:text-zinc-800 dark:hover:text-zinc-200'
                }`}
                aria-label={item.label}
              >
                {/* Active pill background aura */}
                {isActive && (
                  <span className="absolute inset-0 bg-[#056839]/10 dark:bg-[#056839]/20 rounded-xl -z-10 animate-in fade-in zoom-in-95 duration-100" />
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
                  <span className="w-1 h-1 rounded-full bg-[#056839] dark:bg-emerald-400 mt-0.5 shadow-sm shadow-[#056839]/40" />
                )}
              </button>
            );
          })}
        </div>
      </div>
    </nav>
  );
};
