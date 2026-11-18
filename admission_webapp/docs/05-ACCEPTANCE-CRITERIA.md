# 05 · ACCEPTANCE CRITERIA — শেষ হয়েছে কিনা agent কে যাচাই করতে হবে

Agent-কে বলো: **"প্রতিটি আইটেমের সাথে প্রমাণ দাও — সংখ্যা, ব্যবহারিকতা, adjective নয়।"**

---

## A · Performance

| # | মানদণ্ড | প্রমাণ |
|---|---|---|
| A1 | Initial JS payload < ৫০০ KB gzip | build output-এর সংখ্যা |
| A2 | Initial JS decoded < ১.৫ MB | `dist/assets/*.js` ls -la |
| A3 | একটি paper খুললে শুধু ওই paper-ই download হয় | Network tab-এর screenshot |
| A4 | FCP (mobile, throttled) < ১.৮ সেকেন্ড | Lighthouse বা performance timeline |
| A5 | Lighthouse mobile Performance ≥ ৭০ | score report |
| A6 | কোনো route-এ console error নেই | সব route-এর console log |

## B · Data integrity

| # | মানদণ্ড | প্রমাণ |
|---|---|---|
| B1 | `scripts/validate-data.mjs` → **0 error** | command output |
| B2 | Duplicate id = 0 | validator output |
| B3 | Optionless MCQ card = 0 (written হলে written card) | validator + একটা screen |
| B4 | সব গণনা runtime-এ — source-এ কোনো hardcoded total নেই | grep: কোনো কোডে "1,347" বা "22,807" নেই |
| B5 | UI-র দেখানো সংখ্যা data-র সাথে মেলে | একটা পরীক্ষা: UI number == data count |
| B6 | Answer position shuffle কাজ করে, reload-এর পরেও উত্তর ঠিক থাকে | reload করে একই প্রশ্নে উত্তর মিলাও |
| B7 | প্রতিটি master-set প্রশ্ন real bank-এর সাথে মেলে | `coverage-scorer` → 100% REAL-PAST |
| B8 | chapter_id সব taxonomy-তে আছে | validator |

## C · Features

| # | মানদণ্ড | প্রমাণ |
|---|---|---|
| C1 | Drill: MCQ + Written দুটোই কাজ করে | screenshot |
| C2 | Simulator: exact structure, timer, −0.25, per-subject score | একটা সম্পূর্ণ run-এর scorecard |
| C3 | Written-এ খালি রাখা যায় না (না থাকলে warning) | screenshot |
| C4 | Error log persist হয় reload-এর পরেও | browser check |
| C5 | Mistake book due প্রশ্ন দেখায় | screenshot |
| C6 | Weakness radar per chapter কাজ করে, drill-এ যায় | screenshot |
| C7 | Master set A/B/C আলাদা, overlap ০ | set তুলনা |
| C8 | প্রতিটি প্রশ্নে provenance দেখায় (source, বছর, yearsHit) | screenshot |

## D · SEO & deploy

| # | মানদণ্ড | প্রমাণ |
|---|---|---|
| D1 | প্রতিটি route-এ unique title + description | ৩টি route-এর meta তুলনা |
| D2 | canonical + og:* + twitter:card আছে | head output |
| D3 | JSON-LD যাচাই করা (Google Rich Results Test) | test result |
| D4 | `/robots.txt` real content (SPA fallback নয়) | curl output |
| D5 | `/sitemap.xml` real content, সব canonical URL সহ | curl output |
| D6 | অচেনা path → 404 (200 নয়) | curl output |
| D7 | COOP header আছে | `curl -I` |
| D8 | DOMPurify render path-এ | import দেখাও |

## E · Predictor

| # | মানদণ্ড | প্রমাণ |
|---|---|---|
| E1 | Leave-one-year-out backtest সংখ্যা দেয় | coverage % + #1 rank hit % |
| E2 | Coaching Model Test-কে held-out validation হিসেবে ব্যবহার করা হয় | per-model-test coverage % |
| E3 | Master set chapter-বণ্টন predicted-র সাথে মিলে | chapter-map + TVD |
| E4 | `source_type` weight আসলে কাজ করে (A ও B-তে coaching paper বেশি) | source_type distribution |

## F · সাধারণ

| # | মানদণ্ড |
|---|---|
| F1 | বাংলা UI copy অপরিবর্তিত |
| F2 | ডিজাইন token, রঙ, typography অপরিবর্তিত |
| F3 | README-তে নতুন paper যোগ করার নিয়ম |
| F4 | কোনো hardcoded সংখ্যা source-এ নেই |
| F5 | কোনো নতুন backend/database নেই |

---

## REPORT.md-তে agent যা লিখবে

```markdown
## Acceptance Evidence
| ID | Criterion | Result | Proof |
|----|-----------|--------|-------|
| A1 | Initial JS gzip < 500KB | 412 KB | dist output |
| B2 | Duplicate ids | 0 | validator output |
| E1 | Backtest coverage | 81.3% | backtest.json |
...

## Decisions Taken (1 line each)
- MAT Physics quota: used 20 (sources conflict 15 vs 20; DGME circular pending)

## Known Gaps
- Written paper bank: only 16 rows, all Week 09 — needs 3 more per subject
```

**"Done" বলার আগে সব আইটেমের সাথে সংখ্যা।**
