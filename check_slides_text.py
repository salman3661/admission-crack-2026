import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

import glob

for f in sorted(glob.glob("Week_04/01_Varsity_Ka/*.pdf")):
    doc = pymupdf.open(f)
    print(f"\n====================================\nFILE: {f} ({len(doc)} pages)", flush=True)
    text_sample = ""
    for p in range(min(5, len(doc))):
        t = doc[p].get_text().strip()
        if t:
            text_sample += f"\n--- Page {p+1} ---\n" + t[:250]
    if text_sample:
        print(text_sample, flush=True)
    else:
        print("No text in first 5 pages.", flush=True)
