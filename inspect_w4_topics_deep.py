import os
import sys
import pymupdf
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
engine = RapidOCR()

def scan_pdf_top(name, path, pages):
    if not os.path.exists(path):
        return
    doc = pymupdf.open(path)
    print(f"\n==================== {name} ====================", flush=True)
    for p in pages:
        if p >= len(doc):
            continue
        page = doc[p]
        pix = page.get_pixmap(dpi=120)
        res, _ = engine(pix.tobytes("png"))
        if res:
            lines = [r[1] for r in res]
            print(f"Page {p+1}: " + " | ".join(lines[:10]), flush=True)

scan_pdf_top("Weekly 04 Varsity", "Week_04/01_Varsity_Ka/Weekly 4 Varsity Udvash .pdf", [0, 1])
scan_pdf_top("Physics P1", "Week_04/01_Varsity_Ka/Physics-04 (Part-01).pdf", [0, 1, 2, 3])
scan_pdf_top("Physics P2", "Week_04/01_Varsity_Ka/Physics-04 (Part-02).pdf", [0, 1, 2, 3])
scan_pdf_top("Chemistry P1", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-01).pdf", [0, 1, 2, 3])
scan_pdf_top("Chemistry P2", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-02).pdf", [0, 1, 2, 3])
scan_pdf_top("Math P1", "Week_04/01_Varsity_Ka/Higher Math-04 (Part-01).pdf", [0, 1, 2])
scan_pdf_top("Math P2", "Week_04/01_Varsity_Ka/Higher Math-04 (Part-02).pdf", [0, 1, 2, 3])
scan_pdf_top("Biology", "Week_04/01_Varsity_Ka/Biology-04 (Part-01+02).pdf", [0, 1, 2, 3, 4])
scan_pdf_top("Medical W04 Sol", "Week_04/02_Medical_Unmesh/Medical_W04_Solution.pdf", [0, 1])
scan_pdf_top("Engineering W04 Sol", "Week_04/03_Engineering_Extra/Engineering_W04_Solution.pdf", [0, 1])
