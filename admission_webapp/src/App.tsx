import { useState, useEffect, useMemo } from 'react';
import { Navbar } from './components/Navbar';
import { DecksView } from './components/DecksView';
import { SlidesView } from './components/SlidesView';
import { FlashcardsView } from './components/FlashcardsView';
import { ExamView } from './components/ExamView';
import { VaultView } from './components/VaultView';
import { AnalyticsView } from './components/AnalyticsView';
import { PredictorView } from './components/PredictorView';
import { BottomNav } from './components/BottomNav';
import { AuthModal } from './components/AuthModal';
import { CategorySwitcher } from './components/CategorySwitcher';
import { auth, onAuthStateChanged, logoutFirebase } from './lib/firebase';

import slidesData from './data/slides.json';
import flashcardsData from './data/flashcards.json';
import medicalBankData from './data/medical_bank.json';
import varsityBankData from './data/varsity_bank.json';
import predictorSetsData from './data/predictor_sets.json';
import vaultData from './data/vault.json';

import type { 
  AppMode, 
  SubjectType, 
  WeekFilterType, 
  SlideItem, 
  FlashcardItem, 
  QuizQuestion, 
  VaultData as VaultDataType,
  UserProfile,
  TrackType,
  PredictorSet
} from './types';
import { Target, Sparkles, BookOpen, Clock, ShieldCheck } from 'lucide-react';

