// তোমার ব্যাংক → নতুন normalized schema + chapter taxonomy
import fs from 'fs'; import path from 'path'; import { execSync } from 'child_process'; import { gzipSync } from 'zlib';
const HERE = path.dirname(new URL(import.meta.url).pathname);
const OUT = path.join(HERE, '..');
const CACHE = path.join(HERE, '.bankcache');
const BUNDLE_URL = process.env.BANK_URL || 'https://admissionwebapp.vercel.app/assets/index-BVMUvLgv.js';

function loadBank() {
  if (fs.existsSync(CACHE)) return JSON.parse(fs.readFileSync(CACHE, 'utf8'));
  const tmp = path.join(HERE, '.b.js');
  execSync(`curl -sS --max-time 150 -o "${tmp}" "${BUNDLE_URL}"`, { stdio: 'inherit' });
  const src = fs.readFileSync(tmp, 'utf8');
  const re = /JSON\.parse\(`/g; let m; const bank = [];
  while ((m = re.exec(src))) {
    let j = m.index + m[0].length, q = null;
    while (j < src.length) { if (src[j] === '\\') { j += 2; continue; } if (src[j] === '`') { q = j; break; } j++; }
    if (q === null) continue;
    try { const a = JSON.parse(eval('`' + src.slice(m.index + m[0].length, q) + '`')); if (Array.isArray(a) && a.length && a[0].q !== undefined) bank.push(...a); } catch (e) {}
  }
  fs.unlinkSync(tmp); fs.writeFileSync(CACHE, JSON.stringify(bank)); return bank;
}
const BANK = loadBank();
const seen = new Set(); const U = BANK.filter(q => { const k = q.id || (q.q || q.question); if (seen.has(k)) return false; seen.add(k); return true; });

// বাংলা অক্ষর রাখি (URL-encode করে কাজ করবে), শুধু punctuation ও ব্যবধান বদলাই
const slug = s => String(s || '').replace(/\([^)]*\)/g, '').trim()
  .replace(/[^\p{L}\p{N}\s_-]/gu, ' ').replace(/\s+/g, '_').replace(/_+/g, '_')
  .replace(/^_|_$/g, '').slice(0, 48) || 'x';
function sourceType(o, bank) {
  const s = String(o || ''); const b = String(bank || '');
  if (/Weekly|Solve Sheet|B-0\d|W-0\d/i.test(s) && !/Paper Final|Model/i.test(s)) return 'weekly_solve';
  if (/Paper\s*Final/i.test(s)) return 'paper_final';
  if (/Model\s*Test/i.test(s)) return 'model_test';
  if (/Subject\s*Final/i.test(s)) return 'subject_final';
  if (/MAT\s*Line\s*2026|DU-MAT\s*Repeat\s*2026|Speed Hack 2026/i.test(s)) return 'weekly_solve';
  return 'past_paper';
}
function examOf(o) {
  const s = String(o || '');
  if (/MAT|Medical|DMC/i.test(s)) return 'mat';
  if (/DU |DU-|Hubohu|Dhaka University/i.test(s)) return 'du_ka';
  if (/^RU |RU-/i.test(s)) return 'ru';
  if (/^CU |CU-/i.test(s)) return 'cu';
  if (/^JU |JU-/i.test(s)) return 'ju';
  if (/GST/i.test(s)) return 'gst';
  if (/Engineering Bridge/i.test(s)) return 'eng_bridge';
  return 'other';
}
function yearOf(o) {
  const s = String(o || ''); const m = s.match(/'(\d{2})(?:-(\d{2}))?/);
  if (m) { let a = +m[1]; if (a > 40) a -= 100; if (a < 10) a += 90; return 2000 + a; }
  if (/2026/.test(s)) return 2026; return null;
}
function readChapter(raw, mega) {
  const r = String(raw || '').trim();
  if (!r || r === 'UNCLASSIFIED') return null;
  if (/^(bio_|math_)/.test(r)) {
    // raw ID → readable name from mega-type (mega_type প্রায়ই বিষয়বস্তু বলে দেয়)
    const m = String(mega || '').replace(/^Type\s*\d+\s*:\s*/, '').replace(/[.$]/g, '');
    return m.length > 6 ? m.slice(0, 60) : r;
  }
  return r.replace(/\s*\([^)]*\)\s*/g, ' ').trim() || r;
}

