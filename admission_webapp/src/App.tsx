import React, { useState, useEffect, Suspense, lazy } from 'react';
import { Navbar } from './components/Navbar';
import { BottomNav } from './components/BottomNav';
import { AuthModal } from './components/AuthModal';
import { auth, onAuthStateChanged, logoutFirebase } from './lib/firebase';
import type {
  AppMode,
  SubjectType,
  WeekFilterType,
  UserProfile,
  TrackType,
  SlideItem,
  FlashcardItem,
  VaultData as VaultDataType,
} from './types';

// Route-level code splitting (Rule 2: < 500 KB gzip initial payload)
const HomeHubView = lazy(() => import('./components/HomeHubView').then((m) => ({ default: m.HomeHubView })));
const RealExamSimulator = lazy(() => import('./components/RealExamSimulator').then((m) => ({ default: m.RealExamSimulator })));
const MasterSetView = lazy(() => import('./components/MasterSetView').then((m) => ({ default: m.MasterSetView })));
const MistakeBookView = lazy(() => import('./components/MistakeBookView').then((m) => ({ default: m.MistakeBookView })));
const WeaknessRadarView = lazy(() => import('./components/WeaknessRadarView').then((m) => ({ default: m.WeaknessRadarView })));
const MockTrackerView = lazy(() => import('./components/MockTrackerView').then((m) => ({ default: m.MockTrackerView })));
const ChapterExplorerView = lazy(() => import('./components/ChapterExplorerView').then((m) => ({ default: m.ChapterExplorerView })));
const FormulaCardsView = lazy(() => import('./components/FormulaCardsView').then((m) => ({ default: m.FormulaCardsView })));
const PaperBankView = lazy(() => import('./components/PaperBankView').then((m) => ({ default: m.PaperBankView })));
const ActiveRecallView = lazy(() => import('./components/ActiveRecallView').then((m) => ({ default: m.ActiveRecallView })));
const FlashcardsView = lazy(() => import('./components/FlashcardsView').then((m) => ({ default: m.FlashcardsView })));
const SlidesView = lazy(() => import('./components/SlidesView').then((m) => ({ default: m.SlidesView })));
const VaultView = lazy(() => import('./components/VaultView').then((m) => ({ default: m.VaultView })));
const AnalyticsView = lazy(() => import('./components/AnalyticsView').then((m) => ({ default: m.AnalyticsView })));
const QuestionMatcherView = lazy(() => import('./components/QuestionMatcherView').then((m) => ({ default: m.QuestionMatcherView })));
const BookmarksView = lazy(() => import('./components/BookmarksView').then((m) => ({ default: m.BookmarksView })));
const AccountCornerView = lazy(() => import('./components/AccountCornerView').then((m) => ({ default: m.AccountCornerView })));
const NotFoundView = lazy(() => import('./components/NotFoundView').then((m) => ({ default: m.NotFoundView })));

const MODE_TO_PATH: Record<AppMode, string> = {
  decks: '/',
  weekly: '/weekly',
  paper_final: '/paper-final',
  subject_final: '/subject-final',
  full_mock: '/simulator',
  exam: '/bank',
  predictor: '/master-set',
  slides: '/slides',
  flashcards: '/flashcards',
  analytics: '/analytics',
  vault: '/vault',
  recall: '/recall',
  blueprint: '/chapters',
};

function normalizePath(rawPath: string): string {
  const clean = rawPath.replace(/\/+$/, '') || '/';
  return clean.toLowerCase();
}

function pathToMode(path: string): AppMode {
  const p = normalizePath(path);
  if (p === '/') return 'decks';
  if (p === '/weekly') return 'weekly';
  if (p === '/paper-final') return 'paper_final';
  if (p === '/subject-final') return 'subject_final';
  if (p === '/simulator' || p === '/full-mock') return 'full_mock';
  if (p === '/bank' || p === '/exam') return 'exam';
  if (p === '/master-set' || p === '/predictor') return 'predictor';
  if (p === '/slides') return 'slides';
  if (p === '/flashcards') return 'flashcards';
  if (p === '/analytics') return 'analytics';
  if (p === '/vault') return 'vault';
  if (p === '/recall') return 'recall';
  if (p === '/chapters' || p === '/blueprint') return 'blueprint';
  return 'decks';
}

const KNOWN_PATHS = new Set([
  '/',
  '/weekly',
  '/paper-final',
  '/subject-final',
  '/simulator',
  '/full-mock',
  '/bank',
  '/exam',
  '/master-set',
  '/predictor',
  '/mistake-book',
  '/weakness-radar',
  '/mock-tracker',
  '/chapters',
  '/blueprint',
  '/formulas',
  '/matcher',
  '/bookmarks',
  '/account',
  '/recall',
  '/flashcards',
  '/slides',
  '/vault',
  '/analytics',
]);

