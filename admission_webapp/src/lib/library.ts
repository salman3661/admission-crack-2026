import indexData from '../data/index.json';

export type SourceType = 'past_paper' | 'weekly_solve' | 'paper_final' | 'subject_final' | 'model_test';
export type ExamSlug = 'du_ka' | 'mat' | 'ru' | 'ju' | 'cu' | 'gst' | 'eng_bridge' | 'other';
export type CanonicalSubject =
  | 'Physics'
  | 'Chemistry'
  | 'Higher Math'
  | 'Biology'
  | 'English'
  | 'Bangla'
  | 'ICT'
  | 'GK';

export interface Question {
  id: string;
  source_type: SourceType;
  source_name: string;
  exam: ExamSlug;
  exam_year: number | null;
  exam_date?: string | null;
  week?: number | null;
  subject: CanonicalSubject;
  chapter_id: string;
  chapter_name: string;
  mega_type?: string | null;
  question: string;
  options: string[];
  correct_index: number | null;
  explanation: string;
  trap: string;
  is_written: boolean;
  marks: number;
  duration_sec: number;
  probability_label?: string;
  appears_in?: string[];
  // Enriched master-set metadata
  likelihood_pct?: number;
  expected_mcq_in_paper?: number;
  years_hit?: number;
  papers_hit?: number;
  source_weight?: number;
}

export interface PaperIndexEntry {
  path: string;
  count: number;
  mcqs: number;
  written: number;
  exams: string[];
  subjects: string[];
  source_types: string[];
  weeks?: number[];
}

export interface ChapterIndexEntry {
  chapter_id: string;
  chapter_name: string;
  subject: string;
  count: number;
  years_hit: number;
  papers_hit: number;
  exams: string[];
  predicted_pct: number;
  expected_mcq_du_ka: number;
  expected_mcq_mat: number;
}

export interface MegaTypeIndexEntry {
  count: number;
  years_hit: number;
  chapter: string;
  chapter_id: string;
  subject: string;
}

export interface BankIndex {
  generated_at: string;
  total_questions: number;
  total_mcqs: number;
  total_written: number;
  by_exam: Record<string, number>;
  by_subject: Record<string, number>;
  by_source_type: Record<string, number>;
  by_week: Record<string, number>;
  by_mega_type?: Record<string, MegaTypeIndexEntry>;
  master_sets: Record<string, number>;
  papers: PaperIndexEntry[];
  chapters: ChapterIndexEntry[];
}

export const BANK_INDEX: BankIndex = indexData as BankIndex;

// Lazy glob loaders — Vite splits every JSON into its own on-demand chunk!
const bankModules = import.meta.glob('../data/bank/**/*.json');
const masterModules = import.meta.glob('../data/master/*.json');

const paperCache = new Map<string, Question[]>();
const masterCache = new Map<string, Question[]>();
let allBankCache: Question[] | null = null;

const SUBJECT_MAP: Record<string, CanonicalSubject> = {
  physics: 'Physics',
  chemistry: 'Chemistry',
  'higher math': 'Higher Math',
  math: 'Higher Math',
  mathematics: 'Higher Math',
  biology: 'Biology',
  english: 'English',
  bangla: 'Bangla',
  ict: 'ICT',
  gk: 'GK',
  'general knowledge': 'GK',
};

const EXAM_MAP: Record<string, ExamSlug> = {
  du_ka: 'du_ka',
  varsity: 'du_ka',
  mat: 'mat',
  medical: 'mat',
  ru: 'ru',
  ju: 'ju',
  cu: 'cu',
  gst: 'gst',
  eng_bridge: 'eng_bridge',
  other: 'other',
};

export function normalizeSubject(raw?: string): CanonicalSubject {
  const key = String(raw || '').trim().toLowerCase();
  return SUBJECT_MAP[key] || 'Physics';
}

export function normalizeExam(raw?: string): ExamSlug {
  const key = String(raw || '').trim().toLowerCase();
  return EXAM_MAP[key] || 'other';
}

// A1: Authoritative week extractor (id-prefix first, source_name fallback)
export function questionWeek(q: Partial<Question>): number | null {
  if (typeof q.week === 'number' && q.week >= 1 && q.week <= 9) return q.week;
  const m = /^w(\d)(?:_|\b)/i.exec(String(q.id || ''));
  if (m) return parseInt(m[1], 10);
  const s = /(?:^|[\s\-/])(?:week(?:ly)?[\s\-]*0?(\d)|w[\-\s]?0?(\d)|[\w]0(\d)\b)/i.exec(String(q.source_name || ''));
  if (s) {
    const n = parseInt(s[1] || s[2] || s[3], 10);
    if (n >= 1 && n <= 9) return n;
  }
  return null;
}

