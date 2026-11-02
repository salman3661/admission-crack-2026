import { useState } from 'react';
import { Navbar } from './components/Navbar';
import { SlidesView } from './components/SlidesView';
import { FlashcardsView } from './components/FlashcardsView';
import { ExamView } from './components/ExamView';
import { VaultView } from './components/VaultView';

import slidesData from './data/slides.json';
import flashcardsData from './data/flashcards.json';
import quizzesData from './data/quizzes.json';
import vaultData from './data/vault.json';

import type { AppMode, SubjectType, WeekFilterType, SlideItem, FlashcardItem, QuizQuestion, VaultData as VaultDataType } from './types';
import { Target, Sparkles, BookOpen, Clock } from 'lucide-react';

export function App() {
  const [currentMode, setCurrentMode] = useState<AppMode>('slides');
  const [selectedWeek, setSelectedWeek] = useState<WeekFilterType>('all');
  const [selectedSubject, setSelectedSubject] = useState<SubjectType>('All');

  const slides = slidesData as SlideItem[];
  const flashcards = flashcardsData as FlashcardItem[];
  const quizzes = quizzesData as QuizQuestion[];
  const vault = vaultData as VaultDataType;

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-['Hind_Siliguri'] antialiased">
      {/* Top Navbar */}
      <Navbar
        currentMode={currentMode}
        onSelectMode={setCurrentMode}
        selectedWeek={selectedWeek}
        onSelectWeek={setSelectedWeek}
        selectedSubject={selectedSubject}
        onSelectSubject={setSelectedSubject}
      />

      {/* Main Mode View Area */}
      <main className="flex-1 pb-16">
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

        {currentMode === 'exam' && (
          <ExamView
            quizzes={quizzes}
            selectedWeek={selectedWeek}
            selectedSubject={selectedSubject}
          />
        )}

        {currentMode === 'vault' && (
          <VaultView vault={vault} />
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-900 bg-slate-950/90 py-6 px-4 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <Target className="w-4 h-4 text-brand-400" />
            <span className="font-semibold text-slate-400">
              Admission Crack 2026 • ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট ও মেডিকেল অ্যাডমিশন
            </span>
          </div>

          <div className="flex items-center gap-4 text-[11px] text-slate-400">
            <span className="flex items-center gap-1">
              <BookOpen className="w-3.5 h-3.5 text-cyan-400" /> {slides.length} স্লাইড
            </span>
            <span className="flex items-center gap-1">
              <Sparkles className="w-3.5 h-3.5 text-amber-400" /> {flashcards.length} ফ্ল্যাশকার্ড
            </span>
            <span className="flex items-center gap-1">
              <Clock className="w-3.5 h-3.5 text-emerald-400" /> {quizzes.length} রিয়েল MCQ
            </span>
          </div>

          <div className="text-[11px] text-slate-400 font-mono">
            Zero-Config Vercel Ready
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
