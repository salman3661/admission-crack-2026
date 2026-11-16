import type { QuizQuestion, WeekFilterType } from '../types';
import weeksData from '../data/weeks.json';

const textKey = (q: QuizQuestion) =>
  String(q.q || q.question || '')
    .replace(/^\[[^\]]*\]/, '')
    .replace(/\W+/g, '')
    .slice(0, 80);

/** Remove duplicate ids / identical question texts (first occurrence wins). */
export function dedupeQuestions(list: QuizQuestion[]): QuizQuestion[] {
  const ids = new Set<string>();
  const texts = new Set<string>();
  const out: QuizQuestion[] = [];
  for (const q of list) {
    const t = textKey(q);
    if (ids.has(q.id) || (t && texts.has(t))) continue;
    ids.add(q.id);
    if (t) texts.add(t);
    out.push(q);
  }
  return out;
}

/**
 * Tier 1 (Weekly): ONLY the questions whose week_id is exactly the selected week.
 * 'all' (Full Mock pool): every question, de-duplicated.
 * Non-week buckets (e.g. 'varsity_full_syllabus', owned by Tier 2/3) never enter weekly drills.
 */
export function scopeByWeek(list: QuizQuestion[], week: WeekFilterType): QuizQuestion[] {
  if (week === 'all') return dedupeQuestions(list);
  return dedupeQuestions(list.filter((q) => (q.week_id || '').toLowerCase() === week));
}

export interface WeekChapterSummary { chapter: string; count: number }

/** Chapter-wise breakdown of exactly one week's questions. */
export function weekChapterBreakdown(list: QuizQuestion[]): WeekChapterSummary[] {
  const m = new Map<string, number>();
  for (const q of list) {
    const c = ((q as { chapter?: string }).chapter) || String(q.subject || 'অন্যান্য');
    m.set(c, (m.get(c) || 0) + 1);
  }
  return [...m.entries()].map(([chapter, count]) => ({ chapter, count })).sort((a, b) => b.count - a.count);
}

export function weekMeta(week: WeekFilterType): { name: string; badge: string } | null {
  const w = (weeksData as { id: string; name: string; badge: string }[]).find((x) => x.id === week);
  return w ? { name: w.name, badge: w.badge } : null;
}
