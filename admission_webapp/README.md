# Admission Crack 2026 — Webapp

DU 'Ka' (Science Unit) এবং Medical (MAT) ভর্তি পরীক্ষার প্র্যাকটিস ও প্রেডিকশন ইঞ্জিন।

## নতুন Coaching Paper যোগ করার নিয়ম

1. `src/data/bank/<exam>/<source_type>/<name>.json` ফাইল তৈরি করো (যেমন `src/data/bank/du_ka/model_test/model_test_03.json`)।
   - প্রতিটি প্রশ্নে `id`, `source_type` (`model_test` | `paper_final` | `subject_final` | `past_paper` | `weekly_solve`), `source_name`, `exam`, `exam_year`, `exam_date`, `subject`, `chapter_id`, `chapter_name`, `question`, `options`, `correct_index`, `is_written`, `marks`, `duration_sec` থাকতে হবে।
   - লিখিত প্রশ্নের ক্ষেত্রে `options: []`, `correct_index: null`, `is_written: true` দাও।
2. ডেটা যাচাই করো (0 error নিশ্চিত করো):
   ```bash
   node scripts/validate-data.mjs src/data/bank
   ```
3. Master Set, Index ও Backtest পুনর্গঠন করো:
   ```bash
   node scripts/build-master-set.mjs src/data/bank
   ```
4. Master Set যাচাই করো:
   ```bash
   node scripts/coverage-scorer.cjs src/data/master/du_ka_set_a.json
   node scripts/coverage-scorer.cjs src/data/master/mat_set_a.json
   ```
5. প্রোডাকশন বিল্ড করো:
   ```bash
   npm run build
   ```
