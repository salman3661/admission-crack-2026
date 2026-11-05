import os, sys, pymupdf
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
engine = RapidOCR()

doc = pymupdf.open("Week_05/03_Engineering_Extra/Engineering_W05_Solution.pdf")
print("Total pages in Eng Sol:", len(doc))
for p in [1, 5, 10, 15, 20, 25]:
    if p < len(doc):
        pix = doc[p].get_pixmap(dpi=120)
        res, _ = engine(pix.tobytes("png"))
        lines = [r[1] for r in res] if res else []
        print(f"Page {p+1}: " + " | ".join(lines[:10]), flush=True)
