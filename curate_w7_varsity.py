#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_w7_varsity.py
Week 07 Varsity Ka Core (Primary Spine) & DU Written Special (Target 2026-2027)
- 48 MCQs: 12 Physics, 12 Chemistry, 12 Higher Math, 12 Biology (exact 4 slots of 12)
- 16 Written Problems: 4 Physics, 4 Chemistry, 4 Higher Math, 4 Biology with rubrics
- Zero boilerplate trap alerts, authentic chapter-specific pitfalls, valid KaTeX.
"""

def get_varsity_questions():
    questions = []

    # ==========================================
    # PHYSICS (12 MCQs) - Chapters: স্থির তড়িৎ, আধুনিক পদার্থবিজ্ঞান
    # ==========================================
    phy_mcqs = [
        {
            "id": "w7_var_phy_01",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '22-23 Speed Hack",
            "q": "$+4q$ এবং $+q$ মানের দুটি বিন্দু চার্জ পরস্পরের থেকে $d$ দূরত্বে অবস্থিত। এদের সংযোগ রেখার কোন বিন্দুতে লব্ধি তড়িৎ প্রাবল্য শূন্য ($E=0$) হবে?",
            "opts": [
                "$+4q$ হতে $\\frac{2}{3}d$ দূরত্বে",
                "$+4q$ হতে $\\frac{1}{3}d$ দূরত্বে",
                "$+q$ হতে $\\frac{2}{3}d$ দূরত্বে",
                "$+4q$ হতে $\\frac{1}{2}d$ দূরত্বে"
            ],
            "ans": 0,
            "exp": "চার্জদ্বয় সমধর্মী হওয়ায় লব্ধি প্রাবল্য শূন্য হবে এদের মধ্যবর্তী সংযোগ রেখায়। শর্টকাট অনুপাত: $q_1$ থেকে দূরত্ব $x_1 = \\frac{\\sqrt{q_1}}{\\sqrt{q_1} + \\sqrt{q_2}} d = \\frac{\\sqrt{4}}{\\sqrt{4} + \\sqrt{1}} d = \\frac{2}{2 + 1} d = \\frac{2}{3}d$। অর্থাৎ $+4q$ হতে $\\frac{2}{3}d$ (বা $+q$ হতে $\\frac{1}{3}d$) দূরত্বে।",
            "trap_alert": "দূরত্বটি কোন চার্জ হতে চাওয়া হয়েছে ($+4q$ নাকি $+q$) তা লক্ষ্য না করে দ্রুত $\\frac{1}{3}d$ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Core",
            "intelligence_type": "Null Point Field Ratio",
            "source_book": "ইসহাক স্যার / তপন স্যার"
        },
        {
            "id": "w7_var_phy_02",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '20-21 Repeat",
            "q": "একটি বিন্দু চার্জ $Q$-কে কেন্দ্র করে $r$ ব্যাসার্ধের একটি বৃত্তাকার সমবিভব তলে একটি পরীক্ষণ চার্জ $q_0$-কে একবার সম্পূর্ণ ঘুরিয়ে আনতে কৃতকাজের মান কত?",
            "opts": [
                "$0$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{Q q_0}{r}$",
                "$2\\pi r \\cdot \\frac{Q q_0}{4\\pi\\epsilon_0 r^2}$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{Q q_0}{r^2}$"
            ],
            "ans": 0,
            "exp": "সমবিভব তলের প্রতিটি বিন্দুতে বিভব সমান ($V_A = V_B$), ফলে বিভব পার্থক্য $\\Delta V = 0$। কৃতকাজ $W = q_0 \\Delta V = q_0 \\times 0 = 0$। এছাড়াও তড়িৎ বল একটি সংরক্ষণশীল বল, তাই যেকোনো বদ্ধ পথে মোট কৃতকাজ সর্বদা শূন্য।",
            "trap_alert": "বৃত্তের পরিধি $2\\pi r$ দিয়ে বলকে গুণ করে কাজ বের করার বৃথা চেষ্টা করা।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Equipotential Work Concept",
            "source_book": "ইসহাক স্যার"
        },
        {
            "id": "w7_var_phy_03",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '19-20 Repeat",
            "q": "$R$ ব্যাসার্ধের একটি ফাঁপা পরিবাহী গোলককে $+Q$ চার্জে আহিত করা হলো। গোলকের কেন্দ্র হতে $r = \\frac{R}{2}$ দূরত্বে তড়িৎ বিভব কত?",
            "opts": [
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{R}$",
                "$0$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{2Q}{R}$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{4Q}{R}$"
            ],
            "ans": 0,
            "exp": "চার্জিত পরিবাহী গোলকের অভ্যন্তরে কোনো চার্জ থাকে না, ফলে অভ্যন্তরে সর্বত্র তড়িৎ প্রাবল্য $E = 0$। যেহেতু $E = -\\frac{dV}{dr} = 0$, তাই গোলকের কেন্দ্র হতে পৃষ্ঠ পর্যন্ত বিভব সর্বত্র ধ্রুবক এবং পৃষ্ঠের বিভবের সমান ($V_{\\text{inside}} = V_{\\text{surface}} = \\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{R}$)।",
            "trap_alert": "অভ্যন্তরে প্রাবল্য শূন্য ($E=0$) দেখে বিভবও শূন্য ($V=0$) ধরে নেওয়া সবচেয়ে মারাত্মক ফাঁদ।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Spherical Conductor Potential",
            "source_book": "তপন স্যার"
        },
        {
            "id": "w7_var_phy_04",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '23-24 Concept",
            "q": "একটি সমান্তরাল পাত ধারককে ব্যাটারির সাথে যুক্ত করে আহিত করার পর ব্যাটারি বিচ্ছিন্ন করা হলো। এরপর পাতদ্বয়ের মাঝে $\\kappa = 4$ ডাই-ইলেকট্রিক ধ্রুবকের মাধ্যম প্রবেশ করালে সঞ্চিত শক্তির কী পরিবর্তন ঘটবে?",
            "opts": [
                "পূর্বের শক্তির $\\frac{1}{4}$ গুণ হবে",
                "পূর্বের শক্তির $4$ গুণ হবে",
                "অপরিবর্তিত থাকবে",
                "পূর্বের শক্তির $16$ গুণ হবে"
            ],
            "ans": 0,
            "exp": "ব্যাটারি বিচ্ছিন্ন করায় চার্জ $Q$ ধ্রুবক থাকে ($Q' = Q$)। ডাই-ইলেকট্রিক প্রবেশ করালে নতুন ধারকত্ব $C' = \\kappa C = 4C$। সঞ্চিত শক্তি $U = \\frac{Q^2}{2C}$। সুতরাং নতুন সঞ্চিত শক্তি $U' = \\frac{Q^2}{2(4C)} = \\frac{1}{4} U$।",
            "trap_alert": "ব্যাটারি যুক্ত থাকা ($V$ ধ্রুবক, যেখানে $U' = 4U$) এবং ব্যাটারি বিচ্ছিন্ন থাকার ($Q$ ধ্রুবক, যেখানে $U' = U/4$) শর্তের পার্থক্য ভুলে যাওয়া।",
            "yield_stars": 5,
            "probability": "96% DU Hotspot",
            "intelligence_type": "Capacitor Dielectric Energy Shift",
            "source_book": "ইসহাক স্যার"
        },
        {
            "id": "w7_var_phy_05",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "CKRUET '22-23 Speed Hack",
            "q": "একই আকার ও $V$ বিভবের $64$ টি পারদ ফোঁটা একত্রিত হয়ে একটি বৃহৎ ফোঁটায় পরিণত হলে বৃহৎ ফোঁটাটির বিভব কত গুণ বৃদ্ধি পাবে?",
            "opts": [
                "$16$ গুণ",
                "$4$ গুণ",
                "$64$ গুণ",
                "$8$ গুণ"
            ],
            "ans": 0,
            "exp": "$n$ টি ফোঁটা একত্রিত হলে আয়তন সংরক্ষণ নীতি অনুসারে: $R = n^{1/3} r = 64^{1/3} r = 4r$। মোট চার্জ $Q = n q = 64q$। নতুন বিভব $V' = \\frac{Q}{C'} = \\frac{n q}{n^{1/3} C} = n^{2/3} V = (64)^{2/3} V = (4^3)^{2/3} V = 4^2 V = 16V$।",
            "trap_alert": "বিভবের ক্ষেত্রে $n^{2/3}$ এর বদলে ধারকত্বের $n^{1/3}$ ($4$ গুণ) বা চার্জের $n$ ($64$ গুণ) উত্তর দাগানো।",
            "yield_stars": 5,
            "probability": "97% Speed Hack",
            "intelligence_type": "Coalescing Droplets Scaling",
            "source_book": "গিয়াসউদ্দিন স্যার"
        },
        {
            "id": "w7_var_phy_06",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '21-22 Repeat",
            "q": "একটি স্থির কণার ভর $m_0$। কণাটি কত বেগে গতিশীল হলে এর গতিশীল ভর নিশ্চল ভরের দ্বিগুণ ($m = 2m_0$) হবে?",
            "opts": [
                "$\\frac{\\sqrt{3}}{2}c \\approx 0.866c$",
                "$\\frac{1}{2}c = 0.5c$",
                "$\\frac{1}{\\sqrt{2}}c \\approx 0.707c$",
                "$\\frac{\\sqrt{5}}{3}c$"
            ],
            "ans": 0,
            "exp": "আপেক্ষিকতার ভর বৃদ্ধির সূত্র: $m = \\frac{m_0}{\\sqrt{1 - v^2/c^2}} = 2m_0 \\implies \\sqrt{1 - v^2/c^2} = \\frac{1}{2} \\implies 1 - \\frac{v^2}{c^2} = \\frac{1}{4} \\implies \\frac{v^2}{c^2} = \\frac{3}{4} \\implies v = \\frac{\\sqrt{3}}{2}c \\approx 0.866c$।",
            "trap_alert": "ভর দ্বিগুণ দেখে বেগও আলোর বেগের অর্ধেক ($0.5c$) মনে করা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Relativistic Mass Ratio",
            "source_book": "ইসহাক স্যার"
        },
        {
            "id": "w7_var_phy_07",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '18-19 Repeat",
            "q": "একটি $1\\text{ m}$ দৈর্ঘ্যের স্কেল তার দৈর্ঘ্য বরাবর $0.6c$ বেগে গতিশীল হলে একজন স্থির পর্যবেক্ষকের নিকট এর আপাত দৈর্ঘ্য কত হবে?",
            "opts": [
                "$80\\text{ cm}$",
                "$60\\text{ cm}$",
                "$100\\text{ cm}$",
                "$40\\text{ cm}$"
            ],
            "ans": 0,
            "exp": "দৈর্ঘ্য সংকোচন সূত্র: $L = L_0 \\sqrt{1 - v^2/c^2} = 1 \\times \\sqrt{1 - (0.6)^2} = \\sqrt{1 - 0.36} = \\sqrt{0.64} = 0.8\\text{ m} = 80\\text{ cm}$। (ম্যাজিক ট্রিপলেট: $0.6c$ বেগে ফ্যাক্টর সর্বদা $0.8$ এবং $0.8c$ বেগে ফ্যাক্টর সর্বদা $0.6$)।",
            "trap_alert": "মিটারে $0.8$ বের করে অপশনে সেন্টিমিটার খেয়াল না করা অথবা লম্বভাবে গতিশীলের ক্ষেত্রে দৈর্ঘ্য অপরিবর্তিত থাকার নিয়ম গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "98% DU Core",
            "intelligence_type": "Length Contraction Triplet",
            "source_book": "তপন স্যার"
        },
        {
            "id": "w7_var_phy_08",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '23-24 Conceptual",
            "q": "একটি ধাতব পাতে নির্দিষ্ট তরঙ্গদৈর্ঘ্যের আলো ফেলে নিবৃত্তি বিভব $V_s$ পাওয়া গেল। আপতিত আলোর তরঙ্গদৈর্ঘ্য অর্ধেক করা হলে নতুন নিবৃত্তি বিভব $V_s'$ এর মান কীরূপ হবে?",
            "opts": [
                "$V_s' > 2V_s$ (দ্বিগুণের চেয়ে বেশি)",
                "$V_s' = 2V_s$ (ঠিক দ্বিগুণ)",
                "$V_s' < 2V_s$ (দ্বিগুণের চেয়ে কম)",
                "$V_s' = V_s$ (অপরিবর্তিত)"
            ],
            "ans": 0,
            "exp": "আইনস্টাইনের আলোকতড়িৎ সমীকরণ: $eV_s = \\frac{hc}{\\lambda} - W_0 \\implies \\frac{hc}{\\lambda} = eV_s + W_0$। তরঙ্গদৈর্ঘ্য $\\lambda' = \\frac{\\lambda}{2}$ হলে: $eV_s' = \\frac{hc}{\\lambda/2} - W_0 = 2\\frac{hc}{\\lambda} - W_0 = 2(eV_s + W_0) - W_0 = 2eV_s + W_0$। যেহেতু কার্যপেক্ষক $W_0 > 0$, তাই $eV_s' > 2eV_s \\implies V_s' > 2V_s$।",
            "trap_alert": "তরঙ্গদৈর্ঘ্য অর্ধেক হলে ফোটনের শক্তি দ্বিগুণ হয় ঠিকই, কিন্তু বিয়োগফল $W_0$ এর কারণে নিবৃত্তি বিভব ঠিক দ্বিগুণ নয় বরং দ্বিগুণের চেয়ে বেশি হয়।",
            "yield_stars": 5,
            "probability": "96% Analytical Trap",
            "intelligence_type": "Photoelectric Stopping Potential Non-linearity",
            "source_book": "ইসহাক স্যার"
        },
        {
            "id": "w7_var_phy_09",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "CKRUET '21-22 Speed Hack",
            "q": "$100\\text{ V}$ বিভব পার্থক্যে ত্বরান্বিত একটি ইলেকট্রনের ডি-ব্রগলি তরঙ্গদৈর্ঘ্য কত?",
            "opts": [
                "$1.23\\text{ \\AA}$ ($0.123\\text{ nm}$)",
                "$0.123\\text{ \\AA}$",
                "$12.3\\text{ \\AA}$",
                "$1.23\\text{ pm}$"
            ],
            "ans": 0,
            "exp": "ইলেকট্রনের ডি-ব্রগলি তরঙ্গদৈর্ঘ্যের জন্য স্ট্যান্ডার্ড স্পিড হ্যাক: $\\lambda = \\frac{1.227}{\\sqrt{V}}\\text{ nm} = \\sqrt{\\frac{150}{V}}\\text{ \\AA}$। $V = 100\\text{ V}$ বসালে: $\\lambda = \\frac{1.227}{\\sqrt{100}}\\text{ nm} = \\frac{1.227}{10}\\text{ nm} = 0.1227\\text{ nm} = 1.227\\text{ \\AA} \\approx 1.23\\text{ \\AA}$।",
            "trap_alert": "অ্যানগোস্ট্রম ($\\text{\\AA}$) এবং ন্যানোমিটার ($\\text{nm}$) এককের দশমিক স্থান পরিবর্তন নিয়ে ভুল হওয়া।",
            "yield_stars": 5,
            "probability": "97% Speed Hack",
            "intelligence_type": "Electron De Broglie Voltage Formula",
            "source_book": "ইসহাক স্যার"
        },
        {
            "id": "w7_var_phy_10",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '21-22 Repeat",
            "q": "একটি তেজস্ক্রিয় মৌলের অর্ধায়ু $4\\text{ দিন}$। $16\\text{ দিন}$ পর উক্ত নমুনার কত অংশ ক্ষয়প্রাপ্ত হবে?",
            "opts": [
                "$\\frac{15}{16}$ অংশ",
                "$\\frac{1}{16}$ অংশ",
                "$\\frac{7}{8}$ অংশ",
                "$\\frac{3}{4}$ অংশ"
            ],
            "ans": 0,
            "exp": "অর্ধায়ুর সংখ্যা $n = \\frac{t}{T_{1/2}} = \\frac{16}{4} = 4$। $4$ টি অর্ধায়ু পর অবশিষ্ট থাকে $N = N_0 \\left(\\frac{1}{2}\\right)^4 = \\frac{N_0}{16}$ (অর্থাৎ $\\frac{1}{16}$ অংশ অবশিষ্ট)। সুতরাং ক্ষয়প্রাপ্ত অংশ $= 1 - \\frac{1}{16} = \\frac{15}{16}$ অংশ।",
            "trap_alert": "প্রশ্নে 'কত অংশ অবশিষ্ট থাকবে' নাকি 'কত অংশ ক্ষয়প্রাপ্ত হবে' চাওয়া হয়েছে তা ভালো করে না দেখে $\\frac{1}{16}$ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Decay Fraction Pitfall",
            "source_book": "তপন স্যার"
        },
        {
            "id": "w7_var_phy_11",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '22-23 Speed Hack",
            "q": "সূর্যের ভরের দেড়গুণ ($1.5 M_\\odot \\approx 3 \\times 10^{30}\\text{ kg}$) একটি নক্ষত্র ব্ল্যাকহোলে পরিণত হলে এর সোয়ার্জশিল্ড ব্যাসার্ধ (ইভেন্ট হরাইজন) কত হবে?",
            "opts": [
                "$4.5\\text{ km}$ ($4500\\text{ m}$)",
                "$3.0\\text{ km}$",
                "$9.0\\text{ km}$",
                "$1.5\\text{ km}$"
            ],
            "ans": 0,
            "exp": "সোয়ার্জশিল্ড ব্যাসার্ধ $R_s = \\frac{2GM}{c^2}$। ১ সৌর ভরের জন্য $R_{s,\\odot} \\approx 3\\text{ km}$। সুতরাং শর্টকাট: $R_s = 3\\text{ km} \\times \\left(\\frac{M}{M_\\odot}\\right) = 3\\text{ km} \\times 1.5 = 4.5\\text{ km} = 4500\\text{ m}$।",
            "trap_alert": "সোয়ার্জশিল্ড ব্যাসার্ধের বদলে ব্যাস ($9.0\\text{ km}$) দাগানো অথবা একক কিমি বনাম মিটারে বিভ্রান্ত হওয়া।",
            "yield_stars": 4,
            "probability": "94% Speed Hack",
            "intelligence_type": "Schwarzschild Radius Speed Hack",
            "source_book": "ইসহাক স্যার"
        },
        {
            "id": "w7_var_phy_12",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '17-18 Direct",
            "q": "যুগল সৃষ্টি (Pair Production) প্রক্রিয়ায় একটি ফোটন হতে একটি ইলেকট্রন ও একটি পজিট্রন সৃষ্টি হতে আপতিত ফোটনের ন্যূনতম শক্তি কত হতে হবে?",
            "opts": [
                "$1.02\\text{ MeV}$",
                "$0.51\\text{ MeV}$",
                "$2.04\\text{ MeV}$",
                "$0.25\\text{ MeV}$"
            ],
            "ans": 0,
            "exp": "একটি ইলেকট্রন বা পজিট্রনের নিশ্চল ভরশক্তি $E_0 = m_0 c^2 = 0.511\\text{ MeV}$। যুগল সৃষ্টিতে ইলেকট্রন ও পজিট্রন জোড় তৈরি হতে ন্যূনতম শক্তি $E_{\\min} = 2 m_0 c^2 = 2 \\times 0.511\\text{ MeV} \\approx 1.02\\text{ MeV}$।",
            "trap_alert": None,
            "yield_stars": 5,
            "probability": "97% DU Repeat",
            "intelligence_type": "Pair Production Threshold Energy",
            "source_book": "ইসহাক স্যার"
        }
    ]

    # ==========================================
    # CHEMISTRY (12 MCQs) - Chapters: জৈব রসায়ন
    # ==========================================
    che_mcqs = [
        {
            "id": "w7_var_che_01",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '21-22 Repeat",
            "q": "$\\text{CH}_3-\\text{CH}(\\text{OH})-\\text{CH}_2-\\text{COOH}$ যৌগটির সঠিক IUPAC নাম কোনটি?",
            "opts": [
                "৩-হাইড্রোক্সিবিউটানয়িক এসিড",
                "২-হাইড্রোক্সিবিউটানয়িক এসিড",
                "৩-হাইড্রোক্সিবিউটানল",
                "বিউটান-৩-অল-১-ওয়িক এসিড"
            ],
            "ans": 0,
            "exp": "কার্যকরী মূলকের অগ্রগণ্যতার ক্রমানুসারে $-\\text{COOH} > -\\text{OH}$। তাই $-\\text{COOH}$ এর কার্বনকে ১ নম্বর ধরে শিকল গণনা শুরু করতে হবে: $\\overset{4}{\\text{C}}\\text{H}_3-\\overset{3}{\\text{C}}\\text{H}(\\text{OH})-\\overset{2}{\\text{C}}\\text{H}_2-\\overset{1}{\\text{C}}\\text{OOH}$। ৩-নম্বরে হাইড্রক্সিল প্রতিস্থাপক থাকায় সঠিক নাম ৩-হাইড্রোক্সিবিউটানয়িক এসিড।",
            "trap_alert": "$-\\text{OH}$ এর দিক থেকে নাম্বারিং করে '২-হাইড্রোক্সিবিউটানয়িক এসিড' দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "IUPAC Priority Rules",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_02",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '19-20 Repeat",
            "q": "পেনটেন ($\\text{C}_5\\text{H}_{12}$) অ্যালকেনের সম্ভাব্য শিকল সমাণু (Chain Isomers) সংখ্যা কতটি?",
            "opts": [
                "$3$ টি",
                "$5$ টি",
                "$2$ টি",
                "$4$ টি"
            ],
            "ans": 0,
            "exp": "$\\text{C}_5\\text{H}_{12}$ এর সমাণু ৩টি: ১. $n$-পেনটেন (সরল শিকল), ২. আইসোপেনটেন বা ২-মিথাইলবিউটেন, ৩. নিওপেনটেন বা ২,২-ডাইমিথাইলপ্রোপেন। (অ্যালকেন সমাণু সংখ্যা হ্যাক: বিউটেন=২, পেনটেন=৩, হেক্সেন=৫, হেপ্টেন=৯)।",
            "trap_alert": "হেক্সেনের সমাণু ($5$ টি) এর সাথে পেনটেনের সমাণু ($3$ টি) গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Alkane Isomer Counting Hack",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_03",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '22-23 Repeat",
            "q": "নিচের কোন যৌগটি আলোক সমাণুতা (Optical Isomerism) প্রদর্শন করে?",
            "opts": [
                "ল্যাকটিক এসিড ($\\text{CH}_3-\\text{CH(OH)}-\\text{COOH}$)",
                "ইথানল ($\\text{CH}_3-\\text{CH}_2-\\text{OH}$)",
                "প্রোপান-২-অল ($\\text{CH}_3-\\text{CH(OH)}-\\text{CH}_3$)",
                "অ্যাসিটিক এসিড ($\\text{CH}_3-\\text{COOH}$)"
            ],
            "ans": 0,
            "exp": "আলোক সমাণুতার প্রধান শর্ত অণুতে কাইরাল বা অপ্রতিসম কার্বন কেন্দ্র থাকা। ল্যাকটিক এসিডের কেন্দ্রীয় কার্বনে চারটি ভিন্ন মূলক যুক্ত: $-\\text{H}, -\\text{OH}, -\\text{CH}_3, -\\text{COOH}$। প্রোপান-২-অল এ দুটি $-\\text{CH}_3$ একই হওয়ায় তা অকাইরাল।",
            "trap_alert": "প্রোপান-২-অল এ $-\\text{OH}$ থাকা সত্ত্বেও সমধর্মী দুটি মিথাইল মূলক থাকায় এটি কাইরাল নয়—এই সূক্ষ্ম পার্থক্য মিস করা।",
            "yield_stars": 5,
            "probability": "99% DU Hotspot",
            "intelligence_type": "Chiral Center Detection",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_04",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '23-24 Core",
            "q": "নিচের কোন যৌগটিতে জ্যামিতিক সমাণুতা (Cis-Trans) দেখা যায়?",
            "opts": [
                "বাট-২-ইন ($\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3$)",
                "বাট-১-ইন ($\\text{CH}_3-\\text{CH}_2-\\text{CH}=\\text{CH}_2$)",
                "প্রোপিন ($\\text{CH}_3-\\text{CH}=\\text{CH}_2$)",
                "২-মিথাইলপ্রোপিন ($(\\text{CH}_3)_2\\text{C}=\\text{CH}_2$)"
            ],
            "ans": 0,
            "exp": "জ্যামিতিক সমাণুতার অপরিহার্য শর্ত: দ্বিবন্ধনযুক্ত কার্বনদ্বয়ের প্রতিটিতে দুটি ভিন্ন পরমাণু বা মূলক থাকতে হবে ($ab\\text{C}=\\text{C}ab$)। বাট-১-ইন এবং প্রোপিনে প্রান্তীয় কার্বনে দুটি একই হাইড্রোজেন ($=\\text{CH}_2$) থাকায় এরা সিস্ট্রান্স দিতে পারে না। বাট-২-ইন এ প্রতিটি দ্বিবন্ধনযুক্ত কার্বনে $-\\text{H}$ ও $-\\text{CH}_3$ থাকায় সিস্ট্রান্স সমাণুতা দেখা যায়।",
            "trap_alert": "কার্বন-কার্বন দ্বিবন্ধন থাকলেই অন্ধভাবে জ্যামিতিক সমাণুতা ধরে নেওয়া, প্রান্তীয় কার্বনে দুটি হাইড্রোজেন ($=\\text{CH}_2$) খেয়াল না করা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Geometrical Isomerism Criteria",
            "source_book": "সঞ্জিত কুমার গুহ"
        },
        {
            "id": "w7_var_che_05",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '20-21 Repeat",
            "q": "কার্বোক্যাটায়নসমূহের স্থায়িত্বের সঠিক নিম্নক্রম কোনটি?",
            "opts": [
                "$3^\\circ > 2^\\circ > 1^\\circ > \\text{CH}_3^+$",
                "$\\text{CH}_3^+ > 1^\\circ > 2^\\circ > 3^\\circ$",
                "$2^\\circ > 3^\\circ > 1^\\circ > \\text{CH}_3^+$",
                "$3^\\circ > 1^\\circ > 2^\\circ > \\text{CH}_3^+$"
            ],
            "ans": 0,
            "exp": "অ্যালকাইল মূলকের ইলেকট্রন প্রদানকারী $+I$ আবেশীয় প্রভাব এবং হাইপারকনজুগেশনের কারণে কার্বোক্যাটায়নের ধনাত্মক চার্জ প্রশমিত হয়ে স্থায়িত্ব বৃদ্ধি পায়। ৩ ডিগ্রি ক্যাটায়নে ৩টি মিথাইল মূলকের সর্বাধিক হাইপারকনজুগেশন ঘটে। স্থায়িত্ব ক্রম: $3^\\circ > 2^\\circ > 1^\\circ > \\text{CH}_3^+$।",
            "trap_alert": "কার্বোক্যাটায়নের স্থায়িত্বের সাথে কার্বানায়নের স্থায়িত্ব ক্রম ($1^\\circ > 2^\\circ > 3^\\circ$) উল্টে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Core",
            "intelligence_type": "Carbocation Stability Series",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_06",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '21-22 Repeat",
            "q": "নিচের কোনটি প্রশম ইলেকট্রোফাইল (Neutral Electrophile)?",
            "opts": [
                "$\\text{AlCl}_3$",
                "$\\text{H}_3\\text{O}^+$",
                "$\\text{NH}_4^+$",
                "$\\text{NH}_3$"
            ],
            "ans": 0,
            "exp": "$\\text{AlCl}_3$ এবং $\\text{BF}_3$ এর কেন্দ্রীয় পরমাণুর অষ্টক অপূর্ণ থাকে (৬টি যোজ্য ইলেকট্রন), ফলে এরা প্রশম হয়েও মুক্তজোড় ইলেকট্রন গ্রহণ করতে পারে (লুইস এসিড = ইলেকট্রোফাইল)। $\\text{H}_3\\text{O}^+$ এবং $\\text{NH}_4^+$ এ ধনাত্মক চার্জ থাকলেও এদের অষ্টক সম্পূর্ণ এবং অতিরিক্ত ইলেকট্রন গ্রহণের ফাঁকা অরবিটাল না থাকায় এরা ইলেকট্রোফাইল নয়। $\\text{NH}_3$ একটি নিউক্লিওফাইল।",
            "trap_alert": "ধনাত্মক চার্জ দেখে $\\text{NH}_4^+$ বা $\\text{H}_3\\text{O}^+$ কে ইলেকট্রোফাইল ভেবে ভুল করা।",
            "yield_stars": 5,
            "probability": "98% DU Core",
            "intelligence_type": "Electrophile Identity Pitfall",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_07",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '19-20 Speed Hack",
            "q": "কার্বন-কার্বন বন্ধন দূরত্বের সঠিক ক্রম কোনটি?",
            "opts": [
                "$\\text{C}-\\text{C} (0.154\\text{ nm}) > \\text{C}_{\\text{benzene}} (0.139\\text{ nm}) > \\text{C}=\\text{C} (0.134\\text{ nm}) > \\text{C}\\equiv\\text{C} (0.120\\text{ nm})$",
                "$\\text{C}\\equiv\\text{C} > \\text{C}=\\text{C} > \\text{C}_{\\text{benzene}} > \\text{C}-\\text{C}$",
                "$\\text{C}-\\text{C} > \\text{C}=\\text{C} > \\text{C}_{\\text{benzene}} > \\text{C}\\equiv\\text{C}$",
                "$\\text{C}_{\\text{benzene}} > \\text{C}-\\text{C} > \\text{C}=\\text{C} > \\text{C}\\equiv\\text{C}$"
            ],
            "ans": 0,
            "exp": "বন্ধন সংখ্যা ও $s$-চরিত্র বাড়লে বন্ধন দৈর্ঘ্য হ্রাস পায়: ইথেন একক বন্ধন ($0.154\\text{ nm}$) > বেনজিনের রেজোন্যান্স বন্ধন ($0.139\\text{ nm}$) > ইথিন দ্বিবন্ধন ($0.134\\text{ nm}$) > ইথাইন ত্রিবন্ধন ($0.120\\text{ nm}$)।",
            "trap_alert": "বেনজিনের বন্ধন দৈর্ঘ্য দ্বিবন্ধনের চেয়েও ছোট মনে করা অথবা একক ও দ্বিবন্ধনের মাঝামাঝি মান ($0.139\\text{ nm}$) ভুলে যাওয়া।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Bond Length Resonance Order",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_08",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '18-19 Repeat",
            "q": "প্রোপানোন এবং প্রোপ-১-ইন-২-অল এর মধ্যে কোন ধরণের সমাণুতা বিদ্যমান?",
            "opts": [
                "টটোমারিজম (গতিশীল কার্যকরী মূলক সমাণুতা)",
                "মেটামারিজম",
                "অবস্থান সমাণুতা",
                "জ্যামিতিক সমাণুতা"
            ],
            "ans": 0,
            "exp": "কিটো ও ইনোল রূপ পরস্পরের সাথে গতিশীল সাম্যাবস্থায় থাকে: $\\text{CH}_3-\\text{CO}-\\text{CH}_3 \\rightleftharpoons \\text{CH}_3-\\text{C(OH)}=\\text{CH}_2$। হাইড্রোজেন পরমাণু ও পাই বন্ধনের স্থানান্তরের ফলে এই ধরণের গতিশীল কার্যকরী মূলক সমাণুতাকে টটোমারিজম বলে।",
            "trap_alert": "টটোমারিজমকে মেটামারিজম বা সাধারণ কার্যকরী মূলক সমাণুতার সাথে গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "97% DU Repeat",
            "intelligence_type": "Tautomerism Equilibrium",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_09",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '22-23 Speed Hack",
            "q": "একটি অপ্রতিসম জৈব যৌগে $2$ টি ভিন্ন কাইরাল কার্বন পরমাণু থাকলে এর স্টেরিও সমাণু সংখ্যা কতটি হবে?",
            "opts": [
                "$4$ টি",
                "$2$ টি",
                "$3$ টি",
                "$8$ টি"
            ],
            "ans": 0,
            "exp": "ভিন্ন বা অসদৃশ কাইরাল কার্বনের ক্ষেত্রে ভ্যান্ট হফ সূত্র: স্টেরিও সমাণু সংখ্যা $= 2^n = 2^2 = 4$ টি (যার মধ্যে ২ জোড়া এনানশিওমার থাকে)। যদি কাইরাল কার্বন দুটি সদৃশ হতো (যেমন টারটারিক এসিড), তবে মেসো যৌগের কারণে সমাণু হতো $2^{n-1} + 2^{(n/2)-1} = 2 + 1 = 3$ টি।",
            "trap_alert": "টারটারিক এসিডের মেসো সমাণুতার নিয়ম ($3$ টি) সাধারণ অসদৃশ কাইরাল যৌগের উপর প্রয়োগ করা।",
            "yield_stars": 4,
            "probability": "95% Speed Hack",
            "intelligence_type": "Stereoisomer Formula Shortcut",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_10",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '21-22 Core",
            "q": "নিচের কোন হাইড্রোকার্বনটি টলেন বিকারকের সাথে বিক্রিয়ায় ধাতব সিলভার বা সাদা অধঃক্ষেপ তৈরি করে?",
            "opts": [
                "অ্যাসিটিলিন ($\\text{CH}\\equiv\\text{CH}$)",
                "ইথিলিন ($\\text{CH}_2=\\text{CH}_2$)",
                "বিউট-২-আইন ($\\text{CH}_3-\\text{C}\\equiv\\text{C}-\\text{CH}_3$)",
                "বেনজিন ($\\text{C}_6\\text{H}_6$)"
            ],
            "ans": 0,
            "exp": "প্রান্তীয় অ্যালকাইন (১-অ্যালকাইন) এ ত্রিবন্ধনযুক্ত কার্বনে $sp$ সংকরায়ন থাকায় এর $s$-চরিত্র ৫০% এবং তীব্র ইলেকট্রনাকর্ষী হয়। ফলে এর প্রান্তীয় হাইড্রোজেন পরমাণু অম্লধর্মী এবং ডাইঅ্যামিন সিলভার নাইট্রেট (টলেন বিকারক) দ্রবণের সাথে বিক্রিয়া করে সিলভার অ্যালকানাইড ($\\text{AgC}\\equiv\\text{CAg}\\downarrow$) এর সাদা অধঃক্ষেপ ফেলে। বিউট-২-আইন এ কোনো অম্লীয় হাইড্রোজেন নেই।",
            "trap_alert": "বিউট-২-আইন বা ইথিলিন দেখে ট্রিপল বন্ড আছে ভেবে বিউট-২-আইন দাগানো; প্রান্তীয় ট্রিপল বন্ড (অম্লীয় হাইড্রোজেন) আবশ্যক।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Terminal Alkyne Acidity Test",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_11",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '17-18 Repeat",
            "q": "ডাই-ইথাইল ইথার ($\\text{C}_2\\text{H}_5-\\text{O}-\\text{C}_2\\text{H}_5$) এবং মিথাইল প্রোপাইল ইথার ($\\text{CH}_3-\\text{O}-\\text{C}_3\\text{H}_7$) এর মধ্যকার সমাণুতার ধরন কোনটি?",
            "opts": [
                "মেটামারিজম",
                "অবস্থান সমাণুতা",
                "টটোমারিজম",
                "চেইন সমাণুতা"
            ],
            "ans": 0,
            "exp": "একই সমগোত্রীয় শ্রেণীর দ্বি-যোজী কার্যকরী মূলকের (যেমন: $-\\text{O}-, -\\text{CO}-, -\\text{NH}-$) উভয় পাশে কার্বন শিকলের অসম বণ্টনের কারণে সৃষ্ট সমাণুতাকে মেটামারিজম বলে।",
            "trap_alert": "কার্যকরী মূলক এক দেখে সাধারণ অবস্থান সমাণুতা ভেবে ভুল করা।",
            "yield_stars": 5,
            "probability": "96% DU Repeat",
            "intelligence_type": "Metamerism Classification",
            "source_book": "হাজারী-নাগ স্যার"
        },
        {
            "id": "w7_var_che_12",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '20-21 Direct",
            "q": "সূর্যালোকের অতিবেগুনি (UV) রশ্মির উপস্থিতিতে ক্লোরিন অণুর সমভাঙ্গন (Homolytic Fission) ঘটলে কোনটি উৎপন্ন হয়?",
            "opts": [
                "ক্লোরিন মুক্ত মূলক ($\\text{Cl}^\\bullet$)",
                "ক্লোরাইড অ্যানায়ন ($\\text{Cl}^-$)",
                "ক্লোরোনিয়াম ক্যাটায়ন ($\\text{Cl}^+$)",
                "কার্বোক্যাটায়ন"
            ],
            "ans": 0,
            "exp": "সমযোজী বন্ধনের উভয় পরমাণু একটি করে ইলেকট্রন নিজের দিকে টেনে নিয়ে পৃথক হলে যে বিজোড় ইলেকট্রনযুক্ত অত্যন্ত সক্রিয় কণা সৃষ্টি হয় তাকে মুক্ত মূলক (Free Radical) বলে: $\\text{Cl}-\\text{Cl} \\xrightarrow{h\\nu} 2\\text{Cl}^\\bullet$।",
            "trap_alert": None,
            "yield_stars": 5,
            "probability": "98% DU Direct",
            "intelligence_type": "Homolytic Cleavage Radicals",
            "source_book": "হাজারী-নাগ স্যার"
        }
    ]

    # ==========================================
    # HIGHER MATH (12 MCQs) - Chapters: অন্তরীকরণ
    # ==========================================
    mat_mcqs = [
        {
            "id": "w7_var_mat_01",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '21-22 Speed Hack",
            "q": "মান নির্ণয় কর: $\\lim_{x\\to 0} \\frac{1 - \\cos 6x}{x^2}$",
            "opts": [
                "$18$",
                "$36$",
                "$3$",
                "$\\frac{1}{18}$"
            ],
            "ans": 0,
            "exp": "স্ট্যান্ডার্ড লিমিট শর্টকাট: $\\lim_{x\\to 0} \\frac{1 - \\cos ax}{x^2} = \\frac{a^2}{2}$। এখানে $a = 6$, সুতরাং মান $= \\frac{6^2}{2} = \\frac{36}{2} = 18$। (লা'হসপিটাল দিয়েও: $\\lim_{x\\to 0} \\frac{6\\sin 6x}{2x} = \\frac{6 \\times 6}{2} = 18$)।",
            "trap_alert": "সহগ $a$ কে বর্গ করতে ভুলে গিয়ে $\\frac{6}{2} = 3$ দাগানো অথবা ২ দিয়ে ভাগ করতে ভুলে গিয়ে $36$ দাগানো।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Cosine Limit Speed Formula",
            "source_book": "এস ইউ আহাম্মদ"
        },
        {
            "id": "w7_var_mat_02",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '22-23 Speed Hack",
            "q": "মান নির্ণয় কর: $\\lim_{x\\to 0} \\frac{\\sin 5x}{\\ln(1 + 2x)}$",
            "opts": [
                "$\\frac{5}{2} = 2.5$",
                "$\\frac{2}{5} = 0.4$",
                "$10$",
                "$1$"
            ],
            "ans": 0,
            "exp": "এটি $\\frac{0}{0}$ আকার। লা'হসপিটাল প্রয়োগ করে: লবের অন্তরক $5\\cos 5x$ এবং হরের অন্তরক $\\frac{2}{1+2x}$। $x \\to 0$ বসালে: $\\frac{5\\cos 0}{\\frac{2}{1+0}} = \\frac{5 \\times 1}{2} = \\frac{5}{2} = 2.5$।",
            "trap_alert": "লব ও হরের অনুপাত উল্টে দিয়ে $\\frac{2}{5}$ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "98% Speed Hack",
            "intelligence_type": "L'Hopital Direct Derivative",
            "source_book": "অসীম সাহা স্যার"
        },
        {
            "id": "w7_var_mat_03",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '19-20 Speed Hack",
            "q": "মান নির্ণয় কর: $\\lim_{x\\to \\infty} \\left(\\frac{x + 3}{x - 1}\\right)^x$",
            "opts": [
                "$e^4$",
                "$e^2$",
                "$e^3$",
                "$1$"
            ],
            "ans": 0,
            "exp": "সরাসরি গোল্ডেন শর্টকাট: $\\lim_{x\\to \\infty} \\left(\\frac{x + a}{x + b}\\right)^{cx + d} = e^{c(a - b)}$। এখানে $a = 3, b = -1, c = 1$। সুতরাং উত্তর $= e^{1 \\times (3 - (-1))} = e^{3 + 1} = e^4$।",
            "trap_alert": "$b = -1$ এর ঋণাত্মক চিহ্ন খেয়াল না করে $3 - 1 = 2$ ধরে $e^2$ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Infinity Base Exponential Hack",
            "source_book": "কেতাবউদ্দিন স্যার"
        },
        {
            "id": "w7_var_mat_04",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '20-21 Repeat",
            "q": "$y = x^3 - 3x^2 + 2$ বক্ররেখার কোন বিন্দুগুলোতে অঙ্কিত স্পর্শক $x$-অক্ষের সমান্তরাল?",
            "opts": [
                "$(0, 2)$ এবং $(2, -2)$",
                "$(0, 0)$ এবং $(2, 2)$",
                "$(1, 0)$ এবং $(-1, 4)$",
                "$(2, 0)$ এবং $(0, -2)$"
            ],
            "ans": 0,
            "exp": "স্পর্শক $x$-অক্ষের সমান্তরাল হওয়ার শর্ত: $\\frac{dy}{dx} = 0$। বক্ররেখার অন্তরক: $\\frac{dy}{dx} = 3x^2 - 6x = 3x(x - 2) = 0 \\implies x = 0$ অথবা $x = 2$। যখন $x = 0$, তখন $y = 0 - 0 + 2 = 2 \\implies (0, 2)$। যখন $x = 2$, তখন $y = 2^3 - 3(2^2) + 2 = 8 - 12 + 2 = -2 \\implies (2, -2)$।",
            "trap_alert": "$x = 0$ এবং $x = 2$ বের করে সরাসরি $(0, 2)$ এবং $(2, 0)$ অপশন দাগানো, কোটি $y$ এর সঠিক মান সমীকরণ থেকে হিসাব না করা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Horizontal Tangent Stationary Points",
            "source_book": "এস ইউ আহাম্মদ"
        },
        {
            "id": "w7_var_mat_05",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '22-23 Speed Hack",
            "q": "ফাংশন $f(x) = \\sin x + \\cos x$ এর সর্বোচ্চ মান (Maximum Value) কত?",
            "opts": [
                "$\\sqrt{2}$",
                "$2$",
                "$1$",
                "$\\frac{1}{\\sqrt{2}}$"
            ],
            "ans": 0,
            "exp": "$a\\sin x + b\\cos x$ আকারের ফাংশনের সর্বোচ্চ মান সর্বদা $\\sqrt{a^2 + b^2}$ এবং সর্বনিম্ন মান $-\\sqrt{a^2 + b^2}$। এখানে $a = 1, b = 1$, সুতরাং সর্বোচ্চ মান $= \\sqrt{1^2 + 1^2} = \\sqrt{2}$।",
            "trap_alert": "ত্রিকোণমিতিক সাইন ও কস এর সর্বোচ্চ মান ১+১=২ ভেবে ২ দাগানো।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Trigonometric Extrema Formula",
            "source_book": "কেতাবউদ্দিন স্যার"
        },
        {
            "id": "w7_var_mat_06",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '23-24 Core",
            "q": "$y = x^x$ হলে $x$-এর সাপেক্ষে এর অন্তরক সহগ $\\frac{dy}{dx}$ কত?",
            "opts": [
                "$x^x(1 + \\ln x)$",
                "$x \\cdot x^{x-1} = x^x$",
                "$x^x \\ln x$",
                "$x^{x-1}$"
            ],
            "ans": 0,
            "exp": "লগারিদমীয় অন্তরীকরণ: $\\ln y = x \\ln x$। উভয়পক্ষে অন্তরীকরণ করে: $\\frac{1}{y}\\frac{dy}{dx} = x \\cdot \\frac{1}{x} + \\ln x \\cdot 1 = 1 + \\ln x \\implies \\frac{dy}{dx} = y(1 + \\ln x) = x^x(1 + \\ln x)$।",
            "trap_alert": "চলকের ওপর চলক ঘাত থাকলে সাধারণ বীজগণিতীয় ঘাত সূত্র ($n x^{n-1}$) প্রয়োগ করে $x^x$ লিখে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Logarithmic Differentiation",
            "source_book": "অসীম সাহা স্যার"
        },
        {
            "id": "w7_var_mat_07",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '20-21 Repeat",
            "q": "$x = \\frac{\\pi}{4}$ বিন্দুতে $y = \\sin x$ এবং $y = \\cos x$ বক্ররেখাদ্বয়ের মধ্যবর্তী কোণ $\\theta$ কত?",
            "opts": [
                "$\\tan^{-1}(2\\sqrt{2})$",
                "$\\frac{\\pi}{4} = 45^\\circ$",
                "$\\frac{\\pi}{2} = 90^\\circ$",
                "$\\tan^{-1}(\\sqrt{2})$"
            ],
            "ans": 0,
            "exp": "$x = \\pi/4$ বিন্দুতে ১ম বক্ররেখার ঢাল $m_1 = \\cos(\\pi/4) = \\frac{1}{\\sqrt{2}}$। ২য় বক্ররেখার ঢাল $m_2 = -\\sin(\\pi/4) = -\\frac{1}{\\sqrt{2}}$। স্পর্শকদ্বয়ের মধ্যবর্তী কোণ: $\\tan\\theta = \\left|\\frac{m_1 - m_2}{1 + m_1 m_2}\\right| = \\left|\\frac{\\frac{1}{\\sqrt{2}} - (-\\frac{1}{\\sqrt{2}})}{1 + (\\frac{1}{\\sqrt{2}})(-\\frac{1}{\\sqrt{2}})}\\right| = \\frac{\\sqrt{2}}{1 - 1/2} = \\frac{\\sqrt{2}}{1/2} = 2\\sqrt{2} \\implies \\theta = \\tan^{-1}(2\\sqrt{2})$।",
            "trap_alert": "$m_1 m_2 = -1/2 \\neq -1$, সুতরাং বক্ররেখাদ্বয় লম্ব নয়; অন্ধভাবে $90^\\circ$ বা $45^\\circ$ দাগানো।",
            "yield_stars": 5,
            "probability": "96% DU Repeat",
            "intelligence_type": "Curve Intersection Angle Formula",
            "source_book": "এস ইউ আহাম্মদ"
        },
        {
            "id": "w7_var_mat_08",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '18-19 Repeat",
            "q": "পরাবৃত্ত $y^2 = 4ax$ এর $(at^2, 2at)$ বিন্দুতে অঙ্কিত অভিলম্বের সমীকরণ কোনটি?",
            "opts": [
                "$y + tx = 2at + at^3$",
                "$ty = x + at^2$",
                "$y - tx = 2at - at^3$",
                "$tx + y = 2at$"
            ],
            "ans": 0,
            "exp": "$2y \\frac{dy}{dx} = 4a \\implies \\frac{dy}{dx} = \\frac{2a}{y}$। $(at^2, 2at)$ বিন্দুতে স্পর্শকের ঢাল $m = \\frac{2a}{2at} = \\frac{1}{t}$। অতএব অভিলম্বের ঢাল $m_{\\text{norm}} = -t$। অভিলম্বের সমীকরণ: $y - 2at = -t(x - at^2) \\implies y - 2at = -tx + at^3 \\implies y + tx = 2at + at^3$।",
            "trap_alert": "স্পর্শকের সমীকরণ ($ty = x + at^2$) এবং অভিলম্বের সমীকরণের মধ্যে গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "97% DU Repeat",
            "intelligence_type": "Parametric Normal Equation",
            "source_book": "কেতাবউদ্দিন স্যার"
        },
        {
            "id": "w7_var_mat_09",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '21-22 Speed Hack",
            "q": "মান নির্ণয় কর: $\\lim_{x\\to 0} \\frac{e^{3x} - e^{-3x}}{\\sin 2x}$",
            "opts": [
                "$3$",
                "$0$",
                "$\\frac{3}{2}$",
                "$6$"
            ],
            "ans": 0,
            "exp": "লা'হসপিটাল প্রয়োগ করে: লবের অন্তরক $\\frac{d}{dx}(e^{3x} - e^{-3x}) = 3e^{3x} - (-3e^{-3x}) = 3e^{3x} + 3e^{-3x}$। হরের অন্তরক $\\frac{d}{dx}(\\sin 2x) = 2\\cos 2x$। $x = 0$ বসালে: $\\frac{3(1) + 3(1)}{2(1)} = \\frac{6}{2} = 3$।",
            "trap_alert": "লবে অন্তরীকরণের সময় $e^{-3x}$ এর চেইন রুলে ঋণাত্মক চিহ্ন $(-3)$ এসে $+3$ হয়—এখানে চিহ্ন ভুল করে লবে $3 - 3 = 0$ ধরে উত্তর শূন্য দাগানো।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Exponential Limit Sign Trap",
            "source_book": "অসীম সাহা স্যার"
        },
        {
            "id": "w7_var_mat_10",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '22-23 Core",
            "q": "একটি বৃত্তের ক্ষেত্রফলের পরিবর্তনের হার তার ব্যাসার্ধের সাপেক্ষে কত হবে, যখন ব্যাসার্ধ $r = 5\\text{ cm}$?",
            "opts": [
                "$10\\pi\\text{ cm}^2/\\text{cm}$",
                "$25\\pi\\text{ cm}^2/\\text{cm}$",
                "$5\\pi\\text{ cm}^2/\\text{cm}$",
                "$20\\pi\\text{ cm}^2/\\text{cm}$"
            ],
            "ans": 0,
            "exp": "ক্ষেত্রফল $A = \\pi r^2$। ব্যাসার্ধ $r$-এর সাপেক্ষে অন্তরীকরণ করলে: $\\frac{dA}{dr} = \\frac{d}{dr}(\\pi r^2) = 2\\pi r$। $r = 5\\text{ cm}$ বসালে: $\\frac{dA}{dr} = 2\\pi \\times 5 = 10\\pi\\text{ cm}^2/\\text{cm}$।",
            "trap_alert": "সময়ের সাপেক্ষে পরিবর্তনের হার ভেবে $\\frac{dr}{dt}$ খুঁজতে গিয়ে সময় নষ্ট করা অথবা $\\pi r^2 = 25\\pi$ দাগানো।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Derivative Rate of Change",
            "source_book": "এস ইউ আহাম্মদ"
        },
        {
            "id": "w7_var_mat_11",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '20-21 Speed Hack",
            "q": "যদি $y = \\sqrt{\\sin x + \\sqrt{\\sin x + \\sqrt{\\sin x + \\dots \\infty}}}$ হয়, তবে $\\frac{dy}{dx}$ এর মান কত?",
            "opts": [
                "$\\frac{\\cos x}{2y - 1}$",
                "$\\frac{\\cos x}{2y + 1}$",
                "$\\frac{-\\cos x}{2y - 1}$",
                "$\\frac{\\sin x}{2y - 1}$"
            ],
            "ans": 0,
            "exp": "অনন্ত ধারার শর্টকাট: $y = \\sqrt{f(x) + y} \\implies y^2 - y = f(x)$। অন্তরীকরণ করলে: $(2y - 1)\\frac{dy}{dx} = f'(x) \\implies \\frac{dy}{dx} = \\frac{f'(x)}{2y - 1}$। এখানে $f(x) = \\sin x$, তাই $f'(x) = \\cos x$। সুতরাং উত্তর $\\frac{\\cos x}{2y - 1}$।",
            "trap_alert": "হরের চিহ্নে $2y - 1$ এর জায়গায় $2y + 1$ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Infinite Radical Derivative Hack",
            "source_book": "কেতাবউদ্দিন স্যার"
        },
        {
            "id": "w7_var_mat_12",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '19-20 Direct",
            "q": "ব্যবধি $[1, 3]$ এ $f(x) = x^2 - 4x + 3$ ফাংশনটির জন্য রোলের উপপাদ্য (Rolle's Theorem) সিদ্ধকারী $c$ এর মান কত?",
            "opts": [
                "$2$",
                "$1.5$",
                "$2.5$",
                "$0$"
            ],
            "ans": 0,
            "exp": "রোলের শর্ত: $f(1) = 1 - 4 + 3 = 0$ এবং $f(3) = 9 - 12 + 3 = 0$, অর্থাৎ $f(1) = f(3)$। রোলের উপপাদ্য অনুসারে এমন একটি $c \\in (1, 3)$ থাকবে যেখানে $f'(c) = 0$। $f'(x) = 2x - 4 \\implies 2c - 4 = 0 \\implies c = 2 \\in (1, 3)$।",
            "trap_alert": None,
            "yield_stars": 5,
            "probability": "97% DU Direct",
            "intelligence_type": "Rolle's Theorem Point Calculation",
            "source_book": "এস ইউ আহাম্মদ"
        }
    ]

    # ==========================================
    # BIOLOGY (12 MCQs) - Chapters: মানব শারীরতত্ত্ব (সমন্বয় ও নিয়ন্ত্রণ), প্রাণীর আচরণ
    # ==========================================
    bio_mcqs = [
        {
            "id": "w7_var_bio_01",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '21-22 Repeat",
            "q": "অক্ষিগোলকের সুপিরিয়র অবলিক (Superior oblique) পেশির সঞ্চালন নিয়ন্ত্রণ করে কোন করোটিক স্নায়ু?",
            "opts": [
                "৪র্থ - ট্রকলিয়ার (Trochlear)",
                "৩য় - অকুলোমোটর (Oculomotor)",
                "৬ষ্ঠ - অ্যাবডুসেন্স (Abducens)",
                "২য় - অপটিক (Optic)"
            ],
            "ans": 0,
            "exp": "চোখের ৬টি বহিরাক্ষি পেশির মধ্যে সুপিরিয়র অবলিক পেশি নিয়ন্ত্রণ করে ৪র্থ করোটিক স্নায়ু ট্রকলিয়ার ($SO_4$)। ল্যাটেরাল রেকটাস নিয়ন্ত্রণ করে ৬ষ্ঠ স্নায়ু অ্যাবডুসেন্স ($LR_6$)। বাকি ৪টি পেশি নিয়ন্ত্রণ করে ৩য় স্নায়ু অকুলোমোটর ($[SO_4 LR_6]_3$ সূত্র)।",
            "trap_alert": "চোখের সাধারণ পেশি চালনাকারী ৩য় স্নায়ু অকুলোমোটর বা ৬ষ্ঠ অ্যাবডুসেন্সের সাথে সুপিরিয়র অবলিকের ট্রকলিয়ার গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Cranial Nerve Eye Muscle Rule",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_02",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '22-23 Repeat",
            "q": "মানব মস্তিষ্কের কোন অংশ হৃদস্পন্দন, রক্তচাপ, শ্বাসক্রিয়া ও গলধঃকরণ নিয়ন্ত্রণ করে?",
            "opts": [
                "মেডুলা অবলংগাটা (Medulla oblongata)",
                "সেরিবেলাম (Cerebellum)",
                "থ্যালামাস (Thalamus)",
                "হাইপোথ্যালামাস (Hypothalamus)"
            ],
            "ans": 0,
            "exp": "পশ্চাৎ মস্তিষ্কের মেডুলা অবলংগাটা হলো মানবদেহের স্বয়ংক্রিয় জীবন রক্ষাকারী কেন্দ্র; এটি হৃদস্পন্দন, রক্তচাপ, শ্বাস-প্রশ্বাস, লালাক্ষরণ, বমি ও গলধঃকরণ নিয়ন্ত্রণ করে। সেরিবেলাম দেহের ভারসাম্য রক্ষা করে এবং হাইপোথ্যালামাস দেহের তাপমাত্রা, ক্ষুধা ও তৃষ্ণা নিয়ন্ত্রণ করে।",
            "trap_alert": "দেহের তাপমাত্রা ও তৃষ্ণা নিয়ন্ত্রক হাইপোথ্যালামাসের সাথে শ্বাসক্রিয়া নিয়ন্ত্রক মেডুলা অবলংগাটা গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Brainstem Vital Center Matrix",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_03",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '20-21 Repeat",
            "q": "চোখের রেটিনার রড কোষে বিদ্যমান রোডপসিন (Rhodopsin) রঞ্জক কোন প্রোটিন ও ভিটামিনের সমন্বয়ে গঠিত?",
            "opts": [
                "স্কটোপসিন প্রোটিন ও রেটিনিন (ভিটামিন-এ এর অ্যালডিহাইড)",
                "আয়োডপসিন প্রোটিন ও ভিটামিন-সি",
                "ক্যারোটিনয়েড ও ভিটামিন-ডি",
                "অপসিন প্রোটিন ও ভিটামিন-ই"
            ],
            "ans": 0,
            "exp": "রড কোষে থাকে রোডপসিন যা অপসিন (স্কটোপসিন) প্রোটিন এবং ভিটামিন-এ এর অ্যালডিহাইড রেটিনিন (Retinal/Retinene) দ্বারা গঠিত। ভিটামিন-এ এর অভাবে রোডপসিন সংশ্লেষ ব্যাহত হওয়ায় রাতকানা (Nyctalopia) রোগ হয়। কোন কোষে থাকে আয়োডপসিন ও ফটোসিন।",
            "trap_alert": "কোন কোষের আয়োডপসিন এবং রড কোষের রোডপসিন এর নাম ও উপাদানে উল্টাপাল্টা করা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Photoreceptor Biochemistry",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_04",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '23-24 Core",
            "q": "মধ্যকর্ণের কোন ক্ষুদ্রতম অস্থিটি সরাসরি অন্তঃকর্ণের ফেনেস্ট্রা ওভালিসের (ডিম্বাকার গবাক্ষ) সাথে যুক্ত থাকে?",
            "opts": [
                "স্টেপিস (Stapes)",
                "ম্যালিয়াস (Malleus)",
                "ইনকাস (Incus)",
                "ককলিয়া (Cochlea)"
            ],
            "ans": 0,
            "exp": "মধ্যকর্ণের তিনটি ক্ষুদ্র অস্থির ক্রম: ম্যালিয়াস $\\to$ ইনকাস $\\to$ স্টেপিস (শর্টকাট: MIS)। ম্যালিয়াস টিম্প্যানিক পর্দার সাথে যুক্ত থাকে এবং স্টেপিস (মানবদেহের ক্ষুদ্রতম অস্থি) ফেনেস্ট্রা ওভালিসের গায়ে যুক্ত থেকে শব্দতরঙ্গ ২০ গুণ বিবর্ধিত করে অন্তঃকর্ণের পেরিলিম্ফে পাঠায়।",
            "trap_alert": "টিম্প্যানিক পর্দায় যুক্ত ম্যালিয়াস এবং ফেনেস্ট্রা ওভালিসে যুক্ত স্টেপিস এর অবস্থান গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Ear Ossicles Sequence",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_05",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '19-20 Repeat",
            "q": "পিটুইটারি গ্রন্থির পশ্চাৎ খণ্ড (নিউরোহাইপোফাইসিস) হতে নিঃসৃত হয় কোন হরমোনদ্বয়?",
            "opts": [
                "অক্সিটোসিন ও ভেসোপ্রেসিন (ADH)",
                "ACTH ও TSH",
                "গ্রোথ হরমোন (GH) ও প্রোল্যাকটিন",
                "FSH ও LH"
            ],
            "ans": 0,
            "exp": "অক্সিটোসিন এবং অ্যান্টিডাইইউরেটিক হরমোন (ADH বা ভেসোপ্রেসিন) হাইপোথ্যালামাসের নিউরোসিক্রেটরি কোষে তৈরি হয় এবং পিটুইটারির পশ্চাৎ খণ্ডে জমা থেকে রক্তে নিঃসৃত হয়। ACTH, TSH, GH, FSH, LH পিটুইটারির অগ্র খণ্ড (অ্যাডেনোহাইপোফাইসিস) হতে নিঃসৃত হয়।",
            "trap_alert": "অগ্র পিটুইটারি ও পশ্চাৎ পিটুইটারির হরমোন তালিকার মধ্যে বিভ্রান্তি।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Pituitary Hormone Secretion Origin",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_06",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '21-22 Repeat",
            "q": "অগ্ন্যাশয়ের আইলেটস অব ল্যাঙ্গারহ্যান্সের বিটা ($\\beta$) কোষ থেকে নিঃসৃত ইনসুলিন কোন প্রক্রিয়ায় রক্তে গ্লুকোজের মাত্রা কমায়?",
            "opts": [
                "গ্লাইকোজেনেসিস (গ্লুকোজ হতে গ্লাইকোজেন তৈরি)",
                "গ্লাইকোজেনোলাইসিস (গ্লাইকোজেন ভেঙে গ্লুকোজ তৈরি)",
                "গ্লুকোনিওজেনেসিস (অশর্করা হতে গ্লুকোজ তৈরি)",
                "লাইপোলাইসিস"
            ],
            "ans": 0,
            "exp": "ইনসুলিন যকৃত ও পেশিকোষে গ্লাইকোজেনেসিস প্রক্রিয়ায় অতিরিক্ত গ্লুকোজকে গ্লাইকোজেনে রূপান্তর করে জমা রাখে এবং কোষে গ্লুকোজ প্রবেশ ত্বরান্বিত করে। বিপরীতে আলফা কোষ নিঃসৃত গ্লুকাগন গ্লাইকোজেনোলাইসিস ঘটিয়ে রক্তে গ্লুকোজ বাড়ায়।",
            "trap_alert": "গ্লাইকোজেনেসিস (ইনসুলিন) এবং গ্লাইকোজেনোলাইসিস (গ্লুকাগন) এর বিপরীতমুখী ক্রিয়া বিপরীতভাবে দাগানো।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Endocrine Blood Sugar Regulation",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_07",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "প্রাণীর আচরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '22-23 Core",
            "q": "প্রাণীর সহজাত আচরণের অন্তর্ভুক্ত এফএপি (Fixed Action Pattern - FAP) এর মূল বৈশিষ্ট্য কোনটি?",
            "opts": [
                "নির্দিষ্ট সাইন স্টিমুলাস (Sign stimulus) দ্বারা উদ্দীপিত ও অপরিবর্তনীয়",
                "বারবার অনুশীলনের মাধ্যমে ব্যক্তি-নির্দিষ্টভাবে অর্জিত",
                "অনভ্যাসের ফলে সহজেই বিলুপ্ত হয়",
                "মস্তিষ্কের উন্নত সেরিব্রাল কর্টেক্স দ্বারা নিয়ন্ত্রিত"
            ],
            "ans": 0,
            "exp": "FAP হলো জিন নিয়ন্ত্রিত সহজাত স্টিরিওটাইপড আচরণ যা একটি নির্দিষ্ট উদ্দীপক (Sign stimulus) দ্বারা শুরু হলে প্রাণী তা না থেমে শেষ পর্যন্ত সম্পন্ন করে (যেমন: নিকো টিনবার্জেনের তিন কাঁটাযুক্ত পুরুষ স্টিকলব্যাক মাছের লাল পেট দেখে আক্রমণাত্মক আচরণ)।",
            "trap_alert": "সহজাত আচরণ FAP কে অর্জিত বা কন্ডিশনিং আচরণের সাথে মিলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "97% DU Core",
            "intelligence_type": "FAP Innate Behavior Hallmarks",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_08",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "প্রাণীর আচরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '20-21 Repeat",
            "q": "আইভান প্যাভলভের সাপেক্ষ প্রতিবর্ত ক্রিয়ার পরীক্ষায় 'ঘণ্টাধ্বনি' কী হিসেবে কাজ করে?",
            "opts": [
                "অনুবন্ধিত উদ্দীপক (Conditioned Stimulus - CS)",
                "অননুবন্ধিত উদ্দীপক (Unconditioned Stimulus - UCS)",
                "অনুবন্ধিত সাড়া (Conditioned Response - CR)",
                "অননুবন্ধিত সাড়া (Unconditioned Response - UCR)"
            ],
            "ans": 0,
            "exp": "প্যাভলভের পরীক্ষায় খাদ্য হলো অননুবন্ধিত স্বাভাবিক উদ্দীপক (UCS), খাদ্য দেখে লালাক্ষরণ অননুবন্ধিত স্বাভাবিক সাড়া (UCR)। ঘণ্টার শব্দ কৃত্রিম বা অনুবন্ধিত উদ্দীপক (CS) এবং ঘণ্টার শব্দ শুনেই লালাক্ষরণ হলো অনুবন্ধিত সাড়া (CR)।",
            "trap_alert": "ঘণ্টার শব্দকে অননুবন্ধিত উদ্দীপক (UCS) ভেবে ভুল করা।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Pavlov Classical Conditioning Mapping",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_09",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "প্রাণীর আচরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '19-20 Direct",
            "q": "ফসলের ক্ষেতে স্থাপিত কাকতাড়ুয়াকে ক্ষতিকর নয় জেনে প্রথম দিকে ভয় পেলেও পরবর্তীতে পাখি কর্তৃক অবজ্ঞা করার আচরণ কোন ধরনের শিখন?",
            "opts": [
                "অভ্যাসগত আচরণ (Habituation)",
                "অনুবন্ধন (Conditioning)",
                "অন্তর্দৃষ্টি (Insight learning)",
                "অনুকরণ (Imprinting)"
            ],
            "ans": 0,
            "exp": "কোনো উদ্দীপক বারবার উপস্থাপিত হলেও তার দ্বারা কোনো ক্ষতি বা পুরস্কার না ঘটলে প্রাণী ধীরে ধীরে সাড়া প্রদান বন্ধ করে দেয়। এটি সবচেয়ে সরল শিখন আচরণ যার নাম হ্যাবিচুয়েশন বা অভ্যাসগত আচরণ।",
            "trap_alert": None,
            "yield_stars": 5,
            "probability": "98% DU Direct",
            "intelligence_type": "Habituation Behavior Paradigm",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_10",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "DU '21-22 Speed Hack",
            "q": "১২ জোড়া করোটিক স্নায়ুর মধ্যে কোনগুলো সম্পূর্ণ 'মিশ্র স্নায়ু' (Mixed Nerves)?",
            "opts": [
                "৫ম (Trigeminal), ৭ম (Facial), ৯ম (Glossopharyngeal), ১০ম (Vagus)",
                "১ম (Olfactory), ২য় (Optic), ৮ম (Auditory)",
                "৩য় (Oculomotor), ৪র্থ (Trochlear), ৬ষ্ঠ (Abducens)",
                "১১শ (Spinal Accessory), ১২শ (Hypoglossal)"
            ],
            "ans": 0,
            "exp": "করোটিক স্নায়ুর প্রকৃতির সুপার স্পিড হ্যাক: সংবেদী স্নায়ু = ১, ২, ৮ (Olfactory, Optic, Auditory)। চেষ্টিয়/মোটর স্নায়ু = ৩, ৪, ৬, ১১, ১২। মিশ্র স্নায়ু = ৫, ৭, ৯, ১০ (Trigeminal, Facial, Glossopharyngeal, Vagus)।",
            "trap_alert": "৮ম অডিটরি স্নায়ুকে মিশ্র স্নায়ুর সাথে মিলিয়ে ফেলা; এটি সম্পূর্ণ সংবেদী স্নায়ু।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Cranial Nerve Modality Matrix",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_11",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '18-19 Repeat",
            "q": "শ্রবণের প্রধান গ্রাহক অঙ্গ 'অর্গান অব কর্টি' (Organ of Corti) অন্তঃকর্ণের ককলিয়ার কোন নালীর উপর অবস্থিত?",
            "opts": [
                "স্কালা মিডিয়া (ককলিয়ার নালী)",
                "স্কালা ভেস্টিবুলি",
                "স্কালা টিম্প্যানি",
                "অর্ধবৃত্তাকার নালী"
            ],
            "ans": 0,
            "exp": "ককলিয়ার কেন্দ্রীয় নালী হলো স্কালা মিডিয়া যা এন্ডোলিম্ফ তরলে পূর্ণ। স্কালা মিডিয়ার মেমব্রেনা ব্যাসিলারিসের উপর শ্রবণ সংবেদী লোমযুক্ত কোষ সমন্বিত অর্গান অব কর্টি অবস্থিত। স্কালা ভেস্টিবুলি ও টিম্প্যানিতে পেরিলিম্ফ থাকে।",
            "trap_alert": "স্কালা মিডিয়ার সাথে স্কালা ভেস্টিবুলি বা টিম্প্যানি গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "97% DU Repeat",
            "intelligence_type": "Cochlea Hearing Organ Anatomy",
            "source_book": "গাজী আজমল স্যার"
        },
        {
            "id": "w7_var_bio_12",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "DU '20-21 Direct",
            "q": "জরুরি অবস্থায় বা বিপদের মুখোমুখি হলে মানবদেহে 'Fight or Flight' প্রতিক্রিয়া শুরু করতে কোন অন্তঃক্ষরা গ্রন্থি থেকে অ্যাড্রেনালিন নিঃসৃত হয়?",
            "opts": [
                "অ্যাড্রেনাল মেডুলা",
                "অ্যাড্রেনাল কর্টেক্স",
                "থাইরয়েড গ্রন্থি",
                "প্যারাথাইরয়েড গ্রন্থি"
            ],
            "ans": 0,
            "exp": "অ্যাড্রেনাল (সুপ্রারেনাল) গ্রন্থির ভেতরের অংশ মেডুলা হতে সংকটকালীন হরমোন অ্যাড্রেনালিন (এপিনেফ্রিন) ও নর-অ্যাড্রেনালিন নিঃসৃত হয় যা হৃদস্পন্দন ও রক্তচাপ দ্রুত বাড়িয়ে জরুরি পরিস্থিতি মোকাবেলায় দেহকে প্রস্তুত করে। অ্যাড্রেনাল কর্টেক্স হতে কর্টিসোল ও অ্যালডোস্টেরন নিঃসৃত হয়।",
            "trap_alert": None,
            "yield_stars": 5,
            "probability": "98% DU Direct",
            "intelligence_type": "Adrenal Emergency Axis",
            "source_book": "গাজী আজমল স্যার"
        }
    ]

    questions.extend(phy_mcqs)
    questions.extend(che_mcqs)
    questions.extend(mat_mcqs)
    questions.extend(bio_mcqs)

    # Standardize duplicate aliases
    for q in questions:
        q["question"] = q["q"]
        q["options"] = list(q["opts"])
        q["correct_index"] = q["ans"]
        q["explanation"] = q["exp"]
        q["trap"] = q["trap_alert"]

    return questions


def get_du_written_problems():
    problems = [
        # PHYSICS (4)
        {
            "subject": "Physics",
            "tag": "DU Written Special",
            "problem": "$10\\text{ cm}$ ব্যাসার্ধবিশিষ্ট একটি ফাঁপা ধাতব গোলকে $+20\\text{ nC}$ চার্জ দেওয়া হলো। (ক) গোলকের কেন্দ্র থেকে $5\\text{ cm}$, $10\\text{ cm}$ এবং $20\\text{ cm}$ দূরত্বে তড়িৎ বিভবের মান কত? (খ) কেন্দ্র থেকে $5\\text{ cm}$ দূরত্বে তড়িৎ প্রাবল্যের মান কত? [ধরি $\\frac{1}{4\\pi\\epsilon_0} = 9 \\times 10^9\\text{ N m}^2\\text{ C}^{-2}$]",
            "marks": 3.5,
            "solution": "(ক) গোলকের পৃষ্ঠের ব্যাসার্ধ $R = 10\\text{ cm} = 0.1\\text{ m}$। পৃষ্ঠের বিভব $V_{\\text{surf}} = \\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{R} = 9 \\times 10^9 \\times \\frac{20 \\times 10^{-9}}{0.1} = \\frac{180}{0.1} = 1800\\text{ V}$। যেহেতু পরিবাহী গোলকের অভ্যন্তর সমবিভব সম্পন্ন, কেন্দ্র থেকে $5\\text{ cm}$ দূরত্বে বিভব $V = V_{\\text{surf}} = 1800\\text{ V}$। পৃষ্ঠে ($10\\text{ cm}$) বিভব $V = 1800\\text{ V}$। বহিঃস্থ বিন্দু $r = 20\\text{ cm} = 0.2\\text{ m}$ এ বিভব $V = \\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{r} = 9 \\times 10^9 \\times \\frac{20 \\times 10^{-9}}{0.2} = 900\\text{ V}$। (খ) পরিবাহীর অভ্যন্তরে কোনো মুক্ত চার্জ না থাকায় কেন্দ্র থেকে $5\\text{ cm}$ দূরত্বে তড়িৎ প্রাবল্য $E = 0\\text{ N/C}$।",
            "rubric": "অভ্যন্তরে ও পৃষ্ঠের বিভব নির্ণয় ($1800\\text{ V}$): ১.৫ | বাইরের বিন্দুর বিভব ($900\\text{ V}$): ১.০ | অভ্যন্তরে প্রাবল্য শূন্য ($E=0$) যুক্তি সহ: ১.০"
        },
        {
            "subject": "Physics",
            "tag": "DU Written Special",
            "problem": "একটি সমান্তরাল পাত ধারকের প্রতি পাতের ক্ষেত্রফল $0.02\\text{ m}^2$ এবং পাতদ্বয়ের মধ্যবর্তী দূরত্ব $1\\text{ mm}$। পাতদ্বয়ের মধ্যবর্তী স্থান $\\kappa = 4$ পরাবৈদ্যুতিক ধ্রুবকের মাধ্যম দ্বারা পূর্ণ করে $100\\text{ V}$ ব্যাটারির সাথে যুক্ত করা হলো। ধারকটিতে সঞ্চিত শক্তির পরিমাণ এবং প্রতি একক আয়তনে সঞ্চিত শক্তির মান নির্ণয় কর। [$\\epsilon_0 = 8.854 \\times 10^{-12}\\text{ C}^2\\text{ N}^{-1}\\text{ m}^{-2}$]",
            "marks": 2.5,
            "solution": "ধারকত্ব $C = \\frac{\\kappa \\epsilon_0 A}{d} = \\frac{4 \\times 8.854 \\times 10^{-12} \\times 0.02}{10^{-3}} = 4 \\times 8.854 \\times 10^{-12} \\times 20 = 7.083 \\times 10^{-10}\\text{ F}$। সঞ্চিত শক্তি $U = \\frac{1}{2} C V^2 = \\frac{1}{2} \\times 7.083 \\times 10^{-10} \\times (100)^2 = 3.54 \\times 10^{-6}\\text{ J}$। আয়তন $v = A \\cdot d = 0.02 \\times 10^{-3} = 2 \\times 10^{-5}\\text{ m}^3$। একক আয়তনে শক্তি $u = \\frac{U}{v} = \\frac{3.54 \\times 10^{-6}}{2 \\times 10^{-5}} = 0.177\\text{ J/m}^3$।",
            "rubric": "ধারকত্ব $C$ নির্ণয়: ১.০ | মোট শক্তি $U$: ১.০ | শক্তি ঘনত্ব $u$: ০.৫"
        },
        {
            "subject": "Physics",
            "tag": "DU Written Special",
            "problem": "একটি মহাশূন্যযান কত বেগে চললে পৃথিবীতে অবস্থানরত পর্যবেক্ষকের কাছে মহাশূন্যযানের ঘড়ির ১ ঘণ্টা পৃথিবীর ঘড়ির ২ ঘণ্টার সমান মনে হবে? এ অবস্থায় $100\\text{ m}$ দৈর্ঘ্যবিশিষ্ট যানটির আপাত দৈর্ঘ্য কত হবে?",
            "marks": 3.0,
            "solution": "কাল দীর্ঘায়ন: $t = \\frac{t_0}{\\sqrt{1 - \\frac{v^2}{c^2}}}$। এখানে $t_0 = 1\\text{ hr}, t = 2\\text{ hr}$। $\\implies 2 = \\frac{1}{\\sqrt{1 - \\frac{v^2}{c^2}}} \\implies \\sqrt{1 - \\frac{v^2}{c^2}} = \\frac{1}{2} \\implies 1 - \\frac{v^2}{c^2} = \\frac{1}{4} \\implies v = \\frac{\\sqrt{3}}{2}c \\approx 0.866c$ ($2.60 \\times 10^8\\text{ m/s}$)। দৈর্ঘ্য সংকোচন: $L = L_0 \\sqrt{1 - \\frac{v^2}{c^2}} = 100 \\times \\frac{1}{2} = 50\\text{ m}$।",
            "rubric": "বেগ $v = \\frac{\\sqrt{3}}{2}c$ নির্ণয়: ২.০ | আপাত দৈর্ঘ্য $L = 50\\text{ m}$ নির্ণয়: ১.০"
        },
        {
            "subject": "Physics",
            "tag": "DU Written Special",
            "problem": "একটি ধাতুর সূচনা তরঙ্গদৈর্ঘ্য $\\lambda_0 = 5000\\text{ \\AA}$। ধাতুটির উপর $2500\\text{ \\AA}$ তরঙ্গদৈর্ঘ্যের আলো আপতিত হলে নির্গত ফটোইলেকট্রনের সর্বোচ্চ গতিশক্তি ($\\text{eV}$ এককে) এবং নিবৃত্তি বিভব ($V_s$) নির্ণয় কর। [$hc = 12400\\text{ eV}\\cdot\\text{\\AA}$]",
            "marks": 2.5,
            "solution": "ধাতুটির কার্যপেক্ষক $W_0 = \\frac{hc}{\\lambda_0} = \\frac{12400}{5000} = 2.48\\text{ eV}$। আপতিত ফোটনের শক্তি $E = \\frac{hc}{\\lambda} = \\frac{12400}{2500} = 4.96\\text{ eV}$। সর্বোচ্চ গতিশক্তি $K_{\\max} = E - W_0 = 4.96 - 2.48 = 2.48\\text{ eV}$ ($3.97 \\times 10^{-19}\\text{ J}$)। নিবৃত্তি বিভব $V_s$: $e V_s = K_{\\max} \\implies V_s = 2.48\\text{ V}$।",
            "rubric": "কার্যপেক্ষক ও ফোটন শক্তি: ১.০ | সর্বোচ্চ গতিশক্তি: ১.০ | নিবৃত্তি বিভব: ০.৫"
        },

        # CHEMISTRY (4)
        {
            "subject": "Chemistry",
            "tag": "DU Written Special",
            "problem": "$\\text{C}_4\\text{H}_8$ আণবিক সংকেতযুক্ত অ্যালকিনসমূহের সকল সম্ভাব্য সমাণুর গাঠনিক সংকেত লেখ। এদের মধ্যে কোনটি জ্যামিতিক সমাণুতা প্রদর্শন করে এবং কেন? এর cis ও trans সমাণুর গঠন দেখাও।",
            "marks": 3.0,
            "solution": "$\\text{C}_4\\text{H}_8$ অ্যালকিনের মুক্ত শিকল সমাণু ৩টি: ১. $\\text{CH}_3-\\text{CH}_2-\\text{CH}=\\text{CH}_2$ (বাট-১-ইন), ২. $\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3$ (বাট-২-ইন), ৩. $\\text{CH}_3-\\text{C}(\\text{CH}_3)=\\text{CH}_2$ (২-মিথাইলপ্রোপ-১-ইন)। বাট-২-ইন জ্যামিতিক সমাণুতা দেখায় কারণ দ্বিবন্ধনযুক্ত কার্বনদ্বয়ের প্রতিটিতে দুটি ভিন্ন পরমাণু/মূলক ($-\\text{H}$ ও $-\\text{CH}_3$) রয়েছে। Cis-বাট-২-ইন: দুটি $-\\text{CH}_3$ মূলক দ্বিবন্ধনের একই পাশে। Trans-বাট-২-ইন: দুটি $-\\text{CH}_3$ মূলক দ্বিবন্ধনের বিপরীত পাশে।",
            "rubric": "৩টি সমাণুর সঠিক সংকেত: ১.০ | বাট-২-ইন নির্বাচন ও শর্ত ব্যাখ্যা: ১.০ | Cis ও Trans গঠন প্রদর্শন: ১.০"
        },
        {
            "subject": "Chemistry",
            "tag": "DU Written Special",
            "problem": "ল্যাকটিক এসিড ($\\text{CH}_3-\\text{CH(OH)}-\\text{COOH}$) কেন আলোক সমাণুতা প্রদর্শন করে? এর d- ও l- সমাণুর গাঠনিক রূপ দেখাও। সমমোলার $d$ ও $l$ সমাণুর মিশ্রণ কেন আলোক নিষ্ক্রিয় হয়?",
            "marks": 2.5,
            "solution": "ল্যাকটিক এসিডের কেন্দ্রীয় কার্বনের সাথে চারটি ভিন্ন পরমাণু/মূলক ($-\\text{H}, -\\text{OH}, -\\text{CH}_3, -\\text{COOH}$) যুক্ত থাকায় এটি একটি কাইরাল বা অপ্রতিসম কার্বন ($C^*$) কেন্দ্র। অপ্রতিসম কেন্দ্র ও অপরস্পরস্থাপনীয় দর্পণ প্রতিবিম্ব হওয়ার কারণে এটি আলোক সক্রিয়। $d$-ল্যাকটিক এসিড সমতল সমবর্তিত আলোর তলকে ডানদিকে এবং $l$-ল্যাকটিক এসিড বামদিকে আবর্তন করে। সমমোলার মিশ্রণে একটি সমাণুর ডান ঘূর্ণন অপরটির বাম ঘূর্ণন দ্বারা ঠিক সমানভাবে নিষ্ক্রিয় হয় (বাহ্যিক ক্ষতিপূরণ / External Compensation)। ফলে সৃষ্ট রেসিমিক মিশ্রণ আলোক নিষ্ক্রিয়।",
            "rubric": "কাইরাল কার্বনের ব্যাখ্যা ও গঠন: ১.০ | $d$ ও $l$ রূপ প্রদর্শন: ০.৫ | বাহ্যিক ক্ষতিপূরণ ও রেসিমিক ব্যাখ্যা: ১.০"
        },
        {
            "subject": "Chemistry",
            "tag": "DU Written Special",
            "problem": "প্রোপিনের সাথে $\\text{HBr}$ এর যুত বিক্রিয়ায় প্রধান উৎপাদ হিসেবে ২-ব্রোমোপ্রোপেন তৈরি হয় কিন্তু ১-ব্রোমোপ্রোপেন নগণ্য থাকে কেন? মারকভনিকভের নীতি ও কার্বোক্যাটায়নের স্থায়িত্বের মাধ্যমে ব্যাখ্যা কর।",
            "marks": 3.0,
            "solution": "প্রোপিন ($\\text{CH}_3-\\text{CH}=\\text{CH}_2$) একটি অপ্রতিসম অ্যালকিন। ইলেক্ট্রোফাইল $\\text{H}^+$ যুক্ত হয়ে দুটি সম্ভাব্য কার্বোক্যাটায়ন তৈরি করতে পারে: ১. প্রান্তীয় কার্বনে $\\text{H}^+$ যুক্ত হলে ২-ডিগ্রি কার্বোক্যাটায়ন তৈরি হয়: $\\text{CH}_3-\\text{C}^+\\text{H}-\\text{CH}_3$। ২. মধ্যবর্তী কার্বনে $\\text{H}^+$ যুক্ত হলে ১-ডিগ্রি কার্বোক্যাটায়ন তৈরি হয়: $\\text{CH}_3-\\text{CH}_2-\\text{C}^+\\text{H}_2$। যেহেতু দুটি অ্যালকাইল মূলকের $+I$ আবেশীয় প্রভাব ও হাইপারকনজুগেশনের কারণে $2^\\circ$ কার্বোক্যাটায়ন $1^\\circ$ কার্বোক্যাটায়ন অপেক্ষা অধিক সুস্থিত, তাই নিউক্লিওফাইল $\\text{Br}^-$ দ্রুত $2^\\circ$ কার্বোক্যাটায়নে আক্রমণ করে। ফলে ৯১% প্রধান উৎপাদ হিসেবে ২-ব্রোমোপ্রোপেন উৎপন্ন হয়।",
            "rubric": "মারকভনিকভ নীতি ও সমীকরণ: ১.০ | $1^\\circ$ বনাম $2^\\circ$ কার্বোক্যাটায়ন গঠন: ১.০ | স্থায়িত্বের ব্যাখ্যা ও ২-ব্রোমোপ্রোপেন সিদ্ধান্ত: ১.০"
        },
        {
            "subject": "Chemistry",
            "tag": "DU Written Special",
            "problem": "টলুইনের নাইট্রেশনে অর্থো ও প্যারা উৎপাদ গঠিত হয় কিন্তু নাইট্রোবেনজিনের নাইট্রেশনে মেটা উৎপাদ গঠিত হয় কেন? উপযুক্ত অনুনাদন (Resonance) কাঠামোর সাহায্যে ব্যাখ্যা কর।",
            "marks": 2.5,
            "solution": "টলুইনে মিথাইল মূলক ($-\\text{CH}_3$) একটি ইলেকট্রন দাতা মূলক (অর্থো-প্যারা নির্দেশক)। হাইপারকনজুগেশন ও $+I$ প্রভাবের কারণে বেনজিন বলয়ের ২, ৪, ৬ (অর্থো ও প্যারা) অবস্থানে ইলেকট্রন ঘনত্ব মেটা অবস্থানের চেয়ে অনেক বৃদ্ধি পায়। ফলে আক্রমণকারী ইলেক্ট্রোফাইল $\\text{NO}_2^+$ অর্থো ও প্যারা অবস্থানে যুক্ত হয়। অপরদিকে নাইট্রোবেনজিনে নাইট্রো মূলক ($-\\text{NO}_2$) একটি তীব্র ইলেকট্রন আকর্ষী মূলক (মেটা নির্দেশক)। $-M$ মেসোমারিক প্রভাবের কারণে বলয় থেকে পাই ইলেকট্রন টেনে নেওয়ায় অর্থো ও প্যারা অবস্থানে ইলেকট্রন ঘাটতি চরম আকার ধারণ করে। তুলনামূলকভাবে মেটা অবস্থানে ইলেকট্রন ঘনত্ব কিছুটা বেশি থাকায় ইলেক্ট্রোফাইল কেবল মেটা অবস্থানে আক্রমণ করে।",
            "rubric": "টলুইনের $+I$/হাইপারকনজুগেশন ও অর্থো-প্যারা ব্যাখ্যা: ১.০ | নাইট্রোবেনজিনের $-M$ ও মেটা ব্যাখ্যা: ১.০ | রেজোন্যান্স প্রভাবের উল্লেখ: ০.৫"
        },

        # HIGHER MATH (4)
        {
            "subject": "Higher Math",
            "tag": "DU Written Special",
            "problem": "মান নির্ণয় কর: (ক) $\\lim_{x\\to 0} \\frac{x - \\sin x}{x^3}$ (খ) $\\lim_{x\\to 0} \\left(\\frac{\\sin x}{x}\\right)^{1/x^2}$",
            "marks": 2.5,
            "solution": "(ক) $\\lim_{x\\to 0}\\frac{x - \\sin x}{x^3}$ [$\\frac{0}{0}$ আকার]। লা'হসপিটালের নিয়ম প্রয়োগ করে: $\\lim_{x\\to 0}\\frac{1 - \\cos x}{3x^2}$। আবার লা'হসপিটাল প্রয়োগ করে: $\\lim_{x\\to 0}\\frac{\\sin x}{6x} = \\frac{1}{6} \\lim_{x\\to 0}\\frac{\\sin x}{x} = \\frac{1}{6}$। (খ) ধরি $y = \\lim_{x\\to 0}\\left(\\frac{\\sin x}{x}\\right)^{1/x^2}$। $\\ln y = \\lim_{x\\to 0}\\frac{\\ln(\\sin x / x)}{x^2}$। ম্যাকলরিন ধারা $\\frac{\\sin x}{x} = 1 - \\frac{x^2}{6} + \\dots \\implies \\ln\\left(1 - \\frac{x^2}{6}\\right) \\approx -\\frac{x^2}{6}$। $\\implies \\ln y = \\lim_{x\\to 0}\\frac{-x^2/6}{x^2} = -\\frac{1}{6} \\implies y = e^{-1/6}$।",
            "rubric": "(ক) অংশ লা'হসপিটাল ও মান $\\frac{1}{6}$: ১.০ | (খ) অংশ লগারিদম ও লিমিট মান $e^{-1/6}$: ১.৫"
        },
        {
            "subject": "Higher Math",
            "tag": "DU Written Special",
            "problem": "$x^2 - xy + y^2 = 3$ বক্ররেখার কোন কোন বিন্দুতে অঙ্কিত স্পর্শক $x$-অক্ষের সমান্তরাল হবে? বিন্দুসমূহ এবং স্পর্শকের সমীকরণ নির্ণয় কর।",
            "marks": 3.0,
            "solution": "উভয়পক্ষে $x$-এর সাপেক্ষে অন্তরীকরণ করে: $2x - (y + x\\frac{dy}{dx}) + 2y\\frac{dy}{dx} = 0 \\implies \\frac{dy}{dx}(2y - x) = y - 2x \\implies \\frac{dy}{dx} = \\frac{y - 2x}{2y - x}$। স্পর্শক $x$-অক্ষের সমান্তরাল হওয়ার শর্ত: $\\frac{dy}{dx} = 0 \\implies y - 2x = 0 \\implies y = 2x$। মূল সমীকরণে $y = 2x$ বসিয়ে পাই: $x^2 - x(2x) + (2x)^2 = 3 \\implies 3x^2 = 3 \\implies x = \\pm 1$। যখন $x = 1$, $y = 2$; বিন্দুটি $(1, 2)$ এবং স্পর্শকের সমীকরণ $y = 2$। যখন $x = -1$, $y = -2$; বিন্দুটি $(-1, -2)$ এবং স্পর্শকের সমীকরণ $y = -2$।",
            "rubric": "অন্তরীকরণ $\\frac{dy}{dx}$ নির্ণয়: ১.০ | $y = 2x$ শর্ত ও বিন্দুদ্বয় নির্ণয়: ১.০ | স্পর্শকের সমীকরণ: ১.০"
        },
        {
            "subject": "Higher Math",
            "tag": "DU Written Special",
            "problem": "$R$ ব্যাসার্ধের একটি বৃত্তে অন্তর্লিখিত বৃহত্তম ক্ষেত্রফলবিশিষ্ট আয়তক্ষেত্রের ক্ষেত্রফল এবং এর বাহুদ্বয়ের দৈর্ঘ্য নির্ণয় কর।",
            "marks": 3.5,
            "solution": "ধরি আয়তক্ষেত্রের দৈর্ঘ্য $x$ এবং প্রস্থ $y$। বৃত্তে অন্তর্লিখিত হওয়ায় কর্ণ বৃত্তের ব্যাসের সমান ($2R$): $x^2 + y^2 = 4R^2 \\implies y = \\sqrt{4R^2 - x^2}$। ক্ষেত্রফল $A = xy = x\\sqrt{4R^2 - x^2}$। ক্ষেত্রফলের বর্গ $S = A^2 = 4R^2 x^2 - x^4$ বিবেচনা করি। চরম মানের জন্য $\\frac{dS}{dx} = 8R^2 x - 4x^3 = 0 \\implies 4x(2R^2 - x^2) = 0$। যেহেতু $x > 0$, তাই $x^2 = 2R^2 \\implies x = \\sqrt{2}R$। তখন $y = \\sqrt{4R^2 - 2R^2} = \\sqrt{2}R$। দ্বিতীয় অন্তরক: $\\frac{d^2S}{dx^2} = 8R^2 - 12x^2 = 8R^2 - 24R^2 = -16R^2 < 0$, সুতরাং ক্ষেত্রফল সর্বোচ্চ। আয়তক্ষেত্রটি একটি বর্গক্ষেত্র এবং সর্বোচ্চ ক্ষেত্রফল $A_{\\max} = (\\sqrt{2}R)(\\sqrt{2}R) = 2R^2$ বর্গ একক।",
            "rubric": "কর্ণের সমীকরণ ও ক্ষেত্রফলের অপেক্ষক গঠন: ১.০ | ১ম অন্তরক ও বাহুর মান $x = \\sqrt{2}R$: ১.০ | ২য় অন্তরক পরীক্ষা: ০.৫ | সর্বোচ্চ ক্ষেত্রফল $2R^2$: ১.০"
        },
        {
            "subject": "Higher Math",
            "tag": "DU Written Special",
            "problem": "যদি $y = (x + \\sqrt{1 + x^2})^m$ হয়, তবে প্রমাণ কর যে, $(1 + x^2)y_2 + x y_1 - m^2 y = 0$।",
            "marks": 3.0,
            "solution": "$y = (x + \\sqrt{1 + x^2})^m$। ১ম অন্তরীকরণ করে: $y_1 = m(x + \\sqrt{1 + x^2})^{m-1} \\left(1 + \\frac{x}{\\sqrt{1 + x^2}}\\right) = m(x + \\sqrt{1 + x^2})^{m-1} \\left(\\frac{\\sqrt{1 + x^2} + x}{\\sqrt{1 + x^2}}\\right) = \\frac{m(x + \\sqrt{1 + x^2})^m}{\\sqrt{1 + x^2}} = \\frac{my}{\\sqrt{1 + x^2}}$। $\\implies \\sqrt{1 + x^2}y_1 = my$। বর্গ করে: $(1 + x^2) y_1^2 = m^2 y^2$। পুনরায় অন্তরীকরণ করে: $2x y_1^2 + (1 + x^2) 2y_1 y_2 = m^2 \\cdot 2y y_1$। উভয়পক্ষকে $2y_1$ দ্বারা ভাগ করে ($y_1 \\neq 0$): $(1 + x^2)y_2 + x y_1 = m^2 y \\implies (1 + x^2)y_2 + x y_1 - m^2 y = 0$ [প্রমাণিত]।",
            "rubric": "১ম অন্তরীকরণ ও সরলীকরণ: ১.০ | বর্গ করে অপেক্ষক রূপ দেওয়া: ১.০ | ২য় অন্তরীকরণ ও চূড়ান্ত সমীকরণ: ১.০"
        },

        # BIOLOGY (4)
        {
            "subject": "Biology",
            "tag": "DU Written Special",
            "problem": "মানব মস্তিষ্কের তিনটি প্রধান অংশের নাম ও উপ-অংশসমূহের শ্রেণিবিন্যাস ছক আকারে উপস্থাপন কর। হাইপোথ্যালামাসের তিনটি প্রধান শারীরবৃত্তীয় কাজ উল্লেখ কর।",
            "marks": 3.0,
            "solution": "মানব মস্তিষ্ক তিনটি প্রধান অংশে বিভক্ত: ১. অগ্রমস্তিষ্ক (সেরিব্রাম, থ্যালামাস, হাইপোথ্যালামাস); ২. মধ্যমস্তিষ্ক (কর্পোরা কোয়াড্রিজেমিনা, সেরেব্রাল পেডাঙ্কল); ৩. পশ্চাৎমস্তিষ্ক (সেরিবেলাম, পনস, মেডুলা অবলংগাটা)। হাইপোথ্যালামাসের ৩টি প্রধান কাজ: (ক) দেহের অভ্যন্তরীণ তাপমাত্রা নিয়ন্ত্রণ (দেহের প্রধান থার্মোস্ট্যাট); (খ) ক্ষুধা, তৃষ্ণা, ঘুম ও আবেগীয় অনুভূতি নিয়ন্ত্রণ; (গ) নিউরোহরমোন (অক্সিটোসিন ও ভেসোপ্রেসিন) তৈরি এবং পিটুইটারি গ্রন্থির ক্ষরণ নিয়ন্ত্রণকারী র রিলিজিং ও ইনহিবিটিং হরমোন নিঃসরণ।",
            "rubric": "মস্তিষ্কের ৩ অংশের সঠিক শ্রেণিবিন্যাস: ১.৫ | হাইপোথ্যালামাসের ৩টি শারীরবৃত্তীয় কাজ: ১.৫"
        },
        {
            "subject": "Biology",
            "tag": "DU Written Special",
            "problem": "মানবদেহের ৫ম, ৭ম, ৮ম এবং ১০ম করোটিক স্নায়ুর নাম, উৎস, বিস্তার ও প্রকৃতি ছক আকারে উল্লেখ কর।",
            "marks": 2.5,
            "solution": "ছক: ১. ৫ম (V) ট্রাইজেমিনাল: মিশ্র প্রকৃতি; বিস্তার: অক্ষি শাখা, ঊর্ধ্ব ও নিম্ন চোয়াল; কার্য: মুখমণ্ডলের অনুভূতি ও চর্বন পেশির সঞ্চালন। ২. ৭ম (VII) ফেসিয়াল: মিশ্র প্রকৃতি; বিস্তার: মুখের পেশি, স্বাদ কোরক ও লালাগ্রন্থি; কার্য: মুখের অভিব্যক্তি ও স্বাদ গ্রহণ। ৩. ৮ম (VIII) অডিটরি / ভেস্টিবুলোককলিয়ার: সংবেদী প্রকৃতি; বিস্তার: অন্তঃকর্ণের ককলিয়া ও অর্ধবৃত্তাকার নালী; কার্য: শ্রবণ ও দেহের ভারসাম্য রক্ষা। ৪. ১০ম (X) ভেগাস: মিশ্র প্রকৃতি; বিস্তার: গলবিল, স্বরযন্ত্র, হৃৎপিণ্ড, ফুসফুস ও পাকস্থলী; কার্য: শ্বসন, হৃদগতি ও পরিপাক নিয়ন্ত্রণ।",
            "rubric": "স্নায়ুর সঠিক নাম ও প্রকৃতি (প্রতিটির জন্য ০.২৫ করে ১.০) | সঠিক বিস্তার ও কার্য (প্রতিটির জন্য ০.৩৭৫ করে ১.৫)"
        },
        {
            "subject": "Biology",
            "tag": "DU Written Special",
            "problem": "চোখের অক্ষিগোলকের তিনটি স্তরের নাম লেখ। রেটিনার রড ও কোন কোষের মধ্যে প্রধান চারটি পার্থক্য ছকে দেখাও।",
            "marks": 2.5,
            "solution": "অক্ষিগোলকের ৩টি স্তর: ১. তন্তুময় বহিঃস্তর (স্ক্লেরা ও কর্নিয়া); ২. রক্তনালীযুক্ত মধ্যস্তর (কোরয়েড, সিলিয়ারি বডি ও আইরিশ); ৩. সংবেদী অন্তঃস্তর (রেটিনা)। রড ও কোন কোষের পার্থক্য: ১. রঞ্জক: রড কোষে রোডপসিন, কোন কোষে আয়োডপসিন থাকে; ২. আলো সংবেদনশীলতা: রড কোষ মৃদু আলোতে (রাতের দৃষ্টি), কোন কোষ তীব্র আলোতে সংবেদনশীল; ৩. বর্ণ দর্শন: রড কোষ বর্ণ পৃথক করতে পারে না, কোন কোষ লাল, সবুজ ও নীল বর্ণ দর্শনে সক্ষম; ৪. সংখ্যা ও বিস্তার: রড কোষ প্রায় ১২ কোটি ও পরিধিতে বেশি, কোন কোষ প্রায় ৬০-৭০ লাখ ও পীতবিন্দুতে (Fovea centralis) ঘনীভূত।",
            "rubric": "৩টি স্তরের সঠিক নাম: ১.০ | ৪টি সুস্পষ্ট পার্থক্য ছকে উপস্থাপন: ১.৫"
        },
        {
            "subject": "Biology",
            "tag": "DU Written Special",
            "problem": "সহজাত আচরণ (Innate Behavior) এবং অর্জিত/শিক্ষিত আচরণের (Learned Behavior) মধ্যে প্রধান ৩টি মৌলিক পার্থক্য লেখ। প্যাভলভের সাপেক্ষ প্রতিবর্ত ক্রিয়ার পরীক্ষণে অনুবন্ধিত উদ্দীপক ও অনুবন্ধিত সাড়া বলতে কী বোঝায়?",
            "marks": 2.5,
            "solution": "সহজাত ও অর্জিত আচরণের ৩টি পার্থক্য: ১. উৎপত্তি: সহজাত আচরণ জন্মগত ও জিন দ্বারা বংশানুক্রমিক নিয়ন্ত্রিত; অর্জিত আচরণ পরিবেশের সাথে অভিজ্ঞতা ও অনুশীলনে লব্ধ। ২. স্থায়িত্ব: সহজাত আচরণ প্রজাতি-নির্দিষ্ট ও চিরস্থায়ী; অর্জিত আচরণ ব্যক্তি-নির্দিষ্ট এবং অনভ্যাসে বিলুপ্ত হতে পারে। ৩. স্নায়বিক ভিত্তি: সহজাত আচরণ সরল প্রতিবর্ত চক্র দ্বারা নিয়ন্ত্রিত; অর্জিত আচরণ উন্নত সেরেব্রাল কর্টেক্স ও স্মৃতি দ্বারা পরিচালিত। প্যাভলভের পরীক্ষা: অনুবন্ধিত উদ্দীপক (CS) হলো নিরপেক্ষ কৃত্রিম সংকেত (ঘণ্টাধ্বনি) যা খাদ্যের সাথে উপস্থাপনের ফলে প্রতিক্রিয়া সৃষ্টি করতে সক্ষম হয়। অনুবন্ধিত সাড়া (CR) হলো অনুবন্ধিত উদ্দীপকের উপস্থিতিতে সৃষ্ট অর্জিত কৃত্রিম সাড়া (ঘণ্টার শব্দ শুনে লালাক্ষরণ)।",
            "rubric": "৩টি মৌলিক পার্থক্য: ১.৫ | অনুবন্ধিত উদ্দীপক ও সাড়ার সুনির্দিষ্ট সংজ্ঞা: ১.০"
        }
    ]
    return problems

if __name__ == "__main__":
    v_qs = get_varsity_questions()
    w_ps = get_du_written_problems()
    print(f"Varsity MCQs curated: {len(v_qs)} (multiple of 12: {len(v_qs) % 12 == 0})")
    print(f"DU Written Problems curated: {len(w_ps)}")
