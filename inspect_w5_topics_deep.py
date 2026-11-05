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
        # Crop top third or full page
        pix = page.get_pixmap(dpi=130)
        res, _ = engine(pix.tobytes("png"))
        if res:
            # print all detected text lines
            lines = [r[1] for r in res]
            print(f"Page {p+1}: " + " | ".join(lines[:12]), flush=True)

# Let's inspect pages 1 to 6 of each slide deck
scan_pdf_top("Physics P1", "Week_05/01_Varsity_Ka/Physics-05 (Part-01).pdf", [0, 1, 2, 3, 4, 5])
scan_pdf_top("Physics P2", "Week_05/01_Varsity_Ka/Physics-05 (Part-02).pdf", [0, 1, 2, 3, 4, 5])
scan_pdf_top("Chemistry P1", "Week_05/01_Varsity_Ka/Chemistry-05 (Part-01).pdf", [0, 1, 2, 3, 4, 5])
scan_pdf_top("Chemistry P2", "Week_05/01_Varsity_Ka/Chemistry-05 (Part-02).pdf", [0, 1, 2, 3, 4, 5])
scan_pdf_top("Math P1", "Week_05/01_Varsity_Ka/Higher Math-05 (Part-01).pdf", [0, 1, 2, 3, 4, 5])
scan_pdf_top("Math P2", "Week_05/01_Varsity_Ka/Higher Math-05 (Part-02).pdf", [0, 1, 2, 3, 4, 5])
scan_pdf_top("Biology", "Week_05/01_Varsity_Ka/Biology-05 (Part-01+02).pdf", [0, 1, 2, 3, 4, 5, 6, 7])
scan_pdf_top("Weekly 05 Varsity", "Week_05/01_Varsity_Ka/Weekly 05 Varsity Udvash .pdf", [0, 1, 5, 10, 15, 20])
scan_pdf_top("Medical W05 Sol", "Week_05/02_Medical_Unmesh/Medical_W05_Solution.pdf", [0, 1, 5, 10, 15, 20])
scan_pdf_top("Engineering W05 Sol", "Week_05/03_Engineering_Extra/Engineering_W05_Solution.pdf", [0, 1, 5, 10, 15, 20])
