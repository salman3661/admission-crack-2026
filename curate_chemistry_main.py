#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_chemistry_main.py
Assembles all 10 curated Chemistry chapters (200 authentic MCQs, 20 per chapter):
- Chemistry 1st Paper:
  * chem_1st_01: ল্যাবরেটরির নিরাপদ ব্যবহার (Safe Use of Laboratory)
  * chem_1st_02: গুণগত রসায়ন (Qualitative Chemistry)
  * chem_1st_03: মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)
  * chem_1st_04: রাসায়নিক পরিবর্তন (Chemical Changes)
  * chem_1st_05: কর্মমুখী রসায়ন (Applied Chemistry)
- Chemistry 2nd Paper:
  * chem_2nd_01: পরিবেশ রসায়ন (Environmental Chemistry)
  * chem_2nd_02: জৈব রসায়ন (Organic Chemistry)
  * chem_2nd_03: পরিমাণগত রসায়ন (Quantitative Chemistry)
  * chem_2nd_04: তড়িৎ রসায়ন (Electrochemistry)
  * chem_2nd_05: অর্থনৈতিক রসায়ন (Economic Chemistry)

Replaces Chemistry chapters in:
1. src/data/chapter_synthetic_predictors.json
2. admission_webapp/src/data/chapter_synthetic_predictors.json

