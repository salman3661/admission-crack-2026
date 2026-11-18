# 04 · FEATURES — কী বানাবে, কোন ক্রমে

**বানাও যত তত ভালো, কিন্তু P0 শেষ না হওয়া পর্যন্ত P1/P2 ধরবে না।**

---

## P0 · MUST HAVE (এগুলো ছাড়া অ্যাপ অসম্পূর্ণ)

### F1 · Library layer
একটাই module — সব feature এর ভিত্তি।
```js
// src/lib/library.js
export async function loadPaper(exam, sourceType, name)   // JSON fetch + cache
export function buildIndex(rows)                          // subject/chapter/exam/source_type → rows
export function dedupe(rows)                               // id unique, appears_in merge
export function normalize(rows)                            // enum, casing, slug
export function countBy(rows, key)                        // runtime counting
```
- Dedupe: একই `id` → একটি row, `appears_in: [...]` merge
- Normalize: subject/track enum, `chapter_id` slug, `is_written` derive
- সব গণনা এখান থেকে — UI-তে কোনো hardcoded সংখ্যা নেই

### F2 · Drill runner
**MCQ mode**
- একটি প্রশ্ন at a time, soft timer (45 s — চুপচাপ থাকলে highlight)
- অপশন shuffle (session-stable, reload-safe)
- সঠিক/ভুল সাথে সাথে + ব্যাখ্যা + trap দেখাও
- Prev/Next, শেষে সব উত্তর ও score

**Written mode**
- প্রশ্ন + marks (2–5) + timer
- "সিলেবাস স্টাইলে লিখো" prompt
- Model answer reveal (তোমার ব্যাংকের explanation)
- নিজের লেখা save করো → পরে compare

### F3 · Real exam simulator ★
এটাই তোমার সবচেয়ে গুরুত্বপূর্ণ feature।
```
DU Ka:  MCQ 60 (45 min) → break → Written 40 (45 min)
        4 বিষয় × (15 MCQ + 10 written)
        −0.25 প্রতি ভুল MCQ
MAT:    100 MCQ, 75 min, −0.25, pass 40
```
- দুই ধাপে (MCQ আগে শেষ না করলে written-এ যাবে না)
- শেষে: total score / 100, per-subject table, MCQ accuracy, সময়, chapter-wise loss
- **Chapter-wise loss সরাসরি error log-এ যায়** → ওইটাই তোমার লুপ

### F4 · Master Set view
3টি set (A/B/C) × 2 exam, `src/data/master/*.json` থেকে।
প্রতিটি কার্ডে provenance দেখাও (chapter, source paper, বছর, yearsHit, likelihood %)

### F5 · Error log + Mistake Book ★
```js
localStorage['ac_error_log'] = [
  { qid, myAnswer, correct, whyWrong, chapter, subject, source_type, source_name,
    madeAt, retestDue }   // SM-2: 1 / 3 / 7 / 14 দিন
]
```
- Mistake Book screen: due আজ → পুনরায় attempt
- কেন ভুল হিল সেটা লেখো (এটাই তোমার সবচেয়ে বড় সম্পদ)

### F6 · Weakness radar
- per subject + per chapter: attempted, correct, **marks lost**
- bar chart, marks lost অনুযায়ী sorted
- click → ওই chapter-এর drill

### F7 · Mock tracker
`data/mock-tracker-template.csv`-এর কলাম অনুযায়ী:
score / per-subject / MCQ accuracy / minutes used / written blank count / top-3 lossy chapter

### F8 · Chapter explorer
`data/chapter-taxonomy.csv` থেকে — question count, years hit, expected ২৬-২৭ MCQ, drill button

---

## P1 · HIGH VALUE

| # | ফিচার | নোট |
|---|---|---|
| F9 | Formula cards (366) | searchable, per chapter, printable |
| F10 | GK monthly cards | অ্যাপের existing monthly GK dataset |
| F11 | Flashcards (216) | একই drill UI-তে |
| F12 | Exam-day timer screen | 45/45 বা 75 মিনিট, attempt-strategy helper |
| F13 | "Question theory" | chapter, source, year, mega-type, কত বছরে এসেছে — provenance panel |
| F14 | PWA install prompt (iOS) + offline shell | |

---

## P2 · শুধু P0+P1 শেষ ও verify হলে

| # | ফিচার | নোট |
|---|---|---|
| F15 | Google login (Firebase) | copy ঠিক করো — cloud sync দাবি করো না যদি Firestore না থাকে |
| F16 | Custom domain + full SEO | sitemap, robots, JSON-LD, 404 |

---

## 🚫 বানাবে না

- AI দিয়ে প্রশ্ন generate · admin/authoring panel · AI tutor/chat ·
  social feature · payment · database · push notification

**কারণ:** ছাত্র এখন practice করতে চায়, content manage করতে নয়। ২৫ দিন বাকি।
