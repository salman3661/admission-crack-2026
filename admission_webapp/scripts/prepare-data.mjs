// তোমার ব্যাংক → নতুন normalized schema + chapter taxonomy (Round 2: A1 week, A2 text-dedup + appears_in, A3 du_ka relabel)
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { gzipSync } from 'zlib';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const OUT = path.join(HERE, '..');
const DATA_DIR = fs.existsSync(path.join(OUT, 'src', 'data')) ? path.join(OUT, 'src', 'data') : path.join(OUT, 'data');
const CACHE = path.join(HERE, '.bankcache');
const BUNDLE_URL = process.env.BANK_URL || 'https://admissionwebapp.vercel.app/assets/index-BVMUvLgv.js';

function loadBank() {
  const localParts = ['b0.json', 'b1.json', 'b2.json', 'b3.json'].map(f => path.join(HERE, f));
  if (localParts.every(p => fs.existsSync(p))) {
    const bank = [];
    for (const p of localParts) bank.push(...JSON.parse(fs.readFileSync(p, 'utf8')));
    return bank;
  }
  if (fs.existsSync(CACHE)) return JSON.parse(fs.readFileSync(CACHE, 'utf8'));
  const tmp = path.join(HERE, '.b.js');
  execSync(`curl -sS --max-time 150 -o "${tmp}" "${BUNDLE_URL}"`, { stdio: 'inherit' });
  const src = fs.readFileSync(tmp, 'utf8');
  const re = /JSON\.parse\(`/g;
  let m;
  const bank = [];
  while ((m = re.exec(src))) {
    let j = m.index + m[0].length, q = null;
    while (j < src.length) {
      if (src[j] === '\\') { j += 2; continue; }
      if (src[j] === '`') { q = j; break; }
      j++;
    }
    if (q === null) continue;
    try {
      const a = JSON.parse(eval('`' + src.slice(m.index + m[0].length, q) + '`'));
      if (Array.isArray(a) && a.length && a[0].q !== undefined) bank.push(...a);
    } catch (e) {}
  }
  fs.unlinkSync(tmp);
  fs.writeFileSync(CACHE, JSON.stringify(bank));
  return bank;
}

const BANK = loadBank();
const seenId = new Set();
const U = BANK.filter(q => {
  const k = q.id || (q.q || q.question);
  if (seenId.has(k)) return false;
  seenId.add(k);
  return true;
});

// বাংলা অক্ষর রাখি (URL-encode করে কাজ করবে), শুধু punctuation ও ব্যবধান বদলাই
const slug = s => String(s || '').replace(/\([^)]*\)/g, '').trim()
  .replace(/[^\p{L}\p{N}\s_-]/gu, ' ').replace(/\s+/g, '_').replace(/_+/g, '_')
  .replace(/^_|_$/g, '').slice(0, 48) || 'x';

function sourceType(o, bank) {
  const s = String(o || '');
  if (/Weekly|Solve Sheet|B-0\d|W-0\d/i.test(s) && !/Paper Final|Model/i.test(s)) return 'weekly_solve';
  if (/Paper\s*Final/i.test(s)) return 'paper_final';
  if (/Model\s*Test/i.test(s)) return 'model_test';
  if (/Subject\s*Final/i.test(s)) return 'subject_final';
  if (/MAT\s*Line\s*2026|DU-MAT\s*Repeat\s*2026|Speed Hack 2026/i.test(s)) return 'weekly_solve';
  return 'past_paper';
}

const isDuWeekly = /weekly\s*0\d\s*varsity|speed hack|weekly exam W-0\d|W-0\d\s+weekly\s+exam|W-0\d daily/i;

function examOf(o) {
  const s = String(o || '');
  if (/MAT|Medical|DMC/i.test(s)) return 'mat';
  if (/DU |DU-|Hubohu|Dhaka University/i.test(s)) return 'du_ka';
  if (/^RU |RU-/i.test(s)) return 'ru';
  if (/^CU |CU-/i.test(s)) return 'cu';
  if (/^JU |JU-/i.test(s)) return 'ju';
  if (/GST/i.test(s)) return 'gst';
  if (/Engineering Bridge/i.test(s)) return 'eng_bridge';
  if (isDuWeekly.test(s)) return 'du_ka';
  return 'other';
}

