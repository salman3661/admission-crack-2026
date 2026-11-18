# 06 — ROUND 2 SPEC: ডেটা ফিক্স + ৫টি নতুন ফিচার

> **কার জন্য:** AI coding agent (rebuild করছে `admission_webapp`)
> **কেন এখন:** Round 1 rebuild শেষ, কিন্তু live audit-এ ৩টি ভাঙা জিনিস পাওয়া গেছে
> আর ইউজার ৫টি নতুন ফিচার চেয়েছে।
> **গুরুত্ব:** এই ডকুমেন্টটি `docs/00-MASTER-PROMPT.md`-এর সাথে পড়ো — এটা সেটার সম্প্রসারণ।

---

# PART A — যা ভাঙা আছে (live audit, ১৮ নভে ২০২৬)

Audit method: deployed `assets/library-*.js` ও `assets/index-*.js` পড়া + browser-এ প্রতিটি
route চালিয়ে গণনা করা। অনুমান কোনোটিই নেই — সব সংখ্যা measured।

## A1. 🔴 Week-by-week drill ভাঙা (সবচেয়ে বড় সমস্যা)

**Symptom:** `/weekly` ও home-এর Week 01–09 ট্যাবে ৮টি সপ্তাহে **০টি প্রশ্ন** দেখায়।
শুধু Week 08-এ ৬২টি দেখায় (আর সেটাও ভুল — আসলে ১২০)।

**Root cause:** `library.ts`-এর week filter এভাবে কাজ করছে —

```ts
// ❌ বর্তমান (ভাঙা)
if (e.week && e.week !== 'all') {
  const t = e.week.replace('week_', '');
  const n = RegExp(`Week\\s*0?${parseInt(t, 10)}\\b`, 'i');
  r = r.filter(q => n.test(q.source_name));
}
```

অথচ data-তে `source_name` "Week 06" নয় — এভাবে আছে:
`Weekly 06 Varsity (Udvash) W-06 Set-A`, `W-07 Weekly Exam Set-A Q18`,
`W-03 Weekly Exam Set-A Q12`, `Week 08 Solve Sheet - Daily B-08`

regex-এ `Week` শব্দের পরে সরাসরি সংখ্যা চাই, কিন্তু data-তে `Weekly`, `W-06`, `Bio-06`
আসে → **মিলে ০**।

**প্রমাণ (deployed `index.json`-এ app নিজেই লিখে রেখেছে):**

```json
"by_week": { "week_08": 62 }
```

**আসল ডেটা (সবগুলো আছে, মাত্র filter ভুল):**

```
Week 01 → 100    Week 04 → 96     Week 07 → 84
Week 02 → 100    Week 05 → 96     Week 08 → 120
Week 03 → 180    Week 06 → 216    Week 09 → 76
                                  মোট = 1,068
```

**Fix (দুই জায়গায়):**

```ts
// ✅ সঠিক — id-prefix authoritative, source_name শুধু fallback
export function questionWeek(q: Question): number | null {
  const m = /^w(\d)(?:_|\b)/i.exec(q.id);
  if (m) return parseInt(m[1], 10);
  const s = /(?:^|[\s\-/])(?:week[\s\-]*0?(\d)|w[\-\s]?0?(\d)|[\w]0(\d)\b)/i.exec(q.source_name || '');
  if (s) {
    const n = parseInt(s[1] || s[2] || s[3], 10);
    if (n >= 1 && n <= 9) return n;
  }
  return null;
}

// filter-এ
if (e.week && e.week !== 'all') {
  const w = parseInt(e.week.replace('week_', ''), 10);
  r = r.filter(q => questionWeek(q) === w);
}
```

**সাথে `prepare-data.mjs`-এ প্রতিটি row-তে `week` field যোগ করো** (id-prefix থেকে):

```js
const wm = /^w(\d)(?:_|\b)/i.exec(q.id);
q.week = wm ? parseInt(wm[1], 10) : null;
```

তাহলে UI আর কোনো regex guess করবে না — `q.week` সরাসরি পড়বে।

**Regression guard:** `index.json`-এর `by_week` এখন হওয়া উচিত:
`{week_01:100, week_02:100, week_03:180, week_04:96, week_05:96, week_06:216, week_07:84, week_08:120, week_09:76}`

---

## A2. 🔴 ১৪৮টি duplicate প্রশ্ন এখনো আছে

