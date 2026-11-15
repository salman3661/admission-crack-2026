#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_physics_main.py
Assembles all 21 curated Physics chapters (330 authentic MCQs):
- Part 1: phy_1st_01 to phy_1st_06 (112 MCQs)
- Part 2: phy_1st_07 to phy_1st_10 (56 MCQs)
- Part 3: phy_2nd_01 to phy_2nd_06 (88 MCQs)
- Part 4: phy_2nd_07 to phy_2nd_11 (74 MCQs)

Replaces Physics chapters in:
1. src/data/chapter_synthetic_predictors.json
2. admission_webapp/src/data/chapter_synthetic_predictors.json

Naturally distributes answer keys across A, B, C, D (25% each)
while perfectly maintaining answer correctness and option integrity.
"""

import json
import os
from curate_physics_p1 import get_part1_chapters
from curate_physics_p2 import get_part2_chapters
from curate_physics_p3 import get_part3_chapters
from curate_physics_p4 import get_part4_chapters

TARGET_FILES = [
    "src/data/chapter_synthetic_predictors.json",
    "admission_webapp/src/data/chapter_synthetic_predictors.json"
]

def balance_answer_distribution(predictors):
    """
    Given predictors where options[0] is the correct answer and answer is 'A',
    distributes the answers across 'A', 'B', 'C', 'D' deterministically
    by placing the correct answer at target_idx = i % 4 and updating the answer key.
    """
    letters = ['A', 'B', 'C', 'D']
    for i, q in enumerate(predictors):
        target_idx = i % 4
        if target_idx != 0:
            opts = list(q["options"])
            # Swap index 0 (correct answer) with target_idx
            opts[0], opts[target_idx] = opts[target_idx], opts[0]
            q["options"] = opts
            q["answer"] = letters[target_idx]
        else:
            q["answer"] = "A"
    return predictors

def assemble_all_physics_chapters():
    raw_chapters = (
        get_part1_chapters() +
        get_part2_chapters() +
        get_part3_chapters() +
        get_part4_chapters()
    )
    
    physics_chapters = []
    total_mcqs = 0
    seen_ids = set()

    for ch in raw_chapters:
        cid = ch["chapter_id"]
        preds = ch["predictors"]
        # Check duplicate IDs within curated dataset
        for q in preds:
            if q["id"] in seen_ids:
                raise ValueError(f"Duplicate question ID found: {q['id']}")
            seen_ids.add(q["id"])

        # Balance answers across A, B, C, D
        balanced_preds = balance_answer_distribution(preds)
        ch["predictors"] = balanced_preds
        physics_chapters.append(ch)
        total_mcqs += len(balanced_preds)

    print(f"Assembled {len(physics_chapters)} Physics chapters with {total_mcqs} pristine MCQs.")
    return physics_chapters

def update_predictor_files():
    physics_chapters = assemble_all_physics_chapters()
    phy_ids = {c["chapter_id"] for c in physics_chapters}

    for file_path in TARGET_FILES:
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found. Skipping.")
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        existing_chapters = data.get("chapters", [])
        
        # Keep all non-Physics chapters
        non_physics = [c for c in existing_chapters if c.get("chapter_id") not in phy_ids and c.get("subject") != "Physics"]
        
        # Combine non-physics and new physics chapters
        # Put Physics first or in natural order
        combined_chapters = physics_chapters + non_physics
        
        total_preds = sum(len(c.get("predictors", [])) for c in combined_chapters)
        
        data["chapters"] = combined_chapters
        if "metadata" in data:
            data["metadata"]["total_chapters"] = len(combined_chapters)
            data["metadata"]["total_predictors"] = total_preds
            data["metadata"]["version"] = "2026.3-curated"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Successfully updated {file_path}:")
        print(f"  - Total chapters: {len(combined_chapters)}")
        print(f"  - Total predictors: {total_preds}")

if __name__ == "__main__":
    update_predictor_files()
