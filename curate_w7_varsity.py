#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_w7_varsity.py
Week 07 Varsity Ka Core (Primary Spine) & DU Written Special (Target 2026-2027)
Strictly synchronized with 'W-07 Varsity (Udvash).pdf' Weekly Solution Sheet.
- 48 MCQs: 12 Physics, 12 Chemistry, 12 Higher Math, 12 Biology (exact 4 slots of 12)
- 16 Written Problems: 4 Physics, 4 Chemistry, 4 Higher Math, 4 Biology with rubrics
- Zero boilerplate trap alerts, authentic chapter-specific pitfalls, valid KaTeX.
"""

def get_varsity_questions():
    questions = []

    # ==========================================
    # PHYSICS (12 MCQs) - Chapters: স্থির তড়িৎ, আধুনিক পদার্থবিজ্ঞান
    # Source: W-07 Varsity (Udvash).pdf
    # ==========================================
    phy_mcqs = [
        {
            "id": "w7_var_phy_01",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-B Q09",
            "q": "একটি সমান্তরাল পাত ধারকের পাত-দূরত্ব $d$ এবং ধারকত্ব $C$। পাত দুটির ঠিক মাঝখানে $\\frac{d}{4}$ পুরুত্ববিশিষ্ট একটি ধাতব পাত স্থাপন করা হলে, ধারকটির নতুন ধারকত্ব কত হবে?",
            "opts": [
                "$\\frac{4}{3}C$",
                "$\\frac{3}{4}C$",
                "$\\frac{5}{4}C$",
                "$2C$"
            ],
            "ans": 0,
            "exp": "ধাতব পাতের পরাবৈদ্যুতিক ধ্রুবক $\\kappa = \\infty$। $t$ পুরুত্বের ধাতব পাত স্থাপন করলে নতুন ধারকত্ব $C' = \\frac{\\epsilon_0 A}{d - t + \\frac{t}{\\kappa}} = \\frac{\\epsilon_0 A}{d - \\frac{d}{4} + 0} = \\frac{\\epsilon_0 A}{\\frac{3d}{4}} = \\frac{4}{3}\\frac{\\epsilon_0 A}{d} = \\frac{4}{3}C$।",
            "trap_alert": "ধাতব পাতের $\\kappa = \\infty$ মনে না রেখে ডাই-ইলেকট্রিকের মতো ধারকত্ব বহুগুণ বৃদ্ধি না ধরে সরাসরি পাত দূরত্ব কমে $3d/4$ হওয়ায় ধারকত্ব $4C/3$ হয়—এই শর্টকাট মিস করা।",
            "yield_stars": 5,
            "probability": "99% DU Hotspot",
            "intelligence_type": "Capacitor Metallic Insertion Hack",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_02",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q08",
            "q": "$m_0$ স্থির ভরের একটি কণার গতিশীল ভর $m$। কণাটির গতিশক্তি যদি স্থির অবস্থার শক্তির $3$ গুণ হয়, তবে গতিশীল ভর ও নিশ্চল ভরের সঠিক সম্পর্ক কোনটি?",
            "opts": [
                "$m = 4m_0$",
                "$m = 3m_0$",
                "$m = 2m_0$",
                "$m = \\sqrt{10}m_0$"
            ],
            "ans": 0,
            "exp": "মোট আপেক্ষিক শক্তি $E = E_k + E_0$। এখানে গতিশক্তি $E_k = 3E_0$। সুতরাং মোট শক্তি $E = 3E_0 + E_0 = 4E_0 \\implies mc^2 = 4m_0 c^2 \\implies m = 4m_0$।",
            "trap_alert": "গতিশক্তি ৩ গুণ দেখে সরাসরি গতিশীল ভরও ৩ গুণ ($m = 3m_0$) মনে করা; মোট শক্তি ও গতিশক্তির পার্থক্য খেয়াল না করা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Relativistic Total Energy Mass Relation",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_03",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-C Q09",
            "q": "একটি ধারকের ধারকত্বের মান অপর একটি ধারকের মানের অর্ধেক। ধারক দুটি সমান্তরাল সমবায়ে যুক্ত থাকাকালীন তুল্য ধারকত্ব, শ্রেণি সমবায়ে থাকাকালীন তুল্য ধারকত্বের কত গুণ হবে?",
            "opts": [
                "$4.5$ গুণ",
                "$2.0$ গুণ",
                "$3.0$ গুণ",
                "$9.0$ গুণ"
            ],
            "ans": 0,
            "exp": "ধরি ধারক দুটির মান $C$ এবং $2C$। সমান্তরাল সমবায়ে তুল্য ধারকত্ব $C_p = C + 2C = 3C$। শ্রেণি সমবায়ে তুল্য ধারকত্ব $C_s = \\frac{C \\times 2C}{C + 2C} = \\frac{2}{3}C$। অনুপাত $\\frac{C_p}{C_s} = \\frac{3C}{\\frac{2}{3}C} = \\frac{9}{2} = 4.5$ গুণ।",
            "trap_alert": "অনুপাত উল্টে দিয়ে $C_s / C_p = 2/9$ বা ধারক দ্বিগুণ দেখে সরাসরি ৪ গুণ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "97% Speed Hack",
            "intelligence_type": "Capacitor Combination Ratio Hack",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_04",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam P-07 Set-A Q03",
            "q": "একটি তড়িৎ দ্বিমেরুর অক্ষের উপর রাখা একটি আধানের ওপর $F$ বল প্রযুক্ত হয়। দ্বিমেরুর কেন্দ্র হতে উক্ত আধানের দূরত্ব দ্বিগুণ করা হলে, আধানটির ওপর প্রযুক্ত বল কত হবে?",
            "opts": [
                "$\\frac{F}{8}$",
                "$\\frac{F}{4}$",
                "$\\frac{F}{2}$",
                "$8F$"
            ],
            "ans": 0,
            "exp": "তড়িৎ দ্বিমেরুর অক্ষীয় রেখায় প্রাবল্য $E \\propto \\frac{1}{r^3}$, ফলে প্রযুক্ত বল $F = qE \\propto \\frac{1}{r^3}$। দূরত্ব $r' = 2r$ হলে বল $F' = \\frac{F}{2^3} = \\frac{F}{8}$।",
            "trap_alert": "কুলম্বের সাধারণ বিন্দু চার্জের ব্যস্তানুপাতিক বর্গ সূত্র ($F \\propto 1/r^2$) প্রয়োগ করে $F/4$ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Dipole Force Inverse Cube Law",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_05",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam P-07 Set-A Q04",
            "q": "$R$ ব্যাসার্ধের একটি ফাঁপা গোলাকৃতি পরিবাহীর পৃষ্ঠে $+Q$ চার্জ দেওয়া হলো। গোলকের কেন্দ্র হতে $(R - 2)$ একক দূরত্বে কোনো বিন্দুর তড়িৎ বিভব কত? [যেখানে $R > 2$]",
            "opts": [
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{R}$",
                "$0$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{R - 2}$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{(R - 2)^2}$"
            ],
            "ans": 0,
            "exp": "চার্জিত পরিবাহী গোলকের অভ্যন্তরে প্রাবল্য শূন্য ($E = -\\frac{dV}{dr} = 0$), ফলে পৃষ্ঠ হতে কেন্দ্র পর্যন্ত সর্বত্র তড়িৎ বিভব সমান ও ধ্রুবক থাকে। যেহেতু $(R - 2) < R$, বিন্দুটি গোলকের অভ্যন্তরে অবস্থিত। অতএব বিভব $V = V_{\\text{surface}} = \\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{R}$।",
            "trap_alert": "দূরত্বের জায়গায় সরাসরি $(R-2)$ বসিয়ে $\\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{R-2}$ দাগানো অথবা অভ্যন্তরে প্রাবল্য শূন্য দেখে বিভবও শূন্য দাগানো।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Spherical Conductor Interior Potential",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_06",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam P-07 Set-A Q05",
            "q": "তড়িৎ দ্বিমেরুর দিকের সাথে $60^\\circ$ কোণে দ্বিমেরু অক্ষের মধ্যবিন্দু হতে $r$ দূরত্বে অবস্থিত কোনো বিন্দুতে তড়িৎ প্রাবল্যের মান কত?",
            "opts": [
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{\\sqrt{7}p}{2r^3}$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{\\sqrt{3}p}{r^3}$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{p}{r^3}$",
                "$\\frac{1}{4\\pi\\epsilon_0}\\frac{\\sqrt{7}p}{r^3}$"
            ],
            "ans": 0,
            "exp": "দ্বিমেরুর যেকোনো বিন্দুতে প্রাবল্য: $E = \\frac{1}{4\\pi\\epsilon_0}\\frac{p}{r^3}\\sqrt{1 + 3\\cos^2\\theta}$। $\\theta = 60^\\circ$ হলে $\\cos 60^\\circ = \\frac{1}{2}$, ফলে $\\sqrt{1 + 3\\left(\\frac{1}{2}\\right)^2} = \\sqrt{1 + \\frac{3}{4}} = \\sqrt{\\frac{7}{4}} = \\frac{\\sqrt{7}}{2}$। অতএব $E = \\frac{1}{4\\pi\\epsilon_0}\\frac{\\sqrt{7}p}{2r^3}$।",
            "trap_alert": "রুটের ভেতর $1 + 3\\cos^2\\theta$ এর ৩ দিয়ে গুণ করতে ভুলে গিয়ে $\\sqrt{1 + 1/4} = \\sqrt{5}/2$ দাগানো।",
            "yield_stars": 5,
            "probability": "96% DU Core",
            "intelligence_type": "Arbitrary Angle Dipole Field",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_07",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Daily Exam P-07 Set-A Q19",
            "q": "যদি একটি প্রোটনের গতিশক্তি তার নিশ্চল ভরশক্তি $m_0 c^2$ এর সমান হয়, তবে প্রোটনটির ভরবেগের মান কত হবে?",
            "opts": [
                "$\\sqrt{3}m_0 c$",
                "$2m_0 c$",
                "$\\sqrt{2}m_0 c$",
                "$m_0 c$"
            ],
            "ans": 0,
            "exp": "মোট শক্তি $E = E_k + E_0 = m_0 c^2 + m_0 c^2 = 2m_0 c^2$। আবার আইনস্টাইনের ভর-শক্তি-ভরবেগ সম্পর্ক: $E^2 = p^2 c^2 + E_0^2 \\implies (2m_0 c^2)^2 = p^2 c^2 + (m_0 c^2)^2 \\implies 4m_0^2 c^4 = p^2 c^2 + m_0^2 c^4 \\implies p^2 c^2 = 3m_0^2 c^4 \\implies p = \\sqrt{3}m_0 c$।",
            "trap_alert": "$p = mv$ দিয়ে ক্লাসিক্যাল গতিশক্তি $E_k = \\frac{p^2}{2m}$ এর ভুল সূত্রে গিয়ে $p = \\sqrt{2}m_0 c$ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "98% Speed Hack",
            "intelligence_type": "Relativistic Momentum-Energy Triplet",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_08",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q07",
            "q": "একজন নভোচারী $22$ বছর বয়সে $1.8 \\times 10^8\\text{ ms}^{-1}$ বেগে গতিশীল একটি নভোযানে চড়ে মহাকাশ ভ্রমণে গেলেন। পৃথিবীর হিসাবে তিনি $25$ বছর মহাকাশে কাটিয়ে ফিরে এলেন। পৃথিবীতে ফিরে আসার পর নভোচারীর বর্তমান বয়স কত বছর?",
            "opts": [
                "$42$ বছর",
                "$47$ বছর",
                "$37$ বছর",
                "$40$ বছর"
            ],
            "ans": 0,
            "exp": "নভোচারীর নিজস্ব সময় (প্রকৃত কাল) $t_0 = t \\sqrt{1 - \\frac{v^2}{c^2}} = 25 \\times \\sqrt{1 - \\left(\\frac{1.8 \\times 10^8}{3 \\times 10^8}\\right)^2} = 25 \\times \\sqrt{1 - (0.6)^2} = 25 \\times 0.8 = 20\\text{ বছর}$। নভোচারীর বর্তমান বয়স $= 22 + 20 = 42\\text{ বছর}$।",
            "trap_alert": "পৃথিবীর ২৫ বছরকে সরাসরি ২২ এর সাথে যোগ করে ৪৭ বছর দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Time Dilation Age Calculation",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_09",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q10",
            "q": "$5000\\text{ \\AA}$ তরঙ্গদৈর্ঘ্যের একটি দৃশ্যমান আলোকরশ্মির একটি ফোটনের শক্তি ইলেকট্রন-ভোল্ট ($\\text{eV}$) এককে কত?",
            "opts": [
                "$2.48\\text{ eV}$",
                "$1.24\\text{ eV}$",
                "$3.10\\text{ eV}$",
                "$4.96\\text{ eV}$"
            ],
            "ans": 0,
            "exp": "উদভাস ম্যাজিক শর্টকাট: $E(\\text{eV}) = \\frac{12400}{\\lambda(\\text{\\AA})} = \\frac{12400}{5000} = \\frac{124}{50} = 2.48\\text{ eV}$। (ম্যানুয়াল ক্যালকুলেটর ছাড়া মাত্র ৫ সেকেন্ডের হ্যাক!)",
            "trap_alert": "$\\frac{hc}{\\lambda}$ সূত্রে $h = 6.63 \\times 10^{-34}$ এবং $c = 3 \\times 10^8$ বসিয়ে জুলে নিয়ে আবার $1.6 \\times 10^{-19}$ দিয়ে ভাগ করার সময় দশমিকের হিসাবে ভুল করা।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Photon Energy Fast eV Conversion",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_10",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam P-07 Set-A Q02",
            "q": "লরেঞ্জ রূপান্তরে দুইটি বুলেট ট্রেন পরস্পরের বিপরীত দিকে প্রতিটি $300\\text{ km h}^{-1}$ সুষম বেগে অতিক্রম করছে। একটি ট্রেনের সাপেক্ষে অন্য ট্রেনে অবস্থিত ঘড়ির সময়ের আপেক্ষিক পার্থক্য কত হবে?",
            "opts": [
                "$0\\text{ s}$",
                "$1\\text{ s}$",
                "$\\infty$",
                "$0.5\\text{ s}$"
            ],
            "ans": 0,
            "exp": "$300\\text{ km h}^{-1}$ বেগ আলোর বেগের ($c = 3 \\times 10^8\\text{ ms}^{-1}$) তুলনায় অত্যন্ত নগণ্য ($v \\ll c$)। ফলে আপেক্ষিকতার প্রভাব $\\sqrt{1 - v^2/c^2} \\approx 1$। ট্রেনদ্বয়ের ঘড়ির সময়ের মধ্যে কোনো পরিমাপযোগ্য পার্থক্য হবে না, অর্থাৎ পার্থক্য $0\\text{ s}$।",
            "trap_alert": "বিশেষ আপেক্ষিকতার কাল দীর্ঘায়ন সূত্র জোর করে প্রয়োগ করতে গিয়ে হিসাব জটিল করা; সাধারণ পার্থিব বেগে আপেক্ষিকতার প্রভাব শূন্য।",
            "yield_stars": 4,
            "probability": "95% DU Concept",
            "intelligence_type": "Classical Limit of Relativity",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_11",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "স্থির তড়িৎ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Daily Exam P-07 Set-A Q08",
            "q": "একটি সমান্তরাল পাত ধারকের পাতদ্বয়ের মধ্যবর্তী দূরত্ব $d = 1 \\times 10^{-3}\\text{ m}$। এই ধারকের ধারকত্ব $2\\text{ F}$ হলে প্রতি পাতের ক্ষেত্রফল কত হতে হবে? [বায়ু মাধ্যমের ভেদনযোগ্যতা $\\epsilon_0 = 8.85 \\times 10^{-12}\\text{ C}^2\\text{ N}^{-1}\\text{ m}^{-2}$]",
            "opts": [
                "$2.25 \\times 10^8\\text{ m}^2$",
                "$4.50 \\times 10^8\\text{ m}^2$",
                "$1.13 \\times 10^8\\text{ m}^2$",
                "$2.25 \\times 10^5\\text{ m}^2$"
            ],
            "ans": 0,
            "exp": "ধারকত্ব $C = \\frac{\\epsilon_0 A}{d} \\implies A = \\frac{C \\cdot d}{\\epsilon_0} = \\frac{2 \\times 10^{-3}}{8.85 \\times 10^{-12}} \\approx \\frac{2}{8.88} \\times 10^9 \\approx 0.225 \\times 10^9 = 2.25 \\times 10^8\\text{ m}^2$। (এটি প্রমাণ করে যে ১ ফ্যারাড বা ২ ফ্যারাডের বাস্তব ধারক পাত তৈরি করা অসম্ভব বিশাল ক্ষেত্রফল দাবি করে!)",
            "trap_alert": "ঘাত হিসাবের সময় $10^{-3} / 10^{-12} = 10^9$ এর জায়গায় $10^{-15}$ লিখে ফেলা।",
            "yield_stars": 5,
            "probability": "96% DU Direct",
            "intelligence_type": "Capacitor Area Dimensional Analysis",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_phy_12",
            "week_id": "week_07",
            "subject": "Physics",
            "chapter": "আধুনিক পদার্থবিজ্ঞান",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Daily Exam P-07 Set-B Q15",
            "q": "কোনো ধাতব পৃষ্ঠে আপতিত ফোটনের শক্তি কার্যপেক্ষকের দ্বিগুণ ($E_1 = 2W_0$)। আপতিত আলোর তরঙ্গদৈর্ঘ্য কত গুণ করলে দ্রুততম ফটো-ইলেকট্রনের গতিশক্তি দ্বিগুণ হবে?",
            "opts": [
                "$\\frac{2}{3}$ গুণ",
                "$\\frac{1}{2}$ গুণ",
                "$\\frac{3}{4}$ গুণ",
                "$2$ গুণ"
            ],
            "ans": 0,
            "exp": "আইনস্টাইনের আলোকতড়িৎ সমীকরণ: $E_1 = W_0 + E_{k1} \\implies 2W_0 = W_0 + E_{k1} \\implies E_{k1} = W_0$। গতিশক্তি দ্বিগুণ করতে হলে $E_{k2} = 2E_{k1} = 2W_0$। তখন প্রয়োজনীয় ফোটন শক্তি $E_2 = W_0 + E_{k2} = W_0 + 2W_0 = 3W_0$। তরঙ্গদৈর্ঘ্যের অনুপাত: $\\frac{\\lambda_2}{\\lambda_1} = \\frac{E_1}{E_2} = \\frac{2W_0}{3W_0} = \\frac{2}{3}$। অর্থাৎ তরঙ্গদৈর্ঘ্য $\\frac{2}{3}$ গুণ করতে হবে।",
            "trap_alert": "গতিশক্তি দ্বিগুণ দেখে তরঙ্গদৈর্ঘ্য অর্ধেক ($\\frac{1}{2}$) মনে করা; কার্যপেক্ষক যোগ থাকার সম্পর্কটি ভুলে যাওয়া।",
            "yield_stars": 5,
            "probability": "98% Speed Hack",
            "intelligence_type": "Photoelectric Wavelength-Kinetic Energy Ratio",
            "source_book": "W-07 Varsity (Udvash).pdf"
        }
    ]

    # ==========================================
    # CHEMISTRY (12 MCQs) - Chapter: জৈব রসায়ন
    # Source: W-07 Varsity (Udvash).pdf
    # ==========================================
    che_mcqs = [
        {
            "id": "w7_var_che_01",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam C-07 Set-A Q19",
            "q": "মুক্ত শিকল কাঠামোরুক্ত গ্লুকোজ ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) অণুতে কতটি সেকেন্ডারি ($2^\\circ$) অ্যালকোহলীয় মূলক ($-\\text{CH(OH)}-$ ) বিদ্যমান?",
            "opts": [
                "$4$ টি",
                "$5$ টি",
                "$1$ টি",
                "$3$ টি"
            ],
            "ans": 0,
            "exp": "ডি-গ্লুকোজের মুক্ত শিকল কাঠামো: $\\text{CHO}-\\overset{2}{\\text{C}}\\text{H(OH)}-\\overset{3}{\\text{C}}\\text{H(OH)}-\\overset{4}{\\text{C}}\\text{H(OH)}-\\overset{5}{\\text{C}}\\text{H(OH)}-\\overset{6}{\\text{C}}\\text{H}_2\\text{OH}$। এখানে ২, ৩, ৪ এবং ৫ নম্বর কার্বন মোট ৪টি সেকেন্ডারি ($2^\\circ$) অ্যালকোহল মূলক; ৬ নম্বর কার্বনের $-\\text{CH}_2\\text{OH}$ হলো ১টি প্রাইমারি ($1^\\circ$) অ্যালকোহল মূলক এবং ১ নম্বর কার্বনে অ্যালডিহাইড মূলক। মোট হাইড্রক্সিল মূলক ৫টি, কিন্তু সেকেন্ডারি ৪টি।",
            "trap_alert": "গ্লুকোজে মোট ৫টি $-\\text{OH}$ মূলক দেখে ৫টি দাগিয়ে ফেলা; প্রশ্নে সুস্পষ্টভাবে 'সেকেন্ডারি অ্যালকোহলীয় গ্রুপ' চাওয়া হয়েছে।",
            "yield_stars": 5,
            "probability": "99% DU Hotspot",
            "intelligence_type": "Glucose Polyol Functional Group Count",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_02",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam C-07 Set-A Q01",
            "q": "নিচের কোন জৈব যৌগটিতে দুইটি কাইরাল বা অপ্রতিসম কার্বন কেন্দ্র বিদ্যমান?",
            "opts": [
                "বিউটেন-২, ৩-ডাইঅল",
                "২-হাইড্রক্সিপ্রোপানয়িক এসিড",
                "২-মিথাইলপ্রোপেন-২-অল",
                "বিউটান-২-অল"
            ],
            "ans": 0,
            "exp": "বিউটেন-২,৩-ডাইঅলের গাঠনিক সংকেত: $\\text{CH}_3-\\overset{*}{\\text{C}}\\text{H(OH)}-\\overset{*}{\\text{C}}\\text{H(OH)}-\\text{CH}_3$। ২ ও ৩ নম্বর কার্বন দুটির প্রতিটির সাথে ৪টি ভিন্ন মূলক ($-\\text{H}, -\\text{OH}, -\\text{CH}_3, -\\text{CH(OH)CH}_3$) যুক্ত থাকায় এতে ২টি কাইরাল কেন্দ্র আছে। বাকি অপশনগুলোতে ১টি বা ০টি কাইরাল কার্বন রয়েছে।",
            "trap_alert": "বিউটান-২-অল এ মাত্র ১টি কাইরাল কেন্দ্র থাকে, কিন্তু নামের সাদৃশ্যে ভুল হতে পারে।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Chiral Center Identification",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_03",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam C-07 Set-A Q03",
            "q": "IUPAC পদ্ধতি অনুসারে $\\text{CF}_3\\text{CHBrCl}$ চেতনা-নাশক হ্যালোথেন যৌগটির সঠিক নাম কোনটি?",
            "opts": [
                "২-ব্রোমো-২-ক্লোরো-১,১,১-ট্রাইফ্লোরোইথেন",
                "১,১,১-ট্রাইফ্লোরো-২-ব্রোমো-২-ক্লোরোইথেন",
                "২-ক্লোরো-২-ব্রোমো-১,১,১-ট্রাইফ্লোরোইথেন",
                "১-ব্রোমো-১-ক্লোরো-২,২,২-ট্রাইফ্লোরোইথেন"
            ],
            "ans": 0,
            "exp": "কার্বন শিকলে নাম্বারিং এর ক্ষেত্রে সর্বনিম্ন অবস্থানের সমষ্টি নিয়ম: $\\text{CF}_3$ যুক্ত কার্বনকে ১ নম্বর ধরলে প্রতিস্থাপকের অবস্থান হয় $1, 1, 1, 2, 2$ (সমষ্টি = ৭); কিন্তু উল্টো দিক থেকে ধরলে হতো $1, 1, 2, 2, 2$ (সমষ্টি = ৮)। তাই $\\text{CF}_3$ হলো ১ নম্বর কার্বন। এরপর বর্ণানুক্রমিক অগ্রগণ্যতা (Alphabetical order): Bromo > Chloro > Fluoro। সুতরাং নাম: ২-ব্রোমো-২-ক্লোরো-১,১,১-ট্রাইফ্লোরোইথেন।",
            "trap_alert": "বর্ণানুক্রমিকভাবে ব্রোমো ১ নম্বরে হতে হবে ভেবে ভুল দিক থেকে নাম্বারিং করা।",
            "yield_stars": 5,
            "probability": "99% DU Hotspot",
            "intelligence_type": "Halothane IUPAC Numbering Sum Rule",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_04",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Daily Exam C-07 Set-A Q04",
            "q": "$\\text{C}_4\\text{H}_8\\text{O}$ গাঠনিক সংকেত দ্বারা কতটি সমাণু অ্যালডিহাইড গঠন করা সম্ভব?",
            "opts": [
                "$2$ টি",
                "$3$ টি",
                "$4$ টি",
                "$1$ টি"
            ],
            "ans": 0,
            "exp": "$\\text{C}_4\\text{H}_8\\text{O}$ এর অ্যালডিহাইড সমাণু হতে হলে $-\\text{CHO}$ মূলক আবশ্যক। অবশিষ্ট অ্যালকাইল মূলক $\\text{C}_3\\text{H}_7$ (প্রোপাইল মূলক) যা ২ভাবে যুক্ত হতে পারে: ১. $n$-প্রোপাইলযুক্ত সরল শিকল: বিউটান্যাল ($\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CHO}$); ২. আইসো-প্রোপাইলযুক্ত শাখা শিকল: ২-মিথাইলপ্রোপান্যাল ($\\text{CH}_3-\\text{CH(CH}_3)-\\text{CHO}$)। সুতরাং অ্যালডিহাইড সমাণু মোট ২টি।",
            "trap_alert": "কিটোন সমাণু (বিউটানোন) বা ইনল সমাণু অন্তর্ভুক্ত করে ৩ বা ৪টি দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "98% Speed Hack",
            "intelligence_type": "Aldehyde Isomer Enumeration Hack",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_05",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam C-07 Set-A Q18",
            "q": "But-1-ene-3-yne জৈব যৌগটিতে উপস্থিত সিগমা ($\\sigma$) এবং পাই ($\\pi$) বন্ধনের সংখ্যা যথাক্রমে কতটি?",
            "opts": [
                "$7\\sigma$ এবং $3\\pi$",
                "$5\\sigma$ এবং $5\\pi$",
                "$8\\sigma$ এবং $2\\pi$",
                "$6\\sigma$ এবং $4\\pi$"
            ],
            "ans": 0,
            "exp": "যৌগটির সম্পূর্ণ গাঠনিক সংকেত: $\\text{H}_2\\text{C}=\\text{CH}-\\text{C}\\equiv\\text{CH}$। একক বন্ধনে ১টি $\\sigma$, দ্বিবন্ধনে ১টি $\\sigma$ ও ১টি $\\pi$, ত্রিবন্ধনে ১টি $\\sigma$ ও ২টি $\\pi$। $\\text{C}-\\text{H}$ বন্ধন মোট ৪টি (সবগুলো $\\sigma$); $\\text{C}-\\text{C}$ বন্ধন ৩টি (সবগুলো $\\sigma$)। মোট $\\sigma = 4 + 3 = 7$ টি। মোট $\\pi = 1(\\text{দ্বিবন্ধন}) + 2(\\text{ত্রিবন্ধন}) = 3$ টি।",
            "trap_alert": "$\\text{C}-\\text{H}$ একক বন্ধনগুলোকে সিগমা বন্ধন গণনার সময় বাদ দিয়ে শুধু কার্বন-কার্বন ৩টি সিগমা গুনে ভুল করা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Enyne Sigma Pi Bond Inventory",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_06",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q24",
            "q": "সম্পৃক্ত মনো-অ্যামাইড সমগোত্রীয় শ্রেণীর সাধারণ আণবিক সংকেত কোনটি?",
            "opts": [
                "$\\text{C}_n\\text{H}_{2n+1}\\text{CONH}_2$",
                "$\\text{C}_n\\text{H}_{2n}\\text{CONH}_2$",
                "$\\text{C}_n\\text{H}_{2n-1}\\text{CONH}_2$",
                "$\\text{C}_n\\text{H}_{2n+2}\\text{NH}_2$"
            ],
            "ans": 0,
            "exp": "অ্যামাইডের কার্যকরী মূলক $-\\text{CONH}_2$ অ্যালকাইল মূলকের ($\\text{R}- = \\text{C}_n\\text{H}_{2n+1}$) সাথে যুক্ত থাকে। যেমন: ফরমামাইড ($n=0: \\text{HCONH}_2$), অ্যাসিটামাইড বা ইথানামাইড ($n=1: \\text{CH}_3\\text{CONH}_2$)।",
            "trap_alert": "অ্যামিন ($\\text{C}_n\\text{H}_{2n+1}\\text{NH}_2$) এবং অ্যামাইডের সাধারণ সংকেত গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "97% DU Direct",
            "intelligence_type": "Amide Homologous Formula Check",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_07",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q18",
            "q": "$\\text{C}_7\\text{H}_9\\text{N}$ আণবিক সংকেত দ্বারা মোট কতটি অ্যারোমেটিক অ্যামিন সমাণু গঠন করা সম্ভব?",
            "opts": [
                "$5$ টি",
                "$4$ টি",
                "$3$ টি",
                "$6$ টি"
            ],
            "ans": 0,
            "exp": "$\\text{C}_7\\text{H}_9\\text{N}$ এর অ্যারোমেটিক সমাণুসমূহ: ১. অর্থো-টলুইডিন ($o$-methylaniline); ২. মেটা-টলুইডিন ($m$-methylaniline); ৩. প্যারা-টলুইডিন ($p$-methylaniline); ৪. বেনজাইল অ্যামিন ($\\text{C}_6\\text{H}_5\\text{CH}_2\\text{NH}_2$); ৫. $N$-মিথাইল অ্যানিলিন ($\\text{C}_6\\text{H}_5\\text{NHCH}_3$, সেকেন্ডারি অ্যারোমেটিক অ্যামিন)। মোট ৫টি।",
            "trap_alert": "সেকেন্ডারি অ্যামিন ($N$-মিথাইল অ্যানিলিন) অথবা পার্শ্বশিকল অ্যামিন (বেনজাইল অ্যামিন) গণনা করতে ভুলে গিয়ে ৩ বা ৪ দাগানো।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Aromatic Amine Isomer Census",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_08",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q29",
            "q": "অ্যাসিটোফেনন ($\\text{C}_6\\text{H}_5-\\text{CO}-\\text{CH}_3$) যৌগের ক্ষেত্রে কিটো-ইনল টটোমারিজমের মাধ্যমে উৎপন্ন ইনল সমাণুটি কোনটি?",
            "opts": [
                "$\\text{C}_6\\text{H}_5-\\text{C(OH)}=\\text{CH}_2$",
                "$\\text{C}_6\\text{H}_5-\\text{CH}_2-\\text{CHO}$",
                "$\\text{C}_6\\text{H}_5-\\text{CH}=\\text{CH}-\\text{OH}$",
                "$\\text{C}_6\\text{H}_5-\\text{CO}-\\text{CH}_2\\text{OH}$"
            ],
            "ans": 0,
            "exp": "টটোমারিজমে কার্বনিল কার্বনের পাশের $\\alpha$-কার্বন থেকে একটি হাইড্রোজেন অক্সিজেন পরমাণুতে স্থানান্তরিত হয় এবং $\\alpha$-কার্বন ও কার্বনিল কার্বনের মাঝে দ্বিবন্ধন তৈরি হয়: $\\text{C}_6\\text{H}_5-\\overset{\\text{O}}{\\underset{||}{\\text{C}}}-\\text{CH}_3 \\rightleftharpoons \\text{C}_6\\text{H}_5-\\overset{\\text{OH}}{\\underset{|}{\\text{C}}}=\\text{CH}_2$।",
            "trap_alert": "বেনজিন বলয় হতে হাইড্রোজেন সরিয়ে অ্যালডিহাইড ($\\text{C}_6\\text{H}_5\\text{CH}_2\\text{CHO}$) তৈরি হবে ভেবে অপশন (b) দাগানো।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Acetophenone Enolization Equilibrium",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_09",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q30 ও Set-B Q30",
            "q": "গ্লুকোজ অণুর মুক্ত শিকল গঠনে কোন চারটি কার্বন পরমাণু অপ্রতিসম (কাইরাল) এবং গ্লুকোজের মোট সম্ভাব্য স্টেরিও সমাণু সংখ্যা কত?",
            "opts": [
                "২, ৩, ৪, ৫ এবং $16$ টি",
                "১, ২, ৩, ৪ এবং $16$ টি",
                "২, ৩, ৪, ৫ এবং $8$ টি",
                "৩, ৪, ৫, ৬ এবং $32$ টি"
            ],
            "ans": 0,
            "exp": "গ্লুকোজের ১ নম্বর কার্বন অ্যালডিহাইড ($sp^2$) এবং ৬ নম্বর কার্বন $-\\text{CH}_2\\text{OH}$ (২টি H একই) অকাইরাল। অভ্যন্তরীণ কার্বন ২, ৩, ৪, ৫ এর প্রতিটি ভিন্ন ৪টি মূলক ধারণ করায় অপ্রতিসম ($n=4$)। ভ্যান্ট হফ সমীকরণ অনুসারে স্টেরিও সমাণু সংখ্যা $= 2^n = 2^4 = 16$ টি।",
            "trap_alert": "$n=4$ পেয়ে $2 \\times 4 = 8$ হিসাব করা অথবা ১ নম্বর কার্বনকেও কাইরাল ধরে ফেলা।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Glucose Stereocenter Calculation",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_10",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q28 ও Set-B Q28",
            "q": "সিস-সমাণুর সাথে তুলনা করলে ট্রান্স-সমাণুর ভৌত ধর্মের ক্ষেত্রে নিচের কোনটি সঠিক?",
            "opts": [
                "পানিতে দ্রাব্যতা কম এবং গলনাঙ্ক বেশি",
                "পানিতে দ্রাব্যতা বেশি এবং গলনাঙ্ক কম",
                "উভয় সমাণুর গলনাঙ্ক ও দ্রাব্যতা সম্পূর্ণ সমান",
                "পানিতে দ্রাব্যতা বেশি এবং স্ফুটনাঙ্ক বেশি"
            ],
            "ans": 0,
            "exp": "ট্রান্স-সমাণু প্রতিসম (Symmetrical) হওয়ায় এর ডাইপোল মোমেন্ট কম বা শূন্য, ফলে পোলার দ্রাবক পানিতে দ্রাব্যতা কম। কিন্তু প্রতিসমতার কারণে ক্রিস্টাল ল্যাটিসে অণুগুলো অত্যন্ত দৃঢ়ভাবে সন্নিবেশিত থাকে, ফলে ট্রান্স-সমাণুর গলনাঙ্ক সিস-সমাণু অপেক্ষা বেশি এবং অভ্যন্তরীণ শক্তি কম।",
            "trap_alert": "দ্রাব্যতা ও গলনাঙ্ক উভয়ই বাড়বে বা কমবে ভেবে বিভ্রান্ত হওয়া; দ্রাব্যতা কম কিন্তু গলনাঙ্ক বেশি।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Cis Trans Physical Property Paradox",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_11",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam C-07 Set-B Q17",
            "q": "জৈব যৌগের নামকরণের ক্ষেত্রে কার্যকরী মূলকের অগ্রাধিকারের সঠিক ক্রম কোনটি?",
            "opts": [
                "$-\\text{COOH} > -\\text{SO}_3\\text{H} > -\\text{COX} > -\\text{CONH}_2$",
                "$-\\text{SO}_3\\text{H} > -\\text{COOH} > -\\text{CONH}_2 > -\\text{COX}$",
                "$-\\text{COOH} > -\\text{CONH}_2 > -\\text{SO}_3\\text{H} > -\\text{COX}$",
                "$-\\text{COX} > -\\text{COOH} > -\\text{SO}_3\\text{H} > -\\text{CONH}_2$"
            ],
            "ans": 0,
            "exp": "IUPAC অগ্রাধিকার ক্রমের সুপার ট্রিক: কার্বক্সিলিক এসিড ($-\\text{COOH}$) > সালফোনিক এসিড ($-\\text{SO}_3\\text{H}$) > এসিড হ্যালাইড ($-\\text{COX}$) > এসিড অ্যামাইড ($-\\text{CONH}_2$) > নাইট্রাইল ($-\\text{CN}$) > অ্যালডিহাইড ($-\\text{CHO}$) > কিটোন ($>\\text{CO}$) > অ্যালকোহল ($-\\text{OH}$)।",
            "trap_alert": "$-\\text{SO}_3\\text{H}$ কে এসিড হিসেবে $-\\text{COOH}$ এর আগে স্থান দিয়ে অপশন (b) দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Functional Group Priority Ladder",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_che_12",
            "week_id": "week_07",
            "subject": "Chemistry",
            "chapter": "জৈব রসায়ন",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-D Q23",
            "q": "সাইক্লোহেক্সানোন ($\\text{Cyclohexanone}$) অণুতে সর্বমোট কতটি সিগমা ($\\sigma$) বন্ধন উপস্থিত রয়েছে?",
            "opts": [
                "$17$ টি",
                "$16$ টি",
                "$18$ টি",
                "$12$ টি"
            ],
            "ans": 0,
            "exp": "সাইক্লোহেক্সানোনের আণবিক সংকেত $\\text{C}_6\\text{H}_{10}\\text{O}$। বলয়ে ৬টি কার্বনের মাঝে ৬টি $\\text{C}-\\text{C}$ সিগমা বন্ধন। ৫টি $-\\text{CH}_2-$ কার্বনে মোট $5 \\times 2 = 10$ টি $\\text{C}-\\text{H}$ সিগমা বন্ধন। কার্বনিল গ্রুপে $\\text{C}=\\text{O}$ এর মধ্যে ১টি সিগমা ($\\sigma$) ও ১টি পাই ($\\pi$) বন্ধন। মোট $\\sigma = 6 + 10 + 1 = 17$ টি।",
            "trap_alert": "সাইক্লোহেক্সেনের ১৮টি সিগমার সাথে মিলিয়ে ফেলা বা কার্বনিলের সিগমা বাদ দিয়ে ১৬ দাগানো।",
            "yield_stars": 5,
            "probability": "97% Speed Hack",
            "intelligence_type": "Cyclic Ketone Sigma Bond Count",
            "source_book": "W-07 Varsity (Udvash).pdf"
        }
    ]

    # ==========================================
    # HIGHER MATH (12 MCQs) - Chapter: অন্তরীকরণ
    # Source: W-07 Varsity (Udvash).pdf
    # ==========================================
    mat_mcqs = [
        {
            "id": "w7_var_mat_01",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-C Q36",
            "q": "মান নির্ণয় কর: $\\lim_{x\\to -\\infty} \\frac{\\sqrt{x^2 + 2x}}{-x}$",
            "opts": [
                "$1$",
                "$-1$",
                "$\\infty$",
                "$0$"
            ],
            "ans": 0,
            "exp": "যখন $x \\to -\\infty$, তখন $x < 0$। আমরা জানি বাস্তব সংখ্যার ক্ষেত্রে $\\sqrt{x^2} = |x|$। যেহেতু $x$ ঋণাত্মক, $|x| = -x$। লবে: $\\sqrt{x^2 + 2x} = \\sqrt{x^2\\left(1 + \\frac{2}{x}\\right)} = |x|\\sqrt{1 + \\frac{2}{x}} = -x\\sqrt{1 + \\frac{2}{x}}$। সুতরাং $\\lim_{x\\to -\\infty} \\frac{-x\\sqrt{1 + \\frac{2}{x}}}{-x} = \\lim_{x\\to -\\infty} \\sqrt{1 + \\frac{2}{x}} = \\sqrt{1 + 0} = 1$।",
            "trap_alert": "$\\sqrt{x^2} = x$ লিখে লবকে $x$ ধরে হরের $-x$ দিয়ে ভাগ করে উত্তর $-1$ দাগিয়ে ফেলা—এটি ভর্তি পরীক্ষার সবচেয়ে মারাত্মক চিহ্নের ফাঁদ!",
            "yield_stars": 5,
            "probability": "99% DU Hotspot",
            "intelligence_type": "Negative Infinity Absolute Value Root Trap",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_02",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam M-07 Set-A Q01",
            "q": "মান নির্ণয় কর: $\\lim_{x\\to 0} \\frac{e^x}{x}$",
            "opts": [
                "লিমিটের অস্তিত্ব নেই",
                "$1$",
                "$0$",
                "$\\infty$"
            ],
            "ans": 0,
            "exp": "বামপার্শ্বীয় সীমা (L.H.L): $\\lim_{x\\to 0^-} \\frac{e^x}{x} = \\frac{e^0}{0^-} = \\frac{1}{-0} = -\\infty$। ডানপার্শ্বীয় সীমা (R.H.L): $\\lim_{x\\to 0^+} \\frac{e^x}{x} = \\frac{e^0}{0^+} = \\frac{1}{+0} = +\\infty$। যেহেতু L.H.L $\\neq$ R.H.L, তাই $x=0$ বিন্দুতে ফাংশনটির লিমিটের কোনো অস্তিত্ব নেই।",
            "trap_alert": "সরাসরি $x=0$ বসিয়ে $e^0/0 = 1/0 = \\infty$ দাগানো অথবা লা'হসপিটাল প্রয়োগের চেষ্টা করা (যা $\\frac{0}{0}$ আকার ছাড়া প্রয়োগ করা অবৈধ)।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "One-Sided Limit Asymmetry",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_03",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Daily Exam M-07 Set-A Q15",
            "q": "মান নির্ণয় কর: $\\lim_{x\\to 0} \\frac{(e^x - 1)\\tan^2 x}{x^3}$",
            "opts": [
                "$1$",
                "$0$",
                "$\\frac{1}{2}$",
                "$2$"
            ],
            "ans": 0,
            "exp": "স্ট্যান্ডার্ড লিমিট সূত্রে ভাঙালে: $\\lim_{x\\to 0} \\left(\\frac{e^x - 1}{x}\\right) \\times \\lim_{x\\to 0} \\left(\\frac{\\tan x}{x}\\right)^2 = 1 \\times (1)^2 = 1$।",
            "trap_alert": "লা'হসপিটাল তিনবার প্রয়োগ করতে গিয়ে বিশালাকার অন্তরীকরণে সময় নষ্ট করা; আদর্শ লিমিট গুণফল হিসেবে ভাবলে মাত্র ২ সেকেন্ডে সমাধান হয়।",
            "yield_stars": 5,
            "probability": "98% Speed Hack",
            "intelligence_type": "Standard Limit Factorization",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_04",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam M-07 Set-A Q14",
            "q": "ফাংশন $f(x) = e^x - x$ এর লঘুমান (Minimum Value) কত?",
            "opts": [
                "$1$",
                "$0$",
                "$-1$",
                "$e$"
            ],
            "ans": 0,
            "exp": "চরম মানের জন্য $f'(x) = 0 \\implies e^x - 1 = 0 \\implies e^x = 1 = e^0 \\implies x = 0$। দ্বিতীয় অন্তরক: $f''(x) = e^x \\implies f''(0) = e^0 = 1 > 0$। সুতরাং $x = 0$ বিন্দুতে ফাংশনটির লঘুমান বিদ্যমান এবং লঘুমান $f(0) = e^0 - 0 = 1 - 0 = 1$।",
            "trap_alert": "$x = 0$ বের করে সরাসরি উত্তর শূন্য ($0$) দাগিয়ে ফেলা; প্রশ্নে ভুজের মান নয়, ফাংশনের লঘুমান $f(0)$ চাওয়া হয়েছে।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Exponential Function Extrema",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_05",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam M-07 Set-B Q10",
            "q": "$y = x(3 - x^2)$ বক্ররেখার স্পর্শক $x$-অক্ষের সমান্তরাল হলে $x$ এর মান কত?",
            "opts": [
                "$\\pm 1$",
                "$0$",
                "$\\pm \\sqrt{3}$",
                "$\\pm 3$"
            ],
            "ans": 0,
            "exp": "সমীকরণ $y = 3x - x^3$। অন্তরীকরণ করলে স্পর্শকের ঢাল: $\\frac{dy}{dx} = 3 - 3x^2$। স্পর্শক $x$-অক্ষের সমান্তরাল হওয়ার শর্ত: $\\frac{dy}{dx} = 0 \\implies 3 - 3x^2 = 0 \\implies 3x^2 = 3 \\implies x^2 = 1 \\implies x = \\pm 1$।",
            "trap_alert": "$y = 0$ ধরে $x(3 - x^2) = 0 \\implies x = 0, \\pm\\sqrt{3}$ বের করে ছেদবিন্দুর মান দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Horizontal Tangent Point Abscissa",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_06",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-B Q31",
            "q": "যদি $y = \\tan^{-1}\\left(\\frac{p + qx}{q - px}\\right)$ হয়, তবে $\\frac{dy}{dx}$ এর মান কত?",
            "opts": [
                "$\\frac{1}{1 + x^2}$",
                "$\\frac{q}{q^2 + p^2 x^2}$",
                "$\\frac{p}{1 + x^2}$",
                "$0$"
            ],
            "ans": 0,
            "exp": "লব ও হরকে $q$ দ্বারা ভাগ করে: $y = \\tan^{-1}\\left(\\frac{\\frac{p}{q} + x}{1 - \\frac{p}{q}x}\\right)$। ত্রিকোণমিতিক বিপরীত সূত্র: $\\tan^{-1}\\left(\\frac{a + b}{1 - ab}\\right) = \\tan^{-1} a + \\tan^{-1} b$। অতএব $y = \\tan^{-1}\\left(\\frac{p}{q}\\right) + \\tan^{-1} x$। যেহেতু $\\tan^{-1}(p/q)$ সম্পূর্ণ ধ্রুবক, $\\frac{dy}{dx} = 0 + \\frac{1}{1 + x^2} = \\frac{1}{1 + x^2}$।",
            "trap_alert": "বিশাল ইউ/ভি অন্তরীকরণ করতে যাওয়া; সূত্রে ফেললে ধ্রুবক অংশটি শূন্য হয়ে সরাসরি $\\frac{1}{1+x^2}$ আসে।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Inverse Trig Linear Substitution Hack",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_07",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-B Q34",
            "q": "ফাংশন $y = x^2(1 - x)$ এর সর্বোচ্চ মান (Maximum Value) কত?",
            "opts": [
                "$\\frac{4}{27}$",
                "$\\frac{2}{3}$",
                "$\\frac{1}{27}$",
                "$\\frac{2}{9}$"
            ],
            "ans": 0,
            "exp": "সমীকরণ $y = x^2 - x^3$। ১ম অন্তরক: $\\frac{dy}{dx} = 2x - 3x^2 = x(2 - 3x) = 0 \\implies x = 0$ অথবা $x = \\frac{2}{3}$। ২য় অন্তরক: $\\frac{d^2 y}{dx^2} = 2 - 6x$। $x = \\frac{2}{3}$ এ $\\frac{d^2 y}{dx^2} = 2 - 4 = -2 < 0$, তাই এখানে সর্বোচ্চ মান বিদ্যমান। সর্বোচ্চ মান $y = \\left(\\frac{2}{3}\\right)^2 \\left(1 - \\frac{2}{3}\\right) = \\frac{4}{9} \\times \\frac{1}{3} = \\frac{4}{27}$।",
            "trap_alert": "চরম বিন্দুর ভুজ $x = 2/3$ দাগিয়ে ফেলা; কোটি তথা ফাংশনের মান $\\frac{4}{27}$ বের করতে হবে।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Cubic Polynomial Global Extrema",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_08",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Daily Exam M-07 Set-A Q07 ও Weekly Set-B Q38",
            "q": "ধাতুর তৈরি একটি বৃত্তাকার থালার ব্যাসার্ধ তাপ প্রয়োগের ফলে প্রতি সেকেন্ডে $0.25\\text{ cm}$ হারে বাড়ে। যখন থালাটির ব্যাসার্ধ $7\\text{ cm}$, তখন এর ক্ষেত্রফল বৃদ্ধির হার প্রতি সেকেন্ডে কত বর্গ সেন্টিমিটার?",
            "opts": [
                "$10.99\\text{ cm}^2/\\text{s} \\approx 11$",
                "$3.50\\text{ cm}^2/\\text{s}$",
                "$5.50\\text{ cm}^2/\\text{s}$",
                "$22.00\\text{ cm}^2/\\text{s}$"
            ],
            "ans": 0,
            "exp": "ক্ষেত্রফল $A = \\pi r^2$। সময়ের সাপেক্ষে অন্তরীকরণ: $\\frac{dA}{dt} = 2\\pi r \\frac{dr}{dt}$। মান বসিয়ে: $\\frac{dA}{dt} = 2 \\times \\frac{22}{7} \\times 7 \\times 0.25 = 44 \\times \\frac{1}{4} = 11\\text{ cm}^2/\\text{s}$ (বা $10.99\\text{ cm}^2/\\text{s}$)।",
            "trap_alert": "চেইন রুলে সময়ের সাপেক্ষে $\\frac{dr}{dt}$ গুণ করতে ভুলে শুধু $2\\pi r$ হিসাব করা।",
            "yield_stars": 5,
            "probability": "98% Speed Hack",
            "intelligence_type": "Rate of Change Thermal Expansion",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_09",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam M-07 Set-A Q06",
            "q": "যদি $y = \\sqrt{x - \\sqrt{x - \\sqrt{x - \\dots \\infty}}}$ হয়, তবে $\\frac{dy}{dx}$ এর মান কত?",
            "opts": [
                "$\\frac{1}{2y + 1}$",
                "$\\frac{1}{2y - 1}$",
                "$\\frac{-1}{2y + 1}$",
                "$\\frac{1}{1 - 2y}$"
            ],
            "ans": 0,
            "exp": "অনন্ত ধারার সমীকরণ: $y = \\sqrt{x - y} \\implies y^2 = x - y \\implies y^2 + y = x$। উভয়পক্ষে $x$-এর সাপেক্ষে অন্তরীকরণ করে: $2y\\frac{dy}{dx} + \\frac{dy}{dx} = 1 \\implies (2y + 1)\\frac{dy}{dx} = 1 \\implies \\frac{dy}{dx} = \\frac{1}{2y + 1}$।",
            "trap_alert": "যোগবোধক অসীম ধারার সূত্র ($\\frac{1}{2y-1}$) মুখস্থ থেকে বিয়োগবোধক রাশিতে প্রয়োগ করে $2y-1$ দাগিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Infinite Radical Series Sign Reversal",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_10",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q40 ও Set-D Q40",
            "q": "যদি $y = \\log_x a$ হয়, তবে $\\frac{dy}{dx}$ এর মান কোনটি হবে?",
            "opts": [
                "$-\\frac{\\ln a}{x(\\ln x)^2}$",
                "$\\frac{1}{x\\ln a}$",
                "$\\frac{\\ln a}{x}$",
                "$-\\frac{1}{x(\\ln x)^2}$"
            ],
            "ans": 0,
            "exp": "ভিত্তি পরিবর্তন সূত্র: $y = \\frac{\\ln a}{\\ln x} = (\\ln a)(\\ln x)^{-1}$। অন্তরীকরণ করলে: $\\frac{dy}{dx} = (\\ln a) \\cdot (-1)(\\ln x)^{-2} \\cdot \\frac{d}{dx}(\\ln x) = -(\\ln a)(\\ln x)^{-2} \\cdot \\frac{1}{x} = -\\frac{\\ln a}{x(\\ln x)^2}$।",
            "trap_alert": "$\\log_a x$ এর সাধারণ অন্তরক ($\\frac{1}{x\\ln a}$) এর সাথে ভিত্তি ও আর্গুমেন্ট অদলবদল হওয়া $\\log_x a$ গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Logarithmic Base Inversion Differentiation",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_11",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Daily Exam M-07 Set-A Q05",
            "q": "$\\cos x$ এর সাপেক্ষে $\\sin x$ এর অন্তরক সহগ $\\frac{d}{d(\\cos x)}(\\sin x)$ কত?",
            "opts": [
                "$-\\cot x$",
                "$\\cot x$",
                "$-\\tan x$",
                "$\\tan x$"
            ],
            "ans": 0,
            "exp": "প্যারামেট্রিক অন্তরীকরণের নিয়মানুসারে: $\\frac{d(\\sin x)}{d(\\cos x)} = \\frac{\\frac{d}{dx}(\\sin x)}{\\frac{d}{dx}(\\cos x)} = \\frac{\\cos x}{-\\sin x} = -\\cot x$।",
            "trap_alert": "হরের অন্তরকে $\\frac{d}{dx}(\\cos x) = -\\sin x$ এর মাইনাস চিহ্ন ভুলে গিয়ে $+\\cot x$ দাগানো।",
            "yield_stars": 5,
            "probability": "98% Speed Hack",
            "intelligence_type": "Parametric Relative Derivative",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_mat_12",
            "week_id": "week_07",
            "subject": "Higher Math",
            "chapter": "অন্তরীকরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-D Q33",
            "q": "কোনো একটি গতিশীল কণার সরণের সমীকরণ $s = (3t^3 - 2t + 4)\\text{ m}$ হলে, $t = 2\\text{ s}$ পর কণাটির ত্বরণ কত হবে?",
            "opts": [
                "$36\\text{ ms}^{-2}$",
                "$34\\text{ ms}^{-2}$",
                "$18\\text{ ms}^{-2}$",
                "$72\\text{ ms}^{-2}$"
            ],
            "ans": 0,
            "exp": "বেগ $v = \\frac{ds}{dt} = 9t^2 - 2\\text{ ms}^{-1}$। ত্বরণ $a = \\frac{dv}{dt} = \\frac{d}{dt}(9t^2 - 2) = 18t\\text{ ms}^{-2}$। $t = 2\\text{ s}$ সময়ে ত্বরণ $a(2) = 18(2) = 36\\text{ ms}^{-2}$।",
            "trap_alert": "একবার অন্তরীকরণ করে বেগের সূত্রে ($9(2)^2 - 2 = 34$) মান বসিয়ে বেগ দাগানো।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Kinematics Double Derivative Acceleration",
            "source_book": "W-07 Varsity (Udvash).pdf"
        }
    ]

    # ==========================================
    # BIOLOGY (12 MCQs) - Chapters: সমন্বয় ও নিয়ন্ত্রণ, প্রাণীর আচরণ
    # Source: W-07 Varsity (Udvash).pdf
    # ==========================================
    bio_mcqs = [
        {
            "id": "w7_var_bio_01",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "প্রাণীর আচরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam Bio-07 Set-A Q18 ও Set-D Q59",
            "q": "মৌমাছির সামাজিক জীবনে কোন আচরণগত বৈশিষ্ট্যটি অত্যন্ত সুস্পষ্ট ও গুরুত্বপূর্ণ যেখানে কর্মী মৌমাছি নিজের জীবন বলিদান দিয়ে কলোনি রক্ষা করে?",
            "opts": [
                "পরার্থপরতা (Altruism)",
                "অনুকরণ (Imprinting)",
                "অভ্যাসগত শিখন (Habituation)",
                "অনুবন্ধন (Conditioning)"
            ],
            "ans": 0,
            "exp": "অ্যালটুইজম বা পরার্থপরতা হলো এমন একটি আচরণ যেখানে কোনো জীব নিজের প্রজনন ও জীবনের ঝুঁকি নিয়ে দলের অন্য সদস্যদের বেঁচে থাকা ও বংশবৃদ্ধিতে সহায়তা করে। মৌমাছির চাকে বন্ধ্যা কর্মী মৌমাছিরা রাণী ও ড্রোনদের সেবা এবং চাকে আক্রমণকারী শত্রুকে হুল ফুটিয়ে নিজে মৃত্যুবরণ করে যা খাঁটি পরার্থপরতার উদাহরণ।",
            "trap_alert": None,
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Altruistic Social Behavior Paradigm",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_02",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "প্রাণীর আচরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam Bio-07 Set-A Q19",
            "q": "প্রাণীর সহজাত আচরণের অন্তর্ভুক্ত এফএপি (Fixed Action Pattern - FAP) কেন্দ্রিক আচরণ নিচের কোনটি নয়?",
            "opts": [
                "শিখন বা অভ্যাস (Learning)",
                "পাখির বাসা তৈরি",
                "যুগলবন্দি ও যৌন মিলন",
                "শীতের পরিযান (Migration)"
            ],
            "ans": 0,
            "exp": "FAP একটি সম্পূর্ণ বংশগত, জিন-নিয়ন্ত্রিত এবং ছাঁচসম্মত (Stereotyped) আচরণ যা প্রাণী জন্মগতভাবে প্রাপ্ত হয় (যেমন: বাবুই পাখির জটিল বাসা তৈরি, পরিযান, স্টিকলব্যাকের লাল পেট দেখে আক্রমণ)। শিখন (Learning) অভিজ্ঞতা ও অনুশীলনের মাধ্যমে অর্জিত হয়, এটি কোনো FAP নয়।",
            "trap_alert": "পরিযান বা বাসা তৈরিতে কৌশল দেখে এগুলোকে শিখন মনে করা; প্রকৃতপক্ষে এগুলো জন্মগত FAP।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Innate FAP vs Learned Plasticity",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_03",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-D Q53",
            "q": "একজন পূর্ণাঙ্গ সুস্থ মানবদেহে উভয় কর্ণের মধ্যকর্ণ অংশে মোট কয়টি ক্ষুদ্র অস্থি (Ear Ossicles) বিদ্যমান থাকে?",
            "opts": [
                "$6$ টি",
                "$3$ টি",
                "$2$ টি",
                "$8$ টি"
            ],
            "ans": 0,
            "exp": "প্রতিটি কানের মধ্যকর্ণে ৩টি করে ক্ষুদ্রাস্থি থাকে: ম্যালিয়াস (Malleus), ইনকাস (Incus) ও স্টেপিস (Stapes)। যেহেতু মানুষের কর্ণ দুইটি (ডান ও বাম), তাই মানবদেহে মোট মধ্যকর্ণের অস্থির সংখ্যা $= 3 \\times 2 = 6$ টি।",
            "trap_alert": "প্রতি কানের ৩টি অস্থি মনে রেখে দ্রুত অপশনে ৩ দাগিয়ে ফেলা; প্রশ্নে পুরো মানবদেহে মোট অস্থির সংখ্যা চাওয়া হয়েছে।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Bilateral Ear Ossicle Headcount",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_04",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam Bio-07 Set-A Q13",
            "q": "অন্তঃকর্ণের ককলিয়া নালীর কোন প্রকোষ্ঠটি এন্ডোলিম্ফ (Endolymph) নামক বিশেষ তরল দ্বারা পূর্ণ থাকে?",
            "opts": [
                "স্কালা মিডিয়া",
                "স্কালা ভেস্টিবুলি",
                "স্কালা টিম্প্যানি",
                "ভেস্টিবুলার অ্যাপারেটাস"
            ],
            "ans": 0,
            "exp": "ককলিয়া তিনটি সমান্তরাল প্রকোষ্ঠে বিভক্ত: উপরের স্কালা ভেস্টিবুলি এবং নিচের স্কালা টিম্প্যানি—উভয়েই পেরিলিম্ফ তরলে পূর্ণ থাকে। মাঝখানের প্রকোষ্ঠটি স্কালা মিডিয়া (ককলিয়ার নালী) যা সম্পূর্ণ এন্ডোলিম্ফ তরলে পূর্ণ এবং এর ব্যাসিলার পর্দার ওপর শ্রবণ সংবেদী 'অর্গান অব কর্টি' অবস্থিত।",
            "trap_alert": "স্কালা ভেস্টিবুলি বা টিম্প্যানিকে এন্ডোলিম্ফে পূর্ণ মনে করা; কেবল স্কালা মিডিয়াতে এন্ডোলিম্ফ থাকে।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Cochlea Labyrinth Compartment Fluid",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_05",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam Bio-07 Set-A Q05 ও Weekly Set-B Q48",
            "q": "মানবদেহের জৈব ঘড়ি (Circadian Rhythm), দেহের তাপমাত্রা, ক্ষুধা, তৃষ্ণা এবং রাগ-ক্ষোভ নিয়ন্ত্রণ করে মস্তিষ্কের কোন অংশ?",
            "opts": [
                "হাইপোথ্যালামাস (Hypothalamus)",
                "থ্যালামাস (Thalamus)",
                "সেরিবেলাম (Cerebellum)",
                "মেডুলা অবলংগাটা"
            ],
            "ans": 0,
            "exp": "অগ্রমস্তিষ্কের ডায়েনসেফালনে অবস্থিত হাইপোথ্যালামাস হলো স্বয়ংক্রিয় স্নায়ুতন্ত্র ও এন্ডোক্রাইন সিস্টেমের সমন্বয়কারী মাস্টার কেন্দ্র; এটি দেহের তাপমাত্রা নিয়ন্ত্রণ (থার্মোস্ট্যাট), ক্ষুধা, তৃষ্ণা, আবেগ এবং ২৪ ঘণ্টার জৈব ছন্দ (Biological Clock) নিয়ন্ত্রণ করে।",
            "trap_alert": "সংবেদনশীল রিলে স্টেশন থ্যালামাসের সাথে হাইপোথ্যালামাসের কাজের বিভ্রান্তি।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Hypothalamus Homeostatic Center",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_06",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam Bio-07 Set-A Q06",
            "q": "মানবদেহে ১২ জোড়া করোটিক স্নায়ুর মধ্যে ৭ম করোটিক স্নায়ুর (VII) সঠিক নাম কোনটি?",
            "opts": [
                "ফেসিয়াল স্নায়ু (Facial nerve)",
                "ট্রাইজেমিনাল স্নায়ু (Trigeminal)",
                "অকুলোমোটর স্নায়ু (Oculomotor)",
                "গ্লসোফ্যারিঞ্জিয়াল স্নায়ু (Glossopharyngeal)"
            ],
            "ans": 0,
            "exp": "৭ম করোটিক স্নায়ু হলো ফেসিয়াল স্নায়ু যা একটি মিশ্র স্নায়ু। এটি মুখমণ্ডলের পেশি সঞ্চালন, স্বাদ গ্রহণ এবং লালাগ্রন্থির ক্ষরণ নিয়ন্ত্রণ করে। ৫ম হলো ট্রাইজেমিনাল, ৯ম হলো গ্লসোফ্যারিঞ্জিয়াল।",
            "trap_alert": "৫ম (ট্রাইজেমিনাল) এবং ৭ম (ফেসিয়াল) এর ক্রম উল্টে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Cranial Nerve VII Identity",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_07",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam Bio-07 Set-A Q09",
            "q": "চোখের অক্ষিগোলকের অভ্যন্তরীণ চাপ বজায় রাখতে এবং আকৃতি গোলাকার রাখতে কোন স্বচ্ছ তরল মাধ্যমটি মূল ভূমিকা পালন করে?",
            "opts": [
                "ভিট্রিয়াস হিউমার (Vitreous humor)",
                "অ্যাকুয়াস হিউমার (Aqueous humor)",
                "কোরয়েড (Choroid)",
                "সিলিয়ারি বডি"
            ],
            "ans": 0,
            "exp": "লেন্স ও রেটিনার মধ্যবর্তী পেছনের বৃহৎ প্রকোষ্ঠে অবস্থিত জেলির মতো স্বচ্ছ ভিট্রিয়াস হিউমার অক্ষিগোলকের অভ্যন্তরীণ হাইড্রোস্ট্যাটিক চাপ রক্ষা করে এবং অক্ষিগোলককে চুপসে যাওয়া থেকে রক্ষা করে গোলাকার আকৃতি ধরে রাখে। লেন্স ও কর্নিয়ার মাঝে থাকে অ্যাকুয়াস হিউমার যা পুষ্টি যোগায়।",
            "trap_alert": "সামনের অ্যাকুয়াস হিউমারের সাথে পেছনের ভিট্রিয়াস হিউমারের কাজের পার্থক্য মিস করা।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Ocular Vitreous Hydrodynamics",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_08",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Daily Exam Bio-07 Set-A Q14",
            "q": "রক্তে ক্যালসিয়াম ও ফসফেটের ভারসাম্য রক্ষায় প্যারাথাইরয়েড গ্রন্থি নিঃসৃত প্যারাথরমোনের প্রধান কাজ কোনটি?",
            "opts": [
                "রক্তে ক্যালসিয়াম বৃদ্ধি এবং বৃক্কে ফসফেটের রেচন হার বৃদ্ধি করা",
                "রক্তে ক্যালসিয়াম হ্রাস এবং ফসফেট বৃদ্ধি করা",
                "রক্তে ক্যালসিয়াম ও ফসফেট উভয়ই হ্রাস করা",
                "অস্থিতে ক্যালসিয়াম জমা রাখা"
            ],
            "ans": 0,
            "exp": "প্যারাথাইরয়েড গ্রন্থির প্যারাথরমোন (PTH বা কোলিপের হরমোন) অস্থি ক্ষয় করে এবং বৃক্কীয় নালিকায় ক্যালসিয়ামের পুনঃশোষণ বাড়িয়ে রক্তে $\\text{Ca}^{2+}$ বাড়ায়, একইসাথে বৃক্কে ফসফেটের রেচন বৃদ্ধি করে রক্তে ফসফেটের মাত্রা কমায়। বিপরীত কাজটি করে থাইরয়েড নিঃসৃত ক্যালসিটোনিন।",
            "trap_alert": "ক্যালসিটোনিনের কাজের সাথে প্যারাথরমোনের কাজ গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Parathormone Mineral Homeostasis",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_09",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q58",
            "q": "মানবদেহের প্রতিবর্ত ক্রিয়া (Reflex Action) সম্পর্কে নিম্নের কোন বিবৃতিটি সঠিক?",
            "opts": [
                "এটি জন্মগত, অনপেক্ষ, অনিচ্ছাকৃত এবং শিক্ষালব্ধ নয়",
                "এটি মস্তিষ্কের সেরেব্রাল কর্টেক্স দ্বারা নিয়ন্ত্রিত ঐচ্ছিক ক্রিয়া",
                "এটি সম্পূর্ণরূপে অনুশীলন ও স্মৃতিশক্তির উপর নির্ভরশীল",
                "এতে কোনো সংবেদী ও মোটর স্নায়ুর প্রয়োজন হয় না"
            ],
            "ans": 0,
            "exp": "অনপেক্ষ প্রতিবর্ত ক্রিয়া (যেমন গরম বস্তুতে হাত পড়লে দ্রুত হাত টানা, হাঁচি, চোখের পলক ফেলা) সহজাত, জন্মগত, দ্রুতগামী এবং সুষুম্নাকাণ্ড দ্বারা সরাসরি নিয়ন্ত্রিত। এর জন্য কোনো পূর্ব অভিজ্ঞতার প্রয়োজন নেই।",
            "trap_alert": "প্যাভলভের সাপেক্ষ প্রতিবর্ত ক্রিয়ার সাথে জন্মগত অনপেক্ষ প্রতিবর্তের বৈশিষ্ট্য গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% DU Repeat",
            "intelligence_type": "Reflex Action Inherent Modality",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_10",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "প্রাণীর আচরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-A Q59",
            "q": "প্রজনন ঋতুতে স্ত্রী মাছকে আকর্ষণ করার জন্য এবং ডিম ছাড়ার বাসা নির্দেশ করতে 'জিগ-জ্যাগ নৃত্য' (Zig-zag dance) প্রদর্শন করে কোন প্রাণী?",
            "opts": [
                "তিন কাঁটাযুক্ত পুরুষ স্টিকলব্যাক মাছ",
                "কর্মী মৌমাছি (Apis mellifera)",
                "ময়ূর",
                "শিম্পাঞ্জি"
            ],
            "ans": 0,
            "exp": "নোবেলজয়ী বিজ্ঞানী নিকো টিনবার্জেনের গবেষণায় দেখা যায়, প্রজনন ঋতুতে পুরুষ তিন কাঁটাযুক্ত স্টিকলব্যাকের পেট লাল বর্ণ ধারণ করে এবং স্ত্রী মাছের রূপালী চকচকে উদর দেখে পুরুষ মাছটি জিগ-জ্যাগ নৃত্য প্রদর্শন করে স্ত্রীকে বাসার দিকে পথ দেখায়।",
            "trap_alert": "মৌমাছির ওয়াগল নৃত্য (Waggle dance - খাদ্য উৎসের সংকেত) এর সাথে স্টিকলব্যাকের জিগ-জ্যাগ নৃত্যের বিভ্রান্তি।",
            "yield_stars": 5,
            "probability": "98% DU Repeat",
            "intelligence_type": "Stickleback Zig-Zag Courtship Ethology",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_11",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "প্রাণীর আচরণ",
            "tag": "DU Repeat",
            "track": "varsity",
            "origin": "W-07 Weekly Exam Set-B Q57 ও Set-D Q57",
            "q": "কোনো দিকনির্দেশক উদ্দীপকের সাথে নির্দিষ্ট কোণ বজায় রেখে প্রাণীর দিকমুখিতা পরিবর্তনকে কী বলা হয় (যেমন: সূর্যের অবস্থানের সাথে কোণ করে পিঁপড়ার খাদ্য সংগ্রহ)?",
            "opts": [
                "মেনোট্যাক্সিস (Menotaxis)",
                "ক্লিনোট্যাক্সিস (Klinotaxis)",
                "ট্রপোট্যাক্সিস (Tropotaxis)",
                "টেলোট্যাক্সিস (Telotaxis)"
            ],
            "ans": 0,
            "exp": "মেনোট্যাক্সিস হলো এমন এক ধরনের ট্যাক্সিস যেখানে প্রাণী উদ্দীপকের উৎসের দিকে বা বিপরীতে সরাসরি না গিয়ে উদ্দীপকের সাথে একটি ধ্রুবক কোণ (Constant angle) বা লাইট কম্পাস বজায় রেখে গমন করে (যেমন: সূর্যের অবস্থানের সাপেক্ষে পিঁপড়া ও মৌমাছির দিক নির্ণয়)।",
            "trap_alert": "সরাসরি আলোর দিকে গমনকারী পজিটিভ ফটোট্যাক্সিসের সাথে কোণ বজায় রাখা মেনোট্যাক্সিস গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "97% DU Repeat",
            "intelligence_type": "Menotaxis Constant Compass Orientation",
            "source_book": "W-07 Varsity (Udvash).pdf"
        },
        {
            "id": "w7_var_bio_12",
            "week_id": "week_07",
            "subject": "Biology",
            "chapter": "সমন্বয় ও নিয়ন্ত্রণ",
            "tag": "Speed Hack",
            "track": "varsity",
            "origin": "W-07 Daily Exam Bio-07 Set-B Q04",
            "q": "মায়েলিনযুক্ত স্নায়ুতন্তুতে রণভিয়ারের পর্বগুলোর (Nodes of Ranvier) মধ্য দিয়ে অ্যাকশন পটেনশিয়াল দ্রুতগতিতে লাফিয়ে লাফিয়ে পরিবহনকে কী বলা হয়?",
            "opts": [
                "সলটেটরি পরিবহন (Saltatory conduction)",
                "ক্রমাগত পরিবহন (Continuous conduction)",
                "সিন্যাপটিক বিলম্ব",
                "রিফ্র্যাক্টরি পিরিয়ড"
            ],
            "ans": 0,
            "exp": "মায়েলিন সিথ একটি চমৎকার বৈদ্যুতিক অন্তরক। ফলে অ্যাক্সনে আয়ন বিনিময় কেবল মায়েলিনবিহীন রনভিয়ারের পর্বে ঘটে। ফলে উদ্দীপনা এক পর্ব থেকে অন্য পর্বে লাফিয়ে লাফিয়ে অত্যন্ত দ্রুতগতিতে (১০০-১২০ মি/সেকেন্ড বেগে) পরিবাহিত হয় যাকে সলটেটরি পরিবহন বলে।",
            "trap_alert": "মায়েলিনবিহীন স্নায়ুতন্তুর অবিচ্ছিন্ন পরিবহন (Continuous conduction) এর সাথে গুলিয়ে ফেলা।",
            "yield_stars": 5,
            "probability": "99% Speed Hack",
            "intelligence_type": "Saltatory Nerve Conduction Mechanism",
            "source_book": "W-07 Varsity (Udvash).pdf"
        }
    ]

    questions.extend(phy_mcqs)
    questions.extend(che_mcqs)
    questions.extend(mat_mcqs)
    questions.extend(bio_mcqs)

    # Standardize duplicate aliases and enforce option shuffling via Fisher-Yates
    import random
    for q in questions:
        orig_opts = list(q["opts"])
        orig_ans = q.get("ans", 0)
        correct_val = orig_opts[orig_ans]

        # Deterministic Fisher-Yates shuffle per question
        rng = random.Random(f"admission_crack_w07_{q['id']}")
        shuffled = list(orig_opts)
        for i in range(len(shuffled) - 1, 0, -1):
            j = rng.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

        new_ans = shuffled.index(correct_val)
        q["opts"] = shuffled
        q["ans"] = new_ans
        q["question"] = q["q"]
        q["options"] = list(shuffled)
        q["correct_index"] = new_ans
        q["explanation"] = q["exp"]
        q["trap"] = q["trap_alert"]
        q["expected_count"] = q.get("yield_stars", 5)

    return questions


def get_du_written_problems():
    problems = [
        # PHYSICS (4) - Source: W-07 Varsity (Udvash).pdf Written Solutions
        {
            "subject": "Physics",
            "tag": "DU Written Special",
            "problem": "একটি মুক্ত মৌলিক কণার গড় আয়ুষ্কাল $1 \\times 10^{-4}\\text{ s}$। কণাটি $0.88c$ সুষম বেগে গতিশীল হলে গবেষণাগারে অবস্থিত পর্যবেক্ষকের সাপেক্ষে কণাটির গড় আয়ুষ্কাল কত নির্ণয় কর।",
            "marks": 2.5,
            "solution": "কাল দীর্ঘায়ন সূত্রানুসারে: $t = \\frac{t_0}{\\sqrt{1 - \\frac{v^2}{c^2}}}$। এখানে স্থির অবস্থায় গড় আয়ুষ্কাল $t_0 = 1 \\times 10^{-4}\\text{ s}$, বেগ $v = 0.88c$। মান বসিয়ে পাই: $t = \\frac{1 \\times 10^{-4}}{\\sqrt{1 - (0.88)^2}} = \\frac{1 \\times 10^{-4}}{\\sqrt{1 - 0.7744}} = \\frac{1 \\times 10^{-4}}{\\sqrt{0.2256}} \\approx \\frac{1 \\times 10^{-4}}{0.475} = 2.105 \\times 10^{-4}\\text{ s}$। অর্থাৎ গতিশীল কণার গড় আয়ুষ্কাল প্রায় $2.1 \\times 10^{-4}\\text{ s}$।",
            "rubric": "কাল দীর্ঘায়ন সূত্র ও মান প্রতিস্থাপন: ১.০ | বর্গমূল ও দশমিক হিসাব: ১.০ | এককসহ সঠিক উত্তর ($2.1 \\times 10^{-4}\\text{ s}$): ০.৫"
        },
        {
            "subject": "Physics",
            "tag": "DU Written Special",
            "problem": "একটি বর্গক্ষেত্রের দুটি বিপরীত শীর্ষে $+Q$ চার্জ স্থাপন করা হয় এবং অপর দুটি শীর্ষে $+q$ চার্জ স্থাপন করা হয়। $Q$ চার্জের যেকোনোটির উপর যদি লব্ধি বৈদ্যুতিক বল শূন্য হয়, তবে $\\frac{Q}{q}$ অনুপাতের মান কত নির্ণয় কর।",
            "marks": 3.0,
            "solution": "ধরি বর্গক্ষেত্রের বাহুর দৈর্ঘ্য $a$। কর্ণ বরাবর দূরত্ব $\\sqrt{2}a$। শীর্ষবিন্দুতে $Q$ চার্জের ওপর অপর দুটি $q$ চার্জের বিকর্ষণ বল $F_1 = F_2 = \\frac{1}{4\\pi\\epsilon_0}\\frac{Qq}{a^2}$। এদের মধ্যবর্তী কোণ $90^\\circ$, ফলে লব্ধি বল $F_{12} = \\sqrt{F_1^2 + F_2^2} = \\sqrt{2}F_1 = \\sqrt{2}\\frac{Qq}{4\\pi\\epsilon_0 a^2}$। বিপরীত শীর্ষের $Q$ চার্জ দ্বারা বিকর্ষণ বল $F_3 = \\frac{1}{4\\pi\\epsilon_0}\\frac{Q^2}{(\\sqrt{2}a)^2} = \\frac{Q^2}{4\\pi\\epsilon_0 \\cdot 2a^2}$। লব্ধি বল শূন্য হতে হলে: $\\vec{F}_{12} + \\vec{F}_3 = 0 \\implies \\sqrt{2}\\frac{Qq}{a^2} + \\frac{Q^2}{2a^2} = 0 \\implies Q\\left(\\frac{Q}{2} + \\sqrt{2}q\\right) = 0 \\implies \\frac{Q}{2} = -\\sqrt{2}q \\implies \\frac{Q}{q} = -2\\sqrt{2}$।",
            "rubric": "বাহুর দূরত্ব ও $F_1, F_2$ লব্ধি নির্ণয়: ১.০ | কর্ণ বরাবর $F_3$ বল সমীকরণ: ১.০ | সাম্যাবস্থার শর্ত প্রয়োগ করে $\\frac{Q}{q} = -2\\sqrt{2}$ প্রমাণ: ১.০"
        },
        {
            "subject": "Physics",
            "tag": "DU Written Special",
            "problem": "বায়ু মাধ্যমে $24\\text{ cm}$ বাহুবিশিষ্ট একটি সমবাহু ত্রিভুজের তিনটি শীর্ষবিন্দুতে যথাক্রমে $+2\\mu\\text{C}$, $-4\\mu\\text{C}$ এবং $+8\\mu\\text{C}$ চার্জ রয়েছে। উক্ত চার্জ ব্যবস্থার মোট তড়িৎ স্থিতিশক্তি নির্ণয় কর। [ধরি $\\frac{1}{4\\pi\\epsilon_0} = 9 \\times 10^9\\text{ N m}^2\\text{ C}^{-2}$]",
            "marks": 3.0,
            "solution": "সমবাহু ত্রিভুজের বাহু $r = 24\\text{ cm} = 0.24\\text{ m}$। চার্জ ব্যবস্থাটির মোট তড়িৎ স্থিতিশক্তি: $U = U_{12} + U_{23} + U_{31} = \\frac{1}{4\\pi\\epsilon_0 r}[q_1 q_2 + q_2 q_3 + q_3 q_1]$। মান বসিয়ে পাই: $U = \\frac{9 \\times 10^9}{0.24} \\times [(2)(-4) + (-4)(8) + (8)(2)] \\times 10^{-12} = \\frac{9 \\times 10^9}{0.24} \\times [-8 - 32 + 16] \\times 10^{-12} = \\frac{9 \\times 10^9}{0.24} \\times (-24) \\times 10^{-12} = \\frac{9 \\times (-24)}{0.24} \\times 10^{-3} = 9 \\times (-100) \\times 10^{-3} = -0.9\\text{ J}$।",
            "rubric": "স্থিতিশক্তির সাধারণ সূত্র গঠন: ১.০ | প্রতিটি জোড়ের চার্জ গুণফল ও চিহ্ন সঠিক রাখা: ১.০ | ক্যালকুলেশন ও সঠিক মান ($-0.9\\text{ J}$): ১.০"
        },
        {
            "subject": "Physics",
            "tag": "DU Written Special",
            "problem": "$10\\text{ cm}$ ব্যাসার্ধবিশিষ্ট একটি ফাঁপা ধাতব গোলকে $+20\\text{ nC}$ চার্জ দেওয়া হলো। (ক) গোলকের কেন্দ্র থেকে $5\\text{ cm}$, $10\\text{ cm}$ এবং $20\\text{ cm}$ দূরত্বে তড়িৎ বিভবের মান কত? (খ) কেন্দ্র থেকে $5\\text{ cm}$ দূরত্বে তড়িৎ প্রাবল্যের মান কত?",
            "marks": 2.5,
            "solution": "(ক) গোলকের পৃষ্ঠের ব্যাসার্ধ $R = 10\\text{ cm} = 0.1\\text{ m}$। পৃষ্ঠের বিভব $V_{\\text{surf}} = \\frac{1}{4\\pi\\epsilon_0}\\frac{Q}{R} = 9 \\times 10^9 \\times \\frac{20 \\times 10^{-9}}{0.1} = \\frac{180}{0.1} = 1800\\text{ V}$। পরিবাহী গোলকের অভ্যন্তর সমবিভব সম্পন্ন হওয়ায় কেন্দ্র থেকে $5\\text{ cm}$ দূরত্বে বিভব $V = 1800\\text{ V}$। পৃষ্ঠে ($10\\text{ cm}$) বিভব $V = 1800\\text{ V}$। বহিঃস্থ বিন্দু $r = 20\\text{ cm} = 0.2\\text{ m}$ এ বিভব $V = 9 \\times 10^9 \\times \\frac{20 \\times 10^{-9}}{0.2} = 900\\text{ V}$। (খ) পরিবাহীর অভ্যন্তরে চার্জ শূন্য থাকায় কেন্দ্র থেকে $5\\text{ cm}$ দূরত্বে তড়িৎ প্রাবল্য $E = 0\\text{ N/C}$।",
            "rubric": "অভ্যন্তরে ও পৃষ্ঠের বিভব নির্ণয় ($1800\\text{ V}$): ১.০ | বাইরের বিন্দুর বিভব ($900\\text{ V}$): ০.৭৫ | অভ্যন্তরে প্রাবল্য শূন্য ($E=0$) যুক্তি সহ: ০.৭৫"
        },

        # CHEMISTRY (4) - Source: W-07 Varsity (Udvash).pdf Written Solutions
        {
            "subject": "Chemistry",
            "tag": "DU Written Special",
            "problem": "$\\text{C}_4\\text{H}_8\\text{O}$ আণবিক সংকেতবিশিষ্ট তিনটি ভিন্ন চাক্রিক অ্যালকোহল সমাণুর গাঠনিক সংকেত ও IUPAC নাম লেখ।",
            "marks": 2.5,
            "solution": "$\\text{C}_4\\text{H}_8\\text{O}$ এর ৩টি চাক্রিক অ্যালকোহল সমাণু: ১. সাইক্লোবিউটানল (৪-কার্বনের বলয়ে একটি $-\\text{OH}$ মূলক: $\\text{cyclo-C}_4\\text{H}_7\\text{OH}$)। ২. ২-মিথাইলসাইক্লোপ্রোপানল (৩-কার্বনের বলয়ে ১ নম্বরে $-\\text{OH}$ এবং ২ নম্বরে $-\\text{CH}_3$ মূলক)। ৩. ১-মিথাইলসাইক্লোপ্রোপানল (৩-কার্বনের বলয়ে একই কার্বনে $-\\text{OH}$ ও $-\\text{CH}_3$ মূলক যুক্ত)।",
            "rubric": "প্রতিটি চাক্রিক সমাণুর সঠিক গাঠনিক সংকেত ও IUPAC নামের জন্য (০.৭৫ + ০.৭৫ + ১.০) = ২.৫"
        },
        {
            "subject": "Chemistry",
            "tag": "DU Written Special",
            "problem": "মেসো-টার্টারিক এসিডের গঠন সংকেত লিখে এর প্রতিসাম্য তল (Plane of Symmetry) প্রদর্শন কর। মেসো-যৌগ এবং রেসিমিক মিশ্রণের মধ্যে আলোক নিষ্ক্রিয়তার মৌলিক পার্থক্য ব্যাখ্যা কর।",
            "marks": 3.0,
            "solution": "টার্টারিক এসিডের গঠন: $\\text{HOOC}-\\overset{*}{\\text{C}}\\text{H(OH)}-\\overset{*}{\\text{C}}\\text{H(OH)}-\\text{COOH}$। মেসো-টার্টারিক এসিডের উভয় কাইরাল কার্বনে $-\\text{H}$ পরমাণু একই পাশে এবং $-\\text{OH}$ মূলক একই পাশে অবস্থান করে। অণুর ঠিক মাঝামাঝি দিয়ে একটি কাল্পনিক প্রতিসাম্য তল ($\\sigma$-plane) বিদ্যমান যা অণুটিকে দুটি সদৃশ অর্ধাংশে বিভক্ত করে। মৌলিক পার্থক্য: (১) মেসো-যৌগ অভ্যন্তরীণ ক্ষতিপূরণ (Internal Compensation) দ্বারা আলোক নিষ্ক্রিয়, অর্থাৎ একই অণুর উপরের অর্ধাংশের ডান ঘূর্ণন নিচের অর্ধাংশের সমপরিমাণ বাম ঘূর্ণন দ্বারা প্রশমিত হয়; (২) রেসিমিক মিশ্রণ বাহ্যিক ক্ষতিপূরণ (External Compensation) দ্বারা আলোক নিষ্ক্রিয়, যেখানে সমমোলার পৃথক দুটি এনানশিওমারের ($d$ ও $l$) ঘূর্ণন পরস্পরকে নিষ্ক্রিয় করে।",
            "rubric": "প্রতিসাম্য তলসহ মেসো গঠন উপস্থাপন: ১.০ | অভ্যন্তরীণ ক্ষতিপূরণ ব্যাখ্যা: ১.০ | বাহ্যিক ক্ষতিপূরণ ও রেসিমিক তুলনা: ১.০"
        },
        {
            "subject": "Chemistry",
            "tag": "DU Written Special",
            "problem": "পেন্ট-২-ইন ($\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_2-\\text{CH}_3$) যৌগটির সিস ও ট্রান্স জ্যামিতিক সমাণুর গাঠনিক রূপ আঁক। সিস-সমাণুর পোলার দ্রাবকে দ্রবণীয়তা ট্রান্স-সমাণু অপেক্ষা বেশি কেন ব্যাখ্যা কর।",
            "marks": 3.0,
            "solution": "গাঠনিক রূপ: (ক) Cis-পেন্ট-২-ইন: দ্বিবন্ধনযুক্ত কার্বনে মিথাইল ($-\\text{CH}_3$) ও ইথাইল ($-\\text{C}_2\\text{H}_5$) মূলক দ্বিবন্ধনের একই পাশে থাকে। (খ) Trans-পেন্ট-২-ইন: মিথাইল ও ইথাইল মূলক দ্বিবন্ধনের বিপরীত পাশে অবস্থান করে। দ্রবণীয়তার ব্যাখ্যা: সিস-সমাণুতে ইলেকট্রন দাতা অ্যালকাইল মূলকদ্বয় একই পাশে থাকায় এদের ডাইপোল মোমেন্ট একই দিকে কাজ করে, ফলে সিস-সমাণুর একটি নেট ডাইপোল মোমেন্ট ($\\mu > 0$) থাকে এবং এটি অধিক পোলার হয়। অন্যদিকে ট্রান্স-সমাণুতে মূলকগুলো বিপরীত পাশে থাকায় ডাইপোল প্রায় বাতিল হয়ে যায় ($\\mu \\approx 0$)। 'Like dissolves like' নীতি অনুসারে অধিক পোলার সিস-সমাণু পোলার দ্রাবক পানিতে বা অ্যালকোহলে ট্রান্স-সমাণুর চেয়ে অধিক দ্রবণীয়।",
            "rubric": "Cis ও Trans সমাণুর সঠিক ত্রিমাত্রিক গঠন: ১.০ | ডাইপোল মোমেন্ট ও পোলারিটি তুলনা: ১.০ | দ্রাব্যতা সিদ্ধান্তের যৌক্তিক ব্যাখ্যা: ১.০"
        },
        {
            "subject": "Chemistry",
            "tag": "DU Written Special",
            "problem": "$\\text{C}_4\\text{H}_{10}\\text{O}$ আণবিক সংকেত দ্বারা গঠিত তিনটি সম্ভাব্য ইথার সমাণুর গাঠনিক সংকেত ও IUPAC নাম লেখ। এদের মধ্যে কোন জোড়া মেটামারিজম সমাণুতা প্রদর্শন করে?",
            "marks": 2.5,
            "solution": "$\\text{C}_4\\text{H}_{10}\\text{O}$ এর ৩টি ইথার সমাণু: ১. মিথোক্সিপ্রোপেন: $\\text{CH}_3-\\text{O}-\\text{CH}_2-\\text{CH}_2-\\text{CH}_3$। ২. ইথোক্সিইথেন (ডাই-ইথাইল ইথার): $\\text{CH}_3-\\text{CH}_2-\\text{O}-\\text{CH}_2-\\text{CH}_3$। ৩. ২-মিথোক্সিপ্রোপেন: $\\text{CH}_3-\\text{O}-\\text{CH(CH}_3)_2$। মেটামার জোড়া: মিথোক্সিপ্রোপেন এবং ইথোক্সিইথেন পরস্পরের মেটামার, কারণ দ্বিজোজী অক্সিজেন পরমাণুর উভয়পাশে কার্বন পরমাণুর সংখ্যা ও বণ্টনে ভিন্নতা (১, ৩ বনাম ২, ২) রয়েছে।",
            "rubric": "৩টি ইথারের সংকেত ও IUPAC নাম: ১.৫ | মেটামার জোড়া চিহ্নিতকরণ ও ব্যাখ্যা: ১.০"
        },

        # HIGHER MATH (4) - Source: W-07 Varsity (Udvash).pdf Written Solutions
        {
            "subject": "Higher Math",
            "tag": "DU Written Special",
            "problem": "যদি $(\\cos x)^y = (\\sin y)^x$ হয়, তবে $\\frac{dy}{dx}$ নির্ণয় কর।",
            "marks": 3.0,
            "solution": "উভয়পক্ষে স্বাভাবিক লগারিদম ($\\ln$) নিয়ে পাই: $\\ln[(\\cos x)^y] = \\ln[(\\sin y)^x] \\implies y\\ln(\\cos x) = x\\ln(\\sin y)$। এবার উভয়পক্ষে $x$-এর সাপেক্ষে অন্তরীকরণ করি: $\\frac{dy}{dx}\\ln(\\cos x) + y \\cdot \\frac{1}{\\cos x}(-\\sin x) = 1 \\cdot \\ln(\\sin y) + x \\cdot \\frac{1}{\\sin y}(\\cos y)\\frac{dy}{dx}$। $\\implies \\frac{dy}{dx}\\ln(\\cos x) - y\\tan x = \\ln(\\sin y) + x\\cot y \\frac{dy}{dx}$। $\\frac{dy}{dx}$ পদগুলো বামে এনে: $\\frac{dy}{dx}[\\ln(\\cos x) - x\\cot y] = \\ln(\\sin y) + y\\tan x$। অতএব, $\\frac{dy}{dx} = \\frac{\\ln(\\sin y) + y\\tan x}{\\ln(\\cos x) - x\\cot y}$।",
            "rubric": "লগারিদম প্রয়োগ ও সরলীকরণ: ১.০ | গুণের সূত্রে উভয়পক্ষের সঠিক অন্তরীকরণ: ১.০ | $\\frac{dy}{dx}$ কমন নিয়ে সঠিক সমীকরণ: ১.০"
        },
        {
            "subject": "Higher Math",
            "tag": "DU Written Special",
            "problem": "ফাংশন $f(x) = 4e^{2x} + 9e^{-2x}$ এর সর্বনিম্ন মান নির্ণয় কর।",
            "marks": 2.5,
            "solution": "১ম অন্তরক: $f'(x) = 4(2e^{2x}) + 9(-2e^{-2x}) = 8e^{2x} - 18e^{-2x}$। চরম মানের জন্য $f'(x) = 0 \\implies 8e^{2x} = 18e^{-2x} \\implies \\frac{e^{2x}}{e^{-2x}} = \\frac{18}{8} \\implies e^{4x} = \\frac{9}{4} \\implies (e^{2x})^2 = \\left(\\frac{3}{2}\\right)^2 \\implies e^{2x} = \\frac{3}{2}$ [যেহেতু $e^{2x} > 0$]। তখন $e^{-2x} = \\frac{2}{3}$। ২য় অন্তরক: $f''(x) = 16e^{2x} + 36e^{-2x} = 16\\left(\\frac{3}{2}\\right) + 36\\left(\\frac{2}{3}\\right) = 24 + 24 = 48 > 0$। সুতরাং $e^{2x} = \\frac{3}{2}$ এ ফাংশনটির লঘুমান বিদ্যমান। সর্বনিম্ন মান $f_{\\min} = 4\\left(\\frac{3}{2}\\right) + 9\\left(\\frac{2}{3}\\right) = 6 + 6 = 12$।",
            "rubric": "১ম অন্তরক ও $e^{2x} = \\frac{3}{2}$ সমাধান: ১.০ | ২য় অন্তরক পরীক্ষা ($f'' > 0$): ০.৫ | সর্বনিম্ন মান $12$ নির্ণয়: ১.০"
        },
        {
            "subject": "Higher Math",
            "tag": "DU Written Special",
            "problem": "$x^2 + y^2 - 2x - 3 = 0$ বৃত্তের যে সকল বিন্দুতে অঙ্কিত স্পর্শক $x$-অক্ষের সমান্তরাল, তাদের স্থানাঙ্ক নির্ণয় কর।",
            "marks": 2.5,
            "solution": "উভয়পক্ষে $x$-এর সাপেক্ষে অন্তরীকরণ করি: $2x + 2y\\frac{dy}{dx} - 2 - 0 = 0 \\implies 2y\\frac{dy}{dx} = 2 - 2x \\implies \\frac{dy}{dx} = \\frac{1 - x}{y}$। স্পর্শক $x$-অক্ষের সমান্তরাল হওয়ার শর্ত: $\\frac{dy}{dx} = 0 \\implies \\frac{1 - x}{y} = 0 \\implies 1 - x = 0 \\implies x = 1$। মূল সমীকরণে $x = 1$ বসিয়ে পাই: $(1)^2 + y^2 - 2(1) - 3 = 0 \\implies 1 + y^2 - 2 - 3 = 0 \\implies y^2 - 4 = 0 \\implies y^2 = 4 \\implies y = \\pm 2$। অতএব স্পর্শকদ্বয় $x$-অক্ষের সমান্তরাল হওয়ার বিন্দুসমূহ $(1, 2)$ এবং $(1, -2)$।",
            "rubric": "বৃত্তের অন্তরীকরণ ও ঢাল $\\frac{dy}{dx}$: ১.০ | $\\frac{dy}{dx} = 0$ শর্ত হতে $x = 1$: ০.৫ | কোটি $y = \\pm 2$ ও বিন্দুদ্বয় নির্ণয়: ১.০"
        },
        {
            "subject": "Higher Math",
            "tag": "DU Written Special",
            "problem": "দেখাও যে, $f(x) = \\frac{\\ln x}{x}$ ফাংশনটির গুরুমান $\\frac{1}{e}$। [যেখানে $x > 0$]",
            "marks": 2.5,
            "solution": "১ম অন্তরক: ভাগের সূত্রানুসারে $f'(x) = \\frac{x \\cdot \\frac{d}{dx}(\\ln x) - \\ln x \\cdot \\frac{d}{dx}(x)}{x^2} = \\frac{x \\cdot \\frac{1}{x} - \\ln x(1)}{x^2} = \\frac{1 - \\ln x}{x^2}$। চরম মানের জন্য $f'(x) = 0 \\implies \\frac{1 - \\ln x}{x^2} = 0 \\implies 1 - \\ln x = 0 \\implies \\ln x = 1 \\implies x = e$। ২য় অন্তরক: $f''(x) = \\frac{x^2(-\\frac{1}{x}) - (1 - \\ln x)(2x)}{x^4} = \\frac{-x - 2x(1 - \\ln x)}{x^4} = \\frac{-1 - 2(1 - \\ln x)}{x^3}$। $x = e$ বিন্দুতে $f''(e) = \\frac{-1 - 2(1 - 1)}{e^3} = -\\frac{1}{e^3} < 0$। সুতরাং $x = e$ বিন্দুতে ফাংশনটির গুরুমান বিদ্যমান এবং গুরুমান $f(e) = \\frac{\\ln e}{e} = \\frac{1}{e}$ [দেখানো হলো]।",
            "rubric": "ভাগ নিয়মে ১ম অন্তরীকরণ ও $x=e$ নির্ণয়: ১.০ | ২য় অন্তরক পরীক্ষা ($f''(e) < 0$): ০.৭৫ | গুরুমান $\\frac{1}{e}$ প্রমাণ: ০.৭৫"
        },

        # BIOLOGY (4) - Source: W-07 Varsity (Udvash).pdf Written Solutions
        {
            "subject": "Biology",
            "tag": "DU Written Special",
            "problem": "প্রতিবর্তী চক্র (Reflex Arc) বলতে কী বোঝায়? একটি প্রতিবর্তী চক্রের প্রধান পাঁচটি অংশের নাম ক্রমানুসারে লেখ।",
            "marks": 2.5,
            "solution": "প্রতিবর্তী চক্র: যে স্নায়বিক পথের মাধ্যমে প্রতিবর্ত ক্রিয়ার উদ্দীপনা গ্রাহক অঙ্গ থেকে সুষুম্নাকাণ্ডে গৃহীত হয় এবং সাড়াদানের নির্দেশ মোটর স্নায়ু দিয়ে কার্যকারী অঙ্গে প্রেরিত হয় তাকে প্রতিবর্তী চক্র বা রিফ্লেক্স আর্ক বলে। ৫টি প্রধান অংশ: ১. গ্রাহক অঙ্গ (Receptor) - উদ্দীপনা গ্রহণ করে; ২. সংবেদী বা অন্তর্বাহী স্নায়ু (Sensory / Afferent neuron) - উদ্দীপনা বহন করে কেন্দ্রে নেয়; ৩. প্রতিবর্ত কেন্দ্র বা সমন্বয় কেন্দ্র (Reflex Center) - সাধারণত সুষুম্নাকাণ্ডের ধূসর পদার্থে গঠিত রিলে নিউরন; ৪. চেষ্টিয় বা বহির্বাহী স্নায়ু (Motor / Efferent neuron) - সাড়ার নির্দেশ কার্যকরী অঙ্গে বহন করে; ৫. প্রভাবক বা কার্যকরী অঙ্গ (Effector) - সাড়া প্রদানকারী পেশি বা গ্রন্থি।",
            "rubric": "প্রতিবর্তী চক্রের নির্ভুল সংজ্ঞা: ১.০ | ৫টি অংশের সঠিক নাম ও ক্রম: ১.৫"
        },
        {
            "subject": "Biology",
            "tag": "DU Written Special",
            "problem": "প্রাণীর সহজাত আচরণের অন্তর্ভুক্ত এফএপি (Fixed Action Pattern - FAP) এর প্রধান পাঁচটি মৌলিক বৈশিষ্ট্য উল্লেখ কর।",
            "marks": 3.0,
            "solution": "FAP এর ৫টি বৈশিষ্ট্য: ১. ছাঁচসম্মত (Stereotypy): আচরণের প্যাটার্ন প্রজাতির সকল সদস্যে সর্বদা অপরিবর্তনীয় ও নির্দিষ্ট ছাঁচে সম্পন্ন হয়। ২. সার্বজনীনতা (Universality): এটি প্রজাতি-নির্দিষ্ট, অর্থাৎ ঐ প্রজাতির প্রতিটি স্বাভাবিক সদস্যের মধ্যে স্বয়ংক্রিয়ভাবে দৃশ্যমান। ৩. ব্যক্তিগত অভিজ্ঞতা বহির্ভূত (Independence of Individual Experience): পূর্ব অভিজ্ঞতা, শিখন বা অনুশীলন ছাড়াই প্রাণী প্রথম সুযোগেই নিখুঁতভাবে প্রদর্শন করে। ৪. ব্যালিস্টিক ধর্ম (Ballisticness): একবার সাইন স্টিমুলাস দ্বারা সূচিত হলে পারিপার্শ্বিক উদ্দীপক সরিয়ে নিলেও ক্রিয়াটি মাঝপথে থামে না, শেষ পর্যন্ত চলে। ৫. উদ্দেশ্যের একনিষ্ঠতা (Singleness of Purpose): এটি একটি নির্দিষ্ট জৈবিক উদ্দেশ্য (প্রজনন, আত্মরক্ষা, খাদ্য গ্রহণ) সাধনে একনিষ্ঠভাবে পরিচালিত হয়।",
            "rubric": "প্রতিটি বৈশিষ্ট্যের নির্ভুল নামকরণ ও সংক্ষিপ্ত ব্যাখ্যার জন্য (০.৬ × ৫) = ৩.০"
        },
        {
            "subject": "Biology",
            "tag": "DU Written Special",
            "problem": "ট্যাক্সিস (Taxis) কী? বাহ্যিক উদ্দীপকের প্রকৃতির ভিত্তিতে যে কোনো তিন ধরনের ট্যাক্সিসের নাম ও প্রাণিজগৎ থেকে বাস্তব উদাহরণ দাও।",
            "marks": 2.5,
            "solution": "ট্যাক্সিস: কোনো দিকমুখী বাহ্যিক উদ্দীপকের (আলো, তাপ, রাসায়নিক, স্পর্শ ইত্যাদি) প্রভাবে সমগ্র প্রাণিদেহের উদ্দীপকের উৎসের দিকে বা উৎসের বিপরীত দিকে স্থানান্তরমূলক চলনকে ট্যাক্সিস বলে। ৩ ধরনের ট্যাক্সিস: ১. ফটোট্যাক্সিস (Phototaxis): আলোর উদ্দীপনায় চলন; যেমন- আরশোলা আলোর বিপরীত দিকে পালায় (ঋণাত্মক ফটোট্যাক্সিস) এবং ঘাসফড়িং আলোর দিকে আসে (ধনাত্মক ফটোট্যাক্সিস)। ২. মেনোট্যাক্সিস (Menotaxis): দিকনির্দেশক উদ্দীপকের সাথে নির্দিষ্ট ধ্রুব কোণ বজায় রেখে চলন; যেমন- সূর্যের অবস্থানের সাথে কোণ মিলিয়ে কর্মী পিঁপড়ার খাদ্য সংগ্রহ। ৩. থার্মোট্যাক্সিস (Thermotaxis): তাপমাত্রার উদ্দীপনায় চলন; যেমন- তীব্র শীতে ব্যাঙ মাটির নিচে শীতনিদ্রায় চলে যাওয়া (ঋণাত্মক থার্মোট্যাক্সিস)।",
            "rubric": "ট্যাক্সিসের সংজ্ঞা: ১.০ | ৩টি ট্যাক্সিসের নাম ও সঠিক বাস্তব উদাহরণ: ১.৫"
        },
        {
            "subject": "Biology",
            "tag": "DU Written Special",
            "problem": "মানব মস্তিষ্কের সেরিব্রাম (Cerebrum) এবং সেরিবেলামের (Cerebellum) মধ্যে প্রধান পাঁচটি তুলনামূলক পার্থক্য ছক আকারে উপস্থাপন কর।",
            "marks": 3.0,
            "solution": "সেরিব্রাম বনাম সেরিবেলাম পার্থক্য ছক: ১. অবস্থান: সেরিব্রাম অগ্রমস্তিষ্কের প্রধান অংশ; সেরিবেলাম পশ্চাৎমস্তিষ্কের অংশ। ২. আকার ও অনুপাত: মস্তিষ্কের সর্ববৃহৎ অংশ (প্রায় ৮০% আয়তন জুড়ে বিস্তৃত); এটি দ্বিতীয় বৃহত্তম অংশ। ৩. সংযোগ সেতু: সেরিব্রামের দুটি গোলার্ধ কর্পাস ক্যালোসাম (Corpus callosum) দ্বারা যুক্ত; সেরিবেলামের দুটি গোলার্ধ ভার্মিস (Vermis) দ্বারা যুক্ত। ৪. খণ্ড বা লোব: সেরিব্রাম ফ্রন্টাল, প্যারাইটাল, টেম্পোরাল ও অক্সিপিটাল লোবে বিভক্ত; সেরিবেলাম তিনটি উপ-অংশে বিভক্ত হলেও এ ধরনের লোব নেই। ৫. প্রধান কাজ: সেরিব্রাম বুদ্ধি, চিন্তা, স্মৃতি, চেতনা ও সকল ঐচ্ছিক পেশির ক্রিয়া নিয়ন্ত্রণ করে; সেরিবেলাম দেহের ভারসাম্য রক্ষা, অঙ্গভঙ্গি ও পেশিটান সমন্বয় করে।",
            "rubric": "অবস্থান ও আকার পার্থক্য: ১.০ | কর্পাস ক্যালোসাম বনাম ভার্মিস: ১.০ | কার্যাবলীর স্পষ্ট বৈসাদৃশ্য: ১.০"
        }
    ]
    return problems

if __name__ == "__main__":
    v_qs = get_varsity_questions()
    w_ps = get_du_written_problems()
    print(f"Varsity MCQs curated: {len(v_qs)} (multiple of 12: {len(v_qs) % 12 == 0})")
    print(f"DU Written Problems curated: {len(w_ps)}")
