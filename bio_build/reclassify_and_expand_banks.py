# -*- coding: utf-8 -*-
import json
import os
import shutil
from collections import Counter
import sys

sys.path.insert(0, "bio_build")
from refine_classifier import classify_question

# 1. Load balanced biology predictors
with open("bio_build/balanced_biology_predictors.json", "r", encoding="utf-8") as f:
    bio_predictors_by_chap = {c['chapter_id']: c['predictors'] for c in json.load(f)}

all_24_chapters = [f'bio_bot_{i:02d}' for i in range(1, 13)] + [f'bio_zoo_{i:02d}' for i in range(1, 13)]

def make_bank_question(q, ch_id, idx, track, tag_prefix):
    qid = f"{tag_prefix}_{ch_id}_{idx:02d}"
    ans_letter = q['answer']
    ans_idx = ['A', 'B', 'C', 'D'].index(ans_letter)
    origin = "MAT Direct" if track == "medical" else "DU Hubohu"
    tag = f"[{origin}]"
    
    return {
        "id": qid,
        "week_id": "week_08" if "bot" in ch_id else "week_04",
        "subject": "Biology",
        "origin": origin,
        "q": f"{tag} {q['stem']}",
        "question": f"{tag} {q['stem']}",
        "opts": list(q["options"]),
        "options": list(q["options"]),
        "ans": ans_idx,
        "correct_index": ans_idx,
        "exp": q["explanation"],
        "explanation": q["explanation"],
        "trap": q["trap_alert"],
        "trap_insight": q["trap_alert"],
        "trap_alert": q["trap_alert"],
        "track": track,
        "yield_stars": 5,
        "probability": "Very High",
        "intelligence_type": "Analytical",
        "source_book": "Abul Hasan / Gazi Azmal",
        "tag": tag,
        "speed_hack": q["speed_hack"],
        "type_ref": q["type_ref"],
        "blueprint_type_id": f"{ch_id}_t1",
        "blueprint_chapter_id": ch_id,
        "chapter": ch_id,
    }

# =========================================================================
# Reclassify & Expand medical_bank.json
# =========================================================================
print("Processing medical_bank.json...")
with open("medical_bank.json", "r", encoding="utf-8") as f:
    med_data = json.load(f)

# Reclassify existing bio
for q in med_data:
    if q.get("subject") == "Biology":
        new_ch = classify_question(q)
        q["blueprint_chapter_id"] = new_ch
        q["chapter"] = new_ch

# Check counts per chapter
med_counts = Counter(q["blueprint_chapter_id"] for q in med_data if q.get("subject") == "Biology")
existing_med_ids = set(q["id"] for q in med_data)

for ch_id in all_24_chapters:
    current_cnt = med_counts[ch_id]
    target_cnt = 8
    if current_cnt < target_cnt:
        needed = target_cnt - current_cnt
        preds = bio_predictors_by_chap.get(ch_id, [])
        injected = 0
        for i, p in enumerate(preds):
            if injected >= needed:
                break
            new_qid = f"med_qb_{ch_id}_{i+1:02d}"
            if new_qid not in existing_med_ids:
                new_q = make_bank_question(p, ch_id, i+1, "medical", "med_qb")
                med_data.append(new_q)
                existing_med_ids.add(new_qid)
                injected += 1
        print(f"  medical_bank {ch_id}: had {current_cnt}, injected {injected} -> total {current_cnt + injected}")

# Save medical_bank.json
with open("medical_bank.json", "w", encoding="utf-8") as f:
    json.dump(med_data, f, ensure_ascii=False, indent=2)

# =========================================================================
# Reclassify & Expand varsity_bank.json
# =========================================================================
print("\nProcessing varsity_bank.json...")
with open("varsity_bank.json", "r", encoding="utf-8") as f:
    var_data = json.load(f)

for q in var_data:
    if q.get("subject") == "Biology":
        new_ch = classify_question(q)
        q["blueprint_chapter_id"] = new_ch
        q["chapter"] = new_ch

var_counts = Counter(q["blueprint_chapter_id"] for q in var_data if q.get("subject") == "Biology")
existing_var_ids = set(q["id"] for q in var_data)

for ch_id in all_24_chapters:
    current_cnt = var_counts[ch_id]
    target_cnt = 8
    if current_cnt < target_cnt:
        needed = target_cnt - current_cnt
        preds = bio_predictors_by_chap.get(ch_id, [])
        injected = 0
        for i, p in enumerate(preds):
            if injected >= needed:
                break
            new_qid = f"var_qb_{ch_id}_{i+1:02d}"
            if new_qid not in existing_var_ids:
                new_q = make_bank_question(p, ch_id, i+1, "varsity", "var_qb")
                var_data.append(new_q)
                existing_var_ids.add(new_qid)
                injected += 1
        print(f"  varsity_bank {ch_id}: had {current_cnt}, injected {injected} -> total {current_cnt + injected}")

with open("varsity_bank.json", "w", encoding="utf-8") as f:
    json.dump(var_data, f, ensure_ascii=False, indent=2)

# =========================================================================
# Reclassify & Expand questions.json (and weekly_exams.json / quizzes.json)
# =========================================================================
print("\nProcessing questions.json...")
with open("questions.json", "r", encoding="utf-8") as f:
    q_data = json.load(f)

for q in q_data:
    if q.get("subject") == "Biology":
        new_ch = classify_question(q)
        q["blueprint_chapter_id"] = new_ch
        q["chapter"] = new_ch

q_counts = Counter(q["blueprint_chapter_id"] for q in q_data if q.get("subject") == "Biology")
existing_q_ids = set(q["id"] for q in q_data)

for ch_id in all_24_chapters:
    current_cnt = q_counts[ch_id]
    target_cnt = 8
    if current_cnt < target_cnt:
        needed = target_cnt - current_cnt
        preds = bio_predictors_by_chap.get(ch_id, [])
        injected = 0
        for i, p in enumerate(preds):
            if injected >= needed:
                break
            new_qid = f"qb_{ch_id}_{i+1:02d}"
            if new_qid not in existing_q_ids:
                new_q = make_bank_question(p, ch_id, i+1, "medical" if i % 2 == 0 else "varsity", "qb")
                q_data.append(new_q)
                existing_q_ids.add(new_qid)
                injected += 1
        print(f"  questions.json {ch_id}: had {current_cnt}, injected {injected} -> total {current_cnt + injected}")

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

# Copy to weekly_exams.json and quizzes.json
with open("weekly_exams.json", "w", encoding="utf-8") as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

# =========================================================================
# Synchronize data parity across Root, src/data/, and admission_webapp/src/data/
# =========================================================================
print("\nSynchronizing data parity across all mirrors...")
targets = ["src/data", "admission_webapp/src/data"]
files_to_sync = ["questions.json", "weekly_exams.json", "medical_bank.json", "varsity_bank.json"]

for target in targets:
    for fn in files_to_sync:
        dst = os.path.join(target, fn)
        shutil.copyfile(fn, dst)
        print(f"  Synced {fn} -> {dst}")
    # quizzes.json in src/data and admission_webapp/src/data
    q_dst = os.path.join(target, "quizzes.json")
    shutil.copyfile("questions.json", q_dst)
    print(f"  Synced questions.json -> {q_dst}")

print("\nSUCCESS: All question banks expanded and cross-synchronized!")
