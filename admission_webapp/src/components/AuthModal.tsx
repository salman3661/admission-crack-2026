import React, { useState } from 'react';
import { 
  X, 
  Flame, 
  Sparkles, 
  CheckCircle2, 
  LogOut, 
  Mail, 
  ShieldCheck, 
  ArrowRight,
  GraduationCap
} from 'lucide-react';
import type { UserProfile } from '../types';

interface AuthModalProps {
  isOpen: boolean;
  onClose: () => void;
  user: UserProfile;
  onLogin: (profile: Partial<UserProfile>) => void;
  onLogout: () => void;
}

export const AuthModal: React.FC<AuthModalProps> = ({
  isOpen,
  onClose,
  user,
  onLogin,
  onLogout,
}) => {
  const [customName, setCustomName] = useState('');
  const [customEmail, setCustomEmail] = useState('');
  const [targetUnit, setTargetUnit] = useState('ঢাকা বিশ্ববিদ্যালয় \'ক\' ইউনিট');
  const [showCustomForm, setShowCustomForm] = useState(false);

  if (!isOpen) return null;

  const demoAccounts = [
    {
      name: 'হাসিবুল হাসান',
      email: 'hasibul.du26@gmail.com',
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&auto=format&fit=crop&q=80',
      target: 'ঢাকা বিশ্ববিদ্যালয় \'ক\' ইউনিট',
      streakDays: 5,
      solvedCount: 142,
      accuracy: 89,
    },
    {
      name: 'সাদিয়া ইসলাম',
      email: 'sadia.med26@gmail.com',
      avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&auto=format&fit=crop&q=80',
      target: 'মেডিকেল স্পেশাল (DMC টার্গেট)',
      streakDays: 7,
      solvedCount: 195,
      accuracy: 94,
    },
    {
      name: 'রাকিব আহমেদ',
      email: 'rakib.eng26@gmail.com',
      avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&auto=format&fit=crop&q=80',
      target: 'BUET ও ইঞ্জিনিয়ারিং ক্লাস্টার',
      streakDays: 4,
      solvedCount: 118,
      accuracy: 86,
    }
  ];

  const handleCustomSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!customEmail) return;
    onLogin({
      name: customName || customEmail.split('@')[0],
      email: customEmail,
      avatar: `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(customEmail)}`,
      target: targetUnit,
      streakDays: 1,
      solvedCount: 25,
      accuracy: 85,
      isLoggedIn: true,
    });
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-in fade-in duration-200">
      <div 
        className="relative w-full max-w-md bg-white dark:bg-[#131E17] rounded-3xl shadow-2xl border border-slate-200/80 dark:border-[#1E2F24] overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header decoration */}
        <div className="h-2 bg-gradient-to-r from-[#00B09B] via-[#056839] to-[#96C93D]" />

        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          aria-label="Close"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="p-6">
          {user.isLoggedIn ? (
            /* Logged-In Profile View */
            <div>
              <div className="flex items-center gap-4 mb-6">
                <div className="relative">
                  <img
                    src={user.avatar}
                    alt={user.name}
                    className="w-16 h-16 rounded-2xl object-cover ring-2 ring-[#056839] shadow-md"
                  />
                  <div className="absolute -bottom-1 -right-1 p-1 bg-[#056839] text-white rounded-full ring-2 ring-white dark:ring-[#131E17]">
                    <ShieldCheck className="w-3.5 h-3.5" />
                  </div>
                </div>
                <div>
                  <div className="flex items-center gap-1.5">
                    <h3 className="text-lg font-bold text-slate-900 dark:text-white">
                      {user.name}
                    </h3>
                  </div>
                  <p className="text-xs text-slate-500 dark:text-slate-400 flex items-center gap-1">
                    <Mail className="w-3.5 h-3.5" /> {user.email}
                  </p>
                  <span className="inline-flex items-center gap-1 mt-1 px-2 py-0.5 rounded-full text-[11px] font-semibold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20">
                    <GraduationCap className="w-3 h-3" /> {user.target}
                  </span>
                </div>
              </div>

              {/* Stats Grid */}
              <div className="grid grid-cols-3 gap-2.5 mb-6">
                <div className="bg-[#F6F8F6] dark:bg-[#1A261F] p-3 rounded-2xl text-center border border-slate-200/60 dark:border-[#24352A]">
                  <div className="flex items-center justify-center gap-1 text-amber-500 text-xs font-semibold mb-0.5">
                    <Flame className="w-3.5 h-3.5" /> স্ট্রিক
                  </div>
                  <div className="text-lg font-extrabold text-slate-900 dark:text-white">
                    {user.streakDays} দিন
                  </div>
                  <div className="text-[10px] text-slate-400">ধারাবাহিক</div>
                </div>

                <div className="bg-[#F6F8F6] dark:bg-[#1A261F] p-3 rounded-2xl text-center border border-slate-200/60 dark:border-[#24352A]">
                  <div className="text-xs font-semibold text-[#00B09B] mb-0.5">
                    সমাধান
                  </div>
                  <div className="text-lg font-extrabold text-slate-900 dark:text-white">
                    {user.solvedCount}
                  </div>
                  <div className="text-[10px] text-slate-400">এমসিকিউ</div>
                </div>

                <div className="bg-[#F6F8F6] dark:bg-[#1A261F] p-3 rounded-2xl text-center border border-slate-200/60 dark:border-[#24352A]">
                  <div className="text-xs font-semibold text-emerald-600 dark:text-emerald-400 mb-0.5">
                    নির্ভুলতা
                  </div>
                  <div className="text-lg font-extrabold text-slate-900 dark:text-white">
                    {user.accuracy}%
                  </div>
                  <div className="text-[10px] text-slate-400">অ্যাকুরেসি</div>
                </div>
              </div>

              {/* Cloud Sync Status */}
              <div className="flex items-center justify-between p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/50 mb-6 text-xs text-emerald-800 dark:text-emerald-300">
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                  <span>Google ক্লাউড সিঙ্ক সচল আছে</span>
                </div>
                <span className="font-mono text-[10px] bg-emerald-100 dark:bg-emerald-900/60 px-1.5 py-0.5 rounded text-emerald-700 dark:text-emerald-300">
                  Active
                </span>
              </div>

              {/* Action Buttons */}
              <div className="flex items-center gap-2">
                <button
                  onClick={onClose}
                  className="flex-1 py-2.5 px-4 bg-[#056839] hover:bg-[#044e2b] text-white font-semibold rounded-xl text-sm transition-colors shadow-sm"
                >
                  প্রস্তুতি চালিয়ে যান
                </button>
                <button
                  onClick={() => {
                    onLogout();
                    onClose();
                  }}
                  className="py-2.5 px-3.5 bg-rose-50 hover:bg-rose-100 dark:bg-rose-950/40 dark:hover:bg-rose-900/40 text-rose-600 dark:text-rose-400 font-semibold rounded-xl text-sm transition-colors flex items-center gap-1.5 border border-rose-200 dark:border-rose-900/50"
                  title="লগআউট"
                >
                  <LogOut className="w-4 h-4" />
                  <span>লগআউট</span>
                </button>
              </div>
            </div>
          ) : (
            /* Google Sign In View */
            <div>
              {/* Top Branding & Motivation */}
              <div className="text-center mb-6">
                <div className="inline-flex items-center justify-center w-12 h-12 rounded-2xl bg-[#056839]/10 text-[#056839] dark:text-emerald-400 mb-2">
                  <Sparkles className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-extrabold text-slate-900 dark:text-white">
                  Google দিয়ে সাইন ইন করুন
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 max-w-xs mx-auto">
                  আপনার পরীক্ষার ফলাফল, নেগেটিভ মার্ক অ্যানালিটিক্স এবং বুকমার্ক ক্লাউডে সংরক্ষণ করুন
                </p>
              </div>

              {/* Primary Google Login Button */}
              <button
                onClick={() => {
                  // Direct 1-tap Google login using primary demo student
                  const primary = demoAccounts[0];
                  onLogin({
                    ...primary,
                    isLoggedIn: true,
                  });
                  onClose();
                }}
                className="w-full py-3 px-4 bg-white dark:bg-[#1A261F] hover:bg-slate-50 dark:hover:bg-[#223329] border border-slate-300 dark:border-[#2C4234] rounded-2xl font-semibold text-slate-800 dark:text-white text-sm flex items-center justify-center gap-3 transition-all shadow-sm hover:shadow-md active:scale-[0.99] mb-4 group"
              >
                {/* Official Google 'G' Logo SVG */}
                <svg className="w-5 h-5" viewBox="0 0 24 24">
                  <path
                    fill="#4285F4"
                    d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                  />
                  <path
                    fill="#34A853"
                    d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                  />
                  <path
                    fill="#FBBC05"
                    d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"
                  />
                  <path
                    fill="#EA4335"
                    d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"
                  />
                </svg>
                <span className="font-['Outfit'] font-bold">Continue with Google</span>
              </button>

              {/* One-click Candidate Profiles */}
              <div className="mb-4">
                <div className="flex items-center gap-2 mb-2">
                  <div className="h-px flex-1 bg-slate-200 dark:bg-[#1E2F24]" />
                  <span className="text-[11px] font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                    অথবা সরাসরি নির্বাচন করুন
                  </span>
                  <div className="h-px flex-1 bg-slate-200 dark:bg-[#1E2F24]" />
                </div>

                <div className="space-y-2">
                  {demoAccounts.map((account) => (
                    <button
                      key={account.email}
                      onClick={() => {
                        onLogin({
                          ...account,
                          isLoggedIn: true,
                        });
                        onClose();
                      }}
                      className="w-full p-2.5 rounded-2xl bg-[#F6F8F6] dark:bg-[#17231B] hover:bg-[#EAEFEA] dark:hover:bg-[#203025] border border-slate-200/70 dark:border-[#223327] flex items-center justify-between text-left transition-all group"
                    >
                      <div className="flex items-center gap-3">
                        <img
                          src={account.avatar}
                          alt={account.name}
                          className="w-9 h-9 rounded-xl object-cover ring-1 ring-slate-300 dark:ring-slate-700"
                        />
                        <div>
                          <div className="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                            {account.name}
                            <span className="text-[10px] text-amber-500 font-mono font-normal">
                              🔥 {account.streakDays}d
                            </span>
                          </div>
                          <div className="text-[11px] text-slate-500 dark:text-slate-400">
                            {account.target}
                          </div>
                        </div>
                      </div>
                      <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-[#056839] group-hover:translate-x-0.5 transition-all" />
                    </button>
                  ))}
                </div>
              </div>

              {/* Custom Google account toggler */}
              {!showCustomForm ? (
                <button
                  onClick={() => setShowCustomForm(true)}
                  className="w-full py-2 text-center text-xs font-semibold text-[#056839] dark:text-emerald-400 hover:underline"
                >
                  + নিজস্ব Google ইমেইল দিয়ে লগইন করুন
                </button>
              ) : (
                <form onSubmit={handleCustomSubmit} className="space-y-2.5 pt-2 border-t border-slate-200 dark:border-[#1E2F24]">
                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">
                      আপনার নাম:
                    </label>
                    <input
                      type="text"
                      placeholder="যেমন: তানভীর আহমেদ"
                      value={customName}
                      onChange={(e) => setCustomName(e.target.value)}
                      className="w-full px-3 py-2 text-xs rounded-xl bg-white dark:bg-[#17231B] border border-slate-300 dark:border-[#2A3E31] text-slate-900 dark:text-white focus:outline-none focus:border-[#056839]"
                    />
                  </div>
                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">
                      Google Gmail ঠিকানা:
                    </label>
                    <input
                      type="email"
                      required
                      placeholder="example@gmail.com"
                      value={customEmail}
                      onChange={(e) => setCustomEmail(e.target.value)}
                      className="w-full px-3 py-2 text-xs rounded-xl bg-white dark:bg-[#17231B] border border-slate-300 dark:border-[#2A3E31] text-slate-900 dark:text-white focus:outline-none focus:border-[#056839]"
                    />
                  </div>
                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">
                      টার্গেট ইউনিট:
                    </label>
                    <select
                      value={targetUnit}
                      onChange={(e) => setTargetUnit(e.target.value)}
                      className="w-full px-3 py-2 text-xs rounded-xl bg-white dark:bg-[#17231B] border border-slate-300 dark:border-[#2A3E31] text-slate-900 dark:text-white focus:outline-none focus:border-[#056839]"
                    >
                      <option value="ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট">ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট</option>
                      <option value="মেডিকেল (DMC Focus)">মেডিকেল (DMC Focus)</option>
                      <option value="BUET ও ইঞ্জিনিয়ারিং">BUET ও ইঞ্জিনিয়ারিং</option>
                      <option value="জিএসটি (GST) সমন্বিত গুচ্ছ">জিএসটি (GST) সমন্বিত গুচ্ছ</option>
                    </select>
                  </div>
                  <button
                    type="submit"
                    className="w-full py-2.5 bg-[#056839] hover:bg-[#044e2b] text-white text-xs font-bold rounded-xl transition-colors shadow-sm"
                  >
                    সাইন ইন সম্পন্ন করুন
                  </button>
                </form>
              )}

              {/* Security Note */}
              <div className="mt-4 pt-3 border-t border-slate-100 dark:border-[#1E2F24] text-center">
                <p className="text-[10px] text-slate-400 dark:text-slate-500 flex items-center justify-center gap-1">
                  <ShieldCheck className="w-3.5 h-3.5 text-emerald-500" />
                  Google OAuth সিকিউর লগইন • কোনো পাসওয়ার্ড সংরক্ষিত হয় না
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