export function normalize(rows: Partial<Question>[]): Question[] {
  return rows.map((r, idx) => {
    const options = Array.isArray(r.options) ? r.options.filter((o) => String(o).trim().length > 0) : [];
    const isWritten = Boolean(r.is_written) || options.length === 0;
    const correctIndex = isWritten
      ? null
      : typeof r.correct_index === 'number' && r.correct_index >= 0 && r.correct_index < options.length
        ? r.correct_index
        : 0;

    return {
      id: String(r.id || `q_${idx}`),
      source_type: (r.source_type as SourceType) || 'past_paper',
      source_name: String(r.source_name || 'Unknown Paper'),
      exam: normalizeExam(r.exam),
      exam_year: typeof r.exam_year === 'number' ? r.exam_year : null,
      exam_date: r.exam_date ?? null,
      week: questionWeek(r),
      subject: normalizeSubject(r.subject),
      chapter_id: String(r.chapter_id || 'unclassified').trim().toLowerCase(),
      chapter_name: String(r.chapter_name || r.chapter_id || 'অনির্ধারিত'),
      mega_type: r.mega_type ?? null,
      question: String(r.question || ''),
      options,
      correct_index: correctIndex,
      explanation: String(r.explanation || ''),
      trap: String(r.trap || ''),
      is_written: isWritten,
      marks: typeof r.marks === 'number' ? r.marks : isWritten ? 3 : 1,
      duration_sec: typeof r.duration_sec === 'number' ? r.duration_sec : isWritten ? 240 : 45,
      probability_label: r.probability_label,
      appears_in: Array.isArray(r.appears_in) ? r.appears_in : undefined,
      likelihood_pct: r.likelihood_pct,
      expected_mcq_in_paper: r.expected_mcq_in_paper,
      years_hit: r.years_hit,
      papers_hit: r.papers_hit,
      source_weight: r.source_weight,
    };
  });
}

export function dedupe(rows: Question[]): Question[] {
  const byId = new Map<string, Question>();
  const byText = new Map<string, Question>();

  for (const row of rows) {
    if (byId.has(row.id)) {
      const existing = byId.get(row.id)!;
      const merged = new Set([...(existing.appears_in || [existing.source_name]), ...(row.appears_in || [row.source_name])]);
      existing.appears_in = [...merged];
      continue;
    }

    const textKey = row.question.replace(/\s+/g, ' ').trim().toLowerCase().slice(0, 140);
    if (textKey.length > 0 && byText.has(textKey)) {
      const existing = byText.get(textKey)!;
      const merged = new Set([...(existing.appears_in || [existing.source_name]), ...(row.appears_in || [row.source_name])]);
      existing.appears_in = [...merged];
      continue;
    }

    const copy = { ...row };
    byId.set(copy.id, copy);
    if (textKey.length > 0) {
      byText.set(textKey, copy);
    }
  }

  return [...byId.values()];
}

export async function loadPaper(paperPath: string): Promise<Question[]> {
  if (paperCache.has(paperPath)) return paperCache.get(paperPath)!;

  const globKey = `../data/${paperPath.replace(/^\/+/, '')}`;
  const loader = bankModules[globKey];
  if (!loader) {
    console.warn(`[library] Paper not found: ${globKey}`);
    return [];
  }

  const mod = (await loader()) as { default?: Partial<Question>[] } | Partial<Question>[];
  const raw = Array.isArray(mod) ? mod : mod.default || [];
  const processed = dedupe(normalize(raw));
  paperCache.set(paperPath, processed);
  return processed;
}

export async function loadMasterSet(exam: 'du_ka' | 'mat', set: 'set_a' | 'set_b' | 'set_c'): Promise<Question[]> {
  const key = `${exam}_${set}`;
  if (masterCache.has(key)) return masterCache.get(key)!;

  const globKey = `../data/master/${key}.json`;
  const loader = masterModules[globKey];
  if (!loader) {
    console.warn(`[library] Master set not found: ${globKey}`);
    return [];
  }

  const mod = (await loader()) as { default?: Partial<Question>[] } | Partial<Question>[];
  const raw = Array.isArray(mod) ? mod : mod.default || [];
  const processed = dedupe(normalize(raw));
  masterCache.set(key, processed);
  return processed;
}

export async function loadAllBankQuestions(): Promise<Question[]> {
  if (allBankCache) return allBankCache;
  const chunks = await Promise.all(BANK_INDEX.papers.map((p) => loadPaper(p.path)));
  const userAdded = getUserAddedQuestions();
  allBankCache = dedupe([...chunks.flat(), ...userAdded]);
  return allBankCache;
}

