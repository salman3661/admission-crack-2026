import os
import sys
import pymupdf
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')

engine = RapidOCR()

pdf_files = [
    ("Physics P1", "Week_04/01_Varsity_Ka/Physics-04 (Part-01).pdf"),
    ("Physics P2", "Week_04/01_Varsity_Ka/Physics-04 (Part-02).pdf"),
    ("Chemistry P1", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-01).pdf"),
    ("Chemistry P2", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-02).pdf"),
    ("Math P1", "Week_04/01_Varsity_Ka/Higher Math-04 (Part-01).pdf"),
    ("Math P2", "Week_04/01_Varsity_Ka/Higher Math-04 (Part-02).pdf"),
    ("Biology", "Week_04/01_Varsity_Ka/Biology-04 (Part-01+02).pdf"),
    ("Weekly 4 Udvash", "Week_04/01_Varsity_Ka/Weekly 4 Varsity Udvash .pdf"),
    ("Medical Sol", "Week_04/02_Medical_Unmesh/Medical_W04_Solution.pdf"),
    ("Eng Sol", "Week_04/03_Engineering_Extra/Engineering_W04_Solution.pdf"),
]

for name, path in pdf_files:
    if not os.path.exists(path):
        print(f"NOT FOUND: {path}", flush=True)
        continue
    doc = pymupdf.open(path)
    print(f"\n========================================\nFILE: {name} ({len(doc)} pages)\n========================================", flush=True)
    
    # Check text first
    first_pages_text = ""
    for p in range(min(3, len(doc))):
        t = doc[p].get_text().strip()
        if t:
            first_pages_text += f"\n[P{p+1} Text]: " + t[:300]
    
    if first_pages_text:
        print("Text:", first_pages_text[:600], flush=True)
    else:
        # OCR page 2 (index 1) and page 1
        for pno in [0, 1]:
            if pno < len(doc):
                pix = doc[pno].get_pixmap(dpi=120)
                res, _ = engine(pix.tobytes("png"))
                lines = [r[1] for r in res] if res else []
                print(f"[P{pno+1} OCR]: " + " // ".join(lines[:12]), flush=True)
