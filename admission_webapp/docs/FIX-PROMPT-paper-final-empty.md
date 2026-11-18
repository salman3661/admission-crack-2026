# FIX PROMPT — `/paper-final` ও `/subject-final`-এ "০টি প্রশ্ন" বাগ

> এই ফাইলটা agent-কে সরাসরি paste করো। Live site verify করা হয়েছে — নিচের প্রতিটি
> সংখ্যা browser থেকে measure করা, অনুমান নয়।

---

## 🔴 সমস্যা (live-verified)

`/paper-final` ও `/subject-final` রুটে **০টি পেপার / ০টি প্রশ্ন** দেখায়।

**Root cause:** এই দুই রুট route-specific `source_type` filter hard-code করে
(`paper_final` / `subject_final`)। কিন্তু legacy ব্যাংকে এই ধরনের **একটিও paper নেই**:

```
ব্যাংকে আছে:   past_paper 917 (45 file) + weekly_solve 525 (10 file) = 1,442
ব্যাংকে নেই:   paper_final 0 · subject_final 0 · model_test 0
```

তাই filter কাজ করছে, কিন্তু ফলাফল খালি। **ডেটা হারায়নি — শুধু default filter ভুল।**

**Proof (same page, chip বদলালেই):**

```
[সব ধরন]    → 16টি পেপার ফাইল • মোট 844টি প্রশ্ন  ✅
[Past Paper] → 12টি পেপার ফাইল • মোট 439টি প্রশ্ন  ✅
[Weekly Solve] → 4টি পেপার ফাইল • মোট 405টি প্রশ্ন  ✅
[Paper Final] → 0টি পেপার ফাইল • মোট 0টি প্রশ্ন   ❌  ← বাগ
```

---

## ✅ যা ঠিক করতে হবে (৪টি fix)

### Fix 1 — Default filter সবসময় `all` (সবচেয়ে জরুরি)

`PaperBankView.tsx`-এ route যখন `source_type` নির্দিষ্ট করে, সেটা ব্যবহার করো না।
**Default chip সবসময় `all` রাখো**, এবং route-এর নাম শুধু heading-এ দেখাও।

```tsx
// ❌ আগে (ধরো): const [srcType, setSrcType] = useState(defaultSourceType);
// ✅ এখন:
const [srcType, setSrcType] = useState<'all' | SourceType>('all');
```

Heading-এ route-এর নাম থাকবে (`Paper Final`), কিন্তু list সব ধরন দেখাবে।
**ব্যবহার ভাবা:** "Paper Final" ট্যাবে ক্লিক করলে চোখে "সব ধরন" active থাকবে,
নিচে ১৬টি পেপার দেখাবে — খালি পর্দা নয়।

### Fix 2 — Route-এর source_type-এ কিছু থাকলে ওটা আগে দেখাও

`/paper-final`-এ গিয়ে যদি ভবিষ্যতে `paper_final` paper আসে, তখন সেটা
default হওয়া উচিত। তাই:

```tsx
const available = useMemo(() => papersFor(srcType), [srcType]);
const initial = available.length > 0 ? routeSourceType : 'all';
```

অর্থাৎ route-specific filter রাখো, কিন্তু **শূন্য হলে `all`-এ fall back করো**,
আর active chip `all` দেখাও। ফলে coaching paper যোগ হলেই নিজে থেকেই সেটা
default হয়ে যাবে — extra কোড লাগবে না।

### Fix 3 — Empty state-এর কপি ঠিক করো

এখন যা দেখাচ্ছে (ভুল বার্তা — মনে হয় তুমি কিছু যোগ করোনি):

```
এই ফিল্টারে এখন কোনো প্রশ্ন যোগ করা হয়নি।
src/data/bank/ এ JSON ফাইলে যোগ করে build-master-set.mjs চালাও।
```

নতুন কপি:

```
এই ধরনের কোনো paper নেই এখনো।
[সব ধরন দেখো]   ← বাটন, click করলে সব পেপার দেখাবে
```

বাটনে click করলে `srcType = 'all'` সেট করবে। আর যদি সত্যিই কোনো paper না থাকে
(এখনকার মতো, `paper_final` ফাইলের জন্য), তখন লেখো:

```
এই ধরনের paper এখনো আসেনি।
Paper Final / Subject Final / Model Test — coaching-এর paper যোগ করলে এখানে আসবে।
এখনই যা আছে: 16টি পেপার · 844টি প্রশ্ন  [সব ধরন দেখো]
```

### Fix 4 — Tier badge-এর সংখ্যা dynamic করো

এখন header-এ hard-coded: `Tier 2: Paper Final 60+16` · `Tier 3: Subject Final QB` ·
`Tier 4: Final Model Test MOCK` — কিন্তু বাস্তবে ওই tier-এ ০টি paper।
এটা মিথ্যা দাবি, ঠিক করো:

```tsx
// index.json-এর papers[] থেকে গণনা করো
const countByType = (t: SourceType) =>
  papers.filter(p => p.source_types.includes(t)).reduce((n, p) => n + p.count, 0);

Tier 2: Paper Final    → {countByType('paper_final') || 0}   // এখন 0
Tier 3: Subject Final  → {countByType('subject_final') || 0} // এখন 0
Tier 4: Final Model    → {countByType('model_test') || 0}    // এখন 0
```

0 হলে badge দেখাও না (বা ফাঁকা রাখো) — "60+16" লিখে রাখলে ভুল সংখ্যা।

---

## 🟡 বোনাস Fix 5 — `other` exam-এ ভুল লেবেল (data quality)

`other` exam-এ ৪৯৫টি প্রশ্ন আছে, যার মধ্যে আসলে **DU-র weekly solve** ঢুকে আছে:

