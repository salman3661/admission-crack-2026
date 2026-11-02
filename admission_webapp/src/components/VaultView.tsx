import React, { useState } from 'react';
import { 
  Zap, 
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
import type { VaultData } from '../types';
import { MathText } from './MathText';

interface VaultViewProps {
  vault: VaultData;
}

export const VaultView: React.FC<VaultViewProps> = ({ vault }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState<'all' | 'triplets' | 'quick_math' | 'fractions' | 'patterns' | 'traps'>('all');
  const [copiedText, setCopiedText] = useState<string | null>(null);

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedText(text);
    setTimeout(() => setCopiedText(null), 2000);
  };

  const q = searchQuery.toLowerCase().trim();

  // Filtered collections
  const filteredTriplets = vault.triplets.filter((t) => 
    !q || t.sides.toLowerCase().includes(q) || t.result.toLowerCase().includes(q) || t.app.toLowerCase().includes(q)
  );

  const filteredQuickMath = vault.quick_math.filter((m) =>
    !q || m.type.toLowerCase().includes(q) || m.item.toLowerCase().includes(q)
  );

  const filteredFractions = vault.magic_fractions.filter((f) =>
    !q || f.compound.toLowerCase().includes(q) || f.mw.toLowerCase().includes(q) || f.trick.toLowerCase().includes(q)
  );

  const filteredPatterns = vault.patterns.filter((p) =>
    !q || p.code.toLowerCase().includes(q) || p.title.toLowerCase().includes(q) || p.formula.toLowerCase().includes(q) || p.subject.toLowerCase().includes(q)
  );

  const filteredTraps = vault.traps.filter((tr) =>
    !q || tr.trap.toLowerCase().includes(q) || tr.fix.toLowerCase().includes(q) || tr.subject.toLowerCase().includes(q)
  );

  const tabs: { id: typeof activeTab; label: string; count: number }[] = [
    { id: 'all', label: 'সব ভল্ট রিসোর্স', count: vault.triplets.length + vault.quick_math.length + vault.magic_fractions.length + vault.patterns.length + vault.traps.length },
    { id: 'triplets', label: '📐 গোল্ডেন ট্রিপলেট', count: vault.triplets.length },
    { id: 'quick_math', label: '⚡ রুট ও লগ শর্টকাট', count: vault.quick_math.length },
    { id: 'fractions', label: '🧪 স্টয়কিওমেট্রি ফ্র্যাকশন', count: vault.magic_fractions.length },
    { id: 'patterns', label: '📌 ফর্মুলা প্যাটার্ন', count: vault.patterns.length },
    { id: 'traps', label: '🚨 ক্রস-সাবজেক্ট ট্র্যাপ', count: vault.traps.length },
  ];

  return (
    <div className="max-w-6xl mx-auto py-8 px-4">
      {/* Header */}
      <div className="text-center max-w-2xl mx-auto mb-8">
        <div className="inline-flex p-2.5 rounded-2xl bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20 mb-3 shadow-sm">
          <Zap className="w-6 h-6" />
        </div>
        <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white tracking-tight">
          গ্লোবাল ক্যালকুলেটর-বিহীন ভল্ট
        </h2>
        <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-2">
          ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট ও মেডিকেল পরীক্ষায় ক্যালকুলেটর ছাড়া ৫-১০ সেকেন্ডে সমাধানের শর্টকাট ও ২৪টি রেড অ্যালার্ট ট্র্যাপ চিটশীট।
        </p>

        {/* Search Bar */}
        <div className="relative mt-6 max-w-md mx-auto">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5 pointer-events-none" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="যেকোনো সূত্র, ধ্রুবক, মৌল বা ফাঁদ খুঁজুন..."
            className="w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl pl-10 pr-10 py-2.5 text-sm text-slate-900 dark:text-white placeholder-slate-400 dark:placeholder-slate-500 focus:outline-none focus:border-brand-500 transition-all shadow-sm"
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery('')}
              className="absolute right-3.5 top-3 text-slate-400 hover:text-slate-700 dark:hover:text-white"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* Tabs */}
      <div className="flex items-center justify-center gap-1.5 overflow-x-auto pb-4 mb-6 scrollbar-none border-b border-slate-200 dark:border-slate-800">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all whitespace-nowrap border ${
              activeTab === tab.id
                ? 'bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white border-brand-500/50 shadow-sm'
                : 'bg-white dark:bg-slate-900/60 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/40 hover:text-slate-900 dark:hover:text-slate-200'
            }`}
          >
            <span>{tab.label}</span>
            <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-slate-100 dark:bg-slate-900 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-700">
              {tab.count}
            </span>
          </button>
        ))}
      </div>

      {/* Content Grid */}
      <div className="space-y-8">
        {/* Section 1: Golden Triplets */}
        {(activeTab === 'all' || activeTab === 'triplets') && filteredTriplets.length > 0 && (
          <div>
            <div className="flex items-center gap-2 mb-3">
              <Triangle className="w-4 h-4 text-cyan-600 dark:text-cyan-400" />
              <h3 className="text-base font-bold text-cyan-800 dark:text-cyan-300">
                <MathText content="গোল্ডেন পিথাগোরিয়ান ও ভেক্টর ট্রিপলেট ($\sqrt{a^2+b^2}$ বা $\sqrt{x^2+y^2+z^2}$)" />
              </h3>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
              {filteredTriplets.map((item, idx) => (
                <div 
                  key={idx}
                  className="bg-white dark:bg-slate-900/90 rounded-2xl p-4 border border-cyan-200 dark:border-cyan-500/20 hover:border-cyan-400 dark:hover:border-cyan-500/40 shadow-sm transition-all flex flex-col justify-between group"
                >
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span className="font-mono font-bold text-sm text-cyan-800 dark:text-cyan-300">
                        {item.sides}
                      </span>
                      <span className="px-2 py-0.5 rounded-md bg-cyan-50 dark:bg-cyan-500/10 text-cyan-700 dark:text-cyan-400 border border-cyan-200 dark:border-cyan-500/20 text-xs font-mono font-bold">
                        মান: {item.result}
                      </span>
                    </div>
                    <div className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">
                      <MathText content={item.app} />
                    </div>
                  </div>
                  <button
                    onClick={() => copyToClipboard(item.result)}
                    className="mt-3 pt-2 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-end gap-1 text-[11px] text-slate-500 hover:text-cyan-600 dark:hover:text-cyan-400 transition-colors"
                  >
                    {copiedText === item.result ? (
                      <span className="flex items-center gap-1 text-emerald-600 dark:text-emerald-400"><Check className="w-3 h-3" /> কপি করা হয়েছে</span>
                    ) : (
                      <span className="flex items-center gap-1"><Copy className="w-3 h-3" /> কপি মান</span>
                    )}
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Section 2: Quick Math & Roots */}
        {(activeTab === 'all' || activeTab === 'quick_math') && filteredQuickMath.length > 0 && (
          <div>
            <div className="flex items-center gap-2 mb-3">
              <Sparkles className="w-4 h-4 text-amber-500 dark:text-amber-400" />
              <h3 className="text-base font-bold text-amber-800 dark:text-amber-300">
                রুট, লগ, pH ও অমসৃণ বর্গমূল শর্টকাট
              </h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {filteredQuickMath.map((item, idx) => (
                <div 
                  key={idx}
                  className="bg-white dark:bg-slate-900/90 rounded-2xl p-4 border border-amber-200 dark:border-amber-500/20 hover:border-amber-400 dark:hover:border-amber-500/40 shadow-sm transition-all flex items-start justify-between gap-3"
                >
                  <div className="flex-1">
                    <span className="text-xs font-bold px-2 py-0.5 rounded bg-amber-50 dark:bg-amber-500/10 text-amber-800 dark:text-amber-300 border border-amber-200 dark:border-amber-500/20 mb-2 inline-block">
                      {item.type}
                    </span>
                    <div className="text-sm font-medium text-slate-800 dark:text-slate-200">
                      <MathText content={item.item} />
                    </div>
                  </div>
                  <button
                    onClick={() => copyToClipboard(item.item)}
                    className="p-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-all flex-shrink-0"
                    title="কপি করুন"
                  >
                    {copiedText === item.item ? <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Section 3: Stoichiometry Magic Fractions */}
        {(activeTab === 'all' || activeTab === 'fractions') && filteredFractions.length > 0 && (
          <div>
            <div className="flex items-center gap-2 mb-3">
              <Beaker className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
              <h3 className="text-base font-bold text-emerald-800 dark:text-emerald-300">
                রসায়ন স্টয়কিওমেট্রি "ম্যাজিক ফ্র্যাকশন" (Magic Fractions)
              </h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
              {filteredFractions.map((item, idx) => (
                <div 
                  key={idx}
                  className="bg-white dark:bg-slate-900/90 rounded-2xl p-4 border border-emerald-200 dark:border-emerald-500/20 hover:border-emerald-400 dark:hover:border-emerald-500/40 shadow-sm transition-all flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span className="font-bold text-sm text-emerald-800 dark:text-emerald-300">
                        <MathText content={item.compound} />
                      </span>
                      <span className="text-xs font-mono px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                        M = {item.mw}
                      </span>
                    </div>
                    <div className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">
                      <MathText content={item.trick} />
                    </div>
                  </div>
                  <button
                    onClick={() => copyToClipboard(item.trick)}
                    className="mt-3 pt-2 border-t border-slate-100 dark:border-slate-800 flex items-center justify-end gap-1 text-[11px] text-slate-500 hover:text-emerald-600 dark:hover:text-emerald-400 transition-colors"
                  >
                    {copiedText === item.trick ? (
                      <span className="flex items-center gap-1 text-emerald-600 dark:text-emerald-400"><Check className="w-3 h-3" /> কপি হয়েছে</span>
                    ) : (
                      <span className="flex items-center gap-1"><Copy className="w-3 h-3" /> কপি হ্যাক</span>
                    )}
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Section 4: Recurring Formula Patterns */}
        {(activeTab === 'all' || activeTab === 'patterns') && filteredPatterns.length > 0 && (
          <div>
            <div className="flex items-center gap-2 mb-3">
              <Bookmark className="w-4 h-4 text-indigo-600 dark:text-indigo-400" />
              <h3 className="text-base font-bold text-indigo-800 dark:text-indigo-300">
                হাই-ইল্ড রিপিট ফর্মুলা প্যাটার্ন (Recurring Patterns)
              </h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {filteredPatterns.map((item, idx) => (
                <div 
                  key={idx}
                  className="bg-white dark:bg-slate-900/90 rounded-2xl p-4 border border-indigo-200 dark:border-indigo-500/20 hover:border-indigo-400 dark:hover:border-indigo-500/40 shadow-sm transition-all flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-indigo-50 dark:bg-indigo-500/15 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-500/20">
                        {item.code}
                      </span>
                      <div className="flex items-center gap-1.5">
                        <span className="text-[11px] font-semibold text-slate-500 dark:text-slate-400">
                          {item.subject}
                        </span>
                        <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-700">
                          {item.week.toUpperCase()}
                        </span>
                      </div>
                    </div>
                    <h4 className="text-sm font-bold text-slate-900 dark:text-white mb-1.5">
                      {item.title}
                    </h4>
                    <div className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed bg-slate-50 dark:bg-slate-950/60 p-2.5 rounded-xl border border-slate-200 dark:border-slate-800/80">
                      <MathText content={item.formula} />
                    </div>
                  </div>
                  <div className="mt-3 flex justify-end">
                    <button
                      onClick={() => copyToClipboard(item.formula)}
                      className="text-[11px] text-slate-500 hover:text-indigo-600 dark:hover:text-indigo-400 flex items-center gap-1 transition-colors"
                    >
                      {copiedText === item.formula ? <Check className="w-3 h-3 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3 h-3" />} সূত্র কপি
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Section 5: Cross-Subject Traps */}
        {(activeTab === 'all' || activeTab === 'traps') && filteredTraps.length > 0 && (
          <div>
            <div className="flex items-center gap-2 mb-3">
              <ShieldAlert className="w-4 h-4 text-rose-600 dark:text-rose-400" />
              <h3 className="text-base font-bold text-rose-800 dark:text-rose-300">
                ২৪টি ক্রস-সাবজেক্ট ট্র্যাপ ব্রেকার ম্যাট্রিক্স (The Trap & The Fix)
              </h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {filteredTraps.map((item) => (
                <div 
                  key={item.id}
                  className="bg-white dark:bg-slate-900/90 rounded-2xl p-4 border border-rose-200 dark:border-rose-500/20 hover:border-rose-400 dark:hover:border-rose-500/40 shadow-sm transition-all flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-rose-50 dark:bg-rose-500/10 text-rose-700 dark:text-rose-400 border border-rose-200 dark:border-rose-500/20">
                        ট্র্যাপ #{item.id}
                      </span>
                      <span className="text-xs font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                        {item.subject} • {item.week.toUpperCase()}
                      </span>
                    </div>

                    {/* Trap */}
                    <div className="bg-rose-50 dark:bg-rose-500/10 p-2.5 rounded-xl border border-rose-200 dark:border-rose-500/20 mb-2.5 text-xs text-rose-900 dark:text-rose-200">
                      <strong className="text-rose-700 dark:text-rose-400 block mb-0.5 font-bold">পরীক্ষার ফাঁদ:</strong>
                      {item.trap}
                    </div>

                    {/* Fix */}
                    <div className="bg-emerald-50 dark:bg-emerald-500/10 p-2.5 rounded-xl border border-emerald-200 dark:border-emerald-500/20 text-xs text-emerald-900 dark:text-emerald-200">
                      <strong className="text-emerald-700 dark:text-emerald-400 block mb-0.5 font-bold">সঠিক সতর্কতা (The Fix):</strong>
                      <MathText content={item.fix} />
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
