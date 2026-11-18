# 01 · DATA SCHEMA

## একটি প্রশ্ন = একটি object

```jsonc
{
  "id": "pf01_physics_q01",          // globally unique, source-scoped. কখনো duplicate হবে না।
  "source_type": "model_test",       // ← সবচেয়ে গুরুত্বপূর্ণ field, নিচে দেখো
  "source_name": "Model Test 03",    // কোন paper থেকে
  "exam": "du_ka",                   // du_ka | mat | ru | ju | cu | gst | eng_bridge | other
  "exam_year": 2026,
  "exam_date": "2026-12-05",
  "subject": "Physics",
  "chapter_id": "phy_vector",        // stable slug (snake_case, stable over time)
  "chapter_name": "ভেক্টর (Vector)",  // human-readable, বাংলায়
  "mega_type": "Type 1: একক ভেক্টর, অভিক্ষেপ ও উপাংশ নির্ণয়",
  "question": "…",
  "options": ["A…","B…","C…","D…"],
  "correct_index": 0,                // null if is_written
  "explanation": "…",
  "trap": "…",
  "is_written": false,
  "marks": 1,
  "duration_sec": 45,
  "probability_label": "98% DU 'Ka' Pattern Repeat",  // রাখো, কিন্তু কখনো trust করো না
  "appears_in": ["pf01", "mt03"]     // optional: same question 2 paper-এ থাকলে
}
```

---

## `source_type` — এটাই নতুন ডেটার সবচেয়ে দামি অংশ

তুমি যে coaching-এর paperগুলো দিচ্ছে, সেগুলো **আসল exam-pattern paper**। Predictor-এর ওজন এখান থেকেই আসবে।

| `source_type` | মানে | Predictor weight |
|---|---|---|
| `model_test` | coaching-এর Model Test (5টি) | **1.00** |
| `paper_final` | coaching-এর Paper Final (10টি) | **0.95** |
| `subject_final` | coaching-এর Subject Final (per subject) | **0.90** |
| `past_paper` | আসল DU/MAT/RU/JU/CU/GST past paper | **0.85** |
| `weekly_solve` | coaching-এর weekly solve sheet | **0.70** |

### Coaching paper যোগ করার নিয়ম

```
১. প্রতিটি paper = আলাদা JSON ফাইল
   src/data/du_ka/model_test/model_test_03.json
   src/data/du_ka/paper_final/paper_final_01.json
   src/data/du_ka/weekly_solve/week_03.json
   src/data/mat/model_test/mat_model_test_01.json

২. id নামকরণ:  <source_prefix>_<subject_slug>_q<NN>
   pf01_physics_q01 · mt03_chem_q07 · wk03_bio_q12 · sf_physics_q01
   NN তিন সংখ্যা, zero-padded।

৩. exam_date coaching-এর schedule থেকে (কখন সেই paper হয়েছে)।

৪. source_name = "Paper Final 01" / "Model Test 03" / "Weekly 03 Solve Sheet"

৫. chapter_id — chapter-taxonomy.csv থেকে নাও। নতুন chapter হলে নতুন slug
   বানাও (পুরানো slug কখনো বদলাবে না)।

৬. is_written = true হলে options = [] রাখো, correct_index = null,
   marks = 2..5, duration_sec ≈ 240।

৭. যদি একই প্রশ্ন দুটো paper-এ থাকে → id একটাই রাখো, appears_in-এ দুটোই লেখো।
   (progress আলাদা আলাদা count হবে না)
```

### Source prefix convention

| prefix | paper |
|---|---|
| `pf` | Paper Final |
| `mt` | Model Test |
| `sf` | Subject Final |
| `wk` | Weekly solve sheet |
| `du`, `mat`, `ru`… | past papers |

---

## Chapter

`data/chapter-taxonomy.csv` তে ৬৪টি chapter, `chapter_id` + `chapter_name` দিয়ে আছে।
বর্তমান ব্যাংকের `bio_zoo_01`, `math_1st_03` — এগুলো **raw ID**, পড়ার সময় বোঝা যায় না।
Normalized করার সময় `mega_type` থেকে readable নাম বের করা হয়েছে যেখানে পারা গেছে।

**নতুন coaching paper-এর প্রশ্ন বাংলায় chapter পরিচিত না হলে:** প্রশ্নটা পড়ে নাম বানাও —
`chapter_id` রাখো `phy_vector` মতো ছোট, stable, ইংরেজি slug।

---

## যাচাই (agent যেন ব্যাংক ঢোকানোর আগে চেক করে)

```bash
node scripts/validate-data.mjs src/data
```

যা ধরবে:
- duplicate id
- `correct_index` out of range বা null (MCQ হলে)
- `options.length === 0` কিন্তু `is_written !== true`
- `chapter_id` যেটা taxonomy-তে নেই
- missing `source_type` / `exam` / `exam_year`
- answer position bias (A/B/C/D distribution — ২৫%±৮ এর বাইরে হলে সতর্ক)
- ফাঁকা `explanation` (MCQ-তে explanation না থাকলে warning)

---

## ফাইল লেআউট (legacy bank vs নতুন paper)

legacy ব্যাংকের ৪১৬টি "paper" আসলে গড় ৩ প্রশ্নের টুকরো — তাই `prepare-data.mjs`
সেগুলোকে **`<exam>/<source_type>/<subject>.json`** (৫৫টি ফাইল, সবচেয়ে বড় ৩০৪ KB)
হিসেবে split করে। নতুন coaching paper যোগ করার সময় **একটি paper = একটি ফাইল**
ব্যবহার করো (যেমন `model_test_03.json`)। ছোট ফাইলগুলো একত্রে জোড়া লাগানো যাবে।

**সাইজ:** legacy bank compressed = ৩৪৮ KB, split = ২.৪ MB total / ৫৫ ফাইল।
বড়ত্ব content-এ (বাংলা UTF-8 ৩ বাইট/অক্ষর + LaTeX) — pretty-print বাদ দিলেও কমে না।

---

## ফাইল লেআউট

```
src/data/
├── du_ka/
│   ├── past_paper/du_2018.json …
│   ├── weekly_solve/week_01.json …
│   ├── paper_final/paper_final_01.json …
│   ├── subject_final/subject_final_physics.json …
│   └── model_test/model_test_01.json …
├── mat/…
├── other_uni/ru_2019.json, ju_2020.json …
├── master/
│   ├── du_ka_set_a.json, du_ka_set_b.json, du_ka_set_c.json
│   └── mat_set_a.json, mat_set_b.json, mat_set_c.json
├── formulas.json
├── flashcards.json
├── gk_monthly.json
└── index.json          ← generated: chapter → paper list, counts, years
```