function yearOf(o) {
  const s = String(o || '');
  const m = s.match(/'(\d{2})(?:-(\d{2}))?/);
  if (m) {
    let a = +m[1];
    if (a > 40) a -= 100;
    if (a < 10) a += 90;
    return 2000 + a;
  }
  if (/2026/.test(s)) return 2026;
  return null;
}

function inferWeek(id, src) {
  const wm = /^w(\d)(?:_|\b)/i.exec(String(id || ''));
  if (wm) return parseInt(wm[1], 10);
  const s = /(?:^|[\s\-/])(?:week(?:ly)?[\s\-]*0?(\d)|w[\-\s]?0?(\d)|[\w]0(\d)\b)/i.exec(String(src || ''));
  if (s) {
    const n = parseInt(s[1] || s[2] || s[3], 10);
    if (n >= 1 && n <= 9) return n;
  }
  return null;
}

function readChapter(raw, mega) {
  const r = String(raw || '').trim();
  if (!r || r === 'UNCLASSIFIED') return null;
  if (/^(bio_|math_)/.test(r)) {
    const m = String(mega || '').replace(/^Type\s*\d+\s*:\s*/, '').replace(/[.$]/g, '');
    return m.length > 6 ? m.slice(0, 60) : r;
  }
  return r.replace(/\s*\([^)]*\)\s*/g, ' ').trim() || r;
}

const rawNorm = U.map(q => {
  const opts = q.opts || q.options || [];
  const ci = typeof q.correct_index === 'number' ? q.correct_index : (typeof q.ans === 'number' ? q.ans : null);
  const rawChap = (q.chapter || '').trim();
  const mega = q.type_ref || '';
  const name = readChapter(rawChap, mega);
  const srcName = q.origin || null;
  let ex = examOf(srcName);
  if (isDuWeekly.test(String(srcName || '')) && ex === 'other') ex = 'du_ka';
  const wk = inferWeek(q.id, srcName);
  return {
    id: q.id,
    source_type: sourceType(srcName, q.bank_type),
    source_name: srcName,
    exam: ex,
    exam_year: yearOf(srcName),
    week: wk,
    subject: q.subject,
    chapter_id: rawChap ? slug(rawChap) : 'unclassified',
    chapter_name: name || rawChap || 'UNCLASSIFIED',
    chapter_raw: rawChap || null,
    mega_type: mega || null,
    question: String(q.q || q.question || ''),
    options: opts,
    correct_index: (opts.length === 0) ? null : ci,
    explanation: String(q.explanation || q.exp || ''),
    trap: String(q.trap_alert || q.trap || ''),
    is_written: opts.length === 0,
    marks: opts.length === 0 ? 5 : 1,
    duration_sec: opts.length === 0 ? 240 : 45,
    probability_label: q.probability || null,
    source_book: q.source_book || null,
    bank_type: q.bank_type || null,
    appears_in: srcName ? [srcName] : []
  };
});

// A2: Text-dedup with metadata & appears_in merge
const normKey = s => String(s || '').replace(/\s+/g, ' ').trim().toLowerCase().slice(0, 140);
const byText = new Map();
const norm = [];

function metaScore(q) {
  let sc = (q.explanation ? q.explanation.length : 0) + (q.trap ? q.trap.length * 2 : 0);
  if (q.exam_year && q.exam_year >= 2010 && q.exam_year <= 2025) sc += 500;
  if (q.exam === 'du_ka' || q.exam === 'mat') sc += 200;
  if (q.week != null) sc += 100;
  return sc;
}

for (const q of rawNorm) {
  const k = normKey(q.question);
  if (k.length > 0 && byText.has(k)) {
    const existing = byText.get(k);
    const mergedSources = new Set([...(existing.appears_in || []), ...(q.appears_in || [])].filter(Boolean));
    if (metaScore(q) > metaScore(existing)) {
      // Upgrade existing in place with richer fields while preserving week/exam_year if missing
      const keepWeek = existing.week ?? q.week;
      const keepYear = (existing.exam_year && existing.exam_year <= 2025) ? existing.exam_year : (q.exam_year ?? existing.exam_year);
      Object.assign(existing, q, {
        week: q.week ?? keepWeek,
        exam_year: keepYear,
        explanation: q.explanation.length >= existing.explanation.length ? q.explanation : existing.explanation,
        trap: q.trap.length >= existing.trap.length ? q.trap : existing.trap,
        appears_in: [...mergedSources],
      });
    } else {
      if (existing.week == null && q.week != null) existing.week = q.week;
      if (existing.exam_year == null && q.exam_year != null) existing.exam_year = q.exam_year;
      if (q.explanation && q.explanation.length > existing.explanation.length) existing.explanation = q.explanation;
      if (q.trap && q.trap.length > existing.trap.length) existing.trap = q.trap;
      existing.appears_in = [...mergedSources];
    }
    continue;
  }
  if (k.length > 0) byText.set(k, q);
  norm.push(q);
}

