#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inject_du_frequency_weights.py

Tags Biology datasets with DU 100 Topics Frequency Weights:
1. chapter_synthetic_predictors.json
2. master_chapter_blueprint.json
3. questions.json, weekly_exams.json, quizzes.json
4. varsity_bank.json
5. medical_bank.json

Maintains strict data parity across root, src/data/, and admission_webapp/src/data/.
"""

import json
import os
import re
from typing import Dict, Any, Optional, Tuple

CHAPTER_HOTSPOT_METADATA = {
    "bio_zoo_01": {
        "has_hotspot": True,
        "tier": "super_hot",
        "topic": "৯টি পর্বের বৈশিষ্ট্য ও উদাহরণ",
        "freq": 32,
        "badge_text": "🔥 DU Super Hot (৩২ বার)",
        "sub_topics": [
            {"topic": "৯টি পর্বের বৈশিষ্ট্য", "freq": 19, "tier": "super_hot"},
            {"topic": "৯টি পর্বের উদাহরণ", "freq": 13, "tier": "super_hot"}
        ]
    },
    "bio_bot_09": {
        "has_hotspot": True,
        "tier": "super_hot",
        "topic": "C3 ও C4 উদ্ভিদের পার্থক্য",
        "freq": 17,
        "badge_text": "🔥 DU Super Hot (১৭ বার)"
    },
    "bio_zoo_08": {
        "has_hotspot": True,
        "tier": "super_hot",
        "topic": "এন্ডোক্রাইন গ্রন্থি ও করোটিক স্নায়ু",
        "freq": 26,
        "badge_text": "🔥 DU Super Hot (২৬ বার)",
        "sub_topics": [
            {"topic": "এন্ডোক্রাইন গ্রন্থি", "freq": 16, "tier": "super_hot"},
            {"topic": "করোটিক স্নায়ু", "freq": 10, "tier": "super_hot"}
        ]
    },
    "bio_bot_02": {
        "has_hotspot": True,
        "tier": "super_hot",
        "topic": "মায়োসিসের প্রোফেজ-১",
        "freq": 12,
        "badge_text": "🔥 DU Super Hot (১২ বার)"
    },
    "bio_bot_08": {
        "has_hotspot": True,
        "tier": "super_hot",
        "topic": "জাইলেম ও ফ্লোয়েম",
        "freq": 11,
        "badge_text": "🔥 DU Super Hot (১১ বার)"
    },
    "bio_zoo_02": {
        "has_hotspot": True,
        "tier": "hot",
        "topic": "হাইড্রার কোষসমূহ",
        "freq": 9,
        "badge_text": "⚡ DU Hot (৯ বার)"
    },
    "bio_zoo_04": {
        "has_hotspot": True,
        "tier": "hot",
        "topic": "হৃৎপিণ্ড ও রক্ত সংবহন",
        "freq": 9,
        "badge_text": "⚡ DU Hot (৯ বার)"
    },
    "bio_zoo_11": {
        "has_hotspot": True,
        "tier": "hot",
        "topic": "মেন্ডেলের সূত্রের ব্যতিক্রম",
        "freq": 9,
        "badge_text": "⚡ DU Hot (৯ বার)"
    },
    "bio_bot_01": {
        "has_hotspot": True,
        "tier": "hot",
        "topic": "মাইটোকন্ড্রিয়া ও নিউক্লিক অ্যাসিড",
        "freq": 8,
        "badge_text": "⚡ DU Hot (৮ বার)",
        "sub_topics": [
            {"topic": "মাইটোকন্ড্রিয়া", "freq": 8, "tier": "hot"},
            {"topic": "নিউক্লিক অ্যাসিড", "freq": 8, "tier": "hot"}
        ]
    }
}

QUESTION_RULES = {
    "bio_zoo_01": [
        ("৯টি পর্বের উদাহরণ", 13, "super_hot", "🔥 ঢাবি Super Hot: ৯টি পর্বের উদাহরণ (১৩ বার)",
         r"কনড্রিকথিস|অ্যাক্টিনোপটেরিজি|সারকোপটেরিজি|অ্যাম্ফিবিয়া|রেপটিলিয়া|সরীসৃপ|পক্ষীকুল|Aves|স্তন্যপায়ী|Mammalia|প্লেকয়েড|প্লাকয়েড|সাইক্লয়েড|টিনয়েড|গ্যানয়েড|নিউমেটিক|দ্বিপদ\s*নামকরণ|ICZN|আইসিজেডএন|কুমির|পাখি|হাঙর|অস্থিযুক্ত|তরুণাস্থিময়|শ্রেণি"),
        ("৯টি পর্বের বৈশিষ্ট্য", 19, "super_hot", "🔥 ঢাবি Super Hot: ৯টি পর্বের বৈশিষ্ট্য (১৯ বার)",
         r"পর্ব|সিলোম|সিউডোসিলোমেট|ছদ্ম-সিলোমেট|এসিলোমেট|ইউসিলোমেট|দ্বিপার্শ্বীয়\s*প্রতিসম|অরীয়|পরিফেরা|নিডারিয়া|প্লাটিহেলমিনথিস|নেমাটোডা|অ্যানিলিডা|আর্থ্রোপোডা|মলাস্কা|একাইনোডার্মাটা|কর্ডাটা|শিখা\s*কোষ|ফ্লেম\s*সেল|নেফ্রিডিয়া|মালপিজিয়ান|হিমোসিল|রেডুলা|টিউব\s*ফিট|পানি\s*সংবহন|নটোকর্ড|অস্টিয়া|অস্কুলাম|কোয়ানোসাইট|প্যারেনকাইমুলা|অ্যাম্বুলাক্রাল|চলন\s*অঙ্গ|রেচন\s*অঙ্গ")
    ],
    "bio_bot_09": [
        ("C3 ও C4 উদ্ভিদের পার্থক্য", 17, "super_hot", "🔥 ঢাবি Super Hot: C3 ও C4 উদ্ভিদের পার্থক্য (১৭ বার)",
         r"C3|C_3|C4|C_4|ক্যালভিন|হ্যাচ\s*ও\s*স্ল্যাক|হাচ\s*ও\s*স্ল্যাক|RuBP|রুবLoad|রুবিসকো|RuBisCO|ক্র্যাঞ্জ|Kranz|অক্সালোঅ্যাসিটিক|মেসোফিল|বান্ডল\s*সিথ|PEP|ফসফোএনল|আলোক\s*শ্বসন|ফটোরেস্পিরেশন|ম্যালিক\s*এসিড|ডাইকার্বক্সিলিক")
    ],
    "bio_zoo_08": [
        ("করোটিক স্নায়ু", 10, "super_hot", "🔥 ঢাবি Super Hot: করোটিক স্নায়ু (১০ বার)",
         r"করোটিক\s*স্নায়ু|কranial|ক্রেনিয়াল|অলফ্যাক্টরি|অপটিক|অকুলোমোটর|ট্রকলিয়ার|ট্রাইজেমিনাল|অ্যাবডুসেন্স|ফেসিয়াল|অডিটরি|ভেস্টিবুলো|গ্লসোফ্যারিঞ্জিয়াল|ভেগাস|স্পাইনাল\s*অ্যাক্সেসরি|হাইপোগ্লোসাল|সংবেদী\s*স্নায়ু|মোটর\s*স্নায়ু|মিশ্র\s*স্নায়ু"),
        ("এন্ডোক্রাইন গ্রন্থি", 16, "super_hot", "🔥 ঢাবি Super Hot: এন্ডোক্রাইন গ্রন্থি (১৬ বার)",
         r"এন্ডোক্রাইন|অন্তঃক্ষরা|গ্রন্থি|হরমোন|পিটুইটারি|থাইরয়েড|থাইরক্সিন|অ্যাড্রেনাল|এপিনেফ্রিন|প্যারাথরমোন|ল্যাঙ্গারহ্যান্স|ইনসুলিন|গ্লুকাগন|STH|TSH|ACTH|FSH|LH|প্রোল্যাকটিন|অক্সিটোসিন|ভ্যাসোপ্রেসিন|ADH|ক্যালসিটোনিন|আইলেটস|সোমাটোট্রপিন")
    ],
    "bio_bot_02": [
        ("মায়োসিসের প্রোফেজ-১", 12, "super_hot", "🔥 ঢাবি Super Hot: মায়োসিসের প্রোফেজ-১ (১২ বার)",
         r"প্রোফেজ-১|প্রোফেজ\s*১|লেপ্টোটিন|জাইগোটিন|প্যাকাইটিন|প্যাচাইটিন|ডিপ্লোটিন|ডায়াকাইনেসিস|মায়োসিস-১|মায়োসিস\s*১|কায়াজমা|ক্রসিং\s*ওভার|সাইন্যাপসিস|বাইভ্যালেন্ট|টেট্রাড|লুপ|টার্মিনালাইজেশন|প্রান্তীয়করণ|সমসংস্থ|হোমোলোগাস")
    ],
    "bio_bot_08": [
        ("জাইলেম ও ফ্লোয়েম", 11, "super_hot", "🔥 ঢাবি Super Hot: জাইলেম ও ফ্লোয়েম (১১ বার)",
         r"জাইলেম|ফ্লোয়েম|ট্রাকিয়া|ভেসেল|ট্রাকিড|সিভনল|সিভকোষ|সিভ\s*কোষ|সঙ্গীকোষ|সঙ্গী\s*কোষ|বাস্ট\s*ফাইবার|ভাস্কুলার\s*বান্ডল|সংযুক্ত|অরীয়|কেন্দ্রীক|সমপার্শ্বীয়|সমদ্বিপার্শ্বীয়|হ্যাড্রোসেন্ট্রিক|লেপ্টোসেন্ট্রিক|ক্যাম্বিয়াম|মুক্ত|বদ্ধ|পরিবহন\s*কলা")
    ],
    "bio_zoo_02": [
        ("হাইড্রার কোষসমূহ", 9, "hot", "⚡ ঢাবি Hot: হাইড্রার কোষসমূহ (৯ বার)",
         r"হাইড্রা|নিডোসাইট|নিডোব্লাস্ট|নেমাটোসিস্ট|স্টিনোটিল|পেনিট্রান্ট|ভলভেন্ট|গ্লুটিন্যান্ট|ইন্টারস্টিশিয়াল|পেশি-আবরণী|সংবেদী\s*কোষ|স্নায়ু\s*কোষ|গ্রন্থি\s*কোষ|জনন\s*কোষ|মেসোগ্লিয়া|হাইপোস্টোম|সিলেন্টেরন")
    ],
    "bio_zoo_04": [
        ("হৃৎপিণ্ড ও রক্ত সংবহন", 9, "hot", "⚡ ঢাবি Hot: হৃৎপিণ্ড ও রক্ত সংবহন (৯ বার)",
         r"হৃৎপিণ্ড|পেসমেকার|SAN|AVN|হিজের\s*বান্ডল|বান্ডল\s*অব\s*হিজ|পারকিনজি|কার্ডিয়াক|হৃদচক্র|সিস্টোল|ডায়াস্টোল|অলিন্দ|নিলয়|বাইকাসপিড|ট্রাইকাসপিড|সেমিলুনার|অর্ধচন্দ্রাকার|করোনারি|অ্যানজাইনা|হার্ট\s*অ্যাটাক|হার্ট\s*ফেইলিউর|বাইপাস|অ্যানজিওপ্লাস্টি|লাব|ডাব|ECG|ইসিজি|রক্ত\s*সংবহন|সিস্টেমিক|পালমোনারি|পোর্টাল|রক্ত\s*তঞ্চন|ক্লটিং|হেপারিন|ফাইব্রিনোজেন|প্রোথ্রম্বিন|Rh\s*ফ্যাক্টর|এরিথ্রোব্লাস্টোসিস|রক্তরস|প্লাজমা|রক্তকণিকা|RBC|WBC|অণুচক্রিকা|হৃদপেশি|মায়োসাইট")
    ],
    "bio_zoo_11": [
        ("মেন্ডেলের সূত্রের ব্যতিক্রম", 9, "hot", "⚡ ঢাবি Hot: মেন্ডেলের সূত্রের ব্যতিক্রম (৯ বার)",
         r"মেন্ডেল|ব্যতিক্রম|অসম্পূর্ণ\s*প্রকটতা|সমপ্রকটতা|লিথাল\s*জিন|মারন\s*জিন|পরিপূরক\s*জিন|এপিস্ট্যাসিস|প্রকট\s*এপিস্ট্যাসিস|দ্বৈত\s*প্রচ্ছন্ন|পলিজেনিক|১:২:১|২:১|৯:৭|১৩:৩|৯:৩:৪|১২:৩:১|ক্যুনো|সন্ধ্যামালতী|অ্যান্ডালুসিয়ান|বর্ণান্ধতা|হিমোফিলিয়া|সেক্স-লিংকড|ক্রিস-ক্রস")
    ],
    "bio_bot_01": [
        ("মাইটোকন্ড্রিয়া", 8, "hot", "⚡ ঢাবি Hot: মাইটোকন্ড্রিয়া (৮ বার)",
         r"মাইটোকন্ড্রি|ক্রিস্টি|অক্সিজোম|ATP\s*synthase|শ্বসন\s*অঙ্গাণু|পাওয়ার\s*হাউস"),
        ("নিউক্লিক অ্যাসিড", 8, "hot", "⚡ ঢাবি Hot: নিউক্লিক অ্যাসিড (৮ বার)",
         r"DNA|RNA|ডাবল\s*হেলিক্স|দ্বিসূত্রক|নিউক্লিওটাইড|নিউক্লিওসাইড|পিউরিন|পিরিমিডিন|অ্যাডেনিন|গুয়ানিন|সাইটোসিন|থাইমিন|ইউরাসিল|শারগাফ|Chargaff|ফসফোডাইএস্টার|রেপ্লিকেশন|অনুলিপন|ট্রান্সক্রিপশন|ট্রান্সলেশন|mRNA|tRNA|rRNA|জেনেটিক\s*কোড|কোডন|ওকাজাকি|স্টপ\s*কোডন|প্রারম্ভিক\s*কোডন")
    ]
}

def match_hotspot(cid: str, text: str) -> Optional[Tuple[str, int, str, str]]:
    """Returns (topic, freq, tier, badge) if matched, else None."""
    if cid not in QUESTION_RULES:
        return None
    for topic, freq, tier, badge, pat in QUESTION_RULES[cid]:
        if re.search(pat, text, re.IGNORECASE):
            return topic, freq, tier, badge
    # Special fallback for bio_zoo_01 (its entire chapter is 9 phyla characteristics)
    if cid == "bio_zoo_01":
        return "৯টি পর্বের বৈশিষ্ট্য", 19, "super_hot", "🔥 ঢাবি Super Hot: ৯টি পর্বের বৈশিষ্ট্য (১৯ বার)"
    return None

def tag_question_object(q: Dict[str, Any], cid: str):
    """Tags question object in place if it matches a hotspot."""
    # Build search text from all descriptive fields
    text_parts = [
        str(q.get("stem", "")),
        str(q.get("q", "")),
        str(q.get("question", "")),
        str(q.get("explanation", "")),
        str(q.get("exp", "")),
        str(q.get("trap_alert", "")),
        str(q.get("speed_hack", "")),
        str(q.get("trap", "")),
        str(q.get("type_ref", "")),
        " ".join(str(o) for o in q.get("options", q.get("opts", [])))
    ]
    full_text = " ".join(text_parts)
    res = match_hotspot(cid, full_text)
    if res:
        topic, freq, tier, badge = res
        q["du_topic"] = topic
        q["du_freq"] = freq
        q["du_tier"] = tier
        q["du_badge"] = badge
    else:
        # If not matching, remove any stale du_* keys if present
        for k in ["du_topic", "du_freq", "du_tier", "du_badge"]:
            q.pop(k, None)

def update_chapter_synthetic_predictors():
    print("Updating chapter_synthetic_predictors.json...")
    src_path = "src/data/chapter_synthetic_predictors.json"
    with open(src_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    tagged_count = 0
    total_in_target = 0

    for ch in data.get("chapters", []):
        cid = ch.get("chapter_id")
        if cid in CHAPTER_HOTSPOT_METADATA:
            ch["du_hotspot"] = CHAPTER_HOTSPOT_METADATA[cid]
            for p in ch.get("predictors", []):
                total_in_target += 1
                tag_question_object(p, cid)
                if "du_topic" in p:
                    tagged_count += 1
        else:
            ch.pop("du_hotspot", None)

    print(f"  -> Tagged {tagged_count}/{total_in_target} predictors in {len(CHAPTER_HOTSPOT_METADATA)} hotspot chapters.")

    # Write to both locations
    targets = [
        "src/data/chapter_synthetic_predictors.json",
        "admission_webapp/src/data/chapter_synthetic_predictors.json"
    ]
    for target in targets:
        with open(target, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  Saved: {target}")

def update_master_chapter_blueprint():
    print("Updating master_chapter_blueprint.json...")
    src_path = "src/data/master_chapter_blueprint.json"
    with open(src_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    hotspot_chapters_tagged = 0
    for ch in data.get("chapters", []):
        cid = ch.get("id")
        if cid in CHAPTER_HOTSPOT_METADATA:
            ch["du_hotspot"] = CHAPTER_HOTSPOT_METADATA[cid]
            hotspot_chapters_tagged += 1
        else:
            ch.pop("du_hotspot", None)

    print(f"  -> Injected du_hotspot into {hotspot_chapters_tagged} chapters.")

    targets = [
        "src/data/master_chapter_blueprint.json",
        "admission_webapp/src/data/master_chapter_blueprint.json"
    ]
    for target in targets:
        with open(target, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  Saved: {target}")

def update_question_bank(base_name: str, targets: list):
    print(f"Updating {base_name}...")
    src_path = targets[0]
    with open(src_path, "r", encoding="utf-8") as f:
        qs = json.load(f)

    bio_count = 0
    tagged_count = 0

    for q in qs:
        if q.get("subject") == "Biology":
            bio_count += 1
            cid = q.get("blueprint_chapter_id") or q.get("chapter")
            if cid in CHAPTER_HOTSPOT_METADATA:
                tag_question_object(q, cid)
                if "du_topic" in q:
                    tagged_count += 1
            else:
                for k in ["du_topic", "du_freq", "du_tier", "du_badge"]:
                    q.pop(k, None)

    print(f"  -> In {base_name}: {tagged_count} out of {bio_count} Biology questions tagged with DU hotspot weights.")

    for target in targets:
        with open(target, "w", encoding="utf-8") as f:
            json.dump(qs, f, ensure_ascii=False, indent=2)
        print(f"  Saved: {target}")

def main():
    print("=" * 60)
    print("INJECTING DU 100 TOPICS FREQUENCY WEIGHTS ACROSS BIOLOGY DATASETS")
    print("=" * 60)

    # 1. Synthetic Predictors
    update_chapter_synthetic_predictors()

    # 2. Master Chapter Blueprint
    update_master_chapter_blueprint()

    # 3. Questions / Weekly Exams / Quizzes (Mirrors)
    update_question_bank("questions.json", [
        "questions.json",
        "src/data/questions.json",
        "admission_webapp/src/data/questions.json"
    ])

    update_question_bank("weekly_exams.json", [
        "weekly_exams.json",
        "src/data/weekly_exams.json",
        "admission_webapp/src/data/weekly_exams.json"
    ])

    update_question_bank("quizzes.json", [
        "src/data/quizzes.json",
        "admission_webapp/src/data/quizzes.json"
    ])

    # 4. Varsity Bank
    update_question_bank("varsity_bank.json", [
        "varsity_bank.json",
        "src/data/varsity_bank.json",
        "admission_webapp/src/data/varsity_bank.json"
    ])

    # 5. Medical Bank
    update_question_bank("medical_bank.json", [
        "medical_bank.json",
        "src/data/medical_bank.json",
        "admission_webapp/src/data/medical_bank.json"
    ])

    print("=" * 60)
    print("ALL DATASETS SUCCESSFULLY UPDATED WITH DU 100 TOPICS WEIGHTS!")
    print("=" * 60)

if __name__ == "__main__":
    main()
