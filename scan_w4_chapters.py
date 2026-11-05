import os
import sys
import pymupdf
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
engine = RapidOCR()

def scan_file(path, label, pages_to_check):
    print(f"\n*** SCANNING {label} ({path}) ***")
    doc = pymupdf.open(path)
    for p in pages_to_check:
        if p >= len(doc): continue
        t = doc[p].get_text().strip()
        if len(t) > 30:
            print(f"Page {p+1} (Text): {t[:300].replace(chr(10), ' ')}")
        else:
            pix = doc[p].get_pixmap(dpi=100)
            res, _ = engine(pix.tobytes("png"))
            if res:
                lines = [r[1] for r in res]
                print(f"Page {p+1} (OCR): {' // '.join(lines[:10])}")

# Let's inspect:
scan_file("Week_04/01_Varsity_Ka/Physics-04 (Part-01).pdf", "Physics P1", [0, 1, 2, 3])
scan_file("Week_04/01_Varsity_Ka/Physics-04 (Part-02).pdf", "Physics P2", [0, 1, 2, 3])
scan_file("Week_04/01_Varsity_Ka/Chemistry-04 (Part-01).pdf", "Chemistry P1", [0, 1, 2, 3])
scan_file("Week_04/01_Varsity_Ka/Chemistry-04 (Part-02).pdf", "Chemistry P2", [0, 1, 2, 3])
scan_file("Week_04/01_Varsity_Ka/Higher Math-04 (Part-01).pdf", "Math P1", [0, 1, 2, 3])
scan_file("Week_04/01_Varsity_Ka/Higher Math-04 (Part-02).pdf", "Math P2", [0, 1, 2, 3])
scan_file("Week_04/01_Varsity_Ka/Biology-04 (Part-01+02).pdf", "Biology", [0, 1, 2, 3])
scan_file("Week_04/01_Varsity_Ka/Weekly 4 Varsity Udvash .pdf", "Weekly Exam", [0, 1, 2])