export function App() {
  // URL Hash Synchronized Mode Routing (SPA 0ms speed + Real Browser URLs & Phone Back-Button support)
  const getInitialMode = (): AppMode => {
    try {
      const hash = window.location.hash.replace('#', '').toLowerCase();
      const validModes: AppMode[] = ['decks', 'slides', 'flashcards', 'exam', 'vault', 'analytics', 'predictor'];
      if (validModes.includes(hash as AppMode)) {
        return hash as AppMode;
      }
    } catch {
      // fallback
    }
    return 'decks';
  };

  const [currentMode, setCurrentMode] = useState<AppMode>(getInitialMode);

  // Sync mode changes to browser URL hash without page reload
  const handleSelectMode = (mode: AppMode) => {
    setCurrentMode(mode);
    try {
      if (window.location.hash.replace('#', '') !== mode) {
        window.history.pushState(null, '', `#${mode}`);
      }
    } catch {
      // fallback
    }
  };

  // Listen to browser Back / Forward navigation (popstate)
  useEffect(() => {
    const handlePopState = () => {
      try {
        const hash = window.location.hash.replace('#', '').toLowerCase();
        const validModes: AppMode[] = ['decks', 'slides', 'flashcards', 'exam', 'vault', 'analytics', 'predictor'];
        if (validModes.includes(hash as AppMode)) {
          setCurrentMode(hash as AppMode);
        } else {
          setCurrentMode('decks');
        }
      } catch {
        setCurrentMode('decks');
      }
    };
    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, []);

  const [selectedWeek, setSelectedWeek] = useState<WeekFilterType>('all');
  const [selectedSubject, setSelectedSubject] = useState<SubjectType>('All');
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);

  // Active Track Isolation: 'varsity' (Varsity 'Ka') vs 'medical' (Medical MAT)
  const [activeTrack, setActiveTrack] = useState<TrackType>(() => {
    const saved = localStorage.getItem('admission_track');
    if (saved === 'medical' || saved === 'varsity') return saved;
    return 'varsity';
  });

  const handleSelectTrack = (track: TrackType) => {
    setActiveTrack(track);
    localStorage.setItem('admission_track', track);
    setSelectedSubject('All');
    setUser((prev) => ({
      ...prev,
      target: track === 'medical' ? 'মেডিকেল ভর্তি পরীক্ষা (MAT)' : "ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট",
    }));
  };
  
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
    // Default guest profile
    return {
      name: '',
      email: '',
      avatar: '',
      target: "ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট",
      streakDays: 0,
      solvedCount: 0,
      accuracy: 0,
      isLoggedIn: false,
    };
  });

  // Listen to Firebase Auth state changes
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
      if (firebaseUser) {
        setUser((prev) => {
          const updated: UserProfile = {
            ...prev,
            name: firebaseUser.displayName || firebaseUser.email?.split('@')[0] || 'শিক্ষার্থী',
            email: firebaseUser.email || '',
            avatar: firebaseUser.photoURL || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(firebaseUser.email || 'user')}`,
            isLoggedIn: true,
          };
          localStorage.setItem('admission_user', JSON.stringify(updated));
          return updated;
        });
      }
    });
    return () => unsubscribe();
  }, []);

  const handleLogin = (profile: Partial<UserProfile>) => {
    setUser((prev) => {
      const updated = { ...prev, ...profile, isLoggedIn: true };
      localStorage.setItem('admission_user', JSON.stringify(updated));
      return updated;
    });
  };

  const handleLogout = async () => {
    try {
      await logoutFirebase();
    } catch (e) {
      console.warn('Firebase logout notice:', e);
    }
    setUser({
      name: '',
      email: '',
      avatar: '',
      target: "ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট",
      streakDays: 0,
      solvedCount: 0,
      accuracy: 0,
      isLoggedIn: false,
    });
    localStorage.removeItem('admission_user');
  };

  const slides = slidesData as SlideItem[];
  const flashcards = flashcardsData as FlashcardItem[];
  const vault = vaultData as VaultDataType;

  // Strict Track Question Isolation (Medical vs Varsity 'Ka')
  const currentQuizzes = useMemo(() => {
    return (activeTrack === 'medical' ? medicalBankData : varsityBankData) as QuizQuestion[];
  }, [activeTrack]);

  // Combined predictor sets
  const allPredictorSets = useMemo(() => {
    const data = predictorSetsData as { varsity_sets: PredictorSet[]; medical_sets: PredictorSet[] };
    return [...(data.varsity_sets || []), ...(data.medical_sets || [])];
  }, []);

  return (
    <div className="min-h-screen overflow-x-hidden bg-[#F6F8F6] dark:bg-slate-950 text-slate-800 dark:text-slate-100 flex flex-col font-['Hind_Siliguri'] antialiased transition-colors duration-200">
      
      {/* Top Navbar with Chorcha Pill Controls, Track Switcher, Google Login, & Dark/Light Toggle */}
      <Navbar
        currentMode={currentMode}
        onSelectMode={handleSelectMode}
        selectedWeek={selectedWeek}
        onSelectWeek={setSelectedWeek}
        selectedSubject={selectedSubject}
        onSelectSubject={setSelectedSubject}
        theme={theme}
        onToggleTheme={toggleTheme}
        user={user}
        onOpenAuth={() => setIsAuthModalOpen(true)}
        onLogout={handleLogout}
        activeTrack={activeTrack}
        onSelectTrack={handleSelectTrack}
      />

      {/* Main Mode View Area */}
      <main className="flex-1 overflow-x-hidden pb-28">
        {currentMode === 'decks' && (
          <DecksView
            onSelectMode={handleSelectMode}
            onSelectSubject={setSelectedSubject}
            selectedWeek={selectedWeek}
            onSelectWeek={setSelectedWeek}
            user={user}
            onOpenAuth={() => setIsAuthModalOpen(true)}
            totalSlides={slides.length}
            totalFlashcards={flashcards.length}
            totalQuizzes={currentQuizzes.length}
            activeTrack={activeTrack}
            onSelectTrack={handleSelectTrack}
          />
        )}

        {currentMode === 'exam' && (
          <ExamView
            quizzes={currentQuizzes}
            selectedWeek={selectedWeek}
            selectedSubject={selectedSubject}
          />
        )}

        {currentMode === 'predictor' && (
          <PredictorView
            activeTrack={activeTrack}
            questions={currentQuizzes}
            predictorSets={allPredictorSets}
            onSelectTrack={handleSelectTrack}
          />
        )}

        {currentMode === 'vault' && (
          <VaultView 
            vault={vault} 
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

        {currentMode === 'analytics' && (
          <AnalyticsView
            user={user}
            onOpenAuth={() => setIsAuthModalOpen(true)}
            onSelectMode={handleSelectMode}
            activeTrack={activeTrack}
          />
        )}

        {/* Section-Based Quick Category Switcher (shown when studying concepts/formula/vault) */}
        {(currentMode === 'slides' || currentMode === 'vault') && (
          <CategorySwitcher
            currentMode={currentMode}
            onSelectMode={handleSelectMode}
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
              <Clock className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> {currentQuizzes.length} রিয়েল MCQ
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
        onSelectMode={handleSelectMode}
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
