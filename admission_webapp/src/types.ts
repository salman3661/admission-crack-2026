export type SubjectType = 'All' | 'Physics' | 'Chemistry' | 'Higher Math' | 'Biology';
export type WeekFilterType = 'all' | 'week_01' | 'week_02' | 'week_03';
export type AppMode = 'decks' | 'exam' | 'slides' | 'flashcards' | 'analytics' | 'vault';

export interface UserProfile {
  name: string;
  email: string;
  avatar: string;
  target: string;
  streakDays: number;
  solvedCount: number;
  accuracy: number;
  isLoggedIn: boolean;
}

export interface WeekMeta {
  id: string;
  name: string;
  badge: string;
  description: string;
  subjects: string[];
  total_mcqs: number;
  total_slides: number;
  total_flashcards: number;
}

export interface SlideItem {
  id: string;
  week_id: string;
  subject: string;
  title: string;
  formula_matrix: string;
  hand_hacks: string;
  student_traps: string;
  exam_capsule: string;
}

export interface FlashcardItem {
  id: string;
  week_id: string;
  subject: string;
  topic: string;
  front: string;
  back: string;
}

export interface QuizQuestion {
  id: string;
  week_id: string;
  subject: string;
  q: string;
  opts: string[];
  ans: number;
  exp: string;
  trap: string;
}

export interface TripletItem {
  sides: string;
  result: string;
  app: string;
}

export interface QuickMathItem {
  type: string;
  item: string;
}

export interface MagicFractionItem {
  compound: string;
  mw: string;
  trick: string;
}

export interface FormulaPatternItem {
  code: string;
  week: string;
  subject: string;
  title: string;
  formula: string;
}

export interface TrapItem {
  id: number;
  week: string;
  subject: string;
  trap: string;
  fix: string;
}

export interface VaultData {
  triplets: TripletItem[];
  quick_math: QuickMathItem[];
  magic_fractions: MagicFractionItem[];
  patterns: FormulaPatternItem[];
  traps: TrapItem[];
}
