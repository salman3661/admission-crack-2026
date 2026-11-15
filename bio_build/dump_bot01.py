# -*- coding: utf-8 -*-
import json

data = json.load(open('questions.json'))
bio_bot_1 = [q for q in data if q.get('subject') == 'Biology' and q.get('blueprint_chapter_id') == 'bio_bot_01']
for i, q in enumerate(bio_bot_1):
    stem = q.get('question', q.get('q', ''))
    print(f"{i+1:02d}. id={q['id']} stem={stem[:75]}")

