import React, { useState, useMemo } from 'react';
import { BookX, CheckCircle2, Trash2, Clock, RotateCcw } from 'lucide-react';
import {
  getErrorLog,
  reviewMistakeEntry,
  removeErrorLogEntry,
  type ErrorLogEntry,
} from '../lib/library';
import { MathText } from './MathText';
import { useSEO } from '../lib/seo';

const OPTION_LABELS = ['ক', 'খ', 'গ', 'ঘ', 'ঙ'];

export const MistakeBookView: React.FC = () => {
  const [entries, setEntries] = useState<ErrorLogEntry[]>(() => getErrorLog());
  const [tab, setTab] = useState<'due' | 'all'>('due');
  const [whyDrafts, setWhyDrafts] = useState<Record<string, string>>({});
  const [retestQid, setRetestQid] = useState<string | null>(null);
  const [retestChoice, setRetestChoice] = useState<number | null>(null);

  useSEO({
    title: 'Mistake Book (SM-2 Error Log) | Admission Crack 2026',
    description: 'ভুল প্রশ্নের স্বয়ংক্রিয় SM-2 রিভিশন (১ / ৩ / ৭ / ১৪ দিন) ও ভুলের কারণ লগ।',
    path: '/mistake-book',
  });

  const now = Date.now();
  const dueEntries = useMemo(
    () => entries.filter((e) => new Date(e.retestDue).getTime() <= now),
    [entries, now]
  );

  const visible = tab === 'due' ? dueEntries : entries;

  const handleSaveWhy = (qid: string) => {
    const updated = reviewMistakeEntry(qid, false, whyDrafts[qid] ?? '');
    setEntries(updated);
  };

  const handleRetestSubmit = (e: ErrorLogEntry, chosenIdx: number) => {
    setRetestChoice(chosenIdx);
    const ok = chosenIdx === e.correct_index;
    const updated = reviewMistakeEntry(e.qid, ok, whyDrafts[e.qid] ?? e.whyWrong);
    setEntries(updated);
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <BookX className="w-6 h-6 text-rose-600" /> Mistake Book (Error Log)
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            তোমার সবচেয়ে বড় সম্পদ — SM-2 ব্যবধানে (১ / ৩ / ৭ / ১৪ দিন) ভুলগুলো পুনরায় টেস্ট করো।
          </p>
        </div>

        <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-2xl">
          <button
            onClick={() => setTab('due')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              tab === 'due' ? 'bg-rose-600 text-white' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            আজকের Due ({dueEntries.length})
          </button>
          <button
            onClick={() => setTab('all')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              tab === 'all' ? 'bg-slate-900 dark:bg-white text-white dark:text-slate-900' : 'text-slate-600 dark:text-slate-300'
            }`}
          >
            সব ভুল ({entries.length})
          </button>
        </div>
      </div>

      {visible.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-10 text-center">
          <CheckCircle2 className="w-10 h-10 text-emerald-500 mx-auto mb-2" />
          <p className="text-sm font-bold text-slate-700 dark:text-slate-200">
            {tab === 'due' ? 'আজকের জন্য কোনো Due ভুল নেই!' : 'এখনো কোনো ভুল রেকর্ড হয়নি।'}
          </p>
          <p className="text-xs text-slate-500 mt-1">ড্রিল বা সিমুলেটরে কোনো প্রশ্ন ভুল করলে তা এখানে যুক্ত হবে।</p>
        </div>
      ) : (
        <div className="space-y-4">
          {visible.map((e) => (
            <div key={e.qid} className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 space-y-3">
              <div className="flex flex-wrap items-center justify-between gap-2 text-xs">
                <div className="flex flex-wrap items-center gap-1.5">
                  <span className="px-2.5 py-0.5 rounded-full bg-rose-50 dark:bg-rose-950/50 text-rose-700 dark:text-rose-300 font-bold">
                    {e.subject} · {e.chapter}
                  </span>
                  <span className="px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    {e.source_name}
                  </span>
                  <span className="flex items-center gap-1 text-slate-500">
                    <Clock className="w-3 h-3" /> Next: {e.retestDue.slice(0, 10)}
                  </span>
                </div>
                <button
                  onClick={() => setEntries(removeErrorLogEntry(e.qid))}
                  className="text-slate-400 hover:text-rose-600 cursor-pointer"
                  title="মুছে ফেলো"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>

              <div className="text-sm font-semibold text-slate-900 dark:text-white">
                <MathText content={e.question} block />
              </div>

              {retestQid === e.qid && e.options.length > 0 ? (
                <div className="space-y-2 pt-2">
                  {e.options.map((opt, idx) => (
                    <button
                      key={idx}
                      onClick={() => handleRetestSubmit(e, idx)}
                      className={`w-full text-left p-2.5 rounded-xl border text-xs flex items-center gap-2 cursor-pointer ${
                        retestChoice === idx
                          ? idx === e.correct_index
                            ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40'
                            : 'border-rose-500 bg-rose-50 dark:bg-rose-950/40'
                          : 'border-slate-200 dark:border-slate-700'
                      }`}
                    >
                      <span className="font-bold">{OPTION_LABELS[idx] || idx + 1}.</span>
                      <MathText content={opt} />
                    </button>
                  ))}
                </div>
              ) : (
                <div className="flex flex-wrap items-center gap-2">
                  <button
                    onClick={() => {
                      setRetestQid(e.qid);
                      setRetestChoice(null);
                    }}
                    className="px-3 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1 cursor-pointer"
                  >
                    <RotateCcw className="w-3.5 h-3.5" /> আবার চেষ্টা করো
                  </button>
                </div>
              )}

              <div className="flex gap-2 pt-1">
                <input
                  type="text"
                  value={whyDrafts[e.qid] ?? e.whyWrong}
                  onChange={(ev) => setWhyDrafts((p) => ({ ...p, [e.qid]: ev.target.value }))}
                  placeholder="কেন ভুল হলো? (সূত্র ভুল / তাড়াহুড়ো / কনসেপ্ট গ্যাপ)"
                  className="flex-1 px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-xs"
                />
                <button
                  onClick={() => handleSaveWhy(e.qid)}
                  className="px-3 py-2 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-bold cursor-pointer"
                >
                  সেভ
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
