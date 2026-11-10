#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_math_main.py
Assembles all 20 curated Higher Mathematics chapters (382 authentic MCQs):
- Part 1: math_1st_01 to math_1st_05 (96 MCQs)
- Part 2: math_1st_06 to math_1st_10 (98 MCQs)
- Part 3: math_2nd_01 to math_2nd_05 (94 MCQs)
- Part 4: math_2nd_06 to math_2nd_10 (94 MCQs)

1. Balances answer keys across A, B, C, D (25% each).
2. Updates chapter_synthetic_predictors.json in src/data/ and admission_webapp/src/data/.
3. Reclassifies 23 mistagged math questions in questions.json, varsity_bank.json, and weekly_exams.json.
4. Seeds authentic questions for 5 missing chapters (math_1st_01, 02, 06, math_2nd_08, 09).
5. Updates master_chapter_blueprint.json counts.
6. Synchronizes all modified JSON datasets across all target locations.
"""

import json
import os

from curate_math_p1 import get_part1_chapters
from curate_math_p2 import get_part2_chapters
from curate_math_p3 import get_part3_chapters
from curate_math_p4 import get_part4_chapters

PREDICTOR_TARGETS = [
    "src/data/chapter_synthetic_predictors.json",
    "admission_webapp/src/data/chapter_synthetic_predictors.json"
]

BLUEPRINT_TARGETS = [
    "src/data/master_chapter_blueprint.json",
    "admission_webapp/src/data/master_chapter_blueprint.json"
]

RECLASSIFICATION_MAP = {
    # w1_mat questions misclassified as 07/08/09/2nd_03
    "w1_mat_q02": "math_1st_03",
    "w1_mat_q05": "math_1st_03",
    "w1_mat_q07": "math_1st_03",
    "w1_mat_q09": "math_1st_03",
    "w1_mat_q10": "math_2nd_02",
    "w1_mat_q11": "math_2nd_02",
    "w1_mat_q12": "math_1st_03",
    "w1_mat_q13": "math_1st_03",
    "w1_mat_q14": "math_1st_03",
    "w1_mat_q16": "math_1st_03",
    "w1_mat_q17": "math_1st_03",
    "w1_mat_q19": "math_1st_03",
    "w1_mat_q21": "math_1st_03",
    "w1_mat_q22": "math_1st_03",
    "w1_mat_q24": "math_1st_03",
    "w1_mat_q25": "math_1st_03",
    # week 3-6 misclassifications
    "w3_var_sol_048": "math_2nd_06", # hyperbola center misclassified in differentiation
    "w4_var_036": "math_2nd_10",     # dispersion/statistics misclassified in differentiation
    "w5_var_028": "math_2nd_04",     # quadratic polynomial
    "w5_var_029": "math_2nd_04",     # common roots
    "w5_var_034": "math_2nd_04",     # quadratic roots relation
    "w6_quiz_045": "math_1st_07",     # triangle properties
    "w6_quiz_048": "math_1st_07"      # trig max/min a*sin + b*cos
}

def balance_answer_distribution(predictors):
    """
    Given predictors where options[0] is correct and answer is 'A',
    distributes the answers across 'A', 'B', 'C', 'D' deterministically
    by placing the correct answer at target_idx = i % 4.
    """
    letters = ['A', 'B', 'C', 'D']
    for i, q in enumerate(predictors):
        target_idx = i % 4
        if target_idx != 0:
            opts = list(q["options"])
            opts[0], opts[target_idx] = opts[target_idx], opts[0]
            q["options"] = opts
            q["answer"] = letters[target_idx]
        else:
            q["answer"] = "A"
    return predictors

def assemble_all_math_chapters():
    raw_chapters = (
        get_part1_chapters() +
        get_part2_chapters() +
        get_part3_chapters() +
        get_part4_chapters()
    )
    
    math_chapters = []
    total_mcqs = 0
    seen_ids = set()

    for ch in raw_chapters:
        cid = ch["chapter_id"]
        preds = ch["predictors"]
        for q in preds:
            if q["id"] in seen_ids:
                raise ValueError(f"Duplicate question ID found: {q['id']}")
            seen_ids.add(q["id"])

        balanced_preds = balance_answer_distribution(preds)
        ch["predictors"] = balanced_preds
        math_chapters.append(ch)
        total_mcqs += len(balanced_preds)

    print(f"Assembled {len(math_chapters)} Higher Math chapters with {total_mcqs} pristine MCQs.")
    return math_chapters

def update_predictor_files(math_chapters):
    math_ids = {c["chapter_id"] for c in math_chapters}

    for file_path in PREDICTOR_TARGETS:
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found. Skipping.")
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        existing_chapters = data.get("chapters", [])
        # Keep non-math chapters
        non_math = [c for c in existing_chapters if c.get("chapter_id") not in math_ids and c.get("subject") not in ["Higher Math", "Higher Mathematics"]]
        
        # Combine
        combined_chapters = non_math + math_chapters
        total_preds = sum(len(c.get("predictors", [])) for c in combined_chapters)

        data["chapters"] = combined_chapters
        if "metadata" in data:
            data["metadata"]["total_chapters"] = len(combined_chapters)
            data["metadata"]["total_predictors"] = total_preds
            data["metadata"]["version"] = "2026.4-curated"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Updated {file_path}: {len(combined_chapters)} chapters, {total_preds} total predictors.")

def update_question_banks(math_chapters):
    """
    1. Reclassifies mistagged math questions in questions.json, varsity_bank.json, weekly_exams.json.
    2. Seeds authentic questions for missing chapters:
       math_1st_01 (10 MCQs), math_1st_02 (10 MCQs), math_1st_06 (10 MCQs),
       math_2nd_08 (10 MCQs), math_2nd_09 (10 MCQs).
    """
    chap_dict = {c["chapter_id"]: c["predictors"] for c in math_chapters}
    missing_chaps = ["math_1st_01", "math_1st_02", "math_1st_06", "math_2nd_08", "math_2nd_09"]
    
    # Process questions.json
    with open("questions.json", 'r', encoding='utf-8') as f:
        qb = json.load(f)

    reclassified_count = 0
    for q in qb:
        qid = q.get("id")
        if qid in RECLASSIFICATION_MAP:
            new_cid = RECLASSIFICATION_MAP[qid]
            q["blueprint_chapter_id"] = new_cid
            q["chapter"] = new_cid
            reclassified_count += 1

    print(f"Reclassified {reclassified_count} questions in questions.json.")

    existing_ids = {q.get("id") for q in qb}
    seeds_added = 0
    for cid in missing_chaps:
        preds = chap_dict.get(cid, [])
        for p in preds[:10]:
            seed_id = f"vb_{p['id']}"
            if seed_id not in existing_ids:
                letter_map = {"A": 0, "B": 1, "C": 2, "D": 3}
                c_idx = letter_map.get(p.get("answer", "A"), 0)
                
                qb_item = {
                    "id": seed_id,
                    "week_id": "seed_full_syllabus",
                    "subject": "Higher Math",
                    "origin": "[DU/Varsity Standard]",
                    "q": p["stem"],
                    "question": p["stem"],
                    "opts": p["options"],
                    "options": p["options"],
                    "ans": p["options"][c_idx],
                    "correct_index": c_idx,
                    "exp": p["explanation"],
                    "explanation": p["explanation"],
                    "trap": p["trap_alert"],
                    "trap_insight": p["trap_alert"],
                    "trap_alert": p["trap_alert"],
                    "tag": p["type_ref"],
                    "speed_hack": p["speed_hack"],
                    "type_ref": p["type_ref"],
                    "blueprint_type_id": f"{cid}_t1",
                    "blueprint_chapter_id": cid,
                    "chapter": cid
                }
                qb.append(qb_item)
                existing_ids.add(seed_id)
                seeds_added += 1

    print(f"Added {seeds_added} seed questions to questions.json for missing chapters.")

    for path in ["questions.json", "src/data/questions.json", "admission_webapp/src/data/questions.json"]:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(qb, f, ensure_ascii=False, indent=2)
        print(f"Synced {path} (total: {len(qb)})")

    # Process weekly_exams.json (mirrors questions.json)
    for path in ["weekly_exams.json", "src/data/weekly_exams.json", "admission_webapp/src/data/weekly_exams.json"]:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(qb, f, ensure_ascii=False, indent=2)
        print(f"Synced {path} (total: {len(qb)})")

    # Update varsity_bank.json
    with open("varsity_bank.json", 'r', encoding='utf-8') as f:
        vb = json.load(f)

    is_list = isinstance(vb, list)
    vb_list = vb if is_list else vb.get("questions", [])
    vb_ids = {q.get("id") for q in vb_list}
    
    for q in vb_list:
        qid = q.get("id")
        if qid in RECLASSIFICATION_MAP:
            new_cid = RECLASSIFICATION_MAP[qid]
            q["blueprint_chapter_id"] = new_cid
            q["chapter"] = new_cid

    vb_seeds = 0
    for cid in missing_chaps:
        preds = chap_dict.get(cid, [])
        for p in preds[:10]:
            seed_id = f"vb_{p['id']}"
            if seed_id not in vb_ids:
                letter_map = {"A": 0, "B": 1, "C": 2, "D": 3}
                c_idx = letter_map.get(p.get("answer", "A"), 0)
                vb_item = {
                    "id": seed_id,
                    "week_id": "varsity_full_syllabus",
                    "subject": "Higher Math",
                    "origin": "[DU/Varsity Standard]",
                    "q": p["stem"],
                    "question": p["stem"],
                    "opts": p["options"],
                    "options": p["options"],
                    "ans": p["options"][c_idx],
                    "correct_index": c_idx,
                    "exp": p["explanation"],
                    "explanation": p["explanation"],
                    "trap": p["trap_alert"],
                    "trap_insight": p["trap_alert"],
                    "trap_alert": p["trap_alert"],
                    "tag": p["type_ref"],
                    "speed_hack": p["speed_hack"],
                    "type_ref": p["type_ref"],
                    "blueprint_type_id": f"{cid}_t1",
                    "blueprint_chapter_id": cid,
                    "chapter": cid
                }
                vb_list.append(vb_item)
                vb_ids.add(seed_id)
                vb_seeds += 1

    print(f"Added {vb_seeds} seed questions to varsity_bank.json.")

    for path in ["varsity_bank.json", "src/data/varsity_bank.json", "admission_webapp/src/data/varsity_bank.json"]:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(vb if not is_list else vb_list, f, ensure_ascii=False, indent=2)
        print(f"Synced {path}")

def update_blueprint():
    for path in BLUEPRINT_TARGETS:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            bp = json.load(f)

        for c in bp.get("chapters", []):
            cid = c.get("id")
            if cid and "math" in cid:
                if c.get("question_count", 0) < 10:
                    c["question_count"] = 10
                if c.get("total_questions", 0) < 20:
                    c["total_questions"] = 20

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(bp, f, ensure_ascii=False, indent=2)
        print(f"Updated blueprint in {path}")

def main():
    print("=== STARTING HIGHER MATH RESTRUCTURING & CURATION ===")
    math_chapters = assemble_all_math_chapters()
    update_predictor_files(math_chapters)
    update_question_banks(math_chapters)
    update_blueprint()
    print("=== HIGHER MATH CURATION & RESTRUCTURING COMPLETE ===")

if __name__ == "__main__":
    main()
