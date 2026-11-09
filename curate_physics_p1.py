#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_physics_p1.py
Physics 1st Paper Chapters 1 to 6 (104 authentic MCQs):
- phy_1st_01: ভৌতজগৎ ও পরিমাপ (Physical World & Measurement) - 12 MCQs
- phy_1st_02: ভেক্টর (Vector) - 20 MCQs
- phy_1st_03: গতিবিদ্যা ও প্রক্ষেপক (Dynamics & Projectile) - 20 MCQs
- phy_1st_04: নিউটনীয় বলবিদ্যা (Newtonian Mechanics) - 20 MCQs
- phy_1st_05: কাজ, শক্তি ও ক্ষমতা (Work, Energy & Power) - 20 MCQs
- phy_1st_06: মহাকর্ষ ও অভিকর্ষ (Gravitation & Gravity) - 20 MCQs
"""

import gen_physics_predictors

def get_part1_chapters():
    chapters = []

    # -------------------------------------------------------------
    # 1. phy_1st_01: ভৌতজগৎ ও পরিমাপ (12 MCQs)
    # -------------------------------------------------------------
    ch01 = {
        "chapter_id": "phy_1st_01",
        "chapter_title": "ভৌতজগৎ ও পরিমাপ (Physical World & Measurement)",
        "subject": "Physics",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০১",
        "predictors": [
            {
                "id": "pred_phy_1st_01_01",
                "stem": "প্ল্যাঙ্কের ধ্রুবকের ($h$) মাত্রা সমীকরণ নিচের কোন রাশির মাত্রা সমীকরণের অনুরূপ?",
                "options": ["কৌণিক ভরবেগ ($L$)", "রৈখিক ভরবেগ ($p$)", "ক্ষমতা ($P$)", "বল ($F$)"],
                "answer": "A",
                "type_ref": "Type 1: মাত্রা সমীকরণ ও সমমাত্রিকতার নীতি",
                "trap_alert": "রৈখিক ভরবেগ $[MLT^{-1}]$ এর সাথে কৌণিক ভরবেগ $[ML^2T^{-1}]$ গুলিয়ে ফেলা।",
                "speed_hack": "প্ল্যাঙ্কের ধ্রুবক $h = E/\nu \implies [ML^2T^{-2}]/[T^{-1}] = [ML^2T^{-1}]$। কৌণিক ভরবেগ $L = mvr \implies [M][LT^{-1}][L] = [ML^2T^{-1}]$। উভয় মাত্রা হুবহু এক।",
                "explanation": "প্ল্যাঙ্কের ধ্রুবক $h = \\frac{E}{\\nu}$ এর মাত্রা $[ML^2T^{-1}]$। আবার কৌণিক ভরবেগ $L = mvr$ এর মাত্রা $[M][LT^{-1}][L] = [ML^2T^{-1}]$। সুতরাং $h$ ও $L$ এর মাত্রা সমীকরণ একই।"
            },
            {
                "id": "pred_phy_1st_01_02",
                "stem": "সান্দ্রতা গুণাঙ্কের ($\\eta$) সঠিক মাত্রা সমীকরণ এবং এসআই একক কোনটি?",
                "options": [
                    "$[ML^{-1}T^{-1}]$ এবং $\\text{Pa}\\cdot\\text{s}$",
                    "$[MLT^{-2}]$ এবং $\\text{N}\\cdot\\text{m}$",
                    "$[ML^{-2}T^{-1}]$ এবং $\\text{N}/\\text{m}^2$",
                    "$[ML^2T^{-1}]$ এবং $\\text{J}\\cdot\\text{s}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: মাত্রা সমীকরণ ও সমমাত্রিকতার নীতি",
                "trap_alert": "পৃষ্ঠটানের মাত্রা $[MT^{-2}]$ অথবা চাপের মাত্রা $[ML^{-1}T^{-2}]$ দাগানো।",
                "speed_hack": "নিউটনীয় সান্দ্রতা সমীকরণ: $F = \\eta A \\frac{dv}{dx} \\implies [\\eta] = \\frac{[F]}{[A][dv/dx]} = \\frac{MLT^{-2}}{L^2 \\cdot T^{-1}} = [ML^{-1}T^{-1}]$। একক $\\text{Pa}\\cdot\\text{s}$ বা $\\text{N}\\cdot\\text{s}\\cdot\\text{m}^{-2}$।",
                "explanation": "স্টোকসের সূত্র বা নিউটনের সান্দ্রতা সূত্র অনুসারে $F = 6\\pi\\eta r v \\implies \\eta = \\frac{F}{6\\pi r v}$। মাত্রা $= \\frac{MLT^{-2}}{L \\cdot LT^{-1}} = [ML^{-1}T^{-1}]$। এর এসআই একক $\\text{N}\\cdot\\text{s}/\\text{m}^2$ বা প্যাসকেল-সেকেন্ড ($\\text{Pa}\\cdot\\text{s}$)।"
            },
            {
                "id": "pred_phy_1st_01_03",
                "stem": "একটি স্লাইড ক্যালিপার্সের প্রধান স্কেলের ক্ষুদ্রতম ১ ভাগের মান $1\\text{ mm}$ এবং ভার্নিয়ার স্কেলের মোট ভাগ সংখ্যা $20$ হলে ভার্নিয়ার ধ্রুবক ($VC$) কত?",
                "options": ["$0.05\\text{ mm}$ বা $0.005\\text{ cm}$", "$0.02\\text{ mm}$ বা $0.002\\text{ cm}$", "$0.01\\text{ mm}$", "$0.5\\text{ mm}$"],
                "answer": "A",
                "type_ref": "Type 2: ভার্নিয়ার ধ্রুবক, পিচ ও স্ক্রু গজের লঘিষ্ঠ গণন",
                "trap_alert": "ভাগ সংখ্যা ২০ দেখে সাধারণ ১০ ভাগের ভার্নিয়ার ধ্রুবক $0.1\\text{ mm}$ এর কথা ভাবা অথবা একক $\\text{mm}$ ও $\\text{cm}$ এর মধ্যে ভুল করা।",
                "speed_hack": "$VC = \\frac{s}{n} = \\frac{1\\text{ mm}}{20} = 0.05\\text{ mm} = 0.005\\text{ cm}$। সরাসরি ভাগ।",
                "explanation": "ভার্নিয়ার ধ্রুবক $VC = \\frac{s}{n}$, যেখানে মূল স্কেলের ক্ষুদ্রতম এক ভাগ $s = 1\\text{ mm}$ এবং ভার্নিয়ার স্কেলের মোট ভাগ $n = 20$। সুতরাং $VC = \\frac{1}{20}\\text{ mm} = 0.05\\text{ mm} = 0.005\\text{ cm}$।"
            },
            {
                "id": "pred_phy_1st_01_04",
                "stem": "একটি স্ক্রু গজের পিচ $1\\text{ mm}$ এবং বৃত্তাকার স্কেলের মোট ভাগ সংখ্যা $100$ হলে এর লঘিষ্ঠ গণন ($LC$) কত?",
                "options": ["$0.01\\text{ mm}$", "$0.001\\text{ mm}$", "$0.1\\text{ mm}$", "$0.05\\text{ mm}$"],
                "answer": "A",
                "type_ref": "Type 2: ভার্নিয়ার ধ্রুবক, পিচ ও স্ক্রু গজের লঘিষ্ঠ গণন",
                "trap_alert": "পিচকে ভাগ সংখ্যা দিয়ে গুণ করে ফেলা অথবা সেন্টিমিটার ও মিলিমিটারের দশমিক স্থানে ভুল করা।",
                "speed_hack": "$LC = \\frac{\\text{Pitch}}{n} = \\frac{1\\text{ mm}}{100} = 0.01\\text{ mm} = 10^{-5}\\text{ m}$।",
                "explanation": "লঘিষ্ঠ গণন $LC = \\frac{\\text{পিচ}}{\\text{বৃত্তাকার স্কেলের ভাগ সংখ্যা}} = \\frac{1\\text{ mm}}{100} = 0.01\\text{ mm} = 0.001\\text{ cm}$।"
            },
            {
                "id": "pred_phy_1st_01_05",
                "stem": "একটি গোলকের ব্যাসার্ধ পরিমাপে শতকরা ত্রুটি $1.5\\%$ হলে এর আয়তন পরিমাপে শতকরা ত্রুটি কত হবে?",
                "options": ["$4.5\\%$", "$3.0\\%$", "$2.25\\%$", "$6.0\\%$"],
                "answer": "A",
                "type_ref": "Type 3: পরিমাপে শতকরা ত্রুটি ও ঘাতজনিত বিস্তার",
                "trap_alert": "বর্গ ভেবে ৩% ($2 \\times 1.5$) দাগানো; ক্ষেত্রফল চাইলে ৩% হতো, আয়তন চেয়েছে তাই ৩ দিয়ে গুণ হবে।",
                "speed_hack": "আয়তন $V = \\frac{4}{3}\\pi r^3 \\implies$ ঘাত ৩ $\\implies$ ত্রুটি $3 \\times 1.5\\% = 4.5\\%$। ৩ সেকেন্ডে সমাধান।",
                "explanation": "গোলকের আয়তন $V = \\frac{4}{3}\\pi r^3$। ঘাতজনিত ত্রুটির সূত্রানুসারে $\\frac{\\Delta V}{V} \\times 100\\% = 3\\left(\\frac{\\Delta r}{r} \\times 100\\%\\right) = 3 \\times 1.5\\% = 4.5\\%$।"
            },
            {
                "id": "pred_phy_1st_01_06",
                "stem": "মহাকর্ষীয় ধ্রুবক $G$ এর মাত্রা সমীকরণ কোনটি?",
                "options": ["$[M^{-1}L^3T^{-2}]$", "$[ML^3T^{-2}]$", "$[M^{-1}L^2T^{-2}]$", "$[ML^2T^{-1}]$"],
                "answer": "A",
                "type_ref": "Type 1: মাত্রা সমীকরণ ও সমমাত্রিকতার নীতি",
                "trap_alert": "ভর $M$ এর ঘাত ঋণাত্মক ($-1$) না দিয়ে ধনাত্মক $+1$ দাগানো।",
                "speed_hack": "$F = G \\frac{m_1 m_2}{r^2} \\implies G = \\frac{F r^2}{m^2} \\implies \\frac{[MLT^{-2}][L^2]}{[M^2]} = [M^{-1}L^3T^{-2}]$।",
                "explanation": "নিউটনের মহাকর্ষ সূত্রানুসারে $G = \\frac{F d^2}{m_1 m_2}$। মাত্রা $[G] = \\frac{[MLT^{-2}][L^2]}{[M^2]} = [M^{-1}L^3T^{-2}]$। এর এসআই একক $\\text{N}\\cdot\\text{m}^2\\cdot\\text{kg}^{-2}$।"
            },
            {
                "id": "pred_phy_1st_01_07",
                "stem": "নিচের কোন রাশিটি মাত্রাহীন কিন্তু এর সুনির্দিষ্ট এসআই একক বিদ্যমান?",
                "options": ["সমতল কোণ (একক: রেডিয়ান)", "আপেক্ষিক আর্দ্রতা", "পয়সনের অনুপাত", "প্রতিসরাঙ্ক"],
                "answer": "A",
                "type_ref": "Type 1: মাত্রা সমীকরণ ও সমমাত্রিকতার নীতি",
                "trap_alert": "মাত্রাহীন মানেই এককহীন ভাবা। কোণ ও ঘনকোণ মাত্রাহীন কিন্তু এদের একক যথাক্রমে রেডিয়ান ও স্টেরেডিয়ান।",
                "speed_hack": "কোণ $\\theta = \\frac{s}{r} \\implies [L]/[L] = 1$ (মাত্রাহীন), কিন্তু এসআই একক হলো রেডিয়ান ($\\text{rad}$)।",
                "explanation": "কোণ হলো দুটি দৈর্ঘ্যের অনুপাত (চাপ/ব্যাসার্ধ), ফলে এটি মাত্রাহীন। তবে এসআই পদ্ধতিতে কোণের একক রেডিয়ান এবং ঘনকোণের একক স্টেরেডিয়ান নির্ধারণ করা হয়েছে।"
            },
            {
                "id": "pred_phy_1st_01_08",
                "stem": "এক আলোকবর্ষ (1 light year) কত মিটারের সমতুল্য?",
                "options": ["$9.46 \\times 10^{15}\\text{ m}$", "$9.46 \\times 10^{12}\\text{ m}$", "$3.08 \\times 10^{16}\\text{ m}$", "$1.496 \\times 10^{11}\\text{ m}$"],
                "answer": "A",
                "type_ref": "Type 1: মাত্রা সমীকরণ ও সমমাত্রিকতার নীতি",
                "trap_alert": "কিলোমিটারের মান ($9.46 \\times 10^{12}\\text{ km}$) মিটারের এককে দাগিয়ে ফেলা অথবা ১ পারসেকের ($3.08 \\times 10^{16}\\text{ m}$) সাথে গুলিয়ে ফেলা।",
                "speed_hack": "$s = c \\times t = (3 \\times 10^8\\text{ m/s}) \\times (365.25 \\times 86400\\text{ s}) \\approx 9.46 \\times 10^{15}\\text{ m}$।",
                "explanation": "শূন্য মাধ্যমে আলো এক বছরে যে দূরত্ব অতিক্রম করে তাকে ১ আলোকবর্ষ বলে। $1\\text{ ly} = 3 \\times 10^8\\text{ m/s} \\times (365 \\times 24 \\times 3600\\text{ s}) = 9.46 \\times 10^{15}\\text{ m}$।"
            },
            {
                "id": "pred_phy_1st_01_09",
                "stem": "একটি দণ্ডের দৈর্ঘ্য পরিমাপে মূল স্কেলের পাঠ $4.5\\text{ cm}$, ভার্নিয়ার সমপাতন $6$ এবং ভার্নিয়ার ধ্রুবক $0.005\\text{ cm}$ পাওয়া গেলে দণ্ডটির প্রকৃত দৈর্ঘ্য কত?",
                "options": ["$4.530\\text{ cm}$", "$4.560\\text{ cm}$", "$4.800\\text{ cm}$", "$4.503\\text{ cm}$"],
                "answer": "A",
                "type_ref": "Type 2: ভার্নিয়ার ধ্রুবক, পিচ ও স্ক্রু গজের লঘিষ্ঠ গণন",
                "trap_alert": "$6 \\times 0.005 = 0.03$ যোগ না করে সরাসরি $0.06$ যোগ করে $4.56$ দাগানো।",
                "speed_hack": "$L = M + (V \\times VC) = 4.5 + (6 \\times 0.005) = 4.5 + 0.03 = 4.53\\text{ cm}$।",
                "explanation": "স্লাইড ক্যালিপার্সে দৈর্ঘ্য পরিমাপের সূত্র: $L = M + (V \\times VC) = 4.5\\text{ cm} + (6 \\times 0.005\\text{ cm}) = 4.530\\text{ cm}$।"
            },
            {
                "id": "pred_phy_1st_01_10",
                "stem": "পৃষ্ঠটানের ($T$) মাত্রা সমীকরণ নিচের কোন রাশির মাত্রা সমীকরণের অনুরূপ?",
                "options": ["স্প্রিং ধ্রুবক ($k$)", "সান্দ্রতা গুণাঙ্ক ($\\eta$)", "ঘাত বল ($F$)", "টর্ক ($\\tau$)"],
                "answer": "A",
                "type_ref": "Type 1: মাত্রা সমীকরণ ও সমমাত্রিকতার নীতি",
                "trap_alert": "পৃষ্ঠটান ($T=F/l$) বলের ঘাত বা সান্দ্রতার সাথে মিলিয়ে ফেলা।",
                "speed_hack": "পৃষ্ঠটান $T = \\frac{F}{L} \\implies \\frac{MLT^{-2}}{L} = [MT^{-2}]$। স্প্রিং ধ্রুবক $k = \\frac{F}{x} \\implies \\frac{MLT^{-2}}{L} = [MT^{-2}]$। উভয়ই $[MT^{-2}]$।",
                "explanation": "পৃষ্ঠটান $T = F/l$ এবং স্প্রিং ধ্রুবক $k = F/x$; উভয়েরই মাত্রা সমীকরণ $\\frac{MLT^{-2}}{L} = [MT^{-2}]$ এবং একক $\\text{N/m}$।"
            },
            {
                "id": "pred_phy_1st_01_11",
                "stem": "কাজ ($W$) এবং টর্কের ($\\tau$) মাত্রা সমীকরণ উভয়ই $[ML^2T^{-2}]$ হওয়া সত্ত্বেও তাদের মূল ভৌত পার্থক্য কোনটি?",
                "options": [
                    "কাজ একটি স্কেলার রাশি এবং টর্ক একটি ভেক্টর রাশি",
                    "কাজের একক নিউটন-মিটার কিন্তু টর্কের কোনো একক নেই",
                    "টর্কের মাত্রা কাজের চেয়ে এক মাত্রা কম",
                    "উভয়ই ভেক্টর রাশি কিন্তু দিক বিপরীত"
                ],
                "answer": "A",
                "type_ref": "Type 1: মাত্রা সমীকরণ ও সমমাত্রিকতার নীতি",
                "trap_alert": "উভয়ের মাত্রা ও একক ($\text{N}\cdot\text{m}$) এক হওয়ায় উভয়কেই স্কেলার ভাবা।",
                "speed_hack": "কাজ ডট গুণন ($W = \\vec{F}\\cdot\\vec{s}$ $\\implies$ স্কেলার); টর্ক ক্রস গুণন ($\\vec{\\tau} = \\vec{r}\\times\\vec{F}$ $\\implies$ ভেক্টর)।",
                "explanation": "কাজ বল ও সরণের স্কেলার গুণফল ($W = \\vec{F}\\cdot\\vec{d}$), তাই স্কেলার রাশি। টর্ক অবস্থান ভেক্টর ও প্রযুক্ত বলের ভেক্টর গুণফল ($\\vec{\\tau} = \\vec{r}\\times\\vec{F}$), তাই এটি একটি অক্ষীয় ভেক্টর রাশি।"
            },
            {
                "id": "pred_phy_1st_01_12",
                "stem": "একটি ভৌত রাশি $Z = \\frac{A^2 B^3}{C}$ দ্বারা সংজ্ঞায়িত। $A, B$ ও $C$ পরিমাপে শতকরা ত্রুটি যথাক্রমে $1\\%, 2\\%$ এবং $3\\%$ হলে $Z$ এর শতকরা ত্রুটি কত?",
                "options": ["$11\\%$", "$7\\%$", "$5\\%$", "$12\\%$"],
                "answer": "A",
                "type_ref": "Type 3: পরিমাপে শতকরা ত্রুটি ও ঘাতজনিত বিস্তার",
                "trap_alert": "হরের $C$ এর ত্রুটি বিয়োগ করে ফেলা ($2(1) + 3(2) - 3 = 5$ দাগানো)। ত্রুটি সর্বদা যোগ হয়!",
                "speed_hack": "ঘাত গুণ করে সর্বদা যোগ: $2(1\\%) + 3(2\\%) + 1(3\\%) = 2 + 6 + 3 = 11\\%$। ৩ সেকেন্ডে সমাধান।",
                "explanation": "ত্রুটির সংমিশ্রণ সূত্রানুসারে শতকরা ত্রুটি: $\\frac{\\Delta Z}{Z} \\times 100\\% = 2\\frac{\\Delta A}{A} + 3\\frac{\\Delta B}{B} + 1\\frac{\\Delta C}{C} = 2(1\\%) + 3(2\\%) + 3\\% = 2\\% + 6\\% + 3\\% = 11\\%$।"
            }
        ]
    }
    chapters.append(ch01)

    # -------------------------------------------------------------
    # 2-6: Chapters phy_1st_02 to phy_1st_06 from gen_physics_predictors
    # -------------------------------------------------------------
    source_p1 = gen_physics_predictors.get_physics_predictors()
    mapping = {
        "phy_vector": ("phy_1st_02", "ভেক্টর (Vector)", "১ম পত্র", "অধ্যায় ০২"),
        "phy_dynamics": ("phy_1st_03", "গতিবিদ্যা ও প্রক্ষেপক (Dynamics & Projectile)", "১ম পত্র", "অধ্যায় ০৩"),
        "phy_newtonian": ("phy_1st_04", "নিউটনীয় বলবিদ্যা (Newtonian Mechanics)", "১ম পত্র", "অধ্যায় ০৪"),
        "phy_work_energy": ("phy_1st_05", "কাজ, শক্তি ও ক্ষমতা (Work, Energy & Power)", "১ম পত্র", "অধ্যায় ০৫"),
        "phy_gravitation": ("phy_1st_06", "মহাকর্ষ ও অভিকর্ষ (Gravitation & Gravity)", "১ম পত্র", "অধ্যায় ০৬")
    }

    for ch in source_p1:
        old_id = ch["chapter_id"]
        if old_id in mapping:
            new_id, new_title, paper, ch_no = mapping[old_id]
            clean_preds = []
            for i, q in enumerate(ch["predictors"]):
                q_copy = dict(q)
                # Assign pristine unique ID
                q_copy["id"] = f"pred_{new_id}_{i+1:02d}"
                # Ensure explanation is complete
                if "explanation" not in q_copy or not q_copy["explanation"]:
                    if q_copy["id"] == "pred_phy_1st_03_04":
                        q_copy["explanation"] = "বেগের $1/n$ অংশ হারালে মোট তক্তা ভেদ করার শর্টকাট সূত্র $N = \\frac{n^2}{2n - 1}$। এখানে $n=3$, তাই $N = \\frac{3^2}{2(3)-1} = \\frac{9}{5} = 1.8$ টি তক্তা। ১ম তক্তা ইতোমধ্যে ভেদ করায় আরও $1.8 - 1 = 0.8$ টি বা পূর্ণাঙ্গ ১টি তক্তা ভেদ করতে পারবে।"
                    elif q_copy["id"] == "pred_phy_1st_05_10":
                        q_copy["explanation"] = "শক্তির সংরক্ষণশীলতা নীতি অনুসারে কোনো বস্তু মুক্তভাবে পড়ার সময় মোট যান্ত্রিক শক্তি ধ্রুব থাকে ($E = E_k + E_p = \\text{const}$)। ভূমিতে পৌঁছানোর ঠিক পূর্বমুহূর্তে উচ্চতা $h = 0$ হওয়ায় সমস্ত বিভব শক্তি গতিশক্তিতে রূপান্তরিত হয়, ফলে সম্পূর্ণ শক্তিই গতিশক্তি।"
                    elif q_copy["id"] == "pred_phy_1st_05_15":
                        q_copy["explanation"] = "ঘর্ষণ বল ও সান্দ্র বলের বিরুদ্ধে কৃতকাজ বস্তুর মধ্যে সঞ্চিত থাকে না, বরং তা তাপে অপচয় হয় এবং আদি অবস্থায় ফিরিয়ে আনা যায় না। তাই ঘর্ষণ বল অসংরক্ষণশীল বল। অপরদিকে মহাকর্ষ, স্থির তড়িৎ ও স্প্রিং বল সংরক্ষণশীল বল।"
                    else:
                        q_copy["explanation"] = q_copy.get("speed_hack", "সঠিক সমীকরণ প্রয়োগ করে সমাধান করা হলো।")
                clean_preds.append(q_copy)

            chapters.append({
                "chapter_id": new_id,
                "chapter_title": new_title,
                "subject": "Physics",
                "paper": paper,
                "chapter_no": ch_no,
                "predictors": clean_preds
            })

    return chapters

if __name__ == '__main__':
    ch_list = get_part1_chapters()
    total = sum(len(c['predictors']) for c in ch_list)
    print(f"curate_physics_p1: {len(ch_list)} chapters, {total} MCQs generated.")
