#!/usr/bin/env node
// extract-formulas.mjs — ব্যাংকের explanation/trap থেকে LaTeX সূত্র বের করে
// chapter-centric "সূত্র কার্ড" ডেটা বানায় (src/data/formulas.json)।
//
// কেন দরকার: written section-এ (৪০ নম্বর) সূত্র মনে থাকতে হয়।
// যে সূত্র বারবার এসেছে সেটাই "আসল সূত্র" — বাকিগুলো "প্রশ্ন-সংজ্ঞানিত"।
//
// ব্যবহার:
//   node scripts/extract-formulas.mjs [bankDir] [chapterMapCsv]
// উৎপাদ:
//   src/data/formulas.json        ← chapter → formulas → traps → questions

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const BANK = process.argv[2] || path.join(ROOT, 'src', 'data', 'bank');
const MAPCSV = process.argv[3] || path.join(ROOT, 'src', 'data', 'master-set-chapter-map.csv');
const OUT = process.argv[4] || path.join(ROOT, 'src', 'data', 'formulas.json');

// ── 1. ব্যাংক পড়ো ───────────────────────────────────────────────
function walk(dir) {
  const out = [];
  if (!fs.existsSync(dir)) return out;
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...walk(p));
    else if (e.name.endsWith('.json')) {
      try {
        const j = JSON.parse(fs.readFileSync(p, 'utf8'));
        if (Array.isArray(j)) out.push(...j);
      } catch (e) { console.warn('  ! পড়তে পারিনি:', p, e.message); }
    }
  }
  return out;
}
const rows = walk(BANK);
if (!rows.length) { console.error('❌ ব্যাংক খালি:', BANK); process.exit(1); }
console.log(`📥 ${rows.length} প্রশ্ন পড়া হয়েছে (${BANK})`);

// ── 2. chapter-map (probability সহ) পড়ো ─────────────────────────
const chapterMeta = new Map();   // chapterName → {predicted_pct, years_hit, papers_hit}
if (fs.existsSync(MAPCSV)) {
  const lines = fs.readFileSync(MAPCSV, 'utf8').split('\n').filter(Boolean);
  const head = splitCsv(lines[0]);
  const ix = n => head.indexOf(n);
  for (const line of lines.slice(1)) {
    const c = splitCsv(line);
    const name = c[ix('chapter_name')];
    if (!name) continue;
    const prev = chapterMeta.get(name);
    const yrs = +c[ix('years_hit')] || 0;
    const pap = +c[ix('papers_hit')] || 0;
    const pct = +c[ix('predicted_pct')] || 0;
    if (!prev || yrs > prev.years_hit) {
      chapterMeta.set(name, { predicted_pct: pct, years_hit: yrs, papers_hit: pap, subject: c[ix('subject')] });
    }
  }
  console.log(`📊 chapter-map: ${chapterMeta.size}টি chapter (probability সহ)`);
} else {
  console.log('⚠️  chapter-map পাওয়া যায়নি — সূত্রের "easy/possible" ব্যাংক থেকেই হিসাব হবে');
}
function splitCsv(line) {
  const out = []; let cur = '', q = false;
  for (const ch of line) {
    if (ch === '"') q = !q;
    else if (ch === ',' && !q) { out.push(cur); cur = ''; }
    else cur += ch;
  }
  out.push(cur); return out;
}

// ── 3. LaTeX সূত্র বের করো ───────────────────────────────────────
const MATH_RE = /\$([^$]{3,220})\$|\\\(([^\\)]{3,220})\\\)/g;

function extractMath(text) {
  if (!text) return [];
  const out = [];
  let m;
  const re = new RegExp(MATH_RE.source, 'g');
  while ((m = re.exec(text))) {
    const s = (m[1] || m[2] || '').trim();
    if (s.length < 4 || s.length > 200) continue;
    if (!/[=+\-^_\\]/.test(s)) continue;        // সমীকরণের চিহ্ন থাকতে হবে
    if (/[ঀ-৿]/.test(s)) continue;              // বাংলা অংশ বাদ
    out.push(s);
  }
  return out;
}

// ── 4. সূত্র canonicalize ────────────────────────────────────────
function canonical(f) {
  let s = f
    .replace(/\\left|\\right/g, '')
    .replace(/\\dfrac|\\tfrac/g, '\\frac')
    .replace(/\\[ ,;!]/g, '')
    .replace(/[ \t]+/g, '')
    .replace(/\\mathrm\{([^{}]*)\}/g, '$1')
    .replace(/\\text\{([^{}]*)\}/g, '$1');

  let prev;
  do { prev = s; s = s.replace(/\\frac\{([^{}]*)\}\{([^{}]*)\}/g, '{$1}/{$2}'); } while (s !== prev);

  s = s.replace(/\\sqrt\{([^{}]*)\}/g, '√{$1}');
  s = s.replace(/\\sqrt\[([^\]]*)\]/g, '√[$1]');
  s = s.replace(/\\([a-zA-Z]+)/g, '$1');        // কমান্ডের নাম রাখো
  s = s.replace(/[{}]/g, '');
  return s.replace(/\s+/g, '').toLowerCase();
}

// ── 5. গণনা ────────────────────────────────────────────────────
const chMap = new Map();          // chapter → {formulas:Map, traps:Set, questions:Set, years:Set, papers:Set, subjects:Set}
let mathFound = 0;

