import { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { DecksView } from './components/DecksView';
import { SlidesView } from './components/SlidesView';
import { FlashcardsView } from './components/FlashcardsView';
import { ExamView } from './components/ExamView';
import { VaultView } from './components/VaultView';
import { AnalyticsView } from './components/AnalyticsView';
import { BottomNav } from './components/BottomNav';
import { AuthModal } from './components/AuthModal';

import slidesData from './data/slides.json';
import flashcardsData from './data/flashcards.json';
import quizzesData from './data/quizzes.json';
import vaultData from './data/vault.json';

import type { 
  AppMode, 
  SubjectType, 
  WeekFilterType, 
  SlideItem, 
  FlashcardItem, 
  QuizQuestion, 
  VaultData as VaultDataType,
  UserProfile 
} from './types';
import { Target, Sparkles, BookOpen, Clock, ShieldCheck } from 'lucide-react';

export function App() {
  const [currentMode, setCurrentMode] = useState<AppMode>('decks');
  const [selectedWeek, setSelectedWeek] = useState<WeekFilterType>('all');
  const [selectedSubject, setSelectedSubject] = useState<SubjectType>('All');
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);
  
  // Theme state: defaults to light for the ultra-clean Chorcha look, with toggleable dark mode
  const [theme, setTheme] = useState<'dark' | 'light'>(() => {
    const saved = localStorage.getItem('admission_theme');
    if (saved === 'light' || saved === 'dark') return saved;
    return 'light';
  });

  useEffect(() => {
    const root = document.documentElement;
    if (theme === 'dark') {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
    localStorage.setItem('admission_theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((prev) => (prev === 'dark' ? 'light' : 'dark'));
  };

  // User Profile state with Google authentication support
  const [user, setUser] = useState<UserProfile>(() => {
    const savedUser = localStorage.getItem('admission_user');
    if (savedUser) {
      try {
        return JSON.parse(savedUser);
      } catch {
        // fallback
      }
    }
    // Default active candidate profile
    return {
      name: 'হাসিবুল হাসান',
      email: 'hasibul.du26@gmail.com',
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&auto=format&fit=crop&q=80',
      target: "ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট",
      streakDays: 5,
      solvedCount: 142,
      accuracy: 89,
      isLoggedIn: true,
    };
  });

  const handleLogin = (profile: Partial<UserProfile>) => {
    setUser((prev) => {
      const updated = { ...prev, ...profile, isLoggedIn: true };
      localStorage.setItem('admission_user', JSON.stringify(updated));
      return updated;
    });
  };

  const handleLogout = () => {
    setUser((prev) => {
      const updated = { ...prev, isLoggedIn: false };
      localStorage.setItem('admission_user', JSON.stringify(updated));
      return updated;
    });
  };

  const slides = slidesData as SlideItem[];
  const flashcards = flashcardsData as FlashcardItem[];
  const quizzes = quizzesData as QuizQuestion[];
  const vault = vaultData as VaultDataType;

  return (
    <div className="min-h-screen bg-[#F6F8F6] dark:bg-[#0B110D] text-slate-800 dark:text-slate-100 flex flex-col font-['Hind_Siliguri'] antialiased transition-colors duration-200">
      
      {/* Top Navbar with Chorcha Pill Controls, Google Login, & Dark/Light Toggle */}
      <Navbar
        currentMode={currentMode}
        onSelectMode={setCurrentMode}
        selectedWeek={selectedWeek}
        onSelectWeek={setSelectedWeek}
        selectedSubject={selectedSubject}
        onSelectSubject={setSelectedSubject}
        theme={theme}
        onToggleTheme={toggleTheme}
        user={user}
        onOpenAuth={() => setIsAuthModalOpen(true)}
      />

      {/* Main Mode View Area */}
      <main className="flex-1 pb-dock">
        {currentMode === 'decks' && (
          <DecksView
            onSelectMode={setCurrentMode}
            onSelectSubject={setSelectedSubject}
            selectedWeek={selectedWeek}
            onSelectWeek={setSelectedWeek}
            user={user}
            onOpenAuth={() => setIsAuthModalOpen(true)}
            totalSlides={slides.length}
            totalFlashcards={flashcards.length}
            totalQuizzes={quizzes.length}
          />
        )}

        {currentMode === 'exam' && (
          <ExamView
            quizzes={quizzes}
            selectedWeek={selectedWeek}
            selectedSubject={selectedSubject}
          />
        )}

        {currentMode === 'slides' && (
          <SlidesView
            slides={slides}
            selectedWeek={selectedWeek}
            selectedSubject={selectedSubject}
          />
        )}

        {currentMode === 'flashcards' && (
          <FlashcardsView
            flashcards={flashcards}
            selectedWeek={selectedWeek}
            selectedSubject={selectedSubject}
          />
        )}

        {currentMode === 'vault' && (
          <VaultView vault={vault} />
        )}

        {currentMode === 'analytics' && (
          <AnalyticsView
            user={user}
            onOpenAuth={() => setIsAuthModalOpen(true)}
            onSelectMode={setCurrentMode}
          />
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-200/80 dark:border-[#1E2F24] bg-white/70 dark:bg-[#0D1410]/70 py-6 px-4 text-center text-xs text-slate-500 dark:text-slate-400 transition-colors hidden sm:block pb-24">
        <div className="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <Target className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
            <span className="font-semibold text-slate-700 dark:text-slate-300">
              Admission Crack 2026 • Chorcha UI Edition
            </span>
          </div>

          <div className="flex items-center gap-4 text-[11px] text-slate-600 dark:text-slate-400 font-medium">
            <span className="flex items-center gap-1">
              <BookOpen className="w-3.5 h-3.5 text-cyan-600 dark:text-cyan-400" /> {slides.length} স্লাইড
            </span>
            <span className="flex items-center gap-1">
              <Sparkles className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" /> {flashcards.length} ফ্ল্যাশকার্ড
            </span>
            <span className="flex items-center gap-1">
              <Clock className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> {quizzes.length} রিয়েল MCQ
            </span>
          </div>

          <div className="text-[11px] text-slate-500 dark:text-slate-400 font-mono flex items-center gap-1">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-500" />
            Vercel Edge Ready
          </div>
        </div>
      </footer>

      {/* 4. MOBILE-FIRST BOTTOM NAVIGATION DOCK:
          Sticky bottom navigation bar with rounded icons and micro-labels:
          [ 🏠 ডেক ]  [ 📚 প্রশ্নব্যাংক ]  [ ⚡ এক্সপেক্টেড ]  [ 🃏 কার্ডস ]  [ 📊 অ্যানালিটিক্স ] */}
      <BottomNav
        currentMode={currentMode}
        onSelectMode={setCurrentMode}
      />

      {/* Google Authentication & Profile Modal */}
      <AuthModal
        isOpen={isAuthModalOpen}
        onClose={() => setIsAuthModalOpen(false)}
        user={user}
        onLogin={handleLogin}
        onLogout={handleLogout}
      />
    </div>
  );
}

export default App;