// Lazy wrappers for legacy JSON-backed P1 views
const LazySlidesWrapper: React.FC<{ selectedWeek: WeekFilterType; selectedSubject: SubjectType }> = ({
  selectedWeek,
  selectedSubject,
}) => {
  const [slides, setSlides] = useState<SlideItem[]>([]);
  useEffect(() => {
    import('./data/slides.json').then((m) => setSlides((m.default || []) as SlideItem[]));
  }, []);
  return <SlidesView slides={slides} selectedWeek={selectedWeek} selectedSubject={selectedSubject} />;
};

const LazyFlashcardsWrapper: React.FC<{
  selectedWeek: WeekFilterType;
  onSelectWeek: (w: WeekFilterType) => void;
  selectedSubject: SubjectType;
  onSelectSubject: (s: SubjectType) => void;
  activeTrack: TrackType;
  onSelectMode: (m: AppMode) => void;
}> = (props) => {
  const [flashcards, setFlashcards] = useState<FlashcardItem[]>([]);
  useEffect(() => {
    import('./data/flashcards.json').then((m) => setFlashcards((m.default || []) as FlashcardItem[]));
  }, []);
  return <FlashcardsView flashcards={flashcards} {...props} />;
};

const LazyVaultWrapper: React.FC<{ selectedWeek: WeekFilterType; selectedSubject: SubjectType }> = ({
  selectedWeek,
  selectedSubject,
}) => {
  const [vault, setVault] = useState<VaultDataType | null>(null);
  useEffect(() => {
    import('./data/vault.json').then((m) => setVault(m.default as VaultDataType));
  }, []);
  if (!vault) return <div className="p-10 text-center text-sm text-slate-500">ভল্ট লোড হচ্ছে...</div>;
  return <VaultView vault={vault} selectedWeek={selectedWeek} selectedSubject={selectedSubject} />;
};

