# -*- coding: utf-8 -*-
"""
Module providing 200 Curated Flashcards across 4 Topic Decks:
1. 🎯 DU No-Calculator Speed Tricks (50 cards)
2. 🩺 Medical Textbook Exceptions & Values (60 cards)
3. 🇬🇧 High-Yield Medical Prepositions & Vocab (50 cards)
4. 🇧🇩 1971 Liberation War & Core Bangladesh GK Matrix (40 cards)
"""

import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from generate_flashcards import get_flashcards

flashcards_data = get_flashcards()

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OUT_DIR = os.path.join(BASE_DIR, "admission_webapp", "src", "data")
    os.makedirs(OUT_DIR, exist_ok=True)
    out_file = os.path.join(OUT_DIR, "flashcards.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(flashcards_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] {len(flashcards_data)} curated flashcards saved to {out_file} (Curated Topic Decks unconstrained).")