`validate-data.mjs` যেটা warn করছে সেটা real: **id-dedup text-dedup করেনি।**

```
unique id  : 1,442
unique text: 1,294      ← ১৪৮টি অতিরিক্ত কপি
```

গ্রুপের গঠন:

```
৯৬টি গ্রুপ → w6/weekly_solve + w6/weekly_solve
               (Week 06 Set-A আর Set-B = একই paper, শুধু নাম আলাদা)
৩০টি গ্রুপ → med/past_paper + qb/past_paper   (Medical QB + Varsity QB)
২২টি গ্রুপ → qb/past_paper + var/past_paper
```

cross-week duplicate: **০** — তাই একটা week drill-এ একই প্রশ্ন দুইবার আসে না,
কিন্তু **একই drill-এর ভেতরে** (Week 06-এ) আসে।

**Fix:** `prepare-data.mjs`-এ dedup-এর key বদলাও — id-র বদলে normalized text:

```js
const norm = s => String(s || '').replace(/\s+/g, ' ').trim().toLowerCase().slice(0, 140);
// dedup key = norm(question)   ← id নয়
```

**কিন্তু দ্রুত বানাও না** — dup সরালে unique 1,442 → 1,294 (‑১০%)। মানে
master set ও backtest-এর সংখ্যা বদলাবে। তাই:

```bash
node scripts/validate-data.mjs src/data/bank
node scripts/build-master-set.mjs
node scripts/coverage-scorer.cjs src/data/master/du_ka_set_a.json
node scripts/coverage-scorer.cjs src/data/master/mat_set_a.json
```

**Master set-এর composition বদলাবে না** (set-এর প্রশ্ন select করা হয়, বাকিগুলো
বাদ দিলেও selection pool যথেষ্ট বড়) — কিন্তু সংখ্যা যাচাই করো।
`coverage-scorer` 60/60 ও 100/100 REAL-PAST থাকলে ঠিক আছে।

**Duplicate সরানোর আগে source-টা merge করো** — একটা প্রশ্নের দুইটা copy থাকলে
যেটাতে বেশি metadata (explanation/trap/source_name) সেটাই রাখো, `source_name`-এ
দুইটোই লেখো (`appears_in` array)।

---

## A3. 🟡 `other` exam-এ ভুল লেবেলকৃত DU weekly solve (৯৭টি)

```
Weekly 06 Varsity (Udvash) W-06 Set-A/B/C/D
Weekly 06 Varsity (Udvash) Daily Bio/C/M/P-06
Speed Hack 2026
→ এগুলো exam='du_ka' হওয়া উচিত, 'other' নয়
```

`prepare-data.mjs`-এ source_name-এর pattern ধরে relabel করো:

```js
const isDuWeekly = /weekly\s*0\d\s*varsity|speed hack|weekly exam W-0\d|W-0\d daily/i;
if (isDuWeekly.test(q.source_name) && q.exam === 'other') q.exam = 'du_ka';
```

ফলে `/weekly`-তে 4টি ফাইল/405 প্রশ্নের বদলে **সব weekly solve** দেখাবে।

**সতর্কতা:** `exam` বদলালে du_ka pool বাড়বে (844 → ~940)। Master set আবার বানাও
ও coverage re-check করো। যদি 60/60 বা 100/100 ভাঙে → ফেরত ফেরত।

---

## A4. 🟡 Topic-wise (mega_type) drill নেই

`mega_type` field আছে (**২৫৩টি unique topic**) কিন্তু কোনো UI-তে filter নেই।
নিচে F21-এ এটা যোগ করছি।

---

# PART B — ৫টি নতুন ফিচার

## F17. 🎯 Practice-Question Matcher — "এই প্রশ্ন কতটুকু কমন?"

**সমস্যা:** ইউজার coaching-এর প্রশ্ন সমাধান করে, কিন্তু জানে না সেটা আগে বারবার
এসেছে কিনা। ব্যাংকে ১,২৯৪টি যাচাইকৃত প্রশ্ন আছে — ওগুলোর সাথে মিলিয়ে দেখালে
সে বুঝবে সে আসলে কতটুকু "repeat" পেয়েছে।

**UX (একটা পেজ, ৩টা সাইড):**

