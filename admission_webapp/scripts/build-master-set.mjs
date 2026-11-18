#!/usr/bin/env node
/**
 * build-master-set.mjs — ২৬-২৭ এর master set তৈরি (LEARN → PREDICT → SELECT)
 *
 * ইনপুট:  src/data/<exam>/<source_type>/<name>.json  (নতুন schema)
 * আউটপুট: src/data/master/*.json  +  data/master-set-chapter-map.csv
 *
 *   node scripts/build-master-set.mjs [srcDataDir]
 */
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { gunzipSync } from 'zlib';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const ROOT = path.join(HERE, '..');
const DATA_DIR = path.join(ROOT, 'src', 'data');
const SRC = process.argv[2] || path.join(DATA_DIR, 'bank');

const SOURCE_WEIGHT = { model_test: 1.00, paper_final: 0.95, subject_final: 0.90, past_paper: 0.85, weekly_solve: 0.70 };
const LEARN_FROM = 2010, LEARN_TO = 2025, TARGET = 2026;
const recency = y => Math.pow(0.86, LEARN_TO - y);

const DU_KA = [{ subject: 'Physics', mcq: 15 }, { subject: 'Chemistry', mcq: 15 }, { subject: 'Higher Math', mcq: 15 }, { subject: 'Biology', mcq: 15 }];
const MAT = [{ subject: 'Biology', mcq: 30 }, { subject: 'Chemistry', mcq: 25 }, { subject: 'Physics', mcq: 20 }, { subject: 'English', mcq: 15 }, { subject: 'GK', mcq: 10 }];

