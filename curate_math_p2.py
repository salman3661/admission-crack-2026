#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""curate_math_p2.py - Curated with DU Most Repeated & Speed-Hacks"""

true = True
false = False
null = None

def get_part2_chapters():
    return [
    {
        "chapter_id": "math_1st_06",
        "chapter_title": "ত্রিকোণমিতিক অনুপাত (Trigonometric Ratios)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০৬",
        "predictors": [
            {
                "id": "pred_math_1st_06_01",
                "stem": "একটি বৃত্তের ব্যাসার্ধ $14\\text{ cm}$ হলে বৃত্তটির $11\\text{ cm}$ দীর্ঘ চাপ কেন্দ্রে কত ডিগ্রি কোণ উৎপন্ন করে?",
                "options": [
                    "$45^\\circ$",
                    "$30^\\circ$",
                    "$60^\\circ$",
                    "$90^\\circ$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বৃত্তচাপ, ব্যাসার্ধ ও কোণ ($s = r\\theta$)",
                "trap_alert": "কোণকে রেডিয়ান থেকে ডিগ্রিতে রূপান্তর ($180^\\circ/\\pi$) করতে ভুলে যাওয়া।",
                "speed_hack": "$\\theta = \\frac{s}{r} = \\frac{11}{14}\\text{ rad}$। ডিগ্রিতে: $\\frac{11}{14} \\times \\frac{180^\\circ}{22/7} = \\frac{11}{14} \\times \\frac{180 \\times 7}{22} = 45^\\circ$। ৩ সেকেন্ডে সমাধান!",
                "explanation": "$s = r\\theta \\implies \\theta = \\frac{s}{r} = \\frac{11}{14}$ রেডিয়ান $= \\frac{11}{14} \\times \\frac{180^\\circ}{\\pi} = 45^\\circ$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_02",
                "stem": "ঘড়িতে যখন দুপুর ২টা ১৫ মিনিট বাজে, তখন ঘণ্টার কাঁটা ও মিনিটের কাঁটার মধ্যবর্তী সূক্ষ্মকোণ কত?",
                "options": [
                    "$22.5^\\circ$",
                    "$30^\\circ$",
                    "$25^\\circ$",
                    "$37.5^\\circ$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ঘড়ির কাঁটা সংক্রান্ত কোণ",
                "trap_alert": "সরাসরি $30^\\circ$ দাগানো। ১৫ মিনিটে ঘণ্টার কাঁটাও যে কিছুটা এগিয়ে যায় তা খেয়াল রাখতে হবে!",
                "speed_hack": "ম্যাজিক ফর্মুলা: $\\theta = \\left|30H - \\frac{11}{2}M\\right| = \\left|30(2) - \\frac{11}{2}(15)\\right| = |60 - 82.5| = 22.5^\\circ$।",
                "explanation": "ঘড়ির কাঁটা দুটির মধ্যবর্তী কোণ $\\theta = |30H - 5.5M| = |60 - 82.5| = 22.5^\\circ$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_03",
                "stem": "যদি $\\sec\\theta + \\tan\\theta = 5$ হয়, তবে $\\sec\\theta - \\tan\\theta$ এর মান কত?",
                "options": [
                    "$\\frac{1}{5}$",
                    "$5$",
                    "$-5$",
                    "$\\frac{2}{5}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিকোণমিতিক অভেদাবলী ও অনুপাত",
                "trap_alert": "চিহ্ন বদল করে $-5$ ভাবা। এটি গুণাত্মক বিপরীত ($1/5$), যোগাত্মক নয়!",
                "speed_hack": "আমরা জানি $\\sec^2\\theta - \\tan^2\\theta = 1 \\implies (\\sec\\theta + \\tan\\theta)(\\sec\\theta - \\tan\\theta) = 1$। তাই মান হবে $1/5$।",
                "explanation": "$\\sec\\theta - \\tan\\theta = \\frac{1}{\\sec\\theta + \\tan\\theta} = \\frac{1}{5}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_04",
                "stem": "যদি $\\tan\\theta = -\\frac{4}{3}$ এবং $\\cos\\theta > 0$ হয়, তবে $\\sin\\theta$ এর মান কত?",
                "options": [
                    "$-\\frac{4}{5}$",
                    "$\\frac{4}{5}$",
                    "$-\\frac{3}{5}$",
                    "$\\frac{3}{5}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: চতুর্ভাগে চিহ্নের নিয়ম ও অনুপাত",
                "trap_alert": "চতুর্ভাগ ভুল শনাক্ত করা। $\\tan < 0$ ও $\\cos > 0$ মানে কোণটি ৪র্থ চতুর্ভাগে, যেখানে $\\sin$ ঋণাত্মক!",
                "speed_hack": "৪র্থ চতুর্ভাগে $\\sin\\theta$ ঋণাত্মক। ট্রিপলেট $(3, 4, 5) \\implies \\sin\\theta = -4/5$।",
                "explanation": "$\\cos\\theta > 0$ এবং $\\tan\\theta < 0$ হওয়ায় কোণ $\\theta$ ৪র্থ চতুর্ভাগে অবস্থান করে। ৪র্থ চতুর্ভাগে $\\sin\\theta = -4/5$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_05",
                "stem": "$\\tan 1^\\circ \\cdot \\tan 2^\\circ \\cdot \\tan 3^\\circ \\dots \\tan 89^\\circ$ এর মান কত?",
                "options": [
                    "$1$",
                    "$0$",
                    "$\\infty$",
                    "$\\frac{1}{2}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: পূরক কোণের রূপান্তর",
                "trap_alert": "$\\tan 90^\\circ$ মনে করে মান অসংজ্ঞায়িত বা শূন্য দাগানো। এখানে শেষ পদ $\\tan 89^\\circ$!",
                "speed_hack": "$\\tan(90^\\circ - \\theta) = \\cot\\theta \\implies \\tan 89^\\circ = \\cot 1^\\circ$। $\\tan 1^\\circ \\cot 1^\\circ = 1$ এভাবে সব জোড়া কেটে মাঝে শুধু $\\tan 45^\\circ = 1$ থাকে।",
                "explanation": "প্রথম ও শেষ পদগুলো গুণ হয়ে ১ তৈরি করে এবং মাঝের $\\tan 45^\\circ = 1$, ফলে সামগ্রিক গুণফল ১।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_06",
                "stem": "$\\sin^2 10^\\circ + \\sin^2 20^\\circ + \\dots + \\sin^2 80^\\circ$ এর মান কত?",
                "options": [
                    "$4$",
                    "$8$",
                    "$4.5$",
                    "$3.5$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বর্গের সমষ্টি ও পূরক কোণ",
                "trap_alert": "মোট পদের সংখ্যা ও জোড়া ঠিকমতো না গুনে পদ সংখ্যাকে সরাসরি উত্তর ভাবা।",
                "speed_hack": "পদ সংখ্যা $(80-10)/10 + 1 = 8$ টি। প্রতি জোড়ায় $\\sin^2\\theta + \\cos^2\\theta = 1$। মোট ৪টি জোড়া $\\implies 4 \\times 1 = 4$।",
                "explanation": "$\\sin^2 10^\\circ + \\sin^2 80^\\circ = \\sin^2 10^\\circ + \\cos^2 10^\\circ = 1$। এমন ৪টি জোড়ার সমষ্টি $4$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_07",
                "stem": "একটি চাকার ব্যাস $1\\text{ m}$ হলে $314\\text{ m}$ দূরত্ব অতিক্রম করতে চাকাটি কতবার পূর্ণ ঘূর্ণন সম্পন্ন করবে? (ধরি $\\pi \\approx 3.14$)",
                "options": [
                    "$100$",
                    "$50$",
                    "$200$",
                    "$314$"
                ],
                "answer": "A",
                "type_ref": "Type 1: চাকার ঘূর্ণন ও পরিধি",
                "trap_alert": "ব্যাস দেওয়া আছে, ব্যাসার্ধ নয়! পরিধি $=\\pi d = 3.14\\text{ m}$।",
                "speed_hack": "ঘূর্ণন সংখ্যা $N = \\frac{\\text{মোট দূরত্ব}}{\\pi d} = \\frac{314}{3.14 \\times 1} = 100$ বার।",
                "explanation": "১ বার ঘুরলে অতিক্রম করে পরিধি $\\pi d = 3.14\\text{ m}$। সুতরাং ঘূর্ণন সংখ্যা $= 314/3.14 = 100$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_08",
                "stem": "$\\cos\\left(-\\frac{19\\pi}{3}\\right)$ এর সঠিক মান কোনটি?",
                "options": [
                    "$\\frac{1}{2}$",
                    "$-\\frac{1}{2}$",
                    "$\\frac{\\sqrt{3}}{2}$",
                    "$-\\frac{\\sqrt{3}}{2}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ঋণাত্মক ও বৃহৎ কোণের অনুপাত",
                "trap_alert": "$\\cos(-\\theta) = \\cos\\theta$ মনে না রেখে চিহ্নের ভুল করে মাইনাস দাগানো।",
                "speed_hack": "$\\cos(-\\theta) = \\cos\\theta$। $\\cos(19\\pi/3) = \\cos(6\\pi + \\pi/3) = \\cos(\\pi/3) = 1/2$। ৩ সেকেন্ডে সমাধান!",
                "explanation": "$\\cos(-19\\pi/3) = \\cos(19\\pi/3) = \\cos(6\\pi + \\pi/3) = \\cos(\\pi/3) = 1/2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_09",
                "stem": "$r$ ব্যাসার্ধবিশিষ্ট বৃত্তের কোনো বৃত্তকলার কোণ $\\theta$ রেডিয়ান হলে বৃত্তকলাটির ক্ষেত্রফল কত?",
                "options": [
                    "$\\frac{1}{2}r^2\\theta$",
                    "$r^2\\theta$",
                    "$\\frac{1}{2}r\\theta$",
                    "$\\pi r^2\\theta$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বৃত্তকলার ক্ষেত্রফল",
                "trap_alert": "হাফ ($1/2$) বাদ দিয়ে সরাসরি $r^2\\theta$ দাগানো।",
                "speed_hack": "বৃত্তকলার ক্ষেত্রফল $A = \\frac{1}{2}r^2\\theta = \\frac{1}{2}rs$ (যেখানে $s = r\\theta$)।",
                "explanation": "সম্পূর্ণ বৃত্তের ক্ষেত্রফল $\\pi r^2$ এবং সম্পূর্ণ কোণ $2\\pi$, ফলে ক্ষেত্রফল $= \\frac{\\theta}{2\\pi} \\times \\pi r^2 = \\frac{1}{2}r^2\\theta$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_10",
                "stem": "যদি $\\csc\\theta - \\cot\\theta = \\frac{1}{3}$ হয়, তবে $\\cos\\theta$ এর মান কত?",
                "options": [
                    "$\\frac{4}{5}$",
                    "$\\frac{3}{5}$",
                    "$-\\frac{4}{5}$",
                    "$\\frac{5}{4}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিকোণমিতিক রূপান্তর",
                "trap_alert": "যোগ করে $\\csc\\theta = 5/3$ পাওয়ার পর $\\cos\\theta$ বের করতে গিয়ে সাইন ও কস গুলিয়ে ফেলা।",
                "speed_hack": "$\\csc\\theta + \\cot\\theta = 3$। যোগ করলে $2\\csc\\theta = 10/3 \\implies \\sin\\theta = 3/5$। ট্রিপলেট $(3, 4, 5) \\implies \\cos\\theta = 4/5$।",
                "explanation": "$\\csc\\theta + \\cot\\theta = 3$ ও $\\csc\\theta - \\cot\\theta = 1/3$ সমাধান করে $\\sin\\theta = 3/5 \\implies \\cos\\theta = 4/5$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_11",
                "stem": "$\\frac{1 - \\tan^2 30^\\circ}{1 + \\tan^2 30^\\circ}$ এর মান কত?",
                "options": [
                    "$\\frac{1}{2}$",
                    "$\\frac{\\sqrt{3}}{2}$",
                    "$\\frac{1}{\\sqrt{3}}$",
                    "$1$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিকোণমিতিক দ্বিগুণ কোণ রূপান্তর (DU Speed-Hack)",
                "trap_alert": "মান বসিয়ে জটিল ভগ্নাংশ সমাধান করতে গিয়ে সময় নষ্ট করা।",
                "speed_hack": "দ্বিগুণ কোণের সূত্র: $\\frac{1-\\tan^2\\theta}{1+\\tan^2\\theta} = \\cos 2\\theta$। এখানে $\\theta = 30^\\circ$, তাই $\\cos(2 \\times 30^\\circ) = \\cos 60^\\circ = \\frac{1}{2}$! ২ সেকেন্ডে উত্তর!",
                "explanation": "$\\frac{1-\\tan^2 30^\\circ}{1+\\tan^2 30^\\circ} = \\cos(2 \\times 30^\\circ) = \\cos 60^\\circ = 1/2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_12",
                "stem": "$\\cot\\left(-\\frac{15\\pi}{4}\\right)$ এর মান কত?",
                "options": [
                    "$1$",
                    "$-1$",
                    "$0$",
                    "$\\sqrt{3}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ঋণাত্মক কোণের কোট্যাঞ্জেন্ট",
                "trap_alert": "$\\cot(-\\theta) = -\\cot\\theta$ এবং কোয়াড্রেন্টের চিহ্নে মাইনাসে মাইনাসে প্লাস হবে!",
                "speed_hack": "$-\\cot(15\\pi/4) = -\\cot(4\\pi - \\pi/4) = -(-\\cot(\\pi/4)) = 1$।",
                "explanation": "$\\cot(-15\\pi/4) = -\\cot(4\\pi - \\pi/4) = -(-\\cot\\pi/4) = \\cot 45^\\circ = 1$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_13",
                "stem": "সকল বাস্তব $\\theta$ এর জন্য $\\sin^2\\theta + \\cos^4\\theta$ এর সর্বনিম্ন মান কত?",
                "options": [
                    "$\\frac{3}{4}$",
                    "$1$",
                    "$\\frac{1}{2}$",
                    "$0$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিকোণমিতিক রাশির সীমা ও চরম মান",
                "trap_alert": "সর্বনিম্ন মান সরাসরি শূন্য ধরে নেওয়া। এটি একটি পূর্ণবর্গ রাশির ন্যূনতম মান!",
                "speed_hack": "$1 - \\cos^2\\theta + \\cos^4\\theta = \\left(\\cos^2\\theta - \\frac{1}{2}\\right)^2 + \\frac{3}{4}$। ন্যূনতম মান $= 3/4$ (যখন $\\cos^2\\theta = 1/2$)।",
                "explanation": "পূর্ণবর্গ আকারে রূপান্তর করলে ন্যূনতম মান দাঁড়ায় $3/4$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_14",
                "stem": "$\\sin 750^\\circ$ এর মান কোনটি?",
                "options": [
                    "$\\frac{1}{2}$",
                    "$-\\frac{1}{2}$",
                    "$\\frac{\\sqrt{3}}{2}$",
                    "$-\\frac{\\sqrt{3}}{2}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: কোয়াড্রেন্ট রূপান্তর",
                "trap_alert": "$720^\\circ$ মানে দুই পূর্ণ ঘূর্ণন বাদ দিতে ভুল করা।",
                "speed_hack": "$750^\\circ = 2 \\times 360^\\circ + 30^\\circ \\implies \\sin 30^\\circ = 1/2$।",
                "explanation": "$\\sin(2 \\times 360^\\circ + 30^\\circ) = \\sin 30^\\circ = 1/2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_15",
                "stem": "যদি $\\theta$ কোণটি ২য় চতুর্ভাগে থাকে এবং $\\sin\\theta = \\frac{5}{13}$ হয়, তবে $\\tan\\theta$ এর মান কত?",
                "options": [
                    "$-\\frac{5}{12}$",
                    "$\\frac{5}{12}$",
                    "$-\\frac{12}{5}$",
                    "$\\frac{12}{13}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ২য় চতুর্ভাগে ত্রিকোণমিতিক মান",
                "trap_alert": "২য় চতুর্ভাগে $\\tan$ ঋণাত্মক, তাই প্লাস মান বাদ দিতে হবে!",
                "speed_hack": "পিথাগোরাস ট্রিপলেট $(5, 12, 13)$। ২য় চতুর্ভাগে $\\tan\\theta = -\\frac{\\text{লম্ব}}{\\text{ভূমি}} = -\\frac{5}{12}$।",
                "explanation": "২য় চতুর্ভাগে লম্ব $5$, অতিভুজ $13 \\implies$ ভূমি $-12$। সুতরাং $\\tan\\theta = -5/12$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_16",
                "stem": "রেডিয়ানে কোণ প্রকাশের ক্ষেত্রে $1\\text{ rad}$ সমান প্রায় কত ডিগ্রি?",
                "options": [
                    "$57.3^\\circ$",
                    "$60^\\circ$",
                    "$45^\\circ$",
                    "$53.7^\\circ$"
                ],
                "answer": "A",
                "type_ref": "Type 1: রেডিয়ান ও ডিগ্রি সম্পর্ক",
                "trap_alert": "$57.3^\\circ$ এর সাথে $53.7^\\circ$ গুলিয়ে ফেলা।",
                "speed_hack": "$1\\text{ rad} = \\frac{180^\\circ}{\\pi} \\approx \\frac{180}{3.1416} \\approx 57.2958^\\circ \\approx 57.3^\\circ$।",
                "explanation": "$1\\text{ rad} = 180^\\circ / \\pi \\approx 57^\\circ 17' 44'' \\approx 57.3^\\circ$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_17",
                "stem": "$\\cos^2\\theta + \\sec^2\\theta$ এর সর্বনিম্ন মান কত?",
                "options": [
                    "$2$",
                    "$1$",
                    "$0$",
                    "$4$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বীজগণিতীয় অসমতা ও ত্রিকোণমিতি ($AM \\ge GM$)",
                "trap_alert": "$1 + 1 = 2$ কে ভাবা শুধুমাত্র নির্দিষ্ট কোণের মান, এটি সর্বদা $\\ge 2$!",
                "speed_hack": "$a + \\frac{1}{a} \\ge 2$ ($AM \\ge GM$)। এখানে $\\cos^2\\theta + \\frac{1}{\\cos^2\\theta} \\ge 2$। সর্বনিম্ন মান ২।",
                "explanation": "$(\\cos\\theta - \\sec\\theta)^2 + 2 \\ge 2$, ফলে সর্বনিম্ন মান ২।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_06_18",
                "stem": "কোনো সমকোণী ত্রিভুজের সূক্ষ্মকোণদ্বয়ের একটি $30^\\circ$ হলে তাদের ত্রিকোণমিতিক সাইনের অনুপাত কত?",
                "options": [
                    "$1 : \\sqrt{3}$",
                    "$1 : 2$",
                    "$1 : 1$",
                    "$\\sqrt{3} : 2$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সমকোণী ত্রিভুজের কোণ অনুপাত",
                "trap_alert": "অপর কোণটি যে $60^\\circ$ তা বের করে $\\sin 30^\\circ : \\sin 60^\\circ$ এর অনুপাত নিতে হবে!",
                "speed_hack": "কোণদ্বয় $30^\\circ$ ও $60^\\circ$। সাইনের অনুপাত $\\frac{1}{2} : \\frac{\\sqrt{3}}{2} = 1 : \\sqrt{3}$।",
                "explanation": "সূক্ষ্মকোণদ্বয় $30^\\circ$ ও $60^\\circ$, তাদের সাইনের অনুপাত $\\sin 30^\\circ / \\sin 60^\\circ = (1/2)/(\\sqrt{3}/2) = 1/\\sqrt{3}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    },
    {
        "chapter_id": "math_1st_07",
        "chapter_title": "সংযুক্ত কোণের ত্রিকোণমিতিক অনুপাত (Associated Angles)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০৭",
        "predictors": [
            {
                "id": "pred_math_1st_07_01",
                "stem": "$3\\sin\\theta + 4\\cos\\theta$ রাশিটির সর্বোচ্চ (Maximum) মান কত?",
                "options": [
                    "$5$",
                    "$7$",
                    "$1$",
                    "$\\sqrt{7}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: $a\\sin\\theta + b\\cos\\theta$ এর চরম মান",
                "trap_alert": "সরাসরি সহগ দুটি যোগ করে $3 + 4 = 7$ দাগানো। চরম মানের সূত্র $\\sqrt{a^2 + b^2}$!",
                "speed_hack": "সর্বোচ্চ মান $= \\sqrt{a^2 + b^2} = \\sqrt{3^2 + 4^2} = 5$। ১ সেকেন্ডে সমাধান!",
                "explanation": "$a\\sin\\theta + b\\cos\\theta$ এর সর্বোচ্চ মান $+\\sqrt{a^2+b^2} = \\sqrt{9+16} = 5$ এবং সর্বনিম্ন মান $-5$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_02",
                "stem": "$\\cos 20^\\circ \\cos 40^\\circ \\cos 80^\\circ$ এর মান কত?",
                "options": [
                    "$\\frac{1}{8}$",
                    "$\\frac{1}{16}$",
                    "$\\frac{\\sqrt{3}}{8}$",
                    "$\\frac{1}{4}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ঢাবি স্পেশাল কোসাইন গুণন সিরিজ (DU Speed-Hack)",
                "trap_alert": "দীর্ঘ ২ দিয়ে গুণ ও যোগ-বিয়োগ না করে সরাসরি গুণন ট্রিক মনে রাখুন।",
                "speed_hack": "ঢাবি স্পেশাল কোসাইন গুণন শর্টকাট: $\\cos\\theta \\cos 2\\theta \\dots \\cos(2^n\\theta) = \\frac{\\sin(2^{n+1}\\theta)}{2^{n+1}\\sin\\theta}$। এখানে $\\theta = 20^\\circ, n = 2 \\implies \\frac{\\sin(8 \\times 20^\\circ)}{8\\sin 20^\\circ} = \\frac{\\sin 160^\\circ}{8\\sin 20^\\circ} = \\frac{1}{8}$!",
                "explanation": "কোসাইন সিরিজের সরাসরি সূত্রানুসারে মান $\\frac{1}{2^3} = \\frac{1}{8}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_03",
                "stem": "$\\tan 20^\\circ \\tan 40^\\circ \\tan 80^\\circ$ এর মান কত?",
                "options": [
                    "$\\sqrt{3}$",
                    "$\\frac{1}{\\sqrt{3}}$",
                    "$1$",
                    "$3$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ট্যানজেন্ট গুণফল ট্রিক",
                "trap_alert": "হর ও লব উল্টে $1/\\sqrt{3}$ ভাবা।",
                "speed_hack": "শর্টকাট: $\\tan\\theta \\tan(60^\\circ-\\theta) \\tan(60^\\circ+\\theta) = \\tan 3\\theta$। এখানে $\\theta = 20^\\circ \\implies \\tan 60^\\circ = \\sqrt{3}$।",
                "explanation": "$\\tan 20^\\circ \\tan 40^\\circ \\tan 80^\\circ = \\tan(3 \\times 20^\\circ) = \\tan 60^\\circ = \\sqrt{3}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_04",
                "stem": "যদি $A + B = 45^\\circ$ হয়, তবে $(1 + \\tan A)(1 + \\tan B)$ এর মান কত?",
                "options": [
                    "$2$",
                    "$1$",
                    "$0$",
                    "$-1$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বিশেষ কোণের ট্যানজেন্ট অভেদ",
                "trap_alert": "মান বসানোর সময় $A = 45^\\circ, B = 0^\\circ$ ধরলে মুহূর্তেই উত্তর চলে আসে!",
                "speed_hack": "শর্টকাট স্পিড ট্রিক: $A = 45^\\circ, B = 0^\\circ$ বসান! $(1 + \\tan 45^\\circ)(1 + \\tan 0^\\circ) = (1 + 1)(1 + 0) = 2$।",
                "explanation": "$\\tan(A+B) = \\frac{\\tan A+\\tan B}{1-\\tan A\\tan B} = 1 \\implies \\tan A+\\tan B = 1 - \\tan A\\tan B \\implies (1+\\tan A)(1+\\tan B) = 2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_05",
                "stem": "$\\frac{\\cos 8^\\circ + \\sin 8^\\circ}{\\cos 8^\\circ - \\sin 8^\\circ}$ এর মান কোনটির সমান?",
                "options": [
                    "$\\tan 53^\\circ$",
                    "$\\tan 37^\\circ$",
                    "$\\cot 53^\\circ$",
                    "$\\tan 45^\\circ$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ট্যান কোণ রূপান্তর ট্রিক (DU Speed-Hack)",
                "trap_alert": "লবে প্লাস থাকলে কোণ $45^\\circ + \\theta$ হয়; লবে মাইনাস থাকলে $45^\\circ - \\theta$ হয়!",
                "speed_hack": "ট্যান রূপান্তর ট্রিক: $\\frac{\\cos\\theta + \\sin\\theta}{\\cos\\theta - \\sin\\theta} = \\tan(45^\\circ + \\theta)$। এখানে $\\theta = 8^\\circ$, তাই $\\tan(45^\\circ + 8^\\circ) = \\tan 53^\\circ$! মুখে মুখে ১ সেকেন্ডে সমাধান!",
                "explanation": "লব ও হরকে $\\cos 8^\\circ$ দ্বারা ভাগ করলে $\\frac{1 + \\tan 8^\\circ}{1 - \\tan 8^\\circ} = \\tan(45^\\circ + 8^\\circ) = \\tan 53^\\circ$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_06",
                "stem": "$\\sin 75^\\circ$ এর সঠিক মান কোনটি?",
                "options": [
                    "$\\frac{\\sqrt{6} + \\sqrt{2}}{4}$",
                    "$\\frac{\\sqrt{6} - \\sqrt{2}}{4}$",
                    "$\\frac{\\sqrt{3} + 1}{2\\sqrt{2}}$",
                    "$\\frac{\\sqrt{3} - 1}{2\\sqrt{2}}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: যৌগিক কোণ ($45^\\circ + 30^\\circ$)",
                "trap_alert": "$\\sin 75^\\circ$ ধনাত্মক ও বড় (প্রায় $0.96$), তাই মাঝে প্লাস চিহ্ন হবে। মাইনাস চিহ্ন হলো $\\sin 15^\\circ$!",
                "speed_hack": "$\\sin(45^\\circ + 30^\\circ) = \\sin 45^\\circ\\cos 30^\\circ + \\cos 45^\\circ\\sin 30^\\circ = \\frac{1}{\\sqrt{2}}\\frac{\\sqrt{3}}{2} + \\frac{1}{\\sqrt{2}}\\frac{1}{2} = \\frac{\\sqrt{3}+1}{2\\sqrt{2}} = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$।",
                "explanation": "যৌগিক কোণের সূত্রানুসারে $\\sin 75^\\circ = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_07",
                "stem": "$\\sqrt{2 + \\sqrt{2 + 2\\cos 4\\theta}}$ রাশিটির সরলীকৃত মান কোনটি?",
                "options": [
                    "$2\\cos\\theta$",
                    "$2\\cos 2\\theta$",
                    "$2\\sin\\theta$",
                    "$\\sqrt{2}\\cos\\theta$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বহু-বর্গমূল বিশিষ্ট গুণিতক কোণ",
                "trap_alert": "বর্গমূলের বাইরে প্রতিটি ধাপে কোণ অর্ধেক হয়: $4\\theta \\to 2\\theta \\to \\theta$!",
                "speed_hack": "$1 + \\cos 4\\theta = 2\\cos^2 2\\theta \\implies \\sqrt{4\\cos^2 2\\theta} = 2\\cos 2\\theta$। আবার $\\sqrt{2(1+\\cos 2\\theta)} = 2\\cos\\theta$।",
                "explanation": "ধারাবাহিক গুণিতক কোণের সূত্রে মান বের হয় $2\\cos\\theta$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_08",
                "stem": "কোনো ত্রিভুজের বাহুগুলোর দৈর্ঘ্য যথাক্রমে $3, 5, 7$ একক হলে ত্রিভুজটির বৃহত্তম কোণটির মান কত?",
                "options": [
                    "$120^\\circ$",
                    "$135^\\circ$",
                    "$150^\\circ$",
                    "$90^\\circ$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিভুজের কোসাইন সূত্র",
                "trap_alert": "বৃহত্তম বাহুর বিপরীত কোণটিই বৃহত্তম কোণ! $\\cos C = -1/2$ হলে কোণ $120^\\circ$ হয়।",
                "speed_hack": "বৃহত্তম বাহু $c = 7$। $\\cos C = \\frac{3^2 + 5^2 - 7^2}{2 \\times 3 \\times 5} = \\frac{9 + 25 - 49}{30} = \\frac{-15}{30} = -\\frac{1}{2} \\implies C = 120^\\circ$।",
                "explanation": "কোসাইন সূত্র $\\cos C = \\frac{a^2+b^2-c^2}{2ab} = -1/2 \\implies C = 180^\\circ - 60^\\circ = 120^\\circ$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_09",
                "stem": "একটি ত্রিভুজের তিনটি কোণের অনুপাত $1 : 2 : 3$ হলে তাদের বিপরীত বাহুগুলোর অনুপাত কত?",
                "options": [
                    "$1 : \\sqrt{3} : 2$",
                    "$1 : 2 : 3$",
                    "$1 : \\sqrt{2} : \\sqrt{3}$",
                    "$2 : \\sqrt{3} : 1$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিভুজের সাইন সূত্র ও বাহুর অনুপাত",
                "trap_alert": "কোণের অনুপাতকে সরাসরি বাহুর অনুপাত ধরে $1:2:3$ দাগানো! বাহুর অনুপাত হলো সাইনের অনুপাত!",
                "speed_hack": "কোণত্রয়: $30^\\circ, 60^\\circ, 90^\\circ$। বাহুর অনুপাত $a:b:c = \\sin 30^\\circ : \\sin 60^\\circ : \\sin 90^\\circ = \\frac{1}{2} : \\frac{\\sqrt{3}}{2} : 1 = 1 : \\sqrt{3} : 2$।",
                "explanation": "সাইন সূত্রানুসারে $a:b:c = \\sin A : \\sin B : \\sin C$। এখানে $30^\\circ, 60^\\circ, 90^\\circ$ কোণের সাইন মান $1 : \\sqrt{3} : 2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_10",
                "stem": "$\\triangle ABC$-তে $A+B+C = \\pi$ হলে $\\sin 2A + \\sin 2B + \\sin 2C$ এর মান কোনটির সমান?",
                "options": [
                    "$4\\sin A \\sin B \\sin C$",
                    "$2\\sin A \\sin B \\sin C$",
                    "$4\\cos A \\cos B \\cos C$",
                    "$\\sin A + \\sin B + \\sin C$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ৭.৬ রূপান্তর ফ্লো ও কোণ প্রতিস্থাপন ট্রিক (DU Speed-Hack)",
                "trap_alert": "কোসাইন নাকি সাইন গুণফল তা নিয়ে বিভ্রান্ত হওয়া। $\\sin 2A + \\sin 2B + \\sin 2C = 4\\sin A \\sin B \\sin C$!",
                "speed_hack": "৭.৬ ট্রান্সফর্মেশন ফ্লো ট্রিক: সমকোণী ত্রিভুজ অ্যাঙ্গেল সাবস্টিটিউশন ($A = 90^\\circ, B = 45^\\circ, C = 45^\\circ$) বসালে বামপক্ষ $= \\sin 180^\\circ + \\sin 90^\\circ + \\sin 90^\\circ = 0 + 1 + 1 = 2$। ডানপক্ষে $4\\sin 90^\\circ \\sin 45^\\circ \\sin 45^\\circ = 4(1)(1/\\sqrt{2})(1/\\sqrt{2}) = 2$! ম্যাজিক সমাধান!",
                "explanation": "ত্রিকোণমিতিক রূপান্তর প্রক্রিয়ায় $\\sin 2A + \\sin 2B + \\sin 2C = 4\\sin A \\sin B \\sin C$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_11",
                "stem": "$\\sin 15^\\circ \\cos 15^\\circ$ এর মান কত?",
                "options": [
                    "$\\frac{1}{4}$",
                    "$\\frac{1}{2}$",
                    "$\\frac{\\sqrt{3}}{4}$",
                    "$\\frac{1}{8}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: গুণিতক কোণ",
                "trap_alert": "হাফ গুণ করতে ভুলে $\\frac{1}{2}$ দাগানো। $2\\sin A\\cos A = \\sin 2A$!",
                "speed_hack": "$\\sin 15^\\circ \\cos 15^\\circ = \\frac{1}{2}(2\\sin 15^\\circ \\cos 15^\\circ) = \\frac{1}{2}\\sin 30^\\circ = \\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$।",
                "explanation": "$\\frac{1}{2}\\sin(2 \\times 15^\\circ) = \\frac{1}{2}\\sin 30^\\circ = 1/4$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_12",
                "stem": "$\\sin 20^\\circ \\sin 40^\\circ \\sin 80^\\circ$ এর মান কত?",
                "options": [
                    "$\\frac{\\sqrt{3}}{8}$",
                    "$\\frac{1}{8}$",
                    "$\\frac{\\sqrt{3}}{16}$",
                    "$\\frac{3}{8}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: সাইনের গুণিতক গুণফল",
                "trap_alert": "কসের $1/8$ এর সাথে সাইনের মান গুলিয়ে ফেলা।",
                "speed_hack": "শর্টকাট: $\\sin\\theta \\sin(60^\\circ-\\theta) \\sin(60^\\circ+\\theta) = \\frac{1}{4}\\sin 3\\theta$। এখানে $\\theta = 20^\\circ \\implies \\frac{1}{4}\\sin 60^\\circ = \\frac{\\sqrt{3}}{8}$।",
                "explanation": "$\\sin 20^\\circ \\sin 40^\\circ \\sin 80^\\circ = \\frac{1}{4}\\sin 60^\\circ = \\frac{\\sqrt{3}}{8}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_13",
                "stem": "$\\tan A + \\cot A$ রাশিটির সরলীকৃত রূপ কোনটি?",
                "options": [
                    "$2\\csc 2A$",
                    "$2\\sec 2A$",
                    "$\\sin 2A$",
                    "$2\\tan 2A$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ত্রিকোণমিতিক রূপান্তর",
                "trap_alert": "হর ও লব মিলিয়ে কসেক ও সেকের মধ্যে কনফিউজড হওয়া।",
                "speed_hack": "$\\frac{\\sin A}{\\cos A} + \\frac{\\cos A}{\\sin A} = \\frac{\\sin^2 A + \\cos^2 A}{\\sin A\\cos A} = \\frac{1}{\\frac{1}{2}\\sin 2A} = 2\\csc 2A$।",
                "explanation": "লবে ১ এবং হরে $\\frac{1}{2}\\sin 2A$ আসায় উত্তর $2\\csc 2A$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_14",
                "stem": "যদি $\\sin(A+B)\\sin(A-B) = k$ হয়, তবে $k$ এর মান কোনটির সমান?",
                "options": [
                    "$\\sin^2 A - \\sin^2 B$",
                    "$\\sin^2 A + \\sin^2 B$",
                    "$\\cos^2 A - \\cos^2 B$",
                    "$\\sin^2(A-B)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ত্রিকোণমিতিক বর্গের গুণফল সূত্র",
                "trap_alert": "চিহ্ন বদল করে প্লাস দেওয়া। এটি $\\sin^2 A - \\sin^2 B$ অথবা $\\cos^2 B - \\cos^2 A$!",
                "speed_hack": "স্ট্যান্ডার্ড সূত্র: $\\sin(A+B)\\sin(A-B) = \\sin^2 A - \\sin^2 B = \\cos^2 B - \\cos^2 A$।",
                "explanation": "বীজগণিতীয় বিস্তারে $\\sin(A+B)\\sin(A-B) = \\sin^2 A - \\sin^2 B$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_15",
                "stem": "$5\\cos\\theta - 12\\sin\\theta + 3$ রাশিটির সর্বনিম্ন মান কত?",
                "options": [
                    "$-10$",
                    "$-13$",
                    "$16$",
                    "$-16$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ধ্রুবকযুক্ত ত্রিকোণমিতিক চরম মান",
                "trap_alert": "ধ্রুবক $+3$ যোগ করতে ভুলে শুধু $-13$ দাগানো!",
                "speed_hack": "$5\\cos\\theta - 12\\sin\\theta$ এর সর্বনিম্ন মান $= -\\sqrt{5^2 + 12^2} = -13$। সাথে $+3$ যোগ করলে মোট মান $= -13 + 3 = -10$।",
                "explanation": "রাশিটির সর্বনিম্ন মান $-\\sqrt{5^2+(-12)^2} + 3 = -13 + 3 = -10$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_16",
                "stem": "ত্রিভুজ $ABC$-তে পরিব্যাসার্ধ $R$ হলে সাইন সূত্রের সঠিক রূপ কোনটি?",
                "options": [
                    "$\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$",
                    "$\\frac{a}{\\sin A} = R$",
                    "$\\frac{\\sin A}{a} = 2R$",
                    "$a\\sin A = 2R$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিভুজের সাইন সূত্র ও পরিব্যাসার্ধ",
                "trap_alert": "$2R$ এর জায়গায় শুধু $R$ দাগানো। এটি পরিবৃত্তের ব্যাস $2R$ এর সমান!",
                "speed_hack": "সাইন সূত্র: বাহু ও বিপরীত কোণের সাইনের অনুপাত পরিবৃত্তের ব্যাস $2R$ এর সমান।",
                "explanation": "যেকোনো ত্রিভুজে $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_17",
                "stem": "একটি ত্রিভুজের বাহুগুলোর দৈর্ঘ্য যথাক্রমে $13, 14, 15$ একক হলে ত্রিভুজটির ক্ষেত্রফল কত বর্গ একক?",
                "options": [
                    "$84$",
                    "$42$",
                    "$168$",
                    "$105$"
                ],
                "answer": "A",
                "type_ref": "Type 2: হেরনের সূত্র দ্বারা ক্ষেত্রফল",
                "trap_alert": "অর্ধ-পরিসীমা $s = 21$ বের করে সূত্রে ভুল করা। এটি বিখ্যাত $13, 14, 15 \\to 84$ ট্রিপলেট!",
                "speed_hack": "$s = (13+14+15)/2 = 21$। ক্ষেত্রফল $= \\sqrt{21(21-13)(21-14)(21-15)} = \\sqrt{21 \\times 8 \\times 7 \\times 6} = 84$ বর্গ একক। মুখস্থ রাখুন!",
                "explanation": "হেরনের সূত্র প্রয়োগে $\\Delta = \\sqrt{21 \\times 8 \\times 7 \\times 6} = 84$ বর্গ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_18",
                "stem": "$\\frac{1 - \\cos 2\\theta}{\\sin 2\\theta}$ এর সরলীকৃত মান কোনটি?",
                "options": [
                    "$\\tan\\theta$",
                    "$\\cot\\theta$",
                    "$\\sin\\theta$",
                    "$\\tan 2\\theta$"
                ],
                "answer": "A",
                "type_ref": "Type 1: গুণিতক কোণের সরলীকরণ",
                "trap_alert": "লবে $2\\sin^2\\theta$ এবং হরে $2\\sin\\theta\\cos\\theta$ কাটাকাটি ভুল করা।",
                "speed_hack": "$\\frac{2\\sin^2\\theta}{2\\sin\\theta\\cos\\theta} = \\frac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta$। ২ সেকেন্ডে সমাধান!",
                "explanation": "লবে $1 - \\cos 2\\theta = 2\\sin^2\\theta$ ও হরে $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$ বসালে $\\tan\\theta$ পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_19",
                "stem": "$\\cos 105^\\circ$ এর মান কোনটি?",
                "options": [
                    "$\\frac{\\sqrt{2} - \\sqrt{6}}{4}$",
                    "$\\frac{\\sqrt{6} - \\sqrt{2}}{4}$",
                    "$\\frac{\\sqrt{6} + \\sqrt{2}}{4}$",
                    "$-\\frac{\\sqrt{2} + \\sqrt{6}}{4}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: যৌগিক কোণ ($60^\\circ + 45^\\circ$)",
                "trap_alert": "$105^\\circ$ ২য় চতুর্ভাগে থাকায় কসের মান ঋণাত্মক হবে: $\\frac{\\sqrt{2}-\\sqrt{6}}{4} < 0$!",
                "speed_hack": "$\\cos(60^\\circ + 45^\\circ) = \\cos 60^\\circ\\cos 45^\\circ - \\sin 60^\\circ\\sin 45^\\circ = \\frac{1}{2\\sqrt{2}} - \\frac{\\sqrt{3}}{2\\sqrt{2}} = \\frac{1-\\sqrt{3}}{2\\sqrt{2}} = \\frac{\\sqrt{2}-\\sqrt{6}}{4}$।",
                "explanation": "কসের যৌগিক কোণের সূত্রে মান $\\frac{\\sqrt{2}-\\sqrt{6}}{4}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_07_20",
                "stem": "$\\triangle ABC$-তে $\\cos^2 A + \\cos^2 B + \\cos^2 C + 2\\cos A \\cos B \\cos C$ এর মান কত?",
                "options": [
                    "$1$",
                    "$0$",
                    "$2$",
                    "$-1$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সমকোণী ত্রিভুজ অ্যাঙ্গেল সাবস্টিটিউশন ট্রিক (DU Speed-Hack)",
                "trap_alert": "দীর্ঘ ত্রিকোণমিতিক প্রমাণের পেছনে সময় নষ্ট করা।",
                "speed_hack": "সমকোণী ত্রিভুজ অ্যাঙ্গেল সাবস্টিটিউশন ট্রিক: $A = 90^\\circ, B = 60^\\circ, C = 30^\\circ$ ধরলে $\\cos 90^\\circ = 0$! রাশিটি দাঁড়ায় $0 + \\cos^2 60^\\circ + \\cos^2 30^\\circ + 0 = 0 + \\frac{1}{4} + \\frac{3}{4} = 1$! ২ সেকেন্ডে ম্যাজিক সমাধান!",
                "explanation": "যেকোনো ত্রিভুজের জন্য $\\cos^2 A + \\cos^2 B + \\cos^2 C + 2\\cos A \\cos B \\cos C = 1$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    },
    {
        "chapter_id": "math_1st_08",
        "chapter_title": "ফাংশন ও ফাংশনের লেখচিত্র (Functions & Graphs)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০৮",
        "predictors": [
            {
                "id": "pred_math_1st_08_01",
                "stem": "$f(x) = \\sqrt{16 - x^2}$ ফাংশনটির ডোমেন (Domain) কোনটি?",
                "options": [
                    "$[-4, 4]$",
                    "$(-4, 4)$",
                    "$[0, 4]$",
                    "$(0, \\infty)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বাস্তব ফাংশনের ডোমেন নির্ণয়",
                "trap_alert": "খোলা ব্যবধি $(-4, 4)$ এর সাথে বদ্ধ ব্যবধি $[-4, 4]$ এর প্যাঁচ লাগানো। রুটের ভেতর শূন্য গ্রাহ্য!",
                "speed_hack": "রুটের ভেতরের অংশ $\\ge 0 \\implies 16 - x^2 \\ge 0 \\implies x^2 \\le 16 \\implies -4 \\le x \\le 4$। বদ্ধ ব্যবধি $[-4, 4]$।",
                "explanation": "বাস্তব মানের জন্য $16 - x^2 \\ge 0 \\implies x \\in [-4, 4]$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_02",
                "stem": "$f(x) = \\sqrt{9 - x^2}$ ফাংশনটির রেঞ্জ (Range) কোনটি?",
                "options": [
                    "$[0, 3]$",
                    "$[-3, 3]$",
                    "$[0, 9]$",
                    "$(0, 3)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বর্গমূল ফাংশনের রেঞ্জ নির্ণয়",
                "trap_alert": "রেঞ্জকে $[-3, 3]$ দাগানো! মূলসূচক বর্গমূল চিহ্ন সর্বদা অঋণাত্মক মান দেয়, তাই সর্বনিম্ন মান $0$ এবং সর্বোচ্চ মান $3$!",
                "speed_hack": "বর্গমূলের সর্বনিম্ন মান $0$ (যখন $x = \\pm 3$) এবং সর্বোচ্চ মান $\\sqrt{9} = 3$ (যখন $x = 0$)। রেঞ্জ $[0, 3]$।",
                "explanation": "যেহেতু বর্গমূলের মান ঋণাত্মক হতে পারে না এবং সর্বোচ্চ মান ৩, তাই রেঞ্জ $[0, 3]$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_03",
                "stem": "$f(x) = \\frac{2x - 3}{x + 4}$ হলে $f^{-1}(x)$ এর মান কোনটি?",
                "options": [
                    "$\\frac{4x + 3}{2 - x}$",
                    "$\\frac{4x - 3}{x - 2}$",
                    "$\\frac{2x + 4}{x - 3}$",
                    "$\\frac{-4x - 3}{x - 2}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ভগ্নাংশ ফাংশনের বিপরীত ফাংশন ($f^{-1}$)",
                "trap_alert": "চিহ্ন পরিবর্তনের শর্টকাট সূত্র মনে না রাখা।",
                "speed_hack": "শর্টকাট: $f(x) = \\frac{ax+b}{cx+d} \\implies f^{-1}(x) = \\frac{-dx+b}{cx-a}$। এখানে $\\frac{-4x - 3}{x - 2} = \\frac{4x + 3}{2 - x}$। ৩ সেকেন্ডে সমাধান!",
                "explanation": "বিপরীত ফাংশন নির্ণয়ের শর্টকাট সূত্রে মান বসিয়ে পাওয়া যায় $\\frac{4x+3}{2-x}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_04",
                "stem": "$f(x) = \\frac{3x + 1}{2x - 5}$ ফাংশনটির রেঞ্জ (Range) কোনটি?",
                "options": [
                    "$\\mathbb{R} \\setminus \\{3/2\\}$",
                    "$\\mathbb{R} \\setminus \\{5/2\\}$",
                    "$\\mathbb{R} \\setminus \\{-1/3\\}$",
                    "$\\mathbb{R}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: মূলদ ভগ্নাংশের রেঞ্জ",
                "trap_alert": "ডোমেন ($x \\ne 5/2$) এর সাথে রেঞ্জ ($y \\ne 3/2$) গুলিয়ে ফেলা।",
                "speed_hack": "মূলদ ফাংশন $\\frac{ax+b}{cx+d}$ এর রেঞ্জ সর্বদা $\\mathbb{R} \\setminus \\{a/c\\}$। এখানে $a/c = 3/2$। রেঞ্জ $\\mathbb{R} \\setminus \\{3/2\\}$।",
                "explanation": "বিপরীত ফাংশনের ডোমেনই মূল ফাংশনের রেঞ্জ, যা $\\mathbb{R} \\setminus \\{3/2\\}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_05",
                "stem": "$f(x) = \\ln(x - 3)$ ফাংশনটির ডোমেন কোনটি?",
                "options": [
                    "$(3, \\infty)$",
                    "$[3, \\infty)$",
                    "$\\mathbb{R} \\setminus \\{3\\}$",
                    "$(0, \\infty)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: লগারিদমিক ফাংশনের ডোমেন",
                "trap_alert": "লগ এর ইনপুট শূন্য হতে পারে না, তাই ৩ এ খোলা ব্যবধি $(3, \\infty)$ হবে, $[3, \\infty)$ নয়!",
                "speed_hack": "লগ এর আর্গুমেন্ট সর্বদা ধনাত্মক: $x - 3 > 0 \\implies x > 3 \\implies (3, \\infty)$।",
                "explanation": "লগারিদম কেবল ধনাত্মক বাস্তব সংখ্যার জন্য সংজ্ঞায়িত হওয়ায় ডোমেন $(3, \\infty)$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_06",
                "stem": "যদি $f(x) = 2x + 3$ এবং $g(x) = x^2 - 1$ হয়, তবে $(f \\circ g)(2)$ এর মান কত?",
                "options": [
                    "$9$",
                    "$7$",
                    "$15$",
                    "$11$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সংযোজিত ফাংশন (Composite Function)",
                "trap_alert": "$(g \\circ f)(2)$ এর সাথে উল্টো হিসাব করা।",
                "speed_hack": "আগে $g(2) = 2^2 - 1 = 3$। এরপর $f(3) = 2(3) + 3 = 9$। মুখে মুখে হিসাব!",
                "explanation": "$(f \\circ g)(2) = f(g(2)) = f(3) = 2(3) + 3 = 9$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_07",
                "stem": "$f(x) = \\frac{x}{|x|}$ (যেখানে $x \\ne 0$) ফাংশনটির রেঞ্জ কোনটি?",
                "options": [
                    "$\\{-1, 1\\}$",
                    "$[-1, 1]$",
                    "$(-1, 1)$",
                    "$\\mathbb{R}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: চিহ্ন ফাংশন (Signum Function) এর রেঞ্জ",
                "trap_alert": "ব্যবধি $[-1, 1]$ দাগানো। এটি ব্যবধি নয়, শুধুমাত্র দুটি পৃথক উপাদান $\\{-1, 1\\}$!",
                "speed_hack": "$x > 0$ হলে $x/x = 1$; $x < 0$ হলে $x/(-x) = -1$। রেঞ্জ সেটে কেবল $\\{-1, 1\\}$ থাকে।",
                "explanation": "ফাংশনটির আউটপুট কেবল ১ অথবা -১ হতে পারে, তাই রেঞ্জ $\\{-1, 1\\}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_08",
                "stem": "নিচের কোন ফাংশনটি একটি যুগল (Even) ফাংশন?",
                "options": [
                    "$f(x) = \\cos x$",
                    "$f(x) = \\sin x$",
                    "$f(x) = x^3$",
                    "$f(x) = e^x$"
                ],
                "answer": "A",
                "type_ref": "Type 1: যুগল ও অযুগল ফাংশন",
                "trap_alert": "$e^x$ কোনোটিই নয়! যুগল ফাংশনে $f(-x) = f(x)$ হতে হবে।",
                "speed_hack": "$\\cos(-x) = \\cos x = f(x) \\implies$ এটি একটি যুগল (Even) ফাংশন। এর লেখচিত্র $y$-অক্ষের সাপেক্ষে প্রতিসম।",
                "explanation": "যুগল ফাংশনের শর্ত $f(-x) = f(x)$, যা $\\cos x$ সিদ্ধ করে।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_09",
                "stem": "$f(x) = \\sin(4x)$ ফাংশনটির পর্যায়কাল (Period) কত?",
                "options": [
                    "$\\frac{\\pi}{2}$",
                    "$\\pi$",
                    "$2\\pi$",
                    "$\\frac{\\pi}{4}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: পর্যায়বৃত্ত ফাংশন ও পর্যায়কাল",
                "trap_alert": "সরাসরি $2\\pi$ দাগানো। চলকের সহগ দিয়ে ভাগ করতে হবে!",
                "speed_hack": "$\\sin(kx)$ এর পর্যায়কাল $= \\frac{2\\pi}{|k|} = \\frac{2\\pi}{4} = \\frac{\\pi}{2}$।",
                "explanation": "ত্রিকোণমিতিক সাইন ফাংশনের মৌলিক পর্যায় $2\\pi$ কে $x$ এর সহগ ৪ দিয়ে ভাগ করলে পর্যায়কাল $\\pi/2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_10",
                "stem": "$f(x) = 3x - 5$ হলে $f^{-1}(4)$ এর মান কত?",
                "options": [
                    "$3$",
                    "$7$",
                    "$1$",
                    "$\\frac{1}{7}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ফাস্ট ইনভার্স মান নির্ণয় (DU Speed-Hack)",
                "trap_alert": "আগে সম্পূর্ণ ইনভার্স ফাংশন $f^{-1}(x)$ সমীকরণ বের করতে গিয়ে অতিরিক্ত সময় নষ্ট করা।",
                "speed_hack": "ফাস্ট ইনভার্স ট্রিক: সমীকরণ উল্টো করে ইনভার্স ফাংশন না বের করে সরাসরি $f(x) = 4$ বসিয়ে সমাধান করুন: $3x - 5 = 4 \\implies 3x = 9 \\implies x = 3$! ৩ সেকেন্ডে সমাধান!",
                "explanation": "$f^{-1}(4) = x \\implies f(x) = 4 \\implies 3x - 5 = 4 \\implies 3x = 9 \\implies x = 3$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_11",
                "stem": "$f(x) = \\frac{1}{\\sqrt{4 - x^2}}$ ফাংশনটির বাস্তব ডোমেন (Domain) কোনটি?",
                "options": [
                    "$(-2, 2)$",
                    "$[-2, 2]$",
                    "$(-\\infty, -2) \\cup (2, \\infty)$",
                    "$[0, 2)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ভগ্নাংশ মূলের ডোমেন ও সাইন অল্টারনেশন (DU Speed-Hack)",
                "trap_alert": "হর শূন্য হতে পারে না, তাই খোলা ব্যবধি $(-2, 2)$ হবে, বন্ধ ব্যবধি $[-2, 2]$ নয়!",
                "speed_hack": "ভগ্নাংশ মূলের ডোমেন ও সাইন অল্টারনেশন: হরের বর্গমূলের ভেতর $4 - x^2 > 0 \\implies x^2 < 4 \\implies -2 < x < 2$ (খোলা ব্যবধি $(-2, 2)$)। হর শূন্য হতে পারে না তাই প্রান্তবিন্দু বাদ!",
                "explanation": "বাস্তব মানের জন্য $4 - x^2 > 0 \\implies x^2 < 4 \\implies -2 < x < 2$ বা ডোমেন $(-2, 2)$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_12",
                "stem": "যদি $f: \\mathbb{R} \\to \\mathbb{R}$ হয় এবং $f(x) = x^3$ হয়, তবে ফাংশনটি:",
                "options": [
                    "এক-এক এবং সার্বিক (Bijective)",
                    "এক-এক কিন্তু সার্বিক নয়",
                    "সার্বিক কিন্তু এক-এক নয়",
                    "এক-এক বা সার্বিক কোনোটিই নয়"
                ],
                "answer": "A",
                "type_ref": "Type 2: এক-এক ও সার্বিক ফাংশন",
                "trap_alert": "$f(x) = x^2$ হলে এক-এক হতো না, কিন্তু $x^3$ বিজোড় ঘাত হওয়ায় এটি এক-এক ও সার্বিক উভয়ই!",
                "speed_hack": "বিজোড় ঘাত $x^3$ সর্বদা এক-এক এবং প্রতিটি বাস্তব সংখ্যার জন্য একটি বাস্তব ঘনমূল থাকায় সার্বিক।",
                "explanation": "প্রতিটি ভিন্ন ইনপুটের জন্য ভিন্ন আউটপুট এবং রেঞ্জ $\\mathbb{R}$ যা কোডোমেনের সমান, তাই এটি বাইজেক্টিভ।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_13",
                "stem": "$f(x) = |\\sin x|$ ফাংশনটির মৌলিক পর্যায়কাল (Fundamental Period) কত?",
                "options": [
                    "$\\pi$",
                    "$2\\pi$",
                    "$\\frac{\\pi}{2}$",
                    "$4\\pi$"
                ],
                "answer": "A",
                "type_ref": "Type 1: মডুলাস ত্রিকোণমিতিক ফাংশনের পর্যায়",
                "trap_alert": "সাধারণ সাইনের পর্যায়কাল $2\\pi$ ভাবা। পরমমান নিলে ঋণাত্মক অংশ উপরে উঠে এসে পর্যায় অর্ধেক হয়ে যায়!",
                "speed_hack": "পরমমান নিলে সাইন ও কসের পর্যায়কাল $2\\pi$ থেকে কমে $\\pi$ হয়ে যায়।",
                "explanation": "$|\\sin(x + \\pi)| = |-\\sin x| = |\\sin x|$, ফলে পর্যায়কাল $\\pi$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_14",
                "stem": "$f(x) = \\sin^{-1}(2x - 1)$ ফাংশনটির ডোমেন কোনটি?",
                "options": [
                    "$[0, 1]$",
                    "$[-1, 1]$",
                    "$[0, 2]$",
                    "$[-1/2, 1/2]$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বিপরীত বৃত্তীয় ফাংশনের ডোমেন",
                "trap_alert": "$-1 \\le 2x - 1 \\le 1$ অসমতা সমাধান করার সময় ভুল করা।",
                "speed_hack": "$-1 \\le 2x - 1 \\le 1 \\implies 0 \\le 2x \\le 2 \\implies 0 \\le x \\le 1$। ডোমেন $[0, 1]$।",
                "explanation": "ইনভার্স সাইনের আর্গুমেন্ট $-1$ থেকে $1$ এর মধ্যে থাকে, সমাধান করলে $x \\in [0, 1]$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_15",
                "stem": "যদি $f(x) = x^2 + 4$ হয়, তবে এর রেঞ্জ (Range) কোনটি?",
                "options": [
                    "$[4, \\infty)$",
                    "$(4, \\infty)$",
                    "$[0, \\infty)$",
                    "$\\mathbb{R}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: দ্বিঘাত ফাংশনের রেঞ্জ",
                "trap_alert": "$x^2 \\ge 0$ এর সাথে ৪ যোগ করতে ভুলে $[0, \\infty)$ দাগানো।",
                "speed_hack": "$x^2 \\ge 0 \\implies x^2 + 4 \\ge 4$। সর্বনিম্ন মান ৪, সর্বোচ্চ $\\infty$। রেঞ্জ $[4, \\infty)$।",
                "explanation": "যেহেতু $x^2$ এর সর্বনিম্ন মান শূন্য, তাই $f(x)$ এর সর্বনিম্ন মান ৪।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_16",
                "stem": "নিচের কোন ফাংশনটি একটি অযুগল (Odd) ফাংশন?",
                "options": [
                    "$f(x) = x^3 - \\sin x$",
                    "$f(x) = x^2 + \\cos x$",
                    "$f(x) = |x|$",
                    "$f(x) = 5$"
                ],
                "answer": "A",
                "type_ref": "Type 1: অযুগল ফাংশনের শর্ত",
                "trap_alert": "অযুগল ফাংশনের শর্ত $f(-x) = -f(x)$।",
                "speed_hack": "$f(-x) = (-x)^3 - \\sin(-x) = -x^3 + \\sin x = -(x^3 - \\sin x) = -f(x)$। এটি অযুগল!",
                "explanation": "$f(-x) = -f(x)$ হওয়ায় ফাংশনটি অযুগল এবং মূলবিন্দুর সাপেক্ষে প্রতিসম।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_17",
                "stem": "যদি $f(x) = \\frac{x}{1 + |x|}$ হয়, তবে ফাংশনটির রেঞ্জ কোনটি?",
                "options": [
                    "$(-1, 1)$",
                    "$[-1, 1]$",
                    "$\\mathbb{R}$",
                    "$[0, 1)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বিশেষ পরমমান ফাংশনের সীমা ও রেঞ্জ",
                "trap_alert": "মান কখনো $\\pm 1$ এর সমান হতে পারে না, কেবল নিকটবর্তী হয়। তাই খোলা ব্যবধি $(-1, 1)$!",
                "speed_hack": "$x \\to \\infty$ হলে মান $\\to 1$ এবং $x \\to -\\infty$ হলে মান $\\to -1$। কিন্তু কখনোই $\\pm 1$ ছোঁবে না। রেঞ্জ $(-1, 1)$।",
                "explanation": "লবের পরমমান হরের চেয়ে সর্বদা ছোট, তাই আউটপুট কঠোরভাবে $-1 < y < 1$ ব্যবধিতে সীমাবদ্ধ।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_18",
                "stem": "যদি $f(x + y) = f(x) f(y)$ এবং $f(1) = 3$ হয়, তবে $f(4)$ এর মান কত?",
                "options": [
                    "$81$",
                    "$12$",
                    "$27$",
                    "$64$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ফাংশনাল সমীকরণ (Functional Equation)",
                "trap_alert": "রৈখিক ফাংশন ভেবে $3 \\times 4 = 12$ দাগানো। এটি সূচকীয় ফাংশন $f(x) = a^x$!",
                "speed_hack": "$f(x+y) = f(x)f(y) \\implies f(x) = a^x$। $f(1) = 3 \\implies a = 3$। সুতরাং $f(4) = 3^4 = 81$। ৩ সেকেন্ডে সমাধান!",
                "explanation": "সূচকীয় ধর্মের ফাংশনাল সমীকরণ অনুসারে $f(x) = 3^x \\implies f(4) = 3^4 = 81$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_19",
                "stem": "$f(x) = \\sqrt{x^2 - 5x + 6}$ ফাংশনটির বাস্তব ডোমেন (Domain) কোনটি?",
                "options": [
                    "$(-\\infty, 2] \\cup [3, \\infty)$",
                    "$[2, 3]$",
                    "$(2, 3)$",
                    "$(-\\infty, 2) \\cup (3, \\infty)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: দ্বিপদী দ্বিঘাত মূলের ডোমেন ও অঞ্চল সাইন পদ্ধতি (DU Speed-Hack)",
                "trap_alert": "অসমতায় $\\ge 0$ থাকলে বাইরের অঞ্চল হয়, ভেতরের অঞ্চল নয়।",
                "speed_hack": "নাম্বার লাইন সাইন অল্টারনেশন ট্রিক: $(x-2)(x-3) \\ge 0$। যেহেতু অসমতায় $\\ge 0$ (বৃহত্তর), সমাধান হবে প্রান্তিক দুই বাইরের অঞ্চল ($x \\le 2$ অথবা $x \\ge 3$), অর্থাৎ $(-\\infty, 2] \\cup [3, \\infty)$! মাঝের অঞ্চল $[2, 3]$ হতো যদি $< 0$ থাকতো!",
                "explanation": "বর্গমূলের ভেতরের রাশি অশূন্য বা অঋণাত্মক হতে হবে: $x^2 - 5x + 6 \\ge 0 \\implies (x-2)(x-3) \\ge 0 \\implies x \\le 2$ অথবা $x \\ge 3$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_08_20",
                "stem": "$f(x) = x^2$ ফাংশনটি $f: \\mathbb{R} \\to [0, \\infty)$ হলে ফাংশনটি:",
                "options": [
                    "সার্বিক কিন্তু এক-এক নয়",
                    "এক-এক এবং সার্বিক",
                    "এক-এক কিন্তু সার্বিক নয়",
                    "কোনোটিই নয়"
                ],
                "answer": "A",
                "type_ref": "Type 2: এক-এক ও সার্বিক ফাংশন",
                "trap_alert": "ডোমেন $\\mathbb{R}$ হওয়ায় $f(-2) = f(2) = 4$, ফলে এটি এক-এক নয়। তবে কোডোমেন $[0, \\infty)$ রেঞ্জের সমান হওয়ায় সার্বিক!",
                "speed_hack": "ঋণাত্মক ও ধনাত্মক মানে একই আউটপুট $\\implies$ এক-এক নয়। কিন্তু আউটপুট কোডোমেনকে পূর্ণ করে $\\implies$ সার্বিক।",
                "explanation": "ভিন্ন ইনপুটের জন্য একই আউটপুট থাকায় এক-এক নয়, তবে রেঞ্জ ও কোডোমেন সমান হওয়ায় সার্বিক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    },
    {
        "chapter_id": "math_1st_09",
        "chapter_title": "অন্তরীকরণ (Differentiation)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০৯",
        "predictors": [
            {
                "id": "pred_math_1st_09_01",
                "stem": "$\\lim_{x \\to 0} \\frac{\\sin 3x}{\\tan^{-1} 2x}$ এর মান কত?",
                "options": [
                    "$\\frac{3}{2}$",
                    "$\\frac{2}{3}$",
                    "$1$",
                    "$6$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ত্রিকোণমিতিক লিমিট সহগ অনুপাত শর্টকাট (DU Speed-Hack)",
                "trap_alert": "ব্যস্তানুপাতিক ভেবে $2/3$ দাগানো। লব ও হরের চলকের সহগের সরাসরি ভাগফল হয়।",
                "speed_hack": "ত্রিকোণমিতিক লিমিট শর্টকাট: $\\lim_{x \\to 0} \\frac{\\sin ax}{\\tan^{-1} bx} = \\frac{a}{b}$। এখানে $a = 3, b = 2$, তাই মান $\\frac{3}{2}$! সরাসরি ১ সেকেন্ডে টিক!",
                "explanation": "$\\lim_{x \\to 0} \\frac{\\sin 3x}{\\tan^{-1} 2x} = \\frac{3}{2} \\times \\lim \\frac{\\sin 3x}{3x} \\times \\frac{2x}{\\tan^{-1} 2x} = \\frac{3}{2}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_02",
                "stem": "$\\lim_{x \\to 0} \\frac{1 - \\cos 4x}{x^2}$ এর মান কত?",
                "options": [
                    "$8$",
                    "$4$",
                    "$16$",
                    "$2$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ত্রিকোণমিতিক লিমিট শর্টকাট",
                "trap_alert": "শর্টকাটে বর্গ করতে ভুলে গিয়ে শুধু ৪ বা ২ দাগানো।",
                "speed_hack": "সুপার শর্টকাট: $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$। এখানে $k = 4$, তাই $\\frac{4^2}{2} = \\frac{16}{2} = 8$।",
                "explanation": "ত্রিকোণমিতিক সূত্র $2\\sin^2 2x$ ব্যবহার করে অথবা L'Hôpital প্রয়োগে মান পাওয়া যায় ৮।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_03",
                "stem": "$\\lim_{x \\to \\infty} \\left(1 + \\frac{3}{x}\\right)^x$ এর মান কোনটি?",
                "options": [
                    "$e^3$",
                    "$e$",
                    "$e^{-3}$",
                    "$\\infty$"
                ],
                "answer": "A",
                "type_ref": "Type 1: অসীমে সূচকীয় লিমিট",
                "trap_alert": "$1^\\infty = 1$ ভেবে সরাসরি ১ দাগানো। এটি অনির্ণেয় আকার!",
                "speed_hack": "স্ট্যান্ডার্ড শর্টকাট: $\\lim_{x \\to \\infty} \\left(1 + \\frac{k}{x}\\right)^x = e^k$। এখানে $k = 3$, তাই সরাসরি $e^3$।",
                "explanation": "প্রমিত লিমিট সূত্র মতে $\\lim_{x \\to \\infty}(1 + k/x)^x = e^k = e^3$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_04",
                "stem": "$y = x^x$ হলে $\\frac{dy}{dx}$ এর মান কোনটি?",
                "options": [
                    "$x^x(1 + \\ln x)$",
                    "$x \\cdot x^{x-1}$",
                    "$x^x \\ln x$",
                    "$x^x(1 - \\ln x)$"
                ],
                "answer": "A",
                "type_ref": "Type 2: লগারিদমিক অন্তরীকরণ",
                "trap_alert": "$x^n$ এর মতো করে $x \\cdot x^{x-1} = x^x$ দাগানো। ঘাতে চলক থাকলে লগ নিতে হয়!",
                "speed_hack": "চলকের ওপর চলক ডেরিভেটিভ মুখস্থ রাখুন: $\\frac{d}{dx}(x^x) = x^x(1 + \\ln x)$।",
                "explanation": "$\\ln y = x\\ln x \\implies \\frac{1}{y}\\frac{dy}{dx} = 1 + \\ln x \\implies \\frac{dy}{dx} = x^x(1 + \\ln x)$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_05",
                "stem": "$f(x) = 2x^3 - 9x^2 + 12x + 5$ ফাংশনটির গুরুমান (Maximum value) কত?",
                "options": [
                    "$10$",
                    "$9$",
                    "$5$",
                    "$12$"
                ],
                "answer": "A",
                "type_ref": "Type 3: গুরুমান ও লঘুমান (Maxima & Minima)",
                "trap_alert": "যে বিন্দুতে চরম মান পাওয়া যায় ($x = 1$), তাকেই উত্তর ভাবা। ফাংশনে মান বসিয়ে চরম মান বের করতে হয়!",
                "speed_hack": "$f'(x) = 6x^2 - 18x + 12 = 0 \\implies x^2 - 3x + 2 = 0 \\implies x = 1, 2$। $f''(1) < 0$, তাই $x = 1$ এ গুরুমান $= 2(1) - 9(1) + 12(1) + 5 = 10$।",
                "explanation": "$x = 1$ বিন্দুতে $f''(1) = -6 < 0$ হওয়ায় গুরুমান বিদ্যমান এবং মান $f(1) = 10$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_06",
                "stem": "$y = x^2 - 4x + 3$ বক্ররেখার $(1, 0)$ বিন্দুতে স্পর্শকের ঢাল কত?",
                "options": [
                    "$-2$",
                    "$2$",
                    "$0$",
                    "$-4$"
                ],
                "answer": "A",
                "type_ref": "Type 2: স্পর্শকের ঢাল নির্ণয়",
                "trap_alert": "অন্তরীকরণ করার পর চিহ্নে ভুল করে $+2$ দাগানো।",
                "speed_hack": "ঢাল $m = \\left.\\frac{dy}{dx}\\right|_{(1, 0)} = 2x - 4 = 2(1) - 4 = -2$। ২ সেকেন্ডে সমাধান!",
                "explanation": "$dy/dx = 2x - 4$। $(1, 0)$ বিন্দুতে ঢাল $m = 2(1) - 4 = -2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_07",
                "stem": "$y = \\tan^{-1}\\left(\\frac{2x}{1 - x^2}\\right)$ হলে $\\frac{dy}{dx}$ এর মান কোনটি?",
                "options": [
                    "$\\frac{2}{1 + x^2}$",
                    "$\\frac{1}{1 + x^2}$",
                    "$\\frac{2}{1 - x^2}$",
                    "$\\frac{-2}{1 + x^2}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বিপরীত ত্রিকোণমিতিক প্রতিস্থাপন অন্তরীকরণ",
                "trap_alert": "সরাসরি ইনভার্স ট্যানের বড় সূত্রে অন্তরীকরণ করতে গিয়ে ভুল করা।",
                "speed_hack": "ত্রিকোণমিতিক রূপান্তর: $\\tan^{-1}\\left(\\frac{2x}{1-x^2}\\right) = 2\\tan^{-1}x$। সুতরাং $\\frac{d}{dx}(2\\tan^{-1}x) = \\frac{2}{1 + x^2}$।",
                "explanation": "$y = 2\\tan^{-1}x \\implies \\frac{dy}{dx} = \\frac{2}{1+x^2}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_08",
                "stem": "$y = \\sqrt{x + \\sqrt{x + \\sqrt{x + \\dots \\infty}}}$ হলে $\\frac{dy}{dx}$ এর মান কত?",
                "options": [
                    "$\\frac{1}{2y - 1}$",
                    "$\\frac{1}{2y + 1}$",
                    "$\\frac{x}{2y - 1}$",
                    "$\\frac{1}{y - 1}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: অসীম ধারার অন্তরীকরণ",
                "trap_alert": "হরে চিহ্নের ভুল করে $2y + 1$ দাগানো।",
                "speed_hack": "$y = \\sqrt{x + y} \\implies y^2 = x + y$। $x$ এর সাপেক্ষে অন্তরীকরণ: $2y y' = 1 + y' \\implies y'(2y - 1) = 1 \\implies y' = \\frac{1}{2y - 1}$।",
                "explanation": "বর্গ করে অন্তরীকরণ করলে পাই $\\frac{dy}{dx} = \\frac{1}{2y - 1}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_09",
                "stem": "$\\cos x$ এর সাপেক্ষে $\\sin x$ এর অন্তরক সহগ (Derivative) কোনটি?",
                "options": [
                    "$-\\cot x$",
                    "$\\cot x$",
                    "$-\\tan x$",
                    "$\\tan x$"
                ],
                "answer": "A",
                "type_ref": "Type 2: একটি ফাংশনের সাপেক্ষে অপর ফাংশনের অন্তরীকরণ",
                "trap_alert": "মাইনাস চিহ্ন ভুলে গিয়ে $+\\cot x$ দাগানো। $\\frac{d}{dx}(\\cos x) = -\\sin x$!",
                "speed_hack": "$\\frac{d(\\sin x)}{d(\\cos x)} = \\frac{\\cos x dx}{-\\sin x dx} = -\\frac{\\cos x}{\\sin x} = -\\cot x$।",
                "explanation": "$\\frac{dy/dx}{dz/dx} = \\frac{\\cos x}{-\\sin x} = -\\cot x$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_10",
                "stem": "যদি $(1 - x^2)y_2 - x y_1 = 2$ হয়, তবে নিচের কোনটি $y$ এর সঠিক মান?",
                "options": [
                    "$(\\cos^{-1} x)^2$",
                    "$\\cos^{-1} x$",
                    "$\\sin^{-1} x$",
                    "$\\tan^{-1} x$"
                ],
                "answer": "A",
                "type_ref": "Type 1: সাকসেসিভ ডিফারেনশিয়েশন পাওয়ার ট্রিক (DU Speed-Hack)",
                "trap_alert": "ডানপক্ষে শূন্য থাকলে $y = \\cos^{-1}x$ হতো, কিন্তু ডানপক্ষে ২ থাকলে ঘাত ২ হয়!",
                "speed_hack": "ঢাবি সাকসেসিভ ডিফারেনশিয়েশন পাওয়ার ট্রিক: ডানপক্ষে অশূন্য ধ্রুবক $2$ থাকা মানে ইনভার্স ফাংশনের ঘাত ছিল ২! অর্থাৎ $y = (\\cos^{-1}x)^2$। অপশন দেখে ১ সেকেন্ডে নিশ্চিত টিক!",
                "explanation": "$y = (\\cos^{-1}x)^2 \\implies y_1 = 2\\cos^{-1}x \\cdot \\frac{-1}{\\sqrt{1-x^2}} \\implies (1-x^2)y_1^2 = 4y$। পুনরায় অন্তরীকরণ করলে $(1-x^2)y_2 - x y_1 = 2$ পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_11",
                "stem": "বৃত্তের ব্যাসার্ধ $r = 5\\text{ cm}$ হলে এবং ব্যাসার্ধ বৃদ্ধির হার $2\\text{ cm/s}$ হলে এর ক্ষেত্রফল বৃদ্ধির হার কত?",
                "options": [
                    "$20\\pi\\text{ cm}^2\\text{/s}$",
                    "$10\\pi\\text{ cm}^2\\text{/s}$",
                    "$50\\pi\\text{ cm}^2\\text{/s}$",
                    "$25\\pi\\text{ cm}^2\\text{/s}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সময় সাপেক্ষে পরিবর্তনের হার",
                "trap_alert": "বর্গ করে সরাসরি $25 \\times 2$ করা। অন্তরীকরণ করতে হবে: $\\frac{dA}{dt} = 2\\pi r \\frac{dr}{dt}$!",
                "speed_hack": "$A = \\pi r^2 \\implies \\frac{dA}{dt} = 2\\pi r \\frac{dr}{dt} = 2\\pi(5)(2) = 20\\pi\\text{ cm}^2\\text{/s}$।",
                "explanation": "ক্ষেত্রফলের পরিবর্তনের হার $\\frac{dA}{dt} = 2\\pi r \\frac{dr}{dt} = 20\\pi$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_12",
                "stem": "$x^3 + y^3 - 3axy = 0$ বক্ররেখার ক্ষেত্রে $\\frac{dy}{dx}$ এর মান কোনটি?",
                "options": [
                    "$-\\frac{x^2 - ay}{y^2 - ax}$",
                    "$\\frac{x^2 - ay}{y^2 - ax}$",
                    "$-\\frac{y^2 - ax}{x^2 - ay}$",
                    "$-\\frac{x^2 + ay}{y^2 + ax}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: অব্যক্ত ফাংশনের আংশিক অন্তরক শর্টকাট (DU Speed-Hack)",
                "trap_alert": "সূত্রের বাইরের মাইনাস চিহ্ন দিতে ভুলে যাওয়া।",
                "speed_hack": "অব্যক্ত ফাংশনের শর্টকাট: $\\frac{dy}{dx} = -\\frac{\\partial f / \\partial x}{\\partial f / \\partial y} = -\\frac{3x^2 - 3ay}{3y^2 - 3ax} = -\\frac{x^2 - ay}{y^2 - ax}$! ৩ সেকেন্ডে সমাধান!",
                "explanation": "অব্যক্ত ফাংশনের অন্তরক নির্ণয়ে $\\frac{dy}{dx} = -\\frac{f_x}{f_y} = -\\frac{3x^2 - 3ay}{3y^2 - 3ax} = -\\frac{x^2 - ay}{y^2 - ax}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_13",
                "stem": "ফাংশন $f(x) = x(1 - x)$ এর সর্বোচ্চ মান কত?",
                "options": [
                    "$\\frac{1}{4}$",
                    "$\\frac{1}{2}$",
                    "$1$",
                    "$0$"
                ],
                "answer": "A",
                "type_ref": "Type 3: চরম মান নির্ণয়",
                "trap_alert": "যে বিন্দুতে চরম মান পাওয়া যায় ($x = 1/2$), তাকেই উত্তর ভাবা। মান বের করতে হবে: $(1/2)(1/2) = 1/4$!",
                "speed_hack": "দুটি রাশির যোগফল ধ্রুবক ($x + (1-x) = 1$) হলে তাদের গুণফল সর্বোচ্চ হয় যখন তারা সমান হয়: $x = 1/2 \\implies$ সর্বোচ্চ মান $1/4$।",
                "explanation": "$f'(x) = 1 - 2x = 0 \\implies x = 1/2$। সর্বোচ্চ মান $f(1/2) = (1/2)(1 - 1/2) = 1/4$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_14",
                "stem": "$\\lim_{x \\to 0} \\frac{\\ln(1 + 5x)}{x}$ এর মান কত?",
                "options": [
                    "$5$",
                    "$1$",
                    "$\\frac{1}{5}$",
                    "$0$"
                ],
                "answer": "A",
                "type_ref": "Type 1: L'Hôpital ট্রিগার ও স্ট্যান্ডার্ড লিমিট (DU Speed-Hack)",
                "trap_alert": "সহগ ৫ কে উপেক্ষা করে ১ দাগানো।",
                "speed_hack": "L'Hôpital ট্রিগার ($0/0$ আকার): লব ও হরকে অন্তরীকরণ করলে $\\frac{5/(1+5x)}{1} \\to 5$। ১ সেকেন্ডে উত্তর!",
                "explanation": "$\\lim_{x \\to 0} \\frac{\\ln(1 + 5x)}{5x} \\times 5 = 1 \\times 5 = 5$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_15",
                "stem": "$y = x^3 - 3x$ বক্ররেখার যে বিন্দুতে স্পর্শক $x$-অক্ষের সমান্তরাল, তার স্থানাঙ্ক কোনটি?",
                "options": [
                    "$(1, -2)$ এবং $(-1, 2)$",
                    "$(0, 0)$",
                    "$(1, 2)$ এবং $(-1, -2)$",
                    "$(3, 0)$"
                ],
                "answer": "A",
                "type_ref": "Type 2: স্পর্শক সমান্তরাল হওয়ার শর্ত",
                "trap_alert": "$x$-অক্ষের সমান্তরাল মানে ঢাল শূন্য ($dy/dx = 0$)।",
                "speed_hack": "$\\frac{dy}{dx} = 3x^2 - 3 = 0 \\implies x^2 = 1 \\implies x = \\pm 1$। $x=1$ হলে $y = -2$; $x=-1$ হলে $y = 2$।",
                "explanation": "$dy/dx = 0 \\implies 3(x^2 - 1) = 0 \\implies x = \\pm 1$। বিন্দুদ্বয় $(1, -2)$ ও $(-1, 2)$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_16",
                "stem": "যদি $y = \\log_x 10$ হয়, তবে $\\frac{dy}{dx}$ এর মান কোনটি?",
                "options": [
                    "$-\\frac{\\ln 10}{x(\\ln x)^2}$",
                    "$\\frac{1}{x\\ln 10}$",
                    "$\\frac{\\ln 10}{x}$",
                    "$-\\frac{1}{x(\\ln x)^2}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বেস পরিবর্তন করে অন্তরীকরণ",
                "trap_alert": "চলক বেসে থাকলে সরাসরি $\\frac{1}{x\\ln 10}$ দাগানো মারাত্মক ভুল! বেস পরিবর্তন করতে হবে!",
                "speed_hack": "$y = \\frac{\\ln 10}{\\ln x} = \\ln 10 (\\ln x)^{-1} \\implies y' = \\ln 10 \\cdot (-1)(\\ln x)^{-2} \\cdot \\frac{1}{x} = -\\frac{\\ln 10}{x(\\ln x)^2}$।",
                "explanation": "বেস পরিবর্তন সূত্র $y = \\frac{\\ln 10}{\\ln x}$ প্রয়োগ করে অন্তরীকরণ করলে উত্তর পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_17",
                "stem": "$y = \\sqrt{\\sin x}$ হলে $\\frac{dy}{dx}$ এর মান কত?",
                "options": [
                    "$\\frac{\\cos x}{2\\sqrt{\\sin x}}$",
                    "$\\frac{1}{2\\sqrt{\\sin x}}$",
                    "$\\frac{-\\cos x}{2\\sqrt{\\sin x}}$",
                    "$\\frac{\\cos x}{\\sqrt{\\sin x}}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: চেইন রুল (Chain Rule)",
                "trap_alert": "ভেতরের $\\sin x$ কে অন্তরীকরণ করতে ভুলে যাওয়া।",
                "speed_hack": "$\\frac{d}{dx}(\\sqrt{u}) = \\frac{u'}{2\\sqrt{u}} = \\frac{\\cos x}{2\\sqrt{\\sin x}}$।",
                "explanation": "চেইন রুল অনুসারে $\\frac{1}{2\\sqrt{\\sin x}} \\times \\frac{d}{dx}(\\sin x) = \\frac{\\cos x}{2\\sqrt{\\sin x}}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_18",
                "stem": "যদি $x = a\\cos^3\\theta$ এবং $y = a\\sin^3\\theta$ হয়, তবে $\\frac{dy}{dx}$ এর মান কত?",
                "options": [
                    "$-\\tan\\theta$",
                    "$\\tan\\theta$",
                    "$-\\cot\\theta$",
                    "$\\cot\\theta$"
                ],
                "answer": "A",
                "type_ref": "Type 2: পরামিতিক অন্তরীকরণ (Parametric Differentiation)",
                "trap_alert": "চিহ্নে ভুল করা। $\\frac{dx}{d\\theta} = -3a\\cos^2\\theta\\sin\\theta$ এ মাইনাস চিহ্ন থাকে!",
                "speed_hack": "$\\frac{dy/d\\theta}{dx/d\\theta} = \\frac{3a\\sin^2\\theta\\cos\\theta}{-3a\\cos^2\\theta\\sin\\theta} = -\\frac{\\sin\\theta}{\\cos\\theta} = -\\tan\\theta$।",
                "explanation": "পরামিতিক নিয়মে মান $-\\tan\\theta$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_19",
                "stem": "$f(x) = e^x - x$ ফাংশনটির লঘুমান (Minimum value) কত?",
                "options": [
                    "$1$",
                    "$0$",
                    "$e$",
                    "$-1$"
                ],
                "answer": "A",
                "type_ref": "Type 3: চরম মান নির্ণয়",
                "trap_alert": "চরম মান বিন্দু $x = 0$ পেলেও ফাংশনে মান বসাতে হবে: $e^0 - 0 = 1$!",
                "speed_hack": "$f'(x) = e^x - 1 = 0 \\implies e^x = 1 \\implies x = 0$। লঘুমান $f(0) = e^0 - 0 = 1$।",
                "explanation": "$x = 0$ তে $f''(0) = e^0 = 1 > 0$, সুতরাং লঘুমান $f(0) = 1$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_09_20",
                "stem": "$\\lim_{x \\to -\\infty} \\left(\\sqrt{x^2 + 5x} + x\\right)$ এর মান কত?",
                "options": [
                    "$-\\frac{5}{2}$",
                    "$\\frac{5}{2}$",
                    "$5$",
                    "$-5$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ঋণাত্মক অসীম লিমিট ও সাইন ট্র্যাপ (DU Trap-Alert)",
                "trap_alert": "$x < 0$ এর জন্য $\\sqrt{x^2} = |x| = -x$ বিবেচনা না করলে চিহ্নে ভুল হয়ে $+\\frac{5}{2}$ উত্তর আসবে!",
                "speed_hack": "ঋণাত্মক অসীম লিমিট ট্র্যাপ: $x \\to -\\infty$ হলে $x = -t$ (যেখানে $t \\to \\infty$)। $\\sqrt{x^2} = |x| = -x$ বিবেচনায় $\\sqrt{t^2 - 5t} - t = \\frac{-5t}{\\sqrt{t^2 - 5t} + t} \\to -\\frac{5}{2}$। চিহ্নের ট্র্যাপে পড়বেন না!",
                "explanation": "অনুবন্ধী দ্বারা গুণ ও ভাগ করে পাই: $\\frac{(x^2+5x)-x^2}{\\sqrt{x^2+5x}-x} = \\frac{5x}{-x\\sqrt{1+5/x}-x} = \\frac{5}{-2} = -\\frac{5}{2}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    },
    {
        "chapter_id": "math_1st_10",
        "chapter_title": "যোগজীকরণ (Integration)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ১০",
        "predictors": [
            {
                "id": "pred_math_1st_10_01",
                "stem": "$\\int e^x \\left( \\frac{1}{x} - \\frac{1}{x^2} \\right) dx$ এর মান কোনটি?",
                "options": [
                    "$\\frac{e^x}{x} + c$",
                    "$-\\frac{e^x}{x^2} + c$",
                    "$\\frac{e^x}{x^2} + c$",
                    "$e^x \\ln x + c$"
                ],
                "answer": "A",
                "type_ref": "Type 1: $e^x(f(x) + f'(x))$ আদর্শ যোগজ",
                "trap_alert": "কোনটি $f(x)$ আর কোনটি $f'(x)$ তা চিনতে ভুল করা। $\\frac{d}{dx}(1/x) = -1/x^2$!",
                "speed_hack": "শর্টকাট: $\\int e^x(f(x) + f'(x)) dx = e^x f(x) + c$। এখানে $f(x) = 1/x$, তাই উত্তর $\\frac{e^x}{x} + c$।",
                "explanation": "যেহেতু $\\frac{d}{dx}(1/x) = -1/x^2$, তাই আদর্শ সূত্রমতে উত্তর $\\frac{e^x}{x} + c$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_02",
                "stem": "$\\int e^x (\\tan x + \\sec^2 x) dx$ এর মান কত?",
                "options": [
                    "$e^x \\tan x + c$",
                    "$e^x \\sec^2 x + c$",
                    "$e^x \\sec x + c$",
                    "$e^x (\\tan x - \\sec x) + c$"
                ],
                "answer": "A",
                "type_ref": "Type 1: $e^x(f(x) + f'(x))$ আদর্শ যোগজ",
                "trap_alert": "$\\tan x$ এর ডেরিভেটিভ $\\sec^2 x$, তাই উত্তর $e^x f(x)$!",
                "speed_hack": "$f(x) = \\tan x \\implies f'(x) = \\sec^2 x$। সরাসরি $e^x \\tan x + c$।",
                "explanation": "আদর্শ যোগজ সূত্রানুসারে $e^x \\tan x + c$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_03",
                "stem": "$\\int \\frac{2x + 3}{x^2 + 3x + 7} dx$ এর মান কোনটি?",
                "options": [
                    "$\\ln|x^2 + 3x + 7| + c$",
                    "$\\frac{1}{x^2 + 3x + 7} + c$",
                    "$2\\ln|x^2 + 3x + 7| + c$",
                    "$\\sqrt{x^2 + 3x + 7} + c$"
                ],
                "answer": "A",
                "type_ref": "Type 1: হর-লব ডেরিভেটিভ সূত্র $\\int \\frac{f'(x)}{f(x)}dx$",
                "trap_alert": "লবে হরের ডেরিভেটিভ বিদ্যমান থাকলে উত্তর সরাসরি $\\ln|\\text{হর}|$!",
                "speed_hack": "হরের অন্তরক সহগ $\\frac{d}{dx}(x^2 + 3x + 7) = 2x + 3$ লবে উপস্থিত। সুতরাং উত্তর $\\ln|x^2 + 3x + 7| + c$।",
                "explanation": "$\\int \\frac{f'(x)}{f(x)} dx = \\ln|f(x)| + c$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_04",
                "stem": "$\\int_0^{\\pi/2} \\frac{\\sin x}{\\sin x + \\cos x} dx$ এর মান কত?",
                "options": [
                    "$\\frac{\\pi}{4}$",
                    "$\\frac{\\pi}{2}$",
                    "$1$",
                    "$0$"
                ],
                "answer": "A",
                "type_ref": "Type 2: নির্দিষ্ট যোগজের কিং'স প্রোপার্টি (King's Rule)",
                "trap_alert": "নির্দিষ্ট যোগজের কিং প্রোপার্টি প্রয়োগ করলে উত্তর সর্বদা ব্যবধির অর্ধেক $(\\frac{b-a}{2})$ হয়!",
                "speed_hack": "কিং'স রুল শর্টকাট: উত্তর $= \\frac{b - a}{2} = \\frac{\\pi/2 - 0}{2} = \\frac{\\pi}{4}$। ৩ সেকেন্ডে সমাধান!",
                "explanation": "$I = \\int_0^{\\pi/2} \\frac{\\sin x}{\\sin x+\\cos x}dx$ এবং $I = \\int_0^{\\pi/2} \\frac{\\cos x}{\\cos x+\\sin x}dx$ যোগ করলে $2I = \\int_0^{\\pi/2} 1 dx = \\pi/2 \\implies I = \\pi/4$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_05",
                "stem": "$y^2 = 4x$ পরাবৃত্ত এবং $y = x$ সরলরেখা দ্বারা সীমাবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?",
                "options": [
                    "$\\frac{8}{3}$",
                    "$\\frac{16}{3}$",
                    "$\\frac{4}{3}$",
                    "$8$"
                ],
                "answer": "A",
                "type_ref": "Type 3: পরাবৃত্ত ও সরলরেখার আবদ্ধ ক্ষেত্রফল (DU Speed-Hack)",
                "trap_alert": "ইন্টিগ্রেশন করে সীমা বসানোর দরকার নেই, সরাসরি অনুসিদ্ধান্ত ব্যবহার করুন!",
                "speed_hack": "পরাবৃত্ত ও সরলরেখার আবদ্ধ ক্ষেত্রফল শর্টকাট: $y^2 = 4ax$ এবং $y = mx$ এর আবদ্ধ ক্ষেত্রফল $= \\frac{8}{3}\\frac{a^2}{m^3}$। এখানে $4a = 4 \\implies a = 1$ এবং $m = 1$। ক্ষেত্রফল $= \\frac{8}{3}\\frac{1^2}{1^3} = \\frac{8}{3}$ বর্গ একক!",
                "explanation": "ক্ষেত্রফল $= \\int_0^4 (\\sqrt{4x} - x) dx = [\\frac{4}{3}x^{3/2} - \\frac{x^2}{2}]_0^4 = \\frac{32}{3} - 8 = \\frac{8}{3}$ বর্গ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_06",
                "stem": "$\\frac{x^2}{16} + \\frac{y^2}{9} = 1$ উপবৃত্তের মোট ক্ষেত্রফল কত বর্গ একক?",
                "options": [
                    "$12\\pi$",
                    "$25\\pi$",
                    "$144\\pi$",
                    "$7\\pi$"
                ],
                "answer": "A",
                "type_ref": "Type 3: উপবৃত্তের ক্ষেত্রফল শর্টকাট",
                "trap_alert": "$a^2 = 16 \\implies a = 4$ এবং $b^2 = 9 \\implies b = 3$। বর্গমূল করতে ভুলে $144\\pi$ দাগানো!",
                "speed_hack": "উপবৃত্তের ক্ষেত্রফল $= \\pi a b = \\pi (4)(3) = 12\\pi$ বর্গ একক। ১ সেকেন্ডে সমাধান!",
                "explanation": "উপবৃত্তের ক্ষেত্রফল $\\pi a b = \\pi \\times 4 \\times 3 = 12\\pi$ বর্গ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_07",
                "stem": "$\\int_0^1 x e^x dx$ এর মান কত?",
                "options": [
                    "$1$",
                    "$e$",
                    "$e - 1$",
                    "$2$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ইউ-ভি মেথড (Integration by Parts)",
                "trap_alert": "লিমিট বসানোর সময় শূন্য বসালে $0 \\cdot e^0$ শূন্য হলেও $e^x$ এর মান ১ হয় তা খেয়াল রাখা।",
                "speed_hack": "LIATE নিয়ম: $[x e^x - e^x]_0^1 = (e - e) - (0 - 1) = 0 + 1 = 1$।",
                "explanation": "$\\int x e^x dx = x e^x - e^x$। লিমিট $0$ থেকে $1$ বসালে মান $1$ পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_08",
                "stem": "একটি বিজোড় ফাংশন $f(x)$ এর জন্য $\\int_{-a}^a f(x) dx$ এর মান কত?",
                "options": [
                    "$0$",
                    "$2\\int_0^a f(x)dx$",
                    "$2a$",
                    "$a$"
                ],
                "answer": "A",
                "type_ref": "Type 2: প্রতিসম সীমার নির্দিষ্ট যোগজের বৈশিষ্ট্য",
                "trap_alert": "জোড় ফাংশনের সাথে গুলিয়ে দ্বিগুণ ভাবা। বিজোড় ফাংশনে মান সর্বদা শূন্য!",
                "speed_hack": "বিজোড় ফাংশন $\\implies \\int_{-a}^a f(x) dx = 0$; জোড় ফাংশন $\\implies 2\\int_0^a f(x) dx$।",
                "explanation": "বিজোড় ফাংশনের লেখচিত্র মূলবিন্দুর সাপেক্ষে প্রতিসম হওয়ায় ধনাত্মক ও ঋণাত্মক অংশের ক্ষেত্রফল বাতিল হয়ে শূন্য হয়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_09",
                "stem": "$\\int_{-1}^3 |x - 1| dx$ এর মান কত?",
                "options": [
                    "$4$",
                    "$2$",
                    "$8$",
                    "$6$"
                ],
                "answer": "A",
                "type_ref": "Type 2: মডুলাস ফাংশন ও ত্রিভুজ ক্ষেত্রফল শর্টকাট (DU Speed-Hack)",
                "trap_alert": "মডুলাস সীমা ভেঙে দুই খণ্ডে যোগজীকরণ করতে গেলে ৩ মিনিট ব্যয় হবে। গ্রাফ আঁকুন!",
                "speed_hack": "মডুলাস যোগজ গ্রাফ শর্টকাট: $V$-আকৃতির গ্রাফের নিচে দুটি সমদ্বিবাহু ত্রিভুজের ক্ষেত্রফল $= \\frac{1}{2}(1 - (-1))^2 + \\frac{1}{2}(3 - 1)^2 = \\frac{1}{2}(4) + \\frac{1}{2}(4) = 2 + 2 = 4$! মুখে মুখে ২ সেকেন্ডে সমাধান!",
                "explanation": "$x=1$ বিন্দুতে শীর্ষ। বাম পাশের ত্রিভুজের ভূমি ২, উচ্চতা ২ (ক্ষেত্রফল ২) এবং ডান পাশের ত্রিভুজের ভূমি ২, উচ্চতা ২ (ক্ষেত্রফল ২)। মোট ক্ষেত্রফল $২+২=৪$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_10",
                "stem": "$\\int \\frac{dx}{x^2 + 9}$ এর মান কোনটি?",
                "options": [
                    "$\\frac{1}{3}\\tan^{-1}\\left(\\frac{x}{3}\\right) + c$",
                    "$\\tan^{-1}\\left(\\frac{x}{3}\\right) + c$",
                    "$\\frac{1}{9}\\tan^{-1}\\left(\\frac{x}{3}\\right) + c$",
                    "$\\frac{1}{3}\\ln|x + 3| + c$"
                ],
                "answer": "A",
                "type_ref": "Type 1: প্রমিত সূত্রাবলী $\\int \\frac{dx}{x^2 + a^2}$",
                "trap_alert": "সামনে $1/a$ গুণ করতে ভুলে যাওয়া।",
                "speed_hack": "সূত্র: $\\int \\frac{dx}{x^2 + a^2} = \\frac{1}{a}\\tan^{-1}(x/a) + c$। এখানে $a = 3$, তাই $\\frac{1}{3}\\tan^{-1}(x/3) + c$।",
                "explanation": "প্রমিত সূত্র মতে মান $\\frac{1}{3}\\tan^{-1}(x/3) + c$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_11",
                "stem": "$\\int \\ln x dx$ এর মান কোনটি?",
                "options": [
                    "$x\\ln x - x + c$",
                    "$\\frac{1}{x} + c$",
                    "$x\\ln x + x + c$",
                    "$\\frac{(\\ln x)^2}{2} + c$"
                ],
                "answer": "A",
                "type_ref": "Type 1: লগারিদমিক যোগজ ও অংশায়ন",
                "trap_alert": "অন্তরীকরণের সাথে গুলিয়ে $1/x$ দাগানো!",
                "speed_hack": "অংশায়ন সূত্রে $\\int 1 \\cdot \\ln x dx = x\\ln x - \\int x \\cdot \\frac{1}{x} dx = x\\ln x - x + c$। মুখস্থ রাখুন!",
                "explanation": "লগ এর যোগজ $x\\ln x - x + c$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_12",
                "stem": "$\\int_0^{\\pi/2} \\sin^3 x dx$ এর মান কত?",
                "options": [
                    "$\\frac{2}{3}$",
                    "$\\frac{1}{3}$",
                    "$\\frac{3}{4}$",
                    "$\\frac{\\pi}{4}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিকোণমিতিক নির্দিষ্ট যোগজ ও ওয়ালিস সূত্র",
                "trap_alert": "ওয়ালিসের বিজোড় ঘাতের সূত্রের নিয়ম মনে না রাখা।",
                "speed_hack": "ওয়ালিস শর্টকাট (Wallis' formula): $\\int_0^{\\pi/2} \\sin^3 x dx = \\frac{3-1}{3} = \\frac{2}{3}$। ২ সেকেন্ডে সমাধান!",
                "explanation": "ওয়ালিসের সূত্রানুসারে বিজোড় ঘাত ৩ হলে মান $\\frac{2}{3}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_13",
                "stem": "$y = x^2$ এবং $x = y^2$ বক্ররেখাদ্বয় দ্বারা আবদ্ধ অংশের ক্ষেত্রফল কত বর্গ একক?",
                "options": [
                    "$\\frac{1}{3}$",
                    "$\\frac{2}{3}$",
                    "$\\frac{1}{6}$",
                    "$1$"
                ],
                "answer": "A",
                "type_ref": "Type 3: দ্বৈত পরাবৃত্তের আবদ্ধ ক্ষেত্রফল শর্টকাট (DU Speed-Hack)",
                "trap_alert": "দ্বৈত পরাবৃত্ত $y^2 = 4ax$ ও $x^2 = 4by$ এর ক্ষেত্রফল $\\frac{16ab}{3}$। এখানে $4a = 1 \\implies a = 1/4$!",
                "speed_hack": "দ্বৈত পরাবৃত্তের আবদ্ধ ক্ষেত্রফল শর্টকাট: $y = x^2$ এবং $x = y^2$ এর আবদ্ধ ক্ষেত্রফল সর্বদা $\\frac{1}{3}$ বর্গ একক! (সূত্র: $\\frac{16(1/4)(1/4)}{3} = \\frac{1}{3}$)।",
                "explanation": "ক্ষেত্রফল $= \\int_0^1 (\\sqrt{x} - x^2) dx = [\\frac{2}{3}x^{3/2} - \\frac{x^3}{3}]_0^1 = \\frac{2}{3} - \\frac{1}{3} = \\frac{1}{3}$ বর্গ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_14",
                "stem": "$\\int_0^{\\pi/4} \\tan^2 x dx$ এর মান কত?",
                "options": [
                    "$1 - \\frac{\\pi}{4}$",
                    "$\\frac{\\pi}{4} - 1$",
                    "$1$",
                    "$\\frac{\\pi}{4}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ত্রিকোণমিতিক নির্দিষ্ট যোগজ",
                "trap_alert": "$\\tan^2 x = \\sec^2 x - 1$ এ রূপান্তর করতে হবে।",
                "speed_hack": "$\\int_0^{\\pi/4} (\\sec^2 x - 1) dx = [\\tan x - x]_0^{\\pi/4} = \\tan(\\pi/4) - \\pi/4 = 1 - \\frac{\\pi}{4}$।",
                "explanation": "অভেদ ব্যবহার করে ইন্টিগ্রেশন করলে মান $1 - \\pi/4$ পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_15",
                "stem": "$\\int \\frac{dx}{\\sqrt{a^2 - x^2}}$ এর মান কোনটি?",
                "options": [
                    "$\\sin^{-1}\\left(\\frac{x}{a}\\right) + c$",
                    "$\\frac{1}{a}\\sin^{-1}\\left(\\frac{x}{a}\\right) + c$",
                    "$\\cos^{-1}\\left(\\frac{x}{a}\\right) + c$",
                    "$\\ln|x + \\sqrt{a^2 - x^2}| + c$"
                ],
                "answer": "A",
                "type_ref": "Type 1: আদর্শ বিপরীত বৃত্তীয় যোগজ",
                "trap_alert": "ট্যানের মতো সামনে $1/a$ গুণ করা! ইনভার্স সাইনের ক্ষেত্রে বাইরে $1/a$ থাকে না!",
                "speed_hack": "স্ট্যান্ডার্ড ফর্মুলা: $\\int \\frac{dx}{\\sqrt{a^2 - x^2}} = \\sin^{-1}(x/a) + c$ (বাইরে কোনো $1/a$ নেই)।",
                "explanation": "প্রমিত সূত্র মতে মান $\\sin^{-1}(x/a) + c$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_16",
                "stem": "$\\int \\frac{1}{x(1 + \\ln x)} dx$ এর মান কত?",
                "options": [
                    "$\\ln|1 + \\ln x| + c$",
                    "$\\frac{1}{1 + \\ln x} + c$",
                    "$\\ln|x| + c$",
                    "$\\frac{(\\ln x)^2}{2} + c$"
                ],
                "answer": "A",
                "type_ref": "Type 1: প্রতিস্থাপন পদ্ধতি",
                "trap_alert": "প্রতিস্থাপন ধরতে না পারা। $1 + \\ln x = z$ ধরলে $dx/x = dz$!",
                "speed_hack": "লব হলো হরের ডেরিভেটিভ: $\\frac{d}{dx}(1 + \\ln x) = \\frac{1}{x}$। সুতরাং উত্তর $\\ln|\\text{হর}| = \\ln|1 + \\ln x| + c$।",
                "explanation": "$\\int \\frac{f'(x)}{f(x)}dx = \\ln|f(x)| + c$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_17",
                "stem": "$y = x^2$ বক্ররেখা এবং $y = 4$ সরলরেখা দ্বারা সীমাবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?",
                "options": [
                    "$\\frac{32}{3}$",
                    "$\\frac{16}{3}$",
                    "$16$",
                    "$8$"
                ],
                "answer": "A",
                "type_ref": "Type 3: পরাবৃত্ত ও রেখা দ্বারা আবদ্ধ ক্ষেত্রফল",
                "trap_alert": "উভয় পাশের ক্ষেত্রফল নিতে হবে, শুধু ১ম চতুর্ভাগ নিয়ে $16/3$ দাগালে ভুল হবে!",
                "speed_hack": "$2 \\int_0^4 \\sqrt{y} dy = 2 \\left[\\frac{2}{3} y^{3/2}\\right]_0^4 = \\frac{4}{3} (8) = \\frac{32}{3}$ বর্গ একক।",
                "explanation": "$y$-অক্ষের উভয় পাশের মোট ক্ষেত্রফল $2 \\times \\int_0^4 \\sqrt{y} dy = 32/3$ বর্গ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_18",
                "stem": "যদি $\\int_0^4 f(x) dx = 12$ হয়, তবে $\\int_0^2 f(2x) dx$ এর মান কত?",
                "options": [
                    "$6$",
                    "$24$",
                    "$12$",
                    "$3$"
                ],
                "answer": "A",
                "type_ref": "Type 2: নির্দিষ্ট যোগজের বাড়া-কমা নিয়ম (BARA-KOMA Rule) (DU Speed-Hack)",
                "trap_alert": "সহগ ২ দিয়ে গুণ করে ২৪ দাগানো! চলকের সহগ ২ দ্বারা ভাগ হবে!",
                "speed_hack": "নির্দিষ্ট যোগজের বাড়া-কমা নিয়ম (BARA-KOMA Rule): $\\int_a^b f(x) dx = k \\implies \\int_{a/m}^{b/m} f(mx) dx = \\frac{k}{m}$। এখানে $m = 2$, তাই মান $\\frac{12}{2} = 6$! মুখে মুখে ১ সেকেন্ডে!",
                "explanation": "ধরি $2x = u \\implies 2dx = du \\implies dx = du/2$। সীমা $x=0 \\to u=0$, $x=2 \\to u=4$। $\\int_0^4 f(u) \\frac{du}{2} = \\frac{12}{2} = 6$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_19",
                "stem": "$\\int_0^4 \\sqrt{16 - x^2} dx$ এর মান কত?",
                "options": [
                    "$4\\pi$",
                    "$8\\pi$",
                    "$16\\pi$",
                    "$2\\pi$"
                ],
                "answer": "A",
                "type_ref": "Type 3: জ্যামিতিক তাৎপর্য দ্বারা যোগজ নির্ণয়",
                "trap_alert": "বড় ত্রিকোণমিতিক প্রতিস্থাপন করার চেয়ে এটিকে সরাসরি বৃত্তের এক-চতুর্থাংশ ভাবা অনেক সহজ!",
                "speed_hack": "এটি $x^2 + y^2 = 16$ বৃত্তের ১ম চতুর্ভাগের ক্ষেত্রফল! মান $= \\frac{1}{4}\\pi r^2 = \\frac{1}{4}\\pi (16) = 4\\pi$। ১ সেকেন্ডে সমাধান!",
                "explanation": "বক্ররেখাটি ব্যাসার্ধ ৪ বিশিষ্ট বৃত্তের ১ম চতুর্ভাগ নির্দেশ করে, যার ক্ষেত্রফল $\\frac{1}{4}\\pi(4^2) = 4\\pi$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_10_20",
                "stem": "$\\int \\sec x dx$ এর প্রমিত মান কোনটি?",
                "options": [
                    "$\\ln|\\sec x + \\tan x| + c$",
                    "$\\ln|\\sec x - \\tan x| + c$",
                    "$\\sec x \\tan x + c$",
                    "$\\ln|\\cos x| + c$"
                ],
                "answer": "A",
                "type_ref": "Type 1: সেকেন্ট ফাংশনের প্রমিত যোগজ",
                "trap_alert": "মাইনাস চিহ্ন ভেবে ভুল অপশন দাগানো।",
                "speed_hack": "প্রমিত সূত্র: $\\int \\sec x dx = \\ln|\\sec x + \\tan x| + c$।",
                "explanation": "লব ও হরকে $(\\sec x + \\tan x)$ দ্বারা গুণ করে প্রতিস্থাপন করলে উত্তরটি সরাসরি পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    }
]