```
┌─────────────────────────────────────────────┐
│  🎯 প্রশ্ন ম্যাচার                          │
│  ┌───────────────────────────────────────┐  │
│  │ coaching-এর প্রশ্ন এখানে paste করো    │  │
│  │ (LaTeX সহ, ৪টি অপশনসহ)               │  │
│  └───────────────────────────────────────┘  │
│  [মিল খুঁজো]                                │
└─────────────────────────────────────────────┘
```

**মিল পাওয়া গেলে যা দেখাবে:**

```
╔══════════════════════════════════════════════════════╗
║  ✅ EXACT MATCH — DU '18-19 Hubohu (2018)            ║
╠══════════════════════════════════════════════════════╣
║  কমনতা:  ████████████░░░░░░  ৯/১৮ (৯ বছরে, ১৮ paper-এ) ║
║  Chapter: ভেক্টর          Topic: Type 1: একক ভেক্টর   ║
║  ২৬-২৭ সম্ভাবনা:  13.71%                             ║
║  ─────────────────────────────────────────────────  ║
║  🚨 ট্র্যাপ: অনেকে শুধু যোগফল খোঁজে, কিন্তু বিয়োগফলও  ║
║  📖 সমাধান: সামান্তরিকের কর্ণদ্বয় ...                    ║
╚══════════════════════════════════════════════════════╝
```

**মিল না পেলে:**

```
╔══════════════════════════════════════════════════════╗
║  🟡 SIMILAR (৮৩% মিল) — DU '20-21 Hubohu (2020)       ║
║  কমনতা: ████████░░░░░░░░░░  ৫/১১ (৫ বছরে, ১১ paper-এ)  ║
║  Chapter: ভেক্টর          Topic: Type 1: একক ভেক্টর   ║
╚══════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════╗
║  🔴 নতুন প্রশ্ন — ব্যাংকে নেই                        ║
║  ⚠️ এটা নতুন হতে পারে, কিন্তু similar topic আছে:     ║
║     ভেক্টর · Type 1: একক ভেক্টর · ৩৪টি ব্যাংক প্রশ্ন   ║
║     [এই chapter-এর সব প্রশ্ন দেখো]                  ║
╚══════════════════════════════════════════════════════╝
```

**মিলিং algorithm (সহজ, deterministic, কোনো AI/LLM নয়):**

```ts
// 1. Normalize
const norm = (s: string) => s
  .replace(/\\\[|\\\]|\$+/g, '')        // LaTeX ডিলিমিটার
  .replace(/[০-৯]/g, d => '০১২৩৪৫৬৭৮৯'.indexOf(d))  // বাংলা → ইংরেজি ডিজিট
  .replace(/[^\w\sঀ-৿]/g, '')           // punctuation বাদ
  .replace(/\s+/g, ' ')
  .toLowerCase().trim();

// 2. Token shingles (3-gram) — order-insensitive-ish, O(n) per pair
function shingles(text: string, k = 3): Set<string> {
  const w = norm(text).split(' ').filter(Boolean);
  const out = new Set<string>();
  for (let i = 0; i + k <= w.length; i++) out.add(w.slice(i, i + k).join(' '));
  return out;
}
function jaccard(a: Set<string>, b: Set<string>): number {
  let inter = 0;
  for (const x of a) if (b.has(x)) inter++;
  const uni = a.size + b.size - inter;
  return uni === 0 ? 0 : inter / uni;
}

// 3. একই chapter-এর প্রশ্নের সাথে তুলনা করো (candidate set ছোট → দ্রুত)
//    তারপর বাকি ব্যাংকের সাথে (optional, ধীর — শুধু button-এ চাপলে)
```

**Scoring:**

| score | ব্যাখ্যা | UI |
|---|---|---|
| `≥0.97` | exact (normalized text সমান) | ✅ EXACT MATCH |
| `0.80–0.96` | similar | 🟡 SIMILAR (n%) |
| `<0.80` | নতুন | 🔴 নতুন প্রশ্ন |

**"কমনতা" স্কোর কীভাবে দেখাবে:**

```
কমনতা = years_hit / 10   →  ৯ বছরে এসেছে = 90%
পাশাপাশি দেখাও: papers_hit, এবং last_year (সবচেয়ে সাম্প্রতিক কত বছরে)
```

`years_hit` ও `papers_hit` ব্যাংক থেকেই গোনো — প্রতিটি প্রশ্নে
`appears_in: [{source_name, exam_year, paper}]` array থাকলে সহজ হয়।
**না থাকলে `source_name` + `exam_year` থেকে গণনা করো** (এখন এগুলো আছে)।