function loadRows() {
  // 1) split bank থাকলে সেটা পড়ো (src/data/bank/<exam>/<source_type>/<subject>.json)
  const splitDir = fs.existsSync(SRC) && fs.statSync(SRC).isDirectory() ? SRC : path.join(DATA_DIR, 'bank');
  if (fs.existsSync(splitDir)) {
    const out = [];
    const walk = d => { for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) walk(p);
      else if (e.name.endsWith('.json')) { try { const j = JSON.parse(fs.readFileSync(p, 'utf8')); if (Array.isArray(j)) out.push(...j); } catch (er) {} }
    } };
    walk(splitDir);
    if (out.length) { console.log(`ℹ️  split bank: ${out.length} row (${splitDir})`); return out; }
  }
  // 2) combined gzip
  const gz = path.join(KIT, 'data', 'bank-normalized.json.gz');
  if (fs.existsSync(gz)) {
    const j = JSON.parse(gunzipSync(fs.readFileSync(gz)).toString('utf8'));
    if (Array.isArray(j)) { console.log(`ℹ️  combined gzip: ${j.length} row`); return j; }
  }
  // 3) combined json
  if (fs.existsSync(SRC) && SRC.endsWith('.json')) {
    const j = JSON.parse(fs.readFileSync(SRC, 'utf8'));
    return Array.isArray(j) ? j : [];
  }
  // fallback: নতুন paper না থাকলে deployed bundle থেকে আসল ব্যাংক টেনে নাও
  console.log('📥 src data নেই — deployed bundle থেকে টেনে আসছি...');
  const tmp = path.join(HERE, '.b.js');
  execSync(`curl -sS --max-time 150 -o "${tmp}" "https://admissionwebapp.vercel.app/assets/index-BVMUvLgv.js"`, { stdio: 'inherit' });
  const src = fs.readFileSync(tmp, 'utf8');
  const re = /JSON\.parse\(`/g; let m; const bank = [];
  while ((m = re.exec(src))) {
    let j = m.index + m[0].length, q = null;
    while (j < src.length) { if (src[j] === '\\') { j += 2; continue; } if (src[j] === '`') { q = j; break; } j++; }
    if (q === null) continue;
    try { const a = JSON.parse(eval('`' + src.slice(m.index + m[0].length, q) + '`')); if (Array.isArray(a) && a.length && a[0].q !== undefined) bank.push(...a); } catch (e) {}
  }
  fs.unlinkSync(tmp);
  const slug = s => String(s || '').replace(/\([^)]*\)/g, '').trim().replace(/[^\w\sঀ-৿-]/g, ' ').replace(/\s+/g, '_').slice(0, 40) || 'x';
  const st = o => /Weekly|Solve Sheet/i.test(String(o || '')) ? 'weekly_solve' : 'past_paper';
  const ex = o => /MAT|Medical/i.test(String(o || '')) ? 'mat' : /DU|Hubohu/i.test(String(o || '')) ? 'du_ka' : 'other';
  const yr = o => { const m = String(o || '').match(/'(\d{2})/); return m ? 2000 + (+m[1] > 40 ? +m[1] - 100 : +m[1]) : (String(o || '').includes('2026') ? 2026 : null); };
  const seen = new Set();
  return bank.filter(q => { const k = q.id || (q.q || q.question); if (seen.has(k)) return false; seen.add(k); return true; })
    .map(q => ({
      id: q.id, source_type: st(q.origin), source_name: q.origin, exam: ex(q.origin), exam_year: yr(q.origin),
      subject: q.subject, chapter_id: slug(q.chapter), chapter_name: (q.chapter || 'UNCLASSIFIED'),
      mega_type: q.type_ref || null, question: String(q.q || q.question || ''), options: q.opts || q.options || [],
      correct_index: typeof q.correct_index === 'number' ? q.correct_index : (typeof q.ans === 'number' ? q.ans : null),
      explanation: String(q.explanation || q.exp || ''), trap: String(q.trap_alert || q.trap || ''),
      is_written: !(q.opts || q.options || []).length, marks: 1, duration_sec: 45
    }));
}

const rows = loadRows();
const MCQ = rows.filter(r => !r.is_written && (r.options || []).length >= 2);
console.log(`ℹ️  ${rows.length} row → ${MCQ.length} MCQ`);

// ── LEARN ──
const yearChap = new Map(), subjYearTotal = new Map(), chapYears = new Map(), chapPapers = new Map();
for (const r of MCQ) {
  const y = r.exam_year; if (!y || y < LEARN_FROM || y > LEARN_TO) continue;
  const key = `${r.subject}||${r.chapter_id}`;
  if (!yearChap.has(r.subject)) yearChap.set(r.subject, new Map());
  if (!yearChap.get(r.subject).has(y)) yearChap.get(r.subject).set(y, new Map());
  const ym = yearChap.get(r.subject).get(y); ym.set(r.chapter_id, (ym.get(r.chapter_id) || 0) + 1);
  if (!subjYearTotal.has(r.subject)) subjYearTotal.set(r.subject, new Map());
  subjYearTotal.get(r.subject).set(y, (subjYearTotal.get(r.subject).get(y) || 0) + 1);
  if (!chapYears.has(key)) chapYears.set(key, new Set());
  chapYears.get(key).add(y);
  if (!chapPapers.has(key)) chapPapers.set(key, new Set());
  chapPapers.get(key).add(r.source_name || r.id);
}
const PRED = new Map();
for (const [subject, ymap] of yearChap) {
  const score = new Map(); let tot = 0;
  for (const [y, cm] of ymap) {
    const n = subjYearTotal.get(subject).get(y) || 1, w = recency(y);
    for (const [ch, cnt] of cm) { const s = (cnt / n) * w; score.set(ch, (score.get(ch) || 0) + s); tot += s; }
  }
  PRED.set(subject, new Map([...score].map(([k, v]) => [k, v / tot])));
}
const metaOf = (subject, ch) => ({
  years: chapYears.get(`${subject}||${ch}`)?.size || 1,
  papers: chapPapers.get(`${subject}||${ch}`)?.size || 1
});

// ── SELECT ──
function buildSet(subject, quota, exclude) {
  const pool = MCQ.filter(r => r.subject === subject && !exclude.has(r.id)).map(r => ({
    r, p: PRED.get(subject)?.get(r.chapter_id) || 0.004,
    yh: metaOf(subject, r.chapter_id).years, ph: metaOf(subject, r.chapter_id).papers,
    bestYear: r.exam_year || 2026
  }));
  const takenC = new Map(), takenY = new Map(), used = new Set(), picked = [];
  const yearCap = Math.max(4, Math.round(quota * 0.38));
  const score = (it, tc, ty) => {
    const rec = it.r.exam_year ? 0.55 + 0.45 * Math.pow(0.93, TARGET - it.r.exam_year) : 0.9;
    const rep = Math.min(1.55, 1 + 0.07 * (it.yh - 1) + 0.05 * (it.ph - 1));
    return it.p * rec * rep * (SOURCE_WEIGHT[it.r.source_type] || 0.7) * Math.pow(0.68, tc) * Math.pow(0.90, ty);
  };
  const byChap = new Map();
  for (const it of pool) if (!byChap.has(it.r.chapter_id) || it.p > byChap.get(it.r.chapter_id).p) byChap.set(it.r.chapter_id, it);
  for (const s of [...byChap.values()].filter(x => x.p * quota >= 0.4).sort((a, b) => b.p - a.p).slice(0, Math.min(quota, 16))) {
    if (picked.length >= quota) break;
    picked.push(s.r); used.add(s.r.id);
    takenC.set(s.r.chapter_id, (takenC.get(s.r.chapter_id) || 0) + 1);
    takenY.set(s.bestYear, (takenY.get(s.bestYear) || 0) + 1);
  }
  while (picked.length < quota) {
    let best = null, bs = -1, bc = 0, by = 0;
    for (const it of pool) {
      if (used.has(it.r.id)) continue;
      const tc = takenC.get(it.r.chapter_id) || 0, ty = takenY.get(it.bestYear) || 0;
      if (tc >= Math.max(1, Math.ceil(it.p * quota * 1.7))) continue;
      if (ty >= yearCap) continue;
      const s = score(it, tc, ty);
      if (s > bs) { bs = s; best = it; bc = tc; by = ty; }
    }
    if (!best) break;
    used.add(best.r.id); picked.push(best.r);
    takenC.set(best.r.chapter_id, bc + 1); takenY.set(best.bestYear, by + 1);
  }
  return picked;
}
function buildExam(specs, tag) {
  const used = new Set(); const A = [], B = [];
  for (const sp of specs) {
    const a = buildSet(sp.subject, sp.mcq, used); a.forEach(r => used.add(r.id)); A.push(...a);
    const b = buildSet(sp.subject, sp.mcq, used); b.forEach(r => used.add(r.id)); B.push(...b);
  }
  return { A, B };
}
function wildcard(specs, used, quotaRatio = 0.4) {
  const out = [];
  for (const sp of specs) {
    const pool = MCQ.filter(r => r.subject === sp.subject && !used.has(r.id)).map(r => ({
      r, p: PRED.get(sp.subject)?.get(r.chapter_id) || 0.004,
      yh: metaOf(sp.subject, r.chapter_id).years, bestYear: r.exam_year || 2026
    })).sort((a, b) => (b.p * (0.5 + 0.09 * b.yh)) - (a.p * (0.5 + 0.09 * a.yh)));
    const n = Math.max(4, Math.round(sp.mcq * quotaRatio));
    const perChap = new Map();
    for (const it of pool) {
      if (out.filter(x => x.subject === sp.subject).length >= n) break;
      const c = perChap.get(it.r.chapter_id) || 0; if (c >= 3) continue;
      perChap.set(it.r.chapter_id, c + 1); used.add(it.r.id); out.push(it.r);
    }
  }
  return out;
}
const duka = buildExam(DU_KA), mat = buildExam(MAT);
const allUsed = new Set([...duka.A, ...duka.B, ...mat.A, ...mat.B].map(r => r.id));
const dukaC = wildcard(DU_KA, allUsed), matC = wildcard(MAT, allUsed);

// ── EXPORT ──
const outDir = path.join(DATA_DIR, 'master'); fs.mkdirSync(outDir, { recursive: true });
function enrich(r, exam, set, idx) {
  const m = metaOf(r.subject, r.chapter_id);
  const p = (PRED.get(r.subject)?.get(r.chapter_id) || 0);
  return {
    ...r, exam, set, slot: `${r.subject} #${idx + 1}`,
    likelihood_pct: +(p * 100).toFixed(2), expected_mcq_in_paper: +(p * (r.subject === 'Biology' && exam === 'mat' ? 30 : r.subject === 'Chemistry' && exam === 'mat' ? 25 : 15)).toFixed(2),
    years_hit: m.years, papers_hit: m.papers, source_weight: SOURCE_WEIGHT[r.source_type] || 0.7
  };
}
function dump(list, exam, set) {
  fs.writeFileSync(path.join(outDir, `${exam}_${set}.json`), JSON.stringify(list.map((r, i) => enrich(r, exam, set, i)), null, 1), 'utf8');
  console.log(`📄 master/${exam}_${set}.json  ${list.length} প্রশ্ন`);
}
dump(duka.A, 'du_ka', 'set_a'); dump(duka.B, 'du_ka', 'set_b'); dump(dukaC, 'du_ka', 'set_c');
dump(mat.A, 'mat', 'set_a'); dump(mat.B, 'mat', 'set_b'); dump(matC, 'mat', 'set_c');

// chapter map
let csv = 'exam,subject,chapter_id,chapter_name,predicted_pct,expected_mcq,years_hit,papers_hit,set_a,set_b,set_c\n';
for (const [exam, specs, S, C] of [['du_ka', DU_KA, duka, dukaC], ['mat', MAT, mat, matC]]) {
  for (const sp of specs) {
    const p = PRED.get(sp.subject) || new Map();
    const cnt = (list, ch) => list.filter(r => r.subject === sp.subject && r.chapter_id === ch).length;
    for (const [ch, pr] of [...p.entries()].sort((a, b) => b[1] - a[1])) {
      const name = MCQ.find(r => r.subject === sp.subject && r.chapter_id === ch)?.chapter_name || ch;
      const m = metaOf(sp.subject, ch);
      csv += [exam, sp.subject, ch, `"${String(name).replace(/"/g, '""')}"`, (pr * 100).toFixed(3), (pr * sp.mcq).toFixed(2), m.years, m.papers, cnt(S.A, ch), cnt(S.B, ch), cnt(C, ch)].join(',') + '\n';
    }
  }
}
fs.writeFileSync(path.join(DATA_DIR, 'master-set-chapter-map.csv'), csv);
console.log('📄 src/data/master-set-chapter-map.csv');

// ── LEAVE-ONE-YEAR-OUT BACKTEST (2021–2024) ──
const backtestYears = [2021, 2022, 2023, 2024];
const backtestResults = [];
let totalTestQ = 0, totalTop8Hit = 0, totalSubjectsTested = 0, totalRank1Hit = 0;
for (const testYear of backtestYears) {
  const trainRows = MCQ.filter(r => r.exam_year && r.exam_year >= LEARN_FROM && r.exam_year < testYear);
  const testRows = MCQ.filter(r => r.exam_year === testYear);
  if (!trainRows.length || !testRows.length) continue;

  const tYearChap = new Map(), tSubjTotal = new Map();
  for (const r of trainRows) {
    const y = r.exam_year;
    if (!tYearChap.has(r.subject)) tYearChap.set(r.subject, new Map());
    if (!tYearChap.get(r.subject).has(y)) tYearChap.get(r.subject).set(y, new Map());
    const ym = tYearChap.get(r.subject).get(y);
    const sw = SOURCE_WEIGHT[r.source_type] || 0.7;
    ym.set(r.chapter_id, (ym.get(r.chapter_id) || 0) + sw);
    if (!tSubjTotal.has(r.subject)) tSubjTotal.set(r.subject, new Map());
    tSubjTotal.get(r.subject).set(y, (tSubjTotal.get(r.subject).get(y) || 0) + sw);
  }
  const yrSubjCounts = new Map();
  for (const r of testRows) {
    if (!yrSubjCounts.has(r.subject)) yrSubjCounts.set(r.subject, new Map());
    const m = yrSubjCounts.get(r.subject);
    m.set(r.chapter_id, (m.get(r.chapter_id) || 0) + 1);
  }
  let yrQ = 0, yrTop8 = 0, yrSubjs = 0, yrRank1 = 0;
  for (const [subj, actualMap] of yrSubjCounts) {
    const ymap = tYearChap.get(subj);
    if (!ymap) continue;
    const score = new Map();
    for (const [y, cm] of ymap) {
      const n = tSubjTotal.get(subj).get(y) || 1;
      const w = Math.pow(0.86, testYear - 1 - y);
      for (const [ch, cnt] of cm) score.set(ch, (score.get(ch) || 0) + (cnt / n) * w);
    }
    const ranked = [...score.entries()].sort((a, b) => b[1] - a[1]).map(x => x[0]);
    const top8 = new Set(ranked.slice(0, 8));
    const pred1 = ranked[0];
    const actualRanked = [...actualMap.entries()].sort((a, b) => b[1] - a[1]);
    const actual1 = actualRanked[0]?.[0];
    yrSubjs++;
    if (pred1 && actual1 && pred1 === actual1) yrRank1++;
    for (const [ch, cnt] of actualMap) {
      yrQ += cnt;
      if (top8.has(ch)) yrTop8 += cnt;
    }
  }
  totalTestQ += yrQ; totalTop8Hit += yrTop8; totalSubjectsTested += yrSubjs; totalRank1Hit += yrRank1;
  backtestResults.push({
    year: testYear,
    questions: yrQ,
    top8_coverage_pct: yrQ ? +((yrTop8 / yrQ) * 100).toFixed(1) : 0,
    rank1_hit_pct: yrSubjs ? +((yrRank1 / yrSubjs) * 100).toFixed(1) : 0,
  });
}
const backtestSummary = {
  generated_at: new Date().toISOString(),
  overall_top8_coverage_pct: totalTestQ ? +((totalTop8Hit / totalTestQ) * 100).toFixed(1) : 0,
  overall_rank1_hit_pct: totalSubjectsTested ? +((totalRank1Hit / totalSubjectsTested) * 100).toFixed(1) : 0,
  total_test_questions: totalTestQ,
  years: backtestResults,
};
fs.writeFileSync(path.join(DATA_DIR, 'backtest.json'), JSON.stringify(backtestSummary, null, 2));
console.log(`📊 backtest.json: top-8 coverage=${backtestSummary.overall_top8_coverage_pct}%, #1 rank hit=${backtestSummary.overall_rank1_hit_pct}%`);

// ── RUNTIME INDEX (lightweight metadata for 0-MB initial load) ──
const bankRoot = path.join(DATA_DIR, 'bank');
const papers = [];
const byExam = {}, bySubject = {}, bySourceType = {}, byWeek = {};
const chapterStats = new Map();
function scanBank(d) {
  if (!fs.existsSync(d)) return;
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) scanBank(p);
    else if (e.name.endsWith('.json')) {
      const rel = path.relative(DATA_DIR, p).replace(/\\/g, '/');
      const arr = JSON.parse(fs.readFileSync(p, 'utf8'));
      if (!Array.isArray(arr) || !arr.length) continue;
      const exams = new Set(), subjects = new Set(), sourceTypes = new Set();
      let mcqs = 0, written = 0;
      for (const q of arr) {
        exams.add(q.exam || 'other');
        subjects.add(q.subject || 'Physics');
        sourceTypes.add(q.source_type || 'past_paper');
        if (q.is_written || !(q.options || []).length) written++; else mcqs++;
        byExam[q.exam || 'other'] = (byExam[q.exam || 'other'] || 0) + 1;
        bySubject[q.subject || 'Physics'] = (bySubject[q.subject || 'Physics'] || 0) + 1;
        bySourceType[q.source_type || 'past_paper'] = (bySourceType[q.source_type || 'past_paper'] || 0) + 1;
        const wkMatch = String(q.source_name || '').match(/Week\s*0?(\d+)/i);
        if (wkMatch) {
          const wkKey = `week_${wkMatch[1].padStart(2, '0')}`;
          byWeek[wkKey] = (byWeek[wkKey] || 0) + 1;
        }
        const chKey = `${q.subject}||${q.chapter_id}`;
        if (!chapterStats.has(chKey)) {
          chapterStats.set(chKey, {
            chapter_id: q.chapter_id,
            chapter_name: q.chapter_name || q.chapter_id,
            subject: q.subject,
            count: 0,
            years: new Set(),
            papers: new Set(),
            exams: new Set(),
          });
        }
        const cs = chapterStats.get(chKey);
        cs.count++;
        if (q.exam_year) cs.years.add(q.exam_year);
        if (q.source_name) cs.papers.add(q.source_name);
        if (q.exam) cs.exams.add(q.exam);
      }
      papers.push({
        path: rel,
        count: arr.length,
        mcqs,
        written,
        exams: [...exams],
        subjects: [...subjects],
        source_types: [...sourceTypes],
      });
    }
  }
}
scanBank(bankRoot);
const indexPayload = {
  generated_at: new Date().toISOString(),
  total_questions: rows.length,
  total_mcqs: MCQ.length,
  total_written: rows.length - MCQ.length,
  by_exam: byExam,
  by_subject: bySubject,
  by_source_type: bySourceType,
  by_week: byWeek,
  master_sets: {
    du_ka_set_a: duka.A.length,
    du_ka_set_b: duka.B.length,
    du_ka_set_c: dukaC.length,
    mat_set_a: mat.A.length,
    mat_set_b: mat.B.length,
    mat_set_c: matC.length,
  },
  papers,
  chapters: [...chapterStats.values()].map(c => ({
    chapter_id: c.chapter_id,
    chapter_name: c.chapter_name,
    subject: c.subject,
    count: c.count,
    years_hit: c.years.size,
    papers_hit: c.papers.size,
    exams: [...c.exams],
    predicted_pct: +((PRED.get(c.subject)?.get(c.chapter_id) || 0) * 100).toFixed(2),
    expected_mcq_du_ka: +((PRED.get(c.subject)?.get(c.chapter_id) || 0) * 15).toFixed(2),
    expected_mcq_mat: +((PRED.get(c.subject)?.get(c.chapter_id) || 0) * (c.subject === 'Biology' ? 30 : c.subject === 'Chemistry' ? 25 : c.subject === 'Physics' ? 20 : c.subject === 'English' ? 15 : 10)).toFixed(2),
  })),
};
fs.writeFileSync(path.join(DATA_DIR, 'index.json'), JSON.stringify(indexPayload, null, 2));
console.log(`📇 src/data/index.json: ${papers.length} papers, ${indexPayload.chapters.length} chapters`);

// stats
for (const [name, set] of [['DU Ka A', duka.A], ['DU Ka B', duka.B], ['MAT A', mat.A], ['MAT B', mat.B]]) {
  const chs = new Set(set.map(r => r.chapter_id));
  const sd = {}; set.forEach(r => sd[r.source_type] = (sd[r.source_type] || 0) + 1);
  console.log(`  ${name.padEnd(8)} ${String(set.length).padStart(3)} প্রশ্ন | ${chs.size} chapter | source: ${JSON.stringify(sd)}`);
}
