import sys, pymupdf
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
engine = RapidOCR()

def check_pages(name, path, pages):
    doc = pymupdf.open(path)
    print(f"\n==================== {name} ====================")
    for p in pages:
        if p >= len(doc): continue
        pix = doc[p].get_pixmap(dpi=75)
        res, _ = engine(pix.tobytes('png'))
        lines = [r[1] for r in res] if res else []
        print(f"P{p+1}: " + " // ".join(lines[:12]))

check_pages("Phy P1", "Week_04/01_Varsity_Ka/Physics-04 (Part-01).pdf", [1, 2, 3, 5])
check_pages("Chem P1", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-01).pdf", [1, 2, 4])
check_pages("Chem P2", "Week_04/01_Varsity_Ka/Chemistry-04 (Part-02).pdf", [1, 2, 4])
check_pages("Bio", "Week_04/01_Varsity_Ka/Biology-04 (Part-01+02).pdf", [1, 2, 4, 8])
