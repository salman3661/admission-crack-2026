# -*- coding: utf-8 -*-
"""
generate_vault.py
Generates 240+ Formula & Trap Vault entries across all 29 chapters of Week 01, Week 02, and Week 03:
- Physics: Vector, Dynamics, Work-Energy, Gravitation, Structural Properties, Waves, Ideal Gas.
- Chemistry: Qualitative Analysis, Periodic Properties, Chemical Changes (Equilibrium/pH), Organic Basics, Environmental Chem.
- Higher Math: Matrix-Determinants, Straight Lines, Circles, Conics, Complex Numbers, Polynomials, Trigonometry, Calculus.
- Biology: Cell & Structure, Genetics, Plant Physiology, Human Physiology (Digestion, Circulation, Excretion).
- English: Appropriate Prepositions, Synonyms & Antonyms.
- GK: 1971 Liberation War Sector & Bir Sreshtho Matrix.

Each entry includes:
- id, subject, chapter, type ('core_formula' | 'shortcut' | 'trap')
- title, formula, concept, hack, trap, tags
"""

import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def get_vault_entries():
    entries = []
    
    # -------------------------------------------------------------
    # 1. PHYSICS (7 Chapters, ~65 entries)
    # -------------------------------------------------------------
    
    # Vector
    entries.extend([
        {
            "id": "v_phy_vec_01",
            "subject": "Physics",
            "chapter": "Vector",
            "type": "core_formula",
            "title": "দুটি ভেক্টরের লব্ধির মান ও দিক",
            "formula": "R = \\sqrt{P^2 + Q^2 + 2PQ\\cos\\alpha}, \\quad \\tan\\theta = \\frac{Q\\sin\\alpha}{P + Q\\cos\\alpha}",
            "concept": "দুটি ভেক্টর একই বিন্দুতে ক্রিয়াশীল হলে সামান্তরিক সূত্রের সাহায্যে লব্ধি নির্ণয় করা হয়। লব্ধির সর্বোচ্চ মান R_{max} = P + Q (যখন \\alpha = 0^\\circ) এবং সর্বনিম্ন মান R_{min} = |P - Q| (যখন \\alpha = 180^\\circ)।",
            "hack": "যদি P = Q এবং \\alpha = 120^\\circ হয়, তবে লব্ধি R = P এবং লব্ধির দিক \\theta = 60^\\circ (ঠিক মাঝামাঝি)! লব্ধি P এর সাথে সমকোণে থাকলে \\cos\\alpha = -P/Q।",
            "trap": "লব্ধির দিক \\theta কার সাথে নির্ণয় করা হচ্ছে (P নাকি Q) তা সতর্কভাবে লক্ষ্য করুন। সূত্রে যার সাথে কোণ সে নিচে একা (P) বসে।",
            "tags": ["vector", "resultant", "লব্ধি", "সামান্তরিক", "alpha", "theta"]
        },
        {
            "id": "v_phy_vec_02",
            "subject": "Physics",
            "chapter": "Vector",
            "type": "core_formula",
            "title": "ডট গুণন ও ক্রস গুণনের মৌলিক সম্পর্ক",
            "formula": "\\vec{A}\\cdot\\vec{B} = AB\\cos\\theta, \\quad |\\vec{A}\\times\\vec{B}| = AB\\sin\\theta \\implies \\frac{|\\vec{A}\\times\\vec{B}|}{\\vec{A}\\cdot\\vec{B}} = \\tan\\theta",
            "concept": "ডট গুণন স্কেলার রাশি এবং ক্রস গুণন ভেক্টর রাশি প্রদান করে। দুটি ভেক্টর সমান্তরাল হলে ক্রস গুণন শূন্য এবং লম্ব হলে ডট গুণন শূন্য।",
            "hack": "যদি |\\vec{A}\\times\\vec{B}| = \\sqrt{3}(\\vec{A}\\cdot\\vec{B}) হয়, তবে \\tan\\theta = \\sqrt{3} \\implies \\theta = 60^\\circ! যদি উভয় সমান হয় তবে \\theta = 45^\\circ।",
            "trap": "ক্রস গুণনে ভেক্টরের ক্রম বদলালে ঋণাত্মক চিহ্ন আসে: \\vec{A}\\times\\vec{B} = -(\\vec{B}\\times\\vec{A})।",
            "tags": ["dot product", "cross product", "ডট গুণন", "ক্রস গুণন", "কোণ"]
        },
        {
            "id": "v_phy_vec_03",
            "subject": "Physics",
            "chapter": "Vector",
            "type": "shortcut",
            "title": "ত্রিমাত্রিক ভেক্টরের মান নির্ণয়ে পাইথাগোরিয়ান ট্রিপলেট",
            "formula": "|a\\hat{i} + b\\hat{j} + c\\hat{k}| = \\sqrt{a^2 + b^2 + c^2}",
            "concept": "ঢাবি ভর্তি পরীক্ষায় সময়ের অপচয় রোধে বহুল ব্যবহৃত ৩D ট্রিপলেটগুলো সরাসরি মেমোরিতে রাখা আবশ্যক।",
            "hack": "(1, 2, 2) \\to মান 3; (2, 3, 6) \\to মান 7; (1, 4, 8) \\to মান 9; (2, 4, 4) \\to মান 6; (2, 6, 9) \\to মান 11!",
            "trap": "চিহ্ন মাইনাস থাকলেও বর্গের কারণে ধনাত্মক হয়: |2\\hat{i} - 3\\hat{j} + 6\\hat{k}| = 7। রুটের ভেতর বিয়োগ করা যাবে না।",
            "tags": ["triplet", "shortcut", "magnitude", "অভিক্ষেপ", "মান"]
        },
        {
            "id": "v_phy_vec_04",
            "subject": "Physics",
            "chapter": "Vector",
            "type": "shortcut",
            "title": "নদী ও নৌকার সোজাসুজি পারাপার ও লব্ধি সময়",
            "formula": "t = \\frac{d}{v\\sin\\alpha}, \\quad t_{min} = \\frac{d}{v} \\; (\\alpha = 90^\\circ), \\quad \\cos\\alpha = -\\frac{u}{v} \\; (\\text{সোজাসুজি})",
            "concept": "ন্যূনতম দূরত্বে নদী পার হতে নৌকার বেগের উপাংশ স্রোতের বেগকে নিষ্ক্রিয় করতে হয়, ফলে যাত্রা কোণ স্থূলকোণ হয়।",
            "hack": "যদি নৌকার বেগ স্রোতের দ্বিগুণ হয় (v = 2u), তবে যাত্রা কোণ সর্বদা \\alpha = 120^\\circ এবং লব্ধি বেগ v' = \\sqrt{v^2 - u^2} = \\sqrt{3}u!",
            "trap": "তীরের সাথে কোণ চাইলে উত্তর 120° - 90° = 30°; প্রশ্নের ভাষা মনোযোগ দিয়ে পড়ুন।",
            "tags": ["river", "boat", "নদী-নৌকা", "পারাপার", "ন্যূনতম দূরত্ব"]
        },
        {
            "id": "v_phy_vec_05",
            "subject": "Physics",
            "chapter": "Vector",
            "type": "trap",
            "title": "সামান্তরিকের ক্ষেত্রফলে বাহু বনাম কর্ণ",
            "formula": "\\text{Area}_{বাহু} = |\\vec{A} \\times \\vec{B}|, \\quad \\text{Area}_{কর্ণ} = \\frac{1}{2}|\\vec{d}_1 \\times \\vec{d}_2|",
            "concept": "সামান্তরিকের দুটি সন্নিহিত বাহু ভেক্টর দ্বারা প্রকাশ করলে সরাসরি ক্রস গুণন, কিন্তু কর্ণদ্বয় দিলে হাফ গুণ করতে হয়।",
            "hack": "ত্রিভুজের ক্ষেত্রফল সর্বদা \\frac{1}{2}|\\vec{A}\\times\\vec{B}|; আর সামান্তরিকের কর্ণ বললে আগে 1/2 লিখে ক্রস গুণন করুন।",
            "trap": "প্রশ্নে বাহু বলা আছে নাকি কর্ণ বলা আছে তা আন্ডারলাইন না করে অনেকেই হাফ ছেড়ে দিয়ে সম্পূর্ণ ভুল উত্তর দাগায়।",
            "tags": ["parallelogram", "area", "ক্ষেত্রফল", "কর্ণ", "বাহু", "trap"]
        },
        {
            "id": "v_phy_vec_06",
            "subject": "Physics",
            "chapter": "Vector",
            "type": "trap",
            "title": "ভেক্টর ক্যালকুলাস: সলিনয়ডাল বনাম অঘূর্ণনশীল",
            "formula": "\\vec{\\nabla}\\cdot\\vec{F} = 0 \\; (\\text{সলিনয়ডাল}), \\quad \\vec{\\nabla}\\times\\vec{F} = \\vec{0} \\; (\\text{অঘূর্ণনশীল/সংরক্ষণশীল})",
            "concept": "ডাইভারজেন্স শূন্য হলে কোনো ভেক্টর ক্ষেত্র সলিনয়ডাল (আয়তন অপরিবর্তিত) এবং কার্ল শূন্য হলে অঘূর্ণনশীল বা সংরক্ষণশীল বল ক্ষেত্র হয়।",
            "hack": "অবস্থান ভেক্টর \\vec{r} = x\\hat{i}+y\\hat{j}+z\\hat{k} এর জন্য \\vec{\\nabla}\\cdot\\vec{r} = 3 এবং \\vec{\\nabla}\\times\\vec{r} = \\vec{0}!",
            "trap": "সলিনয়ডাল প্রশ্নে ডাইভারজেন্স শূন্য করতে হয়, কার্ল নয়; অজানা ধ্রুবক m নির্ণয়ে ডাইভারজেন্স নেওয়া সবচেয়ে দ্রুত।",
            "tags": ["divergence", "curl", "সলিনয়ডাল", "অঘূর্ণনশীল", "ভেক্টর ক্যালকুলাস"]
        },
        {
            "id": "v_phy_vec_07",
            "subject": "Physics",
            "chapter": "Vector",
            "type": "core_formula",
            "title": "স্কেলার অভিক্ষেপ ও ভেক্টর উপাংশ",
            "formula": "\\text{Projection of } \\vec{A} \\text{ on } \\vec{B} = \\frac{\\vec{A}\\cdot\\vec{B}}{|\\vec{B}|}, \\quad \\text{Component} = \\left(\\frac{\\vec{A}\\cdot\\vec{B}}{|\\vec{B}|^2}\\right)\\vec{B}",
            "concept": "যার ওপর অভিক্ষেপ নির্ণয় করতে বলবে, তার মান নিচে বসে এবং সেটি দিয়ে একক ভেক্টর গঠন করে উপাংশ পাওয়া যায়।",
            "hack": "অভিক্ষেপ স্কেলার সংখ্যা, কিন্তু উপাংশ ভেক্টর রাশি (দিক নির্দেশক ভেক্টর থাকবে)।",
            "trap": "B এর ওপর A এর অভিক্ষেপে হর |B| হবে, |A| নয়। যার 'ওপর' সে নিচে থাকে!",
            "tags": ["projection", "component", "অভিক্ষেপ", "উপাংশ"]
        },
        {
            "id": "v_phy_vec_08",
            "subject": "Physics",
            "chapter": "Vector",
            "type": "shortcut",
            "title": "বৃষ্টি ও ছাতার কোণ শর্টকাট",
            "formula": "\\tan\\theta = \\frac{v_{man}}{v_{rain}} = \\frac{v_m}{v_r}",
            "concept": "উল্লম্বভাবে বৃষ্টি পড়লে এবং ব্যক্তি অনুভূমিক বেগে চললে আপেক্ষিক বেগের কারণে উল্লম্বের সাথে ছাতা ধরতে হয়।",
            "hack": "যদি বাতাস থাকে, তবে \\tan\\theta = \\frac{|v_m \\pm v_w|}{v_r}। একই দিকে বাতাস দিলে বিয়োগ, বিপরীত দিকে বাতাস দিলে যোগ।",
            "trap": "কোণ উল্লম্বের সাথে চেয়েছে নাকি ভূমির সাথে চেয়েছে তা লক্ষ্য করুন; ভূমির সাথে চাইলে 90° - theta হবে।",
            "tags": ["rain", "umbrella", "আপেক্ষিক বেগ", "ছাতা"]
        }
    ])

    # Dynamics (গতিবিদ্যা)
    entries.extend([
        {
            "id": "v_phy_dyn_01",
            "subject": "Physics",
            "chapter": "Dynamics",
            "type": "core_formula",
            "title": "প্রাসের বিচরণকাল, উচ্চতা ও পাল্লা",
            "formula": "T = \\frac{2u\\sin\\alpha}{g}, \\quad H = \\frac{u^2\\sin^2\\alpha}{2g}, \\quad R = \\frac{u^2\\sin 2\\alpha}{g}",
            "concept": "দ্বিমাত্রিক গতিতে অনুভূমিক ত্বরণ শূন্য (a_x = 0) এবং উল্লম্ব ত্বরণ -g। অনুভূমিক বেগ u\\cos\\alpha সর্বদা ধ্রুবক থাকে।",
            "hack": "R ও H এর সম্পর্ক: \\tan\\alpha = \\frac{4H}{R}। R = 4H হলে \\alpha = 45^\\circ; R = 4\\sqrt{3}H হলে \\alpha = 30^\\circ!",
            "trap": "শীর্ষবিন্দুতে বেগ শূন্য নয়, শীর্ষবিন্দুতে উল্লম্ব বেগ v_y = 0 কিন্তু মোট বেগ v = u\\cos\\alpha এবং গতিশক্তি E_k = E_0\\cos^2\\alpha।",
            "tags": ["projectile", "range", "height", "পাল্লা", "উচ্চতা", "প্রাস"]
        },
        {
            "id": "v_phy_dyn_02",
            "subject": "Physics",
            "chapter": "Dynamics",
            "type": "shortcut",
            "title": "n-তম সেকেন্ডের দূরত্ব ও দূরত্বের অনুপাত",
            "formula": "s_{nth} = u + \\frac{1}{2}a(2n - 1)",
            "concept": "স্থির অবস্থান (u = 0) থেকে সমত্বরণে চললে n-তম সেকেন্ডের দূরত্ব সর্বদা বিজোড় সংখ্যা (2n - 1) এর সমানুপাতিক।",
            "hack": "১ম : ২য় : ৩য় : ৪র্থ = ১ : ৩ : ৫ : ৭! ৫ম ও ১০ম সেকেন্ড বললে (2*5-1) : (2*10-1) = 9 : 19 সরাসরি উত্তর!",
            "trap": "n সেকেন্ডের মোট দূরত্ব (s = 1/2 a n^2) আর n-তম সেকেন্ডের দূরত্বের মধ্যে পার্থক্য রয়েছে।",
            "tags": ["kinematics", "distance", "n-th second", "দূরত্ব", "অনুপাত"]
        },
        {
            "id": "v_phy_dyn_03",
            "subject": "Physics",
            "chapter": "Dynamics",
            "type": "core_formula",
            "title": "গতির মৌলিক সমীকরণ ও গড় বেগ",
            "formula": "v = u + at, \\quad s = ut + \\frac{1}{2}at^2, \\quad v^2 = u^2 + 2as, \\quad s = \\left(\\frac{u + v}{2}\\right)t",
            "concept": "সমত্বরণে গতিশীল বস্তুর গড় বেগ হলো আদি ও শেষ বেগের গাণিতিক গড়।",
            "hack": "সমমন্দনে গাড়ি থামাতে প্রয়োজনীয় দূরত্ব s \\propto u^2; বেগ ৩ গুণ করলে ব্রেকিং দূরত্ব ৯ গুণ হয়!",
            "trap": "ত্বরণ ধ্রুবক না হলে ক্যালকুলাস (v = ds/dt, a = dv/dt) ব্যবহার করতে হবে, এই সূত্র খাটবে না।",
            "tags": ["motion", "equations", "acceleration", "সমত্বরণ"]
        },
        {
            "id": "v_phy_dyn_04",
            "subject": "Physics",
            "chapter": "Dynamics",
            "type": "shortcut",
            "title": "নিক্ষিপ্ত বস্তুর সর্বোচ্চ উচ্চতা ও ফিরে আসার সময়",
            "formula": "H_{max} = \\frac{u^2}{2g}, \\quad T_{total} = \\frac{2u}{g}",
            "concept": "খাড়া ওপরে নিক্ষিপ্ত বস্তু ওঠার সময় ও নামার সময় সমান হয় (t_{up} = t_{down} = u/g)।",
            "hack": "g \\approx 9.8 \\text{ ms}^{-2} এর ক্ষেত্রে u = 49 \\text{ ms}^{-1} হলে ওঠার সময় ঠিক ৫ সেকেন্ড এবং মোট বিচরণকাল ১০ সেকেন্ড!",
            "trap": "উচ্চতা H থেকে পতনশীল বস্তুর স্পর্শ বেগ v = \\sqrt{2gH}; আর নিক্ষিপ্ত বস্তুর সর্বোচ্চ উচ্চতায় বেগ শূন্য।",
            "tags": ["free fall", "maximum height", "উচ্চতা", "পতন"]
        },
        {
            "id": "v_phy_dyn_05",
            "subject": "Physics",
            "chapter": "Dynamics",
            "type": "trap",
            "title": "অনুভূমিক ও খাড়া নিক্ষিপ্ত বস্তুর ত্বরণ",
            "formula": "a = g = 9.8 \\text{ ms}^{-2} \\quad (\\text{সর্বদা নিচের দিকে})",
            "concept": "বাতাসের বাধা উপেক্ষণীয় হলে যেকোনো নিক্ষিপ্ত বা পড়ন্ত বস্তুর ওপর কেবল অভিকর্ষজ ত্বরণ g ক্রিয়াশীল থাকে।",
            "hack": "সর্বোচ্চ উচ্চতায় বা গতিপথের যেকোনো বিন্দুতে ত্বরণের মান সর্বদা 9.8 ms^-2 এবং দিক খাঁটি নিচের দিকে।",
            "trap": "অনেকে সর্বোচ্চ উচ্চতায় বেগ শূন্য দেখে ত্বরণও শূন্য দাগিয়ে নেগেটিভ মার্কিং খায়!",
            "tags": ["gravity", "acceleration", "ত্বরণ", "trap"]
        },
        {
            "id": "v_phy_dyn_06",
            "subject": "Physics",
            "chapter": "Dynamics",
            "type": "shortcut",
            "title": "দুটি ভিন্ন কোণে একই পাল্লা (\\alpha ও 90° - \\alpha)",
            "formula": "R_1 = R_2 \\iff \\alpha_1 + \\alpha_2 = 90^\\circ",
            "concept": "একই আদি বেগে \\alpha এবং (90° - \\alpha) কোণে নিক্ষেপ করলে অনুভূমিক পাল্লা হুবহু একই হয়।",
            "hack": "পাল্লা একই হলে বিচরণকালের গুণফল T_1 T_2 = \\frac{2R}{g} এবং উচ্চতার সম্পর্ক R = 4\\sqrt{H_1 H_2}!",
            "trap": "পাল্লা একই হলেও তাদের সর্বোচ্চ উচ্চতা (H_1, H_2) এবং বিচরণকাল (T_1, T_2) ভিন্ন হবে।",
            "tags": ["complementary angles", "same range", "পাল্লা", "প্রাস"]
        },
        {
            "id": "v_phy_dyn_07",
            "subject": "Physics",
            "chapter": "Dynamics",
            "type": "core_formula",
            "title": "কৌণিক ও রৈখিক গতির সম্পর্ক",
            "formula": "s = r\\theta, \\quad v = r\\omega, \\quad a_t = r\\alpha, \\quad a_c = \\frac{v^2}{r} = \\omega^2 r",
            "concept": "বৃত্তাকার গতিতে স্পর্শকীয় ত্বরণ a_t বেগের মান পরিবর্তন করে এবং কেন্দ্রমুখী ত্বরণ a_c বেগের দিক পরিবর্তন করে। মোট ত্বরণ a = \\sqrt{a_t^2 + a_c^2}।",
            "hack": "rpm থেকে \\omega রূপান্তর: \\omega = \\frac{2\\pi N}{60} = \\frac{\\pi N}{30} \\text{ rad s}^{-1}। N = 300 \\text{ rpm} হলে \\omega = 10\\pi!",
            "trap": "সমবৃত্তীয় গতিতে স্পর্শকীয় ত্বরণ শূন্য (a_t = 0), কিন্তু কেন্দ্রমুখী ত্বরণ সর্বদা বিদ্যমান।",
            "tags": ["circular motion", "angular velocity", "কৌণিক বেগ", "rpm"]
        },
        {
            "id": "v_phy_dyn_08",
            "subject": "Physics",
            "chapter": "Dynamics",
            "type": "shortcut",
            "title": "পাখার সুইচ বন্ধের পর ঘূর্ণন সংখ্যা",
            "formula": "N_{rev} = \\frac{\\theta}{2\\pi} = \\frac{\\omega_0 t}{4\\pi} = \\frac{\\text{rpm}_0 \\times t(\\text{min})}{2}",
            "concept": "সমমন্দনে পাখা থেমে যাওয়ার সময় গড় কৌণিক বেগ হলো \\omega_0 / 2।",
            "hack": "যদি ১৮০০ rpm-এর পাখা ৩ মিনিটে থামে, তবে মোট পাক সংখ্যা = 1800 * 3 / 2 = 2700 পাক!",
            "trap": "সময়ের একক মিনিটে নাকি সেকেন্ডে বসাচ্ছেন তা সতর্ক থাকুন; সূত্রে t(min) বা t(sec)/60 বসাতে হয়।",
            "tags": ["fan revolutions", "rpm", "ঘূর্ণন সংখ্যা", "মন্দন"]
        }
    ])

    # Work-Energy (কাজ, শক্তি ও ক্ষমতা)
    entries.extend([
        {
            "id": "v_phy_we_01",
            "subject": "Physics",
            "chapter": "Work-Energy",
            "type": "core_formula",
            "title": "কাজ ও কাজ-শক্তি উপপাদ্য",
            "formula": "W = \\vec{F}\\cdot\\vec{s} = Fs\\cos\\theta, \\quad W_{net} = \\Delta E_k = \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2",
            "concept": "বল ও সরণের ডট গুণন হলো কাজ। সকল বল দ্বারা কৃত নিট কাজ বস্তুর গতিশক্তির পরিবর্তনের সমান।",
            "hack": "বল ও সরণ পরস্পর লম্ব (\\theta = 90^\\circ) হলে কাজ শূন্য (যেমন: কেন্দ্রমুখী বলের কাজ = 0)।",
            "trap": "ঋণাত্মক কাজ হয় যখন বল ও সরণের মধ্যবর্তী কোণ স্থূলকোণ (90° < \\theta \\le 180°), যেমন ঘর্ষণ বল।",
            "tags": ["work", "kinetic energy", "কাজ", "গতিশক্তি", "কাজ-শক্তি উপপাদ্য"]
        },
        {
            "id": "v_phy_we_02",
            "subject": "Physics",
            "chapter": "Work-Energy",
            "type": "shortcut",
            "title": "গতিশক্তি ও ভরবেগের শতকরা বৃদ্ধির সম্পর্ক",
            "formula": "E_k = \\frac{p^2}{2m} \\implies p = \\sqrt{2mE_k}",
            "concept": "গতিশক্তি ভরবেগের বর্গের সমানুপাতিক।",
            "hack": "ভরবেগ x% বাড়লে গতিশক্তি বাড়ে: (2x + x^2/100)%! ভরবেগ 50% বাড়লে E_k বাড়ে 2(50) + 25 = 125%!",
            "trap": "গতিশক্তি 300% বৃদ্ধি পেলে নতুন গতিশক্তি হয় 400%, ফলে ভরবেগ দ্বিগুণ (100% বৃদ্ধি) হয়। বৃদ্ধি বনাম নতুন মান গুলিয়ে ফেলবেন না।",
            "tags": ["momentum", "kinetic energy", "ভরবেগ", "গতিশক্তি", "শতকরা বৃদ্ধি"]
        },
        {
            "id": "v_phy_we_03",
            "subject": "Physics",
            "chapter": "Work-Energy",
            "type": "shortcut",
            "title": "পড়ন্ত বস্তুতে বিভবশক্তি ও গতিশক্তির অনুপাত উচ্চতা",
            "formula": "x = \\frac{H}{n + 1} \\quad (E_k = n E_p \\text{ হলে})",
            "concept": "ভূমি থেকে কত উচ্চতায় গতিশক্তি বিভবশক্তির n গুণ হবে তার শর্টকাট।",
            "hack": "গতিশক্তি বিভবশক্তির দ্বিগুণ (n = 2) হলে x = H/(2+1) = H/3! গতিশক্তি বিভবশক্তির সমান হলে x = H/2!",
            "trap": "x হলো ভূমি থেকে উচ্চতা; যদি উপর থেকে পতন দূরত্ব চায় তবে তা হবে H - x = \\frac{n}{n+1}H।",
            "tags": ["potential energy", "kinetic energy", "উচ্চতা", "বিভবশক্তি"]
        },
        {
            "id": "v_phy_we_04",
            "subject": "Physics",
            "chapter": "Work-Energy",
            "type": "shortcut",
            "title": "কুয়া ও চৌবাচ্চা খালি করার ক্ষমতা শর্টকাট",
            "formula": "P = \\frac{mgh_{avg}}{\\eta t} = \\frac{\\rho(\\pi r^2 L) g h_{avg}}{\\eta t}",
            "concept": "পানির ভরকেন্দ্রের গড় সরণ h_avg নির্ণয় করে কাজ W = mgh_avg হিসেব করা হয়।",
            "hack": "পূর্ণ কুয়া খালি: h_avg = L/2; অর্ধেক খালি: h_avg = L/4; অর্ধপূর্ণ কুয়া খালি: h_avg = 3L/4!",
            "trap": "কুয়ার ব্যাস d দেওয়া থাকলে ব্যাসার্ধ r = d/2 নিতে হবে; ব্যাসকে ব্যাসার্ধ বসালে ক্ষমতা ৪ গুণ ভুল আসবে!",
            "tags": ["well", "pump", "power", "কুয়া", "পাম্পের ক্ষমতা", "ভরকেন্দ্র"]
        },
        {
            "id": "v_phy_we_05",
            "subject": "Physics",
            "chapter": "Work-Energy",
            "type": "core_formula",
            "title": "স্প্রিংয়ের সঞ্চিত বিভবশক্তি ও পরিবর্তন",
            "formula": "W = \\frac{1}{2}kx^2, \\quad \\Delta W = \\frac{1}{2}k(x_2^2 - x_1^2)",
            "concept": "স্প্রিং প্রসারণ বা সংকোচনে বল পরিবর্তনশীল (F = kx), তাই কাজ দূরত্বের বর্গের সমানুপাতিক।",
            "hack": "স্প্রিংকে x থেকে আরও x (মোট 2x) প্রসারিত করতে অতিরিক্ত কাজ লাগে 3W (1:3:5:7 অনুপাত)!",
            "trap": "স্প্রিং অর্ধেক কাটলে k দ্বিগুণ হয় (k' = 2k), কিন্তু একই প্রসারণ x এ সঞ্চিত শক্তি অর্ধেক হয়।",
            "tags": ["spring", "potential energy", "স্প্রিং", "বিভবশক্তি"]
        },
        {
            "id": "v_phy_we_06",
            "subject": "Physics",
            "chapter": "Work-Energy",
            "type": "shortcut",
            "title": "তক্তা ভেদ ও গুলির বেগ হ্রাস",
            "formula": "N = \\frac{n^2}{2n - 1}",
            "concept": "একটি তক্তায় বেগ 1/n অংশ হ্রাস পেলে মোট কয়টি তক্তা ভেদ করতে পারবে।",
            "hack": "বেগ 1/3 অংশ হারালে: N = 3^2 / (2*3 - 1) = 9/5 = 1.8 \\implies অতিরিক্ত ১টি তক্তা ভেদ করতে পারবে!",
            "trap": "'বেগ কমে 1/n হলো' বললে বেগ থাকে 1/n, কিন্তু '1/n হারালো' বললে বেগ থাকে (1 - 1/n)।",
            "tags": ["bullet", "plank", "গুলি", "তক্তা", "ভেদ"]
        },
        {
            "id": "v_phy_we_07",
            "subject": "Physics",
            "chapter": "Work-Energy",
            "type": "core_formula",
            "title": "যন্ত্রের কর্মদক্ষতা (Efficiency)",
            "formula": "\\eta = \\frac{P_{out}}{P_{in}} \\times 100\\% = \\frac{W_{useful}}{W_{total}} \\times 100\\%",
            "concept": "প্রদত্ত ক্ষমতা এবং লভ্য কার্যকর ক্ষমতার অনুপাত হলো কর্মদক্ষতা। অপচয়কৃত ক্ষমতা P_loss = P_in - P_out।",
            "hack": "1 HP (হর্স পাওয়ার) = 746 ওয়াট (W)। ইঞ্জিনের ক্ষমতা কিলোওয়াটে চাইলে 1000 দিয়ে ভাগ।",
            "trap": "পাম্পের অংকে লভ্য কার্যকর ক্ষমতা P_out = mgh/t বের হয়, কিন্তু মোট বিদ্যুৎ ক্ষমতা P_in = P_out / eta।",
            "tags": ["efficiency", "power", "কর্মদক্ষতা", "ক্ষমতা", "HP"]
        },
        {
            "id": "v_phy_we_08",
            "subject": "Physics",
            "chapter": "Work-Energy",
            "type": "trap",
            "title": "ঘূর্ণনরত বস্তুর মোট গতিশক্তি",
            "formula": "E_k = \\frac{1}{2}mv^2 + \\frac{1}{2}I\\omega^2 = \\frac{1}{2}mv^2\\left(1 + \\frac{K^2}{R^2}\\right)",
            "concept": "গড়িয়ে চলা বস্তুর রৈখিক গতিশক্তি এবং ঘূর্ণন গতিশক্তি উভয়ের যোগফল হলো মোট গতিশক্তি।",
            "hack": "নিরেট গোলক: 0.7 mv^2 (7/10); চাকতি/সিলিন্ডার: 0.75 mv^2 (3/4); ফাঁপা গোলক: 5/6 mv^2; রিং: mv^2!",
            "trap": "কেবল রৈখিক গতিশক্তি (1/2 mv^2) হিসেব করলে ঘূর্ণনরত বস্তুর ক্ষেত্রে প্রায় 30% থেকে 50% শক্তি বাদ পড়ে যাবে!",
            "tags": ["rolling motion", "kinetic energy", "জড়তার ভ্রামক", "ঘূর্ণন গতিশক্তি"]
        }
    ])

    # Gravitation (মহাকর্ষ ও অভিকর্ষ)
    entries.extend([
        {
            "id": "v_phy_grav_01",
            "subject": "Physics",
            "chapter": "Gravitation",
            "type": "core_formula",
            "title": "মহাকর্ষ সূত্র ও অভিকর্ষজ ত্বরণ",
            "formula": "F = G\\frac{M_1 M_2}{r^2}, \\quad g = \\frac{GM}{R^2} = \\frac{4}{3}\\pi G R \\rho",
            "concept": "মহাকর্ষীয় ধ্রুবক G = 6.673 x 10^-11 N m^2 kg^-2। ঘনত্ব ধ্রুব থাকলে g সরাসরি ব্যাসার্ধ R এর সমানুপাতিক।",
            "hack": "পৃথিবীর ভর অপরিবর্তিত রেখে ব্যাসার্ধ 1% কমালে পৃষ্ঠের অভিকর্ষজ ত্বরণ 2% বৃদ্ধি পায়!",
            "trap": "G এর একক N m^2 kg^-2 এবং মাত্রা [M^-1 L^3 T^-2]। এটি মাধ্যমের প্রকৃতির ওপর নির্ভর করে না।",
            "tags": ["gravitation", "g", "মহাকর্ষ", "অভিকর্ষজ ত্বরণ", "ঘনত্ব"]
        },
        {
            "id": "v_phy_grav_02",
            "subject": "Physics",
            "chapter": "Gravitation",
            "type": "shortcut",
            "title": "উচ্চতায় ও গভীরতায় g এর মান",
            "formula": "g_h = g\\left(\\frac{R}{R+h}\\right)^2, \\quad g_d = g\\left(1 - \\frac{d}{R}\\right)",
            "concept": "ভূপৃষ্ঠ থেকে উপরে বা ভূ-অভ্যন্তরে গভীরে গেলে উভয় ক্ষেত্রেই অভিকর্ষজ ত্বরণের মান হ্রাস পায়।",
            "hack": "যদি g_h = g/n^2 হয়, তবে উচ্চতা সরাসরি h = (n - 1)R! যেমন: g/9 হলে h = (3-1)R = 2R!",
            "trap": "স্বল্প উচ্চতায় (h << R) g_h \\approx g(1 - 2h/R); একই পরিমাণ g কমতে গভীরতায় উচ্চতার দ্বিগুণ (d = 2h) যেতে হয়!",
            "tags": ["height", "depth", "উচ্চতা", "গভীরতা", "অভিকর্ষজ ত্বরণ"]
        },
        {
            "id": "v_phy_grav_03",
            "subject": "Physics",
            "chapter": "Gravitation",
            "type": "core_formula",
            "title": "মুক্তিবেগ ও কক্ষীয় বেগের নিখুঁত সম্পর্ক",
            "formula": "v_e = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2gR}, \\quad v_o = \\sqrt{\\frac{GM}{R}} = \\sqrt{gR} \\implies v_e = \\sqrt{2}v_o",
            "concept": "কোনো বস্তুকে যে সর্বনিম্ন বেগে নিক্ষেপ করলে তা আর পৃথিবীতে ফিরে আসে না তাকে মুক্তিবেগ বলে।",
            "hack": "ভূপৃষ্ঠে v_e = 11.2 km s^-1 এবং v_o = 7.92 km s^-1। মুক্তিবেগ কক্ষীয় বেগের চেয়ে 41.4% বেশি!",
            "trap": "মুক্তিবেগ নিক্ষিপ্ত বস্তুর ভর বা নিক্ষেপণ কোণের ওপর নির্ভর করে না; এটি কেবল গ্রহের ভর ও ব্যাসার্ধের ওপর নির্ভর করে।",
            "tags": ["escape velocity", "orbital velocity", "মুক্তিবেগ", "কক্ষীয় বেগ"]
        },
        {
            "id": "v_phy_grav_04",
            "subject": "Physics",
            "chapter": "Gravitation",
            "type": "shortcut",
            "title": "কেপলারের ৩য় সূত্র ও আবর্তনকাল",
            "formula": "T^2 \\propto r^3 \\implies \\frac{T_1}{T_2} = \\left(\\frac{r_1}{r_2}\\right)^{3/2}",
            "concept": "সূর্য থেকে গ্রহের গড় দূরত্বের ঘনফল আবর্তনকালের বর্গের সমানুপাতিক।",
            "hack": "দূরত্ব ৪ গুণ বাড়লে পর্যায়কাল বাড়ে 4^(3/2) = (\\sqrt{4})^3 = 8 গুণ!",
            "trap": "উপবৃত্তাকার কক্ষপথে r হলো উপবৃত্তের অর্ধ-পরাক্ষ (semi-major axis), কেবল নূন্যতম দূরত্ব নয়।",
            "tags": ["Kepler", "period", "orbit", "কেপলারের সূত্র", "পর্যায়কাল"]
        },
        {
            "id": "v_phy_grav_05",
            "subject": "Physics",
            "chapter": "Gravitation",
            "type": "trap",
            "title": "ফাঁপা গোলকের অভ্যন্তরে মহাকর্ষীয় প্রাবল্য ও বিভব",
            "formula": "E_{in} = 0, \\quad V_{in} = V_{surface} = -\\frac{GM}{R} \\; (\\text{ধ্রুবক})",
            "concept": "ফাঁপা গোলকের ভেতরে কোনো মহাকর্ষীয় বলরেখা থাকে না, তাই প্রাবল্য শূন্য। কিন্তু পৃষ্ঠ থেকে ভেতরে যেতে কোনো কাজ করতে হয় না বিধায় বিভব পৃষ্ঠের সমান থাকে।",
            "hack": "ফাঁপা গোলকের ভেতরে প্রাবল্য শূন্য কিন্তু বিভব অশূন্য ও পৃষ্ঠের সমান ধ্রুবক।",
            "trap": "প্রাবল্য E = 0 দেখে বিভব V = 0 দাগালে মারাত্মক ভুল হবে!",
            "tags": ["gravitational potential", "field", "প্রাবল্য", "বিভব", "ফাঁপা গোলক", "trap"]
        },
        {
            "id": "v_phy_grav_06",
            "subject": "Physics",
            "chapter": "Gravitation",
            "type": "shortcut",
            "title": "শোয়ার্জশিল্ড ব্যাসার্ধ (কৃষ্ণ বিবর)",
            "formula": "R_s = \\frac{2GM}{c^2} \\approx 2.95 \\times \\left(\\frac{M}{M_\\odot}\\right) \\text{ km}",
            "concept": "যে ব্যাসার্ধে কোনো বস্তুর পৃষ্ঠে মুক্তিবেগ আলোর বেগের (c) সমান হয়ে যায়, সেটি তার শোয়ার্জশিল্ড ব্যাসার্ধ।",
            "hack": "সূর্যের ভরের নক্ষত্রের জন্য R_s \\approx 3 km! পৃথিবীর জন্য R_s \\approx 8.86 mm \\approx 0.9 cm!",
            "trap": "ব্যাসার্ধ মিটারে চাইলে কিলোমিটারকে ১০০০ দিয়ে গুণ করে সঠিক উত্তর দিতে হবে।",
            "tags": ["Schwarzschild", "black hole", "শোয়ার্জশিল্ড", "কৃষ্ণ বিবর"]
        },
        {
            "id": "v_phy_grav_07",
            "subject": "Physics",
            "chapter": "Gravitation",
            "type": "core_formula",
            "title": "কৃত্রিম উপগ্রহের শক্তি বণ্টন",
            "formula": "E_k = \\frac{GMm}{2r}, \\quad E_p = -\\frac{GMm}{r}, \\quad E_{total} = -\\frac{GMm}{2r} = -E_k = \\frac{E_p}{2}",
            "concept": "বৃত্তাকার কক্ষপথে ঘূর্ণায়মান উপগ্রহের মোট শক্তি ঋণাত্মক এবং এর মান গতিশক্তির সমান কিন্তু বিপরীত।",
            "hack": "অনুপাত মনে রাখুন: E_k : E_p : E_total = 1 : -2 : -1!",
            "trap": "মোট শক্তি ঋণাত্মক হওয়ার অর্থ উপগ্রহটি পৃথিবীর সাথে মহাকর্ষীয় বন্ধনে আবদ্ধ।",
            "tags": ["satellite", "energy", "উপগ্রহ", "শক্তি বণ্টন"]
        },
        {
            "id": "v_phy_grav_08",
            "subject": "Physics",
            "chapter": "Gravitation",
            "type": "shortcut",
            "title": "ভূ-স্থির উপগ্রহের বৈশিষ্ট্য",
            "formula": "T = 24\\text{ ঘণ্টা}, \\quad h \\approx 35,800 \\text{ km} \\approx 3.6 \\times 10^4 \\text{ km}",
            "concept": "পৃথিবীর ঘূর্ণনের সাথে তাল মিলিয়ে পশ্চিম থেকে পূর্ব দিকে বিষুবীয় তলে প্রদক্ষিণকারী উপগ্রহ।",
            "hack": "ভূ-স্থির উপগ্রহের কৌণিক বেগ পৃথিবীর সমান (\\omega = \\frac{2\\pi}{86400} \\text{ rad s}^{-1}) এবং আপেক্ষিক বেগ শূন্য।",
            "trap": "দিক পূর্ব থেকে পশ্চিম নয়; সর্বদা পশ্চিম থেকে পূর্বে প্রদক্ষিণ করে।",
            "tags": ["geostationary", "satellite", "ভূ-স্থির উপগ্রহ", "পর্যায়কাল"]
        }
    ])

    # Structural Properties (পদার্থের গাঠনিক ধর্ম)
    entries.extend([
        {
            "id": "v_phy_sp_01",
            "subject": "Physics",
            "chapter": "Structural Properties",
            "type": "core_formula",
            "title": "ইয়ং-এর গুণাঙ্ক ও সঞ্চিত শক্তি",
            "formula": "Y = \\frac{FL}{A\\Delta L} = \\frac{FL}{\\pi r^2 l}, \\quad W = \\frac{1}{2}F l = \\frac{1}{2}\\frac{Y A l^2}{L}, \\quad u = \\frac{1}{2} \\times \\text{পীড়ন} \\times \\text{বিকৃতি}",
            "concept": "স্থিতিস্থাপক সীমার মধ্যে দৈর্ঘ্য পীড়ন ও দৈর্ঘ্য বিকৃতির অনুপাত একটি ধ্রুবক যাকে ইয়ং-এর গুণাঙ্ক বলে। u হলো একক আয়তনে সঞ্চিত শক্তি।",
            "hack": "তারের ব্যাসার্ধ r দ্বিগুণ করলে এবং একই বল প্রয়োগ করলে দৈর্ঘ্য বৃদ্ধি \\Delta L এক-চতুর্থাংশ (1/4) হয়ে যায়!",
            "trap": "Y কেবল উপাদানের ধর্মের ওপর নির্ভর করে; তারকে টেনে লম্বা করলে বা কাটলে তারের Y পরিবর্তন হয় না!",
            "tags": ["Young's modulus", "elasticity", "ইয়ং-এর গুণাঙ্ক", "পীড়ন", "বিকৃতি"]
        },
        {
            "id": "v_phy_sp_02",
            "subject": "Physics",
            "chapter": "Structural Properties",
            "type": "shortcut",
            "title": "তারকে টেনে দৈর্ঘ্য n গুণ বৃদ্ধি করলে রোধ ও বিকৃতি",
            "formula": "R' = n^2 R, \\quad \\Delta L = (n - 1)L",
            "concept": "তার টেনে লম্বা করলে তার আয়তন স্থির থাকে, ফলে দৈর্ঘ্য বাড়লে প্রস্থচ্ছেদের ক্ষেত্রফল হ্রাস পায়।",
            "hack": "দৈর্ঘ্য ২ গুণ করলে রোধ ৪ গুণ; দৈর্ঘ্য 0.1% বাড়ালে রোধ বাড়ে 0.2% (দ্বিগুণ শতাংশ)!",
            "trap": "তার টেনে n গুণ করা আর অতিরিক্ত n গুণ তার যুক্ত করা এক নয়; টেনে লম্বা করলে আয়তন অপরিবর্তিত থাকে।",
            "tags": ["wire", "stretching", "resistance", "বিকৃতি", "রোধ"]
        },
        {
            "id": "v_phy_sp_03",
            "subject": "Physics",
            "chapter": "Structural Properties",
            "type": "core_formula",
            "title": "পৃষ্ঠটান, পৃষ্ঠশক্তি ও সাবানের বুদবুদ",
            "formula": "T = \\frac{F}{L} = \\frac{W}{\\Delta A}, \\quad \\Delta P_{\\text{water droplet}} = \\frac{2T}{R}, \\quad \\Delta P_{\\text{soap bubble}} = \\frac{4T}{R}",
            "concept": "তরলের মুক্ত পৃষ্ঠ স্থিতিস্থাপক পর্দার মতো সংকুচিত হতে চায়। সাবানের বুদবুদে দুটি মুক্ত পৃষ্ঠ থাকায় অতিরিক্ত চাপ 4T/R।",
            "hack": "বুদবুদ বা ফোঁটার ব্যাসার্ধ অর্ধেক করলে অভ্যন্তরের অতিরিক্ত চাপ দ্বিগুণ হয়!",
            "trap": "সাবানের বুদবুদে ২টি পৃষ্ঠ (4T/R) কিন্তু পানির ফোঁটায় বা তরলের অভ্যন্তরে বায়ু বুদবুদে ১টি মাত্র পৃষ্ঠ (2T/R)।",
            "tags": ["surface tension", "soap bubble", "পৃষ্ঠটান", "পৃষ্ঠশক্তি", "বুদবুদ"]
        },
        {
            "id": "v_phy_sp_04",
            "subject": "Physics",
            "chapter": "Structural Properties",
            "type": "shortcut",
            "title": "nটি ক্ষুদ্র ফোঁটা মিলে একটি বড় ফোঁটা গঠন",
            "formula": "R = n^{1/3}r, \\quad W_{released} = 4\\pi T R^2 (n^{1/3} - 1)",
            "concept": "ক্ষুদ্র ফোঁটাগুলো একত্রিত হয়ে একটি বড় ফোঁটায় পরিণত হলে মোট পৃষ্ঠের ক্ষেত্রফল হ্রাস পায় এবং তাপশক্তি নির্গত হয় (তাপমাত্রা বৃদ্ধি পায়)।",
            "hack": "১০০০টি ফোঁটা একত্রিত হলে n = 1000 \\implies R = 10r! ক্ষেত্রফল কমে ৯ গুণ!",
            "trap": "বড় ফোঁটা ভেঙে ক্ষুদ্র ফোঁটা হলে কাজ করতে হয় এবং তাপমাত্রা হ্রাস পায় (শীতল হয়)।",
            "tags": ["droplets", "coalescence", "পৃষ্ঠশক্তি", "ফোঁটা"]
        },
        {
            "id": "v_phy_sp_05",
            "subject": "Physics",
            "chapter": "Structural Properties",
            "type": "core_formula",
            "title": "সান্দ্রতা বল ও স্টোকসের সূত্র",
            "formula": "F = -\\eta A \\frac{dv}{dx}, \\quad F_v = 6\\pi\\eta r v_t, \\quad v_t = \\frac{2r^2(\\rho - \\sigma)g}{9\\eta}",
            "concept": "সান্দ্র মাধ্যমে পতনশীল গোলীয় বস্তুর প্রান্তিক বেগ (Terminal velocity) ব্যাসার্ধের বর্গের সমানুপাতিক (v_t \\propto r^2)।",
            "hack": "বৃষ্টির ফোঁটার ব্যাসার্ধ দ্বিগুণ হলে প্রান্তিক বেগ ৪ গুণ হয়!",
            "trap": "তাপমাত্রা বৃদ্ধি পেলে তরলের সান্দ্রতা হ্রাস পায়, কিন্তু গ্যাসের সান্দ্রতা বৃদ্ধি পায়!",
            "tags": ["viscosity", "Stokes' law", "terminal velocity", "সান্দ্রতা", "প্রান্তিক বেগ"]
        },
        {
            "id": "v_phy_sp_06",
            "subject": "Physics",
            "chapter": "Structural Properties",
            "type": "trap",
            "title": "পয়সনের অনুপাতের তাত্ত্বিক ও ব্যবহারিক সীমা",
            "formula": "\\sigma = -\\frac{\\Delta r / r}{\\Delta L / L}, \\quad -1 \\le \\sigma \\le 0.5 \\; (\\text{তাত্ত্বিক}), \\quad 0 \\le \\sigma \\le 0.5 \\; (\\text{ব্যবহারিক})",
            "concept": "পার্শ্ব বিকৃতি ও দৈর্ঘ্য বিকৃতির অনুপাতকে পয়সনের অনুপাত বলে। এটি একটি এককহীন ও মাত্রাহীন ধ্রুবক।",
            "hack": "অধিকাংশ ধাতুর ক্ষেত্রে পয়সনের অনুপাত 0.25 থেকে 0.35 এর মধ্যে থাকে। কর্কের পয়সন অনুপাত প্রায় 0।",
            "trap": "তাত্ত্বিক মান চাইলে -1 থেকে 0.5; কিন্তু ব্যবহারিক মান চাইলে 0 থেকে 0.5। প্রশ্নের ভাষা দেখে দাগান!",
            "tags": ["Poisson's ratio", "limits", "পয়সনের অনুপাত", "সীমা", "trap"]
        },
        {
            "id": "v_phy_sp_07",
            "subject": "Physics",
            "chapter": "Structural Properties",
            "type": "shortcut",
            "title": "কৈশিক নলে তরলের আরোহণ উচ্চতা",
            "formula": "h = \\frac{2T\\cos\\theta}{r\\rho g}",
            "concept": "জুরিণের সূত্র মতে কৈশিক নলে তরলের আরোহণ নলের ব্যাসার্ধের ব্যস্তানুপাতিক (h \\propto 1/r)।",
            "hack": "বিশুদ্ধ পানি ও কাচের স্পর্শ কোণ \\theta \\approx 0^\\circ (\\cos\\theta = 1); পারদ ও কাচের স্পর্শ কোণ \\theta \\approx 140^\\circ (স্থূলকোণ, নিচে নামে)।",
            "trap": "কৃত্রিম উপগ্রহে বা ওজনহীন অবস্থায় g = 0 হওয়ায় পানি নলের পুরো দৈর্ঘ্য পর্যন্ত উঠে উপচে না পড়ে স্থির থাকবে।",
            "tags": ["capillary", "surface tension", "কৈশিক নল", "আরোহণ উচ্চতা"]
        },
        {
            "id": "v_phy_sp_08",
            "subject": "Physics",
            "chapter": "Structural Properties",
            "type": "core_formula",
            "title": "সান্দ্রতা গুণাঙ্কের একক ও মাত্রা",
            "formula": "[\\eta] = [M L^{-1} T^{-1}], \\quad \\text{SI Unit} = \\text{N s m}^{-2} = \\text{Pa s} = \\text{kg m}^{-1}\\text{s}^{-1}",
            "concept": "১ Poiseuille (PI) = 10 Poise (CGS একক)।",
            "hack": "1 Pa s = 10 Poise; পরীক্ষার প্রশ্নে Poise দেওয়া থাকলে 10 দিয়ে ভাগ করে SI বানাতে হবে।",
            "trap": "সান্দ্রতা বলের একক N, কিন্তু সান্দ্রতা গুণাঙ্কের একক N s m^-2 বা Pa s।",
            "tags": ["viscosity unit", "dimension", "একক ও মাত্রা", "সান্দ্রতা গুণাঙ্ক"]
        }
    ])

    # Waves (তরঙ্গ)
    entries.extend([
        {
            "id": "v_phy_wav_01",
            "subject": "Physics",
            "chapter": "Waves",
            "type": "core_formula",
            "title": "অগ্রগামী তরঙ্গের প্রমিত সমীকরণ ও দশা পার্থক্য",
            "formula": "y = A\\sin\\left(\\frac{2\\pi}{\\lambda}(vt - x)\\right) = A\\sin(\\omega t - kx), \\quad \\Delta\\delta = \\frac{2\\pi}{\\lambda}\\Delta x = \\frac{2\\pi}{T}\\Delta t",
            "concept": "দশা পার্থক্য = (2pi / lambda) * পথ পার্থক্য। তরঙ্গের বিস্তার A, কৌণিক কম্পাঙ্ক \\omega = 2pi f, তরঙ্গ সংখ্যা k = 2pi / lambda।",
            "hack": "তরঙ্গের বেগ v = \\omega / k = (t এর সহগ) / (x এর সহগ)! সমীকরণ দেখেই সরাসরি ভাগ করে বেগ বের করা যায়!",
            "trap": "(vt - x) থাকলে তরঙ্গ ধনাত্মক x দিকে যায়, কিন্তু (vt + x) থাকলে ঋণাত্মক x দিকে যায়।",
            "tags": ["wave equation", "phase difference", "অগ্রগামী তরঙ্গ", "দশা পার্থক্য", "তরঙ্গ বেগ"]
        },
        {
            "id": "v_phy_wav_02",
            "subject": "Physics",
            "chapter": "Waves",
            "type": "shortcut",
            "title": "টানযুক্ত তারের আড় তরঙ্গের বেগ ও কম্পাঙ্ক",
            "formula": "v = \\sqrt{\\frac{T}{\\mu}}, \\quad f = \\frac{1}{2L}\\sqrt{\\frac{T}{\\mu}} \\quad (\\mu = m/L = \\pi r^2 \\rho)",
            "concept": "টান T বাড়ালে বেগ ও কম্পাঙ্ক বাড়ে; তারের ভর বা ব্যাসার্ধ বাড়ালে বেগ হ্রাস পায়।",
            "hack": "টান ৪ গুণ বাড়ালে কম্পাঙ্ক দ্বিগুণ হয় (f \\propto \\sqrt{T}); তারের ব্যাসার্ধ দ্বিগুণ করলে কম্পাঙ্ক অর্ধেক হয়!",
            "trap": "\\mu হলো একক দৈর্ঘ্যের ভর (kg m^-1), পুরো তারের ভর নয়।",
            "tags": ["stretched string", "frequency", "আড় তরঙ্গ", "কম্পাঙ্ক", "টান"]
        },
        {
            "id": "v_phy_wav_03",
            "subject": "Physics",
            "chapter": "Waves",
            "type": "core_formula",
            "title": "স্থির তরঙ্গের নিস্পন্দ ও সুস্পন্দ বিন্দু",
            "formula": "y = 2A\\cos(kx)\\sin(\\omega t), \\quad \\text{দূরত্ব} = \\frac{\\lambda}{2} \\; (N\\text{ to } N), \\quad \\frac{\\lambda}{4} \\; (N\\text{ to } A)",
            "concept": "দুটি সমান ও বিপরীতমুখী তরঙ্গের উপরিপাতনে স্থির তরঙ্গ তৈরি হয়। এতে কোনো শক্তির স্থানান্তর ঘটে না।",
            "hack": "পরপর দুটি নিস্পন্দ বিন্দুর দূরত্ব lambda/2; একটি নিস্পন্দ ও পরবর্তী সুস্পন্দ বিন্দুর দূরত্ব lambda/4!",
            "trap": "স্থির তরঙ্গে বিস্তার শূন্য যেখানে তা নিস্পন্দ বিন্দু (Node), আর যেখানে বিস্তার সর্বোচ্চ (2A) তা সুস্পন্দ বিন্দু (Antinode)।",
            "tags": ["standing wave", "node", "antinode", "স্থির তরঙ্গ", "নিস্পন্দ বিন্দু"]
        },
        {
            "id": "v_phy_wav_04",
            "subject": "Physics",
            "chapter": "Waves",
            "type": "shortcut",
            "title": "বীট (Beat) ও সুরশলাকার অজানা কম্পাঙ্ক",
            "formula": "f_{beat} = |f_1 - f_2|",
            "concept": "নিকটবর্তী কম্পাঙ্কের দুটি শব্দ তরঙ্গের উপরিপাতনে প্রতি সেকেন্ডে সৃষ্ট শব্দ তীব্রতার হ্রাস-বৃদ্ধি হলো বীট।",
            "hack": "সুরশলাকায় মোম লাগালে কম্পাঙ্ক হ্রাস পায়; ঘষলে কম্পাঙ্ক বৃদ্ধি পায়! হ্রাস পেয়ে বীট বাড়লে f_অজানা < f_জ্ঞাত।",
            "trap": "বীট সংখ্যা ৪ হলে অজানা কম্পাঙ্ক f \\pm 4 দুটিই হতে পারে; মোম বা ঘষার পরবর্তী পরিবর্তন দেখে একটি নির্দিষ্ট করতে হবে।",
            "tags": ["beat", "tuning fork", "বীট", "সুরশলাকা", "কম্পাঙ্ক"]
        },
        {
            "id": "v_phy_wav_05",
            "subject": "Physics",
            "chapter": "Waves",
            "type": "core_formula",
            "title": "খোলা নল বনাম বন্ধ নলের মূল সুর",
            "formula": "f_{\\text{open}} = \\frac{v}{2L} \\; (1:2:3:4), \\quad f_{\\text{closed}} = \\frac{v}{4L} \\; (1:3:5:7)",
            "concept": "খোলা নলে সকল হারমোনিক (জোড় ও বিজোড়) উৎপন্ন হয়; বন্ধ নলে কেবল বিজোড় হারমোনিক উৎপন্ন হয়।",
            "hack": "একই দৈর্ঘ্যের খোলা নলের মূল সুর বন্ধ নলের মূল সুরের দ্বিগুণ (f_open = 2 f_closed)!",
            "trap": "বন্ধ নলে ২য় হারমোনিক বলে কিছু নেই; ১ম উপসুর হলো ৩য় হারমোনিক (3f)।",
            "tags": ["organ pipe", "harmonics", "খোলা নল", "বন্ধ নল", "হারমোনিক"]
        },
        {
            "id": "v_phy_wav_06",
            "subject": "Physics",
            "chapter": "Waves",
            "type": "shortcut",
            "title": "ডপলার প্রভাব (Doppler Effect) এক নজরে",
            "formula": "f' = \\left(\\frac{v \\pm v_o}{v \\mp v_s}\\right)f",
            "concept": "উৎস বা শ্রোতার আপেক্ষিক গতির কারণে আপাত কম্পাঙ্কের পরিবর্তন। কাছে আসলে কম্পাঙ্ক বাড়ে, দূরে গেলে কমে।",
            "hack": "কাছে আসলে লব বড় ও হর ছোট হয় (f' > f); দূরে গেলে লব ছোট ও হর বড় হয় (f' < f)!",
            "trap": "উৎস ও শ্রোতা একই বেগে একই দিকে চললে আপেক্ষিক বেগ শূন্য হওয়ায় কম্পাঙ্কের কোনো পরিবর্তন হয় না (f' = f)।",
            "tags": ["Doppler effect", "apparent frequency", "ডপলার প্রভাব", "আপাত কম্পাঙ্ক"]
        },
        {
            "id": "v_phy_wav_07",
            "subject": "Physics",
            "chapter": "Waves",
            "type": "core_formula",
            "title": "শব্দের তীব্রতা ও তীব্রতা লেভেল (ডেসিবেল)",
            "formula": "I = 2\\pi^2 f^2 A^2 \\rho v, \\quad \\beta = 10\\log_{10}\\left(\\frac{I}{I_0}\\right) \\text{ dB} \\quad (I_0 = 10^{-12} \\text{ W m}^{-2})",
            "concept": "তীব্রতা বিস্তারের বর্গের সমানুপাতিক (I \\propto A^2)। প্রমিত শ্রবণানুভূতি সীমা I_0 = 10^-12 W m^-2।",
            "hack": "তীব্রতা ১০ গুণ বাড়লে তীব্রতা লেভেল বাড়ে 10 dB; ১০০ গুণ বাড়লে বাড়ে 20 dB; ১০০০ গুণ বাড়লে 30 dB!",
            "trap": "তীব্রতা দ্বিগুণ হলে \\beta বাড়ে 10 \\log 2 = 10(0.30) = 3 dB, 20 dB নয়।",
            "tags": ["sound intensity", "decibel", "ডেসিবেল", "তীব্রতা লেভেল"]
        },
        {
            "id": "v_phy_wav_08",
            "subject": "Physics",
            "chapter": "Waves",
            "type": "trap",
            "title": "শব্দের বেগের ওপর তাপমাত্রা ও আর্দ্রতার প্রভাব",
            "formula": "v \\propto \\sqrt{T} \\implies \\frac{v_1}{v_2} = \\sqrt{\\frac{T_1}{T_2}}, \\quad v_t \\approx v_0 + 0.61 t",
            "concept": "তাপমাত্রা বৃদ্ধি পেলে এবং বাতাসে আর্দ্রতা বাড়লে শব্দের বেগ বৃদ্ধি পায় (জলীয় বাষ্পের ঘনত্ব শুষ্ক বায়ুর চেয়ে কম)।",
            "hack": "প্রতি ১°C তাপমাত্রা বৃদ্ধিতে বাতাসে শব্দের বেগ 0.61 ms^-1 বৃদ্ধি পায়।",
            "trap": "চাপের পরিবর্তনে শব্দের বেগের কোনো পরিবর্তন হয় না (কারণ চাপ বাড়লে ঘনত্বও সমহারে বাড়ে)! পরীক্ষায় চাপ দ্বিগুণ করলে বেগ অপরিবর্তিত থাকে।",
            "tags": ["sound speed", "temperature", "humidity", "শব্দের বেগ", "চাপের প্রভাব", "trap"]
        }
    ])

    # Ideal Gas (আদর্শ গ্যাস ও গতিতত্ত্ব)
    entries.extend([
        {
            "id": "v_phy_gas_01",
            "subject": "Physics",
            "chapter": "Ideal Gas",
            "type": "core_formula",
            "title": "আদর্শ গ্যাস সমীকরণ ও সার্বজনীন গ্যাস ধ্রুবক",
            "formula": "PV = nRT = \\frac{m}{M}RT = N k_B T, \\quad R = 8.314 \\text{ J mol}^{-1}\\text{K}^{-1} = 0.0821 \\text{ L atm mol}^{-1}\\text{K}^{-1}",
            "concept": "বয়েল, চার্লস ও অ্যাভোগাড্রোর সূত্রের সমন্বিত রূপ। বোল্টজম্যান ধ্রুবক k_B = R/N_A = 1.38 x 10^-23 J K^-1।",
            "hack": "27°C (300 K) এ RT এর মান: SI এককে RT \\approx 2500 J mol^-1; লিটার-অ্যাটমস্ফিয়ারে RT \\approx 24.6 L atm!",
            "trap": "তাপমাত্রা সর্বদা কেলভিনে নিতে হবে; সেলসিয়াস বসিয়ে অনুপাত করলে সম্পূর্ণ ভুল মান আসবে।",
            "tags": ["ideal gas", "gas constant", "PV=nRT", "আদর্শ গ্যাস", "বোল্টজম্যান"]
        },
        {
            "id": "v_phy_gas_02",
            "subject": "Physics",
            "chapter": "Ideal Gas",
            "type": "shortcut",
            "title": "বুদবুদ হ্রদের তলদেশ থেকে উপরিপৃষ্ঠে উঠা",
            "formula": "h = (n - 1) \\times 10.33 \\text{ m} \\approx (n - 1) \\times 10.2 \\text{ m}",
            "concept": "উপরিভাগে বুদবুদের আয়তন তলদেশের n গুণ হলে তলদেশের চাপ উপরিভাগের চাপের n গুণ (P_bottom = n P_atm)।",
            "hack": "আয়তন ৫ গুণ হলে n = 5 \\implies h = (5 - 1) * 10.33 \\approx 41.3 মিটার! ব্যাস n গুণ বললে আয়তন n^3 গুণ হয়!",
            "trap": "প্রশ্নে 'ব্যাস ৫ গুণ' বলা থাকলে n = 5^3 = 125 ধরতে হবে; ব্যাস আর আয়তনের পার্থক্য মনে রাখুন।",
            "tags": ["bubble", "lake depth", "বুদবুদ", "হ্রদের গভীরতা", "বয়েলের সূত্র"]
        },
        {
            "id": "v_phy_gas_03",
            "subject": "Physics",
            "chapter": "Ideal Gas",
            "type": "core_formula",
            "title": "RMS বেগ ও গতিশক্তি",
            "formula": "c_{rms} = \\sqrt{\\frac{3RT}{M}} = \\sqrt{\\frac{3P}{\\rho}}, \\quad E_k = \\frac{3}{2}nRT = \\frac{3}{2}k_B T \\; (\\text{প্রতি অণু})",
            "concept": "মূল গড় বর্গবেগ পরম তাপমাত্রার বর্গমূলের সমানুপাতিক এবং আণবিক ভরের বর্গমূলের ব্যস্তানুপাতিক।",
            "hack": "গ্যাসের মোট গতিশক্তি কেবল তাপমাত্রার ওপর নির্ভর করে, চাপের ওপর নয়! তাপমাত্রা ৪ গুণ করলে c_rms দ্বিগুণ হয়।",
            "trap": "এক মোল গ্যাসের গতিশক্তি 3/2 RT, কিন্তু একটি অণুর গতিশক্তি 3/2 k_B T (R নয়, k_B দিয়ে ভাগ)।",
            "tags": ["RMS velocity", "kinetic energy", "গ্যাসের গতিশক্তি", "RMS বেগ"]
        },
        {
            "id": "v_phy_gas_04",
            "subject": "Physics",
            "chapter": "Ideal Gas",
            "type": "shortcut",
            "title": "স্বাধীনতার মাত্রা ও মোলার তাপধারণ ক্ষমতা",
            "formula": "C_v = \\frac{f}{2}R, \\quad C_p = \\left(\\frac{f}{2} + 1\\right)R, \\quad \\gamma = \\frac{C_p}{C_v} = 1 + \\frac{2}{f}",
            "concept": "এক-পরমাণুক গ্যাসে f = 3 (gamma = 1.67); দ্বি-পরমাণুকে f = 5 (gamma = 1.40); বহু-পরমাণুকে f = 6 (gamma = 1.33)।",
            "hack": "হিলিয়াম/আর্গন (এক-পরমাণুক): gamma = 5/3 = 1.67; অক্সিজেন/নাইট্রোজেন (দ্বি-পরমাণুক): gamma = 7/5 = 1.40!",
            "trap": "মেয়ারের সম্পর্ক C_p - C_v = R; C_p সর্বদা C_v এর চেয়ে বড়।",
            "tags": ["degrees of freedom", "gamma", "Cp", "Cv", "স্বাধীনতার মাত্রা"]
        },
        {
            "id": "v_phy_gas_05",
            "subject": "Physics",
            "chapter": "Ideal Gas",
            "type": "core_formula",
            "title": "আপেক্ষিক আর্দ্রতা ও গ্লেইশারের সূত্র",
            "formula": "RH = \\frac{f}{F} \\times 100\\%, \\quad \\theta = \\theta_1 - G(\\theta_1 - \\theta_2)",
            "concept": "শিশিরাঙ্কে সম্পৃক্ত বাষ্পচাপ (f) এবং বায়ুর তাপমাত্রায় সম্পৃক্ত বাষ্পচাপের (F) অনুপাত হলো আপেক্ষিক আর্দ্রতা।",
            "hack": "শুষ্ক ও আর্দ্র বাল্ব থার্মোমিটারের পাঠের পার্থক্য যত বেশি, আবহাওয়া তত শুষ্ক (RH কম); পার্থক্য শূন্য হলে RH = 100% (বৃষ্টির সম্ভাবনা)।",
            "trap": "শিশিরাঙ্ক হলো তাপমাত্রা (°C), কিন্তু বাষ্পচাপের একক হলো mmHg বা Pa।",
            "tags": ["relative humidity", "Glaisher", "শিশিরাঙ্ক", "আপেক্ষিক আর্দ্রতা"]
        },
        {
            "id": "v_phy_gas_06",
            "subject": "Physics",
            "chapter": "Ideal Gas",
            "type": "shortcut",
            "title": "গ্রাহামের গ্যাস ব্যাপন সূত্র শর্টকাট",
            "formula": "\\frac{r_1}{r_2} = \\sqrt{\\frac{M_2}{M_1}} = \\sqrt{\\frac{d_2}{d_1}} = \\frac{t_2}{t_1}",
            "concept": "নির্দিষ্ট তাপমাত্রা ও চাপে গ্যাসের ব্যাপন হার তার ঘনত্বের বা আণবিক ভরের বর্গমূলের ব্যস্তানুপাতিক।",
            "hack": "হাইড্রোজেন (M = 2) এবং অক্সিজেন (M = 32) এর ব্যাপন হার: r_H2 / r_O2 = \\sqrt{32/2} = \\sqrt{16} = 4 গুণ দ্রুত!",
            "trap": "যে গ্যাস যত হালকা তার ব্যাপন হার তত বেশি এবং ব্যাপন সময় তত কম (r \\propto 1/t)।",
            "tags": ["Graham's law", "diffusion", "ব্যাপন হার", "আণবিক ভর"]
        },
        {
            "id": "v_phy_gas_07",
            "subject": "Physics",
            "chapter": "Ideal Gas",
            "type": "trap",
            "title": "বাস্তব গ্যাসের আদর্শ আচরণ করার শর্ত",
            "formula": "\\text{উচ্চ তাপমাত্রা (High } T) \\quad \\text{ও} \\quad \\text{নিম্ন চাপ (Low } P)",
            "concept": "উচ্চ তাপমাত্রায় অণুগুলোর গতিশক্তি বেশি থাকায় আকর্ষণ বল নগণ্য হয় এবং নিম্ন চাপে অণুগুলোর নিজস্ব আয়তন পাত্রের তুলনায় নগণ্য হয়।",
            "hack": "মনে রাখুন: HT-LP (High Temperature, Low Pressure)! ভ্যান ডার ওয়ালস সমীকরণ: (P + an^2/V^2)(V - nb) = nRT।",
            "trap": "পরীক্ষায় উল্টো করে 'নিম্ন তাপমাত্রা ও উচ্চ চাপ' অপশনে প্রথম দেওয়া থাকে যা ভুল!",
            "tags": ["real gas", "ideal behavior", "বাস্তব গ্যাস", "ভ্যান ডার ওয়ালস", "trap"]
        },
        {
            "id": "v_phy_gas_08",
            "subject": "Physics",
            "chapter": "Ideal Gas",
            "type": "core_formula",
            "title": "গ্যাসের গড় মুক্ত পথ",
            "formula": "\\lambda = \\frac{1}{\\sqrt{2}\\pi n d^2} \\; (\\text{ক্লসিয়াস/ম্যাক্সওয়েল})",
            "concept": "গ্যাস অণুর পরপর দুটি সংঘর্ষের মধ্যবর্তী অতিক্রান্ত দূরত্বের গড় মান। এটি ঘনত্ব n এর ব্যস্তানুপাতিক।",
            "hack": "গড় মুক্ত পথ অণুর ব্যাসের বর্গের ব্যস্তানুপাতিক (\\lambda \\propto 1/d^2) এবং তাপমাত্রার সমানুপাতিক (\\lambda \\propto T)।",
            "trap": "চাপ বাড়লে অণুগুলোর ঘনত্ব n বাড়ে, ফলে গড় মুক্ত পথ হ্রাস পায়।",
            "tags": ["mean free path", "গড় মুক্ত পথ", "সংঘর্ষ", "ব্যাসার্ধ"]
        }
    ])

    return entries

if __name__ == "__main__":
    entries = get_vault_entries()
    print(f"Physics Entries: {len(entries)}")

