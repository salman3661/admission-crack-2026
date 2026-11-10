export type TrackType = 'medical' | 'varsity';
export type SubjectType = 'All' | 'Physics' | 'Chemistry' | 'Higher Math' | 'Biology' | 'English' | 'GK';
export type WeekFilterType = 'all' | 'week_01' | 'week_02' | 'week_03' | 'week_04' | 'week_05' | 'week_06' | 'week_07' | 'week_08';
export type AppMode = 'decks' | 'exam' | 'predictor' | 'slides' | 'flashcards' | 'analytics' | 'vault' | 'recall' | 'blueprint';

export interface RecentGKCard {
  id: string;
  month: string;
  month_bn: string;
  subject: string;
  category: string;
  topic: string;
  front: string;
  back: string;
  concept: string;
  hack: string;
  trap: string;
  exam_targets: string[];
}

export interface RecentGKMonthMeta {
  id: string;
  label_bn: string;
  label_en: string;
  badge: string;
}

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
  deck_id?: string;
  deck_title?: string;
  week_id: string;
  week?: number;
  subject: string;
  chapter?: string;
  topic: string;
  type?: 'core_formula' | 'shortcut' | 'trap' | 'table' | 'macro' | string;
  front: string;
  back: string;
  formula?: string;
  concept?: string;
  hack?: string;
  trap?: string;
  headers?: string[];
  rows?: string[][];
  tags?: string[];
}


export interface QuizQuestion {
  id: string;
  week_id: string;
  week?: number | string;
  subject: string;
  chapter?: string;
  tag?: string;
  track?: TrackType;
  q: string;
  question?: string;
  opts: string[];
  options?: string[];
  ans: number;
  correct_index?: number;
  exp: string;
  explanation?: string;
  trap: string;
  trap_alert?: string;
  trap_insight?: string;
  speed_hack?: string;
  type_ref?: string;
  blueprint_type_id?: string;
  blueprint_chapter_id?: string;
  origin?: string;
  yield_stars?: number;
  probability?: string;
  intelligence_type?: string;
  source_book?: string;
  expected_count?: number | string;
  du_topic?: string;
  du_freq?: number;
  du_tier?: 'super_hot' | 'hot';
  du_badge?: string;
}

export interface PredictorWrittenProblem {
  subject: string;
  problem: string;
  marks: number;
  solution: string;
  rubric?: string;
}

export interface PredictorSet {
  id: string;
  title: string;
  track: TrackType;
  duration_minutes: number;
  total_marks: number;
  negative_marking: number;
  badge: string;
  description: string;
  syllabus_scope?: string;
  subjects: string[];
  target_mcqs: number;
  written_included?: boolean;
  written_problems?: PredictorWrittenProblem[];
  questions?: QuizQuestion[];
  question_ids?: string[];
  week?: number | string;
  week_id?: string;
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

export type VaultCardType = 'core_formula' | 'shortcut' | 'trap' | 'table' | 'speed_hack' | 'concept_trap';

export interface VaultTableData {
  headers: string[];
  rows: string[][];
}

export interface VaultEntry {
  id: string;
  week?: number;
  subject: string;
  chapter: string;
  type: VaultCardType;
  title: string;
  formula: string;
  concept: string;
  hack?: string;
  trap?: string;
  tags?: string[];
  headers?: string[];
  rows?: string[][];
  table?: VaultTableData;
}

export interface VaultData {
  entries?: VaultEntry[];
  triplets?: TripletItem[];
  quick_math?: QuickMathItem[];
  magic_fractions?: MagicFractionItem[];
  patterns?: FormulaPatternItem[];
  traps?: TrapItem[];
}


export interface MasterMegaType {
  type_id: string;
  name: string;
  importance: string;
  stars: string;
  repeat_frequency: number;
  past_tags: string[];
  qb_question_refs: string[];
  core_rule: string;
  speed_elimination: string;
}

export interface DUHotspotSubTopic {
  topic: string;
  freq: number;
  tier: 'super_hot' | 'hot';
}

export interface DUHotspotMeta {
  has_hotspot: boolean;
  tier: 'super_hot' | 'hot';
  topic: string;
  freq: number;
  badge_text: string;
  sub_topics?: DUHotspotSubTopic[];
}

export interface MasterChapterBlueprint {
  id: string;
  title: string;
  subject: string;
  paper: string;
  chapter_no?: string;
  subtitle?: string;
  syllabus?: string;
  aliases?: string[];
  total_questions: number;
  dominant_types_count: number;
  mega_types: MasterMegaType[];
  du_hotspot?: DUHotspotMeta;
}

export interface SyntheticPredictorQuestion {
  id: string;
  stem: string;
  options: string[];
  answer: string;
  type_ref: string;
  trap_alert: string;
  speed_hack: string;
  explanation: string;
  source?: string;
  source_tag?: string;
  du_topic?: string;
  du_freq?: number;
  du_tier?: 'super_hot' | 'hot';
  du_badge?: string;
}

export interface ChapterSyntheticPredictors {
  chapter_id: string;
  chapter_title: string;
  subject: string;
  paper?: string;
  chapter_no?: string;
  du_hotspot?: DUHotspotMeta;
  predictors: SyntheticPredictorQuestion[];
}