**Performance:** ১,২৯৪ প্রশ্ন × paste করা ১টি প্রশ্ন = ১,২৯৪টি Jaccard হিসাব —
client-side-এ ৫ms-এর কম। কিন্তু প্রথম render-এ যেন lag না হয়, তাই:
shingle set আগে থেকে memoize করো (`Map<id, Set<string>>`), ১,২৯৪ entry
≈ ৩ MB RAM — acceptable।

**Bonus — submit & learn:** মিল না পাওয়া প্রশ্নগুলো ইউজার চাইলে
"এটা ব্যাংকে যোগ করো" বাটনে save করতে পারবে → `localStorage` → পরে JSON
export → `src/data/du_ka/past_paper/user_added_<date>.json`-এ merge।
**এটা AI-generated নয় — ইউজারের নিজের কাগজ থেকে, তাই license সমস্যা নেই।**

---

## F18. 👤 Account Corner — sync + progress (header-এর ডান প্রান্ত)

**চেহারা:**

```
┌──────────────────────────────────────────────────┐
│  👤  ┌────────────────────────────────────────┐  │
│  │  সালমান  ·  ঢাবি 'ক' ২০২৬               │  │
│  │  ──────────────────────────────────────  │  │
│  │  📊 অগ্রগতি                              │  │
│  │  MCQ   ████████████░░░░░  ৬৮%  (৮৯০/১,২৯৪)│  │
│  │  Written ██████░░░░░░░░░░  ৩২%  (৫/১৬)   │  │
│  │  Mock  ████░░░░░░░░░░░░░░░  ২/৭          │  │
│  │  ──────────────────────────────────────  │  │
│  │  🗓 কতগুলো exam আছে:  ৭ টি              │  │
│  │    Paper Final 1–10    │  ৩/১০ দিয়েছে    │  │
│  │    Subject Final 4টি   │  ১/৪ দিয়েছে     │  │
│  │    Model Test 1–5      │  ২/৫ দিয়েছে     │  │
│  │  ──────────────────────────────────────  │  │
│  │  🔄 সিঙ্ক: ২ মিনিট আগে  ·  [এখনই সিঙ্ক]  │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

**ক্লিক করলে (dropdown/panel) — ৪টি ট্যাব:**

```
[প্রগতি] [পরীক্ষা] [বুকমার্ক] [সেটিংস]
```

**ট্যাব ১ — প্রগ্রেস (চালু)**
- উপরের progress bar-গুলো
- "এই সপ্তাহে: ১২ প্রশ্ন সমাধান, ৩টি ভুল" — week-wise mini bar (৯টি week-এর progress)
- ২৫ দিনের roadmap-এর সাথে মিলিয়ে "Day 7/25" দেখাও

**ট্যাব ২ — পরীক্ষা (নতুন)**
কোন exam কতগুলো আছে, কয়টা দিয়েছে:

```
পরীক্ষা                        মোট    দিয়েছে   স্কোর
─────────────────────────────────────────────────
Paper Final 01–10              ১০        ৩       ৭২
Subject Final (Phys/Chem/M/B)   ৪        ১       ৬৫
Model Test 01–05                ৫        ২       ৭৮
DU Ka Mock (গোল্ড)              ৩        ১       ৮০
MAT Mock (গোল্ড)                ২        ০        —
─────────────────────────────────────────────────
মোট                             ২৪        ৭
```

**ট্যাব ৩ — বুকমার্ক** (F19-এর লিস্ট)
**ট্যাব ৪ — সেটিংস**
- পরের exam কোনটা (DU Ka / MAT) — ডিফল্ট অনুযায়ী সব প্রগ্রেস আলাদা
- লক্ষ্য স্কোর সেট (default ৭৮–৮০)
- data export/import (JSON)
- "সব ডেটা মুছে ফেলো" (reset)

**Sync কীভাবে কাজ করবে (সত্যি কথা):**

বর্তমানে Firebase project `admission-crack-2026`-এ **Firestore নেই** (শুধু Auth +
Analytics)। তাই ৩টা option:

| option | কী | সুবিধা | সমস্যা |
|---|---|---|---|
| **A. Local-only** | localStorage | এখনই কাজ করে, কোনো setup নেই | ডিভাইস বদলালে ডেটা নেই |
| **B. Firestore enable** | Firestore + rules | সব ডিভাইসে sync | setup লাগে, user নিজে করবে |
| **C. GitHub Gist** | personal access token | free, কোনো billing নেই | token নিজে রাখতে হবে |

**আমার recommendation: A দিয়ে শুরু করো, B-এর জন্য কোড ready রাখো।**
UI-তে "🔄 সিঙ্ক: স্থানীয়" দেখাও। যদি ইউজার চায় তখন Firestore চালু করে
`FirestoreSyncAdapter` বসাবে — interface আগে থেকে define থাকবে:

```ts
export interface SyncAdapter {
  get(): Promise<SyncState>;
  put(state: SyncState): Promise<void>;
  user(): { id: string; name: string } | null;
}
export const adapters: Record<string, SyncAdapter> = {
  local: LocalStorageAdapter,   // default
  // firestore: FirestoreAdapter,  ← ready, শুধু enable করলেই
};
```

> ⚠️ **আগের audit-এর ভুলটা এখানে করো না:** login modal-এ "cloud save" বলে লিখে
> Firestore ছাড়া localStorage-এ save করা হয়েছিল — মানে ইউজার মিথ্যা বুঝত।
> এবার UI-তে সৎভাবে লেখো: **"সিঙ্ক: স্থানীয় (এই ডিভাইসে)"** — Firestore enable না
> হওয়া পর্যন্ত "cloud" বলো না।

---

## F19. 🔖 Bookmark (প্রশ্ন সংরক্ষণ)

**কোথায়:** প্রতিটি প্রশ্ন card-এর উপরে-ডানে একটা bookmark icon (☆ / ★)।
ড্রিল চলাকালীনও, master set-এ, paper bank-এ — সব জায়গায় কাজ করবে।

**UI:**

```
┌────────────────────────────────────┐
│  Q1/60  📌 Physics · ভেক্টর    ★   │  ← চাপলে ভর হবে
│  উৎস: DU '18-19 (2018)             │
│  ...                               │
└────────────────────────────────────┘
```

**ডেটা:**

```ts
interface Bookmark {
  questionId: string;
  createdAt: number;
  source: 'drill' | 'master_set' | 'bank' | 'simulator' | 'matcher';
  setId?: string;          // কোন set থেকে
  exam: 'du_ka' | 'mat';
  subject: string;
  chapter: string;
  note?: string;           // ইউজার নিজের নোট
  tags: string[];          // ইউজার নিজের tag, যেমন "রিভিশন", "important"
}
```

**Bookmark page (`/bookmarks`):**

```
🔖 বুকমার্ক (২৪)

