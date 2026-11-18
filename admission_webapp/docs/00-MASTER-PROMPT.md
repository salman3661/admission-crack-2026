# 00 · MASTER PROMPT — তোমার webapp পুনর্গঠনের সম্পূর্ণ স্পেক

> **ব্যবহার:** নিচের পুরো ব্লকটি একটি AI coding agent-কে (Claude Code / Cursor / Windsurf / GPT-5 Codex) দাও। অন্য ফাইলগুলো (`docs/`, `data/`, `scripts/`) সাপোর্টিং রেফারেন্স হিসেবে দাও — মাস্টার প্রম্পট নিজেই সম্পূর্ণ।

---

```
You are rebuilding a React + Vite + Tailwind admission-exam webapp for a Bangladeshi
HSC student. The student is the only user. Two exams matter:
  • DU 'Ka' (Science Unit) — 12 Dec 2026, 11:00–12:30
      MCQ 60 (45 min, −0.25 each wrong) + Written 40 (45 min) = 100, +20 GPA
      4 subjects × 25 marks (15 MCQ + 10 written): Physics & Chemistry compulsory,
      plus 2 of {Higher Math, Biology, Bangla, English, ICT}
      Pass: 24 MCQ + 12 written + 40 total
  • MAT (MBBS) — 18 Dec 2026, 100 MCQ, 75 min, −0.25 each wrong, pass 40
      Biology 30 + Chemistry 25 + Physics 20 + English 15 + GK 10

GOAL: help the student score 78–80+ by turning a question bank into a
prediction + practice engine. The student has ~25 days.

═══════════════════════════════════════════════════════════════════
SECTION A — WHAT EXISTS TODAY
═══════════════════════════════════════════════════════════════════
Deployed at https://admissionwebapp.vercel.app (Vite build, React, Tailwind).
It works — no runtime errors, all 13 routes render. KEEP: the visual design, the
Bengali UI copy, the drill interaction, the KaTeX math rendering, the PWA shell.
REPLACE: the data layer, the counting, the routing/SEO, the build config.

Known problems (all verified by inspecting the deployed bundle):
 1. 27 MB single JS bundle (3.8 MB brotli) — every question bank is inlined as
    JSON.parse(`...`) inside the bundle. Parsed eagerly at startup.
 2. Content embedded in template literals — one backtick or ${ in a new question
    bricks the whole site (proved by simulation).
 3. Duplicate ids: 1,128 ids appear 3–4× (3,462 of 3,776 rows).
 4. 48 rows have zero options → render as unanswerable cards.
 5. UI counts are hardcoded and wrong: UI says week 1 = 128 MCQ, bank has 147.
    UI says "750 weekly MCQ" (bank: 1,159) and "Week 01–08 / 7 weeks" (data has 9).
    Decks tab says "1,347 predictors", Weekly tab says "1,447" — same product.
 6. `track` values inconsistent: 'varsity' 1995 / 'Varsity' 72 / undefined 857.
 7. Answer position bias: A 41.8% / B 32.4% / C 17.6% / D 8.2% (should be ~25%).
 8. dangerouslySetInnerHTML with no sanitiser (DOMPurify/rehype-raw absent).
 9. `index.html` has no meta description, no og:*, no twitter:card, no canonical,
    no JSON-LD. /robots.txt and /sitemap.xml return the SPA HTML with HTTP 200.
10. Hash routing (#weekly) — only "/" is indexable. 24 routes invisible to Google.
11. Login modal promises "saved securely in the cloud" but Firestore is not
    enabled in the project; all progress lives in localStorage only.
12. Cross-Origin-Opener-Policy error blocks Firebase's popup-close detection.

═══════════════════════════════════════════════════════════════════
SECTION B — DATA SCHEMA (use exactly this)
═══════════════════════════════════════════════════════════════════
One question = one object. Full spec: docs/01-DATA-SCHEMA.md
Reference data already normalised: data/bank-normalized.json (1,442 rows)

{
  "id": "pf01_physics_q01",        // globally unique, source-scoped
  "source_type": "model_test",     // past_paper | weekly_solve | paper_final
                                    // | subject_final | model_test
  "source_name": "Model Test 03",  // which paper
  "exam": "du_ka",                 // du_ka | mat | ru | ju | cu | gst | eng_bridge
  "exam_year": 2026,
  "exam_date": "2026-12-05",
  "subject": "Physics",            // Physics|Chemistry|Higher Math|Biology|English|Bangla|ICT|GK
  "chapter_id": "phy_vector",      // stable slug, snake_case
  "chapter_name": "ভেক্টর (Vector)", // human-readable Bengali
  "mega_type": "Type 1: ...",      // optional
  "question": "…",
  "options": ["…","…","…","…"],    // [] for written questions
  "correct_index": 0,              // null for written
  "explanation": "…",
  "trap": "…",
  "is_written": false,
  "marks": 1,                      // 1 for MCQ, 2–5 for written
  "duration_sec": 45,              // 45 for MCQ, ~240 for written
  "probability_label": "98% DU 'Ka' Pattern Repeat"  // keep, but never trust it
}

CRITICAL — the student is adding coaching papers you do not have yet:
  weekly solve sheets (9), Paper Final (10), Subject Final (per subject),
  Model Test (5). These are the highest-value data in the system because they
  are real exam-pattern papers. You MUST tag them with source_type exactly as
  above, and with exam_date. The predictor weights them accordingly (Section E).

═══════════════════════════════════════════════════════════════════
SECTION C — ENGINEERING RULES (non-negotiable)
═══════════════════════════════════════════════════════════════════
1. DATA IS NEVER INLINED IN JS.
   Put questions in src/data/<exam>/<source_type>/<source_name>.json
   (one JSON per paper; legacy bank-কে prepare-data.mjs
   <exam>/<source_type>/<subject>.json হিসেবে split করে, ৫৫টি ফাইল).
   Import them with dynamic import() or fetch() at the
   moment the drill opens. Never JSON.parse(`...`) a template literal —
   a single backtick or ${ in content must never be able to break the build.
2. CODE SPLITTING.
   React.lazy() per route. Shell bundle target < 500 KB gzip. The bank must
   never be in the initial payload.
3. ROUTING = REAL URLS, NOT HASH.
   Use pathname routing (/weekly, /paper-final, /subject/chemistry,
   /mock/03, /chapter/phy_vector). Add a Vercel rewrite so all paths serve
   index.html, and add a real 404. 24+ indexable URLs are the goal.
4. EVERY COUNT IS COMPUTED AT RUNTIME.
   Delete every hardcoded number (week counts, "1,347 predictors", "22,807",
   "750 MCQ", "7 weeks"). Derive them from the data. If a number is shown,
   it is computed from the loaded JSON in that same render.
5. IDs ARE UNIQUE, BANK IS DEDUPED.
   Load, dedupe by id, and if the same question text appears in two papers keep
   ONE row with a `appears_in: ["pf01","mt03"]` array so progress is not
   double-counted. Never let two rows share an id.
6. TRACK/SUBJECT VALUES ARE NORMALISED AT LOAD TIME.
   One enum, one spelling. No 'Varsity' vs 'varsity'.
7. NO OPTIONLESS MCQ CARDS.
   A question with options: [] must render as a WRITTEN card (marks, model
   solution, "সিলেবাস স্টাইলে লিখো" prompt), never as a broken MCQ.
8. ANSWER POSITION IS SHUFFLED PER SESSION.
   Shuffle options on first render, keep a stable mapping in session state, and
   persist the mapping so a saved answer still maps to the same option after
   a reload. Correct index must be re-derived after shuffle. (Current bank is
   41.8% A — students must not learn "always pick A".)
9. SANITISE ALL HTML.
   The math/markdown renderer uses dangerouslySetInnerHTML. Pipe it through
   DOMPurify. KaTeX output is fine; raw question text is not trusted.
10. HEADERS (vercel.json):
    Cross-Origin-Opener-Policy: same-origin-allow-popups
    Content-Security-Policy: default-src 'self'; script-src 'self' https://accounts.google.com https://www.googletagmanager.com 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://fonts.maateen.me; font-src 'self' https://fonts.gstatic.com https://fonts.maateen.me data:; img-src 'self' data: https://api.dicebear.com;
    Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
11. SEO PER ROUTE (react-helmet-async or equivalent):
    unique <title> + <meta name="description"> + canonical + og:title/og:description/
    og:image (1200×630, absolute URL) + twitter:card. Plus JSON-LD:
    Quiz/Question on question pages, FAQPage, SoftwareApplication, Organization,
    BreadcrumbList. Real public/robots.txt and public/sitemap.xml (never the SPA
    fallback). A 404 page.
12. SERVICE WORKER: cache the app shell (HTML/CSS/JS) but NOT the multi-MB JSON
    bank. Use stale-while-revalidate for JSON. Do not cache unknown-URL fallbacks.
13. FONT: self-host a subset of the Bengali font, font-display: swap. Do not
    load Google Fonts + maateen.me + GTM all at once on first paint.
14. NO NEW ANALYTICS BEYOND the existing Firebase Analytics + GA4 unless asked.
15. Do not add a database, a backend, or an admin panel. The student wants to
    PRACTISE, not to manage content. Progress stays in localStorage (or
    IndexedDB if a single item exceeds the 5 MB localStorage cap).

═══════════════════════════════════════════════════════════════════
SECTION D — FEATURES (build in this order, stop after each is done)
═══════════════════════════════════════════════════════════════════
P0 · MUST HAVE
  F1. Library layer: load paper JSON on demand, dedupe, normalise, index by
      subject/chapter/exam/source_type. One module, used everywhere.
  F2. Drill runner: MCQ mode (one question at a time, 45 s soft timer,
      option shuffle, immediate feedback + explanation + trap) and
      Written mode (question + marks + timer, model answer reveal).
  F3. Real exam simulator: full paper, exact structure, 45 min MCQ then 45 min
      written (DU Ka) or 75 min (MAT), −0.25 per wrong MCQ, partial credit on
      written, final score out of 100, per-subject breakdown.
  F4. Master Set view: the 3 curated sets per exam (SET-A / SET-B / SET-C),
      loaded from src/data/master/*.json, with chapter labels.
  F5. Error log: every answered question stored locally with
      {qid, myAnswer, correct, whyWrong, chapter, source_type, retestDue}.
      A "Mistake Book" screen that re-serves due mistakes (SM-2 style
      intervals 1 / 3 / 7 / 14 days).
  F6. Weakness radar: per subject and per chapter — attempted, correct, and
      marks lost. Bar chart, sorted by marks lost. Clickable → drills that
      chapter only.
  F7. Mock tracker: score sheet per mock (per-subject MCQ + written, MCQ
      accuracy, minutes used, top-3 lossy chapters). Matches
      data/mock-tracker-template.csv.
  F8. Chapter explorer: 64+ chapters (data/chapter-taxonomy.csv) with question
      count, years hit, predicted 2026-27 MCQ count, and a drill button.

P1 · HIGH VALUE
  F9. Formula cards (366 from data/bank-normalized.json's companion file) —
      searchable, per chapter, printable view.
  F10. GK monthly cards (from the app's existing monthly GK dataset).
  F11. Flashcards (216 existing) in the same drill UI.
  F12. Exam-day timer screen: 45/45 or 75 min, attempt strategy helper that
      shows which questions are below 20% confidence.
  F13. "Theory of the question": for each question show chapter, source paper,
      year, mega-type, and "কত বছরে এসেছে" — the provenance that makes it
      feel real, not generated.
  F14. PWA install prompt for iOS, offline shell.

P2 · ONLY IF EVERYTHING ABOVE IS DONE AND VERIFIED
  F15. Google login (Firebase) with the corrected copy — do not promise cloud
      sync unless Firestore is actually enabled with rules.
  F16. The webapp domain → custom domain, sitemap, robots, JSON-LD (Section C).

DO NOT BUILD (explicitly out of scope):
  · question-generation by AI · admin/authoring panel · chat/AI tutor ·
    social features · payments · a database · a PWA push-notification system.

═══════════════════════════════════════════════════════════════════
SECTION E — THE PREDICTOR (this is the core value, not the UI)
═══════════════════════════════════════════════════════════════════
Full spec: docs/03-PREDICTOR-SPEC.md

LEARN → PREDICT → SELECT, run offline in a script (scripts/build-master-set.mjs):

LEARN (from ALL past papers 2010–2026, weighted by source_type):
  weight(source_type) = {
    model_test:      1.00,   ← coaching model tests are exam-pattern papers
    paper_final:     0.95,   ← coaching paper finals
    subject_final:   0.90,   ← coaching subject finals
    past_paper:      0.85,   ← real DU/MAT/RU/JU/CU/GST papers
    weekly_solve:    0.70    ← coaching weekly solve sheets
  }
  For each (subject, chapter):
    · per-year share of that subject's questions
    · distinct years it appeared in
    · distinct source_papers it appeared in   ← NEW, strongest signal
  Recency weight: 0.86^(2025 - year)

PREDICT (2026-27):
  p(chapter | subject) = Σ over years  recency(y) × weight(source_type) × share(y)
  expected_mcq(chapter) = 15 × p   (DU Ka, per subject)
                       = subject_quota × p   (MAT)

SELECT (build the master sets):
  score(q) = p(chapter|subject) × recency(q) × repeatYears(chapter) ×
              sourceWeight(q.source_type) × 0.68^(taken from same chapter) ×
              0.90^(taken from same year)
  constraints:
   · seed one question from every chapter whose expected_mcq ≥ 0.4
   · cap per chapter at ceil(expected_mcq × 1.7)  ← stops one chapter eating the set
   · cap per year at 38% of the set
   · SET-A and SET-B must not share a single question
   · SET-C = wildcard: low-probability chapters + other universities'
     (RU/JU/CU/GST) questions from the SAME chapter (their syllabus overlaps)

VALIDATE (this is what makes it credible — run it and report numbers):
  · leave-one-year-out backtest: predict year Y from years < Y, measure
    (a) what % of year Y's questions fall in the top-8 predicted chapters
        → current baseline 77.9%
    (b) how often the actual #1 chapter is ranked #1 → current baseline 13%
  · once the coaching Model Test papers are ingested, treat each as a HELD-OUT
    validation set: predict its chapter mix from the earlier data, measure the
    overlap. This is the single most informative number the app can show.
  · every question in a master set must trace back to a real source row
    (no synthetic rows). scripts/coverage-scorer.mjs proves this.

═══════════════════════════════════════════════════════════════════
SECTION F — ACCEPTANCE CRITERIA (the agent must show evidence for each)
═══════════════════════════════════════════════════════════════════
Full list: docs/05-ACCEPTANCE-CRITERIA.md
  1. Initial JS payload < 500 KB gzip (show the build output).
  2. Opening a 100-question paper downloads only that paper's JSON.
  3. Every count rendered in the UI equals a count computed from the data
     (show the test). No hardcoded totals remain in the source.
  4. Zero duplicate ids after dedupe. Zero optionless MCQ cards.
  5. Option shuffle is active and the answer key still grades correctly
     after a page reload.
  6. DOMPurify is in the render path (show the import).
  7. Every route has unique title + description + canonical + JSON-LD.
     /robots.txt and /sitemap.xml return real content, not the SPA fallback.
  8. scripts/validate-data.mjs passes with 0 errors on the final dataset.
  9. Backtest numbers reported: top-8 coverage % and #1 rank hit %.
 10. No console errors on any route; Lighthouse mobile performance ≥ 70.
 11. Existing visual design and Bengali copy preserved.
 12. A README explains how to add a new paper (drop a JSON file, run
     scripts/build-master-set.mjs, rebuild).

═══════════════════════════════════════════════════════════════════
SECTION G — HOW TO WORK
═══════════════════════════════════════════════════════════════════
· Work in phases: (1) data layer + library + dedupe, (2) drill + simulator,
  (3) error log + weakness radar + tracker, (4) master sets + predictor,
  (5) SEO + performance + PWA.
· After each phase, run scripts/validate-data.mjs and report the result.
· Never rewrite the Bengali UI copy. Fix numbers, logic and structure.
· Never invent question content. Only use rows that exist in a source file.
· If a requirement is ambiguous, choose the option that keeps the student
  practising and show the decision in one line.
· Keep the existing design tokens, colours, and typography.

DELIVER: a working repo, a REPORT.md with the acceptance evidence (numbers,
not adjectives), and the updated dataset in src/data/.
```

