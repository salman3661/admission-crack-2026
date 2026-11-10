# -*- coding: utf-8 -*-
import json
from collections import Counter

files = [
    "questions.json",
    "weekly_exams.json",
    "medical_bank.json",
    "varsity_bank.json",
    "src/data/quizzes.json"
]

for fn in files:
    data = json.load(open(fn))
    ids = [q['id'] for q in data]
    counts = Counter(ids)
    dups = [k for k, v in counts.items() if v > 1]
    print(f"{fn}: total={len(ids)}, unique={len(counts)}, duplicates={len(dups)}")
    if dups:
        print(f"  Sample dups: {dups[:5]}")