[সব] [Physics] [Chemistry] [শুধু ভুল] [আজকের]

┌────────────────────────────────────┐
│ ★ ভেক্টর · Type 1                   │
│ একটি পাতলা বৃত্তাকার চাকতির ...   │
│ [সমাধান দেখো] [ড্রিলে নিয়ে যাও]   │
│ [🏷️ ট্যাগ] [📝 নোট] [✕ সরাও]      │
└────────────────────────────────────┘
```

**Extra:** bookmark থেকে **"এই bookmark গুলোর একটা সেট বানাও"** বাটন →
`MASTER SET`-এর মতো নতুন custom set তৈরি হবে, ওটা simulator-এ চালানো যাবে।
(এটাই mistake book-এর সাথে মিলিয়ে "My Weak Set" বানানোর সবচেয়ে কার্যকর উপায়।)

**Export:** সব bookmark → JSON + CSV (Anki-এ import করার জন্য TSV-ও)।

---

## F20. 📐 Unified Formula Page — "এক জায়গায় সব সূত্র + ট্র্যাপ"

**চেহারা (একটাই পেজ, সব সূত্র):**

```
📐 সূত্র কার্ড — সবকিছু এক জায়গায়

[🔍 সূত্র খুঁজো]  [বিষয়: সব | Physics | Chemistry | Math | Biology]
[শুধু বারবার আসা ⭐]  [শুধু ট্র্যাপ আছে 🚨]  [শুধু easy ✅]

