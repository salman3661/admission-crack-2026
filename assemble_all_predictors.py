#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assemble_all_predictors.py
Combines all synthetic predictors across Physics (10 chapters), Chemistry (8 chapters),
Higher Mathematics (8 chapters), and Biology (8 chapters) into chapter_synthetic_predictors.json.
Total: 34 chapters, 680 MCQs.
"""

import json
import os
import shutil
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

import gen_physics_predictors
import gen_physics_predictors_part2
import gen_physics_predictors_part3
import gen_chemistry_predictors_part1
import gen_chemistry_predictors_part2
import gen_math_predictors_part1
import gen_math_predictors_part2
import gen_math_predictors_part3
import gen_biology_predictors_part1
import gen_biology_predictors_part2

def assemble():
    all_chapters = []

    # Physics (10 chapters)
    p1 = gen_physics_predictors.get_physics_predictors()
    p2 = gen_physics_predictors_part2.get_physics_part2_predictors()
    p3 = gen_physics_predictors_part3.get_physics_part3_predictors()
    all_chapters.extend(p1)
    all_chapters.extend(p2)
    all_chapters.extend(p3)

    # Chemistry (8 chapters)
    c1 = gen_chemistry_predictors_part1.get_chemistry_part1_predictors()
    c2 = gen_chemistry_predictors_part2.get_chemistry_part2_predictors()
    all_chapters.extend(c1)
    all_chapters.extend(c2)

    # Higher Mathematics (8 chapters)
    m1 = gen_math_predictors_part1.get_math_part1_predictors()
    m2 = gen_math_predictors_part2.get_math_part2_predictors()
    m3 = gen_math_predictors_part3.get_math_part3_predictors()
    all_chapters.extend(m1)
    all_chapters.extend(m2)
    all_chapters.extend(m3)

    # Biology (8 chapters)
    b1 = gen_biology_predictors_part1.get_biology_part1_predictors()
    b2 = gen_biology_predictors_part2.get_biology_part2_predictors()
    all_chapters.extend(b1)
    all_chapters.extend(b2)

    print(f"Total chapters assembled: {len(all_chapters)}")

    # Load master blueprint to ensure chapter alignment
    blueprint_path = "src/data/master_chapter_blueprint.json"
    with open(blueprint_path, 'r', encoding='utf-8') as f:
        blueprint_data = json.load(f)
    bp_chapter_ids = [c['id'] for c in blueprint_data['chapters']]

    # Verification
    total_mcqs = 0
    assembled_ids = []
    for ch in all_chapters:
        cid = ch['chapter_id']
        assembled_ids.append(cid)
        mcq_count = len(ch['predictors'])
        total_mcqs += mcq_count
        if cid not in bp_chapter_ids:
            print(f"WARNING: {cid} is not in blueprint chapters!")
        for i, q in enumerate(ch['predictors']):
            assert 'id' in q, f"Missing id in {cid} #{i}"
            assert 'stem' in q, f"Missing stem in {cid} #{i}"
            assert 'options' in q and len(q['options']) == 4, f"Options not 4 in {cid} #{i}"
            assert q['answer'] in ['A', 'B', 'C', 'D'], f"Invalid answer '{q['answer']}' in {cid} #{i}"
            assert 'type_ref' in q, f"Missing type_ref in {cid} #{i}"
            assert 'trap_alert' in q, f"Missing trap_alert in {cid} #{i}"
            assert 'speed_hack' in q, f"Missing speed_hack in {cid} #{i}"

    print(f"Total MCQs verified: {total_mcqs} across {len(assembled_ids)} chapters")

    # Check for missing blueprint chapters
    missing = set(bp_chapter_ids) - set(assembled_ids)
    if missing:
        print(f"CRITICAL: Missing blueprint chapters: {missing}")
    else:
        print("PERFECT: All 34 blueprint chapters have synthetic predictors!")

    output_payload = {
        "metadata": {
            "title": "Master QB Synthetic Predictors (Full Syllabus PCMB)",
            "description": "20 Unseen Synthetic High-Yield Predictors per chapter for Dhaka University Ka Unit and Medical MAT",
            "total_chapters": len(all_chapters),
            "total_predictors": total_mcqs,
            "version": "2.0.0",
            "generated_at": "2026-11-08T09:00:00+06:00"
        },
        "chapters": all_chapters
    }

    # Save to src/data/chapter_synthetic_predictors.json
    out_file1 = "src/data/chapter_synthetic_predictors.json"
    os.makedirs(os.path.dirname(out_file1), exist_ok=True)
    with open(out_file1, 'w', encoding='utf-8') as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"Saved {out_file1} ({os.path.getsize(out_file1):,} bytes)")

    # Save to admission_webapp/src/data/chapter_synthetic_predictors.json
    out_file2 = "admission_webapp/src/data/chapter_synthetic_predictors.json"
    os.makedirs(os.path.dirname(out_file2), exist_ok=True)
    with open(out_file2, 'w', encoding='utf-8') as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"Saved {out_file2} ({os.path.getsize(out_file2):,} bytes)")

    # Ensure master_chapter_blueprint.json is synced
    bp_webapp = "admission_webapp/src/data/master_chapter_blueprint.json"
    shutil.copyfile(blueprint_path, bp_webapp)
    print(f"Synced {bp_webapp}")

if __name__ == '__main__':
    assemble()
