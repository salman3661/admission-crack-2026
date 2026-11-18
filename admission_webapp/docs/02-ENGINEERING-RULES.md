# 02 · ENGINEERING RULES — প্রতিটির কারণ

Section C-এর rule গুলোর বিস্তারিত। যেগুলো **সাইট ভাঙলে** সেগুলো আগে।

---

## 🔴 Rule 1–2 · Data inline নয়, code-split করো

**সমস্যা:** বর্তমান bundle ২৭ MB (৩.৮ MB brotli)। মোবাইলে FCP ৩ সেকেন্ড, ৩G-তে ৩০–৯০ সেকেন্ড। ২ GB RAM-এর ফোনে ২৭ MB parse করতে tab crash করতে পারে। ৮টি JSON ব্লব স্টার্টআপেই `JSON.parse` হয় — ইউজার কিছু না খুলেই ৩,৭৭৬ প্রশ্ন parse করে ফেলে।

**কেন:** ৯০% ইউজার শুধু একটা paper খুলবে। বাকি ৯০% ডাউনলোড করা কেন?

**কী করো:**
```js
// ✅
const paper = await fetch('/data/du_ka/model_test/model_test_03.json').then(r => r.json());
// ✅ route-level splitting
const Mock = lazy(() => import('./routes/Mock'));
```
**লক্ষ্য:** initial payload < ৫০০ KB gzip · একটি paper খুললে শুধু ওই paper-ই download হবে।

---

## 🔴 Rule 2 · Template literal-এ content নয়

**সমস্যা:** বর্তমান code: `JSON.parse(\`[...questions...]\`)`। JS content-টা **evaluate** করে।

**প্রমাণ (সিমুলেশন করে দেখানো):**
```
একটা backtick ঢোকালে  → SyntaxError: Unexpected identifier 'ব্যাকটিক'  → পুরো bundle ক্র্যাশ
একটা ${x} ঢোকালে     → ReferenceError: x is not defined             → পুরো bundle ক্র্যাশ
```
আজকের content-এ ০টি backtick আছে, কিন্তু **১,৬২২টি প্রশ্নেই LaTeX `$…$`** আছে। পরের weekly solve sheet-এ একটা hint-এ `` ` `` থাকলেই — সব ইউজারের জন্য সাদা স্ক্রিন। এটা তোমার content-add করার workflow-র সবচেয়ে বড় ঝুঁকি।

**কী করো:** আসল `.json` ফাইল। কখনোই content template literal-এ ঢোকাবে না।

---

## 🔴 Rule 3–4 · Real URL + runtime count

**সমস্যা (হ্যাশ routing):** `#weekly`, `#paper_final` — Google URL-এর fragment ইগনোর করে। ফলে Google তোমার **২৪টি route-এর একটিও** index করতে পারে না; শুধু `/`। ১,৪৪২ প্রশ্ন, ৬৪টি chapter, master set — সব একটা URL-এর নিচে চাপা।

**সমস্যা (hardcoded count):**
```
UI বলছে  W01 = 128 MCQ      | ব্যাংকে আছে 147
UI বলছে  "৭৫০ weekly MCQ"   | আছে 1,159
UI বলছে  "৭ সপ্তাহ" / "Week 01–08" | ডেটায় ৯ সপ্তাহ
Decks tab "১,৩৪৭ প্রেডিক্টর" | Weekly tab "১,৪৪৭"  ← একই প্রোডাক্ট, দুই সংখ্যা
```
ছাত্র সাইট খুলেই এই অমিল ধরতে পারবে → বিশ্বাস হারাবে।

**কী করো:**
```js
// ✅ pathname routing + vercel.json rewrite
{ "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }] }

// ✅ সব গণনা data থেকে
const week01 = allQuestions.filter(q => q.week === 'week_01' && q.source_type === 'weekly_solve');
```
UI-তে দেখানো প্রতিটি সংখ্যা সেই মুহূর্তে loaded JSON থেকে গণনা করা হবে।

---

## 🟠 Rule 5–7 · Data integrity