╔═══════════════════════════════════════════════════════╗
║  🟢 EASY — মূল বিষয়                            [★]    ║
║  সমান্তরাল সরলরেখা বলবিদ্যা                                  ║
║  ┌─────────────────────────────────────────────────┐  ║
║  │ $\vec{A}\parallel\vec{B}$ যখন $\vec{A}\times\vec{B}=\vec{0}$ │  ║
║  │ লম্ব: $\vec{A}\cdot\vec{B}=0$                   │  ║
║  │ সমান্তরাল উপাংশ:                                  │  ║
║  │ $\left(\frac{\vec{A}\cdot\vec{B}}{|\vec{B}|^2}\right)\vec{B}$ │  ║
║  └─────────────────────────────────────────────────┘  ║
║  🚨 ট্র্যাপ: কর্ণ ভেক্টর দেওয়া থাকলে সমান্তরিকের ক্ষেত্রফল  ║
║  📊 কমনতা: ৯ বছরে · ১৮ paper    উৎস: DU '18-19          ║
║  [যে প্রশ্নে এসেছে (১৮)] [বুকমার্ক] [নোট]              ║
╚═══════════════════════════════════════════════════════╝
```

**মূল কথা — "same same গুলো একসাথে":**

একই সূত্র বিভিন্ন প্রশ্নে বিভিন্ন রূপে থাকে (যেমন লম্ব/সমান্তরাল/উপাংশ — তিনটা
একই ধারণার তিন রূপ)। **সেগুলো একটা card-এ group করো।** Grouping key:

```
normalize(formula) → সূত্রের LaTeX-কে canonical form-এ আনো
  · \\vec{A} → \\mathbf{A}      · \\dfrac → \\frac
  · \\left( \\right) → ( )      · spaces ঠিক করো
  · ক্রম (term order) বদলাও (যেমন a+b → b+a)
```
তারপর **semantic cluster**: একই chapter + একই mega_type-এর সূত্রগুলোকে
একটা "concept card"-এ জোড়া লাগাও (হাতে-কলমে, কিন্তু বিশ্বাসযোগ্যভাবে)।

**Card-এর ৫টি অংশ:**

1. **সূত্র** — LaTeX, KaTeX-এ রেন্ডার
2. **সংজ্ঞা/শর্ত** — কখন ব্যবহার হয় (যেমন "লম্ব হলে dot = 0")
3. **🚨 ট্র্যাপ** — সবচেয়ে বেশি ভুল হওয়া জায়গা
4. **📊 কমনতা** — years_hit, papers_hit, উৎস
5. **🔗 সংযুক্ত প্রশ্ন** — "এই সূত্র ব্যবহার হয়েছে এই ১৮টি প্রশ্নে" → চাপলে drill চালু

**"easy / possible" চিহ্ন:**

প্রতিটি সূত্র card-এ একটা difficulty tag:

| tag | মানে | কীভাবে নির্ধারণ |
|---|---|---|
| 🟢 EASY | "এটা আসে" — সরাসরি মিলে যায় | যে প্রশ্নে ব্যবহৃত, ওটা ৫+ বছরে repeat হয়েছে **এবং** ব্যাংকে similar প্রশ্ন ≥ ৮টি |
| 🟡 MEDIUM | পরিবর্তন | ২–৪ বছরে repeat |
| 🔴 HARD | খুব কম আসে | ১ বছরে বা source বেশি |

**"possible" বার্গ:**
যে সূত্র/card আগের সব paper-এ একই রূপে এসেছে → **"POSSIBLE"** ব্যাজ।
ব্যাজের ভিত্তি: `years_hit ≥ 7` (বা ২৬-২৭ predictor-এর probability ≥ 60%)।

**সূত্র কোথা থেকে আসবে?**
`src/data/formulas.json` (৩৬৬টি card) — agent-এর তৈরি করা। কিন্তু আরও ভালো:
**ব্যাংকের প্রশ্ন থেকে সূত্র নিজে থেকে বের করো** — যেখানে `explanation`-এ
`$...$` LaTeX আছে সেগুলো extract করে frequency count করো। যেগুলো ≥৩ বার
এসেছে → "আসল সূত্র"। বাকি → "প্রশ্ন-সংজ্ঞানিত"।

```bash
# এই extraction script টা agent-কে দাও — scripts/extract-formulas.mjs
# ব্যাংকের explanation ও trap থেকে $...$ বের করে, normalize করে,
# frequency গুনে output: {formula, count, years_hit, papers_hit, chapters, trap}
```

**§ এই ফিচারটা written section-এর জন্য — কারণ MCQ-তে তুমি option আঁকড়ে
বেছে নিতে পারো, কিন্তু written-এ সূত্র মনে থাকতে হয়। written-এ ৪০ নম্বরের
মধ্যে ২৮+ নিতে হলে এই পেজটা প্রতিদিন দেখা জরুরি।**

---

## F21. 🗂 Week / Chapter / Topic তিনটি সাজসজা ফিরিয়ে আনো

ইউজারের মূল চাওয়া: *"old sob kichu ... week by week + chapter and topic wise sajalam"*।

### A. Week-wise drill (F17 ও A1-এর উপর দাঁড়াবে)

```
📅 সপ্তাহভিত্তিক

  Week 01  ████████████████░░░░  100 প্রশ্ন   ✅
  Week 02  ████████████████░░░░  100 প্রশ্ন   ✅
  Week 03  ████████████████████  180 প্রশ্ন   ✅
  Week 04  ████████████░░░░░░░░   96 প্রশ্ন   ✅
  Week 05  ████████████░░░░░░░░   96 প্রশ্ন   ✅
  Week 06  ████████████████████  216 প্রশ্ন   ⚠️ ৯৬টি dup আছে
  Week 07  ██████████░░░░░░░░░░   84 প্রশ্ন   ✅
  Week 08  ████████████████░░░░  120 প্রশ্ন   ✅
  Week 09  ██████████░░░░░░░░░░   76 প্রশ্ন   ✅
