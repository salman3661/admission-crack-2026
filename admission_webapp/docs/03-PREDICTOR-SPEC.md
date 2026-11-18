# 03 · PREDICTOR SPEC — LEARN → PREDICT → SELECT → VALIDATE

**এটাই তোমার অ্যাপের আসল মূল্য। UI নয় — এই মডেল।**

---

## কেন "AI প্রশ্ন বানানো" কাজ করে না

তুমি চেয়েছিলে AI নিজে predict করে master set বানিয়ে দিক। সমস্যা:

1. ২৬-২৭-এর paper এখনো হয়নি — কেউ জানে না
2. বাংলাদেশের coaching QB (Hubohu/Varsoty/Udvash) public web-এ নেই → model কম জানে
3. AI-generated MCQ-র উত্তর ভুল হতে পারে, আর LLM-এর নিজস্ব position bias থাকে
4. "সবচেয়ে repeat প্রশ্ন" দাবিটার কোনো source থাকে না

**সমাধান:** AI নতুন প্রশ্ন বানাবে না — **তোমার আসল past paper থেকে select করবে**, year-wise model শিখে। তাহলে:
- কোনোটাই fake নয় (প্রতিটির source আছে)
- উত্তর-কি verified
- প্রশ্নের provenance দেখায় → "এটা DU '19-20 Hubohu, ১১ বছরে এসেছে" → ছাত্রের trust বাড়ে

---

## ① LEARN

### source_type weight
```js
const SOURCE_WEIGHT = {
  model_test:    1.00,   // coaching model test — আসল exam-pattern paper
  paper_final:   0.95,   // coaching paper final
  subject_final: 0.90,   // coaching subject final
  past_paper:    0.85,   // আসল DU/MAT/RU/JU/CU/GST paper
  weekly_solve:  0.70    // coaching weekly solve sheet
};
```

### recency weight
```js
const recency = (year) => Math.pow(0.86, 2025 - year);   // 2025 = 1.0, 2016 ≈ 0.16
```

### প্রতি (subject, chapter)-এর জন্য তিনটি সংখ্যা বের করো
```
1. perYearShare[y]  = ওই বছরে ওই subject-এর প্রশ্নের কত % ওই chapter-এ
2. yearsHit         = ওই chapter কতটি ভিন্ন বছরে এসেছে
3. papersHit        = ওই chapter কতটি ভিন্ন paper-এ এসেছে     ← নতুন signal
```
`papersHit` বিশেষ শক্তিশালী: ৮ বছরে একবার আসা chapter ≠ ৮টি আলাদা paper-এ একবার করে আসা chapter।

---

## ② PREDICT

```js
p(chapter | subject) = Σ_y  recency(y) × SOURCE_WEIGHT(sourceType) × perYearShare[y]
expected_mcq(chapter) = 15 × p                    // DU Ka, per subject
                     = subject_quota × p          // MAT: Bio 30, Chem 25, Phys 20, Eng 15, GK 10
```

---

## ③ SELECT

```js
score(q) = p(chapter|subject)
         × recency(q.year)
         × min(1.55, 1 + 0.09 × (yearsHit − 1))
         × SOURCE_WEIGHT[q.source_type]
         × 0.68 ^ (already_taken_from_same_chapter)
         × 0.90 ^ (already_taken_from_same_year)
```

### Constraints (এগুলো না রাখলে একটা chapter সব ধরে ফেলে)
```
· seed: প্রতিটি chapter যার expected_mcq ≥ 0.4 → কমপক্ষে ১টি প্রশ্ন
· per-chapter cap: ceil(expected_mcq × 1.7)
· per-year cap: set-এর 38%
· SET-A ∩ SET-B = ∅ (একটাও প্রশ্ন shared নয়)
· SET-C = wildcard: কম-probability chapter + অন্য university (RU/JU/CU/GST)-এর
         একই chapter-এর প্রশ্ন (syllabus overlap → DU-তে আসতে পারে)
```

