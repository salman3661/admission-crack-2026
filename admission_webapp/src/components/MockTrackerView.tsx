import React, { useState } from 'react';
import { ClipboardList, Plus, Trash2, Download } from 'lucide-react';
import {
  getMockTracker,
  saveMockTrackerEntry,
  deleteMockTrackerEntry,
  type MockTrackerEntry,
} from '../lib/library';
import { useSEO } from '../lib/seo';

export const MockTrackerView: React.FC = () => {
  const [rows, setRows] = useState<MockTrackerEntry[]>(() => getMockTracker());
  const [showForm, setShowForm] = useState(false);
  const [form, setForm] = useState({
    date: new Date().toISOString().slice(0, 10),
    name: 'Model Test 01',
    exam: 'du_ka' as 'du_ka' | 'mat',
    Physics_MCQ: 10,
    Physics_Written: 6,
    Chem_MCQ: 10,
    Chem_Written: 6,
    Math_MCQ: 9,
    Math_Written: 5,
    Bio_MCQ: 11,
    Bio_Written: 7,
    accuracy_pct: 80,
    time_MCQ_used: 43,
    time_written_used: 42,
    written_blank_count: 0,
    top3_lossy_chapter: '',
    next48h_fix: '',
  });

  useSEO({
    title: 'Mock Tracker — কোচিং ও মক টেস্ট স্কোর শিট | Admission Crack 2026',
    description: 'Paper Final, Subject Final ও Model Test 1–5 এর স্কোর, সময় ও Top-3 লসি চ্যাপ্টার ট্র্যাকার।',
    path: '/mock-tracker',
  });

  const handleAdd = (e: React.FormEvent) => {
    e.preventDefault();
    const mcqTotal = +(form.Physics_MCQ + form.Chem_MCQ + form.Math_MCQ + form.Bio_MCQ).toFixed(2);
    const writtenTotal = +(form.Physics_Written + form.Chem_Written + form.Math_Written + form.Bio_Written).toFixed(2);
    const entry: MockTrackerEntry = {
      id: `mt_${Date.now()}`,
      ...form,
      MCQ_total: mcqTotal,
      Written_total: writtenTotal,
      GRAND_TOTAL: +(mcqTotal + writtenTotal).toFixed(2),
    };
    setRows(saveMockTrackerEntry(entry));
    setShowForm(false);
  };

  const handleExportCSV = () => {
    const header =
      'date,name,Physics_MCQ,Physics_Written,Chem_MCQ,Chem_Written,Math_MCQ,Math_Written,Bio_MCQ,Bio_Written,MCQ_total,Written_total,GRAND_TOTAL,accuracy_%,time_MCQ_used,time_written_used,top3_lossy_chapter,next48h_fix,written_blank_count';
    const body = rows
      .map((r) =>
        [
          r.date,
          `"${r.name.replace(/"/g, '""')}"`,
          r.Physics_MCQ,
          r.Physics_Written,
          r.Chem_MCQ,
          r.Chem_Written,
          r.Math_MCQ,
          r.Math_Written,
          r.Bio_MCQ,
          r.Bio_Written,
          r.MCQ_total,
          r.Written_total,
          r.GRAND_TOTAL,
          r.accuracy_pct,
          r.time_MCQ_used,
          r.time_written_used,
          `"${r.top3_lossy_chapter.replace(/"/g, '""')}"`,
          `"${r.next48h_fix.replace(/"/g, '""')}"`,
          r.written_blank_count,
        ].join(',')
      )
      .join('\n');
    const blob = new Blob([`${header}\n${body}`], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'mock-tracker.csv';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
            <ClipboardList className="w-6 h-6 text-emerald-600" /> Mock Tracker
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            Paper Final, Subject Final ও Model Test 1–5 এর সম্পূর্ণ স্কোর ও ৪৮-ঘণ্টার ফিক্স প্ল্যান।
          </p>
        </div>
        <div className="flex gap-2">
          <button
            onClick={handleExportCSV}
            disabled={rows.length === 0}
            className="px-3.5 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold flex items-center gap-1.5 cursor-pointer disabled:opacity-40"
          >
            <Download className="w-3.5 h-3.5" /> CSV এক্সপোর্ট
          </button>
          <button
            onClick={() => setShowForm((s) => !s)}
            className="px-4 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1.5 cursor-pointer"
          >
            <Plus className="w-4 h-4" /> নতুন Mock যোগ করো
          </button>
        </div>
      </div>

      {showForm && (
        <form onSubmit={handleAdd} className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 space-y-4">
          <div className="grid sm:grid-cols-3 gap-3 text-xs">
            <div>
              <label className="font-bold block mb-1">তারিখ</label>
              <input type="date" value={form.date} onChange={(e) => setForm({ ...form, date: e.target.value })} className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800" />
            </div>
            <div>
              <label className="font-bold block mb-1">পরীক্ষার নাম</label>
              <input type="text" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800" />
            </div>
            <div>
              <label className="font-bold block mb-1">Accuracy (%)</label>
              <input type="number" value={form.accuracy_pct} onChange={(e) => setForm({ ...form, accuracy_pct: +e.target.value })} className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800" />
            </div>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
            {[
              ['Physics_MCQ', 'Phys MCQ'],
              ['Physics_Written', 'Phys Writ'],
              ['Chem_MCQ', 'Chem MCQ'],
              ['Chem_Written', 'Chem Writ'],
              ['Math_MCQ', 'Math MCQ'],
              ['Math_Written', 'Math Writ'],
              ['Bio_MCQ', 'Bio MCQ'],
              ['Bio_Written', 'Bio Writ'],
            ].map(([k, label]) => (
              <div key={k}>
                <label className="font-bold block mb-1">{label}</label>
                <input
                  type="number"
                  step="0.25"
                  value={form[k as keyof typeof form] as number}
                  onChange={(e) => setForm({ ...form, [k]: +e.target.value })}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800"
                />
              </div>
            ))}
          </div>

          <div className="grid sm:grid-cols-2 gap-3 text-xs">
            <div>
              <label className="font-bold block mb-1">Top-3 Lossy Chapters</label>
              <input type="text" value={form.top3_lossy_chapter} onChange={(e) => setForm({ ...form, top3_lossy_chapter: e.target.value })} placeholder="যেমন: Vector, Electrochemistry, Integration" className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800" />
            </div>
            <div>
              <label className="font-bold block mb-1">Next 48h Fix</label>
              <input type="text" value={form.next48h_fix} onChange={(e) => setForm({ ...form, next48h_fix: e.target.value })} placeholder="৪৮ ঘণ্টায় কী ঠিক করবে" className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800" />
            </div>
          </div>

          <button type="submit" className="px-5 py-2.5 rounded-xl bg-emerald-600 text-white text-xs font-bold cursor-pointer">
            সেভ করো
          </button>
        </form>
      )}

      <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 overflow-x-auto">
        <table className="w-full text-xs text-left border-collapse min-w-[640px]">
          <thead>
            <tr className="border-b border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 text-slate-600 dark:text-slate-300">
              <th className="p-3">তারিখ</th>
              <th className="p-3">পরীক্ষা</th>
              <th className="p-3">MCQ</th>
              <th className="p-3">Written</th>
              <th className="p-3">মোট</th>
              <th className="p-3">Accuracy</th>
              <th className="p-3">Top-3 লসি অধ্যায়</th>
              <th className="p-3"></th>
            </tr>
          </thead>
          <tbody>
            {rows.length === 0 ? (
              <tr>
                <td colSpan={8} className="p-8 text-center text-slate-500">
                  এখনো কোনো মক টেস্ট এন্ট্রি নেই। সিমুলেটর থেকে সেভ করো অথবা "+ নতুন Mock যোগ করো" বাটনে ক্লিক করো।
                </td>
              </tr>
            ) : (
              rows.map((r) => (
                <tr key={r.id} className="border-b border-slate-100 dark:border-slate-800/60">
                  <td className="p-3 whitespace-nowrap">{r.date}</td>
                  <td className="p-3 font-bold">{r.name}</td>
                  <td className="p-3">{r.MCQ_total}</td>
                  <td className="p-3">{r.Written_total}</td>
                  <td className="p-3 font-black text-emerald-600">{r.GRAND_TOTAL}</td>
                  <td className="p-3">{r.accuracy_pct}%</td>
                  <td className="p-3 max-w-[220px] truncate">{r.top3_lossy_chapter || '—'}</td>
                  <td className="p-3">
                    <button onClick={() => setRows(deleteMockTrackerEntry(r.id))} className="text-slate-400 hover:text-rose-600 cursor-pointer">
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};
