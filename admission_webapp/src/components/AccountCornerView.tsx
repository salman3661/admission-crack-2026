import React, { useState, useMemo } from 'react';
import {
  User,
  BarChart3,
  ClipboardList,
  Bookmark as BookmarkIcon,
  Settings,
  RefreshCw,
  Download,
  Upload,
  Trash2,
  ArrowRight,
  LogIn,
} from 'lucide-react';
import {
  BANK_INDEX,
  LocalStorageAdapter,
  getSolvedQuestionsMap,
  getMockTracker,
  getBookmarks,
  getErrorLog,
  resetAllLocalProgress,
  type SyncState,
} from '../lib/library';
import { useSEO } from '../lib/seo';
import type { TrackType, UserProfile } from '../types';

interface AccountCornerViewProps {
  user: UserProfile;
  activeTrack: TrackType;
  onSelectTrack: (track: TrackType) => void;
  onNavigate: (path: string) => void;
  onOpenAuth: () => void;
}

export const AccountCornerView: React.FC<AccountCornerViewProps> = ({
  user,
  activeTrack,
  onSelectTrack,
  onNavigate,
  onOpenAuth,
}) => {
  const [tab, setTab] = useState<'progress' | 'exams' | 'bookmarks' | 'settings'>('progress');
  const [targetScore, setTargetScore] = useState<number>(() =>
    Number(localStorage.getItem('ac_target_score_v1') || 80)
  );
  const [syncMsg, setSyncMsg] = useState<string>('সিঙ্ক: স্থানীয় (এই ডিভাইসে)');
  const [, setRefreshTick] = useState(0);

  useSEO({
    title: '👤 অ্যাকাউন্ট ও প্রগতি (Account & Progress) | Admission Crack 2026',
    description:
      'তোমার এমসিকিউ, লিখিত, সাপ্তাহিক ড্রিল ও মক পরীক্ষার অগ্রগতি, বুকমার্ক এবং ডেটা ব্যাকআপ সেটিংস।',
    path: '/account',
  });

  const solvedMap = useMemo(() => getSolvedQuestionsMap(), [tab]);
  const mocks = useMemo(() => getMockTracker(), [tab]);
  const bookmarks = useMemo(() => getBookmarks(), [tab]);
  const errors = useMemo(() => getErrorLog(), [tab]);

  const writtenDraftsCount = useMemo(() => {
    try {
      const raw = localStorage.getItem('ac_written_drafts_v1');
      if (!raw) return 0;
      const obj = JSON.parse(raw);
      return Object.values(obj).filter((v) => String(v || '').trim().length > 0).length;
    } catch {
      return 0;
    }
  }, [tab]);

  const solvedEntries = Object.values(solvedMap);
  const solvedCount = solvedEntries.length;
  const wrongCount = solvedEntries.filter((x) => !x.correct).length;
  const mcqPct = BANK_INDEX.total_mcqs
    ? Math.min(100, Math.round((solvedCount / BANK_INDEX.total_mcqs) * 100))
    : 0;
  const writtenPct = BANK_INDEX.total_written
    ? Math.min(100, Math.round((writtenDraftsCount / BANK_INDEX.total_written) * 100))
    : 0;

  const solvedByWeek = useMemo(() => {
    const out: Record<number, number> = {};
    for (const v of solvedEntries) {
      if (v.week) out[v.week] = (out[v.week] || 0) + 1;
    }
    return out;
  }, [solvedEntries]);

  // 25-day roadmap calculation relative to 12 Dec 2026
  const roadmapDay = useMemo(() => {
    const start = new Date('2026-11-18T00:00:00').getTime();
    const diff = Math.floor((Date.now() - start) / 86400000) + 1;
    return Math.max(1, Math.min(25, diff));
  }, []);

  // Exam table stats (Tab 2)
  const examRows = useMemo(() => {
    const pfMocks = mocks.filter((m) => /paper\s*final|pf/i.test(m.name));
    const sfMocks = mocks.filter((m) => /subject\s*final|sf/i.test(m.name));
    const mtMocks = mocks.filter((m) => /model\s*test|mt/i.test(m.name));
    const duMocks = mocks.filter(
      (m) => m.exam === 'du_ka' && !/paper\s*final|subject\s*final|model\s*test/i.test(m.name)
    );
    const matMocks = mocks.filter((m) => m.exam === 'mat');

    const avgScore = (arr: typeof mocks) =>
      arr.length ? Math.round(arr.reduce((a, b) => a + b.GRAND_TOTAL, 0) / arr.length) : null;

    return [
      { label: 'Paper Final 01–10', total: 10, taken: pfMocks.length, score: avgScore(pfMocks) },
      { label: 'Subject Final (Phys/Chem/M/B)', total: 4, taken: sfMocks.length, score: avgScore(sfMocks) },
      { label: 'Model Test 01–05', total: 5, taken: mtMocks.length, score: avgScore(mtMocks) },
      { label: 'DU Ka Mock (গোল্ড)', total: 3, taken: duMocks.length, score: avgScore(duMocks) },
      { label: 'MAT Mock (গোল্ড)', total: 2, taken: matMocks.length, score: avgScore(matMocks) },
    ];
  }, [mocks]);

  const handleManualSync = async () => {
    const state = await LocalStorageAdapter.get();
    await LocalStorageAdapter.put(state);
    setSyncMsg('সিঙ্ক: স্থানীয় (এই ডিভাইসে · এইমাত্র আপডেট হয়েছে)');
    setRefreshTick((t) => t + 1);
  };

  const handleSaveTargetScore = (val: number) => {
    const clamped = Math.max(40, Math.min(100, val));
    setTargetScore(clamped);
    localStorage.setItem('ac_target_score_v1', String(clamped));
  };

  const handleExportAllData = async () => {
    const state = await LocalStorageAdapter.get();
    const payload = {
      ...state,
      solvedQuestions: getSolvedQuestionsMap(),
    };
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `admission_crack_backup_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleImportData = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = async () => {
      try {
        const parsed = JSON.parse(String(reader.result || '{}')) as SyncState & {
          solvedQuestions?: Record<string, unknown>;
        };
        await LocalStorageAdapter.put(parsed);
        if (parsed.solvedQuestions) {
          localStorage.setItem('ac_solved_qids_v1', JSON.stringify(parsed.solvedQuestions));
        }
        setSyncMsg('ডেটা সফলভাবে ইমপোর্ট হয়েছে (স্থানীয় স্টোরেজ)');
        setRefreshTick((t) => t + 1);
      } catch {
        setSyncMsg('JSON ফাইল পড়া যায়নি।');
      }
    };
    reader.readAsText(file);
  };

  const handleReset = () => {
    if (window.confirm('সব স্থানীয় অগ্রগতি, ভুল লগ ও বুকমার্ক মুছে ফেলতে চাও?')) {
      resetAllLocalProgress();
      setRefreshTick((t) => t + 1);
      setSyncMsg('সব ডেটা রিসেট করা হয়েছে।');
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-6">
      {/* Header Summary Card */}
      <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-6 flex flex-wrap items-center justify-between gap-4 shadow-xs">
        <div className="flex items-center gap-3.5">
          <div className="w-12 h-12 rounded-2xl bg-emerald-600/15 text-emerald-700 dark:text-emerald-300 flex items-center justify-center font-black text-lg">
            <User className="w-6 h-6" />
          </div>
          <div>
            <div className="text-lg font-extrabold text-slate-900 dark:text-white">
              {user.name || 'সালমান'} · {activeTrack === 'medical' ? 'মেডিকেল (MAT) ২০২৬' : "ঢাবি 'ক' ২০২৬"}
            </div>
            <div className="text-xs text-slate-500 mt-0.5 flex flex-wrap items-center gap-2">
              <span>টার্গেট স্কোর: {targetScore}+</span>
              <span>•</span>
              <span>Day {roadmapDay}/25 রোডম্যাপ</span>
              <span>•</span>
              <span className="text-emerald-600 dark:text-emerald-400 font-bold">{syncMsg}</span>
            </div>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={handleManualSync}
            className="px-3.5 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-bold flex items-center gap-1.5 cursor-pointer"
          >
            <RefreshCw className="w-3.5 h-3.5" /> এখনই সিঙ্ক
          </button>
          <button
            onClick={onOpenAuth}
            className="px-3.5 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1.5 cursor-pointer"
          >
            <LogIn className="w-3.5 h-3.5" /> {user.isLoggedIn ? 'প্রোফাইল' : 'Google প্রোফাইল'}
          </button>
        </div>
      </div>

      {/* 4 Tabs */}
      <div className="flex flex-wrap gap-2">
        {(
          [
            ['progress', 'প্রগতি', BarChart3],
            ['exams', 'পরীক্ষা', ClipboardList],
            ['bookmarks', `বুকমার্ক (${bookmarks.length})`, BookmarkIcon],
            ['settings', 'সেটিংস', Settings],
          ] as const
        ).map(([k, lbl, Icon]) => (
          <button
            key={k}
            onClick={() => setTab(k)}
            className={`px-4 py-2 rounded-2xl text-xs font-extrabold flex items-center gap-1.5 cursor-pointer ${
              tab === k
                ? 'bg-emerald-600 text-white shadow-xs'
                : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300'
            }`}
          >
            <Icon className="w-4 h-4" /> {lbl}
          </button>
        ))}
      </div>

      {/* TAB 1: PROGRESS */}
      {tab === 'progress' && (
        <div className="space-y-4">
          <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-6 space-y-4">
            <h2 className="text-base font-extrabold text-slate-900 dark:text-white">📊 সামগ্রিক অগ্রগতি</h2>

            <div className="space-y-3 text-xs">
              <div>
                <div className="flex justify-between font-bold mb-1">
                  <span>MCQ অনুশীলন</span>
                  <span>
                    {mcqPct}% ({solvedCount}/{BANK_INDEX.total_mcqs})
                  </span>
                </div>
                <div className="h-2.5 w-full bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                  <div className="h-full bg-emerald-500 rounded-full" style={{ width: `${mcqPct}%` }} />
                </div>
              </div>

              <div>
                <div className="flex justify-between font-bold mb-1">
                  <span>Written অনুশীলন</span>
                  <span>
                    {writtenPct}% ({writtenDraftsCount}/{BANK_INDEX.total_written})
                  </span>
                </div>
                <div className="h-2.5 w-full bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                  <div className="h-full bg-purple-500 rounded-full" style={{ width: `${writtenPct}%` }} />
                </div>
              </div>

              <div>
                <div className="flex justify-between font-bold mb-1">
                  <span>Mock পরীক্ষা</span>
                  <span>{mocks.length}/7</span>
                </div>
                <div className="h-2.5 w-full bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-teal-500 rounded-full"
                    style={{ width: `${Math.min(100, Math.round((mocks.length / 7) * 100))}%` }}
                  />
                </div>
              </div>
            </div>

            <div className="pt-2 text-xs text-slate-600 dark:text-slate-300 flex flex-wrap gap-4">
              <span>
                মোট সমাধান: <strong>{solvedCount}</strong> প্রশ্ন
              </span>
              <span>
                ভুল উত্তর: <strong>{wrongCount}</strong>টি
              </span>
              <span>
                Mistake Book লগ: <strong>{errors.length}</strong>টি
              </span>
              <span>
                রোডম্যাপ: <strong>Day {roadmapDay}/25</strong>
              </span>
            </div>
          </div>

          {/* Week 01-09 Mini Bars */}
          <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-6 space-y-3">
            <h3 className="text-sm font-extrabold text-slate-900 dark:text-white">
              📅 সপ্তাহভিত্তিক অগ্রগতি (Week 01 – Week 09)
            </h3>
            <div className="grid sm:grid-cols-3 gap-3">
              {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((w) => {
                const totalW = BANK_INDEX.by_week[`week_0${w}`] || 0;
                const doneW = solvedByWeek[w] || 0;
                const pct = totalW ? Math.min(100, Math.round((doneW / totalW) * 100)) : 0;
                return (
                  <div
                    key={w}
                    onClick={() => onNavigate('/weekly')}
                    className="p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700 cursor-pointer"
                  >
                    <div className="flex justify-between text-xs font-bold mb-1">
                      <span>Week 0{w}</span>
                      <span className="text-emerald-600 dark:text-emerald-400">
                        {doneW}/{totalW}
                      </span>
                    </div>
                    <div className="h-1.5 w-full bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                      <div className="h-full bg-emerald-500 rounded-full" style={{ width: `${pct}%` }} />
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: EXAMS TABLE */}
      {tab === 'exams' && (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-6 space-y-4">
          <div className="flex items-center justify-between gap-2">
            <h2 className="text-base font-extrabold text-slate-900 dark:text-white">
              🗓 পরীক্ষার তালিকা ও স্কোর সামারি
            </h2>
            <button
              onClick={() => onNavigate('/mock-tracker')}
              className="text-xs font-bold text-emerald-600 flex items-center gap-1 cursor-pointer"
            >
              Mock Tracker খোলো <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead>
                <tr className="border-b border-slate-200 dark:border-slate-800 text-slate-500">
                  <th className="py-2.5 pr-4">পরীক্ষা</th>
                  <th className="py-2.5 px-3 text-center">মোট</th>
                  <th className="py-2.5 px-3 text-center">দিয়েছে</th>
                  <th className="py-2.5 pl-3 text-right">গড় স্কোর</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 dark:divide-slate-800 font-semibold">
                {examRows.map((r) => (
                  <tr key={r.label}>
                    <td className="py-3 pr-4 text-slate-900 dark:text-white font-bold">{r.label}</td>
                    <td className="py-3 px-3 text-center">{r.total}</td>
                    <td className="py-3 px-3 text-center text-emerald-600 dark:text-emerald-400 font-extrabold">
                      {r.taken}
                    </td>
                    <td className="py-3 pl-3 text-right font-extrabold">
                      {r.score !== null ? r.score : '—'}
                    </td>
                  </tr>
                ))}
              </tbody>
              <tfoot>
                <tr className="border-t-2 border-slate-200 dark:border-slate-700 font-extrabold text-slate-900 dark:text-white">
                  <td className="py-3 pr-4">মোট</td>
                  <td className="py-3 px-3 text-center">২৪</td>
                  <td className="py-3 px-3 text-center text-emerald-600">{mocks.length}</td>
                  <td className="py-3 pl-3 text-right">—</td>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>
      )}

      {/* TAB 3: BOOKMARKS */}
      {tab === 'bookmarks' && (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-6 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-base font-extrabold text-slate-900 dark:text-white">
              🔖 সংরক্ষিত বুকমার্ক ({bookmarks.length})
            </h2>
            <button
              onClick={() => onNavigate('/bookmarks')}
              className="px-3.5 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1 cursor-pointer"
            >
              সব বুকমার্ক ও সেট বিল্ডার <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>

          {bookmarks.length === 0 ? (
            <p className="text-xs text-slate-500 py-4">এখনো কোনো প্রশ্ন বুকমার্ক করা হয়নি।</p>
          ) : (
            <div className="space-y-2">
              {bookmarks.slice(0, 6).map((b) => (
                <div
                  key={b.questionId}
                  onClick={() => onNavigate('/bookmarks')}
                  className="p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700 flex items-center justify-between gap-2 text-xs cursor-pointer"
                >
                  <div className="truncate">
                    <span className="font-extrabold text-amber-600 mr-2">
                      ★ {b.subject} · {b.chapter}
                    </span>
                    <span className="text-slate-600 dark:text-slate-300">{b.question.slice(0, 80)}...</span>
                  </div>
                  <ArrowRight className="w-3.5 h-3.5 shrink-0 text-slate-400" />
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* TAB 4: SETTINGS */}
      {tab === 'settings' && (
        <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-5 sm:p-6 space-y-5">
          <h2 className="text-base font-extrabold text-slate-900 dark:text-white">⚙️ সেটিংস ও ব্যাকআপ</h2>

          <div className="grid sm:grid-cols-2 gap-4">
            <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-2">
              <div className="text-xs font-bold text-slate-700 dark:text-slate-200">
                পরের পরীক্ষা নির্বাচন (ডিফল্ট ট্র্যাক):
              </div>
              <div className="flex gap-2">
                <button
                  onClick={() => onSelectTrack('varsity')}
                  className={`flex-1 py-2 rounded-xl text-xs font-bold cursor-pointer ${
                    activeTrack === 'varsity'
                      ? 'bg-emerald-600 text-white'
                      : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700'
                  }`}
                >
                  DU 'Ka' (১২ ডিসে)
                </button>
                <button
                  onClick={() => onSelectTrack('medical')}
                  className={`flex-1 py-2 rounded-xl text-xs font-bold cursor-pointer ${
                    activeTrack === 'medical'
                      ? 'bg-rose-600 text-white'
                      : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700'
                  }`}
                >
                  MAT (১৮ ডিসে)
                </button>
              </div>
            </div>

            <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-2">
              <div className="text-xs font-bold text-slate-700 dark:text-slate-200">
                লক্ষ্য স্কোর (ডিফল্ট ৭৮–৮০):
              </div>
              <input
                type="number"
                min={40}
                max={100}
                value={targetScore}
                onChange={(e) => handleSaveTargetScore(Number(e.target.value))}
                className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-xs font-bold"
              />
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-3 pt-2">
            <button
              onClick={handleExportAllData}
              className="px-4 py-2.5 rounded-xl bg-emerald-600 text-white text-xs font-bold flex items-center gap-1.5 cursor-pointer"
            >
              <Download className="w-4 h-4" /> সব ডেটা Export (JSON)
            </button>

            <label className="px-4 py-2.5 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-bold flex items-center gap-1.5 cursor-pointer">
              <Upload className="w-4 h-4" /> ডেটা Import (JSON)
              <input type="file" accept=".json" onChange={handleImportData} className="hidden" />
            </label>

            <button
              onClick={handleReset}
              className="ml-auto px-4 py-2.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 text-rose-600 dark:text-rose-400 border border-rose-200 dark:border-rose-800 text-xs font-bold flex items-center gap-1.5 cursor-pointer"
            >
              <Trash2 className="w-4 h-4" /> সব ডেটা মুছে ফেলো
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
