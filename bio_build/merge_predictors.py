# -*- coding: utf-8 -*-
import json
import shutil

# Load existing
with open("src/data/chapter_synthetic_predictors.json", "r", encoding="utf-8") as f:
    master = json.load(f)

# Load balanced biology
with open("bio_build/balanced_biology_predictors.json", "r", encoding="utf-8") as f:
    biology_chapters = json.load(f)

# Keep non-bio chapters
non_bio = [c for c in master['chapters'] if 'bio' not in c.get('chapter_id', '')]
print(f"Preserved {len(non_bio)} non-bio chapters.")

# Combine non-bio + biology
combined_chapters = non_bio + biology_chapters
print(f"Total combined chapters: {len(combined_chapters)}")

total_mcqs = sum(len(c['predictors']) for c in combined_chapters)

master['metadata']['total_chapters'] = len(combined_chapters)
master['metadata']['total_predictors'] = total_mcqs
master['metadata']['version'] = "3.0.0"
master['chapters'] = combined_chapters

# Save to src/data/chapter_synthetic_predictors.json
out1 = "src/data/chapter_synthetic_predictors.json"
with open(out1, "w", encoding="utf-8") as f:
    json.dump(master, f, ensure_ascii=False, indent=2)
print(f"Updated {out1}")

# Sync to webapp
out2 = "admission_webapp/src/data/chapter_synthetic_predictors.json"
shutil.copyfile(out1, out2)
print(f"Updated {out2}")

