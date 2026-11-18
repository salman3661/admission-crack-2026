#!/usr/bin/env node
/**
 * coverage-scorer.js  —  তোমার real ব্যাংকের বিরুদ্ধে যেকোনো প্রশ্ন-সেট score করে।
 *
 * কেন দরকার: AI থেকে কেনা প্রশ্ন দেখতে real লাগে, কিন্তু উত্তর ভুল হতে পারে।
 * এই টুল বলে দেয় — "এই প্রশ্নটা তোমার real bank-এর কতটা কাছের? 2026-27-এ আসার সম্ভাবনা কত?"
 *
 * ইনপুট (JSON array): [{ "subject": "Physics", "question": "...", "options": [...], "answer": "A" }]
 * ইনপুট (TSV):        subject \t question \t options(pipe separated) \t answer
 *
 * ব্যবহার:
 *   node coverage-scorer.js candidates.json
 *   node coverage-scorer.js candidates.tsv --format tsv
 *   node coverage-scorer.js --demo
 */
const fs = require('fs');
const path = require('path');

// ---------- 1. real bank load ----------
// ব্যাংক local না থাকলে deployed bundle থেকে নিজে থেকেই টেনে আনে
const BANK_FILES = ['b0.json', 'b1.json', 'b2.json', 'b3.json'];
const BANK = [];
function loadBank() {
  for (const f of BANK_FILES) {
    const p = path.join(__dirname, f);
    if (fs.existsSync(p)) { JSON.parse(fs.readFileSync(p, 'utf8')).forEach(q => BANK.push(q)); }
  }
  if (!BANK.length) {
    console.log('📥 local bank নেই — deployed bundle থেকে টেনে আসছি (একবারই)...');
    const { execSync } = require('child_process');
    const url = 'https://admissionwebapp.vercel.app/assets/index-BVMUvLgv.js';
    const tmp = path.join(__dirname, '.bundle.js');
    execSync(`curl -sS --max-time 120 -o "${tmp}" "${url}"`, { stdio: 'inherit' });
    const src = fs.readFileSync(tmp, 'utf8');
    const re = /JSON\.parse\(`/g; let m, i = 0;
    while ((m = re.exec(src))) {
      let j = m.index + m[0].length, q = null;
      while (j < src.length) { if (src[j] === '\\') { j += 2; continue; } if (src[j] === '`') { q = j; break; } j++; }
      if (q === null) continue;
      const content = src.slice(m.index + m[0].length, q);
      try { const arr = JSON.parse(eval('`' + content + '`')); if (Array.isArray(arr) && arr.length && arr[0].q !== undefined) { fs.writeFileSync(path.join(__dirname, 'b' + i + '.json'), JSON.stringify(arr)); i++; } } catch (e) {}
    }
    fs.unlinkSync(tmp);
    for (const f of BANK_FILES) { const p = path.join(__dirname, f); if (fs.existsSync(p)) JSON.parse(fs.readFileSync(p, 'utf8')).forEach(q => BANK.push(q)); }
  }
}
loadBank();
if (!BANK.length) { console.error('❌ ব্যাংক লোড করা গেল না — ইন্টারনেট চেক করো।'); process.exit(1); }

