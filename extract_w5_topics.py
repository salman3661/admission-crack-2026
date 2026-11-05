import os
import sys
import pymupdf
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')

engine = RapidOCR()

pdf_files = [
    ("Weekly 05 Varsity", "Week_05/01_Varsity_Ka/Weekly 05 Varsity Udvash .pdf"),
    ("Physics P1", "Week_05/01_Varsity_Ka/Physics-05 (Part-01).pdf"),
    ("Physics P2", "Week_05/01_Varsity_Ka/Physics-05 (Part-02).pdf"),
    ("Chemistry P1", "Week_05/01_Varsity_Ka/Chemistry-05 (Part-01).pdf"),
    ("Chemistry P2", "Week_05/01_Varsity_Ka/Chemistry-05 (Part-02).pdf"),
    ("Math P1", "Week_05/01_Varsity_Ka/Higher Math-05 (Part-01).pdf"),
    ("Math P2", "Week_05/01_Varsity_Ka/Higher Math-05 (Part-02).pdf"),
    ("Biology", "Week_05/01_Varsity_Ka/Biology-05 (Part-01+02).pdf"),
    ("Medical Sol", "Week_05/02_Medical_Unmesh/Medical_W05_Solution.pdf"),
    ("Eng Sol", "Week_05/03_Engineering_Extra/Engineering_W05_Solution.pdf"),
]

for name, path in pdf_files:
    if not os.path.exists(path):
        print(f"NOT FOUND: {path}", flush=True)
        continue
    doc = pymupdf.open(path)
    print(f"\n==================== {name} ({len(doc)} pages) ====================", flush=True)
    # Check page 1, 2, 3
    for pno in range(min(3, len(doc))):
        pix = doc[pno].get_pixmap(dpi=130)
        res, _ = engine(pix.tobytes("png"))
        lines = [r[1] for r in res] if res else []
        print(f"--- Page {pno+1} ---", flush=True)
        for line in lines[:15]:
            print(f"  {line}", flush=True)