const norm = U.map(q => {
  const opts = q.opts || q.options || [];
  const ci = typeof q.correct_index === 'number' ? q.correct_index : (typeof q.ans === 'number' ? q.ans : null);
  const rawChap = (q.chapter || '').trim();
  const mega = q.type_ref || '';
  const name = readChapter(rawChap, mega);
  return {
    id: q.id,
    source_type: sourceType(q.origin, q.bank_type),
    source_name: q.origin || null,
    exam: examOf(q.origin),
    exam_year: yearOf(q.origin),
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
    bank_type: q.bank_type || null
  };
});
// ensure unique id
const idSeen = new Set();
norm.forEach(q => { let id = q.id, i = 2; while (idSeen.has(id)) id = `${q.id}__${i++}`; idSeen.add(id); q.id = id; });

// ── SPLIT OUTPUT (target architecture: src/data/<exam>/<source_type>/<subject>.json) ──
const bankDir = path.join(OUT, 'data', 'bank');
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
console.log(`normalized bank: ${norm.length} → data/bank/ (${groups.size} ফাইল, সবচেয়ে বড় ${biggest.kb.toFixed(0)} KB)`);

// combined file শুধু চাইলে: --combined ফ্ল্যাগে (gzip করা, ~350 KB)
if (process.argv.includes('--combined')) {
  const gz = path.join(OUT, 'data', 'bank-normalized.json.gz');
  fs.writeFileSync(gz, gzipSync(Buffer.from(JSON.stringify(norm), 'utf8')));
  console.log(`combined (gzip) → data/bank-normalized.json.gz (${(fs.statSync(gz).size / 1024).toFixed(0)} KB)`);
}

// chapter taxonomy
const tax = new Map();
norm.forEach(q => {
  const k = q.chapter_id;
  if (!tax.has(k)) tax.set(k, { id: k, name: q.chapter_name, raw: q.chapter_raw, subject: q.subject, n: 0, years: new Set(), mega: new Set(), src: new Set() });
  const t = tax.get(k); t.n++; if (q.exam_year) t.years.add(q.exam_year); if (q.mega_type) t.mega.add(q.mega_type); t.src.add(q.source_type);
});
let csv = 'chapter_id,subject,chapter_name,chapter_raw,question_count,distinct_years,source_types,mega_type_sample\n';
[...tax.values()].sort((a, b) => b.n - a.n).forEach(t => {
  csv += [t.id, t.subject, `"${String(t.name).replace(/"/g, '""')}"`, `"${String(t.raw || '').replace(/"/g, '""')}"`, t.n, t.years.size, `"${[...t.src].join('|')}"`, `"${([...t.mega][0] || '').replace(/"/g, '""').slice(0, 80)}"`].join(',') + '\n';
});
fs.writeFileSync(path.join(OUT, 'data', 'chapter-taxonomy.csv'), csv);
console.log('chapters:', tax.size, '→ data/chapter-taxonomy.csv');

// sample for the agent
const sample = [
  norm.find(q => q.source_type === 'past_paper' && q.subject === 'Physics' && q.options.length === 4),
  norm.find(q => q.source_type === 'weekly_solve' && q.subject === 'Chemistry' && q.options.length === 4),
  norm.find(q => q.is_written),
  norm.find(q => q.subject === 'Biology' && q.options.length === 4),
  norm.find(q => q.subject === 'English')
].filter(Boolean);
fs.writeFileSync(path.join(OUT, 'data', 'sample-question.json'), JSON.stringify(sample, null, 1));
console.log('sample rows:', sample.length, '→ data/sample-question.json');

// source type distribution
const sd = {}; norm.forEach(q => sd[q.source_type] = (sd[q.source_type] || 0) + 1);
console.log('source_type distribution:', JSON.stringify(sd));
const ed = {}; norm.forEach(q => ed[q.exam] = (ed[q.exam] || 0) + 1);
console.log('exam distribution:', JSON.stringify(ed));
