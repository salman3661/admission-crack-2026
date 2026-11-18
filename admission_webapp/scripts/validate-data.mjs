#!/usr/bin/env node
/**
 * validate-data.mjs — CI data lint
 * কোনো data ব্যাংক ঢোকানোর আগে চালাও। error = build থামানো উচিত।
 *
 *   node scripts/validate-data.mjs src/data
 */
import fs from 'fs';
import path from 'path';

const target = process.argv[2] || 'src/data';
const SOURCE_TYPES = ['past_paper', 'weekly_solve', 'paper_final', 'subject_final', 'model_test'];
const SUBJECTS = ['Physics', 'Chemistry', 'Higher Math', 'Biology', 'English', 'Bangla', 'ICT', 'GK'];
const EXAMS = ['du_ka', 'mat', 'ru', 'ju', 'cu', 'gst', 'eng_bridge', 'other'];

const errors = [], warns = [], info = [];

function walk(dir) {
  if (!fs.existsSync(dir)) return [];
  const out = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...walk(p));
    else if (e.name.endsWith('.json')) out.push(p);
  }
  return out;
}

const files = fs.existsSync(target) && fs.statSync(target).isFile() ? [target] : walk(target);
if (!files.length) { console.error(`❌ ${target}-এ কোনো JSON পাওয়া যায়নি`); process.exit(2); }

// taxonomy (optional) — chapter_id যাচাই
let taxonomy = null;
const scriptDir = path.dirname(new URL(import.meta.url).pathname);
const taxCandidates = [
  path.join(scriptDir, '..', 'src', 'data', 'chapter-taxonomy.csv'),
  path.join(scriptDir, '..', 'data', 'chapter-taxonomy.csv'),
];
const taxPath = taxCandidates.find(p => fs.existsSync(p));
if (taxPath) {
  taxonomy = new Set(fs.readFileSync(taxPath, 'utf8').split('\n').slice(1)
    .map(l => l.split(',')[0].trim()).filter(Boolean));
}

const rows = [];
for (const f of files) {
  let arr;
  try { arr = JSON.parse(fs.readFileSync(f, 'utf8')); }
  catch (e) { errors.push(`${f}: JSON parse error — ${e.message}`); continue; }
  if (!Array.isArray(arr)) { errors.push(`${f}: array expected, got ${typeof arr}`); continue; }
  arr.forEach((r, i) => rows.push({ ...r, __file: path.relative(process.cwd(), f), __i: i }));
}
console.log(`ℹ️  ${files.length} ফাইল, ${rows.length} প্রশ্ন পড়া হয়েছে\n`);

const idSeen = new Map();
const textSeen = new Map();
const ciDist = [0, 0, 0, 0];

for (const r of rows) {
  const at = `${r.__file}[${r.__i}]`;
  const examScope = r.set ? `${r.exam}:` : '';
  const idKey = `${examScope}${r.id}`;
  if (!r.id) errors.push(`${at}: id নেই`);
  else if (idSeen.has(idKey)) errors.push(`${at}: duplicate id "${r.id}" — আগে ${idSeen.get(idKey)}`);
  else idSeen.set(idKey, at);

  if (!SOURCE_TYPES.includes(r.source_type)) errors.push(`${at}: source_type "${r.source_type}" অবৈধ (চলবে: ${SOURCE_TYPES.join(', ')})`);
  if (!SUBJECTS.includes(r.subject)) warns.push(`${at}: subject "${r.subject}" তালিকার বাইরে`);
  if (!EXAMS.includes(r.exam)) warns.push(`${at}: exam "${r.exam}" অজানা`);
  if (r.exam_year == null) warns.push(`${at}: exam_year নেই`);
  if (!r.chapter_id) errors.push(`${at}: chapter_id নেই`);
  else if (taxonomy && !taxonomy.has(r.chapter_id)) warns.push(`${at}: chapter_id "${r.chapter_id}" taxonomy-তে নেই`);
  if (!r.chapter_name) warns.push(`${at}: chapter_name নেই`);

  const o = r.options || [];
  if (!Array.isArray(o)) errors.push(`${at}: options array নয়`);
  if (o.length === 0) {
    if (!r.is_written) errors.push(`${at}: options ফাঁকা কিন্তু is_written=true নয়`);
    else if (r.correct_index !== null && r.correct_index !== undefined) warns.push(`${at}: written হওয়া সত্ত্বেও correct_index আছে`);
  } else {
    if (o.length !== 4) warns.push(`${at}: options ${o.length}টা (সাধারণত 4)`);
    if (r.correct_index === null || r.correct_index === undefined) errors.push(`${at}: MCQ-র correct_index null`);
    else if (typeof r.correct_index !== 'number') errors.push(`${at}: correct_index number নয়`);
    else if (r.correct_index < 0 || r.correct_index >= o.length) errors.push(`${at}: correct_index ${r.correct_index} options-এর বাইরে (${o.length})`);
    else ciDist[r.correct_index]++;
    if (!r.explanation) warns.push(`${at}: explanation নেই`);
  }
  if (o.some(x => !String(x).trim())) errors.push(`${at}: ফাঁকা option আছে`);

  const key = `${examScope}${String(r.question || '').replace(/\s+/g, ' ').trim().toLowerCase()}`;
  if (key.length > 30 + examScope.length) {
    if (textSeen.has(key)) warns.push(`${at}: একই প্রশ্ন আরেক জায়গায় — appears_in merge করো`);
    else textSeen.set(key, at);
  }
}

// answer position bias
const mcq = ciDist.reduce((a, b) => a + b, 0);
if (mcq > 50) {
  info.push('উত্তরের অবস্থান (should be ~25% each):');
  ciDist.forEach((c, i) => {
    const pct = (c / mcq) * 100;
    const line = `  ${'ABCD'[i]} = ${String(c).padStart(5)} (${pct.toFixed(1)}%)`;
    if (pct > 33 || pct < 17) warns.push(`answer bias ${'ABCD'[i]} = ${pct.toFixed(1)}% — অপশন shuffle ব্যবহার করো`);
    else info.push(line);
  });
}

// source_type distribution
const sd = {}; rows.forEach(r => sd[r.source_type] = (sd[r.source_type] || 0) + 1);
info.push('source_type:', JSON.stringify(sd));
const ed = {}; rows.forEach(r => ed[r.exam] = (ed[r.exam] || 0) + 1);
info.push('exam:', JSON.stringify(ed));
const sub = {}; rows.forEach(r => sub[r.subject] = (sub[r.subject] || 0) + 1);
info.push('subject:', JSON.stringify(sub));

console.log('── INFO ──'); info.forEach(i => console.log('  ' + i));
if (warns.length) {
  console.log('\n── WARN (গ্রুপ করা) ──');
  const g = new Map();
  warns.forEach(w => { const k = w.replace(/\[[\d]+\]/, '[*]'); g.set(k, (g.get(k) || 0) + 1); });
  [...g.entries()].sort((a, b) => b[1] - a[1]).forEach(([k, n]) => console.log(`  ⚠ ${k}  ×${n}`));
}
if (errors.length) { console.log('\n── ERROR ──'); errors.slice(0, 40).forEach(e => console.log('  ✖ ' + e)); if (errors.length > 40) console.log(`  … আরও ${errors.length - 40}টা error`); }
console.log(`\n${errors.length} error, ${warns.length} warning`);
if (errors.length) { console.error('\n❌ BUILD থামাও — error আছে।'); process.exit(1); }
console.log('✅ validation পাস');