// ensure unique id
const idSeen = new Set();
norm.forEach(q => {
  let id = q.id, i = 2;
  while (idSeen.has(id)) id = `${q.id}__${i++}`;
  idSeen.add(id);
  q.id = id;
});

// ── SPLIT OUTPUT (target architecture: src/data/bank/<exam>/<source_type>/<subject>.json) ──
const bankDir = path.join(DATA_DIR, 'bank');
fs.rmSync(bankDir, { recursive: true, force: true });
const groups = new Map();
norm.forEach(q => {
  const k = `${q.exam}|${q.source_type}|${q.subject}`;
  if (!groups.has(k)) groups.set(k, []);
  groups.get(k).push(q);
});
let biggest = { f: '', kb: 0 };
for (const [k, rows_] of groups) {
  const [exam, st, subj] = k.split('|');
  const dir = path.join(bankDir, exam, st);
  fs.mkdirSync(dir, { recursive: true });
  const slug_ = subj.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
  const f = path.join(dir, `${slug_}.json`);
  fs.writeFileSync(f, JSON.stringify(rows_), 'utf8');
  const kb = fs.statSync(f).size / 1024;
  if (kb > biggest.kb) biggest = { f: path.relative(OUT, f), kb };
}
console.log(`normalized bank: ${norm.length} (from ${rawNorm.length} id-unique) → ${path.relative(OUT, bankDir)}/ (${groups.size} ফাইল, সবচেয়ে বড় ${biggest.kb.toFixed(0)} KB)`);

// combined file শুধু চাইলে: --combined ফ্ল্যাগে (gzip করা, ~350 KB)
if (process.argv.includes('--combined')) {
  const gz = path.join(DATA_DIR, 'bank-normalized.json.gz');
  fs.writeFileSync(gz, gzipSync(Buffer.from(JSON.stringify(norm), 'utf8')));
  console.log(`combined (gzip) → ${path.relative(OUT, gz)} (${(fs.statSync(gz).size / 1024).toFixed(0)} KB)`);
}

// chapter taxonomy
const tax = new Map();
norm.forEach(q => {
  const k = q.chapter_id;
  if (!tax.has(k)) tax.set(k, { id: k, name: q.chapter_name, raw: q.chapter_raw, subject: q.subject, n: 0, years: new Set(), mega: new Set(), src: new Set() });
  const t = tax.get(k);
  t.n++;
  if (q.exam_year) t.years.add(q.exam_year);
  if (q.mega_type) t.mega.add(q.mega_type);
  t.src.add(q.source_type);
});
let csv = 'chapter_id,subject,chapter_name,chapter_raw,question_count,distinct_years,source_types,mega_type_sample\n';
[...tax.values()].sort((a, b) => b.n - a.n).forEach(t => {
  csv += [t.id, t.subject, `"${String(t.name).replace(/"/g, '""')}"`, `"${String(t.raw || '').replace(/"/g, '""')}"`, t.n, t.years.size, `"${[...t.src].join('|')}"`, `"${([...t.mega][0] || '').replace(/"/g, '""').slice(0, 80)}"`].join(',') + '\n';
});
fs.writeFileSync(path.join(DATA_DIR, 'chapter-taxonomy.csv'), csv);
console.log('chapters:', tax.size, '→', path.relative(OUT, path.join(DATA_DIR, 'chapter-taxonomy.csv')));

// sample for the agent
const sample = [
  norm.find(q => q.source_type === 'past_paper' && q.subject === 'Physics' && q.options.length === 4),
  norm.find(q => q.source_type === 'weekly_solve' && q.subject === 'Chemistry' && q.options.length === 4),
  norm.find(q => q.is_written),
  norm.find(q => q.subject === 'Biology' && q.options.length === 4),
  norm.find(q => q.subject === 'English')
].filter(Boolean);
fs.writeFileSync(path.join(DATA_DIR, 'sample-question.json'), JSON.stringify(sample, null, 1));
console.log('sample rows:', sample.length, '→', path.relative(OUT, path.join(DATA_DIR, 'sample-question.json')));

// distributions
const sd = {}; norm.forEach(q => sd[q.source_type] = (sd[q.source_type] || 0) + 1);
console.log('source_type distribution:', JSON.stringify(sd));
const ed = {}; norm.forEach(q => ed[q.exam] = (ed[q.exam] || 0) + 1);
console.log('exam distribution:', JSON.stringify(ed));
const wd = {}; norm.forEach(q => { if (q.week) wd[`week_0${q.week}`] = (wd[`week_0${q.week}`] || 0) + 1; });
console.log('week distribution:', JSON.stringify(wd));
