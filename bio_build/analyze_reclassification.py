# -*- coding: utf-8 -*-
import json
from collections import Counter

# Load rules
from test_classifier import RULES

def classify_q(q):
    text = (q.get('question', q.get('q', '')) + " " + 
            q.get('explanation', q.get('exp', '')) + " " + 
            " ".join(q.get('options', q.get('opts', []))))
    for ch_id, kws in RULES:
        for kw in kws:
            if kw.lower() in text.lower():
                return ch_id
    return q.get('blueprint_chapter_id', 'bio_bot_01')

all_24 = [f'bio_bot_{i:02d}' for i in range(1, 13)] + [f'bio_zoo_{i:02d}' for i in range(1, 13)]

for filename in ['questions.json', 'medical_bank.json', 'varsity_bank.json']:
    data = json.load(open(filename))
    bio_q = [q for q in data if q.get('subject') == 'Biology']
    reclass = Counter()
    for q in bio_q:
        reclass[classify_q(q)] += 1
    
    missing = [ch for ch in all_24 if reclass[ch] == 0]
    low = [ch for ch in all_24 if 0 < reclass[ch] < 4]
    good = [ch for ch in all_24 if reclass[ch] >= 4]
    print(f"=== {filename} ===")
    print(f"Total bio: {len(bio_q)}, Covered chapters: {len(reclass)}/24")
    print(f"Missing chapters ({len(missing)}): {missing}")
    print(f"Low chapters (<4) ({len(low)}): {low}")
    print()