for (const q of rows) {
  const chapter = q.chapter_name || q.chapter_raw || 'UNCLASSIFIED';
  if (!chMap.has(chapter)) {
    chMap.set(chapter, {
      formulas: new Map(), traps: new Set(), questions: new Set(),
      years: new Set(), papers: new Set(), subjects: new Set(),
    });
  }
  const c = chMap.get(chapter);
  c.questions.add(q.id);
  c.years.add(q.exam_year || 'unknown');
  c.papers.add(q.source_name || 'unknown');
  c.subjects.add(q.subject || 'unknown');

  if (q.trap) c.traps.add(String(q.trap).trim());

  const forms = [...extractMath(q.explanation), ...extractMath(q.trap)];
  mathFound += forms.length;

  for (const raw of forms) {
    const key = canonical(raw);
    if (!key || key.length < 4) continue;
    const isRelation = key.includes('=') || key.includes('/');
    if (!isRelation) continue;                    // রাসায়নিক species (CO_2, NH_3) বাদ
    if (/^[\d.+\-*/=()a-z]{0,6}$/.test(key)) continue;

    if (!c.formulas.has(key)) {
      c.formulas.set(key, { formula: raw.replace(/\s+/g, ' ').trim(), canonical: key, count: 0, years: new Set(), papers: new Set(), qids: [], trap: null });
    }
    const e = c.formulas.get(key);
    e.count++;
    e.years.add(q.exam_year || 'unknown');
    e.papers.add(q.source_name || 'unknown');
    if (e.qids.length < 5) e.qids.push(q.id);
    if (!e.trap && q.trap) e.trap = String(q.trap).trim();
  }
}

// ── 6. chapter-centric আউটপুট ──────────────────────────────────
const chapters = [];
for (const [chapter, c] of chMap) {
  const meta = chapterMeta.get(chapter) || {};
  const years_hit = Math.max(c.years.size, meta.years_hit || 0);
  const papers_hit = Math.max(c.papers.size, meta.papers_hit || 0);
  const predicted_pct = meta.predicted_pct || 0;

  // সূত্রগুলো গুনে সাজাও
  const formulas = [...c.formulas.values()]
    .map(e => ({
      formula: e.formula,
      count: e.count,
      years_hit: e.years.size,
      papers_hit: e.papers.size,
      confidence: e.count >= 3 ? 'high' : e.count >= 2 ? 'medium' : 'low',
      trap: e.trap,
      question_ids: e.qids,
    }))
    .sort((a, b) => b.count - a.count);

  if (!formulas.length) continue;   // সূত্র-এবং chapter বাদ

  // chapter-level easy / possible — এটাই ইউজার চাইছে
  const easy = years_hit >= 7 || predicted_pct >= 10;
  const possible = years_hit >= 6;

  chapters.push({
    chapter,
    subject: meta.subject || [...c.subjects][0] || '',
    subjects: [...c.subjects],
    question_count: c.questions.size,
    years_hit,
    papers_hit,
    predicted_pct,
    difficulty: easy ? 'easy' : years_hit >= 4 ? 'medium' : 'hard',
    possible,
    formula_count: formulas.length,
    formulas,
    traps: [...c.traps].slice(0, 8),
    trap_count: c.traps.size,
  });
}

// সাজানো: সবচেয়ে "possible" আগে, তারপর predicted_pct
chapters.sort((a, b) => (b.possible - a.possible) || (b.predicted_pct - a.predicted_pct) || (b.years_hit - a.years_hit));

// ── 7. লেখো ───────────────────────────────────────────────────
const payload = {
  generated_at: new Date().toISOString().slice(0, 10),
  source: 'ব্যাংকের explanation + trap থেকে LaTeX extraction',
  total_math_expressions: mathFound,
  chapters_with_formulas: chapters.length,
  total_formulas: chapters.reduce((n, c) => n + c.formulas.length, 0),
  stats: {
    easy_chapters: chapters.filter(c => c.difficulty === 'easy').length,
    possible_chapters: chapters.filter(c => c.possible).length,
    high_confidence_formulas: chapters.reduce((n, c) => n + c.formulas.filter(f => f.confidence === 'high').length, 0),
    traps_collected: chapters.reduce((n, c) => n + c.trap_count, 0),
  },
  chapters,
};

fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(payload, null, 1), 'utf8');

console.log(`🧮 ${mathFound} গণিত-অভিব্যক্তি → ${chapters.length}টি chapter-এ ${payload.total_formulas}টি সূত্র`);
console.log(`📐 → ${path.relative(ROOT, OUT)}`);
console.log(`   🟢 easy chapter: ${payload.stats.easy_chapters}  ·  ⭐ possible: ${payload.stats.possible_chapters}`);
console.log(`   🚨 ট্র্যাপ সংগৃহীত: ${payload.stats.traps_collected}  ·  high-confidence সূত্র: ${payload.stats.high_confidence_formulas}`);
console.log('\nটপ ৫ chapter:');
chapters.slice(0, 5).forEach((c, i) =>
  console.log(`  ${i + 1}. [${c.difficulty}${c.possible ? ' ⭐' : ''} · ${c.formula_count} সূত্র · ${c.years_hit} বছর] ${c.chapter.slice(0, 40)}`));