export function App() {
  const [currentPath, setCurrentPath] = useState<string>(() => {
    // Support legacy #hash URLs by normalizing to pathname
    if (window.location.hash && window.location.hash.length > 1) {
      const h = window.location.hash.replace('#', '').toLowerCase().replace(/_/g, '-');
      const mapped = `/${h === 'decks' ? '' : h}`;
      window.history.replaceState(null, '', mapped);
      return normalizePath(mapped);
    }
    return normalizePath(window.location.pathname);
  });

  const navigate = (path: string) => {
    const clean = normalizePath(path);
    setCurrentPath(clean);
    if (normalizePath(window.location.pathname) !== clean) {
      window.history.pushState(null, '', clean);
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleSelectMode = (mode: AppMode) => {
    navigate(MODE_TO_PATH[mode] || '/');
  };

  useEffect(() => {
    const onPop = () => setCurrentPath(normalizePath(window.location.pathname));
    window.addEventListener('popstate', onPop);
    return () => window.removeEventListener('popstate', onPop);
  }, []);

  const [selectedWeek, setSelectedWeek] = useState<WeekFilterType>('all');
  const [selectedSubject, setSelectedSubject] = useState<SubjectType>('All');
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);

  const [activeTrack, setActiveTrack] = useState<TrackType>(() => {
    const saved = localStorage.getItem('admission_track');
    return saved === 'medical' || saved === 'varsity' ? saved : 'varsity';
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

  const [theme, setTheme] = useState<'dark' | 'light'>(() => {
    const saved = localStorage.getItem('admission_theme');
    return saved === 'light' || saved === 'dark' ? saved : 'light';
  });

  useEffect(() => {
    const root = document.documentElement;
    if (theme === 'dark') root.classList.add('dark');
    else root.classList.remove('dark');
    localStorage.setItem('admission_theme', theme);
  }, [theme]);

  const [user, setUser] = useState<UserProfile>(() => {
    const savedUser = localStorage.getItem('admission_user');
    if (savedUser) {
      try {
        return JSON.parse(savedUser);
      } catch {
        // fallback
      }
    }
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

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
      if (firebaseUser) {
        setUser((prev) => {
          const updated: UserProfile = {
            ...prev,
            name: firebaseUser.displayName || firebaseUser.email?.split('@')[0] || 'শিক্ষার্থী',
            email: firebaseUser.email || '',
            avatar:
              firebaseUser.photoURL ||
              `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(firebaseUser.email || 'user')}`,
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
    } catch {
      // ignore
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

  const currentMode = pathToMode(currentPath);

  const renderRoute = () => {
    if (!KNOWN_PATHS.has(currentPath)) {
      return <NotFoundView onGoHome={() => navigate('/')} />;
    }
    switch (currentPath) {
      case '/':
        return <HomeHubView activeTrack={activeTrack} onNavigate={navigate} />;
      case '/simulator':
      case '/full-mock':
        return <RealExamSimulator activeTrack={activeTrack} onOpenMockTracker={() => navigate('/mock-tracker')} />;
      case '/master-set':
      case '/predictor':
        return <MasterSetView activeTrack={activeTrack} />;
      case '/mistake-book':
        return <MistakeBookView />;
      case '/weakness-radar':
        return <WeaknessRadarView />;
      case '/mock-tracker':
        return <MockTrackerView />;
      case '/chapters':
      case '/blueprint':
        return <ChapterExplorerView activeTrack={activeTrack} />;
      case '/formulas':
        return <FormulaCardsView />;
      case '/matcher':
        return <QuestionMatcherView />;
      case '/bookmarks':
        return <BookmarksView />;
      case '/account':
        return (
          <AccountCornerView
            user={user}
            activeTrack={activeTrack}
            onSelectTrack={handleSelectTrack}
            onNavigate={navigate}
            onOpenAuth={() => setIsAuthModalOpen(true)}
          />
        );
      case '/weekly':
        return (
          <PaperBankView
            title="Weekly Solve Sheets"
            description="কোচিং এর সাপ্তাহিক সলভ শিট — অন-ডিমান্ড লোড।"
            path="/weekly"
            defaultSourceType="weekly_solve"
            activeTrack={activeTrack}
            selectedSubject={selectedSubject}
            selectedWeek={selectedWeek}
            onSelectWeek={setSelectedWeek}
          />
        );
      case '/paper-final':
        return (
          <PaperBankView
            title="Paper Final"
            description="কোচিং এর পেপার ফাইনাল প্রশ্নব্যাংক।"
            path="/paper-final"
            defaultSourceType="paper_final"
            activeTrack={activeTrack}
            selectedSubject={selectedSubject}
          />
        );
      case '/subject-final':
        return (
          <PaperBankView
            title="Subject Final"
            description="বিষয়ভিত্তিক ফাইনাল প্রশ্নব্যাংক।"
            path="/subject-final"
            defaultSourceType="subject_final"
            activeTrack={activeTrack}
            selectedSubject={selectedSubject}
          />
        );
      case '/bank':
      case '/exam':
        return (
          <PaperBankView
            title="প্রশ্নব্যাংক (Paper Bank)"
            description="সকল Past Paper, Weekly Solve, Paper Final ও Model Test।"
            path="/bank"
            defaultSourceType="all"
            activeTrack={activeTrack}
            selectedSubject={selectedSubject}
            selectedWeek={selectedWeek}
            onSelectWeek={setSelectedWeek}
          />
        );
      case '/recall':
        return <ActiveRecallView onSelectMode={handleSelectMode} />;
      case '/flashcards':
        return (
          <LazyFlashcardsWrapper
            selectedWeek={selectedWeek}
            onSelectWeek={setSelectedWeek}
            selectedSubject={selectedSubject}
            onSelectSubject={setSelectedSubject}
            activeTrack={activeTrack}
            onSelectMode={handleSelectMode}
          />
        );
      case '/slides':
        return <LazySlidesWrapper selectedWeek={selectedWeek} selectedSubject={selectedSubject} />;
      case '/vault':
        return <LazyVaultWrapper selectedWeek={selectedWeek} selectedSubject={selectedSubject} />;
      case '/analytics':
        return (
          <AnalyticsView
            user={user}
            onOpenAuth={() => setIsAuthModalOpen(true)}
            onSelectMode={handleSelectMode}
            activeTrack={activeTrack}
          />
        );
      default:
        return <NotFoundView onGoHome={() => navigate('/')} />;
    }
  };

  return (
    <div className="min-h-screen overflow-x-hidden bg-[#F6F8F6] dark:bg-slate-950 text-slate-800 dark:text-slate-100 flex flex-col font-['Hind_Siliguri'] antialiased transition-colors duration-200">
      <Navbar
        currentMode={currentMode}
        onSelectMode={handleSelectMode}
        onNavigate={navigate}
        selectedWeek={selectedWeek}
        onSelectWeek={setSelectedWeek}
        selectedSubject={selectedSubject}
        onSelectSubject={setSelectedSubject}
        theme={theme}
        onToggleTheme={() => setTheme((p) => (p === 'dark' ? 'light' : 'dark'))}
        user={user}
        onOpenAuth={() => setIsAuthModalOpen(true)}
        onLogout={handleLogout}
        activeTrack={activeTrack}
        onSelectTrack={handleSelectTrack}
      />

      <main className="flex-1 overflow-x-hidden pb-32">
        <Suspense
          fallback={
            <div className="max-w-3xl mx-auto px-4 py-16 text-center text-sm text-slate-500">
              লোড হচ্ছে...
            </div>
          }
        >
          {renderRoute()}
        </Suspense>
      </main>

      <BottomNav currentMode={currentMode} onSelectMode={handleSelectMode} />

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
