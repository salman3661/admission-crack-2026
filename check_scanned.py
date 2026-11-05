import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

files = [
    'Week_04/01_Varsity_Ka/Weekly 4 Varsity Udvash .pdf',
    'Week_04/02_Medical_Unmesh/Medical_W04_Solution.pdf',
    'Week_04/03_Engineering_Extra/Engineering_W04_Solution.pdf'
]

for f in files:
    doc = pymupdf.open(f)
    print(f"=== {f} ({len(doc)} pages) ===", flush=True)
    for p in range(len(doc)):
        txt = doc[p].get_text()
        if len(txt.strip()) > 20:
            print(f"Page {p+1} has {len(txt)} chars: {repr(txt[:100])}", flush=True)
            # print first 200 chars
            print(txt[:300], flush=True)
            break
    else:
        print("No text found in any page (scanned image).", flush=True)
