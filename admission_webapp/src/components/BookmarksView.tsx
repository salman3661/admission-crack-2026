import React, { useState, useMemo } from 'react';
import {
  Bookmark as BookmarkIcon,
  Star,
  Play,
  Trash2,
  Tag,
  FileText,
  Download,
  BookOpen,
  AlertTriangle,
  Sparkles,
} from 'lucide-react';
import {
  getBookmarks,
  removeBookmark,
  updateBookmarkMeta,
  bookmarkToQuestion,
  getErrorLog,
  type Bookmark,
  type Question,
} from '../lib/library';
import { MathText } from './MathText';
import { DrillRunner } from './DrillRunner';
import { useSEO } from '../lib/seo';

export const BookmarksView: React.FC = () => {
  const [bookmarks, setBookmarks] = useState<Bookmark[]>(() => getBookmarks());
  const [filter, setFilter] = useState<string>('All');
  const [expandedSol, setExpandedSol] = useState<Record<string, boolean>>({});
  const [editingNote, setEditingNote] = useState<string | null>(null);
  const [editingTag, setEditingTag] = useState<string | null>(null);
  const [tagInput, setTagInput] = useState('');
  const [drill, setDrill] = useState<{ title: string; questions: Question[] } | null>(null);

  useSEO({
    title: '🔖 বুকমার্ক (প্রশ্ন সংরক্ষণ ও কাস্টম সেট) | Admission Crack 2026',
    description:
      'তোমার সংরক্ষিত গুরুত্বপূর্ণ প্রশ্ন, নোট, ট্যাগ, কাস্টম ড্রিল সেট এবং Anki TSV / JSON এক্সপোর্ট।',
    path: '/bookmarks',
  });

  const errorQids = useMemo(() => new Set(getErrorLog().map((e) => e.qid)), [bookmarks]);

  const filtered = useMemo(() => {
    const startOfToday = new Date();
    startOfToday.setHours(0, 0, 0, 0);
    const todayTs = startOfToday.getTime();

    return bookmarks.filter((b) => {
      if (filter === 'All') return true;
      if (filter === 'mistakes') return errorQids.has(b.questionId);
      if (filter === 'today') return b.createdAt >= todayTs;
      return b.subject === filter;
    });
  }, [bookmarks, filter, errorQids]);

  const handleRemove = (qid: string) => {
    setBookmarks(removeBookmark(qid));
  };

  const handleSaveNote = (qid: string, note: string) => {
    setBookmarks(updateBookmarkMeta(qid, { note }));
  };

  const handleAddTag = (b: Bookmark) => {
    const t = tagInput.trim();
    if (!t) return;
    const nextTags = [...new Set([...(b.tags || []), t])];
    setBookmarks(updateBookmarkMeta(b.questionId, { tags: nextTags }));
    setTagInput('');
    setEditingTag(null);
  };

  const handleBuildSetDrill = (list: Bookmark[], label: string) => {
    const qs = list.map(bookmarkToQuestion);
    setDrill({ title: label, questions: qs });
  };

  const handleExportJSON = () => {
    const blob = new Blob([JSON.stringify(bookmarks, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `bookmarks_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleExportAnkiTSV = () => {
    const lines = bookmarks.map((b) => {
      const front = `[${b.subject} · ${b.chapter}] ${b.question} ${(b.options || []).map((o, i) => `(${String.fromCharCode(65 + i)}) ${o}`).join(' ')}`
        .replace(/[\t\r\n]+/g, ' ');
      const ans =
        b.correct_index !== null && b.options?.[b.correct_index]
          ? `উত্তর: ${b.options[b.correct_index]} — `
          : '';
      const back = `${ans}${b.explanation || ''} ${b.trap ? `[ট্র্যাপ: ${b.trap}]` : ''} ${b.note ? `[নোট: ${b.note}]` : ''}`
        .replace(/[\t\r\n]+/g, ' ');
      const tags = [b.subject, b.chapter_id || 'bookmark', ...(b.tags || [])].join(' ');
      return `${front}\t${back}\t${tags}`;
    });
    const blob = new Blob([lines.join('\n')], { type: 'text/tab-separated-values;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `bookmarks_anki_${new Date().toISOString().slice(0, 10)}.tsv`;
    a.click();
    URL.revokeObjectURL(url);
  };

  if (drill) {
    return (
      <DrillRunner
        questions={drill.questions}
        title={drill.title}
        subtitle={`${drill.questions.length}টি বুকমার্ক প্রশ্ন`}
        onBack={() => {
          setBookmarks(getBookmarks());
          setDrill(null);
        }}
        bookmarkSource="drill"
      />
    );
  }

  const tabs = [
    ['All', 'সব'],
    ['Physics', 'Physics'],
    ['Chemistry', 'Chemistry'],
    ['Higher Math', 'Higher Math'],
    ['Biology', 'Biology'],
    ['mistakes', 'শুধু ভুল'],
    ['today', 'আজকের'],
  ] as const;

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <BookmarkIcon className="w-6 h-6 text-amber-500" /> 🔖 বুকমার্ক ({bookmarks.length})
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            ড্রিল, মাস্টার সেট বা প্রশ্নব্যাংকে ★ চিহ্নে চাপলে প্রশ্ন এখানে সংরক্ষিত হয়।
          </p>
        </div>

        {bookmarks.length > 0 && (
          <div className="flex flex-wrap items-center gap-2">
            <button
              onClick={() => handleBuildSetDrill(filtered.length ? filtered : bookmarks, '🔖 আমার বুকমার্ক কাস্টম সেট')}
              className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold flex items-center gap-1.5 cursor-pointer shadow-xs"
            >
              <Sparkles className="w-3.5 h-3.5" /> এই bookmark গুলোর একটা সেট বানাও ({filtered.length || bookmarks.length})
            </button>
            <button
              onClick={handleExportJSON}
              className="px-3 py-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs font-bold flex items-center gap-1 cursor-pointer"
            >
              <Download className="w-3.5 h-3.5" /> JSON
            </button>
            <button
              onClick={handleExportAnkiTSV}
              className="px-3 py-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs font-bold flex items-center gap-1 cursor-pointer"
            >
              <Download className="w-3.5 h-3.5" /> Anki TSV
            </button>
          </div>
        )}
      </div>

      {/* Filter Tabs */}
      <div className="flex flex-wrap gap-1.5">
        {tabs.map(([k, lbl]) => (
          <button
            key={k}
            onClick={() => setFilter(k)}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold cursor-pointer ${
              filter === k
                ? 'bg-emerald-600 text-white'
                : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-300'
            }`}
          >
            {lbl}
          </button>
        ))}
      </div>

      {filtered.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-10 text-center space-y-2">
          <Star className="w-10 h-10 text-amber-400 mx-auto" />
          <div className="text-sm font-extrabold text-slate-800 dark:text-slate-100">
            এই ফিল্টারে এখনো কোনো বুকমার্ক নেই
          </div>
          <p className="text-xs text-slate-500">
            যেকোনো প্রশ্ন ড্রিলে বা মাস্টার সেটে উপরের ডান কোণার ★ বাটনে চাপলে এখানে জমা হবে।
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          {filtered.map((b) => (
            <div
              key={b.questionId}
              className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 space-y-3 shadow-xs"
            >
              <div className="flex flex-wrap items-center justify-between gap-2 text-xs">
                <div className="flex flex-wrap items-center gap-1.5">
                  <span className="px-2.5 py-0.5 rounded-full bg-amber-50 dark:bg-amber-950/50 text-amber-700 dark:text-amber-300 font-extrabold flex items-center gap-1">
                    <Star className="w-3 h-3 fill-current" /> {b.subject} · {b.chapter}
                  </span>
                  {b.mega_type && (
                    <span className="px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 truncate max-w-[240px]">
                      {b.mega_type}
                    </span>
                  )}
                  {(b.tags || []).map((t) => (
                    <span
                      key={t}
                      className="px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 font-bold"
                    >
                      🏷️ {t}
                    </span>
                  ))}
                </div>
                <span className="text-[11px] text-slate-400">{b.source_name}</span>
              </div>

              <div className="text-sm sm:text-base font-semibold text-slate-900 dark:text-white">
                <MathText content={b.question} block />
              </div>

              {expandedSol[b.questionId] && (
                <div className="space-y-2 pt-1">
                  {b.options && b.options.length > 0 && b.correct_index !== null && (
                    <div className="text-xs font-extrabold text-emerald-700 dark:text-emerald-300">
                      সঠিক উত্তর: <MathText content={b.options[b.correct_index] || ''} />
                    </div>
                  )}
                  {b.explanation && (
                    <div className="p-3.5 rounded-2xl bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/50 text-xs">
                      <div className="font-bold text-emerald-800 dark:text-emerald-300 mb-1 flex items-center gap-1">
                        <BookOpen className="w-3.5 h-3.5" /> সমাধান:
                      </div>
                      <MathText content={b.explanation} block />
                    </div>
                  )}
                  {b.trap && (
                    <div className="p-3.5 rounded-2xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/50 text-xs">
                      <div className="font-bold text-amber-800 dark:text-amber-300 mb-1 flex items-center gap-1">
                        <AlertTriangle className="w-3.5 h-3.5" /> ট্র্যাপ:
                      </div>
                      <MathText content={b.trap} block />
                    </div>
                  )}
                </div>
              )}

              {(editingNote === b.questionId || b.note) && (
                <div className="pt-1">
                  <textarea
                    value={b.note || ''}
                    onChange={(e) => handleSaveNote(b.questionId, e.target.value)}
                    rows={2}
                    placeholder="তোমার নিজের নোট লিখে রাখো..."
                    className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 p-2.5 text-xs"
                  />
                </div>
              )}

              {editingTag === b.questionId && (
                <div className="flex items-center gap-2 pt-1">
                  <input
                    type="text"
                    value={tagInput}
                    onChange={(e) => setTagInput(e.target.value)}
                    placeholder="ট্যাগ (যেমন: রিভিশন, important)"
                    className="px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-xs"
                  />
                  <button
                    onClick={() => handleAddTag(b)}
                    className="px-3 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold cursor-pointer"
                  >
                    যোগ করো
                  </button>
                </div>
              )}

              {/* Actions */}
              <div className="pt-2 border-t border-slate-100 dark:border-slate-800 flex flex-wrap items-center gap-2">
                <button
                  onClick={() =>
                    setExpandedSol((p) => ({ ...p, [b.questionId]: !p[b.questionId] }))
                  }
                  className="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold cursor-pointer"
                >
                  {expandedSol[b.questionId] ? 'সমাধান লুকাও' : 'সমাধান দেখো'}
                </button>

                <button
                  onClick={() => handleBuildSetDrill([b], `${b.subject} · ${b.chapter}`)}
                  className="px-3 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1 cursor-pointer"
                >
                  <Play className="w-3 h-3" /> ড্রিলে নিয়ে যাও
                </button>

                <button
                  onClick={() => setEditingTag((k) => (k === b.questionId ? null : b.questionId))}
                  className="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold flex items-center gap-1 cursor-pointer"
                >
                  <Tag className="w-3 h-3" /> ট্যাগ
                </button>

                <button
                  onClick={() => setEditingNote((k) => (k === b.questionId ? null : b.questionId))}
                  className="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold flex items-center gap-1 cursor-pointer"
                >
                  <FileText className="w-3 h-3" /> নোট
                </button>

                <button
                  onClick={() => handleRemove(b.questionId)}
                  className="ml-auto px-3 py-1.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 text-rose-600 dark:text-rose-400 text-xs font-bold flex items-center gap-1 cursor-pointer"
                >
                  <Trash2 className="w-3 h-3" /> সরাও
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
