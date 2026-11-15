# -*- coding: utf-8 -*-
import json

DUMMY_PHRASES = [
    "মান সর্বদা শূন্য বা ধ্রুবক থাকে",
    "প্রদত্ত শর্তের সাথে কোনো সম্পর্ক নেই",
    "কেবলমাত্র আদর্শ অবস্থায় বিপরীতমুখী হয়",
    "দীর্ঘায়িত প্রথাগত সমীকরণ সমাধান যেখানে ৩ মিনিটের অধিক সময় প্রয়োজন",
    "উভয় পক্ষ বর্গ না করে অপরিবর্তিত রাখা",
    "ভুল সমীকরণ অনুসিদ্ধান্ত",
    "অনুপাত ও একক বিবেচনা না করে সরাসরি মুখস্থ মানের প্রয়োগ",
    "সমীকরণের উভয় পাশে শূন্য দ্বারা ভাগ করা",
    "সবসময় প্রথম অপশনটিকে সঠিক ধরে",
    "চলকের মান সর্বদা ঋণাত্মক হবে",
    "মাত্রা সমীকরণ অপরিবর্তিত থাকে না",
    "অতিরিক্ত প্র্যাকটিস প্রশ্ন - মূল সমীকরণ কোনটি"
]

files = [
    "questions.json",
    "weekly_exams.json",
    "medical_bank.json",
    "varsity_bank.json",
    "src/data/quizzes.json"
]

for fn in files:
    data = json.load(open(fn))
    found = 0
    for q in data:
        # Check all strings in question
        for opt in q.get('options', q.get('opts', [])):
            for d in DUMMY_PHRASES:
                if d in str(opt):
                    found += 1
        for d in DUMMY_PHRASES:
            if d in str(q.get('question', '')) or d in str(q.get('explanation', '')):
                found += 1
    print(f"{fn}: {found} dummy phrases found")

