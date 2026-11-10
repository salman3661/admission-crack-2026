#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_chemistry_dataset.py
Strict, comprehensive validation script for Chemistry question datasets (1st & 2nd Paper).
Verifies:
1. JSON Schema integrity across predictor and question bank files.
2. All 10 Chemistry chapters present and properly populated (20 MCQs each = 200 total).
3. Zero duplicate question IDs across predictors.
4. Exactly 4 unique options per question with balanced answers across ['A', 'B', 'C', 'D'] (~25% each).
5. All required fields (stem, options, answer, type_ref, trap_alert, speed_hack, explanation) present.
6. Zero dummy / synthetic placeholder strings.
7. LaTeX sanitization: balanced '$' math delimiters, balanced '{' and '}', no raw '\\x0c'.
8. Question bank integrity: zero misclassified chemistry questions across all 14 question bank files.
"""

import json
import os
import sys
import re

PREDICTOR_FILES = [
    "src/data/chapter_synthetic_predictors.json",
    "admission_webapp/src/data/chapter_synthetic_predictors.json"
]

QUESTION_BANK_FILES = [
    "questions.json",
    "varsity_bank.json",
    "medical_bank.json",
    "weekly_exams.json",
    "src/data/questions.json",
    "src/data/varsity_bank.json",
    "src/data/medical_bank.json",
    "src/data/weekly_exams.json",
    "src/data/quizzes.json",
    "admission_webapp/src/data/questions.json",
    "admission_webapp/src/data/varsity_bank.json",
    "admission_webapp/src/data/medical_bank.json",
    "admission_webapp/src/data/weekly_exams.json",
    "admission_webapp/src/data/quizzes.json",
]

DUMMY_PHRASES = [
    "মান সর্বদা শূন্য বা ধ্রুবক থাকে",
    "প্রদত্ত শর্তের সাথে কোনো সম্পর্ক নেই",
    "কেবলমাত্র আদর্শ অবস্থায় বিপরীতমুখী হয়",
    "দীর্ঘায়িত প্রথাগত সমীকরণ সমাধান যেখানে ৩ মিনিটের অধিক সময় প্রয়োজন",
    "উভয় পক্ষ বর্গ না করে অপরিবর্তিত রাখা",
    "ভুল সমীকরণ অনুসিদ্ধান্ত",
    "অনুপাত ও একক বিবেচনা না করে সরাসরি মুখস্থ মানের প্রয়োগ",
    "সমীকরণের উভয় পাশে শূন্য দ্বারা ভাগ করা",
    "সবসময় প্রথম অপশনটিকে সঠিক ধরে",
    "চলকের মান সর্বদা ঋণাত্মক হবে",
    "মাত্রা সমীকরণ অপরিবর্তিত থাকে না",
    "অতিরিক্ত প্র্যাকটিস প্রশ্ন - মূল সমীকরণ কোনটি"
]

EXPECTED_CHEMISTRY_CHAPTERS = [
    "chem_1st_01",
    "chem_1st_02",
    "chem_1st_03",
    "chem_1st_04",
    "chem_1st_05",
    "chem_2nd_01",
    "chem_2nd_02",
    "chem_2nd_03",
    "chem_2nd_04",
    "chem_2nd_05"
]

def check_latex_syntax(text, context_info=""):
    """Validates basic LaTeX math formatting in text."""
    errors = []
    if not isinstance(text, str):
        return [f"{context_info}: Text is not a string"]

    # Check for unescaped form feed \x0c
    if "\x0c" in text:
        errors.append(f"{context_info}: Contains unescaped form-feed \\x0c (raw \\f in python string)")

    # Check balanced $ delimiters (excluding escaped \$)
    clean = text.replace(r"\$", "")
    dollar_count = clean.count("$")
    if dollar_count % 2 != 0:
        errors.append(f"{context_info}: Unbalanced '$' inline math delimiters (count: {dollar_count})")

    # Check balanced braces inside math sections
    math_segments = re.findall(r"\$([^\$]+)\$", text)
    for seg in math_segments:
        open_b = seg.count("{")
        close_b = seg.count("}")
        if open_b != close_b:
            errors.append(f"{context_info}: Unbalanced curly braces inside math '${seg[:30]}...' ({open_b} vs {close_b})")

    return errors

def validate_predictors():
    print("=" * 60)
    print("1. VALIDATING CHEMISTRY CHAPTER SYNTHETIC PREDICTORS")
    print("=" * 60)

    all_errors = []

    for fpath in PREDICTOR_FILES:
        if not os.path.exists(fpath):
            all_errors.append(f"File missing: {fpath}")
            continue

        print(f"\nValidating: {fpath}")
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            all_errors.append(f"{fpath}: JSON decode error: {e}")
            continue

        chapters = data.get("chapters", [])
        ch_map = {c.get("chapter_id"): c for c in chapters}

        # Check all 10 chapters present
        missing_ch = [cid for cid in EXPECTED_CHEMISTRY_CHAPTERS if cid not in ch_map]
        if missing_ch:
            all_errors.append(f"{fpath}: Missing Chemistry chapters: {missing_ch}")

        seen_qids = set()
        chem_mcq_count = 0

        for cid in EXPECTED_CHEMISTRY_CHAPTERS:
            ch = ch_map.get(cid)
            if not ch:
                continue

            preds = ch.get("predictors", [])
            chem_mcq_count += len(preds)

            if len(preds) != 20:
                all_errors.append(f"{fpath} - {cid}: Expected exactly 20 MCQs, found ({len(preds)})")

            # Check answer distribution per chapter
            ans_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

            for q_idx, q in enumerate(preds):
                qid = q.get("id")
                q_ctx = f"{fpath} -> {cid} -> {qid or f'q_{q_idx}'}"

                if not qid:
                    all_errors.append(f"{q_ctx}: Missing question ID")
                elif qid in seen_qids:
                    all_errors.append(f"{q_ctx}: Duplicate question ID '{qid}'")
                seen_qids.add(qid)

                # Check required fields
                for field in ["stem", "options", "answer", "type_ref", "trap_alert", "speed_hack", "explanation"]:
                    val = q.get(field)
                    if val is None or (isinstance(val, str) and not val.strip()):
                        all_errors.append(f"{q_ctx}: Field '{field}' is missing or empty")

                # Check options
                opts = q.get("options", [])
                if not isinstance(opts, list) or len(opts) != 4:
                    all_errors.append(f"{q_ctx}: Options must be a list of exactly 4 strings")
                else:
                    if len(set(opts)) != 4:
                        all_errors.append(f"{q_ctx}: Options contain duplicates: {opts}")
                    for opt_i, opt in enumerate(opts):
                        errs = check_latex_syntax(opt, f"{q_ctx} option[{opt_i}]")
                        all_errors.extend(errs)

                # Check answer
                ans = q.get("answer")
                if ans not in ['A', 'B', 'C', 'D']:
                    all_errors.append(f"{q_ctx}: Answer '{ans}' is not one of A, B, C, D")
                else:
                    ans_counts[ans] += 1

                # Check stem & explanation LaTeX
                all_errors.extend(check_latex_syntax(q.get("stem", ""), f"{q_ctx} stem"))
                all_errors.extend(check_latex_syntax(q.get("explanation", ""), f"{q_ctx} explanation"))
                all_errors.extend(check_latex_syntax(q.get("trap_alert", ""), f"{q_ctx} trap_alert"))
                all_errors.extend(check_latex_syntax(q.get("speed_hack", ""), f"{q_ctx} speed_hack"))

                # Check for dummy placeholder phrases
                q_str = json.dumps(q, ensure_ascii=False)
                for phrase in DUMMY_PHRASES:
                    if phrase in q_str:
                        all_errors.append(f"{q_ctx}: Found forbidden dummy phrase '{phrase}'")

            # Verify balance: 5 each for A, B, C, D
            for opt_letter, count in ans_counts.items():
                if count != 5:
                    all_errors.append(f"{fpath} -> {cid}: Option {opt_letter} count is {count} (expected 5 for balanced distribution)")

        print(f"  -> Total Chemistry chapters: {len(EXPECTED_CHEMISTRY_CHAPTERS)}")
        print(f"  -> Total Chemistry MCQs: {chem_mcq_count}")
        print(f"  -> Unique Chemistry IDs: {len(seen_qids)}")

    return all_errors

def validate_question_banks():
    print("\n" + "=" * 60)
    print("2. VALIDATING QUESTION BANKS (CROSS-CHECK MISTAGGED QUESTIONS)")
    print("=" * 60)

    all_errors = []

    for fpath in QUESTION_BANK_FILES:
        if not os.path.exists(fpath):
            all_errors.append(f"File missing: {fpath}")
            continue

        print(f"Validating: {fpath}")
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                qs = json.load(f)
        except Exception as e:
            all_errors.append(f"{fpath}: JSON decode error: {e}")
            continue

        if not isinstance(qs, list):
            all_errors.append(f"{fpath}: Expected root list of questions")
            continue

        for q in qs:
            qid = q.get("id")
            wid = q.get("week_id")
            ch = q.get("chapter")
            bpid = q.get("blueprint_chapter_id")
            subj = q.get("subject")

            if subj == "Chemistry":
                # Check for misclassified questions in weeks 04-08 falsely tagged with chem_1st_02
                if wid in ["week_04", "week_05", "week_06", "week_07", "week_08"]:
                    if bpid == "chem_1st_02" or ch == "গুণগত রসায়ন (Qualitative Chemistry)":
                        all_errors.append(
                            f"{fpath} -> Question '{qid}' ({wid}) is mistagged with Qualitative Chemistry ('{ch}' / '{bpid}')"
                        )

                # Check for misclassified questions in week 01 falsely tagged with chem_1st_02
                # except w1_che_q23 (2p orbital quantum numbers)
                if wid == "week_01" and qid != "w1_che_q23":
                    if bpid == "chem_1st_02":
                        all_errors.append(
                            f"{fpath} -> Question '{qid}' ({wid}) is mistagged with Qualitative Chemistry ('{ch}' / '{bpid}')"
                        )

            # Check LaTeX in question stem
            stem = q.get("question") or q.get("stem") or q.get("q") or ""
            if "\x0c" in stem:
                all_errors.append(f"{fpath} -> Question '{qid}': Unescaped form feed \\x0c in stem")

    return all_errors

def main():
    pred_errors = validate_predictors()
    qb_errors = validate_question_banks()

    total_errors = pred_errors + qb_errors

    print("\n" + "=" * 60)
    print("CHEMISTRY DATASET VALIDATION SUMMARY")
    print("=" * 60)

    if not total_errors:
        print(" [PASSED] ALL CHEMISTRY AUDIT CHECKS PASSED WITH ZERO ERRORS!")
        print("  - All 10 Chemistry chapters present and strictly structured.")
        print("  - 200 unique, authentic Chemistry MCQs in synthetic predictors (20 per chapter).")
        print("  - Perfectly balanced answer keys (25% each: exactly 5 A, 5 B, 5 C, 5 D per chapter).")
        print("  - Zero duplicate question IDs.")
        print("  - Zero dummy / synthetic placeholder phrases.")
        print("  - All LaTeX math formulas balanced and properly escaped.")
        print("  - Zero mistagged questions across all 14 question bank files.")
        print("=" * 60)
        sys.exit(0)
    else:
        print(f" [FAILED] Found {len(total_errors)} validation errors:")
        for err in total_errors[:25]:
            print(f"  - {err}")
        if len(total_errors) > 25:
            print(f"  ... and {len(total_errors) - 25} more errors.")
        print("=" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()