```

প্রতিটি week-এ ক্লিক → সেই week-এর ড্রিল (subject filter সহ)।

**A1-এর fix-এর পর সব week-এ প্রশ্ন আসবে।** এটা app-এর **সবচেয়ে বেশি ব্যবহৃত**
drill হওয়া উচিত — ইউজার প্রতিদিন এখানেই practice করবে।

### B. Chapter-wise drill

আছে (Chapter Explorer) কিন্তু **drag করে টেনে topic-এর drill** চাইলে:
প্রতিটি chapter card-এ "এই chapter ড্রিল করো" বাটন (DrillRunner-এ chapterId পাস করে)।

### C. Topic-wise drill (mega_type) — নতুন

```
🧩 টপিক অনুযায়ী (২৫৩টি)

Physics
  Type 1: একক ভেক্টর, অভিক্ষেপ ও উপাংশ নির্ণয়      ২৫ প্রশ্ন  ▓▓▓▓▓▓▓▓░░
  Type 2: বিপরীত ত্রিকোণমিতিক                       ১৮ প্রশ্ন  ▓▓▓▓▓▓░░░░
  ...
```

প্রতিটি mega_type-এর প্রশ্ন count + years_hit + "ড্রিল করো" বাটন।

**`prepare-data.mjs`-এর output-এ `mega_type` index দরকার:**
`src/data/index.json`-এ `by_mega_type: { "Type 1: ...": {count, years_hit, chapter, subject} }`

---

# PART C — ফিচার priority ও implementation order

| # | ফিচার | Priority | কেন | অনুমানিত কাজ |
|---|---|---|---|---|
| A1 | Week filter fix | **P0** | ৮/৯ সপ্তাহ ০ প্রশ্ন — ইউজারের দৈনন্দিন drill ভাঙা | ছোট |
| A2 | text-dedup | **P0** | একই প্রশ্ন ২বার (W06) | ছোট |
| F21 | Week/Chapter/Topic drill | **P0** | ইউজারের মূল চাওয়া | মাঝারি |
| F19 | Bookmark | **P1** | সহজ, মূল্যবান | ছোট |
| F20 | Unified Formula page | **P1** | written section-এর জন্য critical | বড় |
| F17 | Practice-Question Matcher | **P1** | ইউজারের নতুন ধারণা — coaching-এর প্রশ্ন মিলিয়ে দেখা | মাঝারি |
| F18 | Account corner + progress | **P2** | sync ছাড়া (local) করা যায় | মাঝারি |
| A3 | 'other' relabel | **P2** | ৯৭টি mislabelled | ছোট |
| A4 | mega_type index | **P2** | F21-এর dependency | ছোট |

**Order: A1 → A2 → A4 → F21 → F19 → F20 → F17 → F18 → A3**

---

# PART D — Acceptance criteria (সব শেষে চেক করো)

```bash
# 0 error
node scripts/validate-data.mjs src/data/bank
node scripts/validate-data.mjs src/data/master

