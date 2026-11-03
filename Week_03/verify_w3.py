# -*- coding: utf-8 -*-
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

dir_path = r'E:\Admission Crack 2026\Week_03\05_Final_Notes'
files = [
    'Physics_Master_Digest.md',
    'Chemistry_Master_Digest.md',
    'H_Math_Master_Digest.md',
    'Biology_Master_Digest.md'
]

results = []

for f in files:
    full_path = os.path.join(dir_path, f)
    if not os.path.exists(full_path):
        results.append({'file': f, 'error': 'File not found'})
        continue
    
    with open(full_path, 'r', encoding='utf-8') as fh:
        txt = fh.read()
    
    lines = txt.splitlines()
    size = len(txt.encode('utf-8'))
    
    # Check control characters
    bad_chars = re.findall(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', txt)
    
    # Patterns
    patterns = re.findall(r'\[[PCMB]\d+\]', txt)
    if not patterns:
        patterns = re.findall(r'Pattern \d+|প্যাটার্ন \d+', txt)
    
    # Predictive Qs
    predictive = re.findall(r'### Q\d+', txt)
    if not predictive:
        predictive = re.findall(r'#### \*\*Q\d+', txt)
    
    # Flashcards
    flashcards = re.findall(r'FC-\d+', txt)
    
    # Written problems
    written = re.findall(r'Written \d+|Written Problem \d+', txt)
    
    # MCQs
    s8_idx = txt.find('৮.২') if '৮.২' in txt else txt.find('8.2')
    s8_end = txt.find('উত্তরমালা') if 'উত্তরমালা' in txt else len(txt)
    s8_txt = txt[s8_idx:s8_end] if s8_idx != -1 else ''
    mcqs = re.findall(r'\*\*[\d১-৯]+\.\*\*', s8_txt)
    
    results.append({
        'file': f,
        'size_bytes': size,
        'lines': len(lines),
        'bad_chars': len(bad_chars),
        'patterns': len(patterns),
        'predictive_q': len(predictive),
        'flashcards': len(flashcards),
        'written_q': len(written),
        'mcqs': len(mcqs)
    })

print("| Subject File | Size (Bytes) | Lines | Core Patterns | Predictive Qs | Flashcards | Written Qs | Self-Test MCQs | Control Chars |")
print("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
for r in results:
    fn = r['file']
    sz = f"{r['size_bytes']:,}"
    ln = f"{r['lines']:,}"
    pat = r['patterns']
    pq = r['predictive_q']
    fc = r['flashcards']
    wq = r['written_q']
    mcq = r['mcqs']
    bc = r['bad_chars']
    print(f"| [{fn}](file:///e:/Admission%20Crack%202026/Week_03/05_Final_Notes/{fn}) | {sz} | {ln} | {pat} | {pq} | {fc} | {wq} | {mcq} | {bc} |")