```
Weekly 06 Varsity (Udvash) W-06 Set-A / Set-B
Weekly 06 Varsity (Udvash) Daily P-06 Set-A
Speed Hack 2026
→ এগুলো exam='du_ka' হওয়া উচিত, 'other' নয় (৯৭টি প্রশ্ন)
```

ফলে `/weekly`-তে এখন শুধু **4টি ফাইল · 405টি প্রশ্ন** দেখাচ্ছে, বাকি weekly
solve-গুলো লুকানো। `prepare-data.mjs`-এ `source_name`-এর pattern মিলিয়ে
এগুলোকে `du_ka`-তে সরাও।

**সতর্কতা:** `exam` বদলালে master set ও backtest-এর সংখ্যা বদলাবে।
পরিবর্তনের পরে এই চারটা কমান্ড চালিয়ে আগের সংখ্যার সাথে মিলিয়ে নাও:

```bash
node scripts/validate-data.mjs src/data/bank     # এখন: 0 error
node scripts/build-master-set.mjs
node scripts/coverage-scorer.cjs src/data/master/du_ka_set_a.json  # এখন: 60/60 REAL-PAST
node scripts/coverage-scorer.cjs src/data/master/mat_set_a.json    # এখন: 100/100 REAL-PAST
```

**Regression guard:** কোনো সংখ্যা কমে গেলে (60/60 → 59/60 বা 100/100 → 97/100)
সেটা ফেরত ফেরত নাও — কারণ তখন exam re-label সিদ্ধান্ত ভুল হয়েছে।

---

## 🎯 নতুন coaching paper যোগ করার নিয়ম (পরে, কাজ শুরু করলে)

প্রতিটি coaching paper = **একটি JSON ফাইল**, path:
`src/data/du_ka/<source_type>/<paper_name>.json`

```
source_type-এর মান:  paper_final | subject_final | model_test | weekly_solve | past_paper
exam-এর মান:          du_ka | mat
```

### Template (এটা হুবহু কপি করে প্রতিটি paper-এর জন্য বানাও)

```json
[
  {
    "id": "pf_01_phy_q01",
    "source_type": "paper_final",
    "source_name": "Paper Final 01",
    "exam": "du_ka",
    "exam_year": "2026",
    "subject": "Physics",
    "chapter_id": "ভ_ক_টর",
    "chapter_name": "ভেক্টর",
    "chapter_raw": "ভেক্টর (Vector)",
    "mega_type": "Type 1: ...",
    "question": "প্রশ্নের পুরো লেখা, LaTeX সহ",
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

### লিখিত প্রশ্ন (written section)

```json
{
  "id": "pf_01_written_q01",
  "source_type": "paper_final",
  "source_name": "Paper Final 01",
  "exam": "du_ka",
  "exam_year": "2026",
  "subject": "Physics",
  "chapter_name": "ভেক্টর",
  "question": "প্রশ্ন",
  "options": [],
  "correct_index": -1,
  "explanation": "ধাপে ধাপে সমাধান",
  "is_written": true,
  "marks": 10,
  "duration_sec": 270
}
```

### যোগ করার পরে অবশ্যই চালাবে

```bash
node scripts/validate-data.mjs src/data/bank    # 0 error হতে হবে
node scripts/build-master-set.mjs              # master set আবার তৈরি হবে
node scripts/coverage-scorer.cjs src/data/master/du_ka_set_a.json
```

**`model_test` paper আসলেই সবচেয়ে মূল্যবান** — ওটা তোমার predictor-এর
held-out validation set। `03-PREDICTOR-SPEC.md`-এর নিয়মে source_type weight:
`model_test 1.00 > paper_final 0.95 > subject_final 0.90 > past_paper 0.85 > weekly_solve 0.70`

---

## ✅ Acceptance criteria (agent-কে যাচাই করতে বলো)

```bash
# 1) তিনটা route-এই প্রশ্ন আসছে
curl -s https://admissionwebapp.vercel.app/paper-final | head -c 400
# → "0টি পেপার" থাকা যাবে না (SSR না হলে browser-এ চেক করো)

# 2) browser-এ:
#    /paper-final   → chip "সব ধরন" active, 16টি পেপার · 844টি প্রশ্ন
#    /subject-final → chip "সব ধরন" active, 16টি পেপার · 844টি প্রশ্ন
#    /weekly        → chip "সব ধরন" active, weekly file-গুলো দেখা যাচ্ছে
#    /bank          → একই (regression check)

# 3) কোনো পেপারে ক্লিক করলে প্রশ্ন লোড হয় (৪টি অপশন + টাইমার + উৎস)

# 4) 0 JS console error

# 5) Master set অপরিবর্তিত:
node scripts/coverage-scorer.cjs src/data/master/du_ka_set_a.json  # 60/60 REAL-PAST
node scripts/coverage-scorer.cjs src/data/master/mat_set_a.json    # 100/100 REAL-PAST
```

---

## 📌 বোনাস — যা ইতিমধ্যে ঠিক আছে (ছুঁবে না)

```
✅ /master-set drill → DU Ka SET-A, প্রশ্ন 1/60, উৎস + "9টি বছরে, 18টি paper-এ" + 13.71%
✅ /simulator       → MCQ ধাপ, প্রশ্ন 1/60 (Physics), timer 44:58, EV = 1.25P − 0.25 হিন্ট
✅ /weekly          → 4টি পেপার · 405টি প্রশ্ন (Fix 5-এর পরে বাড়বে)
✅ JS console error → 0
✅ Bundle           → 374 KB (আগে ছিল 27.27 MB)
```

**শুধু উপরের ৪টি fix করো, বাকি কিছু নষ্ট করো না।**
