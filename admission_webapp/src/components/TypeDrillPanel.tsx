import React, { useMemo, useState } from 'react';
import { CheckCircle2, Zap, BookOpen, Sparkles, AlertTriangle } from 'lucide-react';
import varsityBank from '../data/varsity_bank.json';
import medicalBank from '../data/medical_bank.json';
import synthPredictors from '../data/chapter_synthetic_predictors.json';
import { MathText } from './MathText';

interface TypeDrillPanelProps {
  typeId: string;
  typeName: string;
  chapterId: string;
  coreRule?: string;
  speedElimination?: string;
  pastTags?: string[];
  qbRefs?: string[];
}

type TrackFilter = 'all' | 'varsity' | 'medical' | 'engineering';
type DrillTab = 'rule' | 'pyq' | 'predictor';

interface NormalizedQ {
  id: string;
  stem: string;
  opts: string[];
  ans: number;
  origin: string;
  track: 'varsity' | 'medical' | 'engineering';
  exp?: string;
  speedHack?: string;
  trap?: string;
}

const toOpts = (raw: unknown): string[] => {
  if (Array.isArray(raw)) return raw.map(String);
  return [];
};

const classifyTrack = (origin: string, bankTrack?: string): 'varsity' | 'medical' | 'engineering' => {
  if (/buet|ruet|cuet|kuet|ckruet|engineer/i.test(origin)) return 'engineering';
  if (bankTrack === 'medical' || /mat|dat|medical/i.test(origin)) return 'medical';
  return 'varsity';
};

