# -*- coding: utf-8 -*-
"""
Master Dataset Generator for Admission Crack 2026:
Generates:
1. 200 Curated Flashcards across 4 Topic Decks:
   - 🎯 DU No-Calculator Speed Tricks (50 cards)
   - 🩺 Medical Textbook Exceptions & Values (60 cards)
   - 🇬🇧 High-Yield Medical Prepositions & Vocab (50 cards)
   - 🇧🇩 1971 Liberation War & Core Bangladesh GK Matrix (40 cards)
2. 240+ Formula & Trap Vault entries organized by Subject -> Chapter -> Card Types (core_formula, shortcut, trap).
Outputs to:
  - build_data_flashcards.py
  - build_data_vault.py
  - admission_webapp/src/data/flashcards.json
  - admission_webapp/src/data/vault.json
"""

import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "admission_webapp", "src", "data")
os.makedirs(DATA_DIR, exist_ok=True)

# We will populate FLASHCARDS and VAULT_ENTRIES in separate modules or here directly.