**Rule 5 (duplicate id):** ১,১২৮টি id ৩–৪ বার এসেছে (৩,৪৬২ / ৩,৭৭৬ row)। React duplicate key → state bleed; একই উত্তর ৩–৪ বার সেভ হচ্ছে; counter বেশি দেখাচ্ছে।
→ Load-এ dedupe by id, `appears_in: [...]` রাখো।

**Rule 6 (track casing):** `'varsity'` 1995 · `'Varsity'` 72 · `undefined` 857 → কোনো strict filter ৭২টি প্রশ্ন silently বাদ দেয়।
→ Load-এ normalize।

**Rule 7 (optionless):** ৪৮ row-এ `options: []` → MCQ কার্ড হিসেবে render হয় কিন্তু কোনো অপশন নেই।
→ `is_written: true` হলে written card render করো (marks + model solution)।

---

## 🟠 Rule 8 · Option shuffle

**সমস্যা:** বর্তমান ব্যাংকে উত্তর **A = 41.8%**, B = 32.4%, C = 17.6%, D = 8.2% (সুষম হওয়ার কথা ~25%)।
একজন শিক্ষার্থী "সবসময় A" শিখে ৬০ MCQ-তে chance-এর চেয়ে ~১৭ নম্বর বেশি পায়। এটাই এই ধরনের অ্যাপের সবচেয়ে বড় দুর্বলতা।

**কী করো:**
```js
const shuffled = useMemo(() => shuffleStable(question.options, qid), [qid]);
const newIndex = shuffled.indexOf(question.options[question.correct_index]);
// sessionStorage-এ mapping রাখো যাতে reload-এর পরেও উত্তর ঠিক থাকে
```
**শিক্ষার্থীর কাছে এটা "শাস্তি" না, "সুরক্ষা"** — এভাবে বলো।

---

## 🟠 Rule 9 · DOMPurify

বর্তমানে `dangerouslySetInnerHTML` আছে, sanitiser নেই (DOMPurify/rehype-raw দুটোই নেই)। আজকের static ব্যাংকে exploitable নয়, কিন্তু **যেদিন তুমি নতুন coaching paper থেকে প্রশ্ন import করবে, সেদিন এটা stored XSS হয়ে যাবে**।
→ Render path-এ DOMPurify। KaTeX output OK, raw text নয়।

---

## 🟠 Rule 10–11 · Headers ও SEO

```
Cross-Origin-Opener-Policy: same-origin-allow-popups
   → Firebase পপ-আপ বন্ধ হয়েছে কিনা window.closed দিয়ে check করে।
     এটা block করলে UI "Google এ লগইন হচ্ছে..."-তে আটকে থাকতে পারে।
```
SEO: প্রতিটি route-এ unique title + description + canonical + og + JSON-LD।
`/robots.txt` ও `/sitemap.xml` **real file** — এখন দুটোই SPA fallback HTML (200) ফেরত দেয়, যা Google-এর জন্য "invalid"।

---

## 🟢 Rule 12–15 · বাকিগুলো

- **Service worker:** app shell cache করো, কিন্তু multi-MB JSON bank না। JSON-এ stale-while-revalidate। Unknown URL-এর fallback cache করো না।
- **Font:** বাংলা font self-host + subset + `font-display: swap`। এখন Google Fonts (৩৯২ KB) + maateen.me + GTM (১৬৩ KB) প্রথম paint-এই আসে।
- **Analytics:** নতুন কিছু যোগ নয় (Firebase Analytics + GA4 আছেই)।
- **Database নয়:** ছাত্র practice করতে চায়, content manage করতে নয়। Progress localStorage/IndexedDB-তেই।

---

## 📐 Performance target

| মেট্রিক | এখন | লক্ষ্য |
|---|---|---|
| Initial JS (gzip) | 3.80 MB | < 500 KB |
| Initial JS (decoded) | 27.3 MB | < 1.5 MB |
| Total first-load transfer | 4.12 MB | < 1.2 MB |
| FCP (mobile 390×844) | 3.0 s | < 1.8 s |
| Bank load (per paper) | সব ২৭ MB | সেই paper-ই (~200–800 KB) |
| Lighthouse mobile perf | ? | ≥ 70 |