Naturally balances answer keys across A, B, C, D (25% each, exactly 5 each per chapter)
while maintaining 100% option integrity and mathematical correctness.
"""

import json
import os
import copy
import gen_chemistry_lab_safety as ls
import gen_chemistry_predictors_part1 as p1
import gen_chemistry_predictors_part2 as p2
import gen_chemistry_economic as ec

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

def assemble_all_chemistry_chapters():
    raw_p1 = p1.get_chemistry_part1_predictors()
    raw_p2 = p2.get_chemistry_part2_predictors()
    raw_ls = ls.get_lab_safety_predictors()
    raw_ec = ec.get_economic_predictors()

    chapters_config = [
        {
            "chapter_id": "chem_1st_01",
            "chapter_title": "ল্যাবরেটরির নিরাপদ ব্যবহার (Safe Use of Laboratory)",
            "subject": "Chemistry",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০১",
            "raw_preds": raw_ls["predictors"]
        },
        {
            "chapter_id": "chem_1st_02",
            "chapter_title": "গুণগত রসায়ন (Qualitative Chemistry)",
            "subject": "Chemistry",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০২",
            "raw_preds": raw_p1[0]["predictors"]
        },
        {
            "chapter_id": "chem_1st_03",
            "chapter_title": "মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)",
            "subject": "Chemistry",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৩",
            "raw_preds": raw_p1[1]["predictors"]
        },
        {
            "chapter_id": "chem_1st_04",
            "chapter_title": "রাসায়নিক পরিবর্তন (Chemical Changes)",
            "subject": "Chemistry",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৪",
            "raw_preds": raw_p1[2]["predictors"]
        },
        {
            "chapter_id": "chem_1st_05",
            "chapter_title": "কর্মমুখী রসায়ন (Applied Chemistry)",
            "subject": "Chemistry",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৫",
            "raw_preds": raw_p1[3]["predictors"]
        },
        {
            "chapter_id": "chem_2nd_01",
            "chapter_title": "পরিবেশ রসায়ন (Environmental Chemistry)",
            "subject": "Chemistry",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০১",
            "raw_preds": raw_p2[0]["predictors"]
        },
        {
            "chapter_id": "chem_2nd_02",
            "chapter_title": "জৈব রসায়ন (Organic Chemistry)",
            "subject": "Chemistry",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০২",
            "raw_preds": raw_p2[1]["predictors"]
        },
        {
            "chapter_id": "chem_2nd_03",
            "chapter_title": "পরিমাণগত রসায়ন (Quantitative Chemistry)",
            "subject": "Chemistry",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৩",
            "raw_preds": raw_p2[2]["predictors"]
        },
        {
            "chapter_id": "chem_2nd_04",
            "chapter_title": "তড়িৎ রসায়ন (Electrochemistry)",
            "subject": "Chemistry",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৪",
            "raw_preds": raw_p2[3]["predictors"]
        },
        {
            "chapter_id": "chem_2nd_05",
            "chapter_title": "অর্থনৈতিক রসায়ন (Economic Chemistry)",
            "subject": "Chemistry",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৫",
            "raw_preds": raw_ec
        }
    ]

    chemistry_chapters = []
    seen_ids = set()
    total_mcqs = 0

    for ch_conf in chapters_config:
        cid = ch_conf["chapter_id"]
        preds = copy.deepcopy(ch_conf["raw_preds"])

        if len(preds) != 20:
            raise ValueError(f"Chapter {cid} does not have exactly 20 MCQs (found {len(preds)})")

        for idx, q in enumerate(preds, 1):
            # Standardize ID: pred_chem_1st_01_01, etc.
            new_id = f"pred_{cid}_{idx:02d}"
            q["id"] = new_id

            if new_id in seen_ids:
                raise ValueError(f"Duplicate question ID found: {new_id}")
            seen_ids.add(new_id)

            # Fix missing explanation in pred_chem_2nd_01_17 (orig pred_chem_env_17) if needed
            if cid == "chem_2nd_01" and idx == 17:
                if not q.get("explanation"):
                    q["explanation"] = "গ্রাহামের ব্যাপন সূত্র (নিঃসরণ) কেবল তখনই সঠিকভাবে খাটে যখন পাত্রের ছিদ্রের ব্যাস অণুসমূহের গড় মুক্তপথের চেয়ে ছোট হয়। ছিদ্র বড় হলে অণুগুলোর যৌথ প্রবাহ (hydrodynamic flow) শুরু হয়, ফলে গ্রাহামের সূত্র কার্যকর থাকে না।"

        # Balance answers across A, B, C, D
        balanced_preds = balance_answer_distribution(preds)

        ch_dict = {
            "chapter_id": cid,
            "chapter_title": ch_conf["chapter_title"],
            "subject": ch_conf["subject"],
            "paper": ch_conf["paper"],
            "chapter_no": ch_conf["chapter_no"],
            "predictors": balanced_preds
        }
        chemistry_chapters.append(ch_dict)
        total_mcqs += len(balanced_preds)

    print(f"Assembled {len(chemistry_chapters)} Chemistry chapters with {total_mcqs} pristine MCQs.")
    return chemistry_chapters

def update_predictor_files():
    chemistry_chapters = assemble_all_chemistry_chapters()
    chem_ids = {c["chapter_id"] for c in chemistry_chapters}

    for file_path in TARGET_FILES:
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found. Skipping.")
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        existing_chapters = data.get("chapters", [])

        # Separate existing chapters into: Physics, Chemistry (to replace), Math, Biology, others
        physics_chs = [c for c in existing_chapters if c.get("subject") == "Physics" or c.get("chapter_id", "").startswith("phy_")]
        math_chs = [c for c in existing_chapters if c.get("subject") == "Higher Math" or c.get("chapter_id", "").startswith("math_")]
        bio_chs = [c for c in existing_chapters if c.get("subject") == "Biology" or c.get("chapter_id", "").startswith("bio_")]
        other_chs = [c for c in existing_chapters if c not in physics_chs and c not in math_chs and c not in bio_chs and c.get("chapter_id") not in chem_ids and c.get("subject") != "Chemistry"]

        combined_chapters = physics_chs + chemistry_chapters + math_chs + bio_chs + other_chs
        total_preds = sum(len(c.get("predictors", [])) for c in combined_chapters)

        data["chapters"] = combined_chapters
        if "metadata" in data:
            data["metadata"]["total_chapters"] = len(combined_chapters)
            data["metadata"]["total_predictors"] = total_preds
            data["metadata"]["version"] = "2026.4-chemistry-curated"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Successfully updated {file_path}:")
        print(f"  - Total chapters: {len(combined_chapters)}")
        print(f"  - Total predictors: {total_preds}")

if __name__ == "__main__":
    update_predictor_files()
