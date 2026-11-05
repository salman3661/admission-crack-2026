import os
import sys
import pymupdf
from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()

files = [
    ("Weekly 04 Varsity", "Week_04/01_Varsity_Ka/Weekly 4 Varsity Udvash .pdf", [0, 1]),
    ("Medical W04 Sol", "Week_04/02_Medical_Unmesh/Medical_W04_Solution.pdf", [0, 1]),
    ("Engineering W04 Sol", "Week_04/03_Engineering_Extra/Engineering_W04_Solution.pdf", [0, 1]),
    ("Physics P1", "Week_04/01_Varsity_Ka/Physics-04 (Part-01).pdf", [0]),
    ("Physics P2", "Week_04/01_Varsity_Ka/Physics-04 (Part-02).pdf", [0]),
    ("Chemistry P1", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-01).pdf", [0]),
    ("Chemistry P2", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-02).pdf", [0]),
    ("Math P1", "Week_04/01_Varsity_Ka/Higher Math-04 (Part-01).pdf", [0, 1]),
    ("Math P2", "Week_04/01_Varsity_Ka/Higher Math-04 (Part-02).pdf", [0, 1]),
    ("Biology", "Week_04/01_Varsity_Ka/Biology-04 (Part-01+02).pdf", [0, 1, 2]),
]

with open("w4_syllabus_dump.txt", "w", encoding="utf-8") as out:
    for name, path, pages in files:
        if not os.path.exists(path):
            out.write(f"NOT FOUND: {path}\n")
            continue
        doc = pymupdf.open(path)
        out.write(f"\n==================== {name} ({len(doc)} pages) ====================\n")
        for pno in pages:
            if pno >= len(doc): continue
            page = doc[pno]
            t = page.get_text().strip()
            if t:
                out.write(f"--- Page {pno+1} [TEXT] ---\n{t}\n")
            else:
                pix = page.get_pixmap(dpi=110)
                res, _ = engine(pix.tobytes("png"))
                lines = [r[1] for r in res] if res else []
                out.write(f"--- Page {pno+1} [OCR] ---\n" + "\n".join(lines) + "\n")
        out.flush()
print("DONE DUMPING")
