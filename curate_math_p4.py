#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_math_p4.py
Aggregates Higher Mathematics 2nd Paper Part 2:
- Chapters math_2nd_06 & math_2nd_07 from curate_math_p4a
- Chapters math_2nd_08, math_2nd_09, math_2nd_10 from curate_math_p4b
"""

from curate_math_p4a import get_math_2nd_06, get_math_2nd_07
from curate_math_p4b import get_math_2nd_08, get_math_2nd_09, get_math_2nd_10

def get_part4_chapters():
    return [
        get_math_2nd_06(),
        get_math_2nd_07(),
        get_math_2nd_08(),
        get_math_2nd_09(),
        get_math_2nd_10()
    ]

if __name__ == "__main__":
    chaps = get_part4_chapters()
    total = sum(len(c["predictors"]) for c in chaps)
    print(f"Successfully loaded {len(chaps)} chapters with {total} MCQs.")
    for c in chaps:
        print(f"  {c['chapter_id']} ({c['chapter_title']}): {len(c['predictors'])} MCQs")
