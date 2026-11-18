import React from 'react';
import { Home } from 'lucide-react';
import { useSEO } from '../lib/seo';

interface NotFoundViewProps {
  onGoHome: () => void;
}

export const NotFoundView: React.FC<NotFoundViewProps> = ({ onGoHome }) => {
  useSEO({
    title: '404 — পাতা পাওয়া যায়নি | Admission Crack 2026',
    description: 'এই পাতাটি খুঁজে পাওয়া যায়নি। হোম পেজে ফিরে যান।',
    path: '/404',
  });

  return (
    <div className="max-w-lg mx-auto px-4 py-20 text-center">
      <div className="text-6xl font-black text-emerald-600 mb-3">৪০৪</div>
      <h1 className="text-xl font-extrabold text-slate-900 dark:text-white mb-2">পাতাটি খুঁজে পাওয়া যায়নি</h1>
      <p className="text-sm text-slate-500 mb-6">তুমি যে লিংকে এসেছো সেটি সঠিক নয় বা সরানো হয়েছে।</p>
      <button
        onClick={onGoHome}
        className="px-5 py-2.5 rounded-2xl bg-emerald-600 text-white text-xs font-bold inline-flex items-center gap-2 cursor-pointer"
      >
        <Home className="w-4 h-4" /> হোম ডেকে ফিরে যাও
      </button>
    </div>
  );
};