### ৩টি set-এর ভূমিকা
| Set | সংখ্যা | ভূমিকা |
|---|---|---|
| **A** | DU Ka 60 / MAT 100 | সবচেয়ে সম্ভাব্য — এটা দিয়ে শুরু করো |
| **B** | DU Ka 60 / MAT 100 | দ্বিতীয় স্তর — A-র সাথে overlap নেই |
| **C** | ~২০–৪০ | wildcard — কম-probability chapter + অন্য varsity |

---

## ④ VALIDATE — এটাই বিশ্বাসযোগ্যতা তৈরি করে

### (a) Leave-one-year-out backtest
```
প্রতিটি test year Y (2021–2024) এর জন্য:
  train = years < Y থেকে predict করো
  measure:
    · coverage = Y-র কত % প্রশ্ন আমার top-8 predicted chapter-এ পড়ে?
    · rank hit = Y-র সবচেয়ে বেশি আসা chapter আমার prediction-এ #1 ছিল কিনা?
```
**বর্তমান baseline: coverage 77.9%, #1 rank hit 13%**
নতুন coaching paper যোগ হলে এই সংখ্যা বদলাবে — সেটাই দেখাবে তোমার model কতটা ভালো হলো।

### (b) Coaching Model Test = HELD-OUT VALIDATION SET 🏆
**এটাই সবচেয়ে মূল্যবান সংখ্যা।**

Coaching-এর Model Test paper আসল exam-pattern। তাই:
```
Model Test 03 (December 2026) → এর chapter-mix আগের ডেটা (2010–2026 + Paper Final)
                                থেকে predict করো → actual MT-03-এর সাথে মিলাও
                                → coverage % বের করো
```
এটাই বলে দেবে **তোমার predictor সত্যিই কতটা কাজ করে** — কোনো অনুমান নয়, পরিমাপ।

### (c) Coverage proof
`scripts/coverage-scorer.mjs` দিয়ে প্রমাণ করো যে master set-এর প্রতিটি প্রশ্ন real bank-এর সাথে মেলে:
```
DU Ka SET-A → 60/60 REAL-PAST (গড় 99.9/100) ✓
```

---

## ⑤ APP-এ যা দেখাবে

প্রতিটি প্রশ্নের পাশে এই provenance দেখাও — এটাই "fake লাগবে না" বোধায়:

```
📌 ভেক্টর (Vector) · Type 1: একক ভেক্টর, অভিক্ষেপ ও উপাংশ নির্ণয়
   উৎস: DU '18-19 Hubohu  ·  এসেছে: 10টি বছরে, 7টি paper-এ
   ২৬-২৭ সম্ভাবনা: 11.5% (chapter-level)  ·  প্রত্যাশিত MCQ: 1.7
```

---

## ⚠️ Model-এর সীমাবদ্ধতা (UI-তে সৎভাবে দেখাও)

1. **Exact-question predictor না** — topic-level। Backtest 77.9% coverage, #1 hit 13%
2. **তোমার ব্যাংকের বছর-অসমতা model-এ ঢুকে যায়** — Physics ২০২০-এ ১০৪টি, ২০২৩-এ ১৫টি। যে বছর/বই কম সংগ্রহ হয়েছে সেটা আগে সাপ্লিমেন্ট করো।
3. **Chapter-name নিজে ঠিক করো** — raw ID (`bio_zoo_01`) দেখালে ছাত্র বুঝবে না
4. **probability_label বিশ্বাস করো না** — সেগুলো editorial, আসল signal হলো yearsHit ও papersHit
5. **Written-এর জন্য আলাদা model দরকার** — written প্রশ্নের chapter বণ্টন MCQ-র চেয়ে ভিন্ন, তাই written-এর জন্য আলাদা weight

---

## Script ব্যবহার

```bash
node scripts/build-master-set.mjs          # master set + chapter map তৈরি
node scripts/validate-data.mjs src/data    # data lint
node scripts/coverage-scorer.js set.json   # real কিনা প্রমাণ
```

সবগুলো স্ক্রিপ্ট standalone চলে — প্রথমবার ব্যাংক না থাকলে deployed bundle থেকে নিজে থেকেই টেনে নেয়।
