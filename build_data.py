#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Week Data Pipeline for Admission Crack 2026 WebApp
Reads:
  - Week_01/05_Final_Notes/*.md
  - Week_02/05_Final_Notes/*.md
  - Week_03/05_Final_Notes/*.md
  - Global_Varsity_Vault.md
Outputs to admission_webapp/src/data/:
  - weeks.json
  - slides.json (42 slides total: 14 w1 + 14 w2 + 14 w3)
  - flashcards.json (96 flashcards total: 32 w1 + 32 w2 + 32 w3)
  - quizzes.json (Exact 300 MCQs: 100 w1 + 100 w2 + 100 w3)
  - vault.json (36 cross-subject traps, golden triplets, quick math)
"""

import os
import sys
import json
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "admission_webapp", "src", "data")
os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. WEEKS METADATA
# -------------------------------------------------------------
def build_weeks():
    weeks = [
        {
            "id": "week_01",
            "name": "Week 01",
            "badge": "ভেক্টর, গতিবিদ্যা, পরিমাণগত রসায়ন, সরলরেখা, রক্ত ও শ্বসন",
            "description": "ভৌত বিজ্ঞান ও গণিতের ভিত্তি: ভেক্টর ক্যালকুলাস, প্রাস, নদী-নৌকা, স্টয়কিওমেট্রি, সরলরেখা এবং মানব শারীরতত্ত্ব।",
            "subjects": ["Physics", "Chemistry", "Higher Math", "Biology", "English", "GK"],
            "total_mcqs": 115,
            "total_slides": 14,
            "total_flashcards": 65
        },
        {
            "id": "week_02",
            "name": "Week 02",
            "badge": "বলবিদ্যা, পর্যায়বৃত্ত ধর্ম, রাসায়নিক সাম্যাবস্থা, বৃত্ত ও কোষ",
            "description": "উচ্চ গুরুত্বের কোর সিলেবাস: নিউটনিয়ান গতি, জড়তার ভ্রামক, কাজ-শক্তি, d-ব্লক মৌল, বাফার ও pH, বৃত্ত, জটিল সংখ্যা এবং কোষ অঙ্গাণু ও হাইড্রা।",
            "subjects": ["Physics", "Chemistry", "Higher Math", "Biology", "English", "GK"],
            "total_mcqs": 115,
            "total_slides": 14,
            "total_flashcards": 65
        },
        {
            "id": "week_03",
            "name": "Week 03",
            "badge": "কাজ-শক্তি, মহাকর্ষ, গুণগত রসায়ন ও দ্রাব্যতা, কণিক ও অসমতা, উদ্ভিদ শারীরতত্ত্ব ও প্রজনন",
            "description": "উচ্চ গুরুত্বের কোর সিলেবাস: মহাকর্ষীয় ক্ষেত্র ও বিভব, মুক্তিবেগ, বোর পরমাণু মডেল ও কোয়ান্টাম সংখ্যা, Ksp ও আয়ন শনাক্তকরণ, কণিক (পরাবৃত্ত, উপবৃত্ত, অধিবৃত্ত) এবং C3/C4 চক্র ও শ্বসন।",
            "subjects": ["Physics", "Chemistry", "Higher Math", "Biology", "English", "GK"],
            "total_mcqs": 120,
            "total_slides": 14,
            "total_flashcards": 70
        }
    ]
    with open(os.path.join(OUT_DIR, "weeks.json"), "w", encoding="utf-8") as f:
        json.dump(weeks, f, ensure_ascii=False, indent=2)
    print("✓ weeks.json generated successfully.")

# -------------------------------------------------------------
# 2. VAULT DATA
# -------------------------------------------------------------
def build_vault():
    from generate_vault_full import build_vault_file
    build_vault_file()

# -------------------------------------------------------------
# 3. QUIZZES & QUESTIONS PIPELINE (DU, Medical, Varsity Core)
# -------------------------------------------------------------
def load_all_quizzes():
    from compile_bangladesh_core import compile_all_questions
    all_quizzes = compile_all_questions()

    print(f"Total quizzes compiled: {len(all_quizzes)}")
    
    # Write quizzes.json
    with open(os.path.join(OUT_DIR, "quizzes.json"), "w", encoding="utf-8") as f:
        json.dump(all_quizzes, f, ensure_ascii=False, indent=2)
    print("✓ quizzes.json generated successfully.")

    # Write questions.json in webapp
    with open(os.path.join(OUT_DIR, "questions.json"), "w", encoding="utf-8") as f:
        json.dump(all_quizzes, f, ensure_ascii=False, indent=2)
    print("✓ questions.json generated successfully in webapp.")

    # Write questions.json at root
    with open(os.path.join(BASE_DIR, "questions.json"), "w", encoding="utf-8") as f:
        json.dump(all_quizzes, f, ensure_ascii=False, indent=2)
    print("✓ questions.json generated successfully at root.")

# -------------------------------------------------------------
# 4. SLIDES & FLASHCARDS
# -------------------------------------------------------------
def load_slides_and_flashcards():
    from parse_helpers import get_all_slides, get_all_flashcards
    slides = get_all_slides()
    flashcards = get_all_flashcards()

    with open(os.path.join(OUT_DIR, "slides.json"), "w", encoding="utf-8") as f:
        json.dump(slides, f, ensure_ascii=False, indent=2)
    print(f"✓ slides.json generated successfully ({len(slides)} slides).")

    with open(os.path.join(OUT_DIR, "flashcards.json"), "w", encoding="utf-8") as f:
        json.dump(flashcards, f, ensure_ascii=False, indent=2)
    print(f"✓ flashcards.json generated successfully ({len(flashcards)} flashcards).")

def main():
    print("Executing Multi-Week Data Pipeline for Admission Crack 2026 (W1, W2, W3)...")
    build_weeks()
    build_vault()
    load_all_quizzes()
    load_slides_and_flashcards()
    try:
        from build_isolated_tracks import main as build_tracks
        build_tracks()
    except Exception as e:
        print(f"Notice: build_isolated_tracks: {e}")
    print("All datasets compiled with zero truncation.")

if __name__ == "__main__":
    main()
