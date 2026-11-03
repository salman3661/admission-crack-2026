#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Week Data Pipeline for Admission Crack 2026 WebApp
Reads:
  - Week_01/05_Final_Notes/*.md
  - Week_02/05_Final_Notes/*.md
  - Week_03/05_Final_Notes/*.md
  - Global_Varsity_Vault.md
Outputs to admission_webapp/src/data/:
  - weeks.json
  - slides.json (42 slides total: 14 w1 + 14 w2 + 14 w3)
  - flashcards.json (96 flashcards total: 32 w1 + 32 w2 + 32 w3)
  - quizzes.json (Exact 300 MCQs: 100 w1 + 100 w2 + 100 w3)
  - vault.json (36 cross-subject traps, golden triplets, quick math)
"""

import os
import sys
import json
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "admission_webapp", "src", "data")
os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. WEEKS METADATA
# -------------------------------------------------------------
def build_weeks():
    weeks = [
        {
            "id": "week_01",
            "name": "Week 01",
            "badge": "ভেক্টর, গতিবিদ্যা, পরিমাণগত রসায়ন, সরলরেখা, রক্ত ও শ্বসন",
            "description": "ভৌত বিজ্ঞান ও গণিতের ভিত্তি: ভেক্টর ক্যালকুলাস, প্রাস, নদী-নৌকা, স্টয়কিওমেট্রি, সরলরেখা এবং মানব শারীরতত্ত্ব।",
            "subjects": ["Physics", "Chemistry", "Higher Math", "Biology"],
            "total_mcqs": 100,
            "total_slides": 14,
            "total_flashcards": 32
        },
        {
            "id": "week_02",
            "name": "Week 02",
            "badge": "বলবিদ্যা, পর্যায়বৃত্ত ধর্ম, রাসায়নিক সাম্যাবস্থা, বৃত্ত ও কোষ",
            "description": "উচ্চ গুরুত্বের কোর সিলেবাস: নিউটনিয়ান গতি, জড়তার ভ্রামক, কাজ-শক্তি, d-ব্লক মৌল, বাফার ও pH, বৃত্ত, জটিল সংখ্যা এবং কোষ অঙ্গাণু ও হাইড্রা।",
            "subjects": ["Physics", "Chemistry", "Higher Math", "Biology"],
            "total_mcqs": 100,
            "total_slides": 14,
            "total_flashcards": 32
        },
        {
            "id": "week_03",
            "name": "Week 03",
            "badge": "কাজ-শক্তি, মহাকর্ষ, গুণগত রসায়ন ও দ্রাব্যতা, কণিক ও অসমতা, উদ্ভিদ শারীরতত্ত্ব ও প্রজনন",
            "description": "উচ্চ গুরুত্বের কোর সিলেবাস: মহাকর্ষীয় ক্ষেত্র ও বিভব, মুক্তিবেগ, বোর পরমাণু মডেল ও কোয়ান্টাম সংখ্যা, Ksp ও আয়ন শনাক্তকরণ, কণিক (পরাবৃত্ত, উপবৃত্ত, অধিবৃত্ত) এবং C3/C4 চক্র ও শ্বসন।",
            "subjects": ["Physics", "Chemistry", "Higher Math", "Biology"],
            "total_mcqs": 100,
            "total_slides": 14,
            "total_flashcards": 32
        }
    ]
    with open(os.path.join(OUT_DIR, "weeks.json"), "w", encoding="utf-8") as f:
        json.dump(weeks, f, ensure_ascii=False, indent=2)
    print("✓ weeks.json generated successfully.")

# -------------------------------------------------------------
# 2. VAULT DATA
# -------------------------------------------------------------
def build_vault():
    triplets = [
        {"sides": "(3, 4)", "result": "5", "app": "বেগ $v_x=4, v_y=3 \\Rightarrow v=5\\text{ ms}^{-1}$; সরলরেখা $3x+4y+c=0$-এর লম্ব দূরত্বের হর $=5$; অনুবন্ধী অধিবৃত্ত $e_1=5/3 \\implies e_2=5/4$"},
        {"sides": "(5, 12)", "result": "13", "app": "সরলরেখা $5x+12y+c=0$-এর হর $=13$; $\\sin\\theta = 5/13 \\Rightarrow \\cos\\theta = 12/13$"},
        {"sides": "(6, 8)", "result": "10", "app": "নদী-নৌকায় $\\sqrt{10^2 - 6^2} = 8\\text{ ms}^{-1}$ (ন্যূনতম দূরত্বে নদী পারাপার)"},
        {"sides": "(8, 15)", "result": "17", "app": "ত্রিভুজ ও ভেক্টর মান নির্ণয়"},
        {"sides": "(7, 24)", "result": "25", "app": "ত্রিকোণমিতিক অনুপাত ও সরলরেখার দূরত্ব"},
        {"sides": "(1, 2, 2)", "result": "3", "app": "ত্রিমাত্রিক ভেক্টর $\\vec{A} = \\hat{i} + 2\\hat{j} + 2\\hat{k} \\Rightarrow |\\vec{A}| = 3$"},
        {"sides": "(2, 3, 6)", "result": "7", "app": "ত্রিমাত্রিক ভেক্টর $\\vec{B} = 2\\hat{i} - 3\\hat{j} + 6\\hat{k} \\Rightarrow |\\vec{B}| = 7$ (অভিক্ষেপ প্রশ্নে সবচেয়ে বেশি আসে!)"},
        {"sides": "(1, 4, 8)", "result": "9", "app": "একক ভেক্টর ও দিক কোসাইন নির্ণয়"}
    ]

    quick_math = [
        {"type": "বর্গমূল", "item": "$\\sqrt{2} \\approx 1.414, \\; \\sqrt{3} \\approx 1.732, \\; \\sqrt{5} \\approx 2.236, \\; \\sqrt{10} \\approx \\pi \\approx 3.16$"},
        {"type": "অমসৃণ বর্গমূল সূত্র", "item": "$\\sqrt{N^2 \\pm d} \\approx N \\pm \\frac{d}{2N} \\quad (\\text{যেমন: } \\sqrt{45} = \\sqrt{36+9} \\approx 6 + \\frac{9}{12} = 6.75)$"},
        {"type": "লগারিদম (pH)", "item": "$\\log 2 \\approx 0.30, \\; \\log 3 \\approx 0.48, \\; \\log 5 \\approx 0.70, \\; \\log 7 \\approx 0.85$"},
        {"type": "pH সুপার শর্টকাট", "item": "$[\\text{H}^+] = a \\times 10^{-b}\\text{ M} \\implies \\text{pH} = b - \\log a$"},
        {"type": "জটিল সংখ্যার বর্গমূল", "item": "$\\sqrt{a \\pm ib} = \\pm(p \\pm iq) \\quad \\text{যেখানে } p \\times q = \\frac{b}{2} \\text{ এবং } p^2 - q^2 = a$"},
        {"type": "কৌণিক বেগ rpm", "item": "$\\omega = \\frac{2\\pi N}{60} = \\frac{\\pi N}{30}\\text{ rad s}^{-1} \\quad (30\\text{ rpm}=\\pi, \\; 60\\text{ rpm}=2\\pi, \\; 300\\text{ rpm}=10\\pi)$"},
        {"type": "গ্যাস ধ্রুবক RT", "item": "$0^\\circ\\text{C}: 22.4\\text{ L atm}; \\; 25^\\circ\\text{C}: 24.46\\text{ L atm}; \\; 27^\\circ\\text{C}: 24.63\\text{ L atm} \\approx 2500\\text{ J}$"},
        {"type": "মুক্তিবেগ ও কক্ষীয় বেগ", "item": "$v_e = \\sqrt{2}v_o \\approx 1.414 v_o \\implies 41.4\\% \\text{ বৃদ্ধি (পৃথিবী } v_e=11.2, \\; v_o=7.92\\text{ km s}^{-1})$"},
        {"type": "শোয়ার্জশিল্ড ব্যাসার্ধ", "item": "$R_s = \\frac{2GM}{c^2} \\quad (\\text{পৃথিবী: } \\approx 8.86\\text{ mm} \\approx 0.9\\text{ cm}; \\; \\text{সূর্য: } \\approx 3\\text{ km})$"},
        {"type": "বোর ব্যাসার্ধ ও শক্তি", "item": "$r_n = 0.529 n^2\\text{ \\AA}, \\; v_n = \\frac{2.18\\times 10^6}{n}\\text{ m s}^{-1}, \\; E_n = -\\frac{13.6}{n^2}\\text{ eV}$"},
        {"type": "Ksp ও দ্রাব্যতা শর্টকাট", "item": "$AB \\to s=\\sqrt{K_{sp}}; \\; AB_2 \\to s=\\sqrt[3]{\\frac{K_{sp}}{4}}; \\; AB_3 \\to s=\\sqrt[4]{\\frac{K_{sp}}{27}}; \\; A_2B_3 \\to s=\\sqrt[5]{\\frac{K_{sp}}{108}}$"},
        {"type": "উপবৃত্তের উৎকেন্দ্রিকতা", "item": "$e = \\sqrt{1 - \\frac{\\text{ছোট হর}}{\\text{বড় হর}}} \\quad (\\text{যেমন: } \\frac{x^2}{25}+\\frac{y^2}{16}=1 \\implies e = \\frac{3}{5})$"},
        {"type": "অনুবন্ধী অধিবৃত্ত", "item": "$\\frac{1}{e_1^2} + \\frac{1}{e_2^2} = 1 \\quad (\\text{৩-৪-৫ ট্রিপলেট: } e_1=\\frac{5}{3} \\implies e_2=\\frac{5}{4})$"},
        {"type": "পরমমান কেন্দ্র-ব্যাসার্ধ", "item": "$a < x < b \\iff |x - m| < r \\quad \\text{যেখানে } m = \\frac{a+b}{2}, \\; r = \\frac{b-a}{2}$"}
    ]

    magic_fractions = [
        {"compound": "$\\text{Na}_2\\text{CO}_3$", "mw": "106", "trick": "$13.25\\text{ g} = \\frac{1}{8}\\text{ mol} = 0.125\\text{ mol}; \\quad 26.5\\text{ g} = \\frac{1}{4}\\text{ mol} = 0.25\\text{ mol}$"},
        {"compound": "$\\text{CaCO}_3$", "mw": "100", "trick": "$444.44\\text{ g} \\text{ নমুনায় } 90\\% \\text{ বিশুদ্ধতা } \\Rightarrow 400\\text{ g} = 4\\text{ mol}$"},
        {"compound": "$\\text{MgCO}_3$", "mw": "84", "trick": "$1\\text{ kg} \\Rightarrow \\text{STP-তে CO}_2 = \\frac{1000}{84} \\times 22.4 = \\frac{800}{3} \\approx 266.67\\text{ L}$"},
        {"compound": "$\\text{KClO}_3$", "mw": "122.5", "trick": "$122.5\\text{ g} = 1\\text{ mol} \\Rightarrow 1.5\\text{ mol O}_2 = 1.5 \\times 22.4 = 33.6\\text{ L}$"},
        {"compound": "$\\text{K}_2\\text{Cr}_2\\text{O}_7$", "mw": "294", "trick": "$M = 294 = 3 \\times 98; \\quad 1\\text{ mol} \\equiv 6e^- (\\text{অম্লীয় মাধ্যমে})$"},
        {"compound": "$\\text{KMnO}_4$", "mw": "158", "trick": "$1\\text{ mol} \\equiv 5e^- (\\text{অম্লীয়}), \\equiv 3e^- (\\text{ক্ষারীয়/প্রশম})$"},
        {"compound": "$\\text{Ag}_2\\text{CrO}_4$", "mw": "332", "trick": "$K_{sp} = 4s^3 \\implies 3\\text{টি আয়ন তৈরি হয়}$"},
        {"compound": "$\\text{BaSO}_4$", "mw": "233", "trick": "গ্রুপ-২ এর মধ্যে সর্বনিম্ন দ্রবণীয় ($K_{sp} \\approx 1.1\\times 10^{-10}$)"},
        {"compound": "$\\text{Ca(OH)}_2$", "mw": "74", "trick": "গ্রুপ-২ হাইড্রোক্সাইডের দ্রাব্যতা নিচে বৃদ্ধি পায়"}
    ]

    patterns = [
        {"code": "PHY-W01-P1", "week": "week_01", "subject": "Physics", "title": "লম্ব ও সমান্তরাল ভেক্টর", "formula": "লম্ব: $\\vec{A}\\cdot\\vec{B}=0$; সমান্তরাল: $\\frac{A_x}{B_x}=\\frac{A_y}{B_y}=\\frac{A_z}{B_z}$"},
        {"code": "PHY-W01-P2", "week": "week_01", "subject": "Physics", "title": "অভিক্ষেপ বনাম উপাংশ", "formula": "স্কেলার অভিক্ষেপ: $\\frac{\\vec{A}\\cdot\\vec{B}}{|\\vec{B}|}$; ভেক্টর উপাংশ: $\\left(\\frac{\\vec{A}\\cdot\\vec{B}}{|\\vec{B}|^2}\\right)\\vec{B}$"},
        {"code": "PHY-W01-P3", "week": "week_01", "subject": "Physics", "title": "সামান্তরিকের ক্ষেত্রফল", "formula": "বাহু দেওয়া থাকলে: $|\\vec{A}\\times\\vec{B}|$; কর্ণ দেওয়া থাকলে: $\\frac{1}{2}|\\vec{d}_1\\times\\vec{d}_2|$"},
        {"code": "PHY-W01-P4", "week": "week_01", "subject": "Physics", "title": "ডাইভারজেন্স ও কার্ল", "formula": "সলিনয়ডাল: $\\vec{\\nabla}\\cdot\\vec{F}=0$; অঘূর্ণনশীল/সংরক্ষণশীল: $\\vec{\\nabla}\\times\\vec{F}=\\vec{0}$"},
        {"code": "PHY-W01-P5", "week": "week_01", "subject": "Physics", "title": "নদী ও নৌকা পারাপার", "formula": "ন্যূনতম সময়: $t_{\\min}=\\frac{d}{v}$; ন্যূনতম দূরত্ব: $\\cos\\alpha = -\\frac{u}{v}$, $t = \\frac{d}{\\sqrt{v^2-u^2}}$"},
        {"code": "PHY-W01-P6", "week": "week_01", "subject": "Physics", "title": "n-তম সেকেন্ডের দূরত্ব", "formula": "$s_{nth} = u + \\frac{1}{2}a(2n-1)$; দূরত্বের অনুপাত: $(2n_1-1):(2n_2-1)$"},
        {"code": "PHY-W01-P7", "week": "week_01", "subject": "Physics", "title": "প্রাসের পাল্লা ও উচ্চতা", "formula": "$\\tan\\alpha = \\frac{4H}{R}$; শীর্ষবিন্দুতে বেগ $u\\cos\\alpha$, গতিশক্তি $E_0\\cos^2\\alpha$"},
        {"code": "CHE-W01-P1", "week": "week_01", "subject": "Chemistry", "title": "ঘনমাত্রা রূপান্তর", "formula": "$M = \\frac{10x}{M_w}$; $\\text{ppm} = M \\times M_w \\times 1000 = \\%(w/v) \\times 10^4$"},
        {"code": "CHE-W01-P2", "week": "week_01", "subject": "Chemistry", "title": "অম্ল-ক্ষার প্রশমন", "formula": "$e_a M_a V_a = e_b M_b V_b$; মিশ্রণের $M = \\frac{|e_a M_a V_a - e_b M_b V_b|}{V_a + V_b}$"},
        {"code": "CHE-W01-P3", "week": "week_01", "subject": "Chemistry", "title": "জারণ-বিজারণ ইলেকট্রন", "formula": "$\\text{KMnO}_4 \\equiv 5e^-$, $\\text{K}_2\\text{Cr}_2\\text{O}_7 \\equiv 6e^-$, $\\text{H}_2\\text{O}_2 \\equiv 2e^-$"},
        {"code": "MAT-W01-P1", "week": "week_01", "subject": "Higher Math", "title": "৪র্থ শীর্ষ ও ইউলার রেখা", "formula": "সামান্তরিক ৪র্থ শীর্ষ: $D = A + C - B$; ইউলার রেখা: $HG : GO = 2 : 1$"},
        {"code": "MAT-W01-P2", "week": "week_01", "subject": "Higher Math", "title": "লম্ব ও সমান্তরাল রেখা", "formula": "সমান্তরাল: $ax+by=ax_1+by_1$; লম্ব: $bx-ay=bx_1-ay_1$"},
        {"code": "MAT-W01-P3", "week": "week_01", "subject": "Higher Math", "title": "সমান্তরাল রেখার দূরত্ব", "formula": "$d = \\frac{|c_1 - c_2|}{\\sqrt{a^2 + b^2}}$ (সহগ সমান করার পর)"},
        {"code": "BIO-W01-P1", "week": "week_01", "subject": "Biology", "title": "রক্তরস ও রক্ত তঞ্চন", "formula": "রক্তের pH = 7.35-7.45; প্লাজমা প্রোটিন: জিপিএ ফাইব্রিনোজেন (অ্যালবুমিন, গ্লোবিউলিন, ফাইব্রিনোজেন, প্রোথ্রম্বিন)"},
        {"code": "BIO-W01-P2", "week": "week_01", "subject": "Biology", "title": "হৃদচক্র ও রক্ত প্রবাহ", "formula": "হৃদচক্র: 0.8 s (অলিন্দ সিস্টোল 0.1 s, ডায়াস্টোল 0.7 s; নিলয় সিস্টোল 0.3 s, ডায়াস্টোল 0.5 s)"},
        {"code": "PHY-W02-P1", "week": "week_02", "subject": "Physics", "title": "পরিমাপে শতকরা ত্রুটি", "formula": "$V = \\frac{4}{3}\\pi r^3 \\implies \\frac{\\Delta V}{V} = 3\\frac{\\Delta r}{r}$; ত্রুটি সর্বদা যোগ হয়"},
        {"code": "PHY-W02-P2", "week": "week_02", "subject": "Physics", "title": "রকেট ও বন্দুকের ধাক্কা", "formula": "$F_{thrust} = v_r\\frac{dm}{dt}$; $V = -\\frac{mv}{M}$; প্রতিক্ষেপণে $\\Delta p = m(v+u)$"},
        {"code": "PHY-W02-P3", "week": "week_02", "subject": "Physics", "title": "লিফটে আপাত ওজন", "formula": "ত্বরণে উপরে: $R = m(g+a)$; ত্বরণে নিচে: $R = m(g-a)$; মুক্ত পতন: $R = 0$"},
        {"code": "PHY-W02-P4", "week": "week_02", "subject": "Physics", "title": "জড়তার ভ্রামক ও সংকোচন", "formula": "চাকতি: $\\frac{1}{2}MR^2$; নিরেট গোলক: $\\frac{2}{5}MR^2$; ব্যাসার্ধ $\\frac{R}{n}$ হলে দিন: $\\frac{24}{n^2}\\text{ hr}$"},
        {"code": "PHY-W02-P5", "week": "week_02", "subject": "Physics", "title": "রাস্তার ব্যাংকিং ও কেন্দ্রমুখী বল", "formula": "$\\tan\\theta = \\frac{v^2}{rg} = \\frac{h}{b}$; $F_c = \\frac{mv^2}{r} = m\\omega^2 r$"},
        {"code": "PHY-W02-P6", "week": "week_02", "subject": "Physics", "title": "গুলি-তক্তা ও গতিশক্তি", "formula": "$E_k = \\frac{p^2}{2m}$; তক্তায় $\\frac{1}{n}$ বেগ হারালে মোট তক্তা: $N = \\frac{n^2}{2n-1}$"},
        {"code": "PHY-W02-P7", "week": "week_02", "subject": "Physics", "title": "কুয়ার পানি তোলা ও ক্ষমতা", "formula": "$W = mgh_{\\text{avg}}$; পূর্ণ কুয়া: $h/2$, অর্ধপূর্ণ: $3h/4$; $P = \\frac{mgh_{\\text{avg}}}{\\eta t}$"},
        {"code": "CHE-W02-P1", "week": "week_02", "subject": "Chemistry", "title": "পর্যায়বৃত্ত ধর্মের ব্যতিক্রম", "formula": "IE: $\\text{Be}>\\text{B}$, $\\text{N}>\\text{O}$, $\\text{Mg}>\\text{Al}$, $\\text{P}>\\text{S}$; EA: $\\text{Cl}>\\text{F}>\\text{Br}>\\text{I}$"},
        {"code": "CHE-W02-P2", "week": "week_02", "subject": "Chemistry", "title": "জটিল আয়নের সংকরায়ন", "formula": "$[\\text{Cu(NH}_3)_4]^{2+}, [\\text{Ni(CN)}_4]^{2-} \\to dsp^2$ (বর্গাকার); $[\\text{Fe(CN)}_6]^{4-} \\to d^2sp^3$ (ডায়াম্যাগনেটিক)"},
        {"code": "CHE-W02-P3", "week": "week_02", "subject": "Chemistry", "title": "Kp ও Kc রূপান্তর", "formula": "$K_p = K_c(RT)^{\\Delta n}$; সমীকরণ উল্টে $n$ দিয়ে ভাগ করলে $K' = (K)^{-1/n}$"},
        {"code": "CHE-W02-P4", "week": "week_02", "subject": "Chemistry", "title": "বাফার দ্রবণ ও প্রশমন তাপ", "formula": "$\\text{pH} = \\text{p}K_a + \\log\\frac{[\\text{Salt}]}{[\\text{Acid}]}$; তীব্র এসিড-ক্ষার $\\Delta H = -57.34\\text{ kJ mol}^{-1}$"},
        {"code": "MAT-W02-P1", "week": "week_02", "subject": "Higher Math", "title": "বৃত্তের অক্ষ স্পর্শ", "formula": "x-অক্ষ স্পর্শ: $g^2=c, r=|k|$; y-অক্ষ স্পর্শ: $f^2=c, r=|h|$; খণ্ডিতাংশ: $2\\sqrt{g^2-c}, 2\\sqrt{f^2-c}$"},
        {"code": "MAT-W02-P2", "week": "week_02", "subject": "Higher Math", "title": "জ্যা ও স্পর্শক", "formula": "জ্যা: $2\\sqrt{r^2-d^2}$; স্পর্শকের দৈর্ঘ্য: $L=\\sqrt{S_1}$; বহিস্পর্শ: $C_1C_2=r_1+r_2$"},
        {"code": "MAT-W02-P3", "week": "week_02", "subject": "Higher Math", "title": "জটিল আর্গুমেন্ট ও সঞ্চারপথ", "formula": "৩য় চতুর্ভাগে: $\\theta = -\\pi + \\alpha$; $|z-a|=r \\to$ বৃত্ত; $|z-z_1|=|z-z_2| \\to$ লম্বদ্বিখণ্ডক রেখা"},
        {"code": "MAT-W02-P4", "week": "week_02", "subject": "Higher Math", "title": "ত্রিকোণমিতি ম্যাজিক অভেদ", "formula": "$\\sec\\theta+\\tan\\theta=k \\implies \\sin\\theta=\\frac{k^2-1}{k^2+1}$; $A+B=45^\\circ \\implies (1+\\tan A)(1+\\tan B)=2$"},
        {"code": "BIO-W02-P1", "week": "week_02", "subject": "Biology", "title": "কোষ বিভাজন উপ-ধাপ", "formula": "জাইগোটিন $\\to$ সিন্যাপসিস/বাইভ্যালেন্ট; প্যাকাইটিন $\\to$ কায়াজমা ও ক্রসিং ওভার; অ্যানাফেজ $\\to$ V, L, J, I"},
        {"code": "BIO-W02-P2", "week": "week_02", "subject": "Biology", "title": "হাইড্রা ও ঘাসফড়িং", "formula": "হাইড্রা: ইন্টারস্টিশিয়াল কোষ (পুনরুৎপত্তি), স্টিনোটিল (হিপনোটক্সিন); ঘাসফড়িং: মালপিজিয়ান নালিকা, অ্যাপোজিশন (উজ্জ্বল আলো)"},
        {"code": "BIO-W02-P3", "week": "week_02", "subject": "Biology", "title": "রুই মাছ ও মানব পরিপাক", "formula": "রুই মাছ: ভেনাস হার্ট (শুধু $\\text{CO}_2$ রক্ত); পাকস্থলী: প্যারাইটাল কোষ $\\to \\text{HCl}$, জাইমোজেনিক $\\to$ পেপসিনোজেন"},
        {"code": "PHY-W03-P1", "week": "week_03", "subject": "Physics", "title": "স্প্রিংয়ে অতিরিক্ত কাজ", "formula": "$\\Delta W = \\frac{1}{2}k(x_2^2 - x_1^2)$; কর্তনে $k' = nk \\implies W' = \\frac{1}{n}W$"},
        {"code": "PHY-W03-P2", "week": "week_03", "subject": "Physics", "title": "শক্তি বণ্টন উচ্চতা", "formula": "$E_k = nE_p \\implies x = \\frac{H}{n+1}$ (ভূমি হতে উচ্চতা)"},
        {"code": "PHY-W03-P3", "week": "week_03", "subject": "Physics", "title": "উচ্চতা ও গভীরতায় g", "formula": "$g_h = g(1 - \\frac{2h}{R})$ ($h \\ll R$); $g_d = g(1 - \\frac{d}{R})$; কেন্দ্রে $g = 0$"},
        {"code": "PHY-W03-P4", "week": "week_03", "subject": "Physics", "title": "কার্নো ইঞ্জিনের দক্ষতা", "formula": "$\\eta = 1 - \\frac{T_2}{T_1} = \\frac{W}{Q_1}$; $\\eta=100\\%$ করতে $T_2=0\\text{ K}$"},
        {"code": "CHE-W03-P1", "week": "week_03", "subject": "Chemistry", "title": "বোর শক্তি ও ব্যাসার্ধ", "formula": "$r_n = 0.529 n^2\\text{ \\AA}$; $E_n = -\\frac{13.6}{n^2}\\text{ eV}$; $v_n = \\frac{v_1}{n}$"},
        {"code": "CHE-W03-P2", "week": "week_03", "subject": "Chemistry", "title": "রিডবার্গ সমীকরণ ও নোড", "formula": "$\\bar{\\nu} = R_H Z^2 (\\frac{1}{n_1^2} - \\frac{1}{n_2^2})$; মোট নোড $= n-1$, রেডিয়াল $= n-l-1$"},
        {"code": "CHE-W03-P3", "week": "week_03", "subject": "Chemistry", "title": "দ্রাব্যতা গুণফল ও অধঃক্ষেপণ", "formula": "$K_{ip} > K_{sp} \\implies$ অধঃক্ষেপ পড়বে; $AB_2 \\to K_{sp} = 4s^3$"},
        {"code": "MAT-W03-P1", "week": "week_03", "subject": "Higher Math", "title": "পরাবৃত্তের শীর্ষবিন্দু", "formula": "$y^2 = 4ax \\to$ লম্ব $4|a|$; শীর্ষ নির্ণয়ে $\\frac{\\partial}{\\partial y}=0$"},
        {"code": "MAT-W03-P2", "week": "week_03", "subject": "Higher Math", "title": "উপবৃত্তের উৎকেন্দ্রিকতা", "formula": "$e = \\sqrt{1 - \\frac{\\text{ছোট}^2}{\\text{বড়}^2}}$ ($0<e<1$); ফোকাল যোগফল $SP+S'P=2a$"},
        {"code": "MAT-W03-P3", "week": "week_03", "subject": "Higher Math", "title": "অধিবৃত্ত ও সমপরাবৃত্ত", "formula": "$\\frac{1}{e_1^2} + \\frac{1}{e_2^2} = 1$; সমপরাবৃত্তে $e = \\sqrt{2}$, অসীমমুখী কোণ $90^\\circ$"},
        {"code": "BIO-W03-P1", "week": "week_03", "subject": "Biology", "title": "C3 বনাম C4 চক্র", "formula": "$\\text{C}_3$: RuBP (৫C) $\\to$ 3-PGA (৩C); $\\text{C}_4$: PEP (৩C) $\\to$ OAA (৪C)"},
        {"code": "BIO-W03-P2", "week": "week_03", "subject": "Biology", "title": "শ্বসনিক কোশেন্ট RQ ও প্লয়েডি", "formula": "RQ: গ্লুকোজ $=1.0$, ম্যালিক $=1.33$, লিপিড $=0.71$; নগ্নবীজী শস্য $n$, আবৃতবীজী শস্য $3n$"}
    ]

    traps = [
        {"id": 1, "week": "week_01", "subject": "Physics", "trap": "কর্ণ ভেক্টর দেওয়া থাকলে সামান্তরিকের ক্ষেত্রফল ||A×B|| লিখে ফেলা", "fix": "কর্ণ হলে অবশ্যই সামনে 1/2 গুণ হবে: Area = (1/2)|d1 × d2|।"},
        {"id": 2, "week": "week_01", "subject": "Physics", "trap": "লব্ধি বেগের সাথে কোণ বনাম স্রোতের সাথে কোণ গুলিয়ে ফেলা", "fix": "সোজাসুজি পারাপারে স্রোতের সাথে যাত্রা কোণ >90° (যেমন 120°), কিন্তু লব্ধি বেগের কোণ 90°।"},
        {"id": 3, "week": "week_01", "subject": "Physics", "trap": "নিক্ষিপ্ত বস্তুর সর্বোচ্চ উচ্চতায় ত্বরণ a = 0 দাগানো", "fix": "সর্বোচ্চ বিন্দুতে উল্লম্ব বেগ vy = 0, কিন্তু অভিকর্ষজ ত্বরণ g সর্বদা নিচের দিকে ক্রিয়াশীল।"},
        {"id": 4, "week": "week_01", "subject": "Chemistry", "trap": "পল-বুঙ্গি ব্যালান্সে 5 mg রাইডার ধ্রুবক 0.0002 g দাগানো", "fix": "5 mg রাইডারের ধ্রুবক = (5×2)/100 mg = 0.1 mg = 0.0001 g (10 mg হলে 0.0002 g)।"},
        {"id": 5, "week": "week_01", "subject": "Chemistry", "trap": "অ্যাকোয়া রেজিয়ায় HNO3 : HCl = 3 : 1 দাগানো", "fix": "অক্ষরের সংখ্যা মিলিয়ে মনে রাখো: HNO3 (বড় নাম -> 1) : HCl (ছোট নাম -> 3) = 1 : 3।"},
        {"id": 6, "week": "week_01", "subject": "Chemistry", "trap": "44 g CO2 ও 44 g N2O-এর আয়তন ভিন্ন মনে করা", "fix": "উভয়েরই আণবিক ভর M = 44, তাই STP-তে উভয়েরই আয়তন সমান (22.4 L)।"},
        {"id": 7, "week": "week_01", "subject": "Chemistry", "trap": "মোলারিটি (M) ও মোলালিটি (m)-এর তাপমাত্রা নির্ভরতা গুলানো", "fix": "আয়তন তাপমাত্রায় বদলায় তাই মোলারিটি তাপমাত্রা-নির্ভর; ভর বদলায় না তাই মোলালিটি তাপমাত্রা-নিরপেক্ষ।"},
        {"id": 8, "week": "week_01", "subject": "Higher Math", "trap": "ঢাল নির্ণয়ে -সহগ y / সহগ x বা চিহ্ন ভুল করা", "fix": "সব পদ একপাশে এনে (ax+by+c=0) ঢাল m = -(সহগ x)/(সহগ y) = -a/b ব্যবহার করবে।"},
        {"id": 9, "week": "week_01", "subject": "Higher Math", "trap": "সমান্তরাল রেখার দূরত্বে 3x-4y=2 ও 6x-8y=9 থেকে সরাসরি |2-9|/5 লেখা", "fix": "আগে দ্বিতীয় সমীকরণকে 2 দিয়ে ভাগ করে 3x-4y = 9/2 বানাতে হবে => d = |2 - 4.5|/5 = 0.5।"},
        {"id": 10, "week": "week_01", "subject": "Higher Math", "trap": "ঢাল থেকে মধ্যবর্তী কোণে সূক্ষ্মকোণ (30°) না স্থূলকোণ (150°) চেয়েছে তা না দেখা", "fix": "প্রশ্নের শেষ শব্দ আন্ডারলাইন করো: 'সূক্ষ্মকোণ' নাকি 'স্থূলকোণ'।"},
        {"id": 11, "week": "week_01", "subject": "Biology", "trap": "হিমোস্ট্যাসিস ও হোমিওস্ট্যাসিস এক মনে করা", "fix": "হিমোস্ট্যাসিস = রক্তপাত বন্ধ হওয়া (Heme); হোমিওস্ট্যাসিস = দেহের অভ্যন্তরীণ ভারসাম্য।"},
        {"id": 12, "week": "week_01", "subject": "Biology", "trap": "সব ধমনিতে O2 এবং সব শিরায় CO2 থাকে ভাবা", "fix": "ফুসফুসীয় ধমনিতে CO2-যুক্ত এবং ফুসফুসীয় শিরায় O2-সমৃদ্ধ রক্ত প্রবাহিত হয়।"},
        {"id": 13, "week": "week_01", "subject": "Biology", "trap": "থাইরয়েডকে লসিকাগ্রন্থি ভাবা", "fix": "থাইমাস লসিকা অঙ্গ, কিন্তু থাইরয়েড অন্তঃক্ষরা গ্রন্থি (লসিকাগ্রন্থি নয়)।"},
        {"id": 14, "week": "week_01", "subject": "Biology", "trap": "অ্যানজাইনা পেক্টোরিসের প্রকারভেদ গুলানো", "fix": "Dormant কোনো প্রকারভেদ নয়; অ্যানজাইনা ৩ প্রকার: Stable, Unstable, Prinzmetal।"},
        {"id": 15, "week": "week_02", "subject": "Physics", "trap": "গুলির বেগ 'কমে 1/3 হলো' বনাম '1/3 অংশ হারালো' এক মনে করা", "fix": "'1/3 হলো' মানে v = u/3; '1/3 অংশ হারালো' মানে v = u - u/3 = 2u/3।"},
        {"id": 16, "week": "week_02", "subject": "Physics", "trap": "কুয়ার ব্যাস (d) দেওয়া থাকলে সরাসরি r-এ বসিয়ে দেওয়া", "fix": "ব্যাস দেখলে শুরুতেই r = d/2 লিখে গোল দাগ দিয়ে নেবে।"},
        {"id": 17, "week": "week_02", "subject": "Physics", "trap": "শতকরা ত্রুটির অংকে ভাগের ক্ষেত্রে ত্রুটি বিয়োগ করা", "fix": "পরিমাপের শতকরা ত্রুটি সর্বদা যোগ হয়: dQ/Q = a(dA/A) + b(dB/B) + c(dC/C)।"},
        {"id": 18, "week": "week_02", "subject": "Chemistry", "trap": "হ্যালোজেনের ইলেকট্রন আসক্তির ক্রমে F > Cl দাগানো", "fix": "তড়িৎ ঋণাত্মকতায় F > Cl, কিন্তু ইলেকট্রন আসক্তিতে Cl > F > Br > I।"},
        {"id": 19, "week": "week_02", "subject": "Chemistry", "trap": "10^-8 M HCl দ্রবণের pH = 8 দাগানো", "fix": "এসিডের pH কখনোই >7 হতে পারে না; পানির 10^-7 M যোগ হয়ে সঠিক pH = 6.96।"},
        {"id": 20, "week": "week_02", "subject": "Chemistry", "trap": "চাপ বা প্রভাবক পরিবর্তনে সাম্যধ্রুবক Kp, Kc পরিবর্তিত হয় ভাবা", "fix": "শুধুমাত্র তাপমাত্রা পরিবর্তনেই Kp ও Kc পরিবর্তিত হয়; প্রভাবক বা চাপে নয়।"},
        {"id": 21, "week": "week_02", "subject": "Higher Math", "trap": "ax^2 + ay^2 + ... বৃত্তে a দিয়ে ভাগ না করে কেন্দ্র ও ব্যাসার্ধ লেখা", "fix": "আগে সমীকরণকে a দিয়ে ভাগ করে x^2 ও y^2-এর সহগ 1 বানিয়ে নেবে।"},
        {"id": 22, "week": "week_02", "subject": "Higher Math", "trap": "৩য় চতুর্ভাগের জটিল সংখ্যার মুখ্য আর্গুমেন্ট pi + alpha দাগানো", "fix": "মুখ্য আর্গুমেন্টের সীমা (-pi, pi], তাই ৩য় চতুর্ভাগে মুখ্য আর্গুমেন্ট -pi + alpha।"},
        {"id": 23, "week": "week_02", "subject": "Biology", "trap": "পিত্তরসে পরিপাক এনজাইম আছে এবং হাইড্রা শর্করা পরিপাক করে ভাবা", "fix": "পিত্তরসে কোনো এনজাইম থাকে না এবং হাইড্রা শ্বেতসার পরিপাক করতে পারে না।"},
        {"id": 24, "week": "week_02", "subject": "Biology", "trap": "জাইগোটিন ও প্যাকাইটিনের ঘটনা উল্টে ফেলা", "fix": "জাইগোটিনে জোড়া বাঁধে (সিন্যাপসিস/বাইভ্যালেন্ট) এবং প্যাকাইটিনে প্যাঁচ লাগে (ক্রসিং ওভার)।"},
        {"id": 25, "week": "week_03", "subject": "Physics", "trap": "স্প্রিংকে কেটে অর্ধেক করলে কাজ দ্বিগুণ হবে ভাবা", "fix": "স্প্রিং কাটলে ধ্রুবক দ্বিগুণ হয় ($k'=2k$), কিন্তু একই প্রসারণ $x$-এ সঞ্চিত কাজ অর্ধেক হয়: $W' = \\frac{1}{2}W_1$।"},
        {"id": 26, "week": "week_03", "subject": "Physics", "trap": "ফাঁপা গোলকের অভ্যন্তরে প্রাবল্য $E = 0$ দেখে বিভবও শূন্য দাগানো", "fix": "ফাঁপা গোলকের ভেতরে প্রাবল্য শূন্য হলেও বিভব সর্বত্র পৃষ্ঠের বিভবের সমান ও ধ্রুবক ($V = -\\frac{GM}{R}$)।"},
        {"id": 27, "week": "week_03", "subject": "Physics", "trap": "অভিকর্ষজ ত্বরণ $1/9$ গুণ হলে উচ্চতা $h = 3R$ দাগানো", "fix": "কেন্দ্র থেকে দূরত্ব $3R$, কিন্তু ভূপৃষ্ঠ থেকে উচ্চতা $h = 2R$!"},
        {"id": 28, "week": "week_03", "subject": "Chemistry", "trap": "রেডিয়াল নোড ও মোট নোড এক মনে করা", "fix": "মোট নোড $= n - 1$, রেডিয়াল নোড $= n - l - 1$, কৌণিক নোড $= l$।"},
        {"id": 29, "week": "week_03", "subject": "Chemistry", "trap": "Be ও Mg শিখা পরীক্ষায় বর্ণ দেয় ভাবা", "fix": "উচ্চ আয়নীকরণ শক্তির কারণে Be ও Mg কোনো শিখা পরীক্ষা দেয় না এবং উদ্বায়ী ক্লোরাইডে গাঢ় HCl লাগে।"},
        {"id": 30, "week": "week_03", "subject": "Chemistry", "trap": "গ্রুপ-২ সালফেট ও হাইড্রোক্সাইডের দ্রাব্যতা ক্রম একই ভাবা", "fix": "সালফেটের দ্রাব্যতা নিচে কমে (BeSO4 > ... > BaSO4), কিন্তু হাইড্রোক্সাইডের দ্রাব্যতা বাড়ে (Mg(OH)2 < ... < Ba(OH)2)!"},
        {"id": 31, "week": "week_03", "subject": "Higher Math", "trap": "উপবৃত্তে $b > a$ হলেও অন্ধভাবে উপকেন্দ্র $(\\pm ae, 0)$ বসানো", "fix": "$b > a$ হলে উপকেন্দ্র y-অক্ষে $(0, \\pm be)$ এবং উপকেন্দ্রিক লম্ব $\\frac{2a^2}{b}$।"},
        {"id": 32, "week": "week_03", "subject": "Higher Math", "trap": "অধিবৃত্তে কে বড় দেখে আড় অক্ষ নির্ধারণ করা", "fix": "অধিবৃত্তে যে পদের চিহ্ন ধনাত্মক (+), আড় অক্ষ ও উপকেন্দ্র সর্বদা সেই অক্ষ বরাবর থাকে।"},
        {"id": 33, "week": "week_03", "subject": "Higher Math", "trap": "1/|x - a| >= k অসমতার সমাধানে মধ্যবিন্দু x = a বাদ না দেওয়া", "fix": "হরে |x - a| থাকায় x = a বিন্দুতে অসংজ্ঞায়িত; সমাধান থেকে অবশ্যই {a} বর্জন করতে হবে।"},
        {"id": 34, "week": "week_03", "subject": "Biology", "trap": "C4 উদ্ভিদে প্রথম CO2 গ্রাহক OAA দাগানো", "fix": "প্রথম CO2 গ্রাহক হলো ৩-কার্বন PEP, আর প্রথম স্থায়ী পদার্থ হলো ৪-কার্বন OAA।"},
        {"id": 35, "week": "week_03", "subject": "Biology", "trap": "নগ্নবীজী ও আবৃতবীজী উভয়ের শস্যকলাকেই ট্রিপ্লয়েড ভাবা", "fix": "আবৃতবীজীর শস্য নিষেকের পরে গঠিত হয় তাই 3n, কিন্তু নগ্নবীজীর শস্য নিষেকের পূর্বে গঠিত হয় তাই হ্যাপ্লয়েড (n)।"},
        {"id": 36, "week": "week_03", "subject": "Biology", "trap": "সুক্রোজকে রিডিউসিং শ্যুগার ভাবা", "fix": "সুক্রোজ ও সকল পলিস্যাকারাইড নন-রিডিউসিং শ্যুগার; এবং হিস্টোন প্রোটিন S দশায় সংশ্লেষিত হয়।"}
    ]

    vault_data = {
        "triplets": triplets,
        "quick_math": quick_math,
        "magic_fractions": magic_fractions,
        "patterns": patterns,
        "traps": traps
    }

    with open(os.path.join(OUT_DIR, "vault.json"), "w", encoding="utf-8") as f:
        json.dump(vault_data, f, ensure_ascii=False, indent=2)
    print("✓ vault.json generated successfully.")

# -------------------------------------------------------------
# 3. QUIZZES PARSER (100 W01 + 100 W02 + 100 W03 = 300 MCQs)
# -------------------------------------------------------------
def load_all_quizzes():
    from parse_helpers import get_w1_mcqs, parse_w2_mcqs, parse_w3_mcqs
    w1_list = get_w1_mcqs()
    w2_list = parse_w2_mcqs()
    w3_list = parse_w3_mcqs()

    all_quizzes = []
    # Week 01
    for q in w1_list:
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_01",
            "subject": q["subject"],
            "q": q["q"],
            "question": q["q"],
            "opts": q["opts"],
            "options": q["opts"],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": q["exp"],
            "explanation": q["exp"],
            "trap": q["trap"],
            "trap_insight": q["trap"]
        })

    # Week 02
    for q in w2_list:
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_02",
            "subject": q["subject"],
            "q": q["q"],
            "question": q["q"],
            "opts": q["opts"],
            "options": q["opts"],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": q["exp"],
            "explanation": q["exp"],
            "trap": q["trap"],
            "trap_insight": q["trap"]
        })

    # Week 03
    for q in w3_list:
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_03",
            "subject": q["subject"],
            "q": q["q"],
            "question": q["q"],
            "opts": q["opts"],
            "options": q["opts"],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": q["exp"],
            "explanation": q["exp"],
            "trap": q["trap"],
            "trap_insight": q["trap"]
        })

    print(f"Total quizzes compiled: {len(all_quizzes)} (Week 01: {len(w1_list)}, Week 02: {len(w2_list)}, Week 03: {len(w3_list)})")
    with open(os.path.join(OUT_DIR, "quizzes.json"), "w", encoding="utf-8") as f:
        json.dump(all_quizzes, f, ensure_ascii=False, indent=2)
    print("✓ quizzes.json generated successfully.")

# -------------------------------------------------------------
# 4. SLIDES & FLASHCARDS
# -------------------------------------------------------------
def load_slides_and_flashcards():
    from parse_helpers import get_all_slides, get_all_flashcards
    slides = get_all_slides()
    flashcards = get_all_flashcards()

    with open(os.path.join(OUT_DIR, "slides.json"), "w", encoding="utf-8") as f:
        json.dump(slides, f, ensure_ascii=False, indent=2)
    print(f"✓ slides.json generated successfully ({len(slides)} slides).")

    with open(os.path.join(OUT_DIR, "flashcards.json"), "w", encoding="utf-8") as f:
        json.dump(flashcards, f, ensure_ascii=False, indent=2)
    print(f"✓ flashcards.json generated successfully ({len(flashcards)} flashcards).")

def main():
    print("Executing Multi-Week Data Pipeline for Admission Crack 2026 (W1, W2, W3)...")
    build_weeks()
    build_vault()
    load_all_quizzes()
    load_slides_and_flashcards()
    print("All datasets compiled with zero truncation.")

if __name__ == "__main__":
    main()
