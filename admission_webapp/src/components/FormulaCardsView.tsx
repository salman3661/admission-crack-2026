import React, { useState, useEffect, useMemo } from 'react';
import { BookMarked, Search, Printer } from 'lucide-react';
import { MathText } from './MathText';
import { useSEO } from '../lib/seo';

interface FormulaCard {
  subject: string;
  chapter: string;
  title?: string;
  formula: string;
  concept?: string;
}

export const FormulaCardsView: React.FC = () => {
  const [cards, setCards] = useState<FormulaCard[]>([]);
  const [loading, setLoading] = useState(true);
  const [subject, setSubject] = useState('All');
  const [query, setQuery] = useState('');

  useSEO({
    title: 'Formula Cards (সূত্র কার্ড) | Admission Crack 2026',
    description: 'DU Ka ও MAT লিখিত এবং MCQ এর জন্য বিষয় ও অধ্যায়ভিত্তিক প্রিন্টযোগ্য সূত্র কার্ড।',
    path: '/formulas',
  });

  useEffect(() => {
    import('../data/formulas.json').then((mod) => {
      const arr = Array.isArray(mod.default) ? mod.default : [];
      setCards(arr as unknown as FormulaCard[]);
      setLoading(false);
    });
  }, []);

  const subjects = useMemo(() => ['All', ...new Set(cards.map((c) => c.subject).filter(Boolean))], [cards]);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return cards.filter((c) => {
      if (subject !== 'All' && c.subject !== subject) return false;
      if (
        q &&
        !String(c.chapter || '').toLowerCase().includes(q) &&
        !String(c.title || '').toLowerCase().includes(q) &&
        !String(c.formula || '').toLowerCase().includes(q)
      ) {
        return false;
      }
      return true;
    });
  }, [cards, subject, query]);

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3 print:hidden">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <BookMarked className="w-6 h-6 text-emerald-600" /> Formula Cards ({cards.length}টি সূত্র)
          </h1>
          <p className="text-xs text-slate-500 mt-1">প্রতিদিন ৩০ মিনিট লিখিত ও MCQ সূত্র রিভিশনের জন্য।</p>
        </div>

        <button
          onClick={() => window.print()}
          className="px-4 py-2 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-bold flex items-center gap-1.5 cursor-pointer"
        >
          <Printer className="w-4 h-4" /> প্রিন্ট করো
        </button>
      </div>

      <div className="flex flex-col sm:flex-row gap-3 print:hidden">
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="সূত্র বা অধ্যায় খুঁজুন..."
            className="w-full pl-10 pr-4 py-2.5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-xs"
          />
        </div>
        <div className="flex flex-wrap gap-1.5">
          {subjects.map((s) => (
            <button
              key={s}
              onClick={() => setSubject(s)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
                subject === s
                  ? 'bg-emerald-600 text-white'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-300'
              }`}
            >
              {s}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="p-10 text-center text-sm text-slate-500">সূত্র কার্ড লোড হচ্ছে...</div>
      ) : (
        <div className="grid sm:grid-cols-2 gap-3.5">
          {filtered.slice(0, 120).map((c, i) => (
            <div
              key={i}
              className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 space-y-2 break-inside-avoid"
            >
              <div className="flex items-center justify-between text-[11px]">
                <span className="px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 font-bold">
                  {c.subject}
                </span>
                <span className="text-slate-500 font-semibold truncate max-w-[200px]">{c.chapter}</span>
              </div>
              {c.title && <div className="text-xs font-bold text-slate-700 dark:text-slate-300">{c.title}</div>}
              <div className="text-sm font-medium text-slate-900 dark:text-white">
                <MathText content={c.formula} block />
              </div>
              {c.concept && (
                <div className="text-xs text-slate-600 dark:text-slate-400 bg-slate-50 dark:bg-slate-800/60 p-2 rounded-xl">
                  <MathText content={c.concept} />
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
