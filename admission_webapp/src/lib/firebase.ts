import { initializeApp, getApps, getApp } from "firebase/app";
import { getAnalytics, isSupported } from "firebase/analytics";
import { 
  getAuth, 
  GoogleAuthProvider, 
  signInWithPopup, 
  signOut,
  onAuthStateChanged,
  type User 
} from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBXWuUwwDeAo1zKBjWywEz8524FI6yONjo",
  authDomain: "admission-crack-2026.firebaseapp.com",
  projectId: "admission-crack-2026",
  storageBucket: "admission-crack-2026.firebasestorage.app",
  messagingSenderId: "431061478062",
  appId: "1:431061478062:web:32234c17b820acaa335b3f",
  measurementId: "G-DEPPSGSMVS"
};

// Initialize Firebase app safely
export const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApp();

// Analytics is initialized if supported in the current environment
export let analytics: ReturnType<typeof getAnalytics> | null = null;
if (typeof window !== "undefined") {
  isSupported().then((supported) => {
    if (supported) {
      analytics = getAnalytics(app);
    }
  }).catch(() => {
    // Analytics unavailable or blocked by browser shields
  });
}

// Authentication setup
export const auth = getAuth(app);
export const googleProvider = new GoogleAuthProvider();
googleProvider.setCustomParameters({ prompt: "select_account" });

/**
 * Sign in using Firebase Google Popup Auth
 */
export async function loginWithGoogle() {
  const result = await signInWithPopup(auth, googleProvider);
  return result.user;
}

/**
 * Sign out from Firebase
 */
export async function logoutFirebase() {
  await signOut(auth);
}

export { onAuthStateChanged, type User };

