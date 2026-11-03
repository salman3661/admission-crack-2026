import React from 'react';
import { 
  BarChart3, 
  Award, 
  Target, 
  CheckCircle2, 
  Clock, 
  Zap, 
  ArrowRight,
  Brain
} from 'lucide-react';
import type { AppMode, UserProfile } from '../types';

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
  const subjectsBreakdown = [
    { name: 'Physics', bn: 'পদার্থবিজ্ঞান', solved: 48, accuracy: 88, color: 'bg-cyan-500', bar: 'w-[88%]', status: 'Strong' },
    { name: 'Chemistry', bn: 'রসায়ন', solved: 52, accuracy: 92, color: 'bg-amber-500', bar: 'w-[92%]', status: 'Strong' },
    { name: 'Higher Math', bn: 'উচ্চতর গণিত', solved: 35, accuracy: 74, color: 'bg-rose-500', bar: 'w-[74%]', status: 'Focus Needed' },
    { name: 'Biology', bn: 'জীববিজ্ঞান', solved: 60, accuracy: 95, color: 'bg-emerald-500', bar: 'w-[95%]', status: 'Mastered' },
  ];

  const recentTests = [
    { title: 'Week 01 DU Ka মক টেস্ট', date: 'আজ, সকাল ৯:৩০', score: '২২.৭৫/২৫', accuracy: '৯১%', time: '২৮ সে/প্রশ্ন' },
    { title: 'মেডিকেল বায়োলজি স্পিড ড্রিল', date: 'গতকাল, রাত ১০:১৫', score: '১৮.৫০/২০', accuracy: '৯৩%', time: '১৮ সে/প্রশ্ন' },
    { title: 'ফিজিক্স ভেক্টর ও গতিবিদ্যা', date: '২ দিন আগে', score: '১৯.০০/২৫', accuracy: '৭৬%', time: '৪০ সে/প্রশ্ন' },
  ];

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-6 pb-24">
      {/* Top Header */}
      <div className="mb-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="p-1.5 rounded-xl bg-[#056839]/10 text-[#056839] dark:text-emerald-400">
              <BarChart3 className="w-5 h-5" />
            </span>
            <span className="text-xs font-bold text-[#056839] dark:text-emerald-400 uppercase tracking-wider">
              পার্সোনালাইজড পারফরম্যান্স মেট্রিক্স
            </span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
            অ্যাডমিশন অ্যানালিটিক্স ও মেরিট প্রেডিকশন
          </h1>
        </div>

        {/* User Card */}
        <div 
          onClick={onOpenAuth}
          className="cursor-pointer bg-white dark:bg-[#131E17] p-3 rounded-2xl border border-slate-200 dark:border-[#1E2F24] shadow-sm flex items-center gap-3 hover:scale-102 transition-transform self-start sm:self-auto"
        >
          <img
            src={user.avatar}
            alt={user.name}
            className="w-11 h-11 rounded-xl object-cover ring-2 ring-[#056839]"
          />
          <div>
            <div className="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
              {user.name}
              <span className="text-amber-500 font-mono text-[11px]">🔥 {user.streakDays}d</span>
            </div>
            <div className="text-[11px] text-[#056839] dark:text-emerald-400 font-semibold">
              {user.target}
            </div>
          </div>
        </div>
      </div>

      {/* Hero Stats Card */}
      <div className="bg-gradient-to-r from-[#056839] via-[#00B09B] to-[#96C93D] rounded-3xl p-6 text-white shadow-xl mb-6 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full blur-2xl pointer-events-none" />

        <div className="relative z-10 grid grid-cols-2 sm:grid-cols-4 gap-4">
          <div>
            <div className="text-white/80 text-xs font-semibold mb-1 flex items-center gap-1">
              <Award className="w-4 h-4" /> অনুমিত ঢাবি মেরিট
            </div>
            <div className="text-2xl sm:text-3xl font-black font-['Outfit']">
              #42 - #85
            </div>
            <div className="text-[11px] text-white/90 mt-0.5">টপ ১% রেঞ্জে আছো</div>
          </div>

          <div>
            <div className="text-white/80 text-xs font-semibold mb-1 flex items-center gap-1">
              <CheckCircle2 className="w-4 h-4" /> মোট সমাধান
            </div>
            <div className="text-2xl sm:text-3xl font-black font-['Outfit']">
              {user.solvedCount} টি
            </div>
            <div className="text-[11px] text-white/90 mt-0.5">MCQ প্র্যাকটিস সম্পন্ন</div>
          </div>

          <div>
            <div className="text-white/80 text-xs font-semibold mb-1 flex items-center gap-1">
              <Target className="w-4 h-4" /> সামগ্রিক নির্ভুলতা
            </div>
            <div className="text-2xl sm:text-3xl font-black font-['Outfit']">
              {user.accuracy}%
            </div>
            <div className="text-[11px] text-white/90 mt-0.5">টার্গেট: ৯০%+</div>
          </div>

          <div>
            <div className="text-white/80 text-xs font-semibold mb-1 flex items-center gap-1">
              <Clock className="w-4 h-4" /> গড় সময়
            </div>
            <div className="text-2xl sm:text-3xl font-black font-['Outfit']">
              ২৮.৫ সে
            </div>
            <div className="text-[11px] text-white/90 mt-0.5">টার্গেট: ৪৫ সেকেন্ড</div>
          </div>
        </div>
      </div>

      {/* Grid: Subject Breakdown & Recent Tests */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        
        {/* Subject Breakdown (2 Cols) */}
        <div className="lg:col-span-2 bg-white dark:bg-[#131E17] rounded-3xl p-6 border border-slate-200/80 dark:border-[#1E2F24] shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
              <Brain className="w-4 h-4 text-[#056839] dark:text-emerald-400" />
              বিষয়ভিত্তিক দক্ষতা বিশ্লেষণ
            </h2>
            <span className="text-xs text-slate-400">সর্বশেষ আপডেট: আজ</span>
          </div>

          <div className="space-y-4">
            {subjectsBreakdown.map((subj) => (
              <div key={subj.name} className="p-3.5 rounded-2xl bg-[#F6F8F6] dark:bg-[#1A261F] border border-slate-200/60 dark:border-[#24352A]">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center gap-2">
                    <span className="text-sm font-bold text-slate-900 dark:text-white">
                      {subj.bn}
                    </span>
                    <span className="text-xs text-slate-400 font-mono">({subj.name})</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full ${
                      subj.status === 'Mastered' ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300' :
                      subj.status === 'Strong' ? 'bg-cyan-100 text-cyan-700 dark:bg-cyan-950/60 dark:text-cyan-300' :
                      'bg-rose-100 text-rose-700 dark:bg-rose-950/60 dark:text-rose-300'
                    }`}>
                      {subj.status}
                    </span>
                    <span className="text-sm font-extrabold text-slate-900 dark:text-white">
                      {subj.accuracy}%
                    </span>
                  </div>
                </div>

                {/* Progress bar */}
                <div className="w-full h-2.5 bg-slate-200 dark:bg-slate-700/60 rounded-full overflow-hidden">
                  <div className={`h-full ${subj.color} ${subj.bar} rounded-full transition-all duration-500`} />
                </div>
                <div className="flex justify-between items-center text-[11px] text-slate-500 dark:text-slate-400 mt-1.5">
                  <span>সমাধান: {subj.solved} টি প্রশ্ন</span>
                  <span>{subj.accuracy < 80 ? '⚠️ শর্টকাট রিভিশন দরকার' : '✓ লক্ষ্যমাত্রায় আছে'}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Right Col: Recent Tests & Vault Callout */}
        <div className="space-y-6">
          {/* Recent Mock Tests Card */}
          <div className="bg-white dark:bg-[#131E17] rounded-3xl p-5 border border-slate-200/80 dark:border-[#1E2F24] shadow-sm">
            <h3 className="text-sm font-bold text-slate-900 dark:text-white mb-3 flex items-center gap-2">
              <Clock className="w-4 h-4 text-emerald-600" />
              সাম্প্রতিক মক টেস্ট
            </h3>

            <div className="space-y-2.5">
              {recentTests.map((t, idx) => (
                <div key={idx} className="p-3 rounded-2xl bg-[#F6F8F6] dark:bg-[#1A261F] border border-slate-200/60 dark:border-[#24352A]">
                  <div className="text-xs font-bold text-slate-900 dark:text-white mb-0.5">
                    {t.title}
                  </div>
                  <div className="text-[11px] text-slate-400 mb-1.5">{t.date}</div>
                  <div className="flex items-center justify-between text-xs font-semibold">
                    <span className="text-[#056839] dark:text-emerald-400 font-mono">
                      স্কোর: {t.score}
                    </span>
                    <span className="text-slate-500 dark:text-slate-400 text-[11px]">
                      {t.time}
                    </span>
                  </div>
                </div>
              ))}
            </div>

            <button
              onClick={() => onSelectMode('exam')}
              className="w-full mt-3 py-2 bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold rounded-xl transition-colors shadow-sm"
            >
              নতুন মক টেস্ট দিন
            </button>
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
            <h4 className="text-sm font-extrabold text-slate-900 dark:text-white mb-1">
              উচ্চতর গণিত ও ফিজিক্সের ট্র্যাপ এড়াতে চাও?
            </h4>
            <p className="text-xs text-slate-600 dark:text-slate-400 mb-3 leading-relaxed">
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
