# -*- coding: utf-8 -*-
import json
import os

ALL_PRED_FILE = "bio_build/all_predictors.json"

def append_chapter(chapter_id, chapter_title, paper, chapter_no, q_tuples):
    if os.path.exists(ALL_PRED_FILE):
        with open(ALL_PRED_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    # Check if already exists, update or append
    predictors = []
    for i, t in enumerate(q_tuples):
        qid = f"pred_{chapter_id}_{i+1:02d}"
        stem, opt_a, opt_b, opt_c, opt_d, type_ref, trap, hack, exp = t
        predictors.append({
            "id": qid,
            "stem": stem,
            "options": [opt_a, opt_b, opt_c, opt_d],
            "answer": "A",
            "type_ref": type_ref,
            "trap_alert": trap,
            "speed_hack": hack,
            "explanation": exp
        })

    # Remove existing if any
    data = [c for c in data if c.get("chapter_id") != chapter_id]

    data.append({
        "chapter_id": chapter_id,
        "chapter_title": chapter_title,
        "subject": "Biology",
        "paper": paper,
        "chapter_no": chapter_no,
        "predictors": predictors
    })

    with open(ALL_PRED_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Appended {chapter_id} ({len(predictors)} MCQs). Total chapters: {len(data)}")

