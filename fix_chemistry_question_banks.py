#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_chemistry_question_banks.py
Reclassifies all mistagged Chemistry questions across the question bank JSON files:
- questions.json
- varsity_bank.json
- medical_bank.json
- weekly_exams.json
- src/data/questions.json
- src/data/varsity_bank.json
- src/data/medical_bank.json
- src/data/weekly_exams.json
- src/data/quizzes.json
- admission_webapp/src/data/questions.json
- admission_webapp/src/data/varsity_bank.json
- admission_webapp/src/data/medical_bank.json
- admission_webapp/src/data/weekly_exams.json
- admission_webapp/src/data/quizzes.json
"""

import json
import os

FILES_TO_FIX = [
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

CHEMISTRY_CORRECTIONS = {
    # Week 01
    "w1_che_q03": ("ল্যাবরেটরির নিরাপদ ব্যবহার (Safe Use of Laboratory)", "chem_1st_01"),
    "w1_che_q06": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q07": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q08": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q09": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q12": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w1_che_q13": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w1_che_q14": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q16": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q17": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q19": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q21": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w1_che_q25": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "du_rep_chem_02": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),

    # Week 02
    "w2_che_q01": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w2_che_q03": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w2_che_q04": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w2_che_q05": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w2_che_q07": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w2_che_q08": ("রাসায়নিক পরিবর্তন (Chemical Changes)", "chem_1st_04"),
    "w2_che_q09": ("রাসায়নিক পরিবর্তন (Chemical Changes)", "chem_1st_04"),
    "w2_che_q10": ("রাসায়নিক পরিবর্তন (Chemical Changes)", "chem_1st_04"),
    "w2_che_q11": ("রাসায়নিক পরিবর্তন (Chemical Changes)", "chem_1st_04"),
    "w2_che_q15": ("রাসায়নিক পরিবর্তন (Chemical Changes)", "chem_1st_04"),
    "w2_che_q16": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w2_che_q18": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w2_che_q20": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w2_che_q21": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w2_che_q22": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w2_che_q23": ("রাসায়নিক পরিবর্তন (Chemical Changes)", "chem_1st_04"),
    "w2_che_q24": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w2_che_q25": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),

    # Week 03
    "w3_che_q09": ("গুণগত রসায়ন (Qualitative Chemistry)", "chem_1st_02"),
    "w3_che_q10": ("গুণগত রসায়ন (Qualitative Chemistry)", "chem_1st_02"),
    "w3_che_q12": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w3_che_q17": ("গুণগত রসায়ন (Qualitative Chemistry)", "chem_1st_02"),
    "w3_che_q19": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w3_che_q21": ("পরিমাণগত রসায়ন (Quantitative Chemistry)", "chem_2nd_03"),
    "w3_var_sol_025": ("গুণগত রসায়ন (Qualitative Chemistry)", "chem_1st_02"),
    "w3_var_sol_027": ("গুণগত রসায়ন (Qualitative Chemistry)", "chem_1st_02"),
    "w3_var_sol_033": ("গুণগত রসায়ন (Qualitative Chemistry)", "chem_1st_02"),
    "w3_var_sol_039": ("গুণগত রসায়ন (Qualitative Chemistry)", "chem_1st_02"),

    # Week 04
    "w4_var_017": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_var_021": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_var_022": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_var_023": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_var_024": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_rep_007": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_rep_008": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_rep_009": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_rep_011": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_rep_012": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_med_007": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_med_010": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),
    "w4_med_012": ("মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties)", "chem_1st_03"),

    # Week 05
    "w5_var_016": ("তড়িৎ রসায়ন (Electrochemistry)", "chem_2nd_04"),
    "w5_var_020": ("তড়িৎ রসায়ন (Electrochemistry)", "chem_2nd_04"),
    "w5_var_023": ("তড়িৎ রসায়ন (Electrochemistry)", "chem_2nd_04"),
    "w5_var_024": ("তড়িৎ রসায়ন (Electrochemistry)", "chem_2nd_04"),
    "w5_rep_007": ("ল্যাবরেটরির নিরাপদ ব্যবহার (Safe Use of Laboratory)", "chem_1st_01"),
    "w5_rep_011": ("তড়িৎ রসায়ন (Electrochemistry)", "chem_2nd_04"),
    "w5_med_009": ("তড়িৎ রসায়ন (Electrochemistry)", "chem_2nd_04"),
    "w5_med_010": ("তড়িৎ রসায়ন (Electrochemistry)", "chem_2nd_04"),

    # Week 06 - quizzes
    "w6_quiz_019": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_020": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_021": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_022": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_023": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_024": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_025": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_026": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_027": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_quiz_028": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_quiz_029": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_quiz_030": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_quiz_031": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_032": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_quiz_034": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_quiz_035": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_quiz_078": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_079": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_080": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_081": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_082": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_quiz_083": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),

    # Week 06 - varsity bank
    "w6_var_019": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_020": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_021": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_022": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_023": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_024": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_025": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_026": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_027": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_var_028": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_var_029": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_var_030": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_var_031": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_var_032": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_var_034": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_var_035": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),

    # Week 06 - medical bank
    "w6_med_013": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_014": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_015": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_016": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_017": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_018": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_019": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_020": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_021": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_022": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),
    "w6_med_023": ("অর্থনৈতিক রসায়ন (Economic Chemistry)", "chem_2nd_05"),
    "w6_med_024": ("পরিবেশ রসায়ন (Environmental Chemistry)", "chem_2nd_01"),

    # Week 07
    "w7_var_che_06": ("জৈব রসায়ন (Organic Chemistry)", "chem_2nd_02"),
    "w7_var_che_12": ("জৈব রসায়ন (Organic Chemistry)", "chem_2nd_02"),

    # Week 08
    "w8_che_022": ("জৈব রসায়ন (Organic Chemistry)", "chem_2nd_02"),
}

def apply_fixes():
    total_modified_files = 0
    total_question_fixes = 0

    for fpath in FILES_TO_FIX:
        if not os.path.exists(fpath):
            print(f"Skipping {fpath} (not found)")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            print(f"Skipping {fpath} (not a list)")
            continue

        file_fixes = 0
        for q in data:
            qid = q.get("id")
            if qid in CHEMISTRY_CORRECTIONS:
                new_ch, new_bpid = CHEMISTRY_CORRECTIONS[qid]
                changed = False
                if q.get("chapter") != new_ch:
                    q["chapter"] = new_ch
                    changed = True
                if q.get("blueprint_chapter_id") != new_bpid:
                    q["blueprint_chapter_id"] = new_bpid
                    changed = True
                if changed:
                    file_fixes += 1

        if file_fixes > 0:
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Updated {fpath}: fixed {file_fixes} questions.")
            total_modified_files += 1
            total_question_fixes += file_fixes
        else:
            print(f"No changes needed for {fpath}.")

    print(f"\nFinished! Fixed {total_question_fixes} question entries across {total_modified_files} files.")

if __name__ == "__main__":
    apply_fixes()
