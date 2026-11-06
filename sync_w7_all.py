#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_w7_all.py
Synchronizes curated Week 07 data across all repository stores:
- admission_webapp/src/data/varsity_bank.json & root varsity_bank.json
- admission_webapp/src/data/medical_bank.json & root medical_bank.json
- admission_webapp/src/data/quizzes.json
- admission_webapp/src/data/questions.json & root questions.json
- admission_webapp/src/data/vault.json
- admission_webapp/src/data/weeks.json
- admission_webapp/src/data/predictor_sets.json & root predictor_sets.json
"""

import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from curate_w7_varsity import get_varsity_questions, get_du_written_problems
from curate_w7_medical import get_medical_questions
from curate_w7_vault import get_vault_entries, get_week_07_meta, get_week_07_predictor_sets

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DATA_DIR = os.path.join(BASE_DIR, "admission_webapp", "src", "data")
SRC_DATA_DIR = os.path.join(BASE_DIR, "src", "data")

def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {path}")

def sync_all():
    print("Beginning multi-stream pattern sync for Week 07...")
    varsity_mcqs = get_varsity_questions()
    written_problems = get_du_written_problems()
    medical_mcqs = get_medical_questions()
    vault_entries = get_vault_entries()
    w7_meta = get_week_07_meta()
    var_pred_set, med_pred_set = get_week_07_predictor_sets(written_problems)

    # 1. VARSITY BANK
    for target in [os.path.join(APP_DATA_DIR, "varsity_bank.json"), os.path.join(SRC_DATA_DIR, "varsity_bank.json"), os.path.join(BASE_DIR, "varsity_bank.json")]:
        data = load_json(target) or []
        # Filter out existing week_07 if any to allow idempotent re-runs
        data = [q for q in data if q.get("week_id") != "week_07"]
        data.extend(varsity_mcqs)
        save_json(target, data)
        print(f"  -> Varsity Bank total items: {len(data)}")

    # 2. MEDICAL BANK
    for target in [os.path.join(APP_DATA_DIR, "medical_bank.json"), os.path.join(SRC_DATA_DIR, "medical_bank.json"), os.path.join(BASE_DIR, "medical_bank.json")]:
        data = load_json(target) or []
        data = [q for q in data if q.get("week_id") != "week_07"]
        data.extend(medical_mcqs)
        save_json(target, data)
        print(f"  -> Medical Bank total items: {len(data)}")

    # 3. QUIZZES & WEEKLY EXAMS (Merged pool for Quizzes / Practice / Weekly Exams)
    q_targets = [
        os.path.join(APP_DATA_DIR, "quizzes.json"),
        os.path.join(SRC_DATA_DIR, "quizzes.json"),
        os.path.join(APP_DATA_DIR, "weekly_exams.json"),
        os.path.join(SRC_DATA_DIR, "weekly_exams.json"),
    ]
    if os.path.exists(os.path.join(BASE_DIR, "quizzes.json")):
        q_targets.append(os.path.join(BASE_DIR, "quizzes.json"))
    for target in q_targets:
        data = load_json(target)
        if not data and "weekly_exams.json" in target:
            # Base it on quizzes.json if newly created
            quiz_src = os.path.join(APP_DATA_DIR, "quizzes.json")
            data = load_json(quiz_src) or []
        data = data or []
        data = [q for q in data if q.get("week_id") != "week_07"]
        data.extend(varsity_mcqs)
        data.extend(medical_mcqs)
        save_json(target, data)
        print(f"  -> Quizzes/Weekly Exams ({os.path.basename(target)}) total items: {len(data)}")

    # 4. QUESTIONS (Merged Master pool)
    for target in [os.path.join(APP_DATA_DIR, "questions.json"), os.path.join(SRC_DATA_DIR, "questions.json"), os.path.join(BASE_DIR, "questions.json")]:
        data = load_json(target) or []
        data = [q for q in data if q.get("week_id") != "week_07"]
        data.extend(varsity_mcqs)
        data.extend(medical_mcqs)
        save_json(target, data)
        print(f"  -> Questions total items: {len(data)}")

    # 5. VAULT
    # Vault entries are kept intact; only populate if empty or missing w7 entries
    for vault_target in [os.path.join(APP_DATA_DIR, "vault.json"), os.path.join(SRC_DATA_DIR, "vault.json")]:
        v_data = load_json(vault_target) or {"entries": [], "triplets": [], "quick_math": [], "magic_fractions": []}
        has_w7 = any(e.get("id", "").startswith("v_w7_") for e in v_data.get("entries", []))
        if not has_w7:
            v_data.setdefault("entries", []).extend(vault_entries)
            save_json(vault_target, v_data)
        print(f"  -> Vault entries total: {len(v_data.get('entries', []))}")

    # 6. WEEKS
    for weeks_target in [os.path.join(APP_DATA_DIR, "weeks.json"), os.path.join(SRC_DATA_DIR, "weeks.json")]:
        weeks_data = load_json(weeks_target) or []
        weeks_data = [w for w in weeks_data if w.get("id") != "week_07"]
        weeks_data.append(w7_meta)
        save_json(weeks_target, weeks_data)
        print(f"  -> Weeks registered: {[w['id'] for w in weeks_data]}")

    # 7. PREDICTOR SETS
    for target in [os.path.join(APP_DATA_DIR, "predictor_sets.json"), os.path.join(SRC_DATA_DIR, "predictor_sets.json"), os.path.join(BASE_DIR, "predictor_sets.json")]:
        ps_data = load_json(target) or {"varsity_sets": [], "medical_sets": []}
        v_sets = [s for s in ps_data.get("varsity_sets", []) if s.get("id") != "var_pred_set_w07"]
        v_sets.append(var_pred_set)
        m_sets = [s for s in ps_data.get("medical_sets", []) if s.get("id") != "med_pred_set_w07"]
        m_sets.append(med_pred_set)
        ps_data["varsity_sets"] = v_sets
        ps_data["medical_sets"] = m_sets
        save_json(target, ps_data)
        print(f"  -> Predictor Sets: {len(v_sets)} varsity sets, {len(m_sets)} medical sets")


    print("\n✅ All JSON stores successfully synchronized for Week 07!")

if __name__ == "__main__":
    sync_all()