export async function loadPapersByFilter(opts: {
  exam?: string;
  sourceType?: SourceType | 'all';
  subject?: string;
  chapterId?: string;
  megaType?: string;
  week?: string;
  questionIds?: string[];
}): Promise<Question[]> {
  if (opts.questionIds && opts.questionIds.length > 0) {
    const allQ = await loadAllBankQuestions();
    const idSet = new Set(opts.questionIds);
    return allQ.filter((q) => idSet.has(q.id));
  }

  const targetWeekNum =
    opts.week && opts.week !== 'all' ? parseInt(opts.week.replace('week_', ''), 10) : null;

  const matchingPapers = BANK_INDEX.papers.filter((p) => {
    // When filtering by a specific week, include all papers that contain that week
    if (targetWeekNum) {
      if (Array.isArray(p.weeks) && p.weeks.length > 0 && !p.weeks.includes(targetWeekNum)) {
        return false;
      }
    } else if (opts.exam && opts.exam !== 'all') {
      if (!p.exams.includes(opts.exam)) return false;
    }
    if (opts.sourceType && opts.sourceType !== 'all' && !p.source_types.includes(opts.sourceType)) {
      return false;
    }
    if (opts.subject && opts.subject !== 'All' && !p.subjects.includes(opts.subject)) {
      return false;
    }
    return true;
  });

  const chunks = await Promise.all(matchingPapers.map((p) => loadPaper(p.path)));
  let all = dedupe(chunks.flat());

  if (opts.exam && opts.exam !== 'all') {
    all = all.filter((q) => q.exam === opts.exam);
  }
  if (opts.sourceType && opts.sourceType !== 'all') {
    all = all.filter((q) => q.source_type === opts.sourceType);
  }
  if (opts.subject && opts.subject !== 'All') {
    all = all.filter((q) => q.subject === opts.subject);
  }
  if (opts.chapterId) {
    all = all.filter((q) => q.chapter_id === opts.chapterId);
  }
  if (opts.megaType) {
    all = all.filter((q) => String(q.mega_type || '').trim() === opts.megaType);
  }
  if (targetWeekNum) {
    all = all.filter((q) => questionWeek(q) === targetWeekNum);
  }
  return all;
}

export function buildIndex(rows: Question[]) {
  const bySubject: Record<string, Question[]> = {};
  const byChapter: Record<string, Question[]> = {};
  const byExam: Record<string, Question[]> = {};
  const bySourceType: Record<string, Question[]> = {};

  for (const r of rows) {
    (bySubject[r.subject] ||= []).push(r);
    (byChapter[r.chapter_id] ||= []).push(r);
    (byExam[r.exam] ||= []).push(r);
    (bySourceType[r.source_type] ||= []).push(r);
  }
  return { bySubject, byChapter, byExam, bySourceType };
}

export function countBy<T extends Record<string, unknown>>(rows: T[], key: keyof T): Record<string, number> {
  const out: Record<string, number> = {};
  for (const r of rows) {
    const k = String(r[key] ?? 'unknown');
    out[k] = (out[k] || 0) + 1;
  }
  return out;
}

// ── SESSION-STABLE OPTION SHUFFLE (Rule 8) ──
const SHUFFLE_STORAGE_KEY = 'ac_shuffle_map_v1';

interface ShuffleRecord {
  order: number[]; // order[newIdx] = origIdx
}

