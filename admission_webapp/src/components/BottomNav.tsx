import React from 'react';
import {
  LayoutDashboard,
  Calendar,
  FileText,
  Layers,
  User,
} from 'lucide-react';
import type { AppMode } from '../types';

interface BottomNavProps {
  currentMode: AppMode;
  currentPath?: string;
  onSelectMode: (mode: AppMode) => void;
  onNavigate?: (path: string) => void;
}

interface BottomNavItem {
  id: string;
  path: string;
  mode?: AppMode;
  label: string;
  icon: React.ReactNode;
}

const NAV_ITEMS: BottomNavItem[] = [
  {
    id: 'home',
    path: '/',
    mode: 'decks',
    label: 'হোম',
    icon: <LayoutDashboard className="w-[19px] h-[19px]" />,
  },
  {
    id: 'weekly',
    path: '/weekly',
    mode: 'weekly',
    label: 'Weekly',
    icon: <Calendar className="w-[19px] h-[19px]" />,
  },
  {
    id: 'paper_final',
    path: '/paper-final',
    mode: 'paper_final',
    label: 'Paper Final',
    icon: <FileText className="w-[19px] h-[19px]" />,
  },
  {
    id: 'chapters',
    path: '/chapters',
    mode: 'blueprint',
    label: 'অধ্যায়',
    icon: <Layers className="w-[19px] h-[19px]" />,
  },
  {
    id: 'account',
    path: '/account',
    label: 'প্রোফাইল',
    icon: <User className="w-[19px] h-[19px]" />,
  },
];

const BottomNavComponent: React.FC<BottomNavProps> = ({
  currentMode,
  currentPath = '/',
  onSelectMode,
  onNavigate,
}) => {
  return (
    <nav className="fixed bottom-0 inset-x-0 z-40 select-none backdrop-blur-md bg-white/90 dark:bg-slate-900/90 border-t border-slate-200/70 dark:border-slate-800/70 pb-[env(safe-area-inset-bottom)]">
      <div className="max-w-md mx-auto px-2">
        <div className="py-1.5 flex items-center justify-around gap-1">
          {NAV_ITEMS.map((item) => {
            const isActive =
              currentPath === item.path ||
              (item.mode !== undefined && currentMode === item.mode && currentPath !== '/account');

            return (
              <button
                key={item.id}
                onClick={() => {
                  if (onNavigate) {
                    onNavigate(item.path);
                  } else if (item.mode) {
                    onSelectMode(item.mode);
                  }
                  window.scrollTo({ top: 0, behavior: 'smooth' });
                }}
                className={`flex-1 py-1.5 px-1 flex flex-col items-center justify-center rounded-xl transition-all duration-150 relative active:scale-95 cursor-pointer group ${
                  isActive
                    ? 'text-emerald-700 dark:text-emerald-400 font-extrabold'
                    : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200'
                }`}
                aria-label={item.label}
              >
                {isActive && (
                  <span className="absolute inset-0 bg-emerald-500/10 dark:bg-emerald-500/20 ring-1 ring-emerald-500/25 dark:ring-emerald-400/25 rounded-xl -z-10" />
                )}

                <div className={`transition-transform duration-150 ${isActive ? 'scale-110 text-emerald-600 dark:text-emerald-400' : 'group-hover:scale-105'}`}>
                  {item.icon}
                </div>

                <span className="text-[10px] sm:text-[11px] tracking-tight mt-1 leading-none font-bold whitespace-nowrap">
                  {item.label}
                </span>

                {isActive && (
                  <span className="w-1 h-1 rounded-full bg-emerald-600 dark:bg-emerald-400 mt-1" />
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