const yearsOf = origin => {
  const s = String(origin || '');
  const m = s.match(/'(\d{2})(?:-(\d{2}))?/);
  if (m) { let a = +m[1]; if (a > 40) a -= 100; if (a < 10) a += 90; const o = [2000 + a]; if (m[2]) { let b = +m[2]; if (b > 40) b -= 100; if (b < 10) b += 90; o.push(2000 + b); } return o.filter(y => y >= 2010 && y <= 2026); }
  if (/Repeat 2026|MAT Line 2026|Speed Hack 2026|Bridge 2026/i.test(s)) return [2026];
  return [];
};

// ---------- 2. normalise + tokenise ----------
const STOP = new Set(['এর', 'এবং', 'ও', 'একটি', 'একটা', 'কোন', 'নিচের', 'উপরের', 'দুটি', 'এই', 'সেই', 'হয়', 'হলে', 'যদি', 'তবে', 'কি', 'সম্ভব', 'নির্ণয়', 'করো', 'করা', 'হিসেবে', 'মান', 'প্রশ্ন', 'the', 'a', 'an', 'of', 'is', 'are', 'in', 'to', 'for', 'and', 'what', 'which', 'following', 'is', 'that', 'this', 'be', 'it', 'on', 'of', 'as', 'at', 'by']);
const norm = s => String(s)
  .replace(/\\begin\{[a-z]+matrix\}/gi, ' ').replace(/\\end\{[a-z]+matrix\}/gi, ' ')
  .replace(/\\[a-zA-Z]+/g, ' ')
  // CRITICAL for Bengali: vowel signs & hasant are \p{M} (marks), not \p{L}.
  // Deleting them (instead of replacing with space) keeps words intact.
  .replace(/\p{M}+/gu, '')
  .replace(/[{}$^_\\]/g, ' ')
  .replace(/[০-৯]/g, d => String('০১২৩৪৫৬৭৮৯'.indexOf(d)))
  .replace(/[^\p{L}\p{N}\s]/gu, ' ').toLowerCase().replace(/\s+/g, ' ').trim();
const tokens = s => norm(s).split(' ').filter(t => t.length > 1 && !STOP.has(t));
// numbers carry the real signal in physics/math — keep them as separate weighted tokens
const nums = s => (String(s).match(/-?\d+(?:\.\d+)?/g) || []).map(String);

// ---------- 3. inverted index over real questions (DEDUPED by id) ----------
const SEEN = new Set();
const UNIQ = BANK.filter(q => { const k = q.id || (q.q || q.question); if (SEEN.has(k)) return false; SEEN.add(k); return true; });
console.log(`ℹ️  ব্যাংক: ${BANK.length} row → ${UNIQ.length} unique question indexed`);

const idx = new Map();      // token -> Set(questionIdx)
const SUBJ_IDX = new Map(); // subject -> Set(questionIdx)
const qTokens = UNIQ.map((q, qi) => {
  const t = new Set(tokens((q.q || q.question || '') + ' ' + (q.explanation || q.exp || '')));
  t.forEach(tok => { if (!idx.has(tok)) idx.set(tok, new Set()); idx.get(tok).add(qi); });
  if (!SUBJ_IDX.has(q.subject)) SUBJ_IDX.set(q.subject, new Set());
  SUBJ_IDX.get(q.subject).add(qi);
  return t;
});
// IDF: a token in only a few questions is highly identifying
const IDF = new Map();
idx.forEach((set, tok) => IDF.set(tok, Math.log(UNIQ.length / (1 + set.size))));

const meta = UNIQ.map(q => ({
  subject: q.subject, chapter: (q.chapter || 'UNCLASSIFIED').trim(),
  years: yearsOf(q.origin), origin: q.origin || '',
  id: q.id, text: norm(q.q || q.question || ''),
  nums: nums(q.q || q.question || '')
}));

// ---------- 4. chapter stats (the predictor signal) ----------
const chapYears = new Map(), chapSubj = new Map(), chapQ = new Map();
UNIQ.forEach((q, i) => {
  const c = (q.chapter || 'UNCLASSIFIED').trim();
  if (!chapYears.has(c)) chapYears.set(c, new Set());
  if (!chapQ.has(c)) chapQ.set(c, new Set());
  if (!chapSubj.has(c)) chapSubj.set(c, new Set());
  chapYears.get(c).add(q.subject);
  chapQ.get(c).add(q.id);
  yearsOf(q.origin).forEach(y => chapYears.get(c).add(y));
});

// exam slot value (marks at stake)
const SLOT = { 'Physics': 25, 'Chemistry': 25, 'Higher Math': 25, 'Biology': 30, 'English': 15, 'GK': 10, 'Bangla': 25, 'ICT': 25 };
const MAT_SUB = { 'Biology': 30, 'Chemistry': 25, 'Physics': 20, 'English': 15, 'GK': 10 };

// ---------- 5. score one candidate question ----------
const SUBJ_EQUIV = { 'Higher Math': ['Higher Math', 'Math'], 'Math': ['Math', 'Higher Math'] };
function scoreCandidate(c) {
  const text = String(c.question || c.q || '');
  const tk = new Set(tokens(text));
  const cNums = nums(text);
  // restrict the search pool to the SAME subject (a Physics question must match a Physics question)
  const pool = new Set();
  const allowed = SUBJ_EQUIV[c.subject] || [c.subject];
  allowed.forEach(s => { const s2 = SUBJ_IDX.get(s); if (s2) s2.forEach(i => pool.add(i)); });
  // tokens common across ALL subjects (too generic) are ignored
  const generic = new Set();
  tk.forEach(t => { const s = idx.get(t); if (!s) return; let inAll = true; for (const sub of SUBJ_IDX.keys()) { if (![...s].some(i => SUBJ_IDX.get(sub).has(i))) { inAll = false; break; } } if (inAll) generic.add(t); });

  let best = null, bestJ = 0;
  const cand = new Set();
  tk.forEach(t => { if (generic.has(t)) return; const s = idx.get(t); if (s && s.size < 900) s.forEach(i => { if (pool.has(i)) cand.add(i); }); });

  for (const i of cand) {
    const bt = qTokens[i];
    let inter = 0, wsum = 0;
    tk.forEach(t => {
      const w = IDF.get(t) || 1;
      wsum += w;
      if (bt.has(t)) inter += w;
    });
    // numeric agreement bonus (physics/math)
    const bn = meta[i].nums;
    let numHit = 0;
    cNums.forEach(n => { if (bn.includes(n)) numHit++; });
    const numBonus = cNums.length ? (numHit / cNums.length) * 0.25 : 0;
    const j = Math.min(1, (wsum ? inter / wsum : 0) + numBonus);
    if (j > bestJ) { bestJ = j; best = meta[i]; }
  }
  // chapter guess from matched question
  let chapter = null, years = 0, nInChapter = 0, nearDup = false;
  if (best) {
    chapter = best.chapter;
    const yrs = new Set();
    UNIQ.forEach(q => { if ((q.chapter || 'UNCLASSIFIED').trim() === chapter) yearsOf(q.origin).forEach(y => yrs.add(y)); });
    years = yrs.size;
    nInChapter = chapQ.get(chapter)?.size || 0;
    nearDup = bestJ >= 0.55;
  }
  // score components
  const chapterConfidence = years ? Math.min(1, years / 10) : 0;
  const dupBonus = nearDup ? 35 : 0;
  const similarity = Math.round(bestJ * 35);
  const slot = SLOT[c.subject] || 10;
  const slotBonus = Math.round((slot / 30) * 20);
  const matSlot = MAT_SUB[c.subject] || 0;
  const matBonus = matSlot ? Math.round((matSlot / 30) * 10) : 0;
  const score = Math.min(100, Math.round(dupBonus + similarity + chapterConfidence * 25 + slotBonus + matBonus));
  let verdict, note;
  if (nearDup) { verdict = 'REAL-PAST'; note = `ব্যাংকের আসল প্রশ্নের সাথে ${(bestJ * 100).toFixed(0)}% মিল — repeat-এর সবচেয়ে শক্তিশালী প্রশ্ন`; }
  else if (bestJ >= 0.38) { verdict = 'NEAR-REAL'; note = `ব্যাংকের কাছাকাছি (${(bestJ * 100).toFixed(0)}%), chapter "${chapter}" ${years} বছরে এসেছে`; }
  else if (bestJ >= 0.18) { verdict = 'TOPIC-MATCH'; note = `শুধু topic মেলে, প্রশ্ন নতুন — chapter "${chapter}" ${years} বছরে এসেছে`; }
  else { verdict = 'UNVERIFIED'; note = 'তোমার ব্যাংকে এর কাছাকাছি কিছু নেই — উত্তর যাচাই করো'; }
  return { score, verdict, note, chapter, years, similarity: bestJ, nearDup, slot, matSlot };
}

// ---------- 6. input parsing ----------
function parseArgs() {
  const a = process.argv.slice(2);
  let file = null, format = 'json';
  for (let i = 0; i < a.length; i++) {
    if (a[i] === '--format') format = a[++i];
    else if (a[i] === '--demo') file = '--demo';
    else if (!a[i].startsWith('--')) file = a[i];
  }
  return { file, format };
}
function loadCandidates(file, format) {
  const raw = fs.readFileSync(file, 'utf8');
  if (format === 'tsv' || file.endsWith('.tsv')) {
    return raw.split('\n').filter(Boolean).map(l => {
      const [subject, question, opts, answer] = l.split('\t');
      return { subject: subject?.trim(), question: question?.trim(), options: (opts || '').split('|'), answer: answer?.trim() };
    });
  }
  const j = JSON.parse(raw);
  return Array.isArray(j) ? j : (j.questions || j.data || []);
}

// ---------- 7. main ----------
const { file, format } = parseArgs();
if (!file) {
  console.log(`coverage-scorer — তোমার real ব্যাংকের বিরুদ্ধে প্রশ্ন-সেট score করে

ব্যবহার:
  node coverage-scorer.js candidates.json
  node coverage-scorer.js candidates.tsv --format tsv
  node coverage-scorer.js --demo

ইনপুট JSON: [{"subject":"Physics","question":"...","options":["..","..","..",".."],"answer":"A"}]
ইনপুট TSV : subject \\t question \\t "opt1|opt2|opt3|opt4" \\t answer

আউটপুট: score 0-100, verdict (REAL-PAST / NEAR-REAL / TOPIC-MATCH / UNVERIFIED), matched chapter, years hit`);
  process.exit(0);
}
let cands;
if (file === '--demo') {
  cands = [
    { subject: 'Physics', question: 'দীর্ঘ সরল পরিবাহীতে চৌম্বক ক্ষেত্র $B = \\frac{\\mu_0 I}{2\\pi r}$। একটি লাইনে 40 A প্রবাহিত হলে 1.0 m দূরত্বে চৌম্বক ক্ষেত্র কত?', options: ['$8\\times10^{-6}$ T', '$4\\times10^{-6}$ T', '$8\\times10^{-5}$ T', '$4\\times10^{-5}$ T'], answer: 'A' },
    { subject: 'Physics', question: 'একটি চৌম্বকক্ষেত্রে 0.05 T ঘনত্ব আছে এবং ক্ষেত্রের ক্ষেত্রফল 0.02 m²। চৌম্বক ফ্লাক্স কত?', options: ['0.001 Wb', '0.0001 Wb', '0.01 Wb', '2.5 Wb'], answer: 'A' },
    { subject: 'Chemistry', question: 'জৈব রসায়নে বেনজিন বলয়ের সক্রিয়কারী প্রতিস্থাপন কোনো?', options: ['অ্যালকাইন', 'অ্যারোম্যাটিক', 'অ্যালিফ্যাটিক', 'কার্বোসাইক্লিক'], answer: 'B' },
    { subject: 'Biology', question: 'মানব শিশুর দুধদাঁতের সংকেতে কোন ধরনের দাঁত সম্পূর্ণ অনুপস্থিত থাকে?', options: ['দাঁতের দাড়ি', 'দুধের দাঁত', 'চিরস্থায়ী দাঁত', 'কার্যকর দাঁত'], answer: 'A' }
  ];
  console.log('--- DEMO (৪টি sample প্রশ্ন) ---\n');
} else {
  cands = loadCandidates(file, format);
}

const rows = cands.map(c => ({ ...c, ...scoreCandidate(c) }));
const cols = ['subject', 'score', 'verdict', 'chapter', 'years', 'similarity', 'question'];
const csv = [cols.join(',')].concat(rows.map(r => [
  r.subject, r.score, r.verdict, `"${(r.chapter || '').replace(/"/g, '""')}"`, r.years,
  (r.similarity || 0).toFixed(2), `"${String(r.question || '').replace(/"/g, '""').replace(/[\n\r]/g, ' ').slice(0, 200)}"`
].join(','))).join('\n');
const outFile = path.join(__dirname, '..', 'output', 'coverage-score-' + path.basename(file).replace(/\.[^.]+$/, '') + '.csv');
try { fs.mkdirSync(path.dirname(outFile), { recursive: true }); fs.writeFileSync(outFile, csv); console.log(`📄 score sheet লেখা হয়েছে: ${outFile}\n`); } catch (e) { console.log('(score sheet লেখা যায়নি)\n'); }

console.log('score | verdict      | yrs | chapter                              | question');
rows.forEach(r => console.log(`${String(r.score).padStart(5)} | ${r.verdict.padEnd(12)} | ${String(r.years || '-').padStart(3)} | ${String(r.chapter || '-').slice(0, 36).padEnd(36)} | ${String(r.question || '').slice(0, 52)}`));

const n = rows.length || 1;
const avg = rows.reduce((a, r) => a + r.score, 0) / n;
const real = rows.filter(r => r.verdict === 'REAL-PAST').length;
const near = rows.filter(r => r.verdict === 'NEAR-REAL').length;
const unver = rows.filter(r => r.verdict === 'UNVERIFIED').length;
console.log(`\n=== সারসংক্ষেপ ===`);
console.log(`  প্রশ্ন: ${rows.length} | গড় score: ${avg.toFixed(1)}/100`);
console.log(`  REAL-PAST (ব্যাংকের আসল প্রশ্ন): ${real} (${(real / n * 100).toFixed(0)}%)`);
console.log(`  NEAR-REAL: ${near} (${(near / n * 100).toFixed(0)}%)`);
console.log(`  UNVERIFIED (যাচাই করা যায়নি): ${unver} (${(unver / n * 100).toFixed(0)}%)`);
if (unver > n * 0.4) console.log(`  ⚠️  ৪০%+ প্রশ্ন তোমার real ব্যাংকে নেই — উত্তর অবশ্যই হাতে-কলমে যাচাই করো।`);
console.log(`\n  মনে রাখো: chapter-level backtest-এ top-8 chapter মাত্র 77.9% coverage দেয়,`);
console.log(`  exact #1 chapter hit 13%। তাই "100% exact question" কোনো method-এই সম্ভব নয়।`);