function loadShuffleMap(): Record<string, ShuffleRecord> {
  try {
    const raw = sessionStorage.getItem(SHUFFLE_STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

function saveShuffleMap(map: Record<string, ShuffleRecord>) {
  try {
    sessionStorage.setItem(SHUFFLE_STORAGE_KEY, JSON.stringify(map));
  } catch {
    // ignore quota errors
  }
}

function seededPermutation(len: number, seedStr: string): number[] {
  let h = 2166136261;
  for (let i = 0; i < seedStr.length; i++) {
    h ^= seedStr.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  const arr = Array.from({ length: len }, (_, i) => i);
  for (let i = len - 1; i > 0; i--) {
    h ^= h << 13;
    h ^= h >>> 17;
    h ^= h << 5;
    const j = Math.abs(h) % (i + 1);
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export interface ShuffledQuestion {
  options: string[];
  correctIndex: number | null;
  order: number[]; // maps shuffledIdx -> originalIdx
}

export function getShuffledOptions(q: Question): ShuffledQuestion {
  if (q.is_written || q.options.length === 0) {
    return { options: [], correctIndex: null, order: [] };
  }

  const map = loadShuffleMap();
  let rec = map[q.id];
  if (!rec || rec.order.length !== q.options.length) {
    const sessionSalt = sessionStorage.getItem('ac_session_salt') || (() => {
      const s = String(Date.now());
      sessionStorage.setItem('ac_session_salt', s);
      return s;
    })();
    rec = { order: seededPermutation(q.options.length, `${q.id}::${sessionSalt}`) };
    map[q.id] = rec;
    saveShuffleMap(map);
  }

  const options = rec.order.map((origIdx) => q.options[origIdx]);
  const correctIndex =
    q.correct_index !== null ? rec.order.indexOf(q.correct_index) : null;

  return { options, correctIndex, order: rec.order };
}

// ── F5: ERROR LOG + MISTAKE BOOK (SM-2) ──
const ERROR_LOG_KEY = 'ac_error_log';
const SM2_INTERVALS = [1, 3, 7, 14]; // days

export interface ErrorLogEntry {
  qid: string;
  question: string;
  options: string[];
  correct_index: number | null;
  explanation: string;
  trap: string;
  myAnswer: number | string | null;
  correct: number | string | null;
  whyWrong: string;
  chapter_id: string;
  chapter: string;
  subject: string;
  source_type: string;
  source_name: string;
  madeAt: string;
  retestDue: string;
  intervalStep: number;
}

export function getErrorLog(): ErrorLogEntry[] {
  try {
    const raw = localStorage.getItem(ERROR_LOG_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function saveErrorLog(entries: ErrorLogEntry[]) {
  try {
    localStorage.setItem(ERROR_LOG_KEY, JSON.stringify(entries));
  } catch {
    // ignore
  }
}

export function addErrorLogEntry(q: Question, myAnswer: number | string | null, whyWrong = ''): ErrorLogEntry[] {
  const list = getErrorLog();
  const now = new Date();
  const due = new Date(now.getTime() + SM2_INTERVALS[0] * 86400000);
  const idx = list.findIndex((e) => e.qid === q.id);
  const entry: ErrorLogEntry = {
    qid: q.id,
    question: q.question,
    options: q.options,
    correct_index: q.correct_index,
    explanation: q.explanation,
    trap: q.trap,
    myAnswer,
    correct: q.correct_index,
    whyWrong: whyWrong || (idx >= 0 ? list[idx].whyWrong : ''),
    chapter_id: q.chapter_id,
    chapter: q.chapter_name,
    subject: q.subject,
    source_type: q.source_type,
    source_name: q.source_name,
    madeAt: now.toISOString(),
    retestDue: due.toISOString(),
    intervalStep: 0,
  };
  if (idx >= 0) list[idx] = entry;
  else list.unshift(entry);
  saveErrorLog(list);
  return list;
}

export function reviewMistakeEntry(qid: string, wasCorrect: boolean, whyWrong?: string): ErrorLogEntry[] {
  const list = getErrorLog();
  const idx = list.findIndex((e) => e.qid === qid);
  if (idx < 0) return list;
  const item = { ...list[idx] };
  if (whyWrong !== undefined) item.whyWrong = whyWrong;
  if (wasCorrect) {
    const nextStep = Math.min(item.intervalStep + 1, SM2_INTERVALS.length - 1);
    item.intervalStep = nextStep;
    item.retestDue = new Date(Date.now() + SM2_INTERVALS[nextStep] * 86400000).toISOString();
  } else {
    item.intervalStep = 0;
    item.retestDue = new Date(Date.now() + SM2_INTERVALS[0] * 86400000).toISOString();
  }
  list[idx] = item;
  saveErrorLog(list);
  return list;
}

export function removeErrorLogEntry(qid: string): ErrorLogEntry[] {
  const list = getErrorLog().filter((e) => e.qid !== qid);
  saveErrorLog(list);
  return list;
}

// ── F6: WEAKNESS RADAR STATS ──
const ATTEMPT_STATS_KEY = 'ac_attempt_stats_v1';

export interface ChapterStat {
  chapter_id: string;
  chapter_name: string;
  subject: string;
  attempted: number;
  correct: number;
  marksLost: number;
  week?: number | null;
}

export function getAttemptStats(): Record<string, ChapterStat> {
  try {
    const raw = localStorage.getItem(ATTEMPT_STATS_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function recordAttemptStat(q: Question, isCorrect: boolean, negativePenalty = 0.25) {
  const stats = getAttemptStats();
  const key = `${q.subject}||${q.chapter_id}`;
  const cur = stats[key] || {
    chapter_id: q.chapter_id,
    chapter_name: q.chapter_name,
    subject: q.subject,
    attempted: 0,
    correct: 0,
    marksLost: 0,
    week: questionWeek(q),
  };
  cur.attempted += 1;
  if (isCorrect) {
    cur.correct += 1;
  } else {
    cur.marksLost = +(cur.marksLost + (q.is_written ? q.marks : 1 + negativePenalty)).toFixed(2);
  }
  stats[key] = cur;
  try {
    localStorage.setItem(ATTEMPT_STATS_KEY, JSON.stringify(stats));
    // Also record per-question solved ID for progress bar
    const solvedRaw = localStorage.getItem('ac_solved_qids_v1');
    const solved: Record<string, { correct: boolean; week: number | null; ts: number }> = solvedRaw
      ? JSON.parse(solvedRaw)
      : {};
    solved[q.id] = { correct: isCorrect, week: questionWeek(q), ts: Date.now() };
    localStorage.setItem('ac_solved_qids_v1', JSON.stringify(solved));
  } catch {
    // ignore
  }
}

export function getSolvedQuestionsMap(): Record<string, { correct: boolean; week: number | null; ts: number }> {
  try {
    const raw = localStorage.getItem('ac_solved_qids_v1');
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

// ── F7: MOCK TRACKER ──
const MOCK_TRACKER_KEY = 'ac_mock_tracker_v1';

export interface MockTrackerEntry {
  id: string;
  date: string;
  name: string;
  exam: 'du_ka' | 'mat';
  Physics_MCQ: number;
  Physics_Written: number;
  Chem_MCQ: number;
  Chem_Written: number;
  Math_MCQ: number;
  Math_Written: number;
  Bio_MCQ: number;
  Bio_Written: number;
  MCQ_total: number;
  Written_total: number;
  GRAND_TOTAL: number;
  accuracy_pct: number;
  time_MCQ_used: number;
  time_written_used: number;
  written_blank_count: number;
  top3_lossy_chapter: string;
  next48h_fix: string;
}

export function getMockTracker(): MockTrackerEntry[] {
  try {
    const raw = localStorage.getItem(MOCK_TRACKER_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function saveMockTrackerEntry(entry: MockTrackerEntry): MockTrackerEntry[] {
  const list = getMockTracker();
  const idx = list.findIndex((e) => e.id === entry.id);
  if (idx >= 0) list[idx] = entry;
  else list.unshift(entry);
  try {
    localStorage.setItem(MOCK_TRACKER_KEY, JSON.stringify(list));
  } catch {
    // ignore
  }
  return list;
}

export function deleteMockTrackerEntry(id: string): MockTrackerEntry[] {
  const list = getMockTracker().filter((e) => e.id !== id);
  try {
    localStorage.setItem(MOCK_TRACKER_KEY, JSON.stringify(list));
  } catch {
    // ignore
  }
  return list;
}

// ── F19: BOOKMARKS ──
const BOOKMARKS_KEY = 'ac_bookmarks_v1';

export interface Bookmark {
  questionId: string;
  createdAt: number;
  source: 'drill' | 'master_set' | 'bank' | 'simulator' | 'matcher' | 'formula';
  setId?: string;
  exam: 'du_ka' | 'mat';
  subject: string;
  chapter: string;
  chapter_id?: string;
  question: string;
  options: string[];
  correct_index: number | null;
  explanation: string;
  trap: string;
  is_written: boolean;
  source_name: string;
  exam_year: number | null;
  mega_type?: string | null;
  note?: string;
  tags: string[];
}

export function getBookmarks(): Bookmark[] {
  try {
    const raw = localStorage.getItem(BOOKMARKS_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function saveBookmarks(list: Bookmark[]) {
  try {
    localStorage.setItem(BOOKMARKS_KEY, JSON.stringify(list));
  } catch {
    // ignore
  }
}

export function isBookmarked(questionId: string): boolean {
  return getBookmarks().some((b) => b.questionId === questionId);
}

export function toggleBookmark(
  q: Question,
  source: Bookmark['source'] = 'drill',
  setId?: string
): { bookmarks: Bookmark[]; added: boolean } {
  const list = getBookmarks();
  const idx = list.findIndex((b) => b.questionId === q.id);
  if (idx >= 0) {
    const next = list.filter((b) => b.questionId !== q.id);
    saveBookmarks(next);
    return { bookmarks: next, added: false };
  }
  const item: Bookmark = {
    questionId: q.id,
    createdAt: Date.now(),
    source,
    setId,
    exam: q.exam === 'mat' ? 'mat' : 'du_ka',
    subject: q.subject,
    chapter: q.chapter_name,
    chapter_id: q.chapter_id,
    question: q.question,
    options: q.options,
    correct_index: q.correct_index,
    explanation: q.explanation,
    trap: q.trap,
    is_written: q.is_written,
    source_name: q.source_name,
    exam_year: q.exam_year,
    mega_type: q.mega_type,
    note: '',
    tags: [],
  };
  const next = [item, ...list];
  saveBookmarks(next);
  return { bookmarks: next, added: true };
}

export function updateBookmarkMeta(
  questionId: string,
  patch: { note?: string; tags?: string[] }
): Bookmark[] {
  const list = getBookmarks().map((b) =>
    b.questionId === questionId ? { ...b, ...patch } : b
  );
  saveBookmarks(list);
  return list;
}

export function removeBookmark(questionId: string): Bookmark[] {
  const next = getBookmarks().filter((b) => b.questionId !== questionId);
  saveBookmarks(next);
  return next;
}

export function bookmarkToQuestion(b: Bookmark): Question {
  return {
    id: b.questionId,
    source_type: 'past_paper',
    source_name: b.source_name || 'Bookmark',
    exam: b.exam,
    exam_year: b.exam_year ?? null,
    subject: normalizeSubject(b.subject),
    chapter_id: b.chapter_id || 'unclassified',
    chapter_name: b.chapter || 'অনির্ধারিত',
    mega_type: b.mega_type ?? null,
    question: b.question,
    options: b.options || [],
    correct_index: b.correct_index,
    explanation: b.explanation || '',
    trap: b.trap || '',
    is_written: Boolean(b.is_written) || (b.options || []).length === 0,
    marks: b.is_written ? 5 : 1,
    duration_sec: b.is_written ? 240 : 45,
  };
}

// ── F17: USER-ADDED QUESTIONS (from Practice-Question Matcher) ──
const USER_QUESTIONS_KEY = 'ac_user_added_questions_v1';

export function getUserAddedQuestions(): Question[] {
  try {
    const raw = localStorage.getItem(USER_QUESTIONS_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function addUserQuestion(q: Question): Question[] {
  const list = getUserAddedQuestions();
  const next = [q, ...list.filter((x) => x.id !== q.id)];
  try {
    localStorage.setItem(USER_QUESTIONS_KEY, JSON.stringify(next));
    allBankCache = null;
  } catch {
    // ignore
  }
  return next;
}

// ── F18: SYNC ADAPTER INTERFACE (Local-first, honest status) ──
export interface SyncState {
  updatedAt: number;
  targetExam: 'du_ka' | 'mat';
  targetScore: number;
  bookmarks: Bookmark[];
  errorLog: ErrorLogEntry[];
  attemptStats: Record<string, ChapterStat>;
  mockTracker: MockTrackerEntry[];
  userAddedQuestions: Question[];
}

export interface SyncAdapter {
  id: string;
  labelBn: string;
  get(): Promise<SyncState>;
  put(state: SyncState): Promise<void>;
  user(): { id: string; name: string } | null;
}

export const LocalStorageAdapter: SyncAdapter = {
  id: 'local',
  labelBn: 'স্থানীয় (এই ডিভাইসে)',
  async get(): Promise<SyncState> {
    const targetExam = localStorage.getItem('admission_track') === 'medical' ? 'mat' : 'du_ka';
    const targetScore = Number(localStorage.getItem('ac_target_score_v1') || 80);
    const updatedAt = Number(localStorage.getItem('ac_last_sync_ts') || Date.now());
    return {
      updatedAt,
      targetExam,
      targetScore,
      bookmarks: getBookmarks(),
      errorLog: getErrorLog(),
      attemptStats: getAttemptStats(),
      mockTracker: getMockTracker(),
      userAddedQuestions: getUserAddedQuestions(),
    };
  },
  async put(state: SyncState): Promise<void> {
    const now = Date.now();
    localStorage.setItem('ac_last_sync_ts', String(now));
    localStorage.setItem('admission_track', state.targetExam === 'mat' ? 'medical' : 'varsity');
    localStorage.setItem('ac_target_score_v1', String(state.targetScore || 80));
    saveBookmarks(state.bookmarks || []);
    saveErrorLog(state.errorLog || []);
    localStorage.setItem(ATTEMPT_STATS_KEY, JSON.stringify(state.attemptStats || {}));
    localStorage.setItem(MOCK_TRACKER_KEY, JSON.stringify(state.mockTracker || []));
    localStorage.setItem(USER_QUESTIONS_KEY, JSON.stringify(state.userAddedQuestions || []));
  },
  user() {
    try {
      const raw = localStorage.getItem('admission_user');
      if (!raw) return null;
      const u = JSON.parse(raw);
      return u?.name ? { id: u.email || 'local', name: u.name } : null;
    } catch {
      return null;
    }
  },
};

export const adapters: Record<string, SyncAdapter> = {
  local: LocalStorageAdapter,
};

export function resetAllLocalProgress() {
  const keys = [
    BOOKMARKS_KEY,
    ERROR_LOG_KEY,
    ATTEMPT_STATS_KEY,
    MOCK_TRACKER_KEY,
    USER_QUESTIONS_KEY,
    'ac_solved_qids_v1',
    'ac_written_drafts_v1',
    'ac_last_sync_ts',
  ];
  keys.forEach((k) => localStorage.removeItem(k));
  allBankCache = null;
}

let extendedBankCache: Array<Question & { __isPredictor?: boolean; __rawChapter?: string }> | null = null;

function mapLegacyToQuestion(
  raw: Record<string, unknown>,
  idx: number,
  opts: { defaultExam?: ExamSlug; defaultSourceType?: SourceType; sourceName?: string; isPredictor?: boolean }
): Question & { __isPredictor?: boolean; __rawChapter?: string } {
  const questionText = String(raw.question || raw.q || '');
  const rawOpts = Array.isArray(raw.options) ? raw.options : Array.isArray(raw.opts) ? raw.opts : [];
  const options = rawOpts.map((o) => String(o)).filter((o) => o.trim().length > 0);
  const isWritten = Boolean(raw.is_written) || options.length === 0;
  const rawAns = typeof raw.correct_index === 'number' ? raw.correct_index : typeof raw.ans === 'number' ? raw.ans : 0;
  const correctIndex = isWritten ? null : rawAns >= 0 && rawAns < options.length ? rawAns : 0;

  const trackStr = String(raw.track || raw.bank_type || '').toLowerCase();
  const inferredExam: ExamSlug =
    raw.exam ? normalizeExam(String(raw.exam)) : trackStr.includes('medical') || trackStr === 'mat' ? 'mat' : opts.defaultExam || 'du_ka';

  const rawChapter = String(raw.chapter_name || raw.chapter || raw.chapter_id || '');
  const id = String(raw.id || `ext_${idx}`);
  const isPred =
    Boolean(opts.isPredictor) ||
    id.startsWith('pred_') ||
    (typeof raw.years_hit === 'number' && raw.years_hit >= 2) ||
    (typeof raw.likelihood_pct === 'number' && raw.likelihood_pct > 0) ||
    (typeof raw.yield_stars === 'number' && raw.yield_stars >= 4) ||
    Boolean(raw.probability);

  return {
    id,
    source_type: (raw.source_type as SourceType) || opts.defaultSourceType || 'past_paper',
    source_name: String(raw.source_name || raw.origin || opts.sourceName || 'Question Bank'),
    exam: inferredExam,
    exam_year: typeof raw.exam_year === 'number' ? raw.exam_year : null,
    exam_date: (raw.exam_date as string | null | undefined) ?? null,
    week: questionWeek(raw as Partial<Question>),
    subject: normalizeSubject(typeof raw.subject === 'string' ? raw.subject : String(raw.subject || '')),
    chapter_id: String(raw.chapter_id || raw.blueprint_chapter_id || 'unclassified').trim().toLowerCase(),
    chapter_name: rawChapter || 'অনির্ধারিত',
    mega_type: (raw.mega_type as string | null | undefined) ?? (raw.type_ref as string | null | undefined) ?? null,
    question: questionText,
    options,
    correct_index: correctIndex,
    explanation: String(raw.explanation || raw.exp || ''),
    trap: String(raw.trap || raw.trap_alert || raw.trap_insight || ''),
    is_written: isWritten,
    marks: typeof raw.marks === 'number' ? raw.marks : isWritten ? 2.5 : 1,
    duration_sec: typeof raw.duration_sec === 'number' ? raw.duration_sec : isWritten ? 240 : 45,
    probability_label: (raw.probability_label as string | undefined) || (raw.probability as string | undefined),
    appears_in: Array.isArray(raw.appears_in) ? (raw.appears_in as string[]) : undefined,
    likelihood_pct: typeof raw.likelihood_pct === 'number' ? raw.likelihood_pct : undefined,
    expected_mcq_in_paper: typeof raw.expected_mcq_in_paper === 'number' ? raw.expected_mcq_in_paper : undefined,
    years_hit: typeof raw.years_hit === 'number' ? raw.years_hit : undefined,
    papers_hit: typeof raw.papers_hit === 'number' ? raw.papers_hit : undefined,
    source_weight: typeof raw.source_weight === 'number' ? raw.source_weight : undefined,
    __isPredictor: isPred,
    __rawChapter: rawChapter,
  };
}

async function loadExtendedBankPool(): Promise<Array<Question & { __isPredictor?: boolean; __rawChapter?: string }>> {
  if (extendedBankCache) return extendedBankCache;

  const collected: Array<Question & { __isPredictor?: boolean; __rawChapter?: string }> = [];

  const [pfMod, sfMod, fmMod, vbMod, mbMod, ...masterMods] = await Promise.all([
    import('../data/paper_final_bank.json').catch(() => null),
    import('../data/subject_final_bank.json').catch(() => null),
    import('../data/full_mock_bank.json').catch(() => null),
    import('../data/varsity_bank.json').catch(() => null),
    import('../data/medical_bank.json').catch(() => null),
    ...Object.entries(masterModules).map(async ([k, loader]) => ({ key: k, mod: await loader().catch(() => null) })),
  ]);

  const pushTestContainer = (mod: unknown, sourceType: SourceType, isPredictor: boolean) => {
    const data = (mod as { default?: { tests?: unknown[]; exams?: unknown[] } } | null)?.default || (mod as { tests?: unknown[]; exams?: unknown[] } | null);
    const list = (data?.tests || data?.exams || []) as Array<{
      track?: string;
      title?: string;
      mcqs?: Record<string, unknown>[];
      written_questions?: Record<string, unknown>[];
    }>;
    for (const t of list) {
      const defaultExam: ExamSlug = String(t.track || '').toLowerCase() === 'medical' ? 'mat' : 'du_ka';
      for (const m of t.mcqs || []) {
        collected.push(mapLegacyToQuestion(m, collected.length, { defaultExam, defaultSourceType: sourceType, sourceName: t.title, isPredictor }));
      }
      for (const w of t.written_questions || []) {
        collected.push(mapLegacyToQuestion({ ...w, is_written: true }, collected.length, { defaultExam, defaultSourceType: sourceType, sourceName: t.title, isPredictor }));
      }
    }
  };

  pushTestContainer(pfMod, 'paper_final', true);
  pushTestContainer(sfMod, 'subject_final', true);
  pushTestContainer(fmMod, 'model_test', true);

  const pushArray = (mod: unknown, defaultExam: ExamSlug, isPredictor: boolean, sourceName: string) => {
    const raw = (mod as { default?: Record<string, unknown>[] } | null)?.default || (mod as Record<string, unknown>[] | null);
    if (!Array.isArray(raw)) return;
    raw.forEach((item, idx) => {
      collected.push(mapLegacyToQuestion(item, idx, { defaultExam, defaultSourceType: 'past_paper', sourceName, isPredictor }));
    });
  };

  pushArray(vbMod, 'du_ka', false, 'Varsity Bank');
  pushArray(mbMod, 'mat', false, 'Medical Bank');

  for (const entry of masterMods) {
    const isMat = entry.key.includes('mat_');
    pushArray(entry.mod, isMat ? 'mat' : 'du_ka', true, 'Master Predictor Set');
  }

  extendedBankCache = collected;
  return collected;
}

const cleanBnChapter = (s: string) =>
  s
    .replace(/\([^)]*\)/g, '')
    .replace(/[^\u0980-\u09FFa-zA-Z0-9]+/g, ' ')
    .trim()
    .toLowerCase();

export async function loadChapterQuestionsComplete(
  chapterId: string,
  chapterName: string,
  subject: string
): Promise<{
  all: Question[];
  varsity: Question[];
  mat: Question[];
  predictor: Question[];
}> {
  const [bankAll, extPool] = await Promise.all([loadAllBankQuestions(), loadExtendedBankPool()]);
  const targetClean = cleanBnChapter(chapterName);
  const targetId = chapterId.trim().toLowerCase();

  const matchesChapter = (qChapterId: string, qChapterName: string, qSubject: string) => {
    if (qChapterId.trim().toLowerCase() === targetId) return true;
    if (normalizeSubject(qSubject) !== normalizeSubject(subject)) return false;
    const cand = cleanBnChapter(qChapterName);
    if (!cand || !targetClean) return false;
    return cand === targetClean || cand.includes(targetClean) || targetClean.includes(cand);
  };

  const bankMatches = bankAll
    .filter((q) => matchesChapter(q.chapter_id, q.chapter_name, q.subject))
    .map((q) => ({
      ...q,
      __isPredictor:
        (q.years_hit ?? 0) >= 2 ||
        (q.likelihood_pct ?? 0) > 0 ||
        q.source_type === 'paper_final' ||
        q.id.startsWith('pred_'),
    }));

  const extMatches = extPool.filter((q) =>
    matchesChapter(q.chapter_id, q.__rawChapter || q.chapter_name, q.subject)
  );

  // Merge and dedupe while preserving __isPredictor if ANY duplicate copy was a predictor
  const predTexts = new Set<string>();
  const combined = [...bankMatches, ...extMatches];
  for (const q of combined) {
    if (q.__isPredictor) {
      predTexts.add(q.question.replace(/\s+/g, ' ').trim().toLowerCase().slice(0, 140));
    }
  }

  const all = dedupe(combined);
  const varsity = all.filter((q) => q.exam !== 'mat');
  const mat = all.filter((q) => q.exam === 'mat');
  const predictor = all.filter((q) => {
    const key = q.question.replace(/\s+/g, ' ').trim().toLowerCase().slice(0, 140);
    return predTexts.has(key) || (q.years_hit ?? 0) >= 2 || (q.likelihood_pct ?? 0) > 0;
  });

  return { all, varsity, mat, predictor };
}

