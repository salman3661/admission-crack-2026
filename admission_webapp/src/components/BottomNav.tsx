import React from 'react';
import { 
  LayoutDashboard, 
  Target, 
  ShieldAlert, 
  Sparkles
} from 'lucide-react';
import type { AppMode } from '../types';

interface BottomNavProps {
  currentMode: AppMode;
  onSelectMode: (mode: AppMode) => void;
}

interface BottomNavItem {
  id: AppMode;
  label: string;
  sublabel: string;
  icon: React.ReactNode;
}

const NAV_ITEMS: BottomNavItem[] = [
  {
    id: 'decks',
    label: 'ড্যাশবোর্ড',
    sublabel: 'Dashboard',
    icon: <LayoutDashboard className="w-[19px] h-[19px]" />,
  },
  {
    id: 'exam',
    label: 'প্র্যাকটিস ড্রিল',
    sublabel: 'Practice Drill',
    icon: <Target className="w-[19px] h-[19px]" />,
  },
  {
    id: 'vault',
    label: 'ট্র্যাপ ভল্ট',
    sublabel: 'Trap Vault',
    icon: <ShieldAlert className="w-[19px] h-[19px]" />,
  },
  {
    id: 'recall',
    label: 'GK/English ডেক',
    sublabel: 'GK/English Deck',
    icon: <Sparkles className="w-[19px] h-[19px]" />,
  },
];

const BottomNavComponent: React.FC<BottomNavProps> = ({
  currentMode,
  onSelectMode,
}) => {
  return (
    <nav className="fixed bottom-0 inset-x-0 z-40 pointer-events-none pb-safe select-none">
      <div className="pointer-events-auto max-w-md mx-auto mb-2 sm:mb-3 px-3">
        <div className="backdrop-blur-2xl bg-white/90 dark:bg-slate-900/90 ring-1 ring-slate-200/90 dark:ring-slate-800/90 rounded-2xl shadow-[0_10px_35px_rgba(0,0,0,0.12)] dark:shadow-[0_10px_35px_rgba(0,0,0,0.5)] p-1.5 flex items-center justify-around gap-1 transition-all">
          {NAV_ITEMS.map((item) => {
            const isActive = currentMode === item.id || (item.id === 'decks' && currentMode === 'blueprint');

            return (
              <button
                key={item.id}
                onClick={() => {
                  onSelectMode(item.id);
                  window.scrollTo({ top: 0, behavior: 'smooth' });
                }}
                className={`flex-1 py-1.5 px-1 flex flex-col items-center justify-center rounded-xl transition-all duration-150 relative active:scale-95 cursor-pointer group ${
                  isActive
                    ? 'text-emerald-700 dark:text-emerald-400 font-extrabold'
                    : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200'
                }`}
                aria-label={`${item.label} (${item.sublabel})`}
              >
                {/* Active pill aura */}
                {isActive && (
                  <span className="absolute inset-0 bg-emerald-500/10 dark:bg-emerald-500/20 ring-1 ring-emerald-500/25 dark:ring-emerald-400/25 rounded-xl -z-10 animate-in fade-in zoom-in-95 duration-100" />
                )}

                <div className={`transition-transform duration-150 ${isActive ? 'scale-110 text-emerald-600 dark:text-emerald-400' : 'group-hover:scale-105'}`}>
                  {item.icon}
                </div>

                {/* Micro Label */}
                <span className="text-[10px] sm:text-[11px] tracking-tight mt-1 leading-none font-bold whitespace-nowrap">
                  {item.label}
                </span>

                {/* Active Dot Indicator */}
                {isActive && (
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-600 dark:bg-emerald-400 mt-1 shadow-sm shadow-emerald-500/50" />
                )}
              </button>
            );
          })}
        </div>
      </div>
    </nav>
  );
};

export const BottomNav = React.memo(BottomNavComponent);
