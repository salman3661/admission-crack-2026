import { useState, useEffect, useMemo } from 'react';
import { Navbar } from './components/Navbar';
import { DecksView } from './components/DecksView';
import { SlidesView } from './components/SlidesView';
import { FlashcardsView } from './components/FlashcardsView';
import { ActiveRecallView } from './components/ActiveRecallView';
import { ExamView } from './components/ExamView';
import { VaultView } from './components/VaultView';
import { AnalyticsView } from './components/AnalyticsView';
import { PredictorView } from './components/PredictorView';
import { ChapterBlueprintView } from './components/ChapterBlueprintView';
import { PaperFinalView } from './components/PaperFinalView';
import { SubjectFinalView } from './components/SubjectFinalView';
import { FullMockView } from './components/FullMockView';
import { BottomNav } from './components/BottomNav';
import { AuthModal } from './components/AuthModal';
import { CategorySwitcher } from './components/CategorySwitcher';
import { auth, onAuthStateChanged, logoutFirebase } from './lib/firebase';

import slidesData from './data/slides.json';
import flashcardsData from './data/flashcards.json';
import weeklyExamsData from './data/weekly_exams.json';
import subjectFinalData from './data/subject_final_bank.json';
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
  PredictorSet,
  SubjectFinalBank
} from './types';

export function App() {
  // URL Hash Synchronized Mode Routing (SPA 0ms speed + Real Browser URLs & Phone Back-Button support)
  const resolveModeFromHash = (rawHash: string): AppMode => {
    const hash = rawHash.replace('#', '').toLowerCase();
    if (hash === 'activerecall' || hash === 'active-recall' || hash === 'recall') return 'recall';
    if (hash === 'weekly' || hash === 'weeks' || hash === 'weekly-mastery') return 'weekly';
    if (hash === 'paper-final' || hash === 'paper_final' || hash === 'paperfinal') return 'paper_final';
    if (hash === 'subject-final' || hash === 'subject_final' || hash === 'subjectfinal') return 'subject_final';
    if (hash === 'full-mock' || hash === 'full_mock' || hash === 'fullmock') return 'full_mock';
    const validModes: AppMode[] = [
      'decks', 'weekly', 'paper_final', 'subject_final', 'full_mock',
      'exam', 'predictor', 'slides', 'flashcards', 'analytics', 'vault', 'recall', 'blueprint'
    ];
    if (validModes.includes(hash as AppMode)) {
      return hash as AppMode;
    }
    return 'decks';
  };

  const getInitialMode = (): AppMode => {
    try {
      return resolveModeFromHash(window.location.hash);
    } catch {
      return 'decks';
    }
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
        setCurrentMode(resolveModeFromHash(window.location.hash));
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
    setSelectedWeek('all');
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

  // Tier 3: Strict Track Question Isolation (Medical vs Varsity 'Ka')
  const subjectBank = subjectFinalData as unknown as SubjectFinalBank;
  const currentQuizzes = useMemo(() => {
    return (activeTrack === 'medical' ? subjectBank.medical : subjectBank.varsity) as QuizQuestion[];
  }, [activeTrack, subjectBank]);

  // Tier 1: Strictly isolated Weekly Solve Sheet pool for Practice Drill when a week is selected
  const weeklyQuizzes = useMemo(() => {
    return weeklyExamsData as QuizQuestion[];
  }, []);

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

        {/* TIER 1: WEEKLY MODE (weekly_exams.json) */}
        {currentMode === 'weekly' && (
          <ChapterBlueprintView
            onSelectMode={handleSelectMode}
            onSelectWeek={setSelectedWeek}
            onSelectSubject={setSelectedSubject}
            forcedWorkflowMode="weekly"
          />
        )}

        {/* TIER 2: PAPER FINAL SECTION (paper_final_bank.json) */}
        {currentMode === 'paper_final' && (
          <PaperFinalView activeTrack={activeTrack} />
        )}

        {/* TIER 3: SUBJECT-WISE FINAL MODEL (subject_final_bank.json) */}
        {currentMode === 'subject_final' && (
          <SubjectFinalView
            activeTrack={activeTrack}
            selectedSubject={selectedSubject}
            onSelectSubject={setSelectedSubject}
          />
        )}

        {/* TIER 4: FINAL MODEL TEST (full_mock_bank.json) */}
        {currentMode === 'full_mock' && (
          <FullMockView activeTrack={activeTrack} />
        )}

        {currentMode === 'exam' && (
          <ExamView
            quizzes={selectedWeek !== 'all' ? weeklyQuizzes : currentQuizzes}
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
            onSelectWeek={setSelectedWeek}
            selectedSubject={selectedSubject}
            onSelectSubject={setSelectedSubject}
            activeTrack={activeTrack}
            onSelectMode={handleSelectMode}
          />
        )}

        {currentMode === 'recall' && (
          <ActiveRecallView onSelectMode={handleSelectMode} />
        )}

        {currentMode === 'blueprint' && (
          <ChapterBlueprintView
            onSelectMode={handleSelectMode}
            onSelectWeek={setSelectedWeek}
            onSelectSubject={setSelectedSubject}
            forcedWorkflowMode="blueprint"
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
