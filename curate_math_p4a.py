#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_math_p4a.py: Chapters math_2nd_06 & math_2nd_07
"""

def get_math_2nd_06():
    """কণিক (20 MCQs)"""
    return {
        "chapter_id": "math_2nd_06",
        "chapter_title": "কণিক",
        "subject": "Higher Mathematics",
        "paper": "2nd",
        "chapter_no": 6,
        "predictors": [
            {
                "id": "pred_math_2nd_06_01",
                "stem": "$y^2 = 12x$ পরাবৃত্তের উপকেন্দ্রের স্থানাঙ্ক এবং উপকেন্দ্রিক লম্বের দৈর্ঘ্য যথাক্রমে কত?",
                "options": ["$(3, 0)$ এবং $12$", "$(0, 3)$ এবং $12$", "$(3, 0)$ এবং $6$", "$(6, 0)$ এবং $12$"],
                "answer": "A",
                "type_ref": "পরাবৃত্তের উপকেন্দ্র ও লম্বের দৈর্ঘ্য",
                "trap_alert": "আদর্শ সমীকরণ $y^2 = 4ax$ এর সাথে তুলনা করতে হবে। $4a = 12 \implies a = 3$।",
                "speed_hack": "$4a = 12 \implies a = 3$, উপকেন্দ্র $(a, 0) = (3, 0)$ এবং উপকেন্দ্রিক লম্বের দৈর্ঘ্য $4a = 12$।",
                "explanation": "$y^2 = 4(3)x$। এখানে $a = 3$। উপকেন্দ্র $S = (a, 0) = (3, 0)$ এবং উপকেন্দ্রিক লম্বের দৈর্ঘ্য $= 4a = 12$ একক।"
            },
            {
                "id": "pred_math_2nd_06_02",
                "stem": "কোনো কণিকের উৎকেন্দ্রিকতা $e = 1$ হলে কণিকটি কী নির্দেশ করে?",
                "options": ["পরাবৃত্ত (Parabola)", "উপবৃত্ত (Ellipse)", "অধিবৃত্ত (Hyperbola)", "বৃত্ত (Circle)"],
                "answer": "A",
                "type_ref": "উৎকেন্দ্রিকতা ও কণিকের প্রকারভেদ",
                "trap_alert": "$e = 0$ বৃত্ত, $0 < e < 1$ উপবৃত্ত, $e = 1$ পরাবৃত্ত, $e > 1$ অধিবৃত্ত।",
                "speed_hack": "$e=1 \implies$ Parabola।",
                "explanation": "কণিকের সংজ্ঞা অনুসারে ফোকাস ও দিকাক্ষ থেকে দূরত্বের অনুপাতকে উৎকেন্দ্রিকতা $e$ বলে। $e = 1$ হলে কণিকটি একটি পরাবৃত্ত।"
            },
            {
                "id": "pred_math_2nd_06_03",
                "stem": "$\\frac{x^2}{25} + \\frac{y^2}{16} = 1$ উপবৃত্তটির উৎকেন্দ্রিকতা (Eccentricity) কত?",
                "options": ["$\\frac{3}{5}$", "$\\frac{4}{5}$", "$\\frac{9}{25}$", "$\\frac{\\sqrt{7}}{5}$"],
                "answer": "A",
                "type_ref": "উপবৃত্তের উৎকেন্দ্রিকতা",
                "trap_alert": "এখানে $a^2 = 25 > b^2 = 16$, তাই সূত্র $e = \\sqrt{1 - b^2/a^2}$।",
                "speed_hack": "$e = \\sqrt{1 - 16/25} = 3/5$।",
                "explanation": "$a = 5, b = 4$ ($a > b$)। $e = \\sqrt{1 - b^2/a^2} = \\sqrt{1 - 16/25} = 3/5$।"
            },
            {
                "id": "pred_math_2nd_06_04",
                "stem": "$\\frac{x^2}{16} - \\frac{y^2}{9} = 1$ অধিবৃত্তটির উৎকেন্দ্রিকতা কত?",
                "options": ["$\\frac{5}{4}$", "$\\frac{5}{3}$", "$\\frac{\\sqrt{7}}{4}$", "$\\frac{25}{16}$"],
                "answer": "A",
                "type_ref": "অধিবৃত্তের উৎকেন্দ্রিকতা",
                "trap_alert": "অধিবৃত্তে মাঝে যোগ চিহ্ন: $e = \\sqrt{1 + b^2/a^2}$। $e > 1$ হতে হবে।",
                "speed_hack": "$e = \\sqrt{1 + 9/16} = 5/4$।",
                "explanation": "$a^2 = 16, b^2 = 9$। $e = \\sqrt{1 + 9/16} = \\sqrt{25/16} = 5/4$।"
            },
            {
                "id": "pred_math_2nd_06_05",
                "stem": "$x^2 = -8y$ পরাবৃত্তের নিয়ামক রেখার (Directrix) সমীকরণ কোনটি?",
                "options": ["$y = 2$", "$y = -2$", "$x = 2$", "$x = -2$"],
                "answer": "A",
                "type_ref": "পরাবৃত্তের নিয়ামক রেখা",
                "trap_alert": "$x^2 = 4ay$ আকারের সমীকরণে নিয়ামকের সমীকরণ $y = -a$। এখানে $4a = -8 \implies a = -2$।",
                "speed_hack": "$a = -2 \implies y = -a = 2$।",
                "explanation": "$x^2 = 4(-2)y$। নিয়ামক রেখার সমীকরণ $y = -a = -(-2) = 2$।"
            },
            {
                "id": "pred_math_2nd_06_06",
                "stem": "$\\frac{x^2}{9} + \\frac{y^2}{4} = 1$ উপবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?",
                "options": ["$\\frac{8}{3}$", "$\\frac{4}{3}$", "$\\frac{16}{9}$", "$4$"],
                "answer": "A",
                "type_ref": "উপবৃত্তের উপকেন্দ্রিক লম্ব",
                "trap_alert": "$a > b$ হলে উপকেন্দ্রিক লম্বের দৈর্ঘ্য $\\frac{2b^2}{a}$।",
                "speed_hack": "দৈর্ঘ্য $= \\frac{2(4)}{3} = \\frac{8}{3}$।",
                "explanation": "$a = 3, b = 2$ ($a > b$)। উপকেন্দ্রিক লম্বের দৈর্ঘ্য $= \\frac{2b^2}{a} = \\frac{2 \\times 4}{3} = \\frac{8}{3}$ একক।"
            },
            {
                "id": "pred_math_2nd_06_07",
                "stem": "$y = mx + c$ সরলরেখাটি $y^2 = 4ax$ পরাবৃত্তের স্পর্শক হওয়ার শর্ত কোনটি?",
                "options": ["$c = \\frac{a}{m}$", "$c = am$", "$c = -am^2$", "$c^2 = a^2(1+m^2)$"],
                "answer": "A",
                "type_ref": "পরাবৃত্তের স্পর্শকের শর্ত",
                "trap_alert": "বৃত্তের ক্ষেত্রে $c = \\pm a\\sqrt{1+m^2}$, কিন্তু পরাবৃত্তে $c = a/m$।",
                "speed_hack": "পরাবৃত্তের স্পর্শকের শর্ত: $c = a/m$।",
                "explanation": "দ্বিঘাত সমীকরণের পৃথায়ক শূন্য বসালে পাওয়া যায় $c = \\frac{a}{m}$।"
            },
            {
                "id": "pred_math_2nd_06_08",
                "stem": "যদি একটি অধিবৃত্ত সমাক্ষ (Rectangular Hyperbola) হয়, তবে এর উৎকেন্দ্রিকতা কত?",
                "options": ["$\\sqrt{2}$", "$2$", "$\\frac{1}{\\sqrt{2}}$", "$\\sqrt{3}$"],
                "answer": "A",
                "type_ref": "সমাক্ষ অধিবৃত্তের উৎকেন্দ্রিকতা",
                "trap_alert": "সমাক্ষ অধিবৃত্তে $a = b$ হয় এবং অসীম তটদ্বয় পরস্পর লম্ব হয়।",
                "speed_hack": "Rectangular Hyperbola এর $e = \\sqrt{2}$ ধ্রুবক।",
                "explanation": "$a = b$ হলে উৎকেন্দ্রিকতা $e = \\sqrt{1 + b^2/a^2} = \\sqrt{1 + 1} = \\sqrt{2}$।"
            },
            {
                "id": "pred_math_2nd_06_09",
                "stem": "$(y - 2)^2 = 8(x + 1)$ পরাবৃত্তের শীর্ষবিন্দুর স্থানাঙ্ক কোনটি?",
                "options": ["$(-1, 2)$", "$(1, -2)$", "$(2, -1)$", "$(-2, 1)$"],
                "answer": "A",
                "type_ref": "স্থানান্তরিত পরাবৃত্তের শীর্ষবিন্দু",
                "trap_alert": "ভুজ প্রথমে: $x + 1 = 0 \implies x = -1$, কোটি $y - 2 = 0 \implies y = 2$।",
                "speed_hack": "শীর্ষ: $(-1, 2)$।",
                "explanation": "$X = x + 1 = 0 \implies x = -1$ এবং $Y = y - 2 = 0 \implies y = 2$। শীর্ষ $(-1, 2)$।"
            },
            {
                "id": "pred_math_2nd_06_10",
                "stem": "$\\frac{x^2}{16} + \\frac{y^2}{25} = 1$ উপবৃত্তটির ফোকাসদ্বয়ের মধ্যবর্তী দূরত্ব কত?",
                "options": ["$6$", "$8$", "$10$", "$3$"],
                "answer": "A",
                "type_ref": "উপকেন্দ্রদ্বয়ের মধ্যবর্তী দূরত্ব",
                "trap_alert": "এখানে $b^2 = 25 > a^2 = 16$, ফলে ফোকাস $y$-অক্ষে এবং দূরত্ব $2be$।",
                "speed_hack": "$b = 5, e = 3/5 \implies 2be = 2(5)(3/5) = 6$।",
                "explanation": "$b > a$ হওয়ায় $e = \\sqrt{1 - 16/25} = 3/5$। দূরত্ব $= 2be = 2 \\times 5 \\times 3/5 = 6$ একক।"
            },
            {
                "id": "pred_math_2nd_06_11",
                "stem": "$y^2 = 4ax$ পরাবৃত্তের ওপর অবস্থিত $(x_1, y_1)$ বিন্দুর ফোকাল দূরত্ব কত?",
                "options": ["$x_1 + a$", "$x_1 - a$", "$\\sqrt{x_1^2 + y_1^2}$", "$2a + x_1$"],
                "answer": "A",
                "type_ref": "পরাবৃত্তের ফোকাল দূরত্ব সূত্র",
                "trap_alert": "ফোকাস দূরত্ব $=$ নিয়ামক হতে লম্ব দূরত্ব $= x_1 + a$।",
                "speed_hack": "$SP = PM = x_1 + a$।",
                "explanation": "পরাবৃত্তের সংজ্ঞানুসারে উপকেন্দ্রিক দূরত্ব নিয়ামকরেখা হতে লম্ব দূরত্বের সমান, যা $x_1 + a$।"
            },
            {
                "id": "pred_math_2nd_06_12",
                "stem": "$\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$ অধিবৃত্তের নিয়ামকরেখাদ্বয়ের মধ্যবর্তী দূরত্ব কত?",
                "options": ["$\\frac{2a}{e}$", "$2ae$", "$\\frac{2b}{e}$", "$\\frac{a}{e}$"],
                "answer": "A",
                "type_ref": "নিয়ামকরেখার দূরত্ব",
                "trap_alert": "নিয়ামক রেখাদ্বয় $x = \\pm a/e$, এদের দূরত্ব $2a/e$।",
                "speed_hack": "দূরত্ব $= 2a/e$।",
                "explanation": "নিয়ামকদ্বয়ের সমীকরণ $x = a/e$ এবং $x = -a/e$। মধ্যবর্তী দূরত্ব $= 2a/e$।"
            },
            {
                "id": "pred_math_2nd_06_13",
                "stem": "$2x^2 + 3y^2 - 4x + 6y - 1 = 0$ সমীকরণটি কোন ধরনের কণিক নির্দেশ করে?",
                "options": ["উপবৃত্ত (Ellipse)", "অধিবৃত্ত (Hyperbola)", "পরাবৃত্ত (Parabola)", "বৃত্ত (Circle)"],
                "answer": "A",
                "type_ref": "সাধারণ সমীকরণ হতে কণিক শনাক্তকরণ",
                "trap_alert": "$x^2$ ও $y^2$ এর সহগ উভয়ই ধনাত্মক কিন্তু অসমান ($2 \\ne 3$), এবং $xy$ পদ নেই।",
                "speed_hack": "$a, b > 0, a \\ne b \implies$ উপবৃত্ত।",
                "explanation": "সহগদ্বয় সমচিহ্নবিশিষ্ট কিন্তু অসমান ($2 \\ne 3$) হওয়ায় এটি একটি উপবৃত্ত।"
            },
            {
                "id": "pred_math_2nd_06_14",
                "stem": "$y^2 = 8x$ পরাবৃত্তের শীর্ষবিন্দুতে স্পর্শকের সমীকরণ কোনটি?",
                "options": ["$x = 0$", "$y = 0$", "$x = 2$", "$x = -2$"],
                "answer": "A",
                "type_ref": "শীর্ষবিন্দুতে স্পর্শক",
                "trap_alert": "$y^2 = 4ax$ এর শীর্ষবিন্দুতে স্পর্শক হলো $y$-অক্ষ ($x = 0$)।",
                "speed_hack": "শীর্ষে স্পর্শক $= y$-অক্ষ $\implies x = 0$।",
                "explanation": "পরাবৃত্তের শীর্ষবিন্দু $(0, 0)$ তে অঙ্কিত স্পর্শক হলো $y$-অক্ষ, যার সমীকরণ $x = 0$।"
            },
            {
                "id": "pred_math_2nd_06_15",
                "stem": "$\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ উপবৃত্তের ক্ষেত্রফল কত বর্গ একক?",
                "options": ["$\\pi ab$", "$2\\pi ab$", "$\\frac{4}{3}\\pi ab$", "$\\pi(a^2 + b^2)$"],
                "answer": "A",
                "type_ref": "উপবৃত্তের ক্ষেত্রফল সূত্র",
                "trap_alert": "বৃত্তের $\\pi r^2$ এর মতো উপবৃত্তের ক্ষেত্রফল $\\pi ab$।",
                "speed_hack": "ক্ষেত্রফল $= \\pi ab$।",
                "explanation": "যোগজীকরণের মাধ্যমে আদর্শ উপবৃত্তের আবদ্ধ ক্ষেত্রফল $= \\pi ab$ বর্গ একক।"
            },
            {
                "id": "pred_math_2nd_06_16",
                "stem": "অধিবৃত্ত $x^2 - y^2 = 16$ এর ফোকাসদ্বয়ের স্থানাঙ্ক কত?",
                "options": ["$(\\pm 4\\sqrt{2}, 0)$", "$(0, \\pm 4\\sqrt{2})$", "$(\\pm 4, 0)$", "$(\\pm 8, 0)$"],
                "answer": "A",
                "type_ref": "সমাক্ষ অধিবৃত্তের ফোকাস",
                "trap_alert": "সমাক্ষ অধিবৃত্তে $a = 4$ এবং $e = \\sqrt{2}$। ফোকাস $(\\pm ae, 0)$।",
                "speed_hack": "$ae = 4\\sqrt{2} \implies (\\pm 4\\sqrt{2}, 0)$।",
                "explanation": "$a = 4, e = \\sqrt{2}$। ফোকাসদ্বয়ের স্থানাঙ্ক $(\\pm ae, 0) = (\\pm 4\\sqrt{2}, 0)$।"
            },
            {
                "id": "pred_math_2nd_06_17",
                "stem": "$x^2 = 16y$ পরাবৃত্তের উপকেন্দ্রিক লম্বের প্রান্তবিন্দুদ্বয়ের স্থানাঙ্ক কোনটি?",
                "options": ["$(8, 4)$ এবং $(-8, 4)$", "$(4, 8)$ এবং $(4, -8)$", "$(4, 2)$ এবং $(-4, 2)$", "$(16, 4)$ এবং $(-16, 4)$"],
                "answer": "A",
                "type_ref": "উপকেন্দ্রিক লম্বের প্রান্তবিন্দু",
                "trap_alert": "$x^2 = 4ay$ তে উপকেন্দ্র $(0, 4)$। $y = 4$ বসালে $x = \\pm 8$।",
                "speed_hack": "$x^2 = 64 \implies x = \\pm 8 \\implies (\\pm 8, 4)$।",
                "explanation": "$a = 4$। $y = 4$ বসালে $x^2 = 64 \implies x = \\pm 8$। প্রান্তবিন্দু $(8, 4)$ এবং $(-8, 4)$।"
            },
            {
                "id": "pred_math_2nd_06_18",
                "stem": "$\\frac{x^2}{16} - \\frac{y^2}{9} = 1$ অধিবৃত্তের অনুবন্ধী অক্ষের দৈর্ঘ্য কত?",
                "options": ["$6$", "$8$", "$3$", "$4$"],
                "answer": "A",
                "type_ref": "অধিবৃত্তের অক্ষের দৈর্ঘ্য",
                "trap_alert": "আড় অক্ষের দৈর্ঘ্য $2a = 8$, অনুবন্ধী অক্ষের দৈর্ঘ্য $2b = 6$।",
                "speed_hack": "$2b = 2(3) = 6$।",
                "explanation": "$b = 3$। অনুবন্ধী অক্ষের দৈর্ঘ্য $= 2b = 2 \\times 3 = 6$ একক।"
            },
            {
                "id": "pred_math_2nd_06_19",
                "stem": "যদি কোনো উপবৃত্তের বৃহৎ অক্ষ ক্ষুদ্র অক্ষের দ্বিগুণ হয়, তবে তার উৎকেন্দ্রিকতা $e$ কত?",
                "options": ["$\\frac{\\sqrt{3}}{2}$", "$\\frac{1}{2}$", "$\\frac{1}{\\sqrt{2}}$", "$\\frac{\\sqrt{5}}{3}$"],
                "answer": "A",
                "type_ref": "অক্ষের অনুপাত হতে উৎকেন্দ্রিকতা",
                "trap_alert": "$a = 2b \implies b/a = 1/2$। $e = \\sqrt{1 - 1/4} = \\sqrt{3}/2$।",
                "speed_hack": "$e = \\sqrt{1 - (1/2)^2} = \\frac{\\sqrt{3}}{2}$।",
                "explanation": "$a = 2b$। $e = \\sqrt{1 - (b/a)^2} = \\sqrt{1 - 1/4} = \\frac{\\sqrt{3}}{2}$।"
            },
            {
                "id": "pred_math_2nd_06_20",
                "stem": "$y^2 - 4y - 4x + 8 = 0$ পরাবৃত্তটির অক্ষের সমীকরণ কোনটি?",
                "options": ["$y = 2$", "$y = -2$", "$x = 1$", "$x = 2$"],
                "answer": "A",
                "type_ref": "পরাবৃত্তের অক্ষের সমীকরণ",
                "trap_alert": "$(y-2)^2 = 4(x-1)$। অক্ষের সমীকরণ $y - 2 = 0$।",
                "speed_hack": "অক্ষ: $\\frac{d}{dy}(y^2 - 4y) = 2y - 4 = 0 \implies y = 2$।",
                "explanation": "$(y - 2)^2 = 4(x - 1)$। অক্ষের সমীকরণ $y - 2 = 0 \implies y = 2$।"
            }
        ]
    }

def get_math_2nd_07():
    """বিপরীত ত্রিকোণমিতিক ফাংশন ও ত্রিকোণমিতিক সমীকরণ (20 MCQs)"""
    return {
        "chapter_id": "math_2nd_07",
        "chapter_title": "বিপরীত ত্রিকোণমিতিক ফাংশন ও ত্রিকোণমিতিক সমীকরণ",
        "subject": "Higher Mathematics",
        "paper": "2nd",
        "chapter_no": 7,
        "predictors": [
            {
                "id": "pred_math_2nd_07_01",
                "stem": "$\\tan^{-1}\\left(\\frac{1}{2}\\right) + \\tan^{-1}\\left(\\frac{1}{3}\\right)$ এর মান কত?",
                "options": ["$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$", "$\\frac{\\pi}{3}$", "$\\frac{\\pi}{6}$"],
                "answer": "A",
                "type_ref": "বিপরীত বৃত্তীয় যোগফল সূত্র",
                "trap_alert": "$xy = 1/6 < 1$, তাই সরাসরি $\\tan^{-1}\\frac{x+y}{1-xy}$ প্রযোজ্য।",
                "speed_hack": "$\\frac{1/2+1/3}{1-1/6} = 1 \implies \\tan^{-1}(1) = \\frac{\\pi}{4}$।",
                "explanation": "$\\tan^{-1}\\left(\\frac{1/2+1/3}{1-1/6}\\right) = \\tan^{-1}(1) = \\frac{\\pi}{4}$।"
            },
            {
                "id": "pred_math_2nd_07_02",
                "stem": "$\\sin^{-1}x + \\cos^{-1}x$ এর মান কত (যেখানে $-1 \\le x \\le 1$)?",
                "options": ["$\\frac{\\pi}{2}$", "$\\pi$", "$0$", "$\\frac{\\pi}{4}$"],
                "answer": "A",
                "type_ref": "পূরক কোণের বিপরীত ত্রিকোণমিতিক অভেদ",
                "trap_alert": "এটি একটি সার্বজনীন মৌলিক অভেদ।",
                "speed_hack": "মান সর্বদা $\\frac{\\pi}{2}$।",
                "explanation": "মৌলিক অভেদ অনুসারে সকল $x \\in [-1, 1]$ এর জন্য $\\sin^{-1}x + \\cos^{-1}x = \\frac{\\pi}{2}$।"
            },
            {
                "id": "pred_math_2nd_07_03",
                "stem": "$\\sin\\theta = 0$ সমীকরণের সাধারণ সমাধান কোনটি?",
                "options": ["$\\theta = n\\pi, n \\in \\mathbb{Z}$", "$\\theta = (2n+1)\\frac{\\pi}{2}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi, n \\in \\mathbb{Z}$", "$\\theta = n\\pi + (-1)^n \\frac{\\pi}{2}$"],
                "answer": "A",
                "type_ref": "ত্রিকোণমিতিক সাধারণ সমাধান",
                "trap_alert": "$\\sin\\theta = 0 \implies \\theta = n\\pi$, কিন্তু $\\cos\\theta = 0 \implies \\theta = (2n+1)\\pi/2$।",
                "speed_hack": "$\\sin\\theta = 0 \implies \\theta = n\\pi$।",
                "explanation": "সাইন অপেক্ষকের শূন্যমানসমূহ $x$-অক্ষের পূর্ণসংখ্যক পাই-তে অবস্থান করে: $\\theta = n\\pi$।"
            },
            {
                "id": "pred_math_2nd_07_04",
                "stem": "$\\cos\\theta = -\\frac{1}{2}$ সমীকরণের সাধারণ সমাধান কোনটি?",
                "options": ["$\\theta = 2n\\pi \\pm \\frac{2\\pi}{3}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi \\pm \\frac{\\pi}{3}, n \\in \\mathbb{Z}$", "$\\theta = n\\pi \\pm \\frac{2\\pi}{3}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi \\pm \\frac{5\\pi}{6}, n \\in \\mathbb{Z}$"],
                "answer": "A",
                "type_ref": "কস সমীকরণের সাধারণ সমাধান",
                "trap_alert": "$\\cos(2\\pi/3) = -1/2$ (২য় চতুর্ভাগ)।",
                "speed_hack": "$\\theta = 2n\\pi \\pm \\frac{2\\pi}{3}$।",
                "explanation": "$\\cos\\theta = \\cos(2\\pi/3) \implies \\theta = 2n\\pi \\pm \\frac{2\\pi}{3}, n \\in \\mathbb{Z}$।"
            },
            {
                "id": "pred_math_2nd_07_05",
                "stem": "$4(\\sin^{-1}\\frac{1}{\\sqrt{2}} + \\cos^{-1}\\frac{1}{2})$ এর মান কত?",
                "options": ["$\\frac{7\\pi}{3}$", "$\\frac{5\\pi}{3}$", "$2\\pi$", "$\\frac{8\\pi}{3}$"],
                "answer": "A",
                "type_ref": "মুখ্য মানের সরলীকরণ",
                "trap_alert": "$\\sin^{-1}(1/\\sqrt{2}) = \\pi/4, \\cos^{-1}(1/2) = \\pi/3$।",
                "speed_hack": "$4(\\pi/4 + \\pi/3) = 4(7\\pi/12) = 7\\pi/3$।",
                "explanation": "$4(\\pi/4 + \\pi/3) = 4(7\\pi/12) = \\frac{7\\pi}{3}$।"
            },
            {
                "id": "pred_math_2nd_07_06",
                "stem": "$2\\tan^{-1}x$ এর মান নিচের কোনটির সমান?",
                "options": ["$\\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$", "$\\sin^{-1}\\left(\\frac{2x}{1-x^2}\\right)$", "$\\cos^{-1}\\left(\\frac{2x}{1+x^2}\\right)$", "$\\tan^{-1}\\left(\\frac{2x}{1+x^2}\\right)$"],
                "answer": "A",
                "type_ref": "বিপরীত বৃত্তীয় দ্বি-কোণ সূত্র",
                "trap_alert": "সাইন ইনভার্সের হরে $1+x^2$ থাকে।",
                "speed_hack": "$2\\tan^{-1}x = \\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$।",
                "explanation": "আদর্শ বিপরীত বৃত্তীয় অভেদ অনুসারে $2\\tan^{-1}x = \\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$।"
            },
            {
                "id": "pred_math_2nd_07_07",
                "stem": "$\\tan\\theta = 1$ সমীকরণের সাধারণ সমাধান কোনটি?",
                "options": ["$\\theta = n\\pi + \\frac{\\pi}{4}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi + \\frac{\\pi}{4}, n \\in \\mathbb{Z}$", "$\\theta = n\\pi \\pm \\frac{\\pi}{4}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi \\pm \\frac{\\pi}{4}, n \\in \\mathbb{Z}$"],
                "answer": "A",
                "type_ref": "ট্যান সমীকরণের সমাধান",
                "trap_alert": "ট্যানের পর্যায়কাল $\\pi$, তাই $n\\pi + \\alpha$।",
                "speed_hack": "$\\theta = n\\pi + \\pi/4$।",
                "explanation": "$\\tan\\theta = \\tan(\\pi/4) \implies \\theta = n\\pi + \\frac{\\pi}{4}, n \\in \\mathbb{Z}$।"
            },
            {
                "id": "pred_math_2nd_07_08",
                "stem": "$\\sin(\\cos^{-1}(\\tan(\\sin^{-1}x)))$ এর মান কত?",
                "options": ["$\\sqrt{\\frac{1-2x^2}{1-x^2}}$", "$\\frac{x}{\\sqrt{1-x^2}}$", "$\\sqrt{1 - x^2}$", "$\\frac{1}{\\sqrt{1+x^2}}$"],
                "answer": "A",
                "type_ref": "বিপরীত বৃত্তীয় ফাংশনের সমন্বয়",
                "trap_alert": "ক্রমান্বয়ে ত্রিভুজ রূপান্তর করতে হবে।",
                "speed_hack": "$\\sin(\\cos^{-1}(x/\\sqrt{1-x^2})) = \\sqrt{1 - x^2/(1-x^2)} = \\sqrt{\\frac{1-2x^2}{1-x^2}}$।",
                "explanation": "$\\sin^{-1}x = \\theta \implies \\tan\\theta = \\frac{x}{\\sqrt{1-x^2}}$। $\\sin(\\cos^{-1}u) = \\sqrt{1-u^2} = \\sqrt{\\frac{1-2x^2}{1-x^2}}$।"
            },
            {
                "id": "pred_math_2nd_07_09",
                "stem": "$\\sqrt{3}\\sin\\theta + \\cos\\theta = 2$ সমীকরণের সাধারণ সমাধান কোনটি?",
                "options": ["$\\theta = 2n\\pi + \\frac{\\pi}{3}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi \\pm \\frac{\\pi}{6}, n \\in \\mathbb{Z}$", "$\\theta = n\\pi + \\frac{\\pi}{3}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi - \\frac{\\pi}{3}, n \\in \\mathbb{Z}$"],
                "answer": "A",
                "type_ref": "$a\\cos\\theta + b\\sin\\theta = c$ সমীকরণ সমাধান",
                "trap_alert": "$2$ দ্বারা ভাগ করলে $\\cos(\\theta - \\pi/3) = 1$।",
                "speed_hack": "$\\theta - \\pi/3 = 2n\\pi \implies \\theta = 2n\\pi + \\pi/3$।",
                "explanation": "$\\frac{1}{2}\\cos\\theta + \\frac{\\sqrt{3}}{2}\\sin\\theta = 1 \implies \\cos(\\theta - \\pi/3) = 1 \implies \\theta = 2n\\pi + \\frac{\\pi}{3}$।"
            },
            {
                "id": "pred_math_2nd_07_10",
                "stem": "$\\sin^{-1}\\left(\\sin\\frac{2\\pi}{3}\\right)$ এর মুখ্য মান কত?",
                "options": ["$\\frac{\\pi}{3}$", "$\\frac{2\\pi}{3}$", "$-\\frac{\\pi}{3}$", "$\\frac{4\\pi}{3}$"],
                "answer": "A",
                "type_ref": "বিপরীত ত্রিকোণমিতিক মুখ্য ব্যবধি",
                "trap_alert": "মুখ্য ব্যবধি $[-\\pi/2, \\pi/2]$। $\\sin(2\\pi/3) = \\sin(\\pi/3)$।",
                "speed_hack": "মুখ্য মান $=\\pi/3$।",
                "explanation": "$\\sin(2\\pi/3) = \\sin(\\pi - \\pi/3) = \\sin(\\pi/3)$। অতএব $\\sin^{-1}(\\sin(\\pi/3)) = \\frac{\\pi}{3}$।"
            },
            {
                "id": "pred_math_2nd_07_11",
                "stem": "$\\cos^{-1}(-x)$ এর মান নিচের কোনটির সমান (যেখানে $|x| \\le 1$)?",
                "options": ["$\\pi - \\cos^{-1}x$", "$-\\cos^{-1}x$", "$\\cos^{-1}x$", "$\\frac{\\pi}{2} - \\cos^{-1}x$"],
                "answer": "A",
                "type_ref": "ঋণাত্মক যুক্তির বিপরীত কস",
                "trap_alert": "$\\cos^{-1}$ এর পরিসর $[0, \\pi]$ বজায় রাখতে $\\pi - \\cos^{-1}x$ হয়।",
                "speed_hack": "$\\cos^{-1}(-x) = \\pi - \\cos^{-1}x$।",
                "explanation": "সংজ্ঞানুসারে এবং মুখ্য মান সীমা $[0, \\pi]$ রাখতে $\\cos^{-1}(-x) = \\pi - \\cos^{-1}x$।"
            },
            {
                "id": "pred_math_2nd_07_12",
                "stem": "$\\cot^{-1}(3) + \\csc^{-1}(\\sqrt{5})$ এর মান কত?",
                "options": ["$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$", "$\\frac{\\pi}{3}$", "$\\frac{\\pi}{6}$"],
                "answer": "A",
                "type_ref": "ট্যানে রূপান্তর করে বিপরীত বৃত্তীয় যোগ",
                "trap_alert": "$\\tan^{-1}(1/3) + \\tan^{-1}(1/2) = \\pi/4$।",
                "speed_hack": "$\\frac{1/3+1/2}{1-1/6} = 1 \implies \\pi/4$।",
                "explanation": "$\\cot^{-1}(3) = \\tan^{-1}(1/3)$ এবং $\\csc^{-1}(\\sqrt{5}) = \\tan^{-1}(1/2)$। যোগফল $=\\tan^{-1}(1) = \\frac{\\pi}{4}$।"
            },
            {
                "id": "pred_math_2nd_07_13",
                "stem": "$\\tan^{-1}(1) + \\tan^{-1}(2) + \\tan^{-1}(3)$ এর মান কত?",
                "options": ["$\\pi$", "$\\frac{\\pi}{2}$", "$2\\pi$", "$\\frac{3\\pi}{4}$"],
                "answer": "A",
                "type_ref": "শর্তসাপেক্ষ বিপরীত ট্যান যোগফল",
                "trap_alert": "$2 \\times 3 > 1$ হওয়ায় $\\pi$ যোগ করতে হয়।",
                "speed_hack": "বিখ্যাত ফলাফল: মান $=\\pi$।",
                "explanation": "$\\tan^{-1}(2) + \\tan^{-1}(3) = \\pi + \\tan^{-1}(-1) = \\frac{3\\pi}{4}$। $\\frac{\\pi}{4} + \\frac{3\\pi}{4} = \\pi$।"
            },
            {
                "id": "pred_math_2nd_07_14",
                "stem": "যদি $\\sin^{-1}x + \\sin^{-1}y = \\frac{\\pi}{2}$ হয়, তবে $x^2 + y^2$ এর মান কত?",
                "options": ["$1$", "$0$", "$2$", "$\\frac{1}{2}$"],
                "answer": "A",
                "type_ref": "বিপরীত সাইন সমীকরণ বিশ্লেষণ",
                "trap_alert": "$\\sin^{-1}x = \\cos^{-1}y \implies x = \\sqrt{1-y^2} \implies x^2+y^2=1$।",
                "speed_hack": "$x^2 + y^2 = 1$।",
                "explanation": "$\\sin^{-1}x = \\frac{\\pi}{2} - \\sin^{-1}y = \\cos^{-1}y \implies x = \\cos(\\cos^{-1}y) = \\sqrt{1-y^2} \implies x^2+y^2=1$।"
            },
            {
                "id": "pred_math_2nd_07_15",
                "stem": "$0 \\le \\theta \\le 2\\pi$ সীমার মধ্যে $\\cos^2\\theta - \\sin^2\\theta = 0$ এর সমাধান সংখ্যা কয়টি?",
                "options": ["$4$", "$2$", "$8$", "$0$"],
                "answer": "A",
                "type_ref": "নির্দিষ্ট ব্যবধিতে সমাধান সংখ্যা",
                "trap_alert": "$\\cos 2\\theta = 0$ এর ৪টি সমাধান রয়েছে।",
                "speed_hack": "চারটি কোণ: $\\frac{\\pi}{4}, \\frac{3\\pi}{4}, \\frac{5\\pi}{4}, \\frac{7\\pi}{4}$।",
                "explanation": "$\\cos 2\\theta = 0 \implies 2\\theta = \\pi/2, 3\\pi/2, 5\\pi/2, 7\\pi/2$। মোট ৪টি সমাধান।"
            },
            {
                "id": "pred_math_2nd_07_16",
                "stem": "$\\cos^{-1}\\left(\\frac{1-x^2}{1+x^2}\\right) = 2\\tan^{-1}x$ অভেদটি সত্য হওয়ার শর্ত কোনটি?",
                "options": ["$x \\ge 0$", "$x \\le 0$", "$-1 \\le x \\le 1$", "সকল বাস্তব $x$"],
                "answer": "A",
                "type_ref": "বিপরীত ত্রিকোণমিতিক শর্তাদি",
                "trap_alert": "$\\cos^{-1}$ এর মান অঋণাত্মক হওয়ায় $x \\ge 0$ হতে হয়।",
                "speed_hack": "$x \\ge 0$।",
                "explanation": "বামে মান $[0, \\pi]$, ডানে $2\\tan^{-1}x$ কেবল তখনই অঋণাত্মক হবে যখন $x \\ge 0$।"
            },
            {
                "id": "pred_math_2nd_07_17",
                "stem": "$\\tan\\theta + \\cot\\theta = 2$ সমীকরণের সাধারণ সমাধান কোনটি?",
                "options": ["$\\theta = n\\pi + \\frac{\\pi}{4}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi + \\frac{\\pi}{4}, n \\in \\mathbb{Z}$", "$\\theta = n\\pi \\pm \\frac{\\pi}{4}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi \\pm \\frac{\\pi}{4}, n \\in \\mathbb{Z}$"],
                "answer": "A",
                "type_ref": "ট্যান দ্বিঘাত সমীকরণ",
                "trap_alert": "$t + 1/t = 2 \implies t = 1$।",
                "speed_hack": "$\\tan\\theta = 1 \implies \\theta = n\\pi + \\frac{\\pi}{4}$।",
                "explanation": "$(\\tan\\theta - 1)^2 = 0 \implies \\tan\\theta = 1 \implies \\theta = n\\pi + \\frac{\\pi}{4}$।"
            },
            {
                "id": "pred_math_2nd_07_18",
                "stem": "$\\sec^{-1}x$ এর ডোমেন (Domain) কোনটি?",
                "options": ["$(-\\infty, -1] \\cup [1, \\infty)$", "$[-1, 1]$", "$\\mathbb{R} \\setminus \\{0\\}$", "$[0, \\infty)$"],
                "answer": "A",
                "type_ref": "বিপরীত সেক এর ডোমেন",
                "trap_alert": "$|x| \\ge 1$ হতে হবে।",
                "speed_hack": "$(-\\infty, -1] \\cup [1, \\infty)$।",
                "explanation": "যেহেতু $|\\sec\\theta| \\ge 1$, বিপরীত ফাংশন $\\sec^{-1}x$ এর ডোমেন হলো $(-\\infty, -1] \\cup [1, \\infty)$।"
            },
            {
                "id": "pred_math_2nd_07_19",
                "stem": "$2\\sin^2\\theta + 3\\cos\\theta = 0$ সমীকরণটির সাধারণ সমাধান কোনটি?",
                "options": ["$\\theta = 2n\\pi \\pm \\frac{2\\pi}{3}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi \\pm \\frac{\\pi}{3}, n \\in \\mathbb{Z}$", "$\\theta = n\\pi \\pm \\frac{2\\pi}{3}, n \\in \\mathbb{Z}$", "$\\theta = 2n\\pi \\pm \\frac{5\\pi}{6}, n \\in \\mathbb{Z}$"],
                "answer": "A",
                "type_ref": "দ্বিঘাত ত্রিকোণমিতিক সমীকরণ",
                "trap_alert": "$\\cos\\theta = -1/2$ গ্রহণযোগ্য ($\\cos\\theta = 2$ অসম্ভব)।",
                "speed_hack": "$\\cos\\theta = -1/2 \implies \\theta = 2n\\pi \\pm 2\\pi/3$।",
                "explanation": "$2\\cos^2\\theta - 3\\cos\\theta - 2 = 0 \implies \\cos\\theta = -1/2 \implies \\theta = 2n\\pi \\pm \\frac{2\\pi}{3}$।"
            },
            {
                "id": "pred_math_2nd_07_20",
                "stem": "$\\sin^{-1}\\left(\\frac{3}{5}\\right) + \\sin^{-1}\\left(\\frac{8}{17}\\right)$ এর মান কত?",
                "options": ["$\\sin^{-1}\\left(\\frac{77}{85}\\right)$", "$\\sin^{-1}\\left(\\frac{84}{85}\\right)$", "$\\sin^{-1}\\left(\\frac{36}{85}\\right)$", "$\\sin^{-1}\\left(\\frac{13}{85}\\right)$"],
                "answer": "A",
                "type_ref": "বিপরীত সাইনের যোগফল সূত্র",
                "trap_alert": "$\\sin^{-1}(x\\sqrt{1-y^2} + y\\sqrt{1-x^2})$।",
                "speed_hack": "$\\frac{3}{5} \\cdot \\frac{15}{17} + \\frac{8}{17} \\cdot \\frac{4}{5} = \\frac{77}{85}$।",
                "explanation": "$\\sin^{-1}\\left(\\frac{3}{5} \\times \\frac{15}{17} + \\frac{8}{17} \\times \\frac{4}{5}\\right) = \\sin^{-1}\\left(\\frac{77}{85}\\right)$।"
            }
        ]
    }