# master set অপরিবর্তিত
node scripts/coverage-scorer.cjs src/data/master/du_ka_set_a.json   # 60/60 REAL-PAST
node scripts/coverage-scorer.cjs src/data/master/mat_set_a.json     # 100/100 REAL-PAST

# week filter ঠিক
# → index.json-এ by_week = {week_01:100, ..., week_09:76}
# → প্রতিটি week chip-এ ক্লিক করলে >0 প্রশ্ন
# → Week 06-এ একই প্রশ্ন ২বার নেই (A2-এর পর)

# build
npm run build    # 0 error
```

**Browser-এ যাচাই (সব route):**

```
/            → হোম, ১,২৯৪ প্রশ্ন, progress bar দেখা যাচ্ছে
/weekly      → ৯টি week chip, প্রতিটিতে >0 প্রশ্ন
/bookmarks   → bookmark page কাজ করছে
/formulas    → unified formula page, 🟢/🟡/🔴 tag + 🚨 trap দেখা যাচ্ছে
/matcher     → paste করে match দেখায় (exact + similar + কমনতা)
/account     → corner dropdown, progress bar + exam table
/simulator   → DU Ka ও MAT দুটোই চলছে, −0.25 মার্কিং সহ
/master-set  → SET-A/B/C ঠিক আছে
```

**সব route-এ 0 JS console error।**

---

# PART E — যা করবে না

```
❌ AI/LLM দিয়ে কোনো প্রশ্ন তৈরি বা সাজানো (user-এর নিজের দেওয়া paper ছাড়া)
❌ Firestore enable না করে "cloud sync" দাবি
❌ নতুন UI theme / রঙ / typography বদলানো (বাংলা কপি ও ভিজ্যুয়াল আছে)
❌ Admin panel, payment, AI tutor/chat
❌ Master set-এর প্রশ্ন সংখ্যা বা composition বদলানো
❌ নতুন package (dependency যোগ করতে হলে কেন দরকার বলো)
```

---

# PART F — ইউজারের কাছ থেকে coaching paper আসলে

**এটা app-এর সবচেয়ে বড় ভবিষ্যৎ মূলধন।** coaching paper এলে:

```
src/data/du_ka/paper_final/paper_final_01.json
src/data/du_ka/subject_final/subject_final_physics.json
src/data/du_ka/model_test/model_test_01.json
```

প্রতিটি file-এর schema (F17-এর matcher-ও এই schema-ই পড়বে):

```json
[
  {
    "id": "pf01_phy_q01",
    "source_type": "paper_final",
    "source_name": "Paper Final 01",
    "exam": "du_ka",
    "exam_year": "2026",
    "exam_date": "2026-11-25",
    "subject": "Physics",
    "chapter_id": "ভ_ক_টর",
    "chapter_name": "ভেক্টর",
    "chapter_raw": "ভেক্টর (Vector)",
    "mega_type": "Type 1: একক ভেক্টর, অভিক্ষেপ ও উপাংশ নির্ণয়",
    "week": null,
    "question": "প্রশ্ন, LaTeX সহ",
    "options": ["A", "B", "C", "D"],
    "correct_index": 2,
    "explanation": "সমাধান",
    "trap": "ভুল করার কারণ",
    "is_written": false,
    "marks": 1,
    "duration_sec": 45
  }
]
```

**লিখিত প্রশ্ন:** `options: []`, `correct_index: -1`, `is_written: true`,
`marks: 10`, `duration_sec: 270`.

**তারপর অবশ্যই:**

```bash
node scripts/validate-data.mjs src/data/bank
node scripts/build-master-set.mjs
node scripts/coverage-scorer.cjs src/data/master/du_ka_set_a.json
```

**Model Test = held-out validation set।** `03-PREDICTOR-SPEC.md`-এর নিয়মে:
`model_test` weight 1.00, `paper_final` 0.95, `subject_final` 0.90,
`past_paper` 0.85, `weekly_solve` 0.70।

প্রতিটি Model Test করার পরে **ইউজারের actual score বনাম predictor-এর prediction**
দুটোই রাখো — এটাই তোমার predictor-এর সত্যিকারের accuracy মাপার একমাত্র উপায়।
**AI-বানানো প্রশ্ন নয় — তোমার নিজের হাতে কলমে করা paper। সেটাই সবচেয়ে বড় সম্পদ।**
