#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_physics_question_banks.py
Reclassifies all mistagged Physics questions across the question bank JSON files:
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

PHYSICS_CORRECTIONS = {
    # Week 01
    "w1_phy_q03": ("গতিবিদ্যা ও প্রক্ষেপক (Dynamics & Projectile)", "phy_1st_03"),
    "w1_phy_q12": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w1_phy_q14": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w1_phy_q15": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w1_phy_q16": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w1_phy_q17": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w1_phy_q20": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w1_phy_q21": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w1_phy_q23": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w1_phy_q24": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),

    # Week 02
    "w2_phy_q04": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w2_phy_q06": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w2_phy_q07": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w2_phy_q10": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w2_phy_q11": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w2_phy_q13": ("মহাকর্ষ ও অভিকর্ষ (Gravitation & Gravity)", "phy_1st_06"),
    "w2_phy_q15": ("কাজ, শক্তি ও ক্ষমতা (Work, Energy & Power)", "phy_1st_05"),
    "w2_phy_q23": ("কাজ, শক্তি ও ক্ষমতা (Work, Energy & Power)", "phy_1st_05"),

    # Week 03
    "w3_phy_q14": ("জ্যোতির্বিজ্ঞান (Astronomy)", "phy_2nd_11"),
    "w3_phy_q15": ("মহাকর্ষ ও অভিকর্ষ (Gravitation & Gravity)", "phy_1st_06"),
    "w3_phy_q18": ("আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)", "phy_2nd_08"),
    "w3_phy_q23": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w3_var_sol_001": ("কাজ, শক্তি ও ক্ষমতা (Work, Energy & Power)", "phy_1st_05"),
    "w3_var_sol_004": ("কাজ, শক্তি ও ক্ষমতা (Work, Energy & Power)", "phy_1st_05"),
    "w3_var_sol_009": ("নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "phy_1st_04"),
    "w3_var_sol_018": ("কাজ, শক্তি ও ক্ষমতা (Work, Energy & Power)", "phy_1st_05"),

    # Week 04
    "w4_var_001": ("পদার্থের গাঠনিক ধর্ম (Structural Properties of Matter)", "phy_1st_07"),
    "w4_var_004": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),
    "w4_var_006": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),
    "w4_var_010": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),
    "w4_var_011": ("পদার্থের গাঠনিক ধর্ম (Structural Properties of Matter)", "phy_1st_07"),
    "w4_var_012": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),
    "w4_rep_002": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),
    "w4_rep_003": ("পদার্থের গাঠনিক ধর্ম (Structural Properties of Matter)", "phy_1st_07"),
    "w4_rep_005": ("পদার্থের গাঠনিক ধর্ম (Structural Properties of Matter)", "phy_1st_07"),
    "w4_rep_006": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),
    "w4_med_014": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),
    "w4_med_015": ("পদার্থের গাঠনিক ধর্ম (Structural Properties of Matter)", "phy_1st_07"),
    "w4_med_016": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),
    "w4_med_017": ("পদার্থের গাঠনিক ধর্ম (Structural Properties of Matter)", "phy_1st_07"),
    "w4_med_018": ("আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)", "phy_1st_10"),

    # Week 05
    "w5_var_004": ("পর্যায়বৃত্ত গতি (Periodic Motion)", "phy_1st_08"),
    "w5_var_006": ("তরঙ্গ (Waves)", "phy_1st_09"),
    "w5_var_007": ("তরঙ্গ (Waves)", "phy_1st_09"),
    "w5_var_008": ("তরঙ্গ (Waves)", "phy_1st_09"),
    "w5_var_009": ("তরঙ্গ (Waves)", "phy_1st_09"),
    "w5_var_010": ("পর্যায়বৃত্ত গতি (Periodic Motion)", "phy_1st_08"),
    "w5_rep_014": ("তরঙ্গ (Waves)", "phy_1st_09"),
    "w5_rep_016": ("তরঙ্গ (Waves)", "phy_1st_09"),
    "w5_rep_017": ("তরঙ্গ (Waves)", "phy_1st_09"),
    "w5_med_015": ("তরঙ্গ (Waves)", "phy_1st_09"),
    "w5_med_016": ("তরঙ্গ (Waves)", "phy_1st_09"),

    # Week 06
    "w6_quiz_001": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_quiz_003": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_quiz_004": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_quiz_005": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_quiz_008": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_quiz_013": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_quiz_076": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_quiz_077": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_var_004": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_var_005": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_var_013": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_med_008": ("তাপগতিবিদ্যা (Thermodynamics)", "phy_2nd_01"),
    "w6_med_010": ("পরমাণুর মডেল ও নিউক্লিয়ার পদার্থবিজ্ঞান (Atomic & Nuclear Physics)", "phy_2nd_09"),


    # Week 07
    "w7_var_phy_02": ("আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)", "phy_2nd_08"),
    "w7_var_phy_04": ("স্থির তড়িৎ (Electrostatics)", "phy_2nd_02"),
    "w7_var_phy_07": ("আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)", "phy_2nd_08"),
    "w7_var_phy_08": ("আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)", "phy_2nd_08"),
    "w7_var_phy_09": ("আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)", "phy_2nd_08"),
    "w7_var_phy_12": ("আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)", "phy_2nd_08"),
    "w7_med_phy_03": ("আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)", "phy_2nd_08"),
    "w7_med_phy_06": ("আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)", "phy_2nd_08"),

    # Week 08
    "w8_phy_003": ("চল তড়িৎ (Current Electricity)", "phy_2nd_03"),
    "w8_phy_009": ("চল তড়িৎ (Current Electricity)", "phy_2nd_03"),
    "w8_phy_010": ("চল তড়িৎ (Current Electricity)", "phy_2nd_03"),
    "w8_phy_011": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
    "w8_phy_017": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
    "w8_phy_018": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
    "w8_phy_022": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
    "w8_phy_023": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
    "w8_phy_024": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
    "w8_phy_025": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
    "w8_phy_028": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
    "w8_phy_030": ("সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)", "phy_2nd_10"),
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
            if qid in PHYSICS_CORRECTIONS:
                new_ch, new_bpid = PHYSICS_CORRECTIONS[qid]
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