export const TypeDrillPanel: React.FC<TypeDrillPanelProps> = ({
  typeId,
  typeName,
  chapterId,
  coreRule,
  speedElimination,
  pastTags,
  qbRefs,
}) => {
  const [activeTab, setActiveTab] = useState<DrillTab>('rule');
  const [trackFilter, setTrackFilter] = useState<TrackFilter>('all');
  const [selectedOpt, setSelectedOpt] = useState<Record<string, number>>({});

  // 1. Pull PYQs strictly matching this typeId (or fallback to chapterId + typeName keyword)
  const pyqList: NormalizedQ[] = useMemo(() => {
    const all = [
      ...(varsityBank as any[]).map((q) => ({ ...q, _bank: 'varsity' })),
      ...(medicalBank as any[]).map((q) => ({ ...q, _bank: 'medical' })),
    ];
    let matched = all.filter((q) => q.blueprint_type_id === typeId);
    if (matched.length === 0) {
      const chMatches = all.filter((q) => q.blueprint_chapter_id === chapterId);
      const tNum = typeName.match(/Type\s*(\d+)/i)?.[1];
      matched = tNum
        ? chMatches.filter((q) => String(q.type_ref || '').includes(`Type ${tNum}`)).slice(0, 6)
        : chMatches.slice(0, 4);
    }
    const seen = new Set<string>();
    const out: NormalizedQ[] = [];
    for (const q of matched) {
      const opts = toOpts(q.opts || q.options);
      const ans = Number(q.ans ?? q.correct_index ?? 0);
      const stem = String(q.q || q.question || '').replace(/^\[[^\]]*\]\s*/, '');
      if (opts.length < 2 || seen.has(stem.slice(0, 60))) continue;
      seen.add(stem.slice(0, 60));
      const origin = String(q.origin || q.origin_badge || (q._bank === 'medical' ? 'MAT Core' : 'DU Core'));
      out.push({
        id: q.id,
        stem,
        opts,
        ans,
        origin,
        track: classifyTrack(origin, q._bank),
        exp: q.exp || q.explanation,
        speedHack: q.speed_hack,
        trap: q.trap_alert || q.trap,
      });
    }
    return out;
  }, [typeId, chapterId, typeName]);

  // 2. Pull 2-3 2026 High-Yield Predictors for this type
  const predictorList: NormalizedQ[] = useMemo(() => {
    const chapters = (synthPredictors as any).chapters || [];
    const ch = chapters.find((c: any) => c.chapter_id === chapterId);
    if (!ch || !Array.isArray(ch.predictors)) return [];
    const tNum = typeName.match(/Type\s*(\d+)/i)?.[1];
    let items = tNum
      ? ch.predictors.filter((p: any) => String(p.type_ref || '').includes(`Type ${tNum}`))
      : [];
    if (items.length === 0) {
      // deterministic slice of 3 predictors for this typeId
      const hash = typeId.split('').reduce((a, c) => a + c.charCodeAt(0), 0);
      const start = hash % Math.max(1, ch.predictors.length - 2);
      items = ch.predictors.slice(start, start + 3);
    }
    return items.slice(0, 3).map((p: any, i: number) => ({
      id: p.id || `${typeId}_pred_${i}`,
      stem: String(p.stem || ''),
      opts: toOpts(p.options),
      ans: Number(p.answer ?? 0),
      origin: "2026 Predictor • DU/MAT/Engg Pattern",
      track: i % 3 === 1 ? 'medical' : i % 3 === 2 ? 'engineering' : 'varsity',
      exp: p.explanation,
      speedHack: p.speed_hack,
      trap: p.trap_alert,
    }));
  }, [typeId, typeName, chapterId]);

  const filteredPyqs = useMemo(
    () => (trackFilter === 'all' ? pyqList : pyqList.filter((q) => q.track === trackFilter)),
    [pyqList, trackFilter]
  );

  const filteredPredictors = useMemo(
    () => (trackFilter === 'all' ? predictorList : predictorList.filter((q) => q.track === trackFilter)),
    [predictorList, trackFilter]
  );

  const renderQuestionList = (list: NormalizedQ[], emptyMsg: string, badgeTone: string) => {
    if (list.length === 0) {
      return (
        <div className="p-4 rounded-xl border border-dashed border-slate-200 dark:border-slate-700 text-xs text-slate-500 dark:text-slate-400 text-center">
          {emptyMsg}
        </div>
      );
    }
    return (
      <div className="space-y-3">
        {list.map((q, idx) => {
          const picked = selectedOpt[q.id];
          const answered = picked !== undefined;
          return (
            <div
              key={q.id}
              className="rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/90 p-3 sm:p-3.5 space-y-2.5"
            >
              <div className="flex items-center justify-between gap-2 flex-wrap">
                <span className={`text-[10px] font-mono font-bold px-2 py-px rounded-md border ${badgeTone}`}>
                  #{idx + 1} • [{q.origin}]
                </span>
                <span className="text-[10px] font-bold px-2 py-px rounded-md border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300">
                  {q.track === 'medical' ? '🩺 MAT/DAT' : q.track === 'engineering' ? '⚙️ Engg Non-Calc' : "🎓 DU 'Ka'/Varsity"}
                </span>
              </div>

              <div className="text-xs sm:text-sm font-medium text-slate-900 dark:text-slate-100 leading-relaxed">
                <MathText content={q.stem} />
              </div>

              <div className="grid sm:grid-cols-2 gap-1.5">
                {q.opts.map((opt, oi) => {
                  const isCorrect = oi === q.ans;
                  const isPicked = picked === oi;
                  let cls =
                    'bg-slate-50 dark:bg-slate-800/70 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800';
                  if (answered) {
                    if (isCorrect) {
                      cls = 'bg-emerald-500/15 border-emerald-500 text-emerald-800 dark:text-emerald-300 font-bold';
                    } else if (isPicked) {
                      cls = 'bg-rose-500/15 border-rose-500 text-rose-800 dark:text-rose-300 font-bold';
                    }
                  }
                  return (
                    <button
                      key={oi}
                      onClick={() => setSelectedOpt((prev) => ({ ...prev, [q.id]: oi }))}
                      className={`text-left text-xs px-2.5 py-2 rounded-lg border flex items-center gap-2 transition-all cursor-pointer ${cls}`}
                    >
                      <span className="w-5 h-5 rounded-md bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-600 flex items-center justify-center text-[10px] font-bold shrink-0">
                        {String.fromCharCode(65 + oi)}
                      </span>
                      <span className="flex-1 overflow-x-auto no-scrollbar">
                        <MathText content={opt} />
                      </span>
                    </button>
                  );
                })}
              </div>

              {answered && (
                <div className="space-y-1.5 pt-1 border-t border-slate-100 dark:border-slate-800 text-[11px] animate-in fade-in duration-150">
                  {q.speedHack && (
                    <div className="p-2 rounded-lg bg-amber-500/10 border border-amber-500/25 text-amber-900 dark:text-amber-200">
                      <span className="font-bold mr-1">⚡ Speed Hack:</span>
                      <MathText content={q.speedHack} />
                    </div>
                  )}
                  {q.exp && (
                    <div className="p-2 rounded-lg bg-emerald-500/10 border border-emerald-500/25 text-slate-700 dark:text-slate-200">
                      <span className="font-bold text-emerald-700 dark:text-emerald-300 mr-1">✔ ব্যাখ্যা:</span>
                      <MathText content={q.exp} />
                    </div>
                  )}
                  {q.trap && (
                    <div className="p-2 rounded-lg bg-rose-500/10 border border-rose-500/25 text-rose-800 dark:text-rose-300 flex items-start gap-1.5">
                      <AlertTriangle className="w-3.5 h-3.5 shrink-0 mt-0.5" />
                      <div>
                        <span className="font-bold mr-1">Trap Alert:</span>
                        <MathText content={q.trap} />
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
    );
  };

  return (
    <div className="space-y-3 animate-in fade-in duration-150">
      {/* Sub-Tabs + Track Filter */}
      <div className="flex flex-wrap items-center justify-between gap-2 pb-2 border-b border-slate-200/70 dark:border-slate-800">
        <div className="flex flex-wrap items-center gap-1.5">
          <button
            onClick={() => setActiveTab('rule')}
            className={`px-2.5 py-1 rounded-lg text-[11px] font-bold flex items-center gap-1 border cursor-pointer transition-all ${
              activeTab === 'rule'
                ? 'bg-emerald-600 text-white border-emerald-600'
                : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700'
            }`}
          >
            <CheckCircle2 className="w-3 h-3" />
            <span>Core Rule & Hack</span>
          </button>
          <button
            onClick={() => setActiveTab('pyq')}
            className={`px-2.5 py-1 rounded-lg text-[11px] font-bold flex items-center gap-1 border cursor-pointer transition-all ${
              activeTab === 'pyq'
                ? 'bg-blue-600 text-white border-blue-600'
                : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700'
            }`}
          >
            <BookOpen className="w-3 h-3" />
            <span>PYQ Vault ({pyqList.length})</span>
          </button>
          <button
            onClick={() => setActiveTab('predictor')}
            className={`px-2.5 py-1 rounded-lg text-[11px] font-bold flex items-center gap-1 border cursor-pointer transition-all ${
              activeTab === 'predictor'
                ? 'bg-violet-600 text-white border-violet-600'
                : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700'
            }`}
          >
            <Sparkles className="w-3 h-3" />
            <span>2026 Predictor ({predictorList.length})</span>
          </button>
        </div>

        {activeTab !== 'rule' && (
          <div className="flex items-center gap-1 flex-wrap">
            {([
              ['all', 'সব ট্র্যাক'],
              ['varsity', "DU / Varsity"],
              ['medical', 'MAT / DAT'],
              ['engineering', 'Engg Non-Calc'],
            ] as [TrackFilter, string][]).map(([id, label]) => (
              <button
                key={id}
                onClick={() => setTrackFilter(id)}
                className={`px-2 py-0.5 rounded-md text-[10px] font-bold border cursor-pointer ${
                  trackFilter === id
                    ? 'bg-slate-900 dark:bg-white text-white dark:text-slate-900 border-slate-900 dark:border-white'
                    : 'bg-transparent text-slate-500 dark:text-slate-400 border-slate-200 dark:border-slate-700'
                }`}
              >
                {label}
              </button>
            ))}
          </div>
        )}
      </div>

      {activeTab === 'rule' && (
        <div className="space-y-2.5">
          {coreRule && (
            <div className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/25 space-y-1">
              <div className="text-[11px] font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                <span>কোর রুল ও ফান্ডামেন্টাল সূত্র (Core Rule):</span>
              </div>
              <div className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed pl-5 font-medium">
                <MathText content={coreRule} />
              </div>
            </div>
          )}

          {speedElimination && (
            <div className="p-3 rounded-xl bg-amber-500/10 border border-amber-500/25 space-y-1">
              <div className="text-[11px] font-bold text-amber-800 dark:text-amber-300 flex items-center gap-1.5">
                <Zap className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" />
                <span>৫-সেকেন্ড স্পিড এলিমিনেশন ট্রিক (Speed Elimination):</span>
              </div>
              <div className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed pl-5 font-medium">
                <MathText content={speedElimination} />
              </div>
            </div>
          )}

          {((pastTags && pastTags.length > 0) || (qbRefs && qbRefs.length > 0)) && (
            <div className="flex flex-wrap items-center gap-1.5 pt-0.5">
              {pastTags?.slice(0, 6).map((tag, i) => (
                <span key={`pt-${i}`} className="text-[10px] font-mono font-semibold px-2 py-px rounded-md border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300">
                  {tag}
                </span>
              ))}
              {qbRefs?.slice(0, 4).map((ref) => (
                <span key={ref} className="text-[10px] font-mono font-bold px-2 py-px rounded-md border border-blue-200 dark:border-blue-800 text-blue-700 dark:text-blue-300">
                  {ref}
                </span>
              ))}
            </div>
          )}
        </div>
      )}

      {activeTab === 'pyq' &&
        renderQuestionList(
          filteredPyqs,
          'এই ট্র্যাক ফিল্টারে কোনো বিগত প্রশ্ন নেই — "সব ট্র্যাক" নির্বাচন করে দেখুন।',
          'border-blue-300 dark:border-blue-800 text-blue-700 dark:text-blue-300'
        )}

      {activeTab === 'predictor' &&
        renderQuestionList(
          filteredPredictors,
          'এই ট্র্যাক ফিল্টারে কোনো ২০২৬ প্রেডিক্টর নেই — "সব ট্র্যাক" নির্বাচন করে দেখুন।',
          'border-violet-300 dark:border-violet-800 text-violet-700 dark:text-violet-300'
        )}
    </div>
  );
};
