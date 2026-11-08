#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
blueprint_chapters_physics.py
Contains complete unbundled blueprint and synthetic predictors for all 21 Physics chapters:
- 1st Paper: 10 chapters (phy_1st_01 to phy_1st_10)
- 2nd Paper: 11 chapters (phy_2nd_01 to phy_2nd_11)
"""

def get_physics_chapters():
    chapters = [
        # =========================================================================
        # PHYSICS 1ST PAPER (পদার্থবিজ্ঞান ১ম পত্র - ১০টি পৃথক অধ্যায়)
        # =========================================================================
        {
            "id": "phy_1st_01",
            "aliases": ["phy_measurement"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০১",
            "title": "ভৌতজগৎ ও পরিমাপ (Physical World & Measurement)",
            "subtitle": "মৌলিক একক, মাত্রা সমীকরণ, স্লাইড ক্যালিপার্স, স্ক্রু গজ ও ত্রুটি গণনা",
            "total_qb_questions": 310,
            "high_yield_score": 93,
            "mega_types": [
                {
                    "type_id": "phy_p01_t1",
                    "name": "Type 1: মাত্রা সমীকরণ ও ধ্রুবকের মাত্রা নির্ণয়",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '22-23", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P03-Q02", "VAR-DU-P05-Q03", "MAD-MAT-Q16"],
                    "core_rule": "প্রধান ধ্রুবকসমূহের মাত্রা ও একক: ১. মহাকর্ষীয় ধ্রুবক $G$: মাত্রা $[M^{-1}L^3T^{-2}]$, একক $\\text{N}\\cdot\\text{m}^2\\cdot\\text{kg}^{-2}$; ২. প্লাঙ্কের ধ্রুবক $h$: মাত্রা $[ML^2T^{-1}]$, একক $\\text{J}\\cdot\\text{s}$; ৩. সান্দ্রতা গুণাঙ্ক $\\eta$: মাত্রা $[ML^{-1}T^{-1}]$, একক $\\text{N}\\cdot\\text{s}\\cdot\\text{m}^{-2}$ বা $\\text{Pa}\\cdot\\text{s}$; ৪. পৃষ্ঠটান $T$: মাত্রা $[MT^{-2}]$, একক $\\text{N/m}$; ৫. স্প্রিং ধ্রুবক $k$: মাত্রা $[MT^{-2}]$; ৬. রৈখিক ভরবেগ ও বলের ঘাতের মাত্রা $[MLT^{-1}]$; ৭. কাজ ও টর্কের মাত্রা $[ML^2T^{-2}]$। মাত্রাহীন রাশি: বিকৃতি, পয়সনের অনুপাত, প্রতিসরাঙ্ক, আপেক্ষিক আর্দ্রতা, কোণ (একক রেডিয়ান হলেও মাত্রাহীন)।",
                    "speed_elimination": "প্লাঙ্কের ধ্রুবক ($h$) এবং কৌণিক ভরবেগের ($L$) মাত্রা হুবহু এক: $[ML^2T^{-1}]$; কাজ ও টর্কের মাত্রা একই: $[ML^2T^{-2}]$।"
                },
                {
                    "type_id": "phy_p01_t2",
                    "name": "Type 2: ভার্নিয়ার ধ্রুবক, লঘিষ্ঠ গণন ও শতকরা ত্রুটি হিসাব",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '22-23", "GST '21-22", "MAT '22", "MAT '20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q15", "VAR-DU-P02-Q14", "MAD-MAT-Q08"],
                    "core_rule": "ভার্নিয়ার ধ্রুবক: $VC = \\frac{s}{n} = 1\\text{ MSD} - 1\\text{ VSD}$ (যেখানে $s =$ মূল স্কেলের ক্ষুদ্রতম ১ ভাগের মান, $n =$ ভার্নিয়ার স্কেলের মোট ভাগ সংখ্যা)। স্লাইড ক্যালিপার্সে পাঠ: $L = M + (V \\times VC) - (\\pm e)$। স্ক্রু গজের লঘিষ্ঠ গণন: $LC = \\frac{\\text{পিচ (Pitch)}}{\\text{বৃত্তাকার স্কেলের মোট ভাগ সংখ্যা}}$। ত্রুটি গণনা: শতকরা ত্রুটি $= \\frac{\\text{পরম ত্রুটি}}{\\text{পরিমাপকৃত মান}} \\times 100\\%$। যদি $Z = \\frac{A^a B^b}{C^c}$ হয়, তবে শতকরা ত্রুটি: $\\frac{\\Delta Z}{Z} \\times 100\\% = a\\left(\\frac{\\Delta A}{A}\\right) + b\\left(\\frac{\\Delta B}{B}\\right) + c\\left(\\frac{\\Delta C}{C}\\right)$। যেমন গোলকের ব্যাসার্ধ পরিমাপে ২% ত্রুটি হলে আয়তন ($V = \\frac{4}{3}\\pi r^3$) পরিমাপে ত্রুটি হবে $3 \\times 2\\% = 6\\%$।",
                    "speed_elimination": "ঘাত যত থাকবে শতকরা ত্রুটি তত গুণ হবে (ব্যাসার্ধে ২% ত্রুটি হলে ক্ষেত্রফলে $2\\times 2\\% = 4\\%$, আয়তনে $3\\times 2\\% = 6\\%$)।"
                }
            ]
        },
        {
            "id": "phy_1st_02",
            "aliases": ["phy_vector"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০২",
            "title": "ভেক্টর (Vector)",
            "subtitle": "ডট-ক্রস গুণন, লম্ব-সমান্তরাল শর্ত, নদী-নৌকা ও ভেক্টর ক্যালকুলাস",
            "total_qb_questions": 450,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p02_t1",
                    "name": "Type 1: ডট ও ক্রস গুণনের শর্ত (লম্ব ও সমান্তরাল ভেক্টর)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '20-21", "GST '22-23", "BUET '18-19", "MAT '17"],
                    "qb_question_refs": ["VAR-JnU-P01-Q01", "VAR-RU-P02-Q16", "VAR-GST-P01-Q04", "VAR-CU-P04-Q12"],
                    "core_rule": "দুটি ভেক্টর পরস্পর লম্ব হলে $\\vec{A} \\cdot \\vec{B} = 0 \\implies A_x B_x + A_y B_y + A_z B_z = 0$; সমান্তরাল হলে $\\vec{A} \\times \\vec{B} = 0 \\implies \\frac{A_x}{B_x} = \\frac{A_y}{B_y} = \\frac{A_z}{B_z}$। সামান্তরিকের ক্ষেত্রফল: দুটি সন্নিহিত বাহু $\\vec{A}, \\vec{B}$ হলে $|\vec{A} \\times \\vec{B}|$; দুটি কর্ণ $\\vec{d_1}, \\vec{d_2}$ হলে $\\frac{1}{2}|\\vec{d_1} \\times \\vec{d_2}|$। ত্রিভুজের ক্ষেত্রফল $= \\frac{1}{2}|\\vec{A} \\times \\vec{B}|$। তিনটি ভেক্টর সমতলীয় হওয়ার শর্ত: $[\vec{A} \ \\vec{B} \ \\vec{C}] = \\vec{A} \\cdot (\\vec{B} \\times \\vec{C}) = 0$।",
                    "speed_elimination": "লম্বের ক্ষেত্রে অনুভূমিক ও উলম্ব উপাংশের গুণফলের সমষ্টি শূন্য মিলিয়ে ৩ সেকেন্ডে অপশন বাছাই করুন; সমান্তরাল হলে অনুপাত সমান।"
                },
                {
                    "type_id": "phy_p02_t2",
                    "name": "Type 2: নদী-নৌকা ও ন্যূনতম সময় বনাম ন্যূনতম দূরত্ব",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '18-19", "RU '20-21", "CU '19-20", "GST '21-22", "BUET '16-17", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q05", "VAR-JU-P08-Q14", "VAR-CU-P05-Q19"],
                    "core_rule": "স্রোতের বেগ $u$, নৌকার বেগ $v$, নদীর প্রস্থ $d$। ১. সোজাসোজি পাড়ি (ন্যূনতম দূরত্ব): লব্ধি বেগ নদীর প্রস্থ বরাবর ($90^\\circ$ কোণে), চালনার কোণ $\\cos\\alpha = -\\frac{u}{v} \\implies \\alpha = \\cos^{-1}\\left(-\\frac{u}{v}\\right)$ ($v > u$ হতে হবে), লব্ধি বেগ $w = \\sqrt{v^2 - u^2}$, সময় $t = \\frac{d}{\\sqrt{v^2 - u^2}}$। ২. ন্যূনতম সময়: সোজা অপর পাড়ের উদ্দেশ্যে চালনা $\\alpha = 90^\\circ$, ন্যূনতম সময় $t_{min} = \\frac{d}{v}$, অনুভূমিক সরণ (Drift) $x = u \\times t_{min} = \\frac{u d}{v}$।",
                    "speed_elimination": "সোজাসোজি পাড়ির কোণ সর্বদা স্থূলকোণ ($>90^\\circ$); নৌকার বেগ স্রোতের দ্বিগুণ ($v=2u$) হলে কোণ সর্বদা $120^\\circ$।"
                },
                {
                    "type_id": "phy_p02_t3",
                    "name": "Type 3: বৃষ্টি ও ছাতার কোণ (আপেক্ষিক বেগ)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 28,
                    "past_tags": ["DU '20-21", "RU '19-20", "JU '21-22", "MAT '19", "SUST '18-19"],
                    "qb_question_refs": ["VAR-JnU-P12-Q14", "VAR-RU-P09-Q03", "MAD-MAT-Q18"],
                    "core_rule": "বৃষ্টি খাড়া নিচের দিকে $v_r$ বেগে পড়লে এবং লোক অনুভূমিকভাবে $v_m$ বেগে চললে লোকের সাপেক্ষে বৃষ্টির আপেক্ষিক বেগ $\\vec{v}_{rm} = \\vec{v}_r - \\vec{v}_m$। উলম্বের সাথে ছাতা ধরার কোণ: $\\tan\\theta = \\frac{v_{man}}{v_{rain}} \\implies \\theta = \\tan^{-1}\\left(\\frac{v_m}{v_r}\\right)$। অনুভূমিক বাতাস $v_w$ থাকলে একই দিকে চললে $\\tan\\theta = \\frac{|v_m - v_w|}{v_r}$; বিপরীত দিকে চললে $\\tan\\theta = \\frac{v_m + v_w}{v_r}$।",
                    "speed_elimination": "লোক ও বৃষ্টির বেগের অনুপাত $\\frac{1}{\\sqrt{3}}$ হলে কোণ $30^\\circ$, অনুপাত ১ হলে $45^\\circ$, অনুপাত $\\sqrt{3}$ হলে $60^\\circ$।"
                },
                {
                    "type_id": "phy_p02_t4",
                    "name": "Type 4: ভেক্টর ক্যালকুলাস (গ্র্যাডিয়েন্ট, ডাইভারজেন্স ও কার্ল)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '23-24", "DU '19-20", "RU '22-23", "GST '20-21", "BUTEX '19-20"],
                    "qb_question_refs": ["VAR-RU-P01-Q02", "VAR-JnU-P19-Q04", "VAR-SUST-P14-Q02"],
                    "core_rule": "১. গ্র্যাডিয়েন্ট (স্কেলার থেকে ভেক্টর): $\\vec{\\nabla}\\phi = \\hat{i}\\frac{\\partial\\phi}{\\partial x} + \\hat{j}\\frac{\\partial\\phi}{\\partial y} + \\hat{k}\\frac{\\partial\\phi}{\\partial z}$। ২. ডাইভারজেন্স (ভেক্টর থেকে স্কেলার): $\\vec{\\nabla} \\cdot \\vec{V} = \\frac{\\partial V_x}{\\partial x} + \\frac{\\partial V_y}{\\partial y} + \\frac{\\partial V_z}{\\partial z}$; সলিনয়ডাল (Solenoidal) বা অসংকোচনীয় হওয়ার শর্ত: $\\vec{\\nabla} \\cdot \\vec{V} = 0$। ৩. কার্ল (ভেক্টর থেকে ভেক্টর): $\\vec{\\nabla} \\times \\vec{V} = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ \\frac{\\partial}{\\partial x} & \\frac{\\partial}{\\partial y} & \\frac{\\partial}{\\partial z} \\\\ V_x & V_y & V_z \\end{vmatrix}$; অঘূর্ণনশীল (Irrotational) ও সংরক্ষণশীল হওয়ার শর্ত: $\\vec{\\nabla} \\times \\vec{V} = 0$। কৌণিক বেগ $\\vec{\\omega} = \\frac{1}{2}(\\vec{\\nabla} \\times \\vec{v})$।",
                    "speed_elimination": "সলিনয়ডাল হলে ডট গুণন শূন্য ($\vec{\\nabla} \\cdot \\vec{V} = 0$); অঘূর্ণনশীল হলে ক্রস গুণন শূন্য ($\vec{\\nabla} \\times \\vec{V} = 0$)।"
                }
            ]
        },
        {
            "id": "phy_1st_03",
            "aliases": ["phy_dynamics"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৩",
            "title": "গতিবিদ্যা ও প্রক্ষেপক (Dynamics & Projectile)",
            "subtitle": "প্রক্ষেপকের পাল্লা, উড্ডয়নকাল, সর্বোচ্চ বিন্দুতে গতিশক্তি ও স্টপিং ডিসট্যান্স",
            "total_qb_questions": 420,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "phy_p03_t1",
                    "name": "Type 1: প্রক্ষেপকের গতিসূত্র ও সর্বোচ্চ পাল্লা-উচ্চতা সম্পর্ক",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '17-18", "RU '20-21", "JU '19-20", "GST '21-22", "Agri '22-23"],
                    "qb_question_refs": ["VAR-HSTU-P01-Q01", "VAR-JnU-P02-Q07", "VAR-RU-P05-Q12"],
                    "core_rule": "আদিবেগ $v_0$ ও নিক্ষেপণ কোণ $\\theta_0$ হলে: উড্ডয়নকাল $T = \\frac{2v_0\\sin\\theta_0}{g}$; সর্বোচ্চ উচ্চতা $H = \\frac{v_0^2\\sin^2\\theta_0}{2g}$; অনুভূমিক পাল্লা $R = \\frac{v_0^2\\sin 2\\theta_0}{g}$। পাল্লা ও উচ্চতার মাস্টার সম্পর্ক: $R = 4H\\cot\\theta_0 \\implies \\tan\\theta_0 = \\frac{4H}{R}$। সর্বোচ্চ পাল্লার শর্ত: $\\theta_0 = 45^\\circ \\implies R_{max} = \\frac{v_0^2}{g} = 4H$। একই পাল্লার জন্য দুটি নিক্ষেপণ কোণ: $\\theta$ এবং $(90^\\circ - \\theta)$; তাদের উড্ডয়নকালের গুণফল $T_1 T_2 = \\frac{2R}{g}$। গতিপথের সমীকরণ: $y = x\\tan\\theta_0 - \\frac{g x^2}{2v_0^2\\cos^2\\theta_0}$ (পরাবৃত্তাকার/Parabolic)।",
                    "speed_elimination": "পাল্লা ও সর্বোচ্চ উচ্চতা সমান ($R = H$) হলে কোণ $\\tan\\theta = 4 \\implies \\theta = 76^\\circ$; $45^\\circ$ কোণে পাল্লা উচ্চতার ঠিক ৪ গুণ।"
                },
                {
                    "type_id": "phy_p03_t2",
                    "name": "Type 2: সর্বোচ্চ বিন্দুতে বেগ ও গতিশক্তি-বিভব শক্তি বণ্টন",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '21-22", "DU '18-19", "RU '21-22", "MAT '20", "SUST '19-20"],
                    "qb_question_refs": ["VAR-JU-P04-Q18", "VAR-CU-P07-Q05", "MAD-MAT-Q09"],
                    "core_rule": "সর্বোচ্চ বিন্দুতে উলম্ব বেগ শূন্য ($v_y = 0$), কেবল অনুভূমিক বেগ থাকে: $v = v_x = v_0\\cos\\theta$। প্রারম্ভিক গতিশক্তি $E_k = \\frac{1}{2}m v_0^2$ হলে: সর্বোচ্চ বিন্দুতে গতিশক্তি $E_k' = \\frac{1}{2}m v_x^2 = E_k \\cos^2\\theta$; সর্বোচ্চ বিন্দুতে বিভব শক্তি $E_p' = m g H = E_k \\sin^2\\theta$। শক্তি সংরক্ষণশীল: $E_k' + E_p' = E_k$।",
                    "speed_elimination": "$45^\\circ$ কোণে নিক্ষিপ্ত বস্তুর সর্বোচ্চ বিন্দুতে গতিশক্তি ঠিক অর্ধেক ($E_k/2$) এবং বিভব শক্তি বাকি অর্ধেক ($E_k/2$)।"
                },
                {
                    "type_id": "phy_p03_t3",
                    "name": "Type 3: তক্তা ভেদ ও ব্রেক কষার স্টপিং ডিসট্যান্স",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '19-20", "RU '18-19", "JU '22-23", "GST '20-21", "CU '17-18", "Agri '21-22"],
                    "qb_question_refs": ["VAR-JnU-P01-Q09", "VAR-RU-P03-Q14", "VAR-GST-P02-Q18"],
                    "core_rule": "সমমন্দনে থামার দূরত্ব $s = \\frac{v^2}{2a} \\implies s \\propto v^2$ (বেগ $n$ গুণ হলে থামার দূরত্ব $n^2$ গুণ হয়)। গুলি তক্তা ভেদ: একটি তক্তা ভেদ করে বেগ $\\frac{1}{n}$ অংশ হারালে (অবশিষ্ট থাকে $v(1 - 1/n)$), মোট তক্তা ভেদ করতে পারবে $N = \\frac{n^2}{2n - 1}$ টি। যেমন বেগ অর্ধেক হারালে ($n=2$): মোট তক্তা $N = \\frac{4}{3} = 1.33$, অর্থাৎ আরও $\\frac{1}{3}$ টি তক্তা ভেদ করে থেমে যাবে।",
                    "speed_elimination": "গাড়ির গতিবেগ দ্বিগুণ করলে স্টপিং ডিসট্যান্স ৪ গুণ হবে ($s \\propto v^2$); বেগ ৩ গুণ করলে দূরত্ব ৯ গুণ হবে।"
                }
            ]
        },
        {
            "id": "phy_1st_04",
            "aliases": ["phy_newtonian"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৪",
            "title": "নিউটনীয় বলবিদ্যা (Newtonian Mechanics)",
            "subtitle": "জড়তার ভ্রামক, চক্রগতির ব্যাসার্ধ, রকেট/বন্দুক, ব্যাংকিং কোণ ও টর্ক",
            "total_qb_questions": 480,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p04_t1",
                    "name": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 40,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "GST '22-23", "BUET '19-20", "MAT '18", "JnU '20-21"],
                    "qb_question_refs": ["VAR-JnU-P01-Q04", "VAR-RU-P07-Q01", "VAR-CU-P02-Q11"],
                    "core_rule": "জড়তার ভ্রামক $I = \\Sigma m r^2 = M K^2$ ($K$ হলো চক্রগতির ব্যাসার্ধ)। স্ট্যান্ডার্ড মানসমূহ: ১. নিরেট গোলক (Solid sphere): $I = \\frac{2}{5}MR^2$, $K = \\sqrt{\\frac{2}{5}}R$; স্পর্শক অক্ষের সাপেক্ষে $I = \\frac{7}{5}MR^2$; ২. ফাঁপা গোলক: $I = \\frac{2}{3}MR^2$; ৩. নিরেট সিলিন্ডার/চাকতি: $I = \\frac{1}{2}MR^2$; ৪. সরু সুষম দণ্ড: মধ্যবিন্দু দিয়ে লম্ব অক্ষে $I = \\frac{1}{12}ML^2$, এক প্রান্তবিন্দু দিয়ে লম্ব অক্ষে $I = \\frac{1}{3}ML^2$। সমান্তরাল অক্ষ উপপাদ্য: $I = I_G + M h^2$। লম্ব অক্ষ উপপাদ্য: $I_z = I_x + I_y$। গড়িয়ে চলার ক্ষেত্রে মোট শক্তি: $E = \\frac{1}{2}M v^2 + \\frac{1}{2}I\\omega^2 = \\frac{1}{2}M v^2 \\left(1 + \\frac{K^2}{R^2}\\right)$ (নিরেট গোলকের মোট শক্তির ঘূর্ণন অংশ $\\frac{2}{7}$ ও রৈখিক অংশ $\\frac{5}{7}$)।",
                    "speed_elimination": "একই ভর ও ব্যাসার্ধের ক্ষেত্রে জড়তার ভ্রামক: ফাঁপা গোলক ($0.67$) > চাকতি ($0.5$) > নিরেট গোলক ($0.4$); ফলে গড়িয়ে পড়ার দৌড়ে নিরেট গোলক সবার আগে পৌঁছাবে।"
                },
                {
                    "type_id": "phy_p04_t2",
                    "name": "Type 2: রাস্তার ব্যাংকিং কোণ ও সর্বোচ্চ নিরাপদ বেগ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '19-20", "JU '21-22", "RU '19-20", "GST '21-22", "Agri '20-21"],
                    "qb_question_refs": ["VAR-JnU-P04-Q15", "VAR-JU-P09-Q02", "VAR-GST-P08-Q12"],
                    "core_rule": "ব্যাংকিং কোণ $\\tan\\theta = \\frac{v^2}{r g}$; সর্বোচ্চ নিরাপদ বেগ $v = \\sqrt{r g \\tan\\theta}$। রেললাইন বা রাস্তার প্রস্থ $d$ এবং ভেতরের ও বাইরের লাইনের উচ্চতার পার্থক্য $h$ হলে: $\\sin\\theta = \\frac{h}{d}$। ক্ষুদ্র কোণের জন্য $\\sin\\theta \\approx \\tan\\theta \\implies \\frac{h}{d} = \\frac{v^2}{r g} \\implies h = \\frac{v^2 d}{r g}$। সাইকেল আরোহীর ক্ষেত্রে উলম্বের সাথে নতি কোণ $\\tan\\theta = \\frac{v^2}{r g}$।",
                    "speed_elimination": "বেগ দ্বিগুণ করলে প্রয়োজনীয় উচ্চতার পার্থক্য ($h$) ৪ গুণ বৃদ্ধি পাবে ($h \\propto v^2$)।"
                },
                {
                    "type_id": "phy_p04_t3",
                    "name": "Type 3: ভরবেগের সংরক্ষণ, রকেট ও বন্দুকের পশ্চাৎবেগ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '20-21", "DU '18-19", "RU '20-21", "MAT '21", "CU '19-20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q02", "VAR-RU-P04-Q19", "MAD-MAT-Q04"],
                    "core_rule": "বন্দুকের পশ্চাৎবেগ: $M V + m v = 0 \\implies V = -\\frac{m v}{M}$। রকেটের ক্ষেত্রে: জ্বালানি নির্গমনের হার $\\frac{\\Delta m}{\\Delta t}$ ও নির্গমন বেগ $v_{ex}$ হলে রকেটের ওপর ধাক্কা বল $F = v_{ex} \\frac{\\Delta m}{\\Delta t}$; ঊর্ধ্বমুখী ত্বরণ $a = \\frac{v_{ex}}{m}\\frac{\\Delta m}{\\Delta t} - g$। বলের ঘাত $J = F \\Delta t = \\Delta p = m(v - u)$।",
                    "speed_elimination": "বন্দুকের পশ্চাৎ বেগ বের করার সময় গুলির ভর গ্রামে থাকলে ১০০০ দিয়ে ভাগ করে কেজিতে নিয়ে সেকেন্ডে হিসাব করুন।"
                }
            ]
        },
        {
            "id": "phy_1st_05",
            "aliases": ["phy_work_energy"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৫",
            "title": "কাজ, শক্তি ও ক্ষমতা (Work, Energy & Power)",
            "subtitle": "কৃতকাজ, স্প্রিং বলের সঞ্চিত শক্তি, কুয়া খালি করার কাজ ও ক্ষমতা",
            "total_qb_questions": 440,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "phy_p05_t1",
                    "name": "Type 1: পরিবর্তনশীল বল ও স্প্রিং সম্প্রসারণে কৃতকাজ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 34,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P02-Q12", "VAR-DU-P04-Q05", "VAR-GST-P03-Q08"],
                    "core_rule": "স্প্রিং বল $F = -kx$; স্প্রিংকে $x$ পরিমাণ প্রসারিত বা সংকুচিত করতে কৃতকাজ বা সঞ্চিত বিভব শক্তি: $W = E_p = \\frac{1}{2}kx^2$। $x_1$ থেকে $x_2$ অবস্থানে প্রসারিত করতে কাজ: $W = \\frac{1}{2}k(x_2^2 - x_1^2)$। দুটি স্প্রিং সমবায়: শ্রেণিতে $\\frac{1}{k_s} = \\frac{1}{k_1} + \\frac{1}{k_2}$; সমান্তরালে $k_p = k_1 + k_2$। একটি স্প্রিংকে কেটে $n$ টুকরো করলে প্রতিটি টুকরোর স্প্রিং ধ্রুবক $n$ গুণ বৃদ্ধি পায় ($k' = n k$)।",
                    "speed_elimination": "একটি স্প্রিংকে কেটে সমান ৩ টুকরো করলে প্রতিটি খণ্ডের স্প্রিং ধ্রুবক ৩ গুণ ($3k$) হবে।"
                },
                {
                    "type_id": "phy_p05_t2",
                    "name": "Type 2: কুয়া ও চৌবাচ্চা খালি করতে কৃতকাজ ও মোটরের ক্ষমতা",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '20-21", "JU '21-22", "GST '21-22", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q11", "VAR-DU-P06-Q08", "VAR-CU-P05-Q14"],
                    "core_rule": "কুয়া সম্পূর্ণ পানি খালি করতে কাজ: $W = m g \\bar{h}$; যেখানে $\\bar{h}$ হলো ভারকেন্দ্রের সরণ। কুয়ার উচ্চতা/গভীরতা $h$ হলে: ১. সম্পূর্ণ পূর্ণ কুয়া সম্পূর্ণ খালি করতে: $\\bar{h} = \\frac{h}{2}$; ২. অর্ধপূর্ণ কুয়া সম্পূর্ণ খালি করতে: $\\bar{h} = \\frac{h}{2} + \\frac{h/2}{2} = \\frac{3h}{4}$; ৩. সম্পূর্ণ পূর্ণ কুয়ার অর্ধেক খালি করতে: $\\bar{h} = \\frac{h/2}{2} = \\frac{h}{4}$ (ভর $m/2$)। পানি পাম্পের ক্ষমতা: $P = \\frac{W}{t} = \\frac{m g \\bar{h}}{t}$ (1 HP $= 746\\text{ W}$)। কর্মদক্ষতা $\\eta = \\frac{P_{out}}{P_{in}} \\times 100\\%$।",
                    "speed_elimination": "সম্পূর্ণ পূর্ণ কুয়ার অর্ধেক খালি করার কাজ, সম্পূর্ণ খালি করার কাজের তুলনায় ঠিক $\\frac{1}{4}$ অংশ।"
                },
                {
                    "type_id": "phy_p05_t3",
                    "name": "Type 3: গতিশক্তি ও রৈখিক ভরবেগের সম্পর্ক",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '22-23", "DU '18-19", "RU '22-23", "GST '20-21", "MAT '21"],
                    "qb_question_refs": ["VAR-DU-P01-Q09", "VAR-RU-P01-Q15", "MAD-MAT-Q20"],
                    "core_rule": "গতিশক্তি $E_k = \\frac{p^2}{2m} \\implies p = \\sqrt{2m E_k}$। ভরবেগ $x\\%$ বৃদ্ধি পেলে নতুন গতিশক্তি: $E_k' = E_k \\left(1 + \\frac{x}{100}\\right)^2$। যেমন ভরবেগ ৫০% বাড়লে গতিশক্তি বৃদ্ধি পায়: $(1.5)^2 - 1 = 1.25$ অর্থাৎ ১২৫% বৃদ্ধি পাবে। ভরবেগ ১০০% বাড়লে গতিশক্তি বৃদ্ধি পায় ৩০০% ($৪$ গুণ হয়)।",
                    "speed_elimination": "ভরবেগ দ্বিগুণ ($+100\\%$) করলে গতিশক্তি ৪ গুণ ($+300\\%$) হবে; গতিশক্তি ৪ গুণ করলে ভরবেগ দ্বিগুণ হবে।"
                }
            ]
        },
        {
            "id": "phy_1st_06",
            "aliases": ["phy_gravitation"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৬",
            "title": "মহাকর্ষ ও অভিকর্ষ (Gravitation & Gravity)",
            "subtitle": "g এর পরিবর্তন, মুক্তিবেগ, উপগ্রহের পর্যায়কাল ও কেপলারের সূত্র",
            "total_qb_questions": 430,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "phy_p06_t1",
                    "name": "Type 1: অভিকর্ষজ ত্বরণ $g$ এর পরিবর্তন (উচ্চতা, গভীরতা ও অক্ষাংশ)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23", "MAT '20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q10", "VAR-DU-P02-Q12", "VAR-RU-P04-Q15"],
                    "core_rule": "ভূপৃষ্ঠে $g = \\frac{GM}{R^2}$। ১. ভূপৃষ্ঠ হতে $h$ উচ্চতায়: $g' = g\\left( \\frac{R}{R+h} \\right)^2$; $h \\ll R$ হলে $g' \\approx g\\left(1 - \\frac{2h}{R}\\right)$। ২. ভূপৃষ্ঠ হতে $h$ গভীরতায়: $g' = g\\left(1 - \\frac{h}{R}\\right)$; পৃথিবীর কেন্দ্রে ($h=R$) অভিকর্ষজ ত্বরণ $g = 0$ এবং বস্তুর ওজন শূন্য। ৩. আহ্নিক গতির কারণে $\\lambda$ অক্ষাংশে: $g' = g - \\omega^2 R \\cos^2\\lambda$; বিষুব অঞ্চলে ($\\lambda = 0^\\circ$) $g$ সর্বনিম্ন ($g - \\omega^2 R$); মেরু অঞ্চলে ($\\lambda = 90^\\circ$) $g$ সর্বোচ্চ ($g = 9.83\\text{ m/s}^2$)। পৃথিবী ঘোরা বন্ধ করলে বিষুব অঞ্চলে ওজন বৃদ্ধি পাবে কিন্তু মেরুতে কোনো পরিবর্তন হবে না।",
                    "speed_elimination": "পৃথিবীর কেন্দ্রে ওজন শূন্য; ভূপৃষ্ঠ থেকে $h$ উচ্চতায় $g$ এর হ্রাস, একই গভীরতায় হ্রাসের দ্বিগুণ।"
                },
                {
                    "type_id": "phy_p06_t2",
                    "name": "Type 2: মুক্তিবেগ ও কৃত্রিম উপগ্রহের বেগ-পর্যায়কাল",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '22-23", "JU '21-22", "GST '21-22", "BUET '21-22", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P04-Q08", "VAR-DU-P03-Q14", "VAR-GST-P01-Q18"],
                    "core_rule": "মুক্তিবেগ (Escape velocity): $v_e = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2gR}$ (পৃথিবীর জন্য $v_e = 11.2\\text{ km/s}$; চাঁদের জন্য $2.4\\text{ km/s}$)। মুক্তিবেগ বস্তুর ভরের ওপর নির্ভর করে না ($m^0$) এবং নিক্ষেপণ কোণের ওপরও নির্ভর করে না। কৃত্রিম উপগ্রহের বেগ: $v = \\sqrt{\\frac{GM}{R+h}}$; ভূপৃষ্ঠের খুব কাছে চললে $v = \\sqrt{gR} = 7.92\\text{ km/s}$। সম্পর্ক: $v_e = \\sqrt{2} v_{orbit} \\approx 1.414 v_{orbit}$ (উপগ্রহের বেগ ৪১.৪% বাড়ালে তা কক্ষপথ ছেড়ে মহাশূন্যে চলে যাবে)। ভূ-স্থির উপগ্রহের পর্যায়কাল $T = 24\\text{ hours}$ এবং উচ্চতা $h \\approx 36,000\\text{ km}$।",
                    "speed_elimination": "মুক্তিবেগ পৃথিবীর পৃষ্ঠে ১১.২ কিমি/সেকেন্ড; কক্ষীয় বেগকে $\\sqrt{2}$ গুণ (৪১.৪% বৃদ্ধি) করলে উপগ্রহটি মুক্ত হয়ে যাবে।"
                },
                {
                    "type_id": "phy_p06_t3",
                    "name": "Type 3: কেপলারের গ্রহীয় গতিসূত্র ও পর্যায়কাল ($T^2 \\propto r^3$)",
                    "importance": "4-Star",
                    "stars": 4,
                    "repeat_frequency": 24,
                    "past_tags": ["DU '20-21", "RU '20-21", "GST '20-21", "MAT '19"],
                    "qb_question_refs": ["VAR-DU-P07-Q10", "MAD-MAT-Q23"],
                    "core_rule": "কেপলারের ৩য় সূত্র (পর্যায়কালের সূত্র): সূর্যের চারদিকে প্রতিটি গ্রহের আবর্তনকালের বর্গ সূর্য থেকে এর গড় দূরত্বের ঘনের সমানুপাতিক: $T^2 \\propto r^3 \\implies \\left(\\frac{T_1}{T_2}\\right)^2 = \\left(\\frac{r_1}{r_2}\\right)^3$। সূর্য ও পৃথিবীর মধ্যবর্তী দূরত্ব অর্ধেক করা হলে বছরের দৈর্ঘ্য হবে: $T_2 = T_1 \\left(\\frac{1}{2}\\right)^{3/2} = \\frac{365}{2\\sqrt{2}} \\approx 129\\text{ days}$।",
                    "speed_elimination": "দূরত্ব ৪ গুণ করা হলে পর্যায়কাল হবে $4^{3/2} = 8$ গুণ।"
                }
            ]
        },
        {
            "id": "phy_1st_07",
            "aliases": ["phy_matter_properties"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৭",
            "title": "পদার্থের গাঠনিক ধর্ম (Structural Properties of Matter)",
            "subtitle": "হুকের সূত্র, ইয়ংয়ের গুণাঙ্ক, পৃষ্ঠটান ও সান্দ্রতা (স্টোকসের সূত্র)",
            "total_qb_questions": 420,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "phy_p07_t1",
                    "name": "Type 1: ইয়ংয়ের গুণাঙ্ক, পীড়ন-বিকৃতি ও তারের প্রসারণে কৃতকাজ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '18-19"],
                    "qb_question_refs": ["VAR-JnU-P02-Q05", "VAR-DU-P03-Q07", "VAR-RU-P01-Q14"],
                    "core_rule": "হুকের সূত্র (স্থিতিস্থাপক সীমার মধ্যে): পীড়ন $\\propto$ বিকৃতি $\\implies \\frac{\\text{পীড়ন}}{\\text{বিকৃতি}} = Y$ (ধ্রুবক)। দৈর্ঘ্য বরাবর ইয়ংয়ের গুণাঙ্ক: $Y = \\frac{F L}{A l} = \\frac{m g L}{\\pi r^2 l}$। তারের প্রসারণে সঞ্চিত শক্তি বা কৃতকাজ: $W = \\frac{1}{2} F l = \\frac{1}{2} \\frac{Y A l^2}{L}$। একক আয়তনে সঞ্চিত শক্তি: $u = \\frac{W}{V} = \\frac{1}{2} \\times \\text{পীড়ন} \\times \\text{বিকৃতি} = \\frac{\\text{পীড়ন}^2}{2Y} = \\frac{1}{2} Y (\\text{বিকৃতি})^2$। পয়সনের অনুপাত: $\\sigma = -\\frac{\\text{পার্শ্ব বিকৃতি}}{\\text{দৈর্ঘ্য বিকৃতি}} = -\\frac{d/D}{l/L}$; তাত্ত্বিক সীমা $-1 < \\sigma < 0.5$, কিন্তু ব্যবহারিক মান $0 < \\sigma < 0.5$।",
                    "speed_elimination": "তারের ব্যাসার্ধ দ্বিগুণ করলে একই বল প্রয়োগে প্রসারণ $l$ হবে $\\frac{1}{4}$ অংশ ($l \\propto 1/r^2$); একক আয়তনে শক্তি $= \\frac{1}{2} \\times$ পীড়ন $\\times$ বিকৃতি।"
                },
                {
                    "type_id": "phy_p07_t2",
                    "name": "Type 2: তরলের পৃষ্ঠটান, পৃষ্ঠশক্তি ও ফোঁটা গঠন",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '20-21", "JU '21-22", "GST '21-22", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P05-Q11", "VAR-DU-P06-Q12", "MAD-MAT-Q15"],
                    "core_rule": "পৃষ্ঠটান $T = \\frac{F}{L}$; পৃষ্ঠশক্তি $W = T \\Delta A$। পানির ফোঁটার ক্ষেত্রে পৃষ্ঠশক্তি: $W = T \\times 4\\pi (r_2^2 - r_1^2)$ (১টি উন্মুক্ত তল); সাবানের বুদ্বুদের ক্ষেত্রে ২টি উন্মুক্ত তল থাকায়: $W = T \\times 8\\pi (r_2^2 - r_1^2)$। $n$ সংখ্যক ছোট ফোঁটা ($r$) যুক্ত হয়ে ১টি বড় ফোঁটা ($R$) গঠন করলে আয়তন ধ্রুব থাকে ($R = n^{1/3} r$); ক্ষেত্রফল হ্রাস পাওয়ায় শক্তি মুক্ত হয় এবং তাপমাত্রা বৃদ্ধি পায়: $\\Delta E = 4\\pi T R^3 \\left(\\frac{1}{r} - \\frac{1}{R}\\right)$। কৈশিক নলে তরল আরোহণ: $h = \\frac{2T\\cos\\theta}{r \\rho g}$। কাচ ও বিশুদ্ধ পানির স্পর্শকোণ $8^\\circ$ (প্রায় $0^\\circ$); পারদ ও কাচের স্পর্শকোণ $140^\\circ$।",
                    "speed_elimination": "সাবানের বুদ্বুদের ২টি উন্মুক্ত তল থাকে, তাই কাজের সূত্রে $8\\pi$ গুণ হবে; ছোট ফোঁটা মিলে বড় ফোঁটা হলে তাপমাত্রা বৃদ্ধি পায়।"
                },
                {
                    "type_id": "phy_p07_t3",
                    "name": "Type 3: সান্দ্রতা ও স্টোকসের সূত্র (প্রান্তিক বেগ $v_t$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 28,
                    "past_tags": ["DU '22-23", "DU '18-19", "RU '22-23", "MAT '20", "Agri '21-22"],
                    "qb_question_refs": ["VAR-DU-P08-Q11", "MAD-MAT-Q19"],
                    "core_rule": "নিউটনীয় সান্দ্র বল: $F = -\\eta A \\frac{dv}{dx}$। স্টোকসের সূত্র (সান্দ্র মাধ্যমে $r$ ব্যাসার্ধের গোলকের ওপর বাধা বল): $F = 6\\pi\\eta r v$। গোলকের প্রান্তিক বেগ (Terminal velocity): গোলকের ওজন = প্লবতা বল + সান্দ্র বল $\\implies v_t = \\frac{2}{9}\\frac{r^2 (\\rho - \\sigma) g}{\\eta}$; অর্থাৎ প্রান্তিক বেগ গোলকের ব্যাসার্ধের বর্গের সমানুপাতিক ($v_t \\propto r^2$)। তাপমাত্রা বৃদ্ধি পেলে তরলের সান্দ্রতা হ্রাস পায়, কিন্তু গ্যাসের সান্দ্রতা বৃদ্ধি পায়।",
                    "speed_elimination": "বৃষ্টির ফোঁটার ব্যাসার্ধ দ্বিগুণ হলে প্রান্তিক বেগ ৪ গুণ ($2^2 = 4$) হবে ($v_t \\propto r^2$); তাপমাত্রা বাড়লে তরলের সান্দ্রতা কমে কিন্তু গ্যাসের বাড়ে।"
                }
            ]
        },
        {
            "id": "phy_1st_08",
            "aliases": ["phy_periodic_motion"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৮",
            "title": "পর্যায়বৃত্ত গতি (Periodic Motion)",
            "subtitle": "সরল ছন্দিত স্পন্দন (SHM), দোলনকাল, সরল দোলক ও পাহাড়ে সময় হারানো",
            "total_qb_questions": 460,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p08_t1",
                    "name": "Type 1: সরল ছন্দিত স্পন্দনের ব্যবকলনীয় সমীকরণ ও সরণ-বেগ-ত্বরণ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '18-19", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P01-Q13", "VAR-DU-P01-Q14", "VAR-RU-P03-Q08"],
                    "core_rule": "SHM ব্যবকলনীয় সমীকরণ: $\\frac{d^2 x}{dt^2} + \\omega^2 x = 0$। সরণ $x = A\\sin(\\omega t + \\delta)$। বেগ $v = \\frac{dx}{dt} = \\omega\\sqrt{A^2 - x^2}$; সাম্যাবস্থানে ($x=0$) বেগ সর্বোচ্চ $v_{max} = \\omega A$; বিস্তার প্রান্তে ($x = \\pm A$) বেগ শূন্য। ত্বরণ $a = -\\omega^2 x$; সাম্যাবস্থানে ত্বরণ শূন্য; বিস্তার প্রান্তে ত্বরণ সর্বোচ্চ $a_{max} = \\omega^2 A$। গতিশক্তি $E_k = \\frac{1}{2}m\\omega^2 (A^2 - x^2)$; বিভব শক্তি $E_p = \\frac{1}{2}m\\omega^2 x^2$; মোট শক্তি $E = E_k + E_p = \\frac{1}{2}m\\omega^2 A^2 = \\text{ধ্রুবক}$। যে অবস্থানে গতিশক্তি ও বিভব শক্তি সমান ($E_k = E_p$): $\\frac{1}{2}m\\omega^2(A^2 - x^2) = \\frac{1}{2}m\\omega^2 x^2 \\implies x = \\pm\\frac{A}{\\sqrt{2}} \\approx 0.707 A$।",
                    "speed_elimination": "যে অবস্থানে গতিশক্তি ও বিভব শক্তি সমান হয় তা হলো $x = \\pm\\frac{A}{\\sqrt{2}}$; সাম্যাবস্থানে বেগ সর্বোচ্চ কিন্তু ত্বরণ শূন্য।"
                },
                {
                    "type_id": "phy_p08_t2",
                    "name": "Type 2: সরল দোলক ও সেকেন্ড দোলক",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '20-21", "JU '21-22", "GST '21-22", "MAT '22", "MAT '18"],
                    "qb_question_refs": ["VAR-JnU-P03-Q14", "VAR-DU-P04-Q11", "MAD-MAT-Q07"],
                    "core_rule": "দোলনকাল $T = 2\\pi\\sqrt{\\frac{L}{g}}$ ($L = l + r$ কার্যকর দৈর্ঘ্য)। সেকেন্ড দোলকের দোলনকাল ঠিক ২ সেকেন্ড ($T=2\\text{ s}$, অর্ধ-দোলন ১ সেকেন্ড); প্রমাণ অভিকর্ষে এর কার্যকর দৈর্ঘ্য $L = \\frac{g}{\\pi^2} \\approx 0.993\\text{ m} = 99.3\\text{ cm}$। কার্যকর দৈর্ঘ্য ৪ গুণ করলে দোলনকাল দ্বিগুণ হয় ($T \\propto \\sqrt{L}$)। চাঁদে অভিকর্ষজ ত্বরণ পৃথিবীর $\\frac{1}{6}$ গুণ ($g_m = g/6$), তাই চাঁদে পর্যায়কাল হবে $\\sqrt{6} \\approx 2.45$ গুণ। লিফটে সরল দোলক: উর্ধমুখী ত্বরণে $a$ উঠলে $T = 2\\pi\\sqrt{\\frac{L}{g+a}}$ (দোলনকাল কমে/দ্রুত দোলে); নিম্নমুখী ত্বরণে $T = 2\\pi\\sqrt{\\frac{L}{g-a}}$ (দোলনকাল বাড়ে); মুক্তভাবে পড়ন্ত লিফটে ($a=g$) দোলনকাল অসীম ($T = \\infty$) অর্থাৎ দোলক থামবে।",
                    "speed_elimination": "কার্যকর দৈর্ঘ্য ৪৪% বাড়ালে ($1.44L$) দোলনকাল ২০% বৃদ্ধি পায় ($\sqrt{1.44} = 1.2$); সেকেন্ড দোলকের পর্যায়কাল ২ সেকেন্ড।"
                },
                {
                    "type_id": "phy_p08_t3",
                    "name": "Type 3: পাহাড়ের চূড়ায় বা খনির গভীরে দোলক ঘড়ির সময় হারানো",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '22-23", "DU '19-20", "RU '22-23", "JU '20-21", "GST '20-21", "BUET '17-18"],
                    "qb_question_refs": ["VAR-JnU-P07-Q10", "VAR-DU-P02-Q15", "VAR-GST-P05-Q11"],
                    "core_rule": "১ দিনে সেকেন্ড সংখ্যা $86400\\text{ s}$। ১. পাহাড়ের চূড়ায় $h$ উচ্চতায় দিনে $n$ সেকেন্ড ধীরে চললে/সময় হারালে: $\\frac{T'}{T} = \\frac{86400}{86400 - n} = \\frac{R+h}{R} = 1 + \\frac{h}{R} \\implies h = \\frac{n}{86400 - n} R \\approx \\frac{n}{86400} R$। ২. খনির গভীরে দিনে $n$ সেকেন্ড সময় হারালে: $g' = g\\left(1 - \\frac{h}{R}\\right) \\implies h = \\frac{2n}{86400} R$। ৩. তাপমাত্রা বৃদ্ধির ফলে দৈর্ঘ্য বৃদ্ধি পেলে প্রতি সেকেন্ডে হারানো সময়: $\\Delta t = \\frac{1}{2}\\alpha \\Delta\\theta \\times 86400\\text{ s/day}$।",
                    "speed_elimination": "পাহাড়ে নিয়ে গেলে $g$ কমে, তাই দোলক ঘড়ি সর্বদা ধীরে চলে বা সময় হারায়; পাহাড়ের উচ্চতা $h = \\frac{n}{86400-n}R$।"
                }
            ]
        },
        {
            "id": "phy_1st_09",
            "aliases": ["phy_waves"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ০৯",
            "title": "তরঙ্গ (Waves)",
            "subtitle": "অগ্রগামী তরঙ্গ সমীকরণ, পথ পার্থক্য, বিট ও টানা তারের কম্পন",
            "total_qb_questions": 390,
            "high_yield_score": 97,
            "mega_types": [
                {
                    "type_id": "phy_p09_t1",
                    "name": "Type 1: অগ্রগামী তরঙ্গের সমীকরণ ও দশা পার্থক্য-পথ পার্থক্য",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 34,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '18-19", "RU '21-22", "JU '21-22", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q07", "VAR-DU-P03-Q12", "VAR-RU-P05-Q10"],
                    "core_rule": "অগ্রগামী তরঙ্গের সমীকরণ: $y = A\\sin 2\\pi \\left(\\frac{t}{T} - \\frac{x}{\\lambda}\\right) = A\\sin(\\omega t - k x)$; যেখানে তরঙ্গ বেগ $v = \\frac{\\lambda}{T} = f\\lambda = \\frac{\\omega}{k}$, তরঙ্গ সংখ্যা $k = \\frac{2\\pi}{\\lambda}$। কণার সর্বোচ্চ বেগ $v_{max} = \\omega A$। দশা পার্থক্য ও পথ পার্থক্যের মাস্টার সম্পর্ক: $\\delta = \\frac{2\\pi}{\\lambda} \\times \\Delta x$; দশা পার্থক্য ও সময়ের সম্পর্ক: $\\delta = \\frac{2\\pi}{T} \\times \\Delta t$।",
                    "speed_elimination": "সমীকরণ $y = A\\sin(\\omega t - k x)$ এ তরঙ্গের বেগ $v = \\frac{t \\text{ এর সহগ}}{x \\text{ এর সহগ}} = \\frac{\\omega}{k}$।"
                },
                {
                    "type_id": "phy_p09_t2",
                    "name": "Type 2: স্বরকম্প বা বিট ($N = |f_1 - f_2|$) ও সুরশলাকা সমস্যা",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '22-23", "JU '22-23", "GST '21-22", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P05-Q09", "VAR-DU-P06-Q11", "VAR-GST-P03-Q14"],
                    "core_rule": "বিট সংখ্যা প্রতি সেকেন্ডে: $N = |f_1 - f_2| \\implies f_2 = f_1 \\pm N$। ১. সুরশলাকায় মোম বা ওজন লাগালে ভর বৃদ্ধি পায় ফলে কম্পাঙ্ক কমে ($f \\downarrow$): যদি মোম লাগানোর পর বিট কমে, তবে $f_2 = f_1 + N$; যদি বিট বাড়ে, তবে $f_2 = f_1 - N$। ২. সুরশলাকা ঘষলে বা চেঁছে ফেললে ভর কমে ফলে কম্পাঙ্ক বাড়ে ($f \\uparrow$): যদি বিট কমে, তবে $f_2 = f_1 - N$; যদি বিট বাড়ে, তবে $f_2 = f_1 + N$। শ্রবণের স্থায়িত্বকাল: শব্দের জন্য ০.১ সেকেন্ড (তাই প্রতি সেকেন্ডে ১০টির বেশি বিট পৃথক শোনা যায় না); দৃষ্টির স্থায়িত্বকাল ১/১৬ সেকেন্ড।",
                    "speed_elimination": "মোম লাগালে কম্পাঙ্ক হ্রাস পায়; ঘষলে কম্পাঙ্ক বৃদ্ধি পায়। শ্রবণের অনুভূতির স্থায়িত্বকাল ০.১ সেকেন্ড।"
                },
                {
                    "type_id": "phy_p09_t3",
                    "name": "Type 3: টানা তারের আড় কম্পন ও স্থির তরঙ্গ",
                    "importance": "4-Star",
                    "stars": 4,
                    "repeat_frequency": 24,
                    "past_tags": ["DU '20-21", "RU '20-21", "GST '20-21", "BUET '19-20"],
                    "qb_question_refs": ["VAR-DU-P08-Q12", "VAR-CU-P06-Q15"],
                    "core_rule": "টানা তারের আড় কম্পনের মূল সুরের কম্পাঙ্ক: $f = \\frac{1}{2L}\\sqrt{\\frac{T}{\\mu}}$; যেখানে $T =$ তারের টান, $\\mu =$ প্রতি একক দৈর্ঘ্যের ভর ($m/L = \\pi r^2 \\rho$)। স্থির তরঙ্গের সমীকরণ: $y = 2A\\cos(kx)\\sin(\\omega t)$। দুটি পরপর নিস্পন্দ বিন্দু (Node) বা দুটি সুস্পন্দ বিন্দুর (Antinode) মধ্যবর্তী দূরত্ব $\\frac{\\lambda}{2}$; একটি নিস্পন্দ ও সন্নিহিত সুস্পন্দ বিন্দুর দূরত্ব $\\frac{\\lambda}{4}$।",
                    "speed_elimination": "টান $4$ গুণ করলে কম্পাঙ্ক দ্বিগুণ হয়; দুটি পরপর নিস্পন্দ বিন্দুর দূরত্ব $\\lambda/2$।"
                }
            ]
        },
        {
            "id": "phy_1st_10",
            "aliases": ["phy_ideal_gas"],
            "subject": "Physics",
            "paper": "১ম পত্র",
            "chapter_no": "অধ্যায় ১০",
            "title": "আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব (Ideal Gas & Kinetic Theory)",
            "subtitle": "PV=nRT, গতিতত্ত্বের চাপ সমীকরণ, আরএমএস বেগ, আপেক্ষিক আর্দ্রতা ও শিশিরাংক",
            "total_qb_questions": 450,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p10_t1",
                    "name": "Type 1: গ্যাসের গতিতত্ত্বের চাপ ও আরএমএস বেগ ($c_{rms}$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '20-21", "MAT '20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q14", "VAR-DU-P02-Q10", "VAR-RU-P01-Q11", "MAD-MAT-Q12"],
                    "core_rule": "গতিতত্ত্বের চাপ সমীকরণ: $P = \\frac{1}{3}\\rho c^2 = \\frac{1}{3}\\frac{m N}{V} c^2$। আরএমএস বেগ: $c = \\sqrt{\\frac{3RT}{M}} = \\sqrt{\\frac{3P}{\\rho}} = \\sqrt{\\frac{3k_B T}{m}}$ ($R=8.314, M\\text{ kg/mol}$ তে)। গ্যাস অণুর মোট গতিশক্তি: $E = \\frac{3}{2}nRT = \\frac{3}{2}PV$; ১টি অণুর গড় গতিশক্তি $E_1 = \\frac{3}{2}k_B T$ (বোল্টজম্যান ধ্রুবক $k_B = \\frac{R}{N_A} = 1.38 \\times 10^{-23}\\text{ J/K}$); ১ গ্রাম গ্যাসের গতিশক্তি $E = \\frac{3RT}{2M}$। স্বাধীনতার মাত্রা (Degree of Freedom, $f$): একপরমাণুক ($He, Ne, Ar$) এর $f=3$; দ্বিপরমাণুক ($O_2, N_2, H_2$) এর $f=5$; ত্রিপরমাণুক রৈখিক ($CO_2$) এর $f=5$, অ-রৈখিক ($H_2O, O_3$) এর $f=6$।",
                    "speed_elimination": "একটি গ্যাস অণুর গড় গতিশক্তি কেবল পরম তাপমাত্রার ওপর নির্ভর করে ($E_1 = \\frac{3}{2}k_B T$), গ্যাসের প্রকৃতি বা ভরের ওপর নির্ভর করে না।"
                },
                {
                    "type_id": "phy_p10_t2",
                    "name": "Type 2: হ্রদের তলদেশ থেকে বুদ্বুদ উঠার সমস্যা",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '22-23", "DU '19-20", "RU '21-22", "JU '21-22", "GST '21-22", "BUET '18-19"],
                    "qb_question_refs": ["VAR-JnU-P04-Q09", "VAR-DU-P05-Q12", "VAR-GST-P02-Q15"],
                    "core_rule": "হ্রদের তলদেশে চাপ $P_1 = P + h\\rho g$, আয়তন $V_1$; পৃষ্ঠে চাপ $P_2 = P = 10^5\\text{ Pa}$, আয়তন $V_2$। স্থির তাপমাত্রায়: $P_1 V_1 = P_2 V_2$। যদি বুদ্বুদের আয়তন পৃষ্ঠে উঠে $n$ গুণ হয় ($V_2 = n V_1$): $(P + h\\rho g) V_1 = P (n V_1) \\implies h\\rho g = (n - 1)P \\implies h = \\frac{(n-1)P}{\\rho g}$। যদি ব্যাস বা ব্যাসার্ধ $n$ গুণ হয়, তবে আয়তন হবে $n^3$ গুণ ($V \\propto r^3$), ফলে গভীরতা $h = \\frac{(n^3 - 1)P}{\\rho g}$।",
                    "speed_elimination": "আয়তন ৪ গুণ হলে $h = \\frac{3P}{\\rho g}$; ব্যাস দ্বিগুণ হলে আয়তন $2^3 = 8$ গুণ, তাই $h = \\frac{7P}{\\rho g} \\approx \\frac{7 \\times 10^5}{1000 \\times 9.8} \\approx 71.4\\text{ m}$।"
                },
                {
                    "type_id": "phy_p10_t3",
                    "name": "Type 3: আপেক্ষিক আর্দ্রতা ও গ্লেসিয়ারের উৎপাদক",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '21-22", "DU '18-19", "RU '20-21", "JU '20-21", "MAT '22", "MAT '19"],
                    "qb_question_refs": ["VAR-JnU-P06-Q10", "VAR-DU-P07-Q11", "MAD-MAT-Q14"],
                    "core_rule": "গ্লেসিয়ারের সূত্র: শিশিরাংক $\\theta = \\theta_1 - G(\\theta_1 - \\theta_2)$; যেখানে $\\theta_1 =$ শুষ্ক থার্মোমিটারের পাঠ (বায়ুর তাপমাত্রা), $\\theta_2 =$ সিক্ত থার্মোমিটারের পাঠ, $G =$ শুষ্ক পাঠে গ্লেসিয়ারের উৎপাদক। আপেক্ষিক আর্দ্রতা: $RH = \\frac{f}{F} \\times 100\\%$; যেখানে $f =$ শিশিরাংকে সম্পৃক্ত বাষ্পচাপ, $F =$ বায়ুর তাপমাত্রায় সম্পৃক্ত বাষ্পচাপ। দুটি পাঠের পার্থক্য বেশি হলে বায়ু শুষ্ক এবং বাষ্পায়ন দ্রুত হয় (কাপড় দ্রুত শুকায়); পার্থক্য শূন্য হলে আপেক্ষিক আর্দ্রতা ১০০% এবং বৃষ্টির সম্ভাবনা থাকে।",
                    "speed_elimination": "শুষ্ক ও সিক্ত বাল্বের তাপমাত্রার পার্থক্য শূন্য হলে আপেক্ষিক আর্দ্রতা ১০০% (বায়ু সম্পৃক্ত)।"
                }
            ]
        },

        # =========================================================================
        # PHYSICS 2ND PAPER (পদার্থবিজ্ঞান ২য় পত্র - ১১টি পৃথক অধ্যায়)
        # =========================================================================
        {
            "id": "phy_2nd_01",
            "aliases": ["phy_thermodynamics"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০১",
            "title": "তাপগতিবিদ্যা (Thermodynamics)",
            "subtitle": "তাপগতিবিদ্যার ১ম ও ২য় সূত্র, সমোষ্ণ-রুদ্ধতাপীয় প্রক্রিয়া, কার্নো ইঞ্জিন ও এন্ট্রপি",
            "total_qb_questions": 490,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p11_t1",
                    "name": "Type 1: ১ম সূত্র ($dQ = dU + dW$) ও ৪টি তাপগতীয় প্রক্রিয়া",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q16", "VAR-DU-P01-Q17", "VAR-RU-P02-Q15"],
                    "core_rule": "১ম সূত্র: $dQ = dU + dW = dU + P dV$। ১. সমোষ্ণ প্রক্রিয়া ($T$ ধ্রুবক, $dT=0$): অন্তঃস্থ শক্তির পরিবর্তন $dU = 0 \\implies dQ = dW = nRT\\ln\\left(\\frac{V_2}{V_1}\\right) = nRT\\ln\\left(\\frac{P_1}{P_2}\\right)$ (ধীর প্রক্রিয়া, বয়েলের সূত্র মানে); ২. রুদ্ধতাপীয় প্রক্রিয়া ($dQ = 0$): $dW = -dU = \\frac{nR(T_1 - T_2)}{\\gamma - 1}$; সূত্র: $P V^\\gamma = \\text{ধ্রুবক}$, $T V^{\\gamma-1} = \\text{ধ্রুবক}$, $T^\\gamma P^{1-\\gamma} = \\text{ধ্রুবক}$ (দ্রুত প্রক্রিয়া, যেমন টায়ার ফেটে যাওয়া ও শব্দ সঞ্চালন); ৩. সমআয়তন প্রক্রিয়া ($dV=0$): $dW = 0 \\implies dQ = dU = n C_v dT$; ৪. সমচাপ প্রক্রিয়া: $dQ = n C_p dT$, $dW = P\\Delta V = nR\\Delta T$। রুদ্ধতাপীয় রেখা সমোষ্ণ রেখার চেয়ে $\\gamma$ গুণ খাড়া (Slope: $\\frac{dP}{dV}_{\\text{রুদ্ধ}} = \\gamma \\times \\frac{dP}{dV}_{\\text{সম}}$)।",
                    "speed_elimination": "সমোষ্ণ প্রক্রিয়ায় অন্তঃস্থ শক্তির পরিবর্তন শূন্য ($dU=0$); রুদ্ধতাপীয় রেখা সমোষ্ণ রেখার চেয়ে $\\gamma$ গুণ বেশি খাড়া।"
                },
                {
                    "type_id": "phy_p11_t2",
                    "name": "Type 2: কার্নো ইঞ্জিন ও এর কর্মদক্ষতা ($\eta$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 40,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '21-22", "MAT '22", "MAT '20", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P03-Q15", "VAR-DU-P03-Q16", "VAR-GST-P01-Q20", "MAD-MAT-Q01"],
                    "core_rule": "কার্নো চক্রের ৪টি ধাপ: সমোষ্ণ প্রসারণ, রুদ্ধতাপীয় প্রসারণ, সমোষ্ণ সংকোচন, রুদ্ধতাপীয় সংকোচন। কর্মদক্ষতা: $\\eta = 1 - \\frac{Q_2}{Q_1} = 1 - \\frac{T_2}{T_1} = \\frac{W}{Q_1} = \\frac{Q_1 - Q_2}{Q_1}$ (তাপমাত্রা অবশ্যই কেলভিন এককে)। কর্মদক্ষতা ১০০% করার শর্ত: গ্রাহকের তাপমাত্রা $T_2 = 0\\text{ K}$ অথবা উৎসের তাপমাত্রা $T_1 = \\infty$ যা বাস্তবে অসম্ভব। রেফ্রিজারেটরের কার্যসম্পাদন সহগ: $K = \\frac{Q_2}{W} = \\frac{T_2}{T_1 - T_2}$।",
                    "speed_elimination": "উৎস $T_1$ ও গ্রাহক $T_2$ কেলভিনে নিয়ে $\\eta = \\frac{T_1 - T_2}{T_1} \\times 100\\%$; উৎসের তাপমাত্রা বাড়ালে বা গ্রাহকের তাপমাত্রা কমালে কর্মদক্ষতা বৃদ্ধি পায়।"
                },
                {
                    "type_id": "phy_p11_t3",
                    "name": "Type 3: এন্ট্রপির পরিবর্তন ($\Delta S$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '21-22", "DU '18-19", "RU '20-21", "GST '20-21", "MAT '21", "MAT '17"],
                    "qb_question_refs": ["VAR-JnU-P05-Q15", "VAR-DU-P06-Q15", "MAD-MAT-Q11"],
                    "core_rule": "এন্ট্রপির পরিবর্তন $dS = \\frac{dQ}{T}$ (একক: $\\text{J/K}$)। ১. স্থির তাপমাত্রায় (দশা পরিবর্তন): বরফ গলন $\\Delta S = \\frac{m L_f}{T_0} = \\frac{m \\times 3.36 \\times 10^5}{273}$; পানি বাষ্পীভবন $\\Delta S = \\frac{m L_v}{T_b} = \\frac{m \\times 2.26 \\times 10^6}{373}$। ২. তাপমাত্রা পরিবর্তনে ($T_1$ থেকে $T_2$): $\\Delta S = m s \\ln\\left(\\frac{T_2}{T_1}\\right)$। প্রত্যবর্তী প্রক্রিয়ায় মহাবিশ্বের মোট এন্ট্রপি স্থির থাকে ($\Delta S = 0$); অপ্রত্যবর্তী বা প্রাকৃতিক প্রক্রিয়ায় মহাবিশ্বের এন্ট্রপি সর্বদা বৃদ্ধি পায় ($\Delta S > 0$); পরম শূন্য তাপমাত্রায় বিশুদ্ধ কেলাসের এন্ট্রপি শূন্য (তাপগতিবিদ্যার ৩য় সূত্র)।",
                    "speed_elimination": "প্রত্যবর্তী প্রক্রিয়ায় এন্ট্রপির পরিবর্তন শূন্য; সকল প্রাকৃতিক অপ্রত্যবর্তী প্রক্রিয়ায় এন্ট্রপি ক্রমাগত বৃদ্ধি পায়।"
                }
            ]
        },
        {
            "id": "phy_2nd_02",
            "aliases": ["phy_electrostatics"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০২",
            "title": "স্থির তড়িৎ (Electrostatics)",
            "subtitle": "কুলম্বের সূত্র, তড়িৎ প্রাবল্য ও বিভব, গোলকের বিভব এবং ধারকত্ব",
            "total_qb_questions": 460,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "phy_p12_t1",
                    "name": "Type 1: কুলম্বের সূত্র ও ডাই-ইলেকট্রিক ধ্রুবক",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '22-23", "MAT '20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q17", "VAR-DU-P02-Q16", "VAR-RU-P03-Q15"],
                    "core_rule": "কুলম্বের বল: $F = \\frac{1}{4\\pi\\varepsilon_0 \\kappa}\\frac{q_1 q_2}{r^2}$; যেখানে শূন্য মাধ্যমে $\\frac{1}{4\\pi\\varepsilon_0} = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2\\cdot\\text{C}^{-2}$ এবং $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ C}^2\\cdot\\text{N}^{-1}\\cdot\\text{m}^{-2}$। মাধ্যমে বল: $F_m = \\frac{F_{air}}{\\kappa}$ (পানির ডাই-ইলেকট্রিক ধ্রুবক $\\kappa = 80$, তাই পানিতে আকর্ষণ বল ৮০ গুণ কমে যায়)।",
                    "speed_elimination": "দূরত্ব অর্ধেক করলে আকর্ষণ বল ৪ গুণ হবে ($F \\propto 1/r^2$); মাধ্যমে রাখলে বল $\\kappa$ গুণ হ্রাস পায়।"
                },
                {
                    "type_id": "phy_p12_t2",
                    "name": "Type 2: তড়িৎ প্রাবল্য ও তড়িৎ বিভব ($E = -dV/dr$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '18-19", "RU '22-23", "JU '20-21", "GST '21-22"],
                    "qb_question_refs": ["VAR-JnU-P02-Q17", "VAR-DU-P04-Q14", "VAR-GST-P02-Q17"],
                    "core_rule": "বিন্দু চার্জের প্রাবল্য $E = \\frac{1}{4\\pi\\varepsilon_0}\\frac{q}{r^2}$; বিভব $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{q}{r}$। সম্পর্ক: $E = -\\frac{dV}{dr}$। চার্জিত পরিবাহী গোলক ($R$ ব্যাসার্ধ, চার্জ $Q$): ১. গোলকের বাইরে ($r > R$): $V = \\frac{Q}{4\\pi\\varepsilon_0 r}$, $E = \\frac{Q}{4\\pi\\varepsilon_0 r^2}$; ২. গোলকের পৃষ্ঠে ($r = R$): $V = \\frac{Q}{4\\pi\\varepsilon_0 R}$, $E = \\frac{Q}{4\\pi\\varepsilon_0 R^2}$; ৩. গোলকের অভ্যন্তরে ($r < R$): তড়িৎ প্রাবল্য $E = 0$ (কোনো বলরেখা থাকে না) এবং বিভব পৃষ্ঠের বিভবের সমান ও সর্বত্র ধ্রুবক ($V = \\frac{Q}{4\\pi\\varepsilon_0 R}$)।",
                    "speed_elimination": "চার্জিত গোলকের অভ্যন্তরে যে কোনো বিন্দুতে তড়িৎ প্রাবল্য শূন্য ($E=0$) কিন্তু বিভব পৃষ্ঠের বিভবের সমান ($V = V_{\\text{পৃষ্ঠ}}$)।"
                },
                {
                    "type_id": "phy_p12_t3",
                    "name": "Type 3: সমান্তরাল পাত ধারক ও ধারকের সঞ্চিত শক্তি",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 34,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '20-21", "JU '22-23", "GST '22-23", "MAT '22"],
                    "qb_question_refs": ["VAR-JnU-P04-Q14", "VAR-DU-P06-Q13", "MAD-MAT-Q17"],
                    "core_rule": "ধারকত্ব $C = \\frac{Q}{V}$। সমান্তরাল পাত ধারক: $C = \\frac{\\varepsilon_0 \\kappa A}{d}$ (পাতদ্বয়ের দূরত্ব $d$ কমালে বা ক্ষেত্রফল $A$ বাড়ালে ধারকত্ব বাড়ে)। গোলকীয় পরিবাহীর ধারকত্ব $C = 4\\pi\\varepsilon_0 R$। ধারকের সমবায়: শ্রেণিতে $\\frac{1}{C_s} = \\frac{1}{C_1} + \\frac{1}{C_2}$; সমান্তরালে $C_p = C_1 + C_2$। সঞ্চিত শক্তি: $U = \\frac{1}{2} C V^2 = \\frac{1}{2} Q V = \\frac{Q^2}{2C}$। একক আয়তনে শক্তি $u = \\frac{1}{2}\\varepsilon_0 E^2$।",
                    "speed_elimination": "পাত-দূরত্ব অর্ধেক করলে ধারকত্ব দ্বিগুণ হবে ($C \\propto 1/d$); বিভব দ্বিগুণ করলে সঞ্চিত শক্তি ৪ গুণ বৃদ্ধি পাবে ($U \\propto V^2$)।"
                }
            ]
        },
        {
            "id": "phy_2nd_03",
            "aliases": ["phy_current_electricity"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৩",
            "title": "চল তড়িৎ (Current Electricity)",
            "subtitle": "তুল্য রোধ, কার্শফের সূত্র, হুইটস্টোন ব্রিজ ও সান্টের নীতি",
            "total_qb_questions": 490,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p13_t1",
                    "name": "Type 1: তুল্য রোধ ও কোষের অভ্যন্তরীণ রোধ ($E = I(R+r)$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P01-Q18", "VAR-DU-P01-Q16", "VAR-RU-P02-Q18"],
                    "core_rule": "রোধের সূত্র: $R = \\rho\\frac{L}{A} = \\rho\\frac{L}{\\pi r^2}$। তার টেনে $n$ গুণ লম্বা করলে (আয়তন ধ্রুব): নতুন রোধ $R' = n^2 R$; তারের ব্যাসার্ধ অর্ধেক করলে নতুন রোধ $2^4 = 16$ গুণ হবে। তাপমাত্রা বৃদ্ধি পেলে রোধের পরিবর্তন: $R_T = R_0 (1 + \\alpha T)$। কোষের সমীকরণ: $I = \\frac{E}{R + r} \\implies E = V + I r$ (যেখানে $V = I R$ প্রান্তীয় বিভব, $I r$ হলো অভ্যন্তরীণ ভোল্টেজ পতন/হারানো ভোল্ট)। $n$ টি অভিন্ন কোষের সমবায়: শ্রেণিতে $I_s = \\frac{n E}{R + n r}$; সমান্তরালে $I_p = \\frac{n E}{n R + r}$।",
                    "speed_elimination": "তার টেনে দৈর্ঘ্য দ্বিগুণ করলে রোধ ৪ গুণ ($2^2 = 4$) হবে; ব্যাসার্ধ অর্ধেক করলে রোধ ১৬ গুণ বৃদ্ধি পাবে ($R \\propto 1/r^4$)।"
                },
                {
                    "type_id": "phy_p13_t2",
                    "name": "Type 2: হুইটস্টোন ব্রিজ নীতি ও মিটার ব্রিজ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '22-23", "JU '21-22", "GST '21-22", "BUET '18-19"],
                    "qb_question_refs": ["VAR-JnU-P03-Q16", "VAR-DU-P03-Q15", "VAR-GST-P04-Q15"],
                    "core_rule": "হুইটস্টোন ব্রিজের সাম্যাবস্থার শর্ত (গ্যালভানোমিটার দিয়ে কোনো তড়িৎ প্রবাহিত না হলে $I_g = 0$): $\\frac{P}{Q} = \\frac{R}{S}$। চতুর্থ বাহুর প্রয়োজনীয় রোধ $S = \\frac{Q R}{P}$; বর্তমান রোধ $S'$ হলে এর সাথে কত রোধ শ্রেণিতে বা সমান্তরালে যুক্ত করতে হবে তা হিসাব করা হয় ($S > S'$ হলে শ্রেণিতে $r = S - S'$; $S < S'$ হলে সমান্তরালে $\\frac{1}{r} = \\frac{1}{S} - \\frac{1}{S'}$)। মিটার ব্রিজ (১ মিটার বা ১০০ সেমি তার): $\\frac{P}{Q} = \\frac{l}{100 - l}$। পোস্ট অফিস বক্স হুইটস্টোন ব্রিজ নীতির ওপর ভিত্তি করে তৈরি।",
                    "speed_elimination": "চার বাহুর অনুপাত সমান হলে ($\frac{P}{Q} = \frac{R}{S}$) গ্যালভানোমিটারের মধ্য দিয়ে কোনো বিদ্যুৎ যাবে না ($I_g = 0$)।"
                },
                {
                    "type_id": "phy_p13_t3",
                    "name": "Type 3: সান্টের নীতি ও অ্যামিটার-ভোল্টমিটারের পাল্লা বৃদ্ধি",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '20-21", "JU '20-21", "GST '22-23", "MAT '22", "MAT '19"],
                    "qb_question_refs": ["VAR-JnU-P05-Q16", "VAR-DU-P05-Q15", "MAD-MAT-Q03"],
                    "core_rule": "সান্ট (Shunt): গ্যালভানোমিটার বা অ্যামিটারের সমান্তরালে যুক্ত অতি ক্ষুদ্র মানের রোধ ($S$)। সান্টের মধ্য দিয়ে প্রবাহ $I_s = I \\frac{G}{G+S}$; গ্যালভানোমিটার প্রবাহ $I_g = I \\frac{S}{G+S}$। অ্যামিটারের পাল্লা $n$ গুণ করতে প্রয়োজনীয় সান্ট: $S = \\frac{G}{n - 1}$ (যেখানে $n = I / I_g$ গুণক ক্ষমতা)। ভোল্টমিটারের পাল্লা $n$ গুণ করতে এর শ্রেণিতে যুক্ত উচ্চ রোধ: $R = (n - 1)G$ (যেখানে $n = V / V_g$)। আদর্শ অ্যামিটারের রোধ শূন্য; আদর্শ ভোল্টমিটারের রোধ অসীম।",
                    "speed_elimination": "অ্যামিটারের পাল্লা ১০ গুণ করতে সান্ট $S = \\frac{G}{10-1} = \\frac{G}{9}$; আদর্শ অ্যামিটারের অভ্যন্তরীণ রোধ শূন্য।"
                }
            ]
        },
        {
            "id": "phy_2nd_04",
            "aliases": ["phy_magnetic_effects"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৪",
            "title": "তড়িৎ প্রবাহের চৌম্বক ক্রিয়া ও চুম্বকত্ব (Magnetism)",
            "subtitle": "বায়ো-সাভার্ট সূত্র, লরেঞ্জ বল, সলিনয়েড ও ভূ-চৌম্বক উপাদান",
            "total_qb_questions": 410,
            "high_yield_score": 97,
            "mega_types": [
                {
                    "type_id": "phy_p14_t1",
                    "name": "Type 1: বায়ো-সাভার্ট সূত্র ও বৃত্তাকার কুণ্ডলীর চৌম্বক ক্ষেত্র",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '22-23", "DU '21-22", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P02-Q18", "VAR-DU-P04-Q16"],
                    "core_rule": "বায়ো-সাভার্ট সূত্র: $dB = \\frac{\\mu_0}{4\\pi} \\frac{I dl \\sin\\theta}{r^2}$ (যেখানে $\\frac{\\mu_0}{4\\pi} = 10^{-7}\\text{ T}\\cdot\\text{m}\\cdot\\text{A}^{-1}$)। ১. অসীম দৈর্ঘ্যের সোজা তার থেকে $r$ দূরত্বে চৌম্বক ক্ষেত্র: $B = \\frac{\\mu_0 I}{2\\pi r}$। ২. $N$ পাকের বৃত্তাকার কুণ্ডলীর কেন্দ্রে চৌম্বক ক্ষেত্র: $B = \\frac{\\mu_0 N I}{2 r}$। ৩. সলিনয়েডের অভ্যন্তরে সুষম চৌম্বক ক্ষেত্র: $B = \\mu_0 n I = \\mu_0 \\frac{N}{L} I$। অ্যাম্পিয়ারের সার্কিটাল সূত্র: $\\oint \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{\\text{enclosed}}$।",
                    "speed_elimination": "বৃত্তাকার তারের কেন্দ্রে $B = \\frac{\\mu_0 I}{2r}$; সোজা তারের জন্য নিচে $\\pi$ থাকে ($B = \\frac{\\mu_0 I}{2\\pi r}$)।"
                },
                {
                    "type_id": "phy_p14_t2",
                    "name": "Type 2: লরেঞ্জ বল ও চৌম্বক ক্ষেত্রে চার্জের গতি",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 34,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '20-21", "JU '21-22", "GST '21-22", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P04-Q16", "VAR-DU-P02-Q17", "MAD-MAT-Q22"],
                    "core_rule": "লরেঞ্জ বল: $\\vec{F} = q(\\vec{E} + \\vec{v} \\times \\vec{B})$। কেবল চৌম্বক বল: $F_B = q v B \\sin\\theta$। চার্জ চৌম্বক ক্ষেত্রের সমান্তরালে চললে ($\theta = 0^\\circ$): কোনো বল অনুভব করে না ($F=0$) এবং সমবেগে সরলরেখায় চলে। চার্জ চৌম্বক ক্ষেত্রের সাথে লম্বভাবে ($90^\\circ$) প্রবেশ করলে: বল সর্বদা বেগের সাথে লম্ব হওয়ায় কোনো কাজ করে না ($W=0$, গতিশক্তি ধ্রুব) এবং বৃত্তাকার পথে ঘোরে: $\\frac{m v^2}{r} = q v B \\implies r = \\frac{m v}{q B}$ (পর্যায়কাল $T = \\frac{2\\pi m}{q B}$ বেগের ওপর নির্ভর করে না)। তীর্যক কোণে প্রবেশ করলে গতিপথ হেলিক্স (সর্পিলাকার)। দুটি সমান্তরাল পরিবাহীর মধ্যে একক দৈর্ঘ্যে বল: $\\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi d}$ (একই দিকে প্রবাহ হলে আকর্ষণ, বিপরীত দিকে হলে বিকর্ষণ)।",
                    "speed_elimination": "চৌম্বক বল দ্বারা কৃতকাজ সর্বদা শূন্য ($W=0$, কারণ বল ও সরণ লম্ব); একই দিকে বিদ্যুৎ প্রবাহিত দুটি সমান্তরাল তার পরস্পরকে আকর্ষণ করে।"
                },
                {
                    "type_id": "phy_p14_t3",
                    "name": "Type 3: ভূ-চৌম্বক উপাদান ও ডায়া-প্যারা-ফেরোচুম্বকত্ব",
                    "importance": "4-Star",
                    "stars": 4,
                    "repeat_frequency": 26,
                    "past_tags": ["MAT '22", "MAT '20", "DU '19-20", "RU '22-23"],
                    "qb_question_refs": ["MAD-MAT-Q08", "VAR-DU-P07-Q16"],
                    "core_rule": "ভূ-চৌম্বক উপাদান ৩টি: ১. বিচ্যুতি কোণ (Declination, $\\theta$): ভৌগোলিক মধ্যতল ও চৌম্বক মধ্যতলের মধ্যবর্তী সূক্ষ্মকোণ; ২. বিনতি কোণ (Dip/Inclination, $\\delta$): অনুভূমিক তলের সাথে চৌম্বক শলাকার নতি কোণ (বিষুবরেখায় $\\delta = 0^\\circ$, মেরুতে $\\delta = 90^\\circ$); ৩. অনুভূমিক প্রাবল্য $H = B\\cos\\delta$, উলম্ব প্রাবল্য $V = B\\sin\\delta \\implies \\tan\\delta = \\frac{V}{H}$ ও $B = \\sqrt{H^2 + V^2}$। চৌম্বক পদার্থ: ১. ডায়াচুম্বক (চৌম্বক ক্ষেত্র দ্বারা মৃদু বিকর্ষিত, $\\mu_r < 1$, চৌম্বক প্রবণতা $\\chi < 0$): তামা, রূপা, সোনা, পানি, বিসমাথ; ২. প্যারাচুম্বক (মৃদু আকৃষ্ট, $\\mu_r > 1$, $\\chi > 0$): অ্যালুমিনিয়াম, প্ল্যাটিনাম, অক্সিজেন, সোডিয়াম; ৩. ফেরোচুম্বক (তীব্র আকৃষ্ট, স্থায়ী চুম্বক হয়, ডোমেন তৈরি করে): লোহা, নিকেল, কোবাল্ট। ক্যুরি বিন্দু: যে তাপমাত্রার উপরে ফেরোচুম্বক প্যারাচুম্বকে পরিণত হয় (লোহার ক্যুরি বিন্দু ৭৭০°C)।",
                    "speed_elimination": "বিষুবরেখায় বিনতি কোণ $0^\\circ$; মেরুতে বিনতি কোণ $90^\\circ$; পানি ও তামা ডায়াচৌম্বক পদার্থ।"
                }
            ]
        },
        {
            "id": "phy_2nd_05",
            "aliases": ["phy_electromagnetic_induction"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৫",
            "title": "তাড়িতচৌম্বকীয় আবেশ ও পরিবর্তী প্রবাহ (Induction & AC)",
            "subtitle": "ফ্যারাডের আবেশ সূত্র, লেনজের নীতি, ট্রান্সফরমার এবং AC এর RMS মান",
            "total_qb_questions": 420,
            "high_yield_score": 97,
            "mega_types": [
                {
                    "type_id": "phy_p15_t1",
                    "name": "Type 1: ফ্যারাডে ও লেনজের আবেশ সূত্র এবং স্বকীয়-পারস্পরিক আবেশ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '22-23", "DU '21-22", "RU '21-22", "JU '21-22", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P03-Q17", "VAR-DU-P05-Q14"],
                    "core_rule": "ফ্যারাডের সূত্র: আবিষ্ট তড়িচ্চালক বল $E = -N \\frac{d\\Phi}{dt}$ (ঋণাত্মক চিহ্ন লেনজের সূত্র প্রকাশ করে: আবিষ্ট প্রবাহের দিক এমন হয় যা সৃষ্টির কারণকেই বাধা দেয় - শক্তির সংরক্ষণশীলতা নীতি মানে)। স্বকীয় আবেশ গুণাঙ্ক $L$: $\\Phi = L I \\implies E = -L \\frac{dI}{dt}$ (একক হেনরি, $\\text{H} = \\text{V}\\cdot\\text{s/A}$); আবেশকের সঞ্চিত শক্তি $U = \\frac{1}{2}L I^2$। পারস্পরিক আবেশ গুণাঙ্ক $M$: $E_s = -M \\frac{dI_p}{dt}$।",
                    "speed_elimination": "লেনজের সূত্র শক্তির সংরক্ষণশীলতা সূত্রের রূপান্তর; আবেশকের সঞ্চিত শক্তি $U = \\frac{1}{2}L I^2$।"
                },
                {
                    "type_id": "phy_p15_t2",
                    "name": "Type 2: ট্রান্সফরমারের রূপান্তর নীতি ($V_p/V_s = N_p/N_s = I_s/I_p$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '20-21", "JU '22-23", "GST '21-22", "MAT '22"],
                    "qb_question_refs": ["VAR-JnU-P01-Q19", "VAR-DU-P02-Q18", "MAD-MAT-Q06"],
                    "core_rule": "ট্রান্সফরমার পারস্পরিক আবেশের ওপর ভিত্তি করে কাজ করে (কেবল পরিবর্তী প্রবাহ AC তে চলে, DC তে কাজ করে না)। রূপান্তর অনুপাত: $\\frac{V_p}{V_s} = \\frac{N_p}{N_s} = \\frac{I_s}{I_p}$। স্টেপ-আপ ট্রান্সফরমার (উচ্চধাপী): $N_s > N_p \\implies V_s > V_p$ কিন্তু $I_s < I_p$ (বিভব বাড়ে, তড়িৎ প্রবাহ কমে)। স্টেপ-ডাউন ট্রান্সফরমার (নিম্নধাপী): $N_s < N_p \\implies V_s < V_p$ কিন্তু $I_s > I_p$। আদর্শ ট্রান্সফরমারে ইনপুট ক্ষমতা = আউটপুট ক্ষমতা ($P_p = P_s \\implies V_p I_p = V_s I_s$)। কর্মদক্ষতা $\\eta = \\frac{V_s I_s}{V_p I_p} \\times 100\\%$।",
                    "speed_elimination": "ট্রান্সফরমারে ভোল্টেজ দ্বিগুণ হলে কারেন্ট ঠিক অর্ধেক হয় ($V_p I_p = V_s I_s$); ডিসি (DC) সাপ্লাই দিলে ট্রান্সফরমার পুড়ে যাবে কিন্তু কোনো ভোল্টেজ তৈরি হবে না।"
                },
                {
                    "type_id": "phy_p15_t3",
                    "name": "Type 3: পরিবর্তী প্রবাহের (AC) শীর্ষ মান ও কার্যকর মান (RMS মান)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '22-23", "MAT '21", "GST '20-21"],
                    "qb_question_refs": ["VAR-JnU-P06-Q14", "VAR-DU-P07-Q15"],
                    "core_rule": "পরিবর্তী প্রবাহ: $I = I_0 \\sin(\\omega t)$, $V = V_0 \\sin(\\omega t)$। মূল গড় বর্গ মান (RMS মান): $I_{rms} = \\frac{I_0}{\\sqrt{2}} \\approx 0.707 I_0$; $V_{rms} = \\frac{V_0}{\\sqrt{2}} \\approx 0.707 V_0$। বাংলাদেশে গৃহস্থালির সরবরাহকৃত ২২০ V, ৫০ Hz হলো মূলত $V_{rms} = 220\\text{ V}$, যার শীর্ষ মান $V_0 = \\sqrt{2} \\times 220 \\approx 311.12\\text{ V}$ (তাই ২২০ V ডিসির চেয়ে ২২০ V এসি বেশি বিপজ্জনক)। গড় মান: $I_{avg} = \\frac{2 I_0}{\\pi} \\approx 0.637 I_0$।",
                    "speed_elimination": "২২০ V এসি সাপ্লাইয়ের পিক বা শীর্ষ মান হলো ৩১১.১ ভোল্ট ($V_0 = \\sqrt{2} V_{rms}$); এসি অ্যামিটার ও ভোল্টমিটার সর্বদা RMS মান পরিমাপ করে।"
                }
            ]
        },
        {
            "id": "phy_2nd_06",
            "aliases": ["phy_geometrical_optics"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৬",
            "title": "জ্যামিতিক আলোকবিজ্ঞান (Geometrical Optics)",
            "subtitle": "প্রতিসরণ, প্রিজমের ন্যূনতম বিচ্যুতি, লেন্স প্রস্তুতকারক সূত্র ও দূরবীক্ষণ",
            "total_qb_questions": 430,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "phy_p16_t1",
                    "name": "Type 1: প্রতিসরণাঙ্ক, সংকট কোণ ও পূর্ণ অভ্যন্তরীণ প্রতিফলন",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 34,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "GST '22-23", "MAT '20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q20", "VAR-DU-P03-Q17", "MAD-MAT-Q05"],
                    "core_rule": "স্নেলের সূত্র: $\\mu_1 \\sin i = \\mu_2 \\sin r \\implies \\frac{\\sin i}{\\sin r} = \\frac{\\mu_2}{\\mu_1} = \\frac{v_1}{v_2} = \\frac{\\lambda_1}{\\lambda_2}$ (এক মাধ্যম থেকে অন্য মাধ্যমে আলো গেলে কম্পাঙ্ক $f$ অপরিবর্তিত থাকে কিন্তু বেগ ও তরঙ্গদৈর্ঘ্য পরিবর্তিত হয়)। সংকট কোণ $\\theta_c$: ঘন মাধ্যম থেকে হালকা মাধ্যমে প্রতিসরণের ক্ষেত্রে প্রতিসরণ কোণ $90^\\circ$ হলে: $\\sin\\theta_c = \\frac{1}{\\mu}$ (কাচের জন্য $\\theta_c \\approx 42^\\circ$; হীরকের $\\mu = 2.42 \\implies \\theta_c = 24.4^\\circ$, তাই হীরা বেশি উজ্জ্বল দেখায়)। আপাত গভীরতা: $\\mu = \\frac{\\text{প্রকৃত গভীরতা}}{\\text{আপাত গভীরতা}}$। অপটিক্যাল ফাইবার পূর্ণ অভ্যন্তরীণ প্রতিফলনের ওপর ভিত্তি করে কাজ করে (কোরের প্রতিসরাঙ্ক ক্ল্যাডিংয়ের চেয়ে বেশি)।",
                    "speed_elimination": "আলোর প্রতিসরণে কম্পাঙ্ক অপরিবর্তিত থাকে; হীরা সবচেয়ে বেশি ঝকঝকে দেখায় কারণ এর সংকট কোণ অতি ক্ষুদ্র ($24.4^\\circ$)।"
                },
                {
                    "type_id": "phy_p16_t2",
                    "name": "Type 2: প্রিজমের বিচ্যুতি ও ন্যূনতম বিচ্যুতি কোণ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '20-21", "JU '20-21", "GST '21-22", "BUET '20-21"],
                    "qb_question_refs": ["VAR-JnU-P04-Q17", "VAR-DU-P05-Q16"],
                    "core_rule": "প্রিজমের প্রতিসারক কোণ $A = r_1 + r_2$; বিচ্যুতি কোণ $\\delta = (i_1 + i_2) - A$। ন্যূনতম বিচ্যুতি অবস্থায়: $i_1 = i_2 = i$ এবং $r_1 = r_2 = r = A/2$, ফলে $\\delta = \\delta_m$। প্রিজমের প্রতিসরাঙ্কের সূত্র: $\\mu = \\frac{\\sin\\left(\\frac{A + \\delta_m}{2}\\right)}{\\sin\\left(\\frac{A}{2}\\right)}$। সরু প্রিজমের ক্ষেত্রে ($A < 6^\\circ$): $\\delta = (\\mu - 1)A$।",
                    "speed_elimination": "সমবাহু প্রিজমে ($A=60^\\circ$) ন্যূনতম বিচ্যুতি অবস্থায় প্রতিসরণ কোণ $r = 60/2 = 30^\\circ$।"
                },
                {
                    "type_id": "phy_p16_t3",
                    "name": "Type 3: লেন্স প্রস্তুতকারকের সূত্র ও লেন্সের সমবায়",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '22-23", "DU '18-19", "RU '22-23", "JU '22-23", "MAT '22", "MAT '18"],
                    "qb_question_refs": ["VAR-JnU-P07-Q12", "VAR-DU-P01-Q20", "MAD-MAT-Q10"],
                    "core_rule": "লেন্স প্রস্তুতকারকের সূত্র: $\\frac{1}{f} = (\\mu - 1) \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right)$। বায়ুতে কাচের ($\mu=1.5$) উভোত্তল লেন্সের উভয় পৃষ্ঠের ব্যাসার্ধ $R$ হলে: $f = R$। পানিতে ($\mu_w = 4/3$) নিমজ্জিত করলে ফোকাস দূরত্ব ৪ গুণ বৃদ্ধি পায় ($f_w = 4 f_a$) এবং ক্ষমতা $\\frac{1}{4}$ হয়। লেন্সের ক্ষমতা $P = \\frac{1}{f(\\text{m})} = \\frac{100}{f(\\text{cm})}$ (একক ডায়োপ্টার D)। দুটি পাতলা লেন্সের স্পর্শে সমবায়: $\\frac{1}{F} = \\frac{1}{f_1} + \\frac{1}{f_2} \\implies P = P_1 + P_2$। বিবর্ধন $m = -\\frac{v}{u}$।",
                    "speed_elimination": "বায়ুতে কাচের লেন্সকে পানিতে ডুবালে ফোকাস দূরত্ব ৪ গুণ বৃদ্ধি পায় এবং ক্ষমতা ৪ গুণ কমে যায়।"
                }
            ]
        },
        {
            "id": "phy_2nd_07",
            "aliases": ["phy_physical_optics", "phy_optics"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৭",
            "title": "ভৌত আলোকবিজ্ঞান (Physical Optics)",
            "subtitle": "হাইগেনসের নীতি, ইয়ংয়ের দ্বি-চির ব্যতিচার, একক চিরের অপবর্তন ও সমবর্তন",
            "total_qb_questions": 440,
            "high_yield_score": 98,
            "mega_types": [
                {
                    "type_id": "phy_p17_t1",
                    "name": "Type 1: ইয়ংয়ের দ্বি-চির ব্যতিচার ও ডোরা প্রস্থ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '19-20", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q21", "VAR-DU-P02-Q19", "VAR-RU-P04-Q16"],
                    "core_rule": "চিরদ্বয়ের দূরত্ব $d$ (বা $2a$), চির থেকে পর্দার দূরত্ব $D$, আলোর তরঙ্গদৈর্ঘ্য $\\lambda$। ১. দুটি পরপর উজ্জ্বল বা দুটি অন্ধকার ডোরার কেন্দ্রদ্বয়ের দূরত্ব (ডোরা ব্যবধান): $\\Delta x = \\frac{\\lambda D}{d}$। ২. একটি ডোরার প্রস্থ (অর্ধেক ব্যবধান): $\\beta = \\frac{\\lambda D}{2d} = \\frac{\\Delta x}{2}$। ৩. কেন্দ্রীয় চরম থেকে $n$-তম উজ্জ্বল ডোরার দূরত্ব: $x_n = n \\frac{\\lambda D}{d}$ (পথ পার্থক্য $\\Delta = n\\lambda$); $n$-তম অন্ধকার ডোরার দূরত্ব: $x_n' = (2n - 1) \\frac{\\lambda D}{2d}$ (পথ পার্থক্য $\\Delta = (2n-1)\\frac{\\lambda}{2}$)। ব্যতিচারের তীব্রতা: $I_{max} \\propto (A_1 + A_2)^2$, $I_{min} \\propto (A_1 - A_2)^2$। ব্যতিচার পরীক্ষা পানিতে নিমজ্জিত করলে তরঙ্গদৈর্ঘ্য কমে ($\lambda' = \lambda/\mu$), তাই ডোরার প্রস্থও হ্রাস পায়।",
                    "speed_elimination": "ডোরা ব্যবধান $\\Delta x = \\frac{\\lambda D}{d}$; ডোরা প্রস্থ $\\beta = \\frac{\\lambda D}{2d}$ (ব্যবধানের ঠিক অর্ধেক)।"
                },
                {
                    "type_id": "phy_p17_t2",
                    "name": "Type 2: অপবর্তন (একক চিরের অপবর্তন ও গ্রেটিং)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 34,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '20-21", "JU '21-22", "GST '21-22", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P03-Q18", "VAR-DU-P04-Q17", "VAR-GST-P05-Q15"],
                    "core_rule": "১. একক চিরের ফ্রনহফার অপবর্তন (চিরের প্রস্থ $a$): অবম বা অন্ধকারের শর্ত: $a\\sin\\theta = n\\lambda$ ($n=1,2,3\\dots$); চরম বা উজ্জ্বলের শর্ত: $a\\sin\\theta = (2n+1)\\frac{\\lambda}{2}$। কেন্দ্রীয় চরমের কৌণিক বিস্তার: $2\\theta = 2\\frac{\\lambda}{a}$; রৈখিক বিস্তার $= 2\\frac{\\lambda D}{a}$। ২. অপবর্তন গ্রেটিং (গ্রেটিং ধ্রুবক $d = a + b = \\frac{1}{N}$, যেখানে প্রতি মিটারে দাগ সংখ্যা $N$): চরম বা প্রধান উজ্জ্বল রেখার শর্ত: $d\\sin\\theta = n\\lambda \\implies \\sin\\theta = N n \\lambda$। সর্বোচ্চ অপবর্তন ক্রম: $n_{max} = \\frac{d}{\\lambda} = \\frac{1}{N\\lambda}$ (যেহেতু $\\sin\\theta \\le 1$)।",
                    "speed_elimination": "অপবর্তন গ্রেটিংয়ে উজ্জ্বল ডোরার শর্ত $d\\sin\\theta = n\\lambda$; একক চিরে অবমের শর্ত $a\\sin\\theta = n\\lambda$।"
                },
                {
                    "type_id": "phy_p17_t3",
                    "name": "Type 3: আলোর সমবর্তন, ব্রুস্টারের সূত্র ও মেলাসের সূত্র",
                    "importance": "4-Star",
                    "stars": 4,
                    "repeat_frequency": 25,
                    "past_tags": ["DU '22-23", "DU '18-19", "MAT '21", "GST '20-21"],
                    "qb_question_refs": ["VAR-DU-P06-Q16", "MAD-MAT-Q13"],
                    "core_rule": "সমবর্তন কেবল অনুপ্রস্থ বা আড় তরঙ্গের বৈশিষ্ট্য (অনুদৈর্ঘ্য বা শব্দ তরঙ্গের সমবর্তন হয় না)। ব্রুস্টারের সূত্র: সমবর্তন কোণ $i_p$ হলে $\\tan i_p = \\mu$; সমবর্তন কোণে প্রতিফলিত রশ্মি ও প্রতিসরিত রশ্মি পরস্পর লম্ব হয় ($r + i_p = 90^\\circ$)। মেলাসের সূত্র: সমবর্তক ও বিশ্লেষকের অক্ষদ্বয়ের মধ্যবর্তী কোণ $\\theta$ হলে নির্গত আলোর তীব্রতা $I = I_0 \\cos^2\\theta$ (কোণ $90^\\circ$ হলে কোনো আলো নির্গত হয় না $I=0$)।",
                    "speed_elimination": "সমবর্তন কোণে প্রতিফলিত ও প্রতিসরিত রশ্মির মধ্যবর্তী কোণ সর্বদা $90^\\circ$; সমবর্তন প্রমাণ করে আলো একটি অনুপ্রস্থ তরঙ্গ।"
                }
            ]
        },
        {
            "id": "phy_2nd_08",
            "aliases": ["phy_modern_physics"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৮",
            "title": "আধুনিক পদার্থবিজ্ঞানের সূচনা (Modern Physics)",
            "subtitle": "আপেক্ষিকতা (কাল দীর্ঘায়ন, দৈর্ঘ্য সংকোচন, ভর বৃদ্ধি) ও আলোকতড়িৎ ক্রিয়া",
            "total_qb_questions": 470,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p18_t1",
                    "name": "Type 1: বিশেষ আপেক্ষিকতা তত্ত্ব (কাল দীর্ঘায়ন, দৈর্ঘ্য সংকোচন ও ভর বৃদ্ধি)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 40,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P01-Q22", "VAR-DU-P01-Q21", "VAR-RU-P01-Q18"],
                    "core_rule": "লরেন্টজ রূপান্তর উৎপাদক: $\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}} > 1$। ১. কাল দীর্ঘায়ন (Time dilation): গতিশীল ঘড়ি ধীরে চলে, $t = \\frac{t_0}{\\sqrt{1 - v^2/c^2}} = \\gamma t_0$ ($t > t_0$); ২. দৈর্ঘ্য সংকোচন (Length contraction): গতির অভিমুখে দৈর্ঘ্য হ্রাস পায়, $L = L_0\\sqrt{1 - v^2/c^2} = \\frac{L_0}{\\gamma}$ ($L < L_0$); ৩. ভর বৃদ্ধি: গতিশীল ভর $m = \\frac{m_0}{\\sqrt{1 - v^2/c^2}} = \\gamma m_0$ ($m > m_0$); ৪. ভর-শক্তি সম্পর্ক: মোট শক্তি $E = m c^2 = E_k + m_0 c^2$; গতিশক্তি $E_k = (m - m_0)c^2 = (\\gamma - 1)m_0 c^2$; আপেক্ষিকীয় ভরবেগ $p = m v = \\frac{m_0 v}{\\sqrt{1-v^2/c^2}}$, শক্তি-ভরবেগ সম্পর্ক $E^2 = p^2 c^2 + m_0^2 c^4$।",
                    "speed_elimination": "বেগ $v = 0.6c$ হলে $\\gamma = 1.25$, দৈর্ঘ্য সংকোচন ২০%; বেগ $v = 0.8c$ হলে $\\gamma = 1.67$, দৈর্ঘ্য ৬০% অবশিষ্ট থাকে; ভর দ্বিগুণ ($m=2m_0$) হতে প্রয়োজনীয় বেগ $v = \\frac{\\sqrt{3}}{2}c \\approx 0.866c$।"
                },
                {
                    "type_id": "phy_p18_t2",
                    "name": "Type 2: আলোকতড়িৎ ক্রিয়া ও আইনস্টাইনের সমীকরণ",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '19-20", "RU '20-21", "JU '21-22", "GST '21-22", "MAT '22", "MAT '19", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P04-Q19", "VAR-DU-P03-Q18", "MAD-MAT-Q07"],
                    "core_rule": "ফোটনের শক্তি: $E = h f = \\frac{h c}{\\lambda}$ (১ eV $= 1.6 \\times 10^{-19}\\text{ J}$, $h c \\approx 12400\\text{ eV}\\cdot\\text{Å}$)। আইনস্টাইনের ফটোইলেকট্রিক সমীকরণ: $h f = W_0 + K_{max} = h f_0 + \\frac{1}{2}m v_{max}^2 = h f_0 + e V_s$ (যেখানে $W_0 = h f_0 = \\frac{h c}{\\lambda_0}$ হলো কার্য-অপেক্ষক, $f_0$ হলো সূচনা বা প্রারম্ভ কম্পাঙ্ক, $\\lambda_0$ হলো সূচনা তরঙ্গদৈর্ঘ্য, $V_s$ হলো নিবৃত্তি বিভব/থামানো বিভব)। গুরুত্বপূর্ণ ধর্ম: আপতিত আলোর তীব্রতা বৃদ্ধি করলে নির্গত ইলেকট্রনের সংখ্যা বা ফটোকারেন্ট বাড়ে (গতিশক্তি বাড়ে না); আপতিত আলোর কম্পাঙ্ক বৃদ্ধি করলে ইলেকট্রনের সর্বোচ্চ গতিশক্তি ও নিবৃত্তি বিভব বাড়ে।",
                    "speed_elimination": "আলোর তীব্রতা বাড়ালে কারেন্ট বাড়ে; কম্পাঙ্ক বাড়ালে ইলেকট্রনের বেগ ও নিবৃত্তি বিভব বাড়ে।"
                },
                {
                    "type_id": "phy_p18_t3",
                    "name": "Type 3: ডি-ব্রগলি তরঙ্গদৈর্ঘ্য ও এক্স-রে কম্পটন ক্রিয়া",
                    "importance": "4-Star",
                    "stars": 4,
                    "repeat_frequency": 28,
                    "past_tags": ["DU '21-22", "DU '20-21", "RU '22-23", "GST '20-21"],
                    "qb_question_refs": ["VAR-JnU-P08-Q12", "VAR-DU-P07-Q17"],
                    "core_rule": "১. ডি-ব্রগলি পদার্থ তরঙ্গদৈর্ঘ্য: $\\lambda = \\frac{h}{p} = \\frac{h}{m v} = \\frac{h}{\\sqrt{2m E_k}}$। $V$ ভোল্ট বিভব পার্থক্যে ত্বরান্বিত ইলেকট্রনের জন্য: $\\lambda = \\frac{h}{\\sqrt{2m e V}} = \\frac{1.227}{\\sqrt{V}}\\text{ nm} = \\frac{12.27}{\\sqrt{V}}\\text{ Å}$। ২. কম্পটন ক্রিয়া: এক্স-রে ফোটন স্থির ইলেকট্রনে আঘাত করলে বিক্ষিপ্ত ফোটনের তরঙ্গদৈর্ঘ্য বৃদ্ধি পায়; তরঙ্গদৈর্ঘ্যের বৃদ্ধি $\\Delta \\lambda = \\lambda' - \\lambda = \\frac{h}{m_0 c}(1 - \\cos\\phi) = \\lambda_c (1 - \\cos\\phi)$; কম্পটন তরঙ্গদৈর্ঘ্য $\\lambda_c = \\frac{h}{m_0 c} = 0.0243\\text{ Å} = 2.43 \\times 10^{-12}\\text{ m}$। ৩. হাইজেনবার্গের অনিশ্চয়তা নীতি: $\\Delta x \\cdot \\Delta p \\ge \\frac{h}{4\\pi} = \\frac{\\hbar}{2}$।",
                    "speed_elimination": "ইলেকট্রনের ডি-ব্রগলি $\\lambda = \\frac{12.27}{\\sqrt{V}}\\text{ Å}$; কম্পটন তরঙ্গদৈর্ঘ্য $\\lambda_c = 0.0243\\text{ Å}$।"
                }
            ]
        },
        {
            "id": "phy_2nd_09",
            "aliases": ["phy_nuclear_physics"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ০৯",
            "title": "পরমাণুর মডেল ও নিউক্লিয়ার পদার্থবিজ্ঞান (Atomic & Nuclear Physics)",
            "subtitle": "বোর মডেল, কক্ষপথের ব্যাসার্ধ, তেজস্ক্রিয় ক্ষয় সূত্র, অর্ধায়ু ও বন্ধন শক্তি",
            "total_qb_questions": 480,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p19_t1",
                    "name": "Type 1: বোর পরমাণু মডেল (কক্ষপথের ব্যাসার্ধ, বেগ ও শক্তি)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '21-22", "RU '21-22", "JU '22-23", "GST '22-23", "MAT '21", "BUET '20-21"],
                    "qb_question_refs": ["VAR-JnU-P02-Q22", "VAR-DU-P02-Q22", "VAR-RU-P03-Q18"],
                    "core_rule": "বোরের কৌণিক ভরবেগ শর্ত: $L = m v r = n \\frac{h}{2\\pi}$ ($n = 1, 2, 3\\dots$)। হাইড্রোজেন পরমাণুর $n$-তম কক্ষপথের ব্যাসার্ধ: $r_n = n^2 r_1 = n^2 \\frac{\\varepsilon_0 h^2}{\\pi m e^2}$ (১ম বোর ব্যাসার্ধ $r_1 = 0.53\\text{ Å} = 0.53 \\times 10^{-10}\\text{ m}$, অর্থাৎ $r_n \\propto n^2$)। $n$-তম কক্ষপথে ইলেকট্রনের বেগ: $v_n = \\frac{v_1}{n} = \\frac{e^2}{2\\varepsilon_0 n h}$ ($v_n \\propto 1/n$)। মোট শক্তি: $E_n = -\\frac{13.6}{n^2}\\text{ eV}$ ($E_1 = -13.6\\text{ eV}, E_2 = -3.4\\text{ eV}, E_3 = -1.51\\text{ eV}, E_4 = -0.85\\text{ eV}$)। গতিশক্তি $K_n = -E_n = +\\frac{13.6}{n^2}\\text{ eV}$; বিভব শক্তি $U_n = 2 E_n = -\\frac{27.2}{n^2}\\text{ eV}$।",
                    "speed_elimination": "কক্ষপথের ব্যাসার্ধ $r_n \\propto n^2$ (২য় কক্ষপথের ব্যাসার্ধ ১ম এর ৪ গুণ); শক্তি $E_n = -13.6/n^2\\text{ eV}$।"
                },
                {
                    "type_id": "phy_p19_t2",
                    "name": "Type 2: তেজস্ক্রিয় ক্ষয় সূত্র, অর্ধায়ু ($T_{1/2}$) ও গড় আয়ু ($\\tau$)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 42,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '22-23", "JU '21-22", "GST '22-23", "MAT '22", "MAT '20", "Agri '22-23"],
                    "qb_question_refs": ["VAR-JnU-P01-Q23", "VAR-DU-P04-Q18", "VAR-RU-P02-Q20", "MAD-MAT-Q02"],
                    "core_rule": "তেজস্ক্রিয় ক্ষয় সূত্র: $N = N_0 e^{-\\lambda t}$; অবক্ষয় ধ্রুবক $\\lambda$। অর্ধায়ু: $T_{1/2} = \\frac{\\ln 2}{\\lambda} = \\frac{0.693}{\\lambda}$। গড় আয়ু: $\\tau = \\frac{1}{\\lambda} = \\frac{T_{1/2}}{0.693} \\approx 1.44 T_{1/2}$। $n$ সংখ্যক অর্ধায়ু ($t = n T_{1/2}$) অতিবাহিত হওয়ার পর অবশিষ্ট পরমাণুর সংখ্যা: $N = N_0 \\left(\\frac{1}{2}\\right)^n = \\frac{N_0}{2^{t/T_{1/2}}}$। ক্ষয়প্রাপ্ত অংশ $= N_0 - N = N_0 \\left[1 - \\left(\\frac{1}{2}\\right)^n\\right]$। সক্রিয়তা: $A = \\lambda N$ (একক বেকারেল $\\text{Bq} = 1\\text{ decay/s}$; ১ ক্যুরি $\\text{Ci} = 3.7 \\times 10^{10}\\text{ Bq}$)।",
                    "speed_elimination": "১টি অর্ধায়ুতে অবশিষ্ট থাকে ৫০%, ২টি অর্ধায়ুতে ২৫%, ৩টি অর্ধায়ুতে ১২.৫%, ৪টি অর্ধায়ুতে ৬.২৫%; গড় আয়ু অর্ধায়ুর ১.৪৪ গুণ।"
                },
                {
                    "type_id": "phy_p19_t3",
                    "name": "Type 3: ভর ত্রুটি, নিউক্লীয় বন্ধন শক্তি ও ফিশন-ফিউশন",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '20-21", "JU '20-21", "BUET '19-20"],
                    "qb_question_refs": ["VAR-JnU-P03-Q20", "VAR-DU-P06-Q18"],
                    "core_rule": "ভর ত্রুটি (Mass defect): $\\Delta m = [Z m_p + (A - Z) m_n] - M_{\\text{nucleus}}$। বন্ধন শক্তি: $B.E. = \\Delta m \\times c^2 = \\Delta m(\\text{amu}) \\times 931.5\\text{ MeV}$ (১ amu $= 1.66 \\times 10^{-27}\\text{ kg} = 931.5\\text{ MeV}$)। নিউক্লিয়ন প্রতি বন্ধন শক্তি $= \\frac{B.E.}{A}$; এর সর্বোচ্চ মান লোহা $^{56}\\text{Fe}$ এর ক্ষেত্রে প্রায় $8.8\\text{ MeV}$ (সবচেয়ে সুস্থিত নিউক্লিয়াস)। নিউক্লীয় ফিশন: ভারী নিউক্লিয়াস তাপীয় নিউট্রন দ্বারা আঘাতপ্রাপ্ত হয়ে দুটি মাঝারি নিউক্লিয়াসে ভাঙে (যেমন $^{235}\\text{U} + n \\rightarrow ^{141}\\text{Ba} + ^{92}\\text{Kr} + 3n + 200\\text{ MeV}$ শক্তি)। নিউক্লীয় ফিউশন: অতি উচ্চ তাপমাত্রায় দুটি হালকা নিউক্লিয়াস মিলে ভারী নিউক্লিয়াস গঠন (সূর্যের শক্তি উৎপাদন, হাইড্রোজেন বোমা)।",
                    "speed_elimination": "১ amu ভর বিনষ্ট হলে নির্গত শক্তি ৯৩১.৫ MeV; সর্বাধিক স্থিতিশীল নিউক্লিয়াস $^{56}\\text{Fe}$।"
                }
            ]
        },
        {
            "id": "phy_2nd_10",
            "aliases": ["phy_semiconductor_electronics"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ১০",
            "title": "সেমিকন্ডাক্টর ও ইলেকট্রনিক্স (Semiconductor & Electronics)",
            "subtitle": "p-n ডায়োড, রেকটিফায়ার, ট্রানজিস্টর (α, β সম্পর্ক) ও লজিক গেট",
            "total_qb_questions": 490,
            "high_yield_score": 99,
            "mega_types": [
                {
                    "type_id": "phy_p20_t1",
                    "name": "Type 1: p-n জংশন ডায়োড ও রেকটিফিকেশন",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 36,
                    "past_tags": ["DU '22-23", "DU '21-22", "DU '20-21", "RU '21-22", "JU '22-23", "GST '22-23", "MAT '22", "MAT '20"],
                    "qb_question_refs": ["VAR-JnU-P02-Q23", "VAR-DU-P03-Q20", "MAD-MAT-Q09"],
                    "core_rule": "বিশুদ্ধ অর্ধপরিবাহী (Si, Ge) তে ত্রিযোজী অপদ্রব্য (B, Al, In, Ga) ডোপিং করলে p-টাইপ (সংখ্যাগুরু হোল, সংখ্যালঘিষ্ঠ ইলেকট্রন) এবং পঞ্চযোজী অপদ্রব্য (P, As, Sb) ডোপিং করলে n-টাইপ (সংখ্যাগুরু ইলেকট্রন, সংখ্যালঘিষ্ঠ হোল) তৈরি হয় (উভয় স্ফটিকই সামগ্রিকভাবে তড়িৎ নিরপেক্ষ)। p-n জংশনে নিঃশেষিত স্তর (Depletion layer) গঠিত হয়; সিলিকনের বিভব প্রাচীর ০.৭ V এবং জার্মেনিয়ামের ০.৩ V। ফরওয়ার্ড বায়াসে (p প্রান্তে পজিটিভ, n প্রান্তে নেগেটিভ) নিঃশেষিত স্তর হ্রাস পায় ও তড়িৎ প্রবাহিত হয়; রিভার্স বায়াসে নিঃশেষিত স্তর বৃদ্ধি পায় ও তড়িৎ বন্ধ থাকে। জেনার ডায়োড ভোল্টেজ নিয়ন্ত্রক (Voltage regulator) হিসেবে বিপরীত বায়াসে কাজ করে। অর্ধ-তরঙ্গ একমুখীকরণে ১টি ডায়োড এবং পূর্ণ-তরঙ্গ ব্রিজ একমুখীকরণে ৪টি ডায়োড লাগে।",
                    "speed_elimination": "p-টাইপ ও n-টাইপ সেমিকন্ডাক্টর সামগ্রিকভাবে তড়িৎ নিরপেক্ষ; সিলিকনের বিভব প্রাচীর ০.৭ V ও জার্মেনিয়ামের ০.৩ V।"
                },
                {
                    "type_id": "phy_p20_t2",
                    "name": "Type 2: ট্রানজিস্টর প্রবাহ লাভ ($\\alpha$ ও $\\beta$ এর সম্পর্ক)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 38,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '22-23", "JU '21-22", "GST '21-22", "BUET '21-22"],
                    "qb_question_refs": ["VAR-JnU-P04-Q20", "VAR-DU-P05-Q19", "VAR-GST-P03-Q18"],
                    "core_rule": "ট্রানজিস্টরে তিনটি অঞ্চল: নিঃসারক (Emitter - সর্বাধিক ডোপিংযুক্ত, মাঝারি আকার), ভূমি (Base - অতি পাতলা ও সর্বনিম্ন ডোপিংযুক্ত) এবং সংগ্রাহক (Collector - সবচেয়ে বড় আকার, মাঝারি ডোপিং)। প্রবাহ সমীকরণ: $I_E = I_B + I_C$ (সাধারণত $I_B$ মোট প্রবাহের মাত্র ২-৫% এবং $I_C$ ৯৫-৯৮%)। সাধারণ ভূমি বিন্যাসে প্রবাহ লাভ (Current gain): $\\alpha = \\frac{\\Delta I_C}{\\Delta I_E}$ (সর্বদা $\\alpha < 1$, মান সাধারণত ০.৯৫ - ০.৯৯)। সাধারণ নিঃসারক বিন্যাসে প্রবাহ বিবর্ধন গুণক (Amplification factor): $\\beta = \\frac{\\Delta I_C}{\\Delta I_B}$ (মান সাধারণত ২০ থেকে ৫০০)। $\\alpha$ ও $\\beta$ এর মাস্টার সম্পর্ক: $\\beta = \\frac{\\alpha}{1 - \\alpha}$ এবং $\\alpha = \\frac{\\beta}{1 + \\beta}$।",
                    "speed_elimination": "যদি $\\alpha = 0.98$ হয়, তবে $\\beta = \\frac{0.98}{1 - 0.98} = \\frac{0.98}{0.02} = 49$; $\\alpha$ সর্বদা ১ এর চেয়ে ছোট, $\\beta$ সর্বদা ১ এর চেয়ে বড়।"
                },
                {
                    "type_id": "phy_p20_t3",
                    "name": "Type 3: বুলিয়ান অ্যালজেব্রা ও লজিক গেট (AND, OR, NOT, NAND, NOR, XOR)",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 35,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '20-21", "JU '20-21", "GST '22-23", "MAT '21"],
                    "qb_question_refs": ["VAR-JnU-P05-Q18", "VAR-DU-P07-Q18", "MAD-MAT-Q18"],
                    "core_rule": "মৌলিক গেট: AND ($Y = A \\cdot B$), OR ($Y = A + B$), NOT ($Y = \\bar{A}$)। সার্বজনীন গেট (Universal gates): NAND ($Y = \\overline{A \\cdot B}$) ও NOR ($Y = \\overline{A + B}$)। বিশেষ গেট: XOR ($Y = A \\oplus B = A\\bar{B} + \\bar{A}B$ - বিজোড় সংখ্যক ১ ইনপুট হলে আউটপুট ১); XNOR ($Y = \\overline{A \\oplus B} = AB + \\bar{A}\\bar{B}$)। ডিমরগ্যানের সূত্র: $\\overline{A + B} = \\bar{A} \\cdot \\bar{B}$ এবং $\\overline{A \\cdot B} = \\bar{A} + \\bar{B}$। বুলিয়ান অভেদ: $A + A = A$, $A \\cdot A = A$, $A + 1 = 1$, $A \\cdot 1 = A$, $A + \\bar{A} = 1$, $A \\cdot \\bar{A} = 0$, $\\bar{\\bar{A}} = A$।",
                    "speed_elimination": "সার্বজনীন গেট হলো NAND ও NOR; XOR গেটে দুটি ইনপুট ভিন্ন হলে আউটপুট ১, একই হলে আউটপুট ০।"
                }
            ]
        },
        {
            "id": "phy_2nd_11",
            "aliases": ["phy_astronomy"],
            "subject": "Physics",
            "paper": "২য় পত্র",
            "chapter_no": "অধ্যায় ১১",
            "title": "জ্যোতির্বিজ্ঞান (Astronomy)",
            "subtitle": "চন্দ্রশেখর সীমা, তারার জীবনচক্র, কৃষ্ণগহ্বর, হাবলের সূত্র ও বিগ ব্যাং",
            "total_qb_questions": 320,
            "high_yield_score": 93,
            "mega_types": [
                {
                    "type_id": "phy_p21_t1",
                    "name": "Type 1: তারার জীবনচক্র, শ্বেত বামন ও চন্দ্রশেখর সীমা",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 30,
                    "past_tags": ["DU '22-23", "DU '20-21", "RU '21-22", "JU '21-22", "MAT '20"],
                    "qb_question_refs": ["VAR-DU-P08-Q15", "MAD-MAT-Q21"],
                    "core_rule": "তারার জন্ম প্রোটোস্টার (আদি নক্ষত্র) ও হাইড্রোজেন ফিউশন বিক্রিয়ায় হিলিয়াম সৃষ্টির মাধ্যমে। জ্বালানি শেষ হলে রেড জায়ান্ট (লোহিত দানব) হয়। নক্ষত্রের শেষ পরিণতি নির্ধারণ করে চন্দ্রশেখর সীমা (Chandrasekhar Limit, নোবেলজয়ী সুব্রামানিয়ান চন্দ্রশেখর): $1.4 M_\\odot$ (সূর্যের ভরের ১.৪ গুণ বা প্রায় $2.8 \\times 10^{30}\\text{ kg}$)। ১. যদি কোর ভর $< 1.4 M_\\odot$ হয়: ইলেকট্রন ডিজেনারেসি চাপের কারণে স্থিতিশীল শ্বেত বামন (White Dwarf) তৈরি হয়; ২. যদি ভর $1.4 M_\\odot$ থেকে $3.0 M_\\odot$ হয়: সুপারনোভা বিস্ফোরণের পর নিউট্রন তারা বা পালসার (Pulsar - দ্রুত ঘূর্ণনশীল রেডিও সংকেত নিঃসরণকারী নিউট্রন তারা) গঠিত হয়; ৩. যদি ভর $> 3.0 M_\\odot$ হয়: অবিরাম মহাকর্ষীয় পতনের ফলে কৃষ্ণগহ্বর বা ব্ল্যাক হোল (Black Hole) সৃষ্টি হয়।",
                    "speed_elimination": "চন্দ্রশেখর সীমা হলো সূর্যের ভরের ১.৪ গুণ ($1.4 M_\\odot$); ১.৪ গুণের কম হলে শ্বেত বামন, ৩ গুণের বেশি হলে কৃষ্ণগহ্বর।"
                },
                {
                    "type_id": "phy_p21_t2",
                    "name": "Type 2: কৃষ্ণগহ্বর (সোয়ার্জশিল্ড ব্যাসার্ধ $R_s$) ও হাবলের মহাবিশ্ব সম্প্রসারণ সূত্র",
                    "importance": "5-Star",
                    "stars": 5,
                    "repeat_frequency": 32,
                    "past_tags": ["DU '21-22", "DU '19-20", "RU '20-21", "GST '22-23"],
                    "qb_question_refs": ["VAR-JnU-P06-Q17", "VAR-DU-P04-Q19"],
                    "core_rule": "১. কৃষ্ণগহ্বর ও ঘটনা দিগন্ত (Event Horizon): এমন মহাকর্ষীয় ক্ষেত্র যেখান থেকে আলোও বের হতে পারে না ($v_{escape} \\ge c$); সোয়ার্জশিল্ড ব্যাসার্ধ: $R_s = \\frac{2 G M}{c^2}$ (ব্যাসার্ধ ভরের সমানুপাতিক $R_s \\propto M$)। যদি পৃথিবীকে ব্ল্যাক হোলে পরিণত করতে হয় তবে এর ব্যাসার্ধ হবে প্রায় $9\\text{ mm}$। ২. হাবলের সূত্র: ছায়াপথগুলোর অপসারণ বেগ তাদের দূরত্বের সমানুপাতিক: $v = H_0 d$; যেখানে হাবল ধ্রুবক $H_0 \\approx 70\\text{ km}\\cdot\\text{s}^{-1}\\cdot\\text{Mpc}^{-1}$। মহাবিশ্বের আনুমানিক বয়স (হাবল সময়): $T = \\frac{1}{H_0} \\approx 13.8\\text{ billion years}$। গ্যালাক্সি দূরে সরে যাওয়ার প্রমাণ হিসেবে ডপলার ক্রিয়ার কারণে বর্ণালীর লোহিত অপসরণ (Redshift, $z = \\frac{\\Delta \\lambda}{\\lambda_0}$) পরিলক্ষিত হয়। বিগ ব্যাং তত্ত্বের জনক জর্জ লেমাইত্রে (১৯২৭)।",
                    "speed_elimination": "সোয়ার্জশিল্ড ব্যাসার্ধ $R_s = \\frac{2GM}{c^2}$; হাবলের সূত্রে ছায়াপথের গতিবেগ দূরত্বের সমানুপাতিক ($v = H_0 d$); মহাবিশ্বের বয়স ১৩.৮ বিলিয়ন বছর।"
                }
            ]
        }
    ]
    return chapters