---

## এই প্রম্পটের সাথে যা দেবে

| ফাইল | কী |
|---|---|
| `docs/01-DATA-SCHEMA.md` | schema, tagging rule, নতুন coaching paper যোগ করার নিয়ম |
| `docs/02-ENGINEERING-RULES.md` | Section C-এর ১৫টি rule বিস্তারিত, কেন কেন |
| `docs/03-PREDICTOR-SPEC.md` | LEARN→PREDICT→SELECT, weight, validation, backtest |
| `docs/04-FEATURES-SCOPE.md` | F1–F16 বিস্তারিত, P0/P1/P2 ভাগ |
| `docs/05-ACCEPTANCE-CRITERIA.md` | যাচাইয়ের পুরো checklist |
| `data/bank-normalized.json` | তোমার ১,৪৪২ প্রশ্ন **নতুন schema-তে** (reference) |
| `data/chapter-taxonomy.csv` | ৬৪টি chapter: slug + readable নাম + বছর + source type |
| `data/sample-question.json` | ৫টি example row (একটি written সহ) |
| `data/mock-tracker-template.csv` | mock tracker-এর কলাম |
| `scripts/validate-data.mjs` | CI data-lint — duplicate id, zero-option, count mismatch, A-bias |
| `scripts/build-master-set.mjs` | master set builder (source_type weight সহ) |
| `scripts/coverage-scorer.mjs` | যেকোনো প্রশ্ন-সেট score করা |
| `README.md` | kit কীভাবে ব্যবহার করবে |

> ⚠️ **ROUND 2 — পড়া বাকি আছে:** `docs/06-NEW-FEATURES.md`
> (A1 week-filter fix, A2 text-dedup, F17 Practice-Question Matcher,
> F18 Account corner + progress, F19 Bookmark, F20 Unified Formula page,
> F21 Week/Chapter/Topic drill)। ১৮ নভে ২০২৬-এর live audit-এ এগুলোর
> সংখ্যা যাচাই করা আছে — অনুমান নয়।
