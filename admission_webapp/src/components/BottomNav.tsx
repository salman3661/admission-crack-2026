import React from 'react';
import { 
  Home, 
  BookOpen, 
  Zap, 
  Layers, 
  BarChart3 
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
  const navItems: { id: AppMode; label: string; icon: React.ReactNode; badge?: string }[] = [
    {
      id: 'decks',
      label: '🏠 ডেক',
      icon: <Home className="w-5 h-5" />,
    },
    {
      id: 'exam',
      label: '📚 প্রশ্নব্যাংক',
      icon: <BookOpen className="w-5 h-5" />,
      badge: '300',
    },
    {
      id: 'slides',
      label: '⚡ এক্সপেক্টেড',
      icon: <Zap className="w-5 h-5" />,
      badge: '42',
    },
    {
      id: 'flashcards',
      label: '🃏 কার্ডস',
      icon: <Layers className="w-5 h-5" />,
    },
    {
      id: 'analytics',
      label: '📊 অ্যানালিটিক্স',
      icon: <BarChart3 className="w-5 h-5" />,
    },
  ];

  return (
    <nav className="fixed bottom-0 inset-x-0 z-40 pointer-events-none pb-safe">
      <div className="pointer-events-auto max-w-lg mx-auto sm:mb-3">
        <div className="bg-white/95 dark:bg-[#0D1410]/95 backdrop-blur-xl border-t sm:border border-slate-200/90 dark:border-[#1E2F24] sm:rounded-3xl shadow-[0_-4px_24px_rgba(0,0,0,0.08)] dark:shadow-[0_-4px_24px_rgba(0,0,0,0.4)] px-2 py-1.5 flex items-center justify-around transition-all">
          {navItems.map((item) => {
            // Also treat 'vault' as part of analytics/vault navigation
            const isActive = currentMode === item.id || (item.id === 'analytics' && currentMode === 'vault');
            
            return (
              <button
                key={item.id}
                onClick={() => onSelectMode(item.id)}
                className={`flex-1 py-1 px-1.5 flex flex-col items-center justify-center rounded-2xl transition-all duration-200 relative group active:scale-95 ${
                  isActive
                    ? 'text-[#056839] dark:text-emerald-400 font-bold'
                    : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200'
                }`}
                aria-label={item.label}
              >
                {/* Active pill background aura */}
                {isActive && (
                  <span className="absolute inset-0 bg-[#056839]/10 dark:bg-[#056839]/25 rounded-2xl -z-10 animate-in fade-in zoom-in-95 duration-150" />
                )}

                {/* Icon with relative badge */}
                <div className="relative">
                  <div className={`transition-transform duration-200 ${isActive ? 'scale-110' : 'group-hover:scale-105'}`}>
                    {item.icon}
                  </div>
                  {item.badge && !isActive && (
                    <span className="absolute -top-1 -right-2 px-1 text-[9px] font-bold rounded-full bg-emerald-500 text-white leading-none py-0.5">
                      {item.badge}
                    </span>
                  )}
                </div>

                {/* Micro Label */}
                <span className="text-[11px] tracking-tight mt-0.5 leading-none font-medium whitespace-nowrap">
                  {item.label}
                </span>

                {/* Active Indicator Dot */}
                {isActive && (
                  <span className="w-1.5 h-1.5 rounded-full bg-[#056839] dark:bg-emerald-400 mt-0.5 shadow-sm shadow-[#056839]/40" />
                )}
              </button>
            );
          })}
        </div>
      </div>
    </nav>
  );
};
