# -*- coding: utf-8 -*-
import json
from collections import Counter

with open("bio_build/all_predictors.json", "r", encoding="utf-8") as f:
    chapters = json.load(f)

ans_letters = ['A', 'B', 'C', 'D']
total_counts = Counter()

for ch in chapters:
    ch_counts = Counter()
    for i, q in enumerate(ch['predictors']):
        target_idx = i % 4
        # The correct answer is initially at options[0]
        # Swap options[0] and options[target_idx]
        if target_idx != 0:
            q['options'][0], q['options'][target_idx] = q['options'][target_idx], q['options'][0]
        q['answer'] = ans_letters[target_idx]
        ch_counts[q['answer']] += 1
        total_counts[q['answer']] += 1

    print(f"Chapter {ch['chapter_id']} answers: {dict(ch_counts)}")

print(f"\nOverall answer distribution: {dict(total_counts)}")

with open("bio_build/balanced_biology_predictors.json", "w", encoding="utf-8") as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("\nSaved bio_build/balanced_biology_predictors.json!")
