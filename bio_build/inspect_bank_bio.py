# -*- coding: utf-8 -*-
import json
from collections import Counter

data = json.load(open('questions.json'))
bio_q = [q for q in data if q.get('subject') == 'Biology']
print(f"Total bio questions in questions.json: {len(bio_q)}")

# Check chapter distribution
chaps = Counter(q.get('blueprint_chapter_id', q.get('chapter')) for q in bio_q)
print("Current chapter counts:", chaps)

# Let's inspect those in bio_bot_01
bot_01 = [q for q in bio_q if q.get('blueprint_chapter_id') == 'bio_bot_01']
print(f"Count in bio_bot_01: {len(bot_01)}")
for i, q in enumerate(bot_01[:25]):
    stem = q.get('question', q.get('q', ''))
    print(f"{i+1}. id={q['id']} stem={stem[:60]}")

