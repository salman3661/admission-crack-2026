#!/usr/bin/env python3
"""
4-Tier Admission Preparation Architecture & Data Isolation Builder
Generates and validates:
  Tier 1: admission_webapp/src/data/weekly_exams.json (Strictly Week 01 - Week 09/10)
  Tier 2: admission_webapp/src/data/paper_final_bank.json (Paper Final Tests: 60 MCQ + 16 Written @ 2.5m)
  Tier 3: admission_webapp/src/data/subject_final_bank.json (Subject-wise & Chapter-wise Varsity + MAT QB)
  Tier 4: admission_webapp/src/data/full_mock_bank.json (Full-Syllabus Master Mock Tests)
"""

import json
import os
import re
from collections import defaultdict

DATA_DIR = os.path.join("admission_webapp", "src", "data")


def load_json(name):
    path = os.path.join(DATA_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(name, data):
    path = os.path.join(DATA_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {path}")


def normalize_subject(subj: str) -> str:
    if not subj:
        return "Physics"
    s = subj.strip()
    if s in ("Higher Mathematics", "Higher Math", "Math", "Mathematics"):
        return "Higher Math"
    if s in ("Physics", "Chemistry", "Biology", "English", "GK"):
        return s
    return s


def normalize_paper(paper: str) -> str:
    if not paper:
        return "১ম পত্র"
    p = paper.strip()
    if p in ("1st", "1st Paper", "১ম পত্র", "Paper 1"):
        return "১ম পত্র"
    if p in ("2nd", "2nd Paper", "২য় পত্র", "২য় পত্র", "Paper 2"):
        return "২য় পত্র"
    return p


def convert_synthetic_to_quiz(pred: dict, chapter: dict, idx: int) -> dict:
    opts = pred.get("options") or []
    ans_raw = pred.get("answer", "")
    ans_idx = 0
    if isinstance(ans_raw, int):
        ans_idx = ans_raw
    elif isinstance(ans_raw, str):
        ans_str = ans_raw.strip()
        if ans_str in opts:
            ans_idx = opts.index(ans_str)
        else:
            # Try matching A/B/C/D or ক/খ/গ/ঘ
            letter_map = {"A": 0, "B": 1, "C": 2, "D": 3, "ক": 0, "খ": 1, "গ": 2, "ঘ": 3}
            if ans_str.upper() in letter_map:
                ans_idx = letter_map[ans_str.upper()]
            else:
                for i, o in enumerate(opts):
                    if ans_str in o or o in ans_str:
                        ans_idx = i
                        break
    subj = normalize_subject(chapter.get("subject", "Physics"))
    paper = normalize_paper(chapter.get("paper", "১ম পত্র"))
    stem = pred.get("stem", "")
    return {
        "id": pred.get("id", f"pf_{chapter.get('chapter_id', 'ch')}_{idx}"),
        "week_id": "paper_final",
        "subject": subj,
        "paper": paper,
        "chapter": chapter.get("chapter_title", ""),
        "blueprint_chapter_id": chapter.get("chapter_id", ""),
        "origin": pred.get("source_tag") or pred.get("source") or f"Paper Final Standard ({paper})",
        "q": stem,
        "question": stem,
        "opts": opts,
        "options": opts,
        "ans": ans_idx,
        "correct_index": ans_idx,
        "exp": pred.get("explanation", ""),
        "explanation": pred.get("explanation", ""),
        "trap": pred.get("trap_alert", ""),
        "trap_alert": pred.get("trap_alert", ""),
        "speed_hack": pred.get("speed_hack", ""),
        "type_ref": pred.get("type_ref", ""),
        "du_topic": pred.get("du_topic"),
        "du_freq": pred.get("du_freq"),
        "du_tier": pred.get("du_tier"),
        "du_badge": pred.get("du_badge"),
        "written_essential": pred.get("written_essential", False),
        "bank_type": "paper_final",
    }


def main():
    weekly_raw = load_json("weekly_exams.json")
    varsity_raw = load_json("varsity_bank.json")
    medical_raw = load_json("medical_bank.json")
    synthetic_raw = load_json("chapter_synthetic_predictors.json")
    du_master = load_json("du_master_predictor_2026.json")
    mat_master = load_json("mat_master_predictor_2026.json")
    predictor_sets = load_json("predictor_sets.json")

    # =========================================================================
    # TIER 1: Weekly Mode (weekly_exams.json)
    # Strictly Week 01 to Week 09/10 — remove seed_full_syllabus contamination
    # =========================================================================
    valid_week_pattern = re.compile(r"^week_(0[1-9]|1[0-2])$")
    clean_weekly = []
    removed_from_weekly = []
    for q in weekly_raw:
        wid = str(q.get("week_id", "")).strip()
        if valid_week_pattern.match(wid):
            item = dict(q)
            item["subject"] = normalize_subject(item.get("subject", ""))
            item["bank_type"] = "weekly"
            clean_weekly.append(item)
        else:
            removed_from_weekly.append(q)

    save_json("weekly_exams.json", clean_weekly)
    print(f"Tier 1 (weekly_exams.json): {len(clean_weekly)} weekly questions kept, {len(removed_from_weekly)} non-weekly removed.")

    # =========================================================================
    # TIER 2: Paper Final Section (paper_final_bank.json)
    # Dedicated exclusively to college/coaching-standard Paper Final model tests
    # Varsity: 60 MCQs + 16 Written (2.5 marks each = 40 marks, total 100 marks)
    # Medical: 60 MCQs (MAT Paper Final standard, 60 marks, 40 mins)
    # =========================================================================
    paper_pools = defaultdict(list)
    for ch in synthetic_raw.get("chapters", []):
        subj = normalize_subject(ch.get("subject", ""))
        paper = normalize_paper(ch.get("paper", "১ম পত্র"))
        for idx, pred in enumerate(ch.get("predictors", [])):
            paper_pools[(subj, paper)].append(convert_synthetic_to_quiz(pred, ch, idx))

    # Collect all written problems by subject from du_master + predictor_sets
    written_by_subject = defaultdict(list)
    seen_problems = set()
    for s in du_master.get("sets", []) + predictor_sets.get("varsity_sets", []):
        for wp in s.get("written_problems", []):
            subj = normalize_subject(wp.get("subject", "Physics"))
            prob_text = wp.get("problem", "").strip()
            if prob_text and prob_text not in seen_problems:
                seen_problems.add(prob_text)
                written_by_subject[subj].append({
                    "subject": subj,
                    "problem": prob_text,
                    "marks": 2.5,
                    "solution": wp.get("solution", ""),
                    "rubric": wp.get("rubric", "সূত্র ও ধারণা: ১.০ | সঠিক গণনা: ১.০ | একক ও চূড়ান্ত উত্তর: ০.৫"),
                })

    # Also supplement written problems from written_essential questions in varsity_bank if < 32 per subject
    for q in varsity_raw:
        subj = normalize_subject(q.get("subject", ""))
        if subj in ("Physics", "Chemistry", "Higher Math", "Biology") and q.get("written_essential"):
            prob_text = re.sub(r"^\[.*?\]\s*", "", q.get("q", "")).strip()
            if prob_text and prob_text not in seen_problems:
                seen_problems.add(prob_text)
                opts = q.get("opts") or []
                ans_idx = q.get("ans", 0)
                ans_val = opts[ans_idx] if 0 <= ans_idx < len(opts) else ""
                sol = q.get("exp") or f"সঠিক উত্তর: {ans_val}"
                written_by_subject[subj].append({
                    "subject": subj,
                    "problem": f"{prob_text} (গাণিতিক/তাত্ত্বিক প্রমাণ ও ব্যাখ্যা দাও)",
                    "marks": 2.5,
                    "solution": sol,
                    "rubric": "মূল সূত্র/তত্ত্ব: ১.০ | ধাপে ধাপে সমাধান: ১.০ | চূড়ান্ত উত্তর: ০.৫",
                })

    paper_final_tests = []
    subject_meta = [
        ("Physics", "পদার্থবিজ্ঞান", "⚛️"),
        ("Chemistry", "রসায়ন", "🧪"),
        ("Higher Math", "উচ্চতর গণিত", "📐"),
        ("Biology", "জীববিজ্ঞান", "🧬"),
    ]

    for subj, subj_bn, icon in subject_meta:
        w_pool = written_by_subject[subj]
        for paper_idx, (paper_code, paper_bn) in enumerate([("১ম পত্র", "1st Paper"), ("২য় পত্র", "2nd Paper")]):
            mcq_pool = paper_pools[(subj, paper_code)]
            mcqs = mcq_pool[:60]
            # Split written pool deterministically between 1st and 2nd paper (16 each)
            start_w = paper_idx * 16
            written_16 = w_pool[start_w:start_w + 16]
            if len(written_16) < 16 and len(w_pool) > 0:
                # Wrap around without crashing if pool is slightly under 32
                needed = 16 - len(written_16)
                written_16 = written_16 + w_pool[:needed]

            paper_final_tests.append({
                "id": f"pf_varsity_{subj.lower().replace(' ', '_')}_{paper_idx + 1}",
                "title": f"{icon} {subj} {paper_bn} Full Test ({subj_bn} {paper_code})",
                "subtitle": "কলেজ ও কোচিং-স্ট্যান্ডার্ড পেপার ফাইনাল মডেল টেস্ট",
                "track": "varsity",
                "subject": subj,
                "subject_bn": subj_bn,
                "paper": paper_code,
                "paper_en": paper_bn,
                "badge": f"Paper Final • {paper_code}",
                "duration_minutes": 90,
                "total_marks": 100,
                "mcq_marks": 60,
                "written_marks": 40,
                "written_marks_per_question": 2.5,
                "negative_marking": 0.25,
                "target_mcqs": len(mcqs),
                "target_written": len(written_16),
                "mcqs": mcqs,
                "written_questions": written_16,
            })

            # Medical MAT-standard Paper Final (for Physics, Chemistry, Biology)
            if subj in ("Physics", "Chemistry", "Biology"):
                med_mcqs = [q for q in medical_raw if normalize_subject(q.get("subject", "")) == subj][:60]
                if len(med_mcqs) < 60:
                    # Supplement with textbook-line synthetic mcqs
                    existing_ids = {m["id"] for m in med_mcqs}
                    for extra in mcq_pool:
                        if extra["id"] not in existing_ids:
                            med_mcqs.append(extra)
                        if len(med_mcqs) >= 60:
                            break
                paper_final_tests.append({
                    "id": f"pf_medical_{subj.lower().replace(' ', '_')}_{paper_idx + 1}",
                    "title": f"🩺 MAT {subj} {paper_bn} Final ({subj_bn} {paper_code})",
                    "subtitle": "মেডিকেল এডমিশন (MAT) স্ট্যান্ডার্ড পেপার ফাইনাল",
                    "track": "medical",
                    "subject": subj,
                    "subject_bn": subj_bn,
                    "paper": paper_code,
                    "paper_en": paper_bn,
                    "badge": f"MAT Paper Final • {paper_code}",
                    "duration_minutes": 45,
                    "total_marks": len(med_mcqs),
                    "mcq_marks": len(med_mcqs),
                    "written_marks": 0,
                    "written_marks_per_question": 0,
                    "negative_marking": 0.25,
                    "target_mcqs": len(med_mcqs),
                    "target_written": 0,
                    "mcqs": med_mcqs,
                    "written_questions": [],
                })

    paper_final_bank = {
        "metadata": {
            "tier": "Tier 2: Paper Final Section",
            "description": "Dedicated exclusively to college/coaching-standard Paper Final model tests (60 MCQs + 16 Written @ 2.5 marks). Completely isolated from Weekly Solve Sheets.",
            "total_tests": len(paper_final_tests),
        },
        "tests": paper_final_tests,
    }
    save_json("paper_final_bank.json", paper_final_bank)
    print(f"Tier 2 (paper_final_bank.json): {len(paper_final_tests)} Paper Final tests built.")

    # =========================================================================
    # TIER 3: Subject-wise Final Model (subject_final_bank.json)
    # Chapter-wise and subject-wise comprehensive past-paper banks
    # Varsity QB + Medical MAT QB mapped strictly by subject and track
    # =========================================================================
    varsity_qb = []
    for q in varsity_raw:
        item = dict(q)
        item["subject"] = normalize_subject(item.get("subject", ""))
        item["track"] = "varsity"
        item["bank_type"] = "varsity"
        varsity_qb.append(item)

    # Include non-weekly seed_full_syllabus items into varsity_qb if not already present
    existing_v_ids = {q["id"] for q in varsity_qb}
    for q in removed_from_weekly:
        if q.get("id") not in existing_v_ids:
            item = dict(q)
            item["subject"] = normalize_subject(item.get("subject", ""))
            item["track"] = "varsity"
            item["bank_type"] = "varsity"
            varsity_qb.append(item)

    medical_qb = []
    for q in medical_raw:
        item = dict(q)
        item["subject"] = normalize_subject(item.get("subject", ""))
        item["track"] = "medical"
        item["bank_type"] = "medical"
        medical_qb.append(item)

    subject_final_bank = {
        "metadata": {
            "tier": "Tier 3: Subject-wise Final Model",
            "description": "Chapter-wise and subject-wise comprehensive past-paper banks (Varsity QB + Medical MAT QB mapped strictly by subject and track).",
            "varsity_count": len(varsity_qb),
            "medical_count": len(medical_qb),
        },
        "varsity": varsity_qb,
        "medical": medical_qb,
    }
    save_json("subject_final_bank.json", subject_final_bank)
    print(f"Tier 3 (subject_final_bank.json): varsity={len(varsity_qb)}, medical={len(medical_qb)}")

    # =========================================================================
    # TIER 4: Final Model Test (full_mock_bank.json)
    # Full-syllabus master mock tests simulating DU Science 'Ka' & Medical MAT
    # =========================================================================
    varsity_by_subj = defaultdict(list)
    for q in varsity_qb:
        varsity_by_subj[q["subject"]].append(q)

    medical_by_subj = defaultdict(list)
    for q in medical_qb:
        medical_by_subj[q["subject"]].append(q)

    def build_balanced_mcqs(by_subj_pool, weights: dict, target: int, offset: int = 0):
        chosen = []
        used_ids = set()
        for subj, count in weights.items():
            pool = by_subj_pool.get(subj, [])
            if not pool:
                continue
            start = (offset * 7) % len(pool)
            rotated = pool[start:] + pool[:start]
            for q in rotated:
                if q["id"] not in used_ids:
                    chosen.append(q)
                    used_ids.add(q["id"])
                if len([c for c in chosen if c["subject"] == subj]) >= count:
                    break
        # Fill remaining if any
        if len(chosen) < target:
            for subj, pool in by_subj_pool.items():
                for q in pool:
                    if q["id"] not in used_ids:
                        chosen.append(q)
                        used_ids.add(q["id"])
                    if len(chosen) >= target:
                        break
                if len(chosen) >= target:
                    break
        return chosen[:target]

    varsity_mocks = []
    for idx, s in enumerate(du_master.get("sets", [])):
        m = dict(s)
        m["track"] = "varsity"
        m["standard"] = "DU Science 'Ka' Unit Standard"
        m["written_included"] = True
        varsity_mocks.append(m)

    # Add full-syllabus sets from predictor_sets (excluding weekly-only sets 04/05/06/w07)
    for idx, s in enumerate(predictor_sets.get("varsity_sets", [])):
        sid = s.get("id", "")
        if sid.startswith("du_2026_master_set"):
            continue
        if any(w in sid for w in ("set_04", "set_05", "set_06", "set_w07")):
            continue
        m = dict(s)
        m["track"] = "varsity"
        m["standard"] = "DU 'Ka' & Engineering/GST Standard"
        if not m.get("questions"):
            target = m.get("target_mcqs") or 60
            per_subj = target // 4
            m["questions"] = build_balanced_mcqs(
                varsity_by_subj,
                {"Physics": per_subj, "Chemistry": per_subj, "Higher Math": per_subj, "Biology": target - 3 * per_subj},
                target,
                offset=idx + 1,
            )
        varsity_mocks.append(m)

    medical_mocks = []
    for idx, s in enumerate(mat_master.get("sets", [])):
        m = dict(s)
        m["track"] = "medical"
        m["standard"] = "Medical Admission Test (MAT) Standard"
        m["written_included"] = False
        medical_mocks.append(m)

    for idx, s in enumerate(predictor_sets.get("medical_sets", [])):
        sid = s.get("id", "")
        if sid.startswith("mat_2026_master_set"):
            continue
        if any(w in sid for w in ("set_04", "set_05", "set_06", "set_w07")):
            continue
        m = dict(s)
        m["track"] = "medical"
        m["standard"] = "Medical Admission Test (MAT) Standard"
        if not m.get("questions"):
            target = m.get("target_mcqs") or 100
            m["questions"] = build_balanced_mcqs(
                medical_by_subj,
                {"Biology": 30, "Chemistry": 25, "Physics": 20, "English": 15, "GK": 10},
                target,
                offset=idx + 1,
            )
        medical_mocks.append(m)

    full_mock_bank = {
        "metadata": {
            "tier": "Tier 4: Final Model Test",
            "description": "Full-syllabus master mock tests simulating final admission standards (DU Science 'Ka' Unit & Engineering / Medical MAT standards).",
            "varsity_mocks_count": len(varsity_mocks),
            "medical_mocks_count": len(medical_mocks),
        },
        "varsity_mocks": varsity_mocks,
        "medical_mocks": medical_mocks,
    }
    save_json("full_mock_bank.json", full_mock_bank)
    print(f"Tier 4 (full_mock_bank.json): varsity_mocks={len(varsity_mocks)}, medical_mocks={len(medical_mocks)}")


if __name__ == "__main__":
    main()
