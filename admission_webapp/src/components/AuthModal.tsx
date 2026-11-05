import React, { useState } from 'react';
import { 
  X, 
  Flame, 
  Sparkles, 
  CheckCircle2, 
  LogOut, 
  Mail, 
  ShieldCheck, 
  GraduationCap,
  Loader2,
  AlertCircle
} from 'lucide-react';
import type { UserProfile } from '../types';
import { loginWithGoogle } from '../lib/firebase';

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
  const [targetUnit, setTargetUnit] = useState<string>(user.target || "ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট");
  const [isLoggingIn, setIsLoggingIn] = useState(false);
  const [authError, setAuthError] = useState<string | null>(null);

  if (!isOpen) return null;

  const handleGoogleSignIn = async () => {
    setIsLoggingIn(true);
    setAuthError(null);
    try {
      const fbUser = await loginWithGoogle();
      const authenticProfile: Partial<UserProfile> = {
        name: fbUser.displayName || fbUser.email?.split('@')[0] || 'ভর্তিযোদ্ধা',
        email: fbUser.email || '',
        avatar: fbUser.photoURL || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(fbUser.email || 'student')}`,
        target: targetUnit,
        streakDays: user.streakDays > 0 ? user.streakDays : 1,
        solvedCount: user.solvedCount,
        accuracy: user.accuracy > 0 ? user.accuracy : 100,
        isLoggedIn: true,
      };
      onLogin(authenticProfile);
      onClose();
    } catch (err: unknown) {
      console.error('Firebase Google Sign-In error:', err);
      const errorObj = err as { code?: string; message?: string };
      if (errorObj?.code === 'auth/popup-closed-by-user') {
        setAuthError('লগইন পপ-আপ উইন্ডো বন্ধ করা হয়েছে। আবার চেষ্টা করুন।');
      } else if (errorObj?.code === 'auth/unauthorized-domain') {
        setAuthError('এই ডোমেনটি Firebase Console-এ Authorized Domains হিসেবে যোগ করা প্রয়োজন।');
      } else {
        setAuthError(errorObj?.message || 'Google সাইন ইন সম্পন্ন করা সম্ভব হয়নি। অনুগ্রহ করে ইন্টারনেট সংযোগ চেক করুন।');
      }
    } finally {
      setIsLoggingIn(false);
    }
  };

  const units = [
    "ঢাকা বিশ্ববিদ্যালয় 'ক' ইউনিট",
    "মেডিকেল (DMC Focus)",
    "BUET ও ইঞ্জিনিয়ারিং",
    "জিএসটি (GST) সমন্বিত গুচ্ছ"
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-none md:backdrop-blur-sm animate-in fade-in duration-200">
      <div 
        className="relative w-full max-w-md bg-white dark:bg-[#131E17] rounded-3xl shadow-2xl border border-slate-200/80 dark:border-[#1E2F24] overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Top Gradient Highlight */}
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
                    src={user.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(user.email || 'user')}`}
                    alt={user.name}
                    className="w-16 h-16 rounded-2xl object-cover ring-2 ring-[#056839] shadow-md"
                  />
                  <div className="absolute -bottom-1 -right-1 p-1 bg-[#056839] text-white rounded-full ring-2 ring-white dark:ring-[#131E17]">
                    <ShieldCheck className="w-3.5 h-3.5" />
                  </div>
                </div>
                <div className="overflow-hidden">
                  <h3 className="text-lg font-bold text-slate-900 dark:text-white truncate">
                    {user.name}
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 flex items-center gap-1 truncate">
                    <Mail className="w-3.5 h-3.5 shrink-0" /> {user.email}
                  </p>
                  <span className="inline-flex items-center gap-1 mt-1 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-[#056839]/10 text-[#056839] dark:text-emerald-400 border border-[#056839]/20 truncate">
                    <GraduationCap className="w-3 h-3 shrink-0" /> {user.target}
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
                  <span>Firebase ক্লাউড অথেনটিকেশন অ্যাক্টিভ</span>
                </div>
                <span className="font-mono text-[10px] bg-emerald-100 dark:bg-emerald-900/60 px-1.5 py-0.5 rounded text-emerald-700 dark:text-emerald-300">
                  Verified
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
                  className="py-2.5 px-4 bg-rose-50 hover:bg-rose-100 dark:bg-rose-950/40 dark:hover:bg-rose-900/40 text-rose-600 dark:text-rose-400 font-semibold rounded-xl text-sm transition-colors flex items-center gap-1.5 border border-rose-200 dark:border-rose-900/50"
                  title="সাইন আউট"
                >
                  <LogOut className="w-4 h-4" />
                  <span>লগআউট</span>
                </button>
              </div>
            </div>
          ) : (
            /* Google Sign In View */
            <div>
              {/* Top Motivation */}
              <div className="text-center mb-5">
                <div className="inline-flex items-center justify-center w-12 h-12 rounded-2xl bg-[#056839]/10 text-[#056839] dark:text-emerald-400 mb-2">
                  <Sparkles className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-extrabold text-slate-900 dark:text-white">
                  Google দিয়ে সাইন ইন করুন
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 max-w-xs mx-auto">
                  রিয়েলটাইম পরীক্ষার মার্কস, নেগেটিভ মার্কিং ট্র্যাকার এবং অ্যানালিটিক্স নিরাপদে ক্লাউডে সংরক্ষণ করুন।
                </p>
              </div>

              {/* Target Unit Selector */}
              <div className="mb-4">
                <label className="block text-[11px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-2">
                  আপনার টার্গেট নির্বাচন করুন:
                </label>
                <div className="grid grid-cols-2 gap-1.5">
                  {units.map((unit) => {
                    const isSelected = targetUnit === unit;
                    return (
                      <button
                        key={unit}
                        type="button"
                        onClick={() => setTargetUnit(unit)}
                        className={`p-2 rounded-xl text-xs font-semibold border text-left transition-all ${
                          isSelected
                            ? 'bg-[#056839] text-white border-[#056839] shadow-sm'
                            : 'bg-[#F6F8F6] dark:bg-[#17231B] text-slate-700 dark:text-slate-300 border-slate-200 dark:border-[#223328] hover:border-[#056839]/40'
                        }`}
                      >
                        {unit}
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Error Alert */}
              {authError && (
                <div className="mb-4 p-3 rounded-2xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/50 flex items-start gap-2.5 text-xs text-rose-700 dark:text-rose-300">
                  <AlertCircle className="w-4 h-4 shrink-0 mt-0.5 text-rose-500" />
                  <div className="flex-1">
                    <p className="font-semibold">{authError}</p>
                  </div>
                </div>
              )}

              {/* Primary Google Auth Button */}
              <button
                onClick={handleGoogleSignIn}
                disabled={isLoggingIn}
                className="w-full py-3.5 px-4 bg-white dark:bg-[#1A261F] hover:bg-slate-50 dark:hover:bg-[#223329] border border-slate-300 dark:border-[#2C4234] rounded-2xl font-bold text-slate-800 dark:text-white text-sm flex items-center justify-center gap-3 transition-all shadow-sm hover:shadow-md active:scale-[0.99] mb-4 group disabled:opacity-60"
              >
                {isLoggingIn ? (
                  <Loader2 className="w-5 h-5 animate-spin text-[#056839]" />
                ) : (
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
                )}
                <span className="font-['Outfit'] font-bold text-sm">
                  {isLoggingIn ? 'Google এ লগইন হচ্ছে...' : 'Continue with Google'}
                </span>
              </button>

              {/* Security Note */}
              <div className="pt-2 text-center">
                <p className="text-[11px] text-slate-400 dark:text-slate-500 flex items-center justify-center gap-1.5">
                  <ShieldCheck className="w-3.5 h-3.5 text-emerald-500" />
                  Firebase OAuth 2.0 • সরাসরি অফিসিয়াল Google একাউন্ট দিয়ে সুরক্ষিত
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
