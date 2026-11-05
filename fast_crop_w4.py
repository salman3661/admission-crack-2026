import os
import sys
import pymupdf
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
engine = RapidOCR()

files = [
    ("Physics P1", "Week_04/01_Varsity_Ka/Physics-04 (Part-01).pdf"),
    ("Physics P2", "Week_04/01_Varsity_Ka/Physics-04 (Part-02).pdf"),
    ("Chemistry P1", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-01).pdf"),
    ("Chemistry P2", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-02).pdf"),
    ("Math P1", "Week_04/01_Varsity_Ka/Higher Math-04 (Part-01).pdf"),
    ("Math P2", "Week_04/01_Varsity_Ka/Higher Math-04 (Part-02).pdf"),
    ("Biology", "Week_04/01_Varsity_Ka/Biology-04 (Part-01+02).pdf"),
    ("Weekly 04 Varsity", "Week_04/01_Varsity_Ka/Weekly 4 Varsity Udvash .pdf"),
    ("Medical W04 Sol", "Week_04/02_Medical_Unmesh/Medical_W04_Solution.pdf"),
    ("Engineering W04 Sol", "Week_04/03_Engineering_Extra/Engineering_W04_Solution.pdf"),
]

for name, path in files:
    if not os.path.exists(path):
        continue
    doc = pymupdf.open(path)
    print(f"\n==================== {name} ====================", flush=True)
    # Check page 0 (cover) and page 1 (syllabus/TOC)
    for pno in [0, 1]:
        if pno >= len(doc): continue
        page = doc[pno]
        # Check text
        t = page.get_text().strip()
        if t:
            print(f"Page {pno+1} Text: {t[:200]}", flush=True)
        else:
            # Crop top 40% of page
            r = page.rect
            crop_rect = pymupdf.Rect(0, 0, r.width, r.height * 0.45)
            pix = page.get_pixmap(clip=crop_rect, dpi=90)
            res, _ = engine(pix.tobytes("png"))
            if res:
                lines = [r[1] for r in res]
                print(f"Page {pno+1} Top OCR: {' // '.join(lines[:8])}", flush=True)
