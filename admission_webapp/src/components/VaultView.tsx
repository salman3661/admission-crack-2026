import React, { useState } from 'react';
import { 
  Search, 
  Copy, 
  Check, 
  ShieldAlert, 
  Sparkles, 
  X,
  Triangle,
  Beaker,
  Bookmark
} from 'lucide-react';
import type { VaultData, SubjectType, WeekFilterType } from '../types';
import { MathText } from './MathText';

interface VaultViewProps {
  vault: VaultData;
  selectedWeek?: WeekFilterType;
  selectedSubject?: SubjectType;
}

export const VaultView: React.FC<VaultViewProps> = ({ 
  vault, 
  selectedWeek = 'all', 
  selectedSubject = 'All' 
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState<'all' | 'traps' | 'triplets' | 'quick_math' | 'fractions' | 'patterns'>('all');
  const [copiedText, setCopiedText] = useState<string | null>(null);

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedText(text);
    setTimeout(() => setCopiedText(null), 2000);
  };

  const q = searchQuery.toLowerCase().trim();

  // Filtered collections respecting selected week, subject & search
  const filteredTriplets = vault.triplets.filter((t) => 
    (!q || t.sides.toLowerCase().includes(q) || t.result.toLowerCase().includes(q) || t.app.toLowerCase().includes(q))
  );

  const filteredQuickMath = vault.quick_math.filter((m) =>
    (!q || m.type.toLowerCase().includes(q) || m.item.toLowerCase().includes(q))
  );

  const filteredFractions = vault.magic_fractions.filter((f) =>
    (selectedSubject === 'All' || selectedSubject === 'Chemistry') &&
    (!q || f.compound.toLowerCase().includes(q) || f.mw.toLowerCase().includes(q) || f.trick.toLowerCase().includes(q))
  );

  const filteredPatterns = vault.patterns.filter((p) => {
    const matchWeek = selectedWeek === 'all' || p.week === selectedWeek;
    const matchSubject = selectedSubject === 'All' || p.subject === selectedSubject;
    const matchQuery = !q || p.code.toLowerCase().includes(q) || p.title.toLowerCase().includes(q) || p.formula.toLowerCase().includes(q);
    return matchWeek && matchSubject && matchQuery;
  });

  const filteredTraps = vault.traps.filter((tr) => {
    const matchWeek = selectedWeek === 'all' || tr.week === selectedWeek;
    const matchSubject = selectedSubject === 'All' || tr.subject === selectedSubject;
    const matchQuery = !q || tr.trap.toLowerCase().includes(q) || tr.fix.toLowerCase().includes(q);
    return matchWeek && matchSubject && matchQuery;
  });

  const tabs: { id: typeof activeTab; label: string; count: number }[] = [
    { id: 'all', label: 'সব রিসোর্স', count: filteredTraps.length + filteredPatterns.length + filteredTriplets.length + filteredQuickMath.length + filteredFractions.length },
    { id: 'traps', label: '🚨 ক্রস-সাবজেক্ট ট্র্যাপ', count: filteredTraps.length },
    { id: 'triplets', label: '📐 গোল্ডেন ট্রিপলেট', count: filteredTriplets.length },
    { id: 'quick_math', label: '⚡ রুট ও লগ শর্টকাট', count: filteredQuickMath.length },
    { id: 'fractions', label: '🧪 স্টয়কিওমেট্রি ফ্র্যাকশন', count: filteredFractions.length },
    { id: 'patterns', label: '📌 ফর্মুলা প্যাটার্ন', count: filteredPatterns.length },
  ];

  return (
    <div className="max-w-4xl mx-auto py-4 px-3 sm:px-4">
      
      {/* Top Search & Filter Bar */}
      <div className="mb-4">
        <div className="flex items-center gap-2 mb-3">
          <div className="relative flex-1">
            <Search className="w-4 h-4 text-zinc-400 absolute left-3.5 top-3 pointer-events-none" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="সূত্র, ধ্রুবক, মৌল বা ফাঁদ খুঁজুন..."
              className="w-full bg-white dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 rounded-xl pl-10 pr-9 py-2 text-xs sm:text-sm text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-[#056839] transition-all shadow-sm"
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-3 top-2.5 text-zinc-400 hover:text-zinc-700 dark:hover:text-white"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>
        </div>

        {/* Sub-Tabs with no-scrollbar */}
        <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-1">
          {tabs.map((tab) => {
            const isActive = activeTab === tab.id;
            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all whitespace-nowrap shrink-0 shadow-sm ${
                  isActive
                    ? 'bg-[#056839] text-white scale-[1.02]'
                    : 'bg-white dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 border border-zinc-200/80 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                }`}
              >
                <span>{tab.label}</span>
                <span className={`text-[10px] font-mono px-1.5 py-0.2 rounded-full font-bold ${
                  isActive ? 'bg-white/20 text-white' : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-500'
                }`}>
                  {tab.count}
                </span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Content Area */}
      <div className="space-y-6">
        
        {/* Traps First (Highest Priority for Avoidance) */}
        {(activeTab === 'all' || activeTab === 'traps') && filteredTraps.length > 0 && (
          <div>
            <div className="flex items-center gap-1.5 mb-2.5">
              <ShieldAlert className="w-4 h-4 text-rose-600 dark:text-rose-400" />
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white">
                ক্রস-সাবজেক্ট ট্র্যাপ ব্রেকার ({filteredTraps.length}টি)
              </h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {filteredTraps.map((item) => (
                <div 
                  key={item.id}
                  className="bg-white dark:bg-zinc-900 rounded-2xl p-4 border border-zinc-200/80 dark:border-zinc-800 shadow-sm flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-[11px] font-mono font-bold px-2 py-0.5 rounded-full bg-rose-500/10 text-rose-700 dark:text-rose-400 border border-rose-500/20">
                        ট্র্যাপ #{item.id}
                      </span>
                      <span className="text-[11px] font-semibold text-zinc-500">
                        {item.subject} • {item.week.toUpperCase()}
                      </span>
                    </div>

                    <div className="bg-rose-50/70 dark:bg-rose-950/20 p-2.5 rounded-xl border border-rose-200/60 dark:border-rose-900/30 mb-2 text-xs text-rose-900 dark:text-rose-200 overflow-x-auto no-scrollbar">
                      <strong className="text-rose-700 dark:text-rose-400 block mb-0.5 font-bold">পরীক্ষার ফাঁদ:</strong>
                      <MathText content={item.trap} />
                    </div>

                    <div className="bg-emerald-50/70 dark:bg-emerald-950/20 p-2.5 rounded-xl border border-emerald-200/60 dark:border-emerald-900/30 text-xs text-emerald-900 dark:text-emerald-200 overflow-x-auto no-scrollbar">
                      <strong className="text-emerald-700 dark:text-emerald-400 block mb-0.5 font-bold">সঠিক সতর্কতা (The Fix):</strong>
                      <MathText content={item.fix} />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Golden Triplets */}
        {(activeTab === 'all' || activeTab === 'triplets') && filteredTriplets.length > 0 && (
          <div>
            <div className="flex items-center gap-1.5 mb-2.5">
              <Triangle className="w-4 h-4 text-cyan-600 dark:text-cyan-400" />
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white">
                গোল্ডেন পিথাগোরিয়ান ও ভেক্টর ট্রিপলেট
              </h3>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5">
              {filteredTriplets.map((item, idx) => (
                <div 
                  key={idx}
                  className="bg-white dark:bg-zinc-900 rounded-2xl p-3.5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-1.5">
                      <span className="font-mono font-bold text-xs text-cyan-700 dark:text-cyan-400">
                        {item.sides}
                      </span>
                      <span className="px-2 py-0.5 rounded-full bg-cyan-50 dark:bg-cyan-950/30 text-cyan-700 dark:text-cyan-400 border border-cyan-200 dark:border-cyan-800/40 text-[11px] font-mono font-bold">
                        মান: {item.result}
                      </span>
                    </div>
                    <div className="text-xs text-zinc-600 dark:text-zinc-400 leading-relaxed overflow-x-auto no-scrollbar">
                      <MathText content={item.app} />
                    </div>
                  </div>
                  <button
                    onClick={() => copyToClipboard(item.result)}
                    className="mt-2.5 pt-1.5 border-t border-zinc-100 dark:border-zinc-800 flex items-center justify-end gap-1 text-[11px] text-zinc-400 hover:text-cyan-600 transition-colors"
                  >
                    {copiedText === item.result ? (
                      <span className="flex items-center gap-1 text-emerald-600"><Check className="w-3 h-3" /> কপি হয়েছে</span>
                    ) : (
                      <span className="flex items-center gap-1"><Copy className="w-3 h-3" /> কপি মান</span>
                    )}
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Quick Math & Roots */}
        {(activeTab === 'all' || activeTab === 'quick_math') && filteredQuickMath.length > 0 && (
          <div>
            <div className="flex items-center gap-1.5 mb-2.5">
              <Sparkles className="w-4 h-4 text-amber-500" />
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white">
                রুট, লগ, pH ও অমসৃণ বর্গমূল শর্টকাট
              </h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
              {filteredQuickMath.map((item, idx) => (
                <div 
                  key={idx}
                  className="bg-white dark:bg-zinc-900 rounded-2xl p-3.5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm flex items-start justify-between gap-3"
                >
                  <div className="flex-1 overflow-x-auto no-scrollbar">
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-700 dark:text-amber-400 border border-amber-500/20 mb-1.5 inline-block">
                      {item.type}
                    </span>
                    <div className="text-xs sm:text-sm font-medium text-zinc-800 dark:text-zinc-200">
                      <MathText content={item.item} />
                    </div>
                  </div>
                  <button
                    onClick={() => copyToClipboard(item.item)}
                    className="p-1.5 rounded-xl bg-zinc-100 dark:bg-zinc-800 text-zinc-500 hover:text-zinc-900 dark:hover:text-white transition-all shrink-0"
                    title="কপি"
                  >
                    {copiedText === item.item ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5" />}
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Magic Fractions */}
        {(activeTab === 'all' || activeTab === 'fractions') && filteredFractions.length > 0 && (
          <div>
            <div className="flex items-center gap-1.5 mb-2.5">
              <Beaker className="w-4 h-4 text-emerald-600" />
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white">
                রসায়ন স্টয়কিওমেট্রি ম্যাজিক ফ্র্যাকশন
              </h3>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5">
              {filteredFractions.map((item, idx) => (
                <div 
                  key={idx}
                  className="bg-white dark:bg-zinc-900 rounded-2xl p-3.5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-1.5">
                      <span className="font-bold text-xs text-emerald-700 dark:text-emerald-400">
                        <MathText content={item.compound} />
                      </span>
                      <span className="text-[11px] font-mono px-2 py-0.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-300">
                        M = {item.mw}
                      </span>
                    </div>
                    <div className="text-xs text-zinc-600 dark:text-zinc-400 leading-relaxed overflow-x-auto no-scrollbar">
                      <MathText content={item.trick} />
                    </div>
                  </div>
                  <button
                    onClick={() => copyToClipboard(item.trick)}
                    className="mt-2.5 pt-1.5 border-t border-zinc-100 dark:border-zinc-800 flex items-center justify-end gap-1 text-[11px] text-zinc-400 hover:text-emerald-600 transition-colors"
                  >
                    {copiedText === item.trick ? (
                      <span className="flex items-center gap-1 text-emerald-600"><Check className="w-3 h-3" /> কপি হয়েছে</span>
                    ) : (
                      <span className="flex items-center gap-1"><Copy className="w-3 h-3" /> কপি হ্যাক</span>
                    )}
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Formula Patterns */}
        {(activeTab === 'all' || activeTab === 'patterns') && filteredPatterns.length > 0 && (
          <div>
            <div className="flex items-center gap-1.5 mb-2.5">
              <Bookmark className="w-4 h-4 text-indigo-600" />
              <h3 className="text-sm font-bold text-zinc-900 dark:text-white">
                হাই-ইল্ড রিপিট ফর্মুলা প্যাটার্ন
              </h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
              {filteredPatterns.map((item, idx) => (
                <div 
                  key={idx}
                  className="bg-white dark:bg-zinc-900 rounded-2xl p-3.5 border border-zinc-200/80 dark:border-zinc-800 shadow-sm flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-1.5">
                      <span className="font-mono text-[10px] font-bold px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-700 dark:text-indigo-400 border border-indigo-500/20">
                        {item.code}
                      </span>
                      <span className="text-[11px] font-semibold text-zinc-400">
                        {item.subject} • {item.week.toUpperCase()}
                      </span>
                    </div>
                    <h4 className="text-xs font-bold text-zinc-900 dark:text-white mb-1">
                      {item.title}
                    </h4>
                    <div className="text-xs text-zinc-700 dark:text-zinc-300 bg-zinc-50 dark:bg-zinc-800/60 p-2.5 rounded-xl border border-zinc-200/60 dark:border-zinc-700/60 overflow-x-auto no-scrollbar">
                      <MathText content={item.formula} />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

      </div>
    </div>
  );
};
