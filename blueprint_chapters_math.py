#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
blueprint_chapters_math.py
Contains complete unbundled blueprint and synthetic predictors for all 20 Higher Math chapters:
- 1st Paper: 10 chapters (math_1st_01 to math_1st_10)
- 2nd Paper: 10 chapters (math_2nd_01 to math_2nd_10)
"""

def get_math_chapters():
    chapters = [
        # =========================================================================
        # HIGHER MATH 1ST PAPER (উচ্চতর গণিত ১ম পত্র - ১০টি পৃথক অধ্যায়)
        # =========================================================================
        {
            "id": "math_1st_01",
            "aliases": ["math_matrices"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০১",
            "title": "ম্যাট্রিক্স ও নির্ণায়ক (Matrices & Determinants)",
            "subtitle": "ব্যতিক্রমী ম্যাট্রিক্স, ইনভার্স ম্যাট্রিক্স, ট্রেস, নির্ণায়কের ধর্ম ও ক্র্যামার",
            "total_qb_questions": 460,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m01_t1",
                    "name": "Type 1: ব্যতিক্রমী ম্যাট্রিক্স ও অজানা চলকের মান নির্ণয়",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '18-19"],
                    "qb_question_refs": ["VAR-JnU-P01-Q10", "VAR-DU-P01-Q01", "VAR-RU-P02-Q02"],
                    "core_rule": "ব্যতিক্রমী (Singular) ম্যাট্রিক্সের নির্ণায়কের মান শূন্য হয় ($|A| = 0$); অবিকতিক্রমী (Non-singular) হলে $|A| \\ne 0$। $2 \\times 2$ ম্যাট্রিক্স $\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ ব্যতিক্রমী হলে $ad - bc = 0$। ট্রেস (Trace): প্রধান কর্ণের ভুক্তিগুলোর যোগফল $\\text{Tr}(A) = \\Sigma a_{ii}$। সমঘাতি (Idempotent): $A^2 = A$; শূন্যঘাতি (Nilpotent): $A^k = 0$; অভেদঘাতি (Involuntary): $A^2 = I$; লম্ব ম্যাট্রিক্স (Orthogonal): $A A^T = I \\implies A^{-1} = A^T$ এবং $|A| = \\pm 1$।",
                    "speed_elimination": "ব্যতিক্রমী বললে নির্ণায়কের মান শূন্য মিলিয়ে অজানা ধ্রুবকের মান ৩ সেকেন্ডে মুখে মুখে বের করুন ($ad - bc = 0$)।"
                },
                {
                    "type_id": "math_m01_t2",
                    "name": "Type 2: বিপরীত ম্যাট্রিক্স ($A^{-1}$) ও অ্যাডজয়েন্ট ম্যাট্রিক্স",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '20-21", "JU '21-22", "GST '21-22", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P02-Q09", "VAR-DU-P03-Q04", "VAR-GST-P01-Q03"],
                    "core_rule": "$A^{-1} = \\frac{1}{|A|} \\text{adj}(A)$ (শর্ত: $|A| \\ne 0$)। $2 \\times 2$ ম্যাট্রিক্সের শর্টকাট ইনভার্স: $A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\implies A^{-1} = \\frac{1}{ad - bc} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$ (প্রধান কর্ণের ভুক্তিদ্বয় স্থান বদল এবং গৌণ কর্ণের ভুক্তিদ্বয় চিহ্ন বদল করে)। নির্ণায়কের বৈশিষ্ট্য: $|A^T| = |A|$; $|A B| = |A| |B|$; $|k A| = k^n |A|$ ($n \\times n$ ম্যাট্রিক্স); $|A^{-1}| = \\frac{1}{|A|}$; $|\\text{adj}(A)| = |A|^{n-1}$।",
                    "speed_elimination": "$3 \\times 3$ ম্যাট্রিক্স হলে $|2A| = 2^3 |A| = 8|A|$; $2 \\times 2$ ম্যাট্রিক্সে কর্ণ ভুক্তি অদলবদল ও গৌণ কর্ণে মাইনাস চিহ্ন দিন।"
                },
                {
                    "type_id": "math_m01_t3",
                    "name": "Type 3: নির্ণায়কের ধর্মাবলী ও ক্র্যামারের নিয়ম",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '21-22", "DU '18-19", "RU '22-23", "GST '20-21", "Agri '22-23"],
                    "qb_question_refs": ["VAR-DU-P05-Q05", "VAR-RU-P04-Q02"],
                    "core_rule": "নির্ণায়কের দুটি সারি বা দুটি কলাম হুবহু এক বা সমানুপাতিক হলে নির্ণায়কের মান শূন্য। ক্র্যামারের নিয়ম (সমীকরণ জোট সমাধান): $D = |A|$; $x = \\frac{D_x}{D}, y = \\frac{D_y}{D}, z = \\frac{D_z}{D}$। অনন্য সমাধানের শর্ত: $D \\ne 0$; অসংখ্য সমাধানের শর্ত: $D = D_x = D_y = D_z = 0$; কোনো সমাধান না থাকার শর্ত (অসামঞ্জস্য): $D = 0$ কিন্তু অন্তত একটি $D_x, D_y, D_z \\ne 0$।",
                    "speed_elimination": "নির্ণায়কের অপশনগুলোতে $a=1, b=2, c=3$ মান বসিয়ে ৩ সেকেন্ডে সঠিক অপশন শনাক্ত করুন।"
                }
            ]
        },
        {
            "id": "math_1st_02",
            "aliases": ["math_vectors"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০২",
            "title": "ভেক্টর (Vectors)",
            "subtitle": "স্কেলার ও ভেক্টর গুণন, অভিক্ষেপ ও উপাংশ, এবং স্কেলার ট্রিপল গুণন",
            "total_qb_questions": 340,
            "high_yield_score": 95,
            "mega_types": [
                {
                    "type_id": "math_m02_t1",
                    "name": "Type 1: ভেক্টরের ডট গুণন, কোণ নির্ণয় ও লম্ব অভিক্ষেপ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q03", "VAR-DU-P02-Q02"],
                    "core_rule": "মধ্যবর্তী কোণ: $\\cos\\theta = \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{A}| |\\vec{B}|}$। লম্ব হওয়ার শর্ত: $\\vec{A} \\cdot \\vec{B} = 0$। $\\vec{B}$ এর ওপর $\\vec{A}$ এর লম্ব অভিক্ষেপ $= \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{B}|}$; $\\vec{B}$ বরাবর $\\vec{A}$ এর উপাংশ $= \\left(\\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{B}|}\\right) \\frac{\\vec{B}}{|\\vec{B}|} = \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{B}|^2} \\vec{B}$।",
                    "speed_elimination": "যার 'ওপর' বা 'বরাবর' অভিক্ষেপ বলবে তার মান নিচে হরে বসবে ($|\\vec{B}|$)।"
                },
                {
                    "type_id": "math_m02_t2",
                    "name": "Type 2: ক্রস গুণন, সমতলীয় ভেক্টর ও সামান্তরিক-ত্রিভুজের ক্ষেত্রফল",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '22-23", "GST '21-22", "BUET '20-21"],
                    "qb_question_refs": ["VAR-JnU-P05-Q04", "VAR-GST-P02-Q04"],
                    "core_rule": "দুটি ভেক্টর সমান্তরাল হওয়ার শর্ত: $\\vec{A} \\times \\vec{B} = 0 \\implies \\frac{A_x}{B_x} = \\frac{A_y}{B_y} = \\frac{A_z}{B_z}$। $\\vec{A}$ ও $\\vec{B}$ উভয়ের ওপর লম্ব একক ভেক্টর: $\\hat{\\eta} = \\pm \\frac{\\vec{A} \\times \\vec{B}}{|\\vec{A} \\times \\vec{B}|}$। তিনটি ভেক্টর সমতলীয় হওয়ার শর্ত: স্কেলার ট্রিপল গুণন $[\vec{A} \ \\vec{B} \ \\vec{C}] = \\begin{vmatrix} A_x & A_y & A_z \\\\ B_x & B_y & B_z \\\\ C_x & C_y & C_z \\end{vmatrix} = 0$।",
                    "speed_elimination": "লম্ব একক ভেক্টরে অবশ্যই $\\pm$ চিহ্ন থাকবে; সমতলীয় বললে নির্ণায়কের মান শূন্য হবে।"
                }
            ]
        },
        {
            "id": "math_1st_03",
            "aliases": ["math_straight_lines"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৩",
            "title": "সরলরেখা (Straight Lines)",
            "subtitle": "স্থানাঙ্ক রূপান্তর, অন্তর্বিভক্ত, ঢাল, দুটি রেখার লম্ব-সমান্তরাল শর্ত ও লম্ব দূরত্ব",
            "total_qb_questions": 490,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m03_t1",
                    "name": "Type 1: কার্তেসীয়-পোলার রূপান্তর ও অন্তর্বিভক্ত-বহির্বিভক্ত বিন্দু",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P01-Q11", "VAR-DU-P01-Q02", "VAR-RU-P03-Q01"],
                    "core_rule": "কার্তেসীয় ও পোলার: $x = r\\cos\\theta, y = r\\sin\\theta \\implies r = \\sqrt{x^2+y^2}, \\theta = \\tan^{-1}(|y/x|)$ (১ম চতুর্ভাগে $\\theta$, ২য় চতুর্ভাগে $\\pi - \\theta$, ৩য় চতুর্ভাগে $-\\pi + \\theta$ বা $\\pi + \\theta$, ৪র্থ চতুর্ভাগে $-\\theta$)। অন্তর্বিভক্তকারী বিন্দু: $x = \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, y = \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2}$। অক্ষ দ্বারা বিভক্তকরণ: $x$-অক্ষ রেখাকে বিভক্ত করে $-y_1/y_2$ অনুপাতে; $y$-অক্ষ বিভক্ত করে $-x_1/x_2$ অনুপাতে। ত্রিভুজের ভরকেন্দ্র: $G = \\left( \\frac{x_1+x_2+x_3}{3}, \\frac{y_1+y_2+y_3}{3} \\right)$।",
                    "speed_elimination": "$x$-অক্ষ যে অনুপাতে বিভক্ত করে তা কোটিদ্বয়ের অনুপাত ($|y_1:y_2|$); $y$-অক্ষ ভুজদ্বয়ের অনুপাত ($|x_1:x_2|$)।"
                },
                {
                    "type_id": "math_m03_t2",
                    "name": "Type 2: সমান্তরাল ও লম্ব রেখার সমীকরণ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '21-22", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P02-Q10", "VAR-DU-P02-Q03", "VAR-GST-P01-Q05"],
                    "core_rule": "$ax + by + c = 0$ এর: ১. সমান্তরাল রেখা: $ax + by + k = 0$ ($m_1 = m_2$); ২. লম্ব রেখা: $bx - ay + k = 0$ ($m_1 m_2 = -1$)। দুটি রেখার মধ্যবর্তী কোণ: $\\tan\\theta = \\pm \\frac{m_1 - m_2}{1 + m_1 m_2}$। অক্ষদ্বয় থেকে সমদূরত্ববর্তী বা সমান অংশ ছেদকারী রেখার ঢাল $m = \\pm 1$।",
                    "speed_elimination": "লম্ব রেখার ক্ষেত্রে $x$ ও $y$ এর সহগ অদলবদল হয়ে মাঝের চিহ্ন উল্টে যাবে ($ax+by \\rightarrow bx-ay$)।"
                },
                {
                    "type_id": "math_m03_t3",
                    "name": "Type 3: বিন্দু হতে রেখার লম্ব দূরত্ব ও সমান্তরাল রেখাদ্বয়ের দূরত্ব",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '21-22", "DU '18-19", "RU '20-21", "JU '20-21", "GST '22-23", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q12", "VAR-DU-P04-Q03", "VAR-CU-P02-Q06"],
                    "core_rule": "$(x_1, y_1)$ বিন্দু হতে $ax + by + c = 0$ রেখার লম্ব দূরত্ব: $d = \\frac{|ax_1 + by_1 + c|}{\\sqrt{a^2 + b^2}}$। মূলবিন্দু হতে দূরত্ব $d = \\frac{|c|}{\\sqrt{a^2 + b^2}}$। দুটি সমান্তরাল রেখা $ax + by + c_1 = 0$ এবং $ax + by + c_2 = 0$ এর মধ্যবর্তী লম্ব দূরত্ব: $d = \\frac{|c_1 - c_2|}{\\sqrt{a^2 + b^2}}$। দুটি রেখার অন্তর্ভুক্ত কোণের সমদ্বিখণ্ডকের সমীকরণ: $\\frac{a_1 x + b_1 y + c_1}{\\sqrt{a_1^2 + b_1^2}} = \\pm \\frac{a_2 x + b_2 y + c_2}{\\sqrt{a_2^2 + b_2^2}}$ ($a_1 a_2 + b_1 b_2 > 0$ হলে $+$ চিহ্ন স্থূলকোণের এবং $-$ চিহ্ন সূক্ষ্মকোণের সমদ্বিখণ্ডক)।",
                    "speed_elimination": "সমান্তরাল রেখাদ্বয়ের দূরত্বের জন্য আগে সহগ সমান করুন, তারপর ধ্রুবকদ্বয়ের পার্থক্যের পরমমানকে $\\sqrt{a^2+b^2}$ দিয়ে ভাগ করুন।"
                }
            ]
        },
        {
            "id": "math_1st_04",
            "aliases": ["math_circles"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৪",
            "title": "বৃত্ত (Circles)",
            "subtitle": "কেন্দ্র ও ব্যাসার্ধ, অক্ষদ্বয়ের ছেদাংশ, অক্ষ স্পর্শের শর্ত ও স্পর্শক সমীকরণ",
            "total_qb_questions": 470,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m04_t1",
                    "name": "Type 1: সাধারণ সমীকরণ, কেন্দ্র-ব্যাসার্ধ ও অক্ষদ্বয়ের ছেদাংশ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P01-Q12", "VAR-DU-P01-Q04", "VAR-RU-P01-Q03"],
                    "core_rule": "সাধারণ সমীকরণ: $x^2 + y^2 + 2gx + 2fy + c = 0$; কেন্দ্র $(-g, -f) = \\left(-\\frac{x\\text{ এর সহগ}}{2}, -\\frac{y\\text{ এর সহগ}}{2}\\right)$; ব্যাসার্ধ $r = \\sqrt{g^2 + f^2 - c}$ ($x^2, y^2$ এর সহগ ১ হতে হবে এবং $xy$ পদ থাকবে না)। অক্ষদ্বয়ের খণ্ডিতাংশ: $x$-অক্ষের খণ্ডিতাংশ $= 2\\sqrt{g^2 - c}$; $y$-অক্ষের খণ্ডিতাংশ $= 2\\sqrt{f^2 - c}$। ব্যাসের প্রান্তবিন্দু $(x_1, y_1)$ ও $(x_2, y_2)$ হলে বৃত্তের সমীকরণ: $(x - x_1)(x - x_2) + (y - y_1)(y - y_2) = 0$।",
                    "speed_elimination": "কেন্দ্র বের করতে $x$ ও $y$ এর সহগকে $-2$ দিয়ে ভাগ করুন (আগে $x^2, y^2$ এর সহগ ১ করতে হবে); খণ্ডিতাংশ $2\\sqrt{g^2-c}$।"
                },
                {
                    "type_id": "math_m04_t2",
                    "name": "Type 2: অক্ষদ্বয়কে স্পর্শ করার শর্ত",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '22-23", "JU '21-22", "GST '21-22", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P02-Q11", "VAR-DU-P03-Q03", "VAR-GST-P02-Q05"],
                    "core_rule": "১. $x$-অক্ষকে স্পর্শ করলে: খণ্ডিতাংশ শূন্য $\\implies g^2 = c$ এবং ব্যাসার্ধ $r = |f|$ (কেন্দ্রের কোটির পরমমান)। ২. $y$-অক্ষকে স্পর্শ করলে: খণ্ডিতাংশ শূন্য $\\implies f^2 = c$ এবং ব্যাসার্ধ $r = |g|$ (কেন্দ্রের ভুজের পরমমান)। ৩. উভয় অক্ষকে স্পর্শ করলে: $g^2 = f^2 = c$ এবং ব্যাসার্ধ $r = |g| = |f|$। মূলবিন্দুগামী হলে ধ্রুবক $c = 0$।",
                    "speed_elimination": "$x$-অক্ষ স্পর্শ করলে $g^2 = c$; $y$-অক্ষ স্পর্শ করলে $f^2 = c$; উভয় অক্ষ স্পর্শ করলে $g^2 = f^2 = c$।"
                },
                {
                    "type_id": "math_m04_t3",
                    "name": "Type 3: স্পর্শকের সমীকরণ ও স্পর্শক হওয়ার শর্ত ($c^2 = a^2(1+m^2)$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '18-19", "RU '20-21", "JU '20-21", "GST '22-23", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P04-Q11", "VAR-DU-P05-Q04", "VAR-CU-P01-Q07"],
                    "core_rule": "স্পর্শক হওয়ার মৌলিক শর্ত: বৃত্তের কেন্দ্র থেকে সরলরেখার লম্ব দূরত্ব বৃত্তের ব্যাসার্ধের সমান হতে হবে ($d = r$)। $y = mx + c$ রেখাটি $x^2 + y^2 = a^2$ বৃত্তের স্পর্শক হওয়ার শর্ত: $c = \\pm a\\sqrt{1 + m^2} \\implies c^2 = a^2(1 + m^2)$। বৃত্তের ওপরিস্থিত $(x_1, y_1)$ বিন্দুতে স্পর্শকের সমীকরণ: $x x_1 + y y_1 + g(x + x_1) + f(y + y_1) + c = 0$। অভিলম্বের সমীকরণ সর্বদা বৃত্তের কেন্দ্র $(-g, -f)$ দিয়ে যায়। বহিঃস্থ বিন্দু $(x_1, y_1)$ হতে স্পর্শকের দৈর্ঘ্য: $L = \\sqrt{x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c}$।",
                    "speed_elimination": "কেন্দ্র থেকে রেখার দূরত্ব ব্যাসার্ধের সমান মিলিয়ে অজানা ধ্রুবকের মান এক লাইনে বের করুন ($d = r$)।"
                }
            ]
        },
        {
            "id": "math_1st_05",
            "aliases": ["math_permutations_combinations"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৫",
            "title": "বিন্যাস ও সমাবেশ (Permutations & Combinations)",
            "subtitle": "শব্দের বর্ণ সাজানো, গোল টেবিল বিন্যাস, দল গঠন ও সম্পূরক সমাবেশ",
            "total_qb_questions": 450,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "math_m05_t1",
                    "name": "Type 1: পুনরাবৃত্তিযুক্ত শব্দের বর্ণ বিন্যাস ও স্বরবর্ণ একত্রে রাখার শর্ত",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P01-Q13", "VAR-DU-P02-Q05", "VAR-RU-P03-Q03"],
                    "core_rule": "মোট $n$ টি বস্তুর মধ্যে $p$ টি একরকম, $q$ টি অন্যরকম হলে মোট বিন্যাস সংখ্যা $= \\frac{n!}{p! q!}$। স্বরবর্ণ একত্রে রেখে বিন্যাস: সকল স্বরবর্ণকে ১টি বর্ণ বিবেচনা করে মোট বিন্যাস $\\times$ স্বরবর্ণগুলোর নিজস্ব অভ্যন্তরীণ বিন্যাস। স্বরবর্ণ পাশাপাশি না রেখে বিন্যাস: মোট বিন্যাস মাইনাস স্বরবর্ণ একত্রে রেখে বিন্যাস। আপেক্ষিক ক্রম পরিবর্তন না করে বিন্যাস: স্বরবর্ণগুলোর আপেক্ষিক অবস্থান ঠিক থাকলে তাদের নিজস্ব ফ্যাক্টোরিয়াল দিয়ে ভাগ হবে। চক্রাকার বা গোল টেবিলে বিন্যাস: $n$ জনের জন্য $(n-1)!$; ফুলের মালা বা মুক্তার হারের ক্ষেত্রে উল্টানো যায় বলে $\\frac{(n-1)!}{2}$।",
                    "speed_elimination": "স্বরবর্ণ একত্রে না রাখার নিয়ম = মোট বিন্যাস $-$ স্বরবর্ণ একত্রে রেখে বিন্যাস; গোল টেবিলে বিন্যাস $(n-1)!$।"
                },
                {
                    "type_id": "math_m05_t2",
                    "name": "Type 2: সমাবেশ, দল গঠন ও জ্যামিতিক বিন্দুর সংযোগ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '22-23", "JU '21-22", "GST '21-22", "BUET '20-21"],
                    "qb_question_refs": ["VAR-JnU-P03-Q13", "VAR-DU-P04-Q04", "VAR-GST-P03-Q05"],
                    "core_rule": "সমাবেশ $^nC_r = \\frac{n!}{r!(n-r)!}$। সম্পর্ক: $^nP_r = r! \\times ^nC_r$। সম্পূরক সমাবেশ: $^nC_x = ^nC_y \\implies x = y$ অথবা $x + y = n$। প্যাসকেলের অভেদ: $^nC_r + ^nC_{r-1} = ^{n+1}C_r$। মোট উপসেট সংখ্যা $2^n$ ($^nC_0 + ^nC_1 + \\dots + ^nC_n = 2^n$); অন্তত একটি বস্তু নিয়ে সমাবেশ $= 2^n - 1$। জ্যামিতিক সমস্যা: $n$ টি বিন্দুর মধ্যে কোনো ৩টি সমরেখ না হলে: সরলরেখা সংখ্যা $= ^nC_2$; ত্রিভুজ সংখ্যা $= ^nC_3$; কর্ণ সংখ্যা (বহুভুজের) $= ^nC_2 - n = \\frac{n(n-3)}{2}$।",
                    "speed_elimination": "যদি $^nC_8 = ^nC_{12}$ হয়, তবে $n = 8 + 12 = 20$; বহুভুজের কর্ণ সংখ্যা $= \\frac{n(n-3)}{2}$ (দশভুজের কর্ণ $\\frac{10 \\times 7}{2} = 35$)।"
                }
            ]
        },
        {
            "id": "math_1st_06",
            "aliases": ["math_trig_ratios"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৬",
            "title": "ত্রিকোণমিতিক অনুপাত (Trigonometric Ratios)",
            "subtitle": "বৃত্তীয় পরিমাপ (s=rθ), চতুর্ভাগ চিহ্ন এবং মৌলিক অনুপাত অভেদ",
            "total_qb_questions": 320,
            "high_yield_score": 94,
            "mega_types": [
                {
                    "type_id": "math_m06_t1",
                    "name": "Type 1: বৃত্তচাপ, ব্যাসার্ধ ও কোণ ($s = r\theta$) এবং ঘড়ির কাঁটার কোণ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P04-Q05", "VAR-DU-P06-Q02"],
                    "core_rule": "বৃত্তচাপের দৈর্ঘ্য $s = r\\theta$ (যেখানে $\\theta$ অবশ্যই রেডিয়ান এককে, $1^\\circ = \\frac{\\pi}{180}\\text{ rad}$)। বৃত্তাংশের ক্ষেত্রফল $A = \\frac{1}{2}r^2\\theta = \\frac{1}{2}s r$। ঘড়ির কাঁটা ও মিনিটের কাঁটার মধ্যবর্তী কোণ: $\\theta = |30 H - \\frac{11}{2} M|$ (যদি $\\theta > 180^\\circ$ হয় তবে $360^\\circ - \\theta$ বিয়োগ করতে হবে)। যেমন ২টা ১৫ মিনিটে কোণ: $|30(2) - \\frac{11}{2}(15)| = |60 - 82.5| = 22.5^\\circ$।",
                    "speed_elimination": "ঘড়ির কাঁটার কোণের শর্টকাট: $\\theta = |30H - 5.5M|$; $s = r\\theta$ সূত্রে $\\theta$ অবশ্যই রেডিয়ানে রাখতে হবে।"
                },
                {
                    "type_id": "math_m06_t2",
                    "name": "Type 2: চতুর্ভাগে চিহ্নের নিয়ম ও ত্রিকোণমিতিক রূপান্তর",
                    "importance": "4-Star",
                    "stars": 4,
                    "repeat_frequency": 24,
                    "past_tags": ["DU '21-22", "RU '20-21", "GST '21-22"],
                    "qb_question_refs": ["VAR-DU-P08-Q04", "VAR-RU-P05-Q03"],
                    "core_rule": "All-Sin-Tan-Cos নিয়ম: ১ম চতুর্ভাগে সকল অনুপাত ধ্রুবক; ২য় চতুর্ভাগে $\\sin, \\csc$ পজিটিভ; ৩য় চতুর্ভাগে $\\tan, \\cot$ পজিটিভ; ৪র্থ চতুর্ভাগে $\\cos, \\sec$ পজিটিভ। ঋণাত্মক কোণ: $\\cos(-\\theta) = \\cos\\theta$, $\\sec(-\\theta) = \\sec\\theta$; কিন্তু $\\sin(-\\theta) = -\\sin\\theta$, $\\tan(-\\theta) = -\\tan\\theta$। $(n \\frac{\\pi}{2} \\pm \\theta)$: $n$ জোড় হলে অনুপাত অপরিবর্তিত থাকে; $n$ বিজোড় হলে পরিবর্তিত হয় ($\sin \\leftrightarrow \cos, \tan \\leftrightarrow \cot, \sec \\leftrightarrow \csc$)।",
                    "speed_elimination": "কস ও সেক ঋণাত্মক চিহ্ন শোষণ করে ($\cos(-\\theta) = \cos\\theta$); বিজোড় $\\pi/2$ থাকলে অনুপাত পাল্টে যায়।"
                }
            ]
        },
        {
            "id": "math_1st_07",
            "aliases": ["math_trig_associated"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৭",
            "title": "সংযুক্ত কোণের ত্রিকোণমিতিক অনুপাত (Associated Angles)",
            "subtitle": "যৌগিক কোণ, রূপান্তর সূত্র, গুণিতক কোণ (2A/3A) ও ত্রিভুজের গুণাবলী",
            "total_qb_questions": 470,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m07_t1",
                    "name": "Type 1: গুণিতক কোণের সূত্র ও বর্গের যোগফল সিরিজ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P01-Q15", "VAR-DU-P01-Q06", "VAR-RU-P02-Q05"],
                    "core_rule": "গুণিতক কোণ: $\\sin 2A = 2\\sin A\\cos A = \\frac{2\\tan A}{1+\\tan^2 A}$; $\\cos 2A = \\cos^2 A - \\sin^2 A = 2\\cos^2 A - 1 = 1 - 2\\sin^2 A = \\frac{1-\\tan^2 A}{1+\\tan^2 A}$। অত্যন্ত গুরুত্বপূর্ণ সিরিজ রেজাল্ট: $\\sin^2 10^\\circ + \\sin^2 20^\\circ + \\dots + \\sin^2 80^\\circ = 4$; $\\cos^2 10^\\circ + \\dots + \\cos^2 80^\\circ = 4$। যদি $A+B = 45^\\circ$ বা $\\frac{\\pi}{4}$ হয়, তবে $(1+\\tan A)(1+\\tan B) = 2$ এবং $(\\cot A - 1)(\\cot B - 1) = 2$।",
                    "speed_elimination": "$A+B = 45^\\circ$ হলে $(1+\\tan A)(1+\\tan B) = 2$ ফিক্সড রেজাল্ট; $\\sin^2\\theta + \cos^2\\theta = 1$ মিলিয়ে সিরিজ মান বের করুন।"
                },
                {
                    "type_id": "math_m07_t2",
                    "name": "Type 2: ত্রিভুজের সাইন ও কোসাইন সূত্র এবং ক্ষেত্রফল",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '20-21", "JU '21-22", "GST '21-22", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q10", "VAR-DU-P03-Q06", "VAR-CU-P04-Q08"],
                    "core_rule": "সাইন সূত্র: $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$ ($R$ হলো পরিব্যাসার্ধ)। কোসাইন সূত্র: $\\cos A = \\frac{b^2 + c^2 - a^2}{2bc}$, $\\cos B = \\frac{c^2 + a^2 - b^2}{2ca}$, $\\cos C = \\frac{a^2 + b^2 - c^2}{2ab}$। ত্রিভুজের ক্ষেত্রফল: $\\Delta = \\frac{1}{2}ab\\sin C = \\frac{abc}{4R} = r s = \\sqrt{s(s-a)(s-b)(s-c)}$ (যেখানে $s = \\frac{a+b+c}{2}$, $r$ হলো অন্তর্ব্যাসার্ধ)। অভিক্ষেপ সূত্র: $a = b\\cos C + c\\cos B$।",
                    "speed_elimination": "যদি বাহুত্রয় ৩, ৫, ৭ হয় তবে বৃহত্তম কোণ $\\cos C = \\frac{9+25-49}{30} = -\\frac{1}{2} \\implies C = 120^\\circ$।"
                }
            ]
        },
        {
            "id": "math_1st_08",
            "aliases": ["math_functions"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৮",
            "title": "ফাংশন ও ফাংশনের লেখচিত্র (Functions & Graphs)",
            "subtitle": "ডোমেন, রেঞ্জ, বিপরীত ফাংশন (f^-1), সংযোজিত ফাংশন ও সমতা",
            "total_qb_questions": 420,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "math_m08_t1",
                    "name": "Type 1: ফাংশনের ডোমেন ও রেঞ্জ নির্ণয়",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q14", "VAR-DU-P02-Q07", "VAR-RU-P01-Q05"],
                    "core_rule": "১. ভগ্নাংশ ফাংশন $f(x) = \\frac{ax+b}{cx+d}$: ডোমেন $\\mathbb{R} - \\{-d/c\\}$; রেঞ্জ $\\mathbb{R} - \\{a/c\\}$ (সহগের অনুপাত)। ২. বর্গমূল ফাংশন: $f(x) = \\sqrt{a^2 - x^2}$ এর ডোমেন $[-a, a]$; রেঞ্জ $[0, a]$। ৩. লগারিদম ফাংশন $f(x) = \\ln(x - a)$: ডোমেন $(a, \\infty)$; রেঞ্জ $\\mathbb{R}$। ৪. $f(x) = \\sqrt{\\frac{x-a}{x-b}}$: ডোমেন $(-\\infty, a] \\cup (b, \\infty)$।",
                    "speed_elimination": "$f(x) = \\frac{2x+3}{5x-4}$ এর ডোমেন $\\mathbb{R} - \\{4/5\\}$ এবং রেঞ্জ $\\mathbb{R} - \\{2/5\\}$ (৩ সেকেন্ডে সহগ দেখে উত্তর); $\\sqrt{16-x^2}$ এর ডোমেন $[-4, 4]$ ও রেঞ্জ $[0, 4]$।"
                },
                {
                    "type_id": "math_m08_t2",
                    "name": "Type 2: বিপরীত ফাংশন ($f^{-1}$) ও সংযোজিত ফাংশন ($f \\circ g$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '22-23", "JU '21-22", "GST '21-22"],
                    "qb_question_refs": ["VAR-JnU-P02-Q12", "VAR-DU-P04-Q06", "VAR-GST-P02-Q07"],
                    "core_rule": "বিপরীত ফাংশন বিদ্যমান থাকার শর্ত: ফাংশনটিকে অবশ্যই এক-এক ও সার্বিক (Bijective) হতে হবে। লিনিয়ার ভগ্নাংশের শর্টকাট ইনভার্স: $f(x) = \\frac{ax+b}{cx+d} \\implies f^{-1}(x) = \\frac{-dx+b}{cx-a}$ ($a$ ও $d$ স্থান বদল ও চিহ্ন বদল করে)। সংযোজিত ফাংশন: $(f \\circ g)(x) = f(g(x))$; $(g \\circ f)(x) = g(f(x))$। সমতা: $f(f^{-1}(x)) = x$।",
                    "speed_elimination": "$f(x) = \\frac{ax+b}{cx+d}$ এর ইনভার্স বের করতে প্রধান কর্ণের $a$ ও $d$ এর চিহ্ন উল্টে স্থান পরিবর্তন করুন।"
                }
            ]
        },
        {
            "id": "math_1st_09",
            "aliases": ["math_differentiation", "math_p1_ch09"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৯",
            "title": "অন্তরীকরণ (Differentiation)",
            "subtitle": "লিমিট ও এল-হসপিটাল নিয়ম, চেইন রুল, স্পর্শক-অভিলম্ব ও গুরুমান-লঘুমান",
            "total_qb_questions": 520,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m09_t1",
                    "name": "Type 1: লিমিট নির্ণয় ও এল-হসপিটাল (L'Hôpital) শর্টকাট",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 42,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '21-22", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P01-Q16", "VAR-DU-P01-Q08", "VAR-RU-P01-Q07", "VAR-GST-P01-Q07"],
                    "core_rule": "মান বসিয়ে অনির্ণেয় আকার ($\frac{0}{0}$ বা $\frac{\\infty}{\\infty}$) এলে লব ও হরকে পৃথকভাবে $x$ এর সাপেক্ষে অন্তরীকরণ করতে হবে: $\\lim_{x \\to a} \\frac{f(x)}{g(x)} = \\lim_{x \\to a} \\frac{f'(x)}{g'(x)}$। স্ট্যান্ডার্ড ফর্মুলা: ১. $\\lim_{x \\to 0} \\frac{\\sin ax}{bx} = \\frac{a}{b}$, $\\lim_{x \\to 0} \\frac{\\tan ax}{bx} = \\frac{a}{b}$; ২. $\\lim_{x \\to 0} \\frac{1 - \\cos ax}{x^2} = \\frac{a^2}{2}$; ৩. $\\lim_{x \\to 0} \\frac{1 - \\cos ax}{1 - \\cos bx} = \\frac{a^2}{b^2}$; ৪. $\\lim_{x \\to 0} (1 + ax)^{b/x} = e^{ab}$; $\\lim_{x \\to \\infty} \\left(1 + \\frac{a}{x}\\right)^{bx} = e^{ab}$; ৫. $\\lim_{x \\to \\infty} \\frac{a x^n + \\dots}{b x^n + \\dots} = \\frac{a}{b}$ (সর্বোচ্চ ঘাতের সহগের অনুপাত)।",
                    "speed_elimination": "$\lim_{x\\to 0} \\frac{1-\\cos 4x}{x^2} = \\frac{4^2}{2} = 8$; $\lim_{x\\to 0} (1+3x)^{2/x} = e^{3\\times 2} = e^6$ (১ সেকেন্ডে উত্তর)।"
                },
                {
                    "type_id": "math_m09_t2",
                    "name": "Type 2: স্পর্শক ও অভিলম্বের ঢাল এবং সমীকরণ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '21-22", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P02-Q14", "VAR-DU-P03-Q07", "VAR-RU-P04-Q05"],
                    "core_rule": "বক্ররেখার $(x_1, y_1)$ বিন্দুতে স্পর্শকের ঢাল $m = \\left(\\frac{dy}{dx}\\right)_{(x_1, y_1)}$। স্পর্শকের সমীকরণ: $y - y_1 = m (x - x_1)$। অভিলম্বের ঢাল $m' = -\\frac{1}{m}$। অভিলম্বের সমীকরণ: $y - y_1 = -\\frac{1}{m} (x - x_1)$। স্পর্শক $x$-অক্ষের সমান্তরাল হলে $\\frac{dy}{dx} = 0$; স্পর্শক $y$-অক্ষের সমান্তরাল (বা $x$-অক্ষের ওপর লম্ব) হলে $\\frac{dy}{dx} = \\infty \\implies \\frac{dx}{dy} = 0$।",
                    "speed_elimination": "স্পর্শক $x$-অক্ষের সমান্তরাল বললে ১ম ডেরিভেটিভ শূন্য ($\frac{dy}{dx} = 0$) বসিয়ে বিন্দুর স্থানাঙ্ক বের করুন।"
                },
                {
                    "type_id": "math_m09_t3",
                    "name": "Type 3: গুরুমান ও লঘুমান (Maxima & Minima) নির্ণয়",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '20-21", "JU '20-21", "GST '22-23", "BUET '20-21"],
                    "qb_question_refs": ["VAR-JnU-P04-Q12", "VAR-DU-P05-Q07", "VAR-CU-P03-Q08"],
                    "core_rule": "চরম মানের প্রয়োজনীয় শর্ত: $f'(x) = 0$; এখান থেকে সংকট বিন্দু বা টার্নিং পয়েন্ট $x = c$ পাওয়া যায়। পর্যাপ্ত শর্ত: ১. গুরুমানের জন্য: $f''(c) < 0$ (ঋণাত্মক হলে গুরুমান বিদ্যমান); ২. লঘুমানের জন্য: $f''(c) > 0$ (ধনাত্মক হলে লঘুমান বিদ্যমান)। নতি পরিবর্তন বিন্দু (Point of inflection): $f''(x) = 0$ এবং $f'''(x) \\ne 0$। স্ট্যান্ডার্ড রেজাল্ট: $f(x) = x^{1/x}$ এর সর্বোচ্চ মান $x = e$ বিন্দুতে এবং সর্বোচ্চ মান $e^{1/e}$।",
                    "speed_elimination": "$f'(x)=0$ বসিয়ে প্রান্তিক বিন্দু পান; ২য় ডেরিভেটিভ ঋণাত্মক হলে গুরুমান এবং ধনাত্মক হলে লঘুমান।"
                }
            ]
        },
        {
            "id": "math_1st_10",
            "aliases": ["math_integration", "math_p1_ch10"],
            "subject": "Higher Math",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ১০",
            "title": "যোগজীকরণ (Integration)",
            "subtitle": "প্রতিস্থাপন, আংশিক ভগ্নাংশ, নির্দিষ্ট যোগজ ও আবদ্ধ অঞ্চলের ক্ষেত্রফল",
            "total_qb_questions": 510,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m10_t1",
                    "name": "Type 1: আদর্শ প্রতিস্থাপন ও লব-হর ডেরিভেটিভ শর্টকাট",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 40,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P01-Q17", "VAR-DU-P01-Q11", "VAR-RU-P02-Q07", "VAR-GST-P01-Q10"],
                    "core_rule": "মাস্টার শর্টকাট সূত্রাবলী: ১. $\\int \\frac{f'(x)}{f(x)} dx = \\ln|f(x)| + c$; ২. $\\int \\frac{f'(x)}{\\sqrt{f(x)}} dx = 2\\sqrt{f(x)} + c$; ৩. $\\int [f(x)]^n f'(x) dx = \\frac{[f(x)]^{n+1}}{n+1} + c$; ৪. $\\int e^x [f(x) + f'(x)] dx = e^x f(x) + c$। আদর্শ রূপান্তর: $\\int \\frac{1}{x^2 - a^2} dx = \\frac{1}{2a}\\ln\\left|\\frac{x-a}{x+a}\\right| + c$; $\\int \\frac{1}{\\sqrt{a^2 - x^2}} dx = \\sin^{-1}\\left(\\frac{x}{a}\\right) + c$; $\\int \\frac{1}{a^2 + x^2} dx = \\frac{1}{a}\\tan^{-1}\\left(\\frac{x}{a}\\right) + c$।",
                    "speed_elimination": "হরের অন্তরীকরণ লবে থাকলে উত্তর সরাসরি $\\ln|\\text{হর}|$; যেমন $\\int \\frac{2x+3}{x^2+3x+5} dx = \\ln|x^2+3x+5| + c$।"
                },
                {
                    "type_id": "math_m10_t2",
                    "name": "Type 2: নির্দিষ্ট যোগজের ধর্মাবলী ও মডুলাস ফাংশন",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '19-20", "RU '22-23", "JU '21-22", "GST '21-22", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P03-Q14", "VAR-DU-P03-Q10", "VAR-GST-P03-Q09"],
                    "core_rule": "১. কিং'স প্রোপার্টি (King's Property): $\\int_0^a f(x) dx = \\int_0^a f(a - x) dx$। এর প্রয়োগ: $\\int_0^{\\pi/2} \\frac{\\sin^n x}{\\sin^n x + \\cos^n x} dx = \\frac{\\pi/2 - 0}{2} = \\frac{\\pi}{4}$ (যেকোনো ঘাত $n$ এর জন্য উত্তর সর্বদা $\\pi/4$)। ২. বিজোড় ফাংশন [$f(-x) = -f(x)$]: $\\int_{-a}^a f(x) dx = 0$ (যেমন $\\int_{-1}^1 x^3 dx = 0$, $\\int_{-\\pi/2}^{\\pi/2} \\sin^5 x dx = 0$); জোড় ফাংশন [$f(-x) = f(x)$]: $\\int_{-a}^a f(x) dx = 2\\int_0^a f(x) dx$। ৩. মডুলাস: $\\int_{-a}^a |x| dx = 2 \\int_0^a x dx = a^2$।",
                    "speed_elimination": "$-a$ থেকে $+a$ সীমার মধ্যে বিজোড় ফাংশনের ইন্টিগ্রেশনের মান সর্বদা শূন্য ($0$); প্রতিসম সাইন-কস ভগ্নাংশে উত্তর $\\pi/4$।"
                },
                {
                    "type_id": "math_m10_t3",
                    "name": "Type 3: আবদ্ধ ক্ষেত্রের ক্ষেত্রফল (বক্ররেখা ও সরলরেখা)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '20-21", "GST '22-23", "BUET '18-19"],
                    "qb_question_refs": ["VAR-JnU-P05-Q12", "VAR-DU-P04-Q09", "VAR-RU-P04-Q07"],
                    "core_rule": "ক্ষেত্রফল সংক্রান্ত সুপার শর্টকাট: ১. পরাবৃত্ত $y^2 = 4ax$ এবং সরলরেখা $y = mx$ দ্বারা আবদ্ধ ক্ষেত্রফল: $A = \\frac{8a^2}{3m^3}$। ২. দুটি পরাবৃত্ত $y^2 = 4ax$ এবং $x^2 = 4by$ দ্বারা আবদ্ধ ক্ষেত্রফল: $A = \\frac{16ab}{3}$ (যেমন $y^2 = 4x$ ও $x^2 = 4y$ এর জন্য $a=1, b=1 \\implies A = \\frac{16}{3}$)। ৩. উপবৃত্ত $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ এর ক্ষেত্রফল: $A = \\pi a b$। ৪. বৃত্ত $x^2 + y^2 = a^2$ এর ক্ষেত্রফল: $A = \\pi a^2$।",
                    "speed_elimination": "উপবৃত্তের ক্ষেত্রফল $\\pi a b$ (যেমন $\\frac{x^2}{16} + \\frac{y^2}{9} = 1$ এর ক্ষেত্রফল $\\pi \\times 4 \\times 3 = 12\\pi$); দুটি পরাবৃত্তে $A = \\frac{16ab}{3}$।"
                }
            ]
        },

        # =========================================================================
        # HIGHER MATH 2ND PAPER (উচ্চতর গণিত ২য় পত্র - ১০টি পৃথক অধ্যায়)
        # =========================================================================
        {
            "id": "math_2nd_01",
            "aliases": ["math_real_numbers"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০১",
            "title": "বাস্তব সংখ্যা ও অসমতা (Real Numbers & Inequalities)",
            "subtitle": "পরম মান সম্বলিত অসমতা, পরম মান চিহ্ন বর্জন, সুপ্রিমাম ও ইনফিমাম",
            "total_qb_questions": 330,
            "high_yield_score": 94,
            "mega_types": [
                {
                    "type_id": "math_m11_t1",
                    "name": "Type 1: পরম মান সম্বলিত অসমতা সমাধান ও পরম মান বর্জন",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P02-Q15", "VAR-DU-P05-Q08"],
                    "core_rule": "১. $|x| < a \\iff -a < x < a$ (ব্যবধি: $(-a, a)$)। ২. $|x| > a \\iff x > a$ অথবা $x < -a$ (ব্যবধি: $(-\\infty, -a) \\cup (a, \\infty)$)। ৩. অসমতাকে পরম মান চিহ্নের সাহায্যে প্রকাশ: $a < x < b$ হলে উভয় প্রান্তের গড় $m = \\frac{a+b}{2}$ বিয়োগ করতে হবে: $-\\frac{b-a}{2} < x - \\frac{a+b}{2} < \\frac{b-a}{2} \\implies \\left|x - \\frac{a+b}{2}\\right| < \\frac{b-a}{2}$। ৪. ত্রিভুজীয় অসমতা: $|a + b| \\le |a| + |b|$ এবং $|a - b| \\ge ||a| - |b||$।",
                    "speed_elimination": "$a < x < b$ কে পরম মানে নিতে: $|x - \\text{গড়}| < \\text{অর্ধ-দূরত্ব}$; যেমন $-1 < x < 5$ এ গড় ২, দূরত্ব ৩, তাই $|x - 2| < 3$।"
                },
                {
                    "type_id": "math_m11_t2",
                    "name": "Type 2: সুপ্রিমাম (লঘিষ্ঠ ঊর্ধ্বসীমা) ও ইনফিমাম (গরিষ্ঠ নিম্নসীমা)",
                    "importance": "4-Star",
                    "stars": 4,
                    "repeat_frequency": 24,
                    "past_tags": ["DU '21-22", "RU '20-21", "JU '21-22", "GST '21-22"],
                    "qb_question_refs": ["VAR-DU-P07-Q06", "VAR-RU-P03-Q06"],
                    "core_rule": "সুপ্রিমাম (Supremum): ঊর্ধ্বসীমাসমূহের মধ্যে ক্ষুদ্রতম মান (LUB - Least Upper Bound)। ইনফিমাম (Infimum): নিম্নসীমাসমূহের মধ্যে বৃহত্তম মান (GLB - Greatest Lower Bound)। উদাহরণ: $S = \\left\\{ \\frac{1}{n} : n \\in \\mathbb{N} \\right\\} = \\{1, \\frac{1}{2}, \\frac{1}{3}, \\dots\\}$ এর সুপ্রিমাম $\\sup(S) = 1$ (সেটের অন্তর্ভুক্ত) এবং ইনফিমাম $\\inf(S) = 0$ (সেটের বাইরে)। মুক্ত ব্যবধি $(a, b)$ এর সুপ্রিমাম $b$ এবং ইনফিমাম $a$ (উভয়ই সেটের বাইরে)। বাস্তব সংখ্যার পূর্ণাঙ্গতা স্বীকার্য: বাস্তব সংখ্যার যেকোনো অশূন্য ওপরের দিকে সীমাবদ্ধ উপসেটের একটি সুপ্রিমাম থাকে।",
                    "speed_elimination": "সেটের উপাদানগুলোর সর্বোচ্চ সীমা হলো সুপ্রিমাম এবং সর্বনিম্ন সীমা হলো ইনফিমাম (সেটের অন্তর্ভুক্ত হওয়া বাধ্যতামূলক নয়)।"
                }
            ]
        },
        {
            "id": "math_2nd_02",
            "aliases": ["math_linear_programming"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০২",
            "title": "যোগাশ্রয়ী প্রোগ্রাম (Linear Programming)",
            "subtitle": "অভিষ্ট ফাংশন, সীমাবদ্ধতা, সম্ভাব্য এলাকা ও প্রান্তিক বিন্দু পদ্ধতি",
            "total_qb_questions": 290,
            "high_yield_score": 93,
            "mega_types": [
                {
                    "type_id": "math_m12_t1",
                    "name": "Type 1: প্রান্তিক বিন্দু পদ্ধতি ও চরম মান (সর্বোচ্চকরণ/সর্বনিম্নকরণ)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 28,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P04-Q13", "VAR-DU-P06-Q07"],
                    "core_rule": "যোগাশ্রয়ী প্রোগ্রামে অভিষ্ট ফাংশন $Z = ax + by$ এর সর্বোচ্চ বা সর্বনিম্ন মান সর্বদা সমাধান এলাকার শীর্ষবিন্দু বা প্রান্তিক বিন্দুতে (Corner points) ঘটে। সমাধান কৌশল: ১. সীমাবদ্ধতাসমূহের অসমতাকে সমীকরণ ধরে রেখাগুলোর অক্ষদ্বয়ের ছেদবিন্দু নির্ণয়; ২. রেখাদ্বয়ের পারস্পরিক ছেদবিন্দু বের করা; ৩. সম্ভাব্য সমাধান এলাকার সকল শীর্ষবিন্দুতে $Z$ এর মান বের করে বৃহত্তম মানকে সর্বোচ্চ মান এবং ক্ষুদ্রতম মানকে সর্বনিম্ন মান হিসেবে নির্বাচন করা। অঋণাত্মক শর্ত: $x \\ge 0, y \\ge 0$ (সমাধান এলাকা ১ম চতুর্ভাগে সীমাবদ্ধ)।",
                    "speed_elimination": "রেখাগুলোর ছেদবিন্দু ও অক্ষের ছেদবিন্দুগুলো সরাসরি অভিষ্ট ফাংশন $Z$-এ বসিয়ে মান তুলনা করুন।"
                }
            ]
        },
        {
            "id": "math_2nd_03",
            "aliases": ["math_complex_numbers"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৩",
            "title": "জটিল সংখ্যা (Complex Numbers)",
            "subtitle": "মডুলাস, মুখ্য আর্গুমেন্ট, বর্গমূল, ১ এর কাল্পনিক ঘনমূল (ω) ও সঞ্চারপথ",
            "total_qb_questions": 470,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m13_t1",
                    "name": "Type 1: মডুলাস ও মুখ্য আর্গুমেন্ট নির্ণয় ($-\\pi < \\theta \\le \\pi$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q18", "VAR-DU-P01-Q13", "VAR-RU-P02-Q09"],
                    "core_rule": "$z = x + iy$ এর মডুলাস $|z| = \\sqrt{x^2 + y^2}$। মুখ্য আর্গুমেন্ট $\\theta$: ১. ১ম চতুর্ভাগ ($x>0, y>0$): $\\theta = \\tan^{-1}\\left(\\frac{y}{x}\\right)$; ২. ২য় চতুর্ভাগ ($x<0, y>0$): $\\theta = \\pi - \\tan^{-1}\\left|\\frac{y}{x}\\right|$; ৩. ৩য় চতুর্ভাগ ($x<0, y<0$): $\\theta = -\\pi + \\tan^{-1}\\left|\\frac{y}{x}\\right|$; ৪. ৪র্থ চতুর্ভাগ ($x>0, y<0$): $\\theta = -\\tan^{-1}\\left|\\frac{y}{x}\\right|$। বৈশিষ্ট্য: $|z_1 z_2| = |z_1| |z_2|$; $\\text{Arg}(z_1 z_2) = \\text{Arg}(z_1) + \\text{Arg}(z_2)$; $\\text{Arg}(z_1/z_2) = \\text{Arg}(z_1) - \\text{Arg}(z_2)$। $i$ এর ঘাত: $i^{4n} = 1, i^{4n+1} = i, i^{4n+2} = -1, i^{4n+3} = -i$ (ঘাতকে ৪ দিয়ে ভাগ করে ভাগশেষ নিতে হবে)।",
                    "speed_elimination": "$z = -1 - \\sqrt{3}i$ ৩য় চতুর্ভাগে, তাই আর্গুমেন্ট $-\\pi + \\frac{\\pi}{3} = -\\frac{2\\pi}{3}$; $i^{-49} = i^{-1} = -i$।"
                },
                {
                    "type_id": "math_m13_t2",
                    "name": "Type 2: ১ এর কাল্পনিক ঘনমূল ($\omega, \omega^2$) ও বর্গমূল",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '21-22", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q16", "VAR-DU-P03-Q12", "VAR-GST-P01-Q13"],
                    "core_rule": "১ এর ৩টি ঘনমূল: ১, $\\omega = \\frac{-1 + \\sqrt{3}i}{2}$, $\\omega^2 = \\frac{-1 - \\sqrt{3}i}{2}$। ধর্মাবলী: ১. $1 + \\omega + \\omega^2 = 0$; ২. $\\omega^3 = 1 \\implies \\omega^{3n} = 1, \\omega^{3n+1} = \\omega, \\omega^{3n+2} = \\omega^2$; ৩. $\\omega$ ও $\\omega^2$ পরস্পরের অনুবন্ধী ও বর্গ। জটিল সংখ্যার বর্গমূল শর্টকাট: $\\sqrt{a \\pm ib} = \\pm \\left[ \\sqrt{\\frac{|z|+a}{2}} \\pm i \\sqrt{\\frac{|z|-a}{2}} \\right]$। যেমন $\\sqrt{-8 - 6i} = \\pm (1 - 3i)$ (যেহেতু $|z| = \\sqrt{64+36} = 10$). সঞ্চারপথ: $|z - z_0| = r$ হলো $z_0$ কেন্দ্র ও $r$ ব্যাসার্ধের বৃত্ত।",
                    "speed_elimination": "$\\omega$ এর ঘাতকে ৩ দিয়ে ভাগ করে ভাগশেষ নিন (যেমন $\\omega^{2026} = \\omega^1 = \\omega$); বর্গমূলের অপশনগুলো বর্গ করে মূল সংখ্যা মিলিয়ে নিন।"
                }
            ]
        },
        {
            "id": "math_2nd_04",
            "aliases": ["math_polynomials"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৪",
            "title": "বহুপদী ও বহুপদী সমীকরণ (Polynomials)",
            "subtitle": "দ্বিঘাত সমীকরণের মূলের প্রকৃতি, মূল ও সহগ সম্পর্ক এবং সাধারণ মূলের শর্ত",
            "total_qb_questions": 480,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m14_t1",
                    "name": "Type 1: নিশ্চয়ক ও মূলের প্রকৃতি (বাস্তব, মূলদ ও কাল্পনিক)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P01-Q19", "VAR-DU-P02-Q10", "VAR-RU-P01-Q09"],
                    "core_rule": "$ax^2 + bx + c = 0$ এর নিশ্চয়ক/পৃথায়ক $D = b^2 - 4ac$। ১. $D > 0$: মূলদ্বয় বাস্তব ও অসমান; $D$ পূর্ণবর্গ হলে মূলদ, পূর্ণবর্গ না হলে অমূলদ এবং অনুবন্ধী জোড়ায় থাকে ($p + \\sqrt{q}$ ও $p - \\sqrt{q}$); ২. $D = 0$: মূলদ্বয় বাস্তব ও সমান ($x = -b/2a$); ৩. $D < 0$: মূলদ্বয় কাল্পনিক/জটিল ও অনুবন্ধী জোড়ায় থাকে ($p + iq$ ও $p - iq$)। মূলদ্বয় সমান হওয়ার শর্ত: $b^2 - 4ac = 0$। পূর্ণবর্গ রাশি হওয়ার শর্ত: নিশ্চয়ক শূন্য ($D=0$)।",
                    "speed_elimination": "একটি মূল $2 + \\sqrt{3}$ হলে অপর মূলটি স্বয়ংক্রিয়ভাবে $2 - \\sqrt{3}$; মূলদ্বয় সমান বললে $b^2 - 4ac = 0$ বসান।"
                },
                {
                    "type_id": "math_m14_t2",
                    "name": "Type 2: মূল ও সহগের সম্পর্ক এবং নতুন সমীকরণ গঠন",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '20-21", "JU '21-22", "GST '21-22", "BUET '20-21"],
                    "qb_question_refs": ["VAR-JnU-P02-Q16", "VAR-DU-P04-Q10", "VAR-GST-P02-Q11"],
                    "core_rule": "$ax^2 + bx + c = 0$ এর মূলদ্বয় $\\alpha, \\beta$ হলে: $\\alpha + \\beta = -\\frac{b}{a}$, $\\alpha\\beta = \\frac{c}{a}$। সমীকরণ: $x^2 - (\\alpha+\\beta)x + \\alpha\\beta = 0$। মূলদ্বয়ের অন্তর $|\alpha - \beta| = \\frac{\\sqrt{b^2 - 4ac}}{|a|}$। ত্রিঘাত সমীকরণ $ax^3 + bx^2 + cx + d = 0$ এর মূলত্রয় $\\alpha, \\beta, \\gamma$ হলে: $\\Sigma\\alpha = -\\frac{b}{a}$, $\\Sigma\\alpha\\beta = \\frac{c}{a}$, $\\alpha\\beta\\gamma = -\\frac{d}{a}$। একটি সাধারণ মূল থাকার শর্ত ($a_1 x^2 + b_1 x + c_1 = 0$ ও $a_2 x^2 + b_2 x + c_2 = 0$): বজ্রগুণনে $(c_1 a_2 - c_2 a_1)^2 = (a_1 b_2 - a_2 b_1)(b_1 c_2 - b_2 c_1)$।",
                    "speed_elimination": "মূলদ্বয় একটি অপরটির উল্টো ($\alpha, 1/\alpha$) হলে ধ্রুবক ও $x^2$ এর সহগ সমান ($c = a$); মূলদ্বয় সমান ও বিপরীত চিহ্নযুক্ত হলে $b = 0$।"
                }
            ]
        },
        {
            "id": "math_2nd_05",
            "aliases": ["math_binomial"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৫",
            "title": "দ্বিপদী বিস্তৃতি (Binomial Expansion)",
            "subtitle": "সাধারণ পদ (T_r+1), মধ্যপদ, x-বর্জিত পদ ও দ্বিপদী সহগ",
            "total_qb_questions": 420,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "math_m15_t1",
                    "name": "Type 1: সাধারণ পদ ($T_{r+1}$) ও $x$-বর্জিত পদ নির্ণয়",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P01-Q20", "VAR-DU-P03-Q08", "VAR-RU-P02-Q12"],
                    "core_rule": "$(a + x)^n$ এর বিস্তৃতিতে $(r+1)$-তম সাধারণ পদ: $T_{r+1} = ^nC_r a^{n-r} x^r$। $\\left(ax^p + \\frac{b}{x^q}\\right)^n$ এর বিস্তৃতিতে: ১. $x$-বর্জিত পদ বা ধ্রুব পদের জন্য $r = \\frac{n p}{p + q}$; ২. $x^k$ এর সহগের জন্য $r = \\frac{n p - k}{p + q}$ (যেখানে $r$ অবশ্যই অঋণাত্মক পূর্ণসংখ্যা হতে হবে)। দ্বিপদী সহগসমূহের সমষ্টি: $C_0 + C_1 + C_2 + \\dots + C_n = 2^n$; বিজোড় ও জোড় পদের সহগের সমষ্টি সমান: $C_0 + C_2 + \\dots = C_1 + C_3 + \\dots = 2^{n-1}$।",
                    "speed_elimination": "$\\left(x + \\frac{1}{x}\\right)^{2n}$ এ $x$-বর্জিত পদ হলো মধ্যপদ এবং এর মান $^{2n}C_n$।"
                },
                {
                    "type_id": "math_m15_t2",
                    "name": "Type 2: মধ্যপদ (Middle term) নির্ণয়",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '20-21", "JU '21-22", "GST '21-22"],
                    "qb_question_refs": ["VAR-JnU-P03-Q17", "VAR-DU-P05-Q10"],
                    "core_rule": "$(a + x)^n$ এর মোট পদ সংখ্যা $(n + 1)$ টি। ১. $n$ জোড় হলে: পদ সংখ্যা বিজোড়, ফলে ঠিক ১টি মধ্যপদ থাকে এবং তা হলো $\\left(\\frac{n}{2} + 1\\right)$-তম পদ ($T_{n/2 + 1} = ^nC_{n/2} a^{n/2} x^{n/2}$)। ২. $n$ বিজোড় হলে: পদ সংখ্যা জোড়, ফলে ২টি মধ্যপদ থাকে এবং তারা হলো $\\frac{n+1}{2}$-তম পদ ও $\\left(\\frac{n+1}{2} + 1\\right)$-তম পদ।",
                    "speed_elimination": "ঘাত জোড় ($n=10$) হলে মধ্যপদ ১টি ($10/2 + 1 = 6$-তম পদ); ঘাত বিজোড় ($n=9$) হলে মধ্যপদ ২টি (৫ম ও ৬ষ্ঠ পদ)।"
                }
            ]
        },
        {
            "id": "math_2nd_06",
            "aliases": ["math_conics"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৬",
            "title": "কনিক্স (Conics)",
            "subtitle": "পরাবৃত্ত, উপবৃত্ত, অধিবৃত্তের উপকেন্দ্র, উৎকেন্দ্রিকতা ও নিয়ামক রেখা",
            "total_qb_questions": 510,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m16_t1",
                    "name": "Type 1: পরাবৃত্ত ($y^2 = 4ax$ ও $x^2 = 4ay$) এর শীর্ষ, উপকেন্দ্র ও নিয়ামক",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q21", "VAR-DU-P01-Q15", "VAR-RU-P01-Q10"],
                    "core_rule": "কনিকের সংজ্ঞা $\\frac{SP}{PM} = e$ (পরাবৃত্তে $e = 1$, উপবৃত্তে $e < 1$, অধিবৃত্তে $e > 1$, বৃত্তে $e = 0$, জোড় সরলরেখায় $e = \\infty$)। পরাবৃত্ত $y^2 = 4ax$: শীর্ষ $(0,0)$; উপকেন্দ্র $(a, 0)$; অক্ষের সমীকরণ $y = 0$; নিয়ামক রেখার সমীকরণ $x = -a \\implies x + a = 0$; উপকেন্দ্রিক লম্বের দৈর্ঘ্য $|4a|$; উপকেন্দ্রিক লম্বের সমীকরণ $x = a$। শীর্ষবিন্দু বের করার ৩-সেকেন্ড শর্টকাট: সমীকরণে যে চলকের ওপর বর্গ আছে তার সাপেক্ষে আংশিক অন্তরীকরণ করে শূন্য ধরুন ($\frac{\partial f}{\partial y} = 0$) এবং প্রাপ্ত মান মূল সমীকরণে বসিয়ে অপর স্থানাঙ্ক বের করুন।",
                    "speed_elimination": "শীর্ষবিন্দু বের করতে বর্গের চলকে আংশিক অন্তরীকরণ করে শূন্য বসান (যেমন $y^2 - 4y - 8x + 12 = 0 \\implies 2y - 4 = 0 \\implies y = 2$, সমীকরণে বসালে $x = 1$, শীর্ষ $(1, 2)$)।"
                },
                {
                    "type_id": "math_m16_t2",
                    "name": "Type 2: উপবৃত্তের উৎকেন্দ্রিকতা ($e$) ও অক্ষদ্বয়ের সমীকরণ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 40,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '21-22", "GST '22-23", "MAT '21", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P02-Q18", "VAR-DU-P02-Q13", "VAR-RU-P03-Q11"],
                    "core_rule": "উপবৃত্ত $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$: ১. যখন $a > b$: উৎকেন্দ্রিকতা $e = \\sqrt{1 - \\frac{b^2}{a^2}} = \\sqrt{\\frac{a^2 - b^2}{a^2}}$; উপকেন্দ্র $(\\pm ae, 0)$; বৃহদাক্ষ $2a$ ($x$-অক্ষ বরাবর, $y=0$); ক্ষুদ্রাক্ষ $2b$ ($y$-অক্ষ বরাবর, $x=0$); উপকেন্দ্রিক লম্বের দৈর্ঘ্য $\\frac{2b^2}{a}$; নিয়ামকের সমীকরণ $x = \\pm \\frac{a}{e}$। ২. যখন $b > a$: $e = \\sqrt{1 - \\frac{a^2}{b^2}}$; উপকেন্দ্র $(0, \\pm be)$; উপকেন্দ্রিক লম্ব $\\frac{2a^2}{b}$; নিয়ামক $y = \\pm \\frac{b}{e}$। উপবৃত্তের ওপরিস্থিত যেকোনো বিন্দু $P$ হতে উপকেন্দ্রদ্বয়ের দূরত্বের সমষ্টি বৃহদাক্ষের সমান: $SP + S'P = 2a$ (ধ্রুবক)।",
                    "speed_elimination": "উৎকেন্দ্রিকতা $e = \\sqrt{1 - \\frac{\\text{ছোট সহগ}}{\\text{বড় সহগ}}}$; উপকেন্দ্রদ্বয়ের দূরত্বের যোগফল সর্বদা বৃহদাক্ষের সমান ($2a$)।"
                },
                {
                    "type_id": "math_m16_t3",
                    "name": "Type 3: অধিবৃত্তের উৎকেন্দ্রিকতা ও অসীমতটের সমীকরণ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '20-21", "JU '20-21", "GST '21-22", "BUET '18-19"],
                    "qb_question_refs": ["VAR-JnU-P04-Q15", "VAR-DU-P04-Q12", "VAR-GST-P04-Q11"],
                    "core_rule": "অধিবৃত্ত $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$: উৎকেন্দ্রিকতা $e = \\sqrt{1 + \\frac{b^2}{a^2}} = \\sqrt{\\frac{a^2 + b^2}{a^2}} > 1$; উপকেন্দ্র $(\\pm ae, 0)$; আরড় অক্ষ $2a$, অনুবন্ধী অক্ষ $2b$; উপকেন্দ্রিক লম্বের দৈর্ঘ্য $\\frac{2b^2}{a}$; নিয়ামক $x = \\pm \\frac{a}{e}$। অসীমতটের (Asymptotes) সমীকরণ: $y = \\pm \\frac{b}{a} x \\implies \\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 0$। সমপরাবৃত্ত (Rectangular hyperbola): $a = b \\implies x^2 - y^2 = a^2$ বা $xy = c^2$, এর উৎকেন্দ্রিকতা সর্বদা $e = \\sqrt{2}$ এবং অসীমতটদ্বয় পরস্পর লম্ব। উপকেন্দ্রদ্বয়ের দূরত্বের বিয়োগফল: $|SP - S'P| = 2a$।",
                    "speed_elimination": "সমপরাবৃত্তের (Rectangular hyperbola) উৎকেন্দ্রিকতা ফিক্সড $e = \\sqrt{2}$; অসীমতটের সমীকরণে ধ্রুবকটি ০ হয়।"
                }
            ]
        },
        {
            "id": "math_2nd_07",
            "aliases": ["math_inverse_trig"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৭",
            "title": "বিপরীত ত্রিকোণমিতিক ফাংশন ও সমীকরণ (Inverse Trig & Equations)",
            "subtitle": "ডোমেন-রেঞ্জ, tan^-1 সূত্রাবলী এবং সাধারণ সমাধান (θ=nπ, 2nπ)",
            "total_qb_questions": 470,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "math_m17_t1",
                    "name": "Type 1: বিপরীত ত্রিকোণমিতিক সূত্রাবলী ও যোগফল-বিয়োগফল",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '20-21"],
                    "qb_question_refs": ["VAR-JnU-P01-Q22", "VAR-DU-P01-Q17", "VAR-RU-P02-Q11"],
                    "core_rule": "১. $\\tan^{-1} x + \\tan^{-1} y = \\tan^{-1}\\left(\\frac{x+y}{1-xy}\\right)$ ($xy < 1$); বিয়োগফল: $\\tan^{-1} x - \\tan^{-1} y = \\tan^{-1}\\left(\\frac{x-y}{1+xy}\\right)$। ২. $2\\tan^{-1} x = \\tan^{-1}\\left(\\frac{2x}{1-x^2}\\right) = \\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right) = \\cos^{-1}\\left(\\frac{1-x^2}{1+x^2}\\right)$। ৩. সম্পূরক সূত্র: $\\sin^{-1} x + \\cos^{-1} x = \\frac{\\pi}{2}$, $\\tan^{-1} x + \\cot^{-1} x = \\frac{\\pi}{2}$, $\\sec^{-1} x + \\csc^{-1} x = \\frac{\\pi}{2}$। ৪. ডোমেন ও রেঞ্জ: $\\sin^{-1} x$ এর ডোমেন $[-1, 1]$, মুখ্য মান সীমা $[-\\pi/2, \\pi/2]$; $\\cos^{-1} x$ এর ডোমেন $[-1, 1]$, মুখ্য মান $[0, \\pi]$; $\\tan^{-1} x$ এর ডোমেন $\\mathbb{R}$, মুখ্য মান $(-\\pi/2, \\pi/2)$।",
                    "speed_elimination": "$\\tan^{-1}(1/2) + \\tan^{-1}(1/3) = \\tan^{-1}\\left(\\frac{5/6}{5/6}\\right) = \\tan^{-1}(1) = \\frac{\\pi}{4}$ (বারংবার আসা রেজাল্ট)।"
                },
                {
                    "type_id": "math_m17_t2",
                    "name": "Type 2: ত্রিকোণমিতিক সমীকরণের সাধারণ সমাধান",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '22-23", "DU '19-20", "RU '21-22", "JU '21-22", "GST '21-22", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q19", "VAR-DU-P03-Q14", "VAR-GST-P02-Q14"],
                    "core_rule": "সাধারণ সমাধানের সূত্রাবলী ($n \\in \\mathbb{Z}$): ১. $\\sin\\theta = 0 \\implies \\theta = n\\pi$; $\\cos\\theta = 0 \\implies \\theta = (2n+1)\\frac{\\pi}{2}$; $\\tan\\theta = 0 \\implies \\theta = n\\pi$। ২. $\\sin\\theta = 1 \\implies \\theta = (4n+1)\\frac{\\pi}{2}$; $\\sin\\theta = -1 \\implies \\theta = (4n-1)\\frac{\\pi}{2}$। ৩. $\\cos\\theta = 1 \\implies \\theta = 2n\\pi$; $\\cos\\theta = -1 \\implies \\theta = (2n+1)\\pi$। ৪. $\\sin\\theta = \\sin\\alpha \\implies \\theta = n\\pi + (-1)^n \\alpha$; ৫. $\\cos\\theta = \\cos\\alpha \\implies \\theta = 2n\\pi \\pm \\alpha$; ৬. $\\tan\\theta = \\tan\\alpha \\implies \\theta = n\\pi + \\alpha$।",
                    "speed_elimination": "অপশন টেস্ট ট্রিক: $n = 0$ বা $n = 1$ বসিয়ে যে কোণটি সমীকরণকে সিদ্ধ করে তা অপশন দেখে সেকেন্ডে বের করুন।"
                }
            ]
        },
        {
            "id": "math_2nd_08",
            "aliases": ["math_statics"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৮",
            "title": "স্থিতিবিদ্যা (Statics)",
            "subtitle": "লামির উপপাদ্য, বলের সামান্তরিক সূত্র, সদৃশ-অসদৃশ সমান্তরাল বল ও ভারকেন্দ্র",
            "total_qb_questions": 440,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "math_m18_t1",
                    "name": "Type 1: লামির উপপাদ্য ও তিনটি বলের সাম্যাবস্থা",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P02-Q19", "VAR-DU-P02-Q14", "VAR-RU-P01-Q12"],
                    "core_rule": "লামির উপপাদ্য (Lami's Theorem): তিনটি সমতলীয় বল কোনো বিন্দুতে ক্রিয়া করে সাম্যাবস্থা সৃষ্টি করলে প্রতিটি বল অপর দুটি বলের মধ্যবর্তী কোণের সাইনের সমানুপাতিক: $\\frac{P}{\\sin\\alpha} = \\frac{Q}{\\sin\\beta} = \\frac{R}{\\sin\\gamma}$ (যেখানে $\\alpha$ হলো $Q$ ও $R$ এর মধ্যবর্তী কোণ ইত্যাদি)। বল ত্রিভুজ সূত্র: তিনটি বল কোনো ত্রিভুজের একই ক্রমে গৃহীত তিনটি বাহু দ্বারা মানে ও দিকে সূচিত হলে তারা সাম্যাবস্থায় থাকে: $\\frac{P}{BC} = \\frac{Q}{CA} = \\frac{R}{AB}$। তিনটি সমান বল পরস্পর $120^\\circ$ কোণে ক্রিয়া করলে তারা সাম্যাবস্থায় থাকে।",
                    "speed_elimination": "তিনটি সমান বল সাম্যাবস্থায় থাকলে তাদের প্রত্যেকের মধ্যবর্তী কোণ ঠিক $120^\\circ$।"
                },
                {
                    "type_id": "math_m18_t2",
                    "name": "Type 2: সদৃশ ও অসদৃশ সমান্তরাল বল এবং লব্ধির ক্রিয়াবিন্দু",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 34,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '20-21", "JU '20-21", "GST '21-22", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P04-Q17", "VAR-DU-P04-Q14"],
                    "core_rule": "১. সদৃশ সমান্তরাল বল ($P, Q$ একই দিকে $A, B$ বিন্দুতে ক্রিয়াশীল): লব্ধি $R = P + Q$; ক্রিয়াবিন্দু $C$ রেখাংশের অন্তর্বিভক্তকারী এবং $P \\times AC = Q \\times BC$। ২. অসদৃশ সমান্তরাল বল ($P > Q$ বিপরীতমুখী): লব্ধি $R = P - Q$; ক্রিয়াবিন্দু বহির্বিভক্তকারী (বৃহত্তর বলের দিকে) এবং $P \\times AC = Q \\times BC$। যুগল বা দ্বন্দ্ব (Couple): সমান ও বিপরীতমুখী দুটি সমান্তরাল বল $P$ এর মধ্যবর্তী লম্ব দূরত্ব $d$ হলে যুগলের ভ্রামক $M = P \\times d$।",
                    "speed_elimination": "সদৃশ বলে লব্ধি উভয়ের যোগফল এবং এদের মাঝখানে থাকে; অসদৃশ বলে লব্ধি বিয়োগফল এবং বৃহত্তর বলের বাইরে থাকে।"
                }
            ]
        },
        {
            "id": "math_2nd_09",
            "aliases": ["math_dynamics_plane"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৯",
            "title": "সমতলে বস্তু কণার গতি (Dynamics in a Plane)",
            "subtitle": "উল্লম্ব তলে গতি, প্রক্ষেপক, দুটি ট্রেনের ক্রসিং ও আপেক্ষিক বেগ",
            "total_qb_questions": 430,
            "high_yield_score": 97,
            "mega_types": [
                {
                    "type_id": "math_m19_t1",
                    "name": "Type 1: সরলরৈখিক সমত্বরণ ও ট্রেনের ক্রসিং সমস্যা",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '22-23", "DU '21-22", "RU '21-22", "JU '21-22", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P01-Q23", "VAR-DU-P03-Q13"],
                    "core_rule": "গতিসূত্র: $v = u + at$, $s = ut + \\frac{1}{2}at^2$, $v^2 = u^2 + 2as$, $s_t = u + \\frac{1}{2}a(2t - 1)$ ($t$-তম সেকেন্ডে সরণ)। ট্রেনের সমস্যা: দুটি ট্রেন $L_1, L_2$ দৈর্ঘ্যের এবং তাদের বেগ $v_1, v_2$। একে অপরকে সম্পূর্ণ অতিক্রম করতে অতিক্রান্ত মোট দূরত্ব $D = L_1 + L_2$। ১. বিপরীত দিকে চললে আপেক্ষিক বেগ $v_{rel} = v_1 + v_2$, অতিক্রমের সময় $t = \\frac{L_1 + L_2}{v_1 + v_2}$। ২. একই দিকে চললে আপেক্ষিক বেগ $v_{rel} = |v_1 - v_2|$, সময় $t = \\frac{L_1 + L_2}{|v_1 - v_2|}$।",
                    "speed_elimination": "বিপরীত দিকে চললে বেগ যোগ হবে ($v_1+v_2$); একই দিকে চললে বেগ বিয়োগ হবে ($v_1-v_2$); মোট দূরত্ব সর্বদা দৈর্ঘ্যের যোগফল ($L_1+L_2$)।"
                },
                {
                    "type_id": "math_m19_t2",
                    "name": "Type 2: খাড়া উপরের দিকে নিক্ষিপ্ত বস্তু ও উচ্চতার অনুপাত",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '22-23", "GST '21-22", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q18", "VAR-DU-P05-Q12"],
                    "core_rule": "খাড়া নিক্ষিপ্ত বস্তু ($u$ আদিবেগ): সর্বোচ্চ উচ্চতা $H = \\frac{u^2}{2g}$; মোট উত্থান-পতন সময় $T = \\frac{2u}{g}$। ভূপৃষ্ঠ হতে $h$ উচ্চতায় উঠার সময় $t_1$ এবং সেখান থেকে পুনরায় ভূপৃষ্ঠে ফিরে আসার সময় $t_2$ হলে: ১. মোট সময় $t_1 + t_2 = \\frac{2u}{g}$; ২. উচ্চতা $h = \\frac{1}{2}g t_1 t_2$; ৩. আদিবেগ $u = \\frac{1}{2}g(t_1 + t_2)$। সর্বোচ্চ উচ্চতার এক-তৃতীয়াংশে বেগ $\\sqrt{\\frac{2}{3}}u$।",
                    "speed_elimination": "$h$ উচ্চতায় যেতে ও ফিরে আসতে সময় $t_1, t_2$ লাগলে উচ্চতা সরাসরি $h = \\frac{1}{2}g t_1 t_2$।"
                }
            ]
        },
        {
            "id": "math_2nd_10",
            "aliases": ["math_probability"],
            "subject": "Higher Math",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ১০",
            "title": "বিস্তার পরিমাপ ও সম্ভাবনা (Dispersion & Probability)",
            "subtitle": "ভেদাঙ্ক, পরিমিত ব্যবধান, বিভেদাঙ্ক (CV), ছক্কা-মুদ্রা ও তাসের সম্ভাবনা",
            "total_qb_questions": 410,
            "high_yield_score": 97,
            "mega_types": [
                {
                    "type_id": "math_m20_t1",
                    "name": "Type 1: বিস্তার পরিমাপ (ভেদাঙ্ক $\sigma^2$, পরিমিত ব্যবধান $\sigma$ ও বিভেদাঙ্ক CV)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 34,
                    "past_tags": ["DU '22-23", "DU '21-22", "RU '21-22", "JU '22-23", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P02-Q20", "VAR-DU-P01-Q18", "VAR-RU-P03-Q13"],
                    "core_rule": "১. পরিমিত ব্যবধান (Standard Deviation): $\\sigma = \\sqrt{\\frac{\\Sigma (x_i - \\bar{x})^2}{N}} = \\sqrt{\\frac{\\Sigma x_i^2}{N} - \\bar{x}^2}$। ২. ভেদাঙ্ক (Variance): $\\sigma^2$ (পরিমিত ব্যবধানের বর্গ)। ৩. বিভেদাঙ্ক (Coefficient of Variation): $CV = \\frac{\\sigma}{\\bar{x}} \\times 100\\%$ ($CV$ যার কম সে তত বেশি সুষম ও নির্ভরযোগ্য)। মূল ও মাপনী পরিবর্তন: চলক $y = a + bx$ হলে: $\\bar{y} = a + b\\bar{x}$; কিন্তু পরিমিত ব্যবধান মূল হতে স্বাধীন কেবল মাপনীর ওপর নির্ভরশীল: $\\sigma_y = |b| \\sigma_x$ এবং ভেদাঙ্ক $\\sigma_y^2 = b^2 \\sigma_x^2$। প্রথম $n$ সংখ্যক স্বাভাবিক সংখ্যার ভেদাঙ্ক $= \\frac{n^2 - 1}{12}$।",
                    "speed_elimination": "প্রতিটি উপাত্তের সাথে কোনো ধ্রুবক যোগ বা বিয়োগ করলে পরিমিত ব্যবধান ও ভেদাঙ্ক অপরিবর্তিত থাকে; কিন্তু $b$ গুণ করলে পরিমিত ব্যবধান $|b|$ গুণ ও ভেদাঙ্ক $b^2$ গুণ হয়।"
                },
                {
                    "type_id": "math_m20_t2",
                    "name": "Type 2: ক্লাসিক্যাল সম্ভাবনা (মুদ্রা, ছক্কা ও ৫২ তাসের প্যাকেট)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '22-23", "JU '21-22", "GST '21-22", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P04-Q18", "VAR-DU-P03-Q15", "MAD-MAT-Q24"],
                    "core_rule": "সম্ভাবনা $P(A) = \\frac{n(A)}{n(S)}$ ($0 \\le P(A) \\le 1$)। বর্জনশীল ঘটনা হলে $P(A \\cup B) = P(A) + P(B)$; অবর্জনশীল হলে $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$। স্বাধীন ঘটনা (Independent events): $P(A \\cap B) = P(A) \\times P(B)$। ১. ছক্কার সমস্যা: দুটি ছক্কা নিক্ষেপে মোট নমুনা বিন্দু $6^2 = 36$; সমষ্টি ৭ হওয়ার সম্ভাবনা $\\frac{6}{36} = \\frac{1}{6}$; সমষ্টি ৮ হওয়ার সম্ভাবনা $\\frac{5}{36}$। ২. ৫২ তাসের প্যাকেট: ৪টি টেক্কা (Ace), ১২টি ফেস কার্ড (রাজা ৪, রানী ৪, গোলাম ৪), ২৬টি লাল (হরতনের ১৩, রুইতনের ১৩) ও ২৬টি কালো (ইস্কাপনের ১৩, চিড়িতনের ১৩)। ৩. লিপ ইয়ার (Leap year): ৫৩টি শুক্রবার বা রবিবার থাকার সম্ভাবনা $\\frac{2}{7}$; সাধারণ বছরে ৫৩টি শুক্রবার থাকার সম্ভাবনা $\\frac{1}{7}$।",
                    "speed_elimination": "লিপ ইয়ারে ৫৩টি কোনো নির্দিষ্ট দিন থাকার সম্ভাবনা সর্বদা $\\frac{2}{7}$; সাধারণ বছরে $\\frac{1}{7}$।"
                }
            ]
        }
    ]
    return chapters
