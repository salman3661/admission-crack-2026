import React, { useState, useEffect } from 'react';
import { 
  BarChart3, 
  Award, 
  Target, 
  CheckCircle2, 
  Clock, 
  Zap, 
  ArrowRight,
  Brain,
  RotateCcw,
  Sparkles,
  HelpCircle
} from 'lucide-react';
import type { AppMode, UserProfile } from '../types';
import { getExamHistory, computeAggregateStats, clearExamHistory, type ExamAttemptRecord } from '../lib/analytics';

interface AnalyticsViewProps {
  user: UserProfile;
  onOpenAuth: () => void;
  onSelectMode: (mode: AppMode) => void;
}

export const AnalyticsView: React.FC<AnalyticsViewProps> = ({
  user,
  onOpenAuth,
  onSelectMode,
}) => {
  const [history, setHistory] = useState<ExamAttemptRecord[]>([]);

  useEffect(() => {
    setHistory(getExamHistory());
  }, []);

  const stats = computeAggregateStats(history);
  const isZeroState = stats.attemptedCount === 0;

  const handleResetHistory = () => {
    if (window.confirm('আপনি কি নিশ্চিত যে আপনার সমস্ত টেস্ট হিস্ট্রি রিসেট করতে চান?')) {
      clearExamHistory();
      setHistory([]);
    }
  };

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-6 pb-28">
      {/* Top Header */}
      <div className="mb-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="p-1.5 rounded-xl bg-[#056839]/10 text-[#056839] dark:text-emerald-400">
              <BarChart3 className="w-5 h-5" />
            </span>
            <span className="text-xs font-bold text-[#056839] dark:text-emerald-400 uppercase tracking-wider">
              লাইভ পারফরম্যান্স ও মেরিট ট্র্যাকার
            </span>
          </div>
          <h1 className="text-xl sm:text-2xl md:text-3xl font-extrabold text-zinc-900 dark:text-white">
            অ্যাডমিশন অ্যানালিটিক্স ও মেরিট প্রেডিকশন
          </h1>
        </div>

        {/* User Card */}
        <div 
          onClick={onOpenAuth}
          className="cursor-pointer bg-white dark:bg-zinc-900 p-2.5 sm:p-3 rounded-2xl border border-zinc-200/80 dark:border-zinc-800 shadow-sm flex items-center gap-3 hover:scale-102 transition-transform self-start sm:self-auto"
        >
          <img
            src={user.avatar}
            alt={user.name}
            className="w-10 h-10 rounded-xl object-cover ring-2 ring-[#056839]"
          />
          <div>
            <div className="text-xs font-bold text-zinc-900 dark:text-white flex items-center gap-1.5">
              {user.name}
              <span className="text-amber-500 font-mono text-[11px]">🔥 {user.streakDays}d</span>
            </div>
            <div className="text-[11px] text-[#056839] dark:text-emerald-400 font-semibold">
              {user.target}
            </div>
          </div>
        </div>
      </div>

      {/* Hero Stats Card - Vibrant Chorcha Green Gradient */}
      <div className="bg-gradient-to-r from-[#056839] via-[#00B09B] to-[#96C93D] rounded-3xl p-5 sm:p-6 text-white shadow-xl mb-6 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full blur-2xl pointer-events-none" />

        <div className="relative z-10 grid grid-cols-2 sm:grid-cols-4 gap-4">
          {/* Predicted Merit */}
          <div className="p-3 rounded-2xl bg-white/10 backdrop-blur-sm border border-white/15">
            <div className="text-white/80 text-xs font-semibold mb-1 flex items-center gap-1">
              <Award className="w-4 h-4" /> অনুমিত ঢাবি মেরিট
            </div>
            <div className="text-lg sm:text-2xl font-black font-['Outfit']">
              {stats.predictedRank}
            </div>
            <div className="text-[11px] text-white/90 mt-0.5">
              {isZeroState ? 'কমপক্ষে ১টি টেস্ট প্রয়োজন' : `মোট ${stats.attemptedCount}টি টেস্টের ভিত্তিতে`}
            </div>
          </div>

          {/* Solved Count */}
          <div className="p-3 rounded-2xl bg-white/10 backdrop-blur-sm border border-white/15">
            <div className="text-white/80 text-xs font-semibold mb-1 flex items-center gap-1">
              <CheckCircle2 className="w-4 h-4" /> মোট সমাধান
            </div>
            <div className="text-2xl sm:text-3xl font-black font-['Outfit']">
              {stats.totalSolved}
            </div>
            <div className="text-[11px] text-white/90 mt-0.5">MCQ প্র্যাকটিস সম্পন্ন</div>
          </div>

          {/* Overall Accuracy */}
          <div className="p-3 rounded-2xl bg-white/10 backdrop-blur-sm border border-white/15">
            <div className="text-white/80 text-xs font-semibold mb-1 flex items-center gap-1">
              <Target className="w-4 h-4" /> সার্বিক নির্ভুলতা
            </div>
            <div className="text-2xl sm:text-3xl font-black font-['Outfit']">
              {stats.overallAccuracy}
            </div>
            <div className="text-[11px] text-white/90 mt-0.5">টার্গেট: ৯০%+</div>
          </div>

          {/* Average Time */}
          <div className="p-3 rounded-2xl bg-white/10 backdrop-blur-sm border border-white/15">
            <div className="text-white/80 text-xs font-semibold mb-1 flex items-center gap-1">
              <Clock className="w-4 h-4" /> গড় সময়
            </div>
            <div className="text-2xl sm:text-3xl font-black font-['Outfit']">
              {stats.avgTime}
            </div>
            <div className="text-[11px] text-white/90 mt-0.5">টার্গেট: ৪৫ সেকেন্ড</div>
          </div>
        </div>
      </div>

      {/* Zero State Alert Banner if no attempts */}
      {isZeroState && (
        <div className="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm mb-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 rounded-2xl bg-emerald-50 dark:bg-emerald-950/40 text-[#056839] dark:text-emerald-400 flex items-center justify-center flex-shrink-0">
              <Sparkles className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white">
                এখনও কোনো মডেল টেস্ট সম্পন্ন হয়নি
              </h3>
              <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-0.5">
                মডেল টেস্ট সম্পন্ন করলে আপনার নির্ভুলতা, সময় এবং অনুমিত মেরিট র্যাংক রিয়েল-টাইমে গণনা হবে।
              </p>
            </div>
          </div>
          <button
            onClick={() => onSelectMode('exam')}
            className="flex-shrink-0 inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#056839] hover:bg-[#044e2b] text-white font-bold text-xs shadow-md shadow-[#056839]/20 transition-all hover:scale-105 active:scale-95"
          >
            <span>প্রথম মডেল টেস্ট দিন</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      )}

      {/* Grid: Subject Breakdown & Recent Tests */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        
        {/* Subject Breakdown (2 Cols) */}
        <div className="lg:col-span-2 bg-white dark:bg-zinc-900 rounded-3xl p-5 sm:p-6 border border-zinc-200/80 dark:border-zinc-800 shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-sm sm:text-base font-bold text-zinc-900 dark:text-white flex items-center gap-2">
              <Brain className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
              বিষয়ভিত্তিক দক্ষতা বিশ্লেষণ
            </h2>
            <span className="text-xs text-zinc-400">
              {isZeroState ? 'পরীক্ষার অপেক্ষা' : 'লাইভ হিস্ট্রি'}
            </span>
          </div>

          <div className="space-y-3.5">
            {stats.subjects.map((subj) => (
              <div key={subj.name} className="p-3.5 rounded-2xl bg-[#F6F8F6] dark:bg-zinc-800/60 border border-zinc-200/60 dark:border-zinc-800">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center gap-2">
                    <span className="text-xs sm:text-sm font-bold text-zinc-900 dark:text-white">
                      {subj.bn}
                    </span>
                    <span className="text-xs text-zinc-400 font-mono">({subj.name})</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full ${
                      subj.status === 'Mastered' ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300' :
                      subj.status === 'Strong' ? 'bg-cyan-100 text-cyan-700 dark:bg-cyan-950/60 dark:text-cyan-300' :
                      subj.status === 'Focus Needed' ? 'bg-rose-100 text-rose-700 dark:bg-rose-950/60 dark:text-rose-300' :
                      'bg-zinc-100 text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400'
                    }`}>
                      {subj.status}
                    </span>
                    <span className="text-xs sm:text-sm font-extrabold text-zinc-900 dark:text-white font-mono">
                      {subj.solved === 0 ? '০%' : `${subj.accuracy}%`}
                    </span>
                  </div>
                </div>

                {/* Progress bar */}
                <div className="w-full h-2 bg-zinc-200 dark:bg-zinc-700/60 rounded-full overflow-hidden">
                  <div 
                    className={`h-full ${subj.color} rounded-full transition-all duration-500`}
                    style={{ width: `${subj.solved === 0 ? 0 : subj.accuracy}%` }}
                  />
                </div>
                <div className="flex justify-between items-center text-[11px] text-zinc-500 dark:text-zinc-400 mt-1.5">
                  <span>সমাধান: {subj.solved} টি প্রশ্ন</span>
                  <span>
                    {subj.solved === 0 
                      ? 'অংশগ্রহণ বাকি' 
                      : subj.accuracy < 70 
                      ? '⚠️ শর্টকাট রিভিশন দরকার' 
                      : '✓ লক্ষ্যমাত্রায় আছে'}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Right Col: Recent Tests & Vault Callout */}
        <div className="space-y-6">
          {/* Recent Mock Tests Card */}
          <div className="bg-white dark:bg-zinc-900 rounded-3xl p-5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm">
            <div className="flex items-center justify-between mb-3">
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white flex items-center gap-2">
                <Clock className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
                সাম্প্রতিক মক টেস্ট
              </h3>
              {!isZeroState && (
                <button
                  onClick={handleResetHistory}
                  title="হিস্ট্রি রিসেট করুন"
                  className="p-1 rounded-lg hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-400 hover:text-rose-500 transition-colors"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                </button>
              )}
            </div>

            {isZeroState ? (
              <div className="p-4 rounded-2xl bg-[#F6F8F6] dark:bg-zinc-800/60 border border-zinc-200/60 dark:border-zinc-800 text-center py-6">
                <HelpCircle className="w-8 h-8 text-zinc-300 dark:text-zinc-600 mx-auto mb-2" />
                <p className="text-xs text-zinc-500 dark:text-zinc-400 font-medium">
                  এখনও কোনো টেস্ট রেকর্ড নেই
                </p>
                <button
                  onClick={() => onSelectMode('exam')}
                  className="mt-3 px-4 py-1.5 bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold rounded-xl transition-colors shadow-sm"
                >
                  টেস্ট শুরু করুন
                </button>
              </div>
            ) : (
              <div className="space-y-2.5">
                {stats.recentTests.map((t, idx) => (
                  <div key={idx} className="p-3 rounded-2xl bg-[#F6F8F6] dark:bg-zinc-800/60 border border-zinc-200/60 dark:border-zinc-800">
                    <div className="text-xs font-bold text-zinc-900 dark:text-white mb-0.5">
                      {t.title}
                    </div>
                    <div className="text-[11px] text-zinc-400 mb-1.5">{t.date}</div>
                    <div className="flex items-center justify-between text-xs font-semibold">
                      <span className="text-[#056839] dark:text-emerald-400 font-mono">
                        স্কোর: {t.score}
                      </span>
                      <span className="text-zinc-500 dark:text-zinc-400 text-[11px]">
                        নির্ভুলতা: {t.accuracy} • {t.time}
                      </span>
                    </div>
                  </div>
                ))}

                <button
                  onClick={() => onSelectMode('exam')}
                  className="w-full mt-3 py-2 bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold rounded-xl transition-colors shadow-sm"
                >
                  নতুন মক টেস্ট দিন
                </button>
              </div>
            )}
          </div>

          {/* Trap & Shortcut Vault Callout */}
          <div 
            onClick={() => onSelectMode('vault')}
            className="p-5 rounded-3xl bg-amber-500/10 dark:bg-amber-950/20 border border-amber-500/30 hover:border-amber-500/60 cursor-pointer transition-all hover:scale-102 group"
          >
            <div className="flex items-center gap-2 text-amber-700 dark:text-amber-300 font-bold text-xs mb-1">
              <Zap className="w-4 h-4 text-amber-500 fill-current" />
              ক্যালকুলেটর-বিহীন ভল্ট
            </div>
            <h4 className="text-sm font-extrabold text-zinc-900 dark:text-white mb-1">
              উচ্চতর গণিত ও ফিজিক্সের ট্র্যাপ এড়াতে চাও?
            </h4>
            <p className="text-xs text-zinc-600 dark:text-zinc-400 mb-3 leading-relaxed">
              গোল্ডেন ট্রিপলেট, স্টয়কিওমেট্রি টেবিল এবং বিগত ২০ বছরের ট্র্যাপ চিটশীট এক ক্লিকে দেখো।
            </p>
            <div className="flex items-center gap-1 text-xs font-bold text-amber-600 dark:text-amber-400 group-hover:translate-x-1 transition-transform">
              <span>ভল্ট খুলুন</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};
