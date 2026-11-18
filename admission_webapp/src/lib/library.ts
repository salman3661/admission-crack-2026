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

export interface BankIndex {
  generated_at: string;
  total_questions: number;
  total_mcqs: number;
  total_written: number;
  by_exam: Record<string, number>;
  by_subject: Record<string, number>;
  by_source_type: Record<string, number>;
  by_week: Record<string, number>;
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

    const textKey = row.question.replace(/\s+/g, ' ').trim().toLowerCase();
    if (textKey.length > 30 && byText.has(textKey)) {
      const existing = byText.get(textKey)!;
      const merged = new Set([...(existing.appears_in || [existing.source_name]), ...(row.appears_in || [row.source_name])]);
      existing.appears_in = [...merged];
      continue;
    }

    const copy = { ...row };
    byId.set(copy.id, copy);
    if (textKey.length > 30) {
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

export async function loadPapersByFilter(opts: {
  exam?: string;
  sourceType?: SourceType | 'all';
  subject?: string;
  chapterId?: string;
  week?: string;
}): Promise<Question[]> {
  const matchingPapers = BANK_INDEX.papers.filter((p) => {
    if (opts.exam && opts.exam !== 'all') {
      if (opts.exam === 'du_ka' && !p.exams.includes('du_ka') && !p.exams.includes('other')) return false;
      if (opts.exam === 'mat' && !p.exams.includes('mat') && !p.exams.includes('other')) return false;
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

  if (opts.subject && opts.subject !== 'All') {
    all = all.filter((q) => q.subject === opts.subject);
  }
  if (opts.chapterId) {
    all = all.filter((q) => q.chapter_id === opts.chapterId);
  }
  if (opts.week && opts.week !== 'all') {
    const wkNum = opts.week.replace('week_', '');
    const re = new RegExp(`Week\\s*0?${parseInt(wkNum, 10)}\\b`, 'i');
    all = all.filter((q) => re.test(q.source_name));
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
  } catch {
    // ignore
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
