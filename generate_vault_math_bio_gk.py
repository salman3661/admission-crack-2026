# -*- coding: utf-8 -*-
"""
generate_vault_math_bio_gk.py
Contains all Vault entries for:
- Higher Math (8 chapters, 68 entries)
- Biology (6 chapters, 48 entries)
- English (2 chapters, 22 entries)
- GK (1 chapter, 16 entries)
"""

def get_math_entries():
    entries = []

    # 1. Matrix-Determinants
    entries.extend([
        {
            "id": "v_mat_mat_01",
            "subject": "Higher Math",
            "chapter": "Matrix-Determinants",
            "type": "core_formula",
            "title": "ম্যাট্রিক্সের গুণনের শর্ত ও ক্রম",
            "formula": "A_{m \\times n} \\times B_{n \\times p} = C_{m \\times p}",
            "concept": "১ম ম্যাট্রিক্সের কলাম সংখ্যা ২য় ম্যাট্রিক্সের সারি সংখ্যার সমান হলেই কেবল গুণন সম্ভব। গুণফল ম্যাট্রিক্সের ক্রম হয় ১মটির সারি x ২য়টির কলাম।",
            "hack": "ম্যাট্রিক্স গুণন সাধারণত বিনিময় বিধি মানে না (AB \\neq BA), তবে সংযোগ বিধি (A(BC) = (AB)C) ও বণ্টন বিধি মানে!",
            "trap": "AB সংজ্ঞায়িত হলেও BA সংজ্ঞায়িত নাও হতে পারে (যদি m \\neq p হয়)।",
            "tags": ["matrix multiplication", "order", "ম্যাট্রিক্স গুণন", "ক্রম"]
        },
        {
            "id": "v_mat_mat_02",
            "subject": "Higher Math",
            "chapter": "Matrix-Determinants",
            "type": "shortcut",
            "title": "2x2 ম্যাট্রিক্সের বিপরীত ম্যাট্রিক্স শর্টকাট",
            "formula": "A = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} \\implies A^{-1} = \\frac{1}{ad - bc}\\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix}",
            "concept": "মুখ্য কর্ণের ভুক্তিদ্বয় স্থান বিনিময় করে এবং গৌণ কর্ণের ভুক্তিদ্বয়ের শুধু চিহ্ন পরিবর্তিত হয়।",
            "hack": "তিন সেকেন্ডে উত্তর: মুখ্য কর্ণ সোয়াপ, গৌণ কর্ণ সাইন চেঞ্জ, আর ভাগ হবে নির্ণায়ক মান (ad - bc) দিয়ে!",
            "trap": "যদি নির্ণায়ক মান ad - bc = 0 হয় তবে ম্যাট্রিক্সটি ব্যতিক্রমী (Singular) এবং এর কোনো বিপরীত ম্যাট্রিক্স থাকে না।",
            "tags": ["inverse matrix", "singular", "বিপরীত ম্যাট্রিক্স", "ব্যতিক্রমী"]
        },
        {
            "id": "v_mat_mat_03",
            "subject": "Higher Math",
            "chapter": "Matrix-Determinants",
            "type": "core_formula",
            "title": "নির্ণায়কের স্কেলার গুণনের বৈশিষ্ট্য",
            "formula": "|k A_{n \\times n}| = k^n |A|, \\quad |A^{-1}| = \\frac{1}{|A|}, \\quad |A B| = |A| |B|",
            "concept": "n ক্রমের বর্গ ম্যাট্রিক্সকে k দিয়ে গুণ করলে নির্ণায়ক মান থেকে প্রতি সারি বা কলাম থেকে k কমন এসে k^n গুণ হয়।",
            "hack": "3x3 ম্যাট্রিক্সে |A| = 5 হলে |2A| = 2^3 * 5 = 8 * 5 = 40! k এর ঘাত ম্যাট্রিক্সের ক্রমের সমান।",
            "trap": "ম্যাট্রিক্সে kA মানে সকল ভুক্তিতে k গুণ, কিন্তু নির্ণায়কে k|A| মানে যেকোনো একটি সারি বা কলামে k গুণ।",
            "tags": ["determinant properties", "scalar multiplication", "নির্ণায়ক", "স্কেলার গুণ"]
        },
        {
            "id": "v_mat_mat_04",
            "subject": "Higher Math",
            "chapter": "Matrix-Determinants",
            "type": "shortcut",
            "title": "অনুপুষ্পক/শূন্য নির্ণায়ক শর্ত",
            "formula": "\\text{দুটি সারি বা কলাম সদৃশ বা সমান হলে নির্ণায়ক মান } = 0",
            "concept": "নির্ণায়কের যেকোনো দুটি সারি বা কলাম যদি অভিন্ন হয় অথবা পরস্পর সমানুপাতিক হয় তবে তার মান শূন্য হয়।",
            "hack": "চক্রক্রমিক রাশি সম্বলিত নির্ণায়ক যেমন |1 a a^2; 1 b b^2; 1 c c^2| এর মান সরাসরি (a-b)(b-c)(c-a)!",
            "trap": "সারি বা কলাম পরস্পর অদলবদল করলে একটি ঋণাত্মক চিহ্ন সামনে চলে আসে।",
            "tags": ["zero determinant", "Vandermonde", "নির্ণায়ক মান শূন্য", "চক্রক্রমিক"]
        },
        {
            "id": "v_mat_mat_05",
            "subject": "Higher Math",
            "chapter": "Matrix-Determinants",
            "type": "core_formula",
            "title": "প্রতিসম ও বিপ্রতিসম ম্যাট্রিক্স",
            "formula": "A^T = A \\; (\\text{প্রতিসম}), \\quad A^T = -A \\; (\\text{বিপ্রতিসম / Skew-symmetric})",
            "concept": "বিপ্রতিসম ম্যাট্রিক্সের মুখ্য কর্ণের সকল ভুক্তি সর্বদা শূন্য হতে হয় (a_ii = 0)।",
            "hack": "যেকোনো বিজোড় ক্রমের (যেমন 3x3) বিপ্রতিসম ম্যাট্রিক্সের নির্ণায়ক মান সর্বদা শূন্য (|A| = 0)!",
            "trap": "বিপ্রতিসম ম্যাট্রিক্সের কর্ণের উপাদান শূন্য না হলে সেটি কখনোই বিপ্রতিসম হতে পারে না।",
            "tags": ["symmetric", "skew-symmetric", "প্রতিসম", "বিপ্রতিসম"]
        },
        {
            "id": "v_mat_mat_06",
            "subject": "Higher Math",
            "chapter": "Matrix-Determinants",
            "type": "shortcut",
            "title": "ক্র্যামারের নিয়ম (Cramer's Rule)",
            "formula": "x = \\frac{D_x}{D}, \\quad y = \\frac{D_y}{D}, \\quad z = \\frac{D_z}{D}",
            "concept": "চলকের সহগ দ্বারা গঠিত নির্ণায়ক D অশূন্য (D \\neq 0) হলে একমাত্র সমাধান বিদ্যমান থাকে।",
            "hack": "যদি D = 0 কিন্তু Dx, Dy, Dz এর অন্তত একটি অশূন্য হয় তবে কোনো সমাধান নেই (অসঙ্গতিপূর্ণ)।",
            "trap": "D = 0 এবং Dx = Dy = Dz = 0 হলে অসংখ্য সমাধান বিদ্যমান থাকে।",
            "tags": ["Cramer's rule", "linear equations", "ক্র্যামারের নিয়ম", "সহগ"]
        },
        {
            "id": "v_mat_mat_07",
            "subject": "Higher Math",
            "chapter": "Matrix-Determinants",
            "type": "core_formula",
            "title": "ম্যাট্রিক্সের ট্রেস (Trace)",
            "formula": "\\text{Tr}(A) = \\sum_{i=1}^n a_{ii} = a_{11} + a_{22} + \\dots + a_{nn}",
            "concept": "যেকোনো বর্গ ম্যাট্রিক্সের প্রধান/মুখ্য কর্ণের ভুক্তিগুলোর বীজগণিতীয় যোগফলকে ট্রেস বলে।",
            "hack": "ট্রেসের বৈশিষ্ট্য: Tr(A + B) = Tr(A) + Tr(B) এবং Tr(AB) = Tr(BA)!",
            "trap": "ট্রেস কেবল বর্গ ম্যাট্রিক্সেরই নির্ণয় করা যায়, আয়তাকার ম্যাট্রিক্সের ট্রেস হয় না।",
            "tags": ["trace", "principal diagonal", "ট্রেস", "মুখ্য কর্ণ"]
        },
        {
            "id": "v_mat_mat_08",
            "subject": "Higher Math",
            "chapter": "Matrix-Determinants",
            "type": "shortcut",
            "title": "ম্যাট্রিক্সের ঘাত চক্র (Idempotent, Nilpotent, Involutary)",
            "formula": "A^2 = A \\; (\\text{সমঘাতি}), \\quad A^2 = I \\; (\\text{অভেদঘাতি}), \\quad A^k = O \\; (\\text{শূন্যঘাতি})",
            "concept": "ম্যাট্রিক্সের বিশেষ ঘাতের আচরণ যা বারবার গুণ করার প্রয়োজন ছাড়াই ফলাফল নির্ধারণ করে।",
            "hack": "অভেদঘাতি হলে A^-1 = A (ম্যাট্রিক্স নিজেই নিজের বিপরীত)! সমঘাতি হলে A^n = A!",
            "trap": "A^2 = O হলে ঘাত সূচক (Index of nilpotency) হলো ২।",
            "tags": ["matrix power", "idempotent", "সমঘাতি", "অভেদঘাতি"]
        }
    ])

    # 2. Straight Lines
    entries.extend([
        {
            "id": "v_mat_sl_01",
            "subject": "Higher Math",
            "chapter": "Straight Lines",
            "type": "core_formula",
            "title": "বিন্দু থেকে সরলরেখার লম্ব দূরত্ব",
            "formula": "d = \\frac{|ax_1 + by_1 + c|}{\\sqrt{a^2 + b^2}}",
            "concept": "(x1, y1) বিন্দু থেকে ax + by + c = 0 রেখার লম্ব দূরত্ব। মূলবিন্দু (0, 0) থেকে দূরত্ব d = |c| / \\sqrt{a^2 + b^2}।",
            "hack": "হর \\sqrt{a^2+b^2} এ ৩-৪ থাকলে হর ৫; ৫-১২ থাকলে হর ১৩; ৮-১৫ থাকলে হর ১৭; ৭-২৪ থাকলে হর ২৫ সরাসরি বসান!",
            "trap": "দূরত্ব সর্বদা পরমমান (ধনাত্মক) হবে; কখনো দূরত্বের মান ঋণাত্মক হতে পারে না।",
            "tags": ["perpendicular distance", "straight line", "লম্ব দূরত্ব", "সরলরেখা"]
        },
        {
            "id": "v_mat_sl_02",
            "subject": "Higher Math",
            "chapter": "Straight Lines",
            "type": "shortcut",
            "title": "সমান্তরাল রেখার ৪-সেকেন্ড সোয়াপ রুল",
            "formula": "ax + by = ax_1 + by_1",
            "concept": "প্রদত্ত ax + by + c = 0 রেখার সমান্তরাল এবং (x1, y1) বিন্দুগামী রেখার দ্রুত সমীকরণ।",
            "hack": "x ও y এর সহগ হুবহু একই রেখে ডানপাশে বিন্দুটি সরাসরি বসিয়ে মান নির্ণয় করুন!",
            "trap": "লম্ব রেখার ক্ষেত্রে সহগ সোয়াপ ও মাঝের চিহ্ন উল্টাতে হয়: bx - ay = bx1 - ay1।",
            "tags": ["parallel line", "perpendicular line", "সমান্তরাল রেখা", "সোয়াপ রুল"]
        },
        {
            "id": "v_mat_sl_03",
            "subject": "Higher Math",
            "chapter": "Straight Lines",
            "type": "core_formula",
            "title": "সমান্তরাল সরলরেখাদ্বয়ের মধ্যকার দূরত্ব",
            "formula": "d = \\frac{|c_1 - c_2|}{\\sqrt{a^2 + b^2}}",
            "concept": "উভয় সমীকরণে x ও y এর সহগ অভিন্ন অবস্থায় রূপান্তরের পর ধ্রুবকদ্বয়ের পার্থক্যের পরমমানকে লব্ধি সহগ দিয়ে ভাগ।",
            "hack": "যদি 3x - 4y + 2 = 0 এবং 6x - 8y - 6 = 0 থাকে, তবে ২য়টিকে ২ দিয়ে ভাগ করে 3x - 4y - 3 = 0 বানান; d = |2 - (-3)| / 5 = 5/5 = 1 একক!",
            "trap": "সহগ সমান না করে সরাসরি ধ্রুবক বিয়োগ করলে সম্পূর্ণ ভুল ফলাফল আসবে।",
            "tags": ["parallel distance", "constants", "দূরত্ব", "সমান্তরাল"]
        },
        {
            "id": "v_mat_sl_04",
            "subject": "Higher Math",
            "chapter": "Straight Lines",
            "type": "shortcut",
            "title": "অক্ষদ্বয় দ্বারা কর্তিত ত্রিভুজের ক্ষেত্রফল",
            "formula": "\\text{Area} = \\frac{c^2}{2|ab|} \\quad (ax + by + c = 0 \\text{ রেখার জন্য})",
            "concept": "রেখাটি অক্ষদ্বয়কে (-c/a, 0) এবং (0, -c/b) বিন্দুতে ছেদ করে, ফলে সমকোণী ত্রিভুজ গঠিত হয়।",
            "hack": "3x + 4y = 12 রেখার জন্য c = 12, a = 3, b = 4 \\implies \\text{Area} = 12^2 / (2 * 12) = 6 বর্গ একক!",
            "trap": "সমীকরণের সব পদকে একপাশে এনে ধ্রুবক c এর মান নির্ধারণ করতে হবে।",
            "tags": ["intercept triangle", "area", "ক্ষেত্রফল", "ছেদিতাংশ"]
        },
        {
            "id": "v_mat_sl_05",
            "subject": "Higher Math",
            "chapter": "Straight Lines",
            "type": "core_formula",
            "title": "মধ্যবর্তী কোণ ও লম্ব/সমান্তরাল শর্ত",
            "formula": "\\tan\\theta = \\pm\\frac{m_1 - m_2}{1 + m_1 m_2}, \\quad m_1 m_2 = -1 \\; (\\text{লম্ব}), \\quad m_1 = m_2 \\; (\\text{সমান্তরাল})",
            "concept": "ঢাল m = -a/b (ax + by + c = 0 রেখার জন্য)।",
            "hack": "সূক্ষ্মকোণ চাইলে ধনুচিহ্ন প্লাস (+) নিতে হবে; স্থূলকোণ চাইলে ঋণাত্মক (-) চিহ্ন নিতে হবে।",
            "trap": "দুটি রেখার ঢালের গুণফল -1 হলে তারা পরস্পর লম্ব; সহগ দিয়ে বললে a1 a2 + b1 b2 = 0।",
            "tags": ["angle between lines", "slope", "ঢাল", "মধ্যবর্তী কোণ", "লম্ব শর্ত"]
        },
        {
            "id": "v_mat_sl_06",
            "subject": "Higher Math",
            "chapter": "Straight Lines",
            "type": "shortcut",
            "title": "ছেদবিন্দুর মধ্যবিন্দু জানা থাকলে রেখার সমীকরণ",
            "formula": "\\frac{x}{\\alpha} + \\frac{y}{\\beta} = 2 \\quad (\\text{মধ্যবিন্দু } (\\alpha, \\beta) \\text{ হলে})",
            "concept": "অক্ষদ্বয়ের মধ্যবর্তী খণ্ডিতাংশের মধ্যবিন্দু যদি (\\alpha, \\beta) হয় তবে অক্ষের ছেদাংশদ্বয় হয় 2\\alpha ও 2\\beta।",
            "hack": "মধ্যবিন্দু (2, 3) হলে সরাসরি x/2 + y/3 = 2 \\implies 3x + 2y = 12!",
            "trap": "মধ্যবিন্দু না দিয়ে যদি বলে বিন্দুটি খণ্ডিতাংশকে 2:1 অনুপাতে অন্তর্বিভক্ত করে, তবে সাধারণ অনুপাত সূত্র ব্যবহার করতে হবে।",
            "tags": ["midpoint", "line equation", "মধ্যবিন্দু", "সরলরেখা"]
        },
        {
            "id": "v_mat_sl_07",
            "subject": "Higher Math",
            "chapter": "Straight Lines",
            "type": "core_formula",
            "title": "ত্রিভুজের ভরকেন্দ্র ও অন্তর্বিভক্তিকরণ",
            "formula": "G = \\left(\\frac{x_1 + x_2 + x_3}{3}, \\frac{y_1 + y_2 + y_3}{3}\\right), \\quad P = \\left(\\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2}\\right)",
            "concept": "ভরকেন্দ্র ত্রিভুজের প্রতিটি মধ্যমাকে ২ : ১ অনুপাতে অন্তর্বিভক্ত করে।",
            "hack": "বহির্বিভক্তির ক্ষেত্রে সূত্রে প্লাস চিহ্নের স্থলে মাইনাস (-) চিহ্ন বসবে।",
            "trap": "অনুপাত m1 : m2 এর সাথে বিপরীত বিন্দুর স্থানাঙ্ক গুণ হয় (m1 এর সাথে x2, m2 এর সাথে x1)।",
            "tags": ["centroid", "internal division", "ভরকেন্দ্র", "অন্তর্বিভক্ত"]
        },
        {
            "id": "v_mat_sl_08",
            "subject": "Higher Math",
            "chapter": "Straight Lines",
            "type": "shortcut",
            "title": "বিন্দুর সরলরেখার সাপেক্ষে প্রতিবিম্ব",
            "formula": "\\frac{x' - x_1}{a} = \\frac{y' - y_1}{b} = -2\\left(\\frac{ax_1 + by_1 + c}{a^2 + b^2}\\right)",
            "concept": "(x1, y1) বিন্দুর ax + by + c = 0 রেখার সাপেক্ষে প্রতিবিম্ব বিন্দু (x', y') নির্ণয়।",
            "hack": "যদি কেবল পাদবিন্দু (Foot of perpendicular) চায়, তবে সামনে -2 এর স্থলে শুধু -1 বসবে!",
            "trap": "y = x রেখার সাপেক্ষে প্রতিবিম্ব চাইলে স্থানাঙ্ক সোয়াপ হয় (x, y) -> (y, x); y = -x রেখায় (-y, -x) হয়।",
            "tags": ["reflection", "foot of perpendicular", "প্রতিবিম্ব", "পাদবিন্দু"]
        }
    ])

    # 3. Circles
    entries.extend([
        {
            "id": "v_mat_cir_01",
            "subject": "Higher Math",
            "chapter": "Circles",
            "type": "core_formula",
            "title": "বৃত্তের সাধারণ সমীকরণ ও কেন্দ্র-ব্যাসার্ধ",
            "formula": "x^2 + y^2 + 2gx + 2fy + c = 0 \\implies \\text{কেন্দ্র } (-g, -f), \\quad r = \\sqrt{g^2 + f^2 - c}",
            "concept": "বৃত্ত হওয়ার শর্ত: x^2 ও y^2 এর সহগ সমান ও অশূন্য হতে হবে এবং xy সম্বলিত কোনো পদ থাকবে না (h = 0)।",
            "hack": "x এর সহগকে -2 দিয়ে ভাগ করলে কেন্দ্রের x এবং y এর সহগকে -2 দিয়ে ভাগ করলে কেন্দ্রের y পাওয়া যায়!",
            "trap": "x^2 ও y^2 এর সহগ 1 না থাকলে আগে তা দিয়ে পুরো সমীকরণকে ভাগ করে নিতে হবে, নতুবা কেন্দ্র ও ব্যাসার্ধ ভুল আসবে।",
            "tags": ["circle equation", "center", "radius", "বৃত্ত", "কেন্দ্র", "ব্যাসার্ধ"]
        },
        {
            "id": "v_mat_cir_02",
            "subject": "Higher Math",
            "chapter": "Circles",
            "type": "shortcut",
            "title": "বৃত্তের অক্ষ স্পর্শের শর্ত",
            "formula": "x\\text{-অক্ষ স্পর্শ: } g^2 = c, \\; r = |f|; \\quad y\\text{-অক্ষ স্পর্শ: } f^2 = c, \\; r = |g|",
            "concept": "উভয় অক্ষ স্পর্শ করলে g^2 = f^2 = c এবং ব্যাসার্ধ r = |g| = |f| হয়।",
            "hack": "x-অক্ষের খণ্ডিতাংশ = 2\\sqrt{g^2 - c}; y-অক্ষের খণ্ডিতাংশ = 2\\sqrt{f^2 - c}!",
            "trap": "স্পর্শ করলে খণ্ডিতাংশ শূন্য হয় বিধায় রুটের ভেতরের অংশ g^2 - c = 0 হয়।",
            "tags": ["axis tangent", "intercept", "অক্ষ স্পর্শ", "খণ্ডিতাংশ"]
        },
        {
            "id": "v_mat_cir_03",
            "subject": "Higher Math",
            "chapter": "Circles",
            "type": "core_formula",
            "title": "বৃত্তে সরলরেখা স্পর্শক হওয়ার শর্ত",
            "formula": "d = r \\iff \\frac{|ah + bk + c|}{\\sqrt{a^2 + b^2}} = r",
            "concept": "বৃত্তের কেন্দ্র (h, k) থেকে কোনো রেখার লম্ব দূরত্ব বৃত্তের ব্যাসার্ধের সমান হলে রেখাটি স্পর্শক হয়।",
            "hack": "x^2 + y^2 = a^2 বৃত্তে y = mx + c রেখা স্পর্শক হওয়ার শর্ত: c = \\pm a\\sqrt{1 + m^2}!",
            "trap": "যদি d < r হয় তবে রেখাটি বৃত্তকে দুটি বিন্দুতে ছেদ করে (ছেদক); d > r হলে রেখাটি বৃত্তের বাইরে থাকে।",
            "tags": ["tangent condition", "circle", "স্পর্শকের শর্ত"]
        },
        {
            "id": "v_mat_cir_04",
            "subject": "Higher Math",
            "chapter": "Circles",
            "type": "shortcut",
            "title": "বৃত্তের স্পর্শকের দৈর্ঘ্য (\\sqrt{S1})",
            "formula": "L = \\sqrt{x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c}",
            "concept": "বহিঃস্থ বিন্দু (x1, y1) থেকে বৃত্তে অঙ্কিত স্পর্শকের দৈর্ঘ্য।",
            "hack": "প্রদত্ত বিন্দুটি সরাসরি বৃত্তের সমীকরণের বামপাশে বসিয়ে বর্গমূল নিলেই স্পর্শকের দৈর্ঘ্য পাওয়া যায়!",
            "trap": "যদি রুটের ভেতরের মান শূন্য আসে তবে বিন্দুটি বৃত্তের ওপর অবস্থিত; ঋণাত্মক আসলে বৃত্তের ভেতরে অবস্থিত (স্পর্শক অসম্ভব)।",
            "tags": ["tangent length", "S1", "স্পর্শকের দৈর্ঘ্য"]
        },
        {
            "id": "v_mat_cir_05",
            "subject": "Higher Math",
            "chapter": "Circles",
            "type": "core_formula",
            "title": "ব্যাসদ্বয়ের প্রান্তবিন্দু জানা থাকলে বৃত্তের সমীকরণ",
            "formula": "(x - x_1)(x - x_2) + (y - y_1)(y - y_2) = 0",
            "concept": "ব্যাসের প্রান্তবিন্দুদ্বয় (x1, y1) ও (x2, y2) দ্বারা পরিধিতে উৎপন্ন কোণ এক সমকোণ (90°)।",
            "hack": "বৃত্তের কেন্দ্র সরাসরি মধ্যবিন্দু ((x1+x2)/2, (y1+y2)/2) এবং ব্যাস হলো বিন্দুদ্বয়ের মধ্যবর্তী দূরত্ব!",
            "trap": "ব্যাসদ্বয়ের প্রান্তবিন্দু বলা থাকলে এই সূত্র ব্যবহার সবচেয়ে দ্রুত, কেন্দ্র-ব্যাসার্ধ আলাদা বের করার প্রয়োজন নেই।",
            "tags": ["diameter endpoints", "circle", "ব্যাসের প্রান্তবিন্দু"]
        },
        {
            "id": "v_mat_cir_06",
            "subject": "Higher Math",
            "chapter": "Circles",
            "type": "shortcut",
            "title": "দুই বৃত্তের সাধারণ জ্যা ও স্পর্শক",
            "formula": "S_1 - S_2 = 0",
            "concept": "দুটি বৃত্তের সমীকরণের বিয়োগফল একটি ১-ঘাতের সরলরেখা নির্দেশ করে যা তাদের সাধারণ জ্যা বা সাধারণ স্পর্শকের সমীকরণ।",
            "hack": "উভয় বৃত্ত পরস্পরকে স্পর্শ করলে S1 - S2 = 0 সরাসরি তাদের সাধারণ স্পর্শকের সমীকরণ প্রদান করে!",
            "trap": "বিয়োগ করার পূর্বে অবশ্যই উভয় বৃত্তে x^2 ও y^2 এর সহগ ১ বানিয়ে নিতে হবে।",
            "tags": ["common chord", "radical axis", "সাধারণ জ্যা", "সাধারণ স্পর্শক"]
        },
        {
            "id": "v_mat_cir_07",
            "subject": "Higher Math",
            "chapter": "Circles",
            "type": "core_formula",
            "title": "বৃত্তের জ্যা-এর দৈর্ঘ্য",
            "formula": "\\text{জ্যা-এর দৈর্ঘ্য} = 2\\sqrt{r^2 - d^2}",
            "concept": "কেন্দ্র থেকে জ্যা-এর লম্ব দূরত্ব d এবং বৃত্তের ব্যাসার্ধ r হলে পিথাগোরাস প্রয়োগে জ্যা পাওয়া যায়।",
            "hack": "d = 0 হলে জ্যা-এর দৈর্ঘ্য 2r (সর্ববৃহৎ জ্যা বা ব্যাস); d = r হলে জ্যা-এর দৈর্ঘ্য শূন্য (স্পর্শক)!",
            "trap": "জ্যা-এর মধ্যবিন্দু ও কেন্দ্রের সংযোগ রেখা জ্যা-এর ওপর সর্বদা লম্ব হয়।",
            "tags": ["chord length", "perpendicular", "জ্যা-এর দৈর্ঘ্য"]
        },
        {
            "id": "v_mat_cir_08",
            "subject": "Higher Math",
            "chapter": "Circles",
            "type": "shortcut",
            "title": "দুই বৃত্তের স্পর্শ ও সাধারণ স্পর্শক সংখ্যা",
            "formula": "C_1 C_2 = r_1 + r_2 \\; (\\text{বহিঃস্পর্শ, ৩টি}), \\quad C_1 C_2 = |r_1 - r_2| \\; (\\text{অন্তঃস্পর্শ, ১টি})",
            "concept": "কেন্দ্রদ্বয়ের দূরত্ব d এবং ব্যাসার্ধের যোগফল বা বিয়োগফলের সম্পর্কের ওপর স্পর্শক সংখ্যা নির্ভর করে।",
            "hack": "d > r1+r2 হলে স্পর্শক ৪টি; d = r1+r2 হলে ৩টি; ছেদ করলে ২টি; অন্তঃস্পর্শে ১টি; ভেতরে থাকলে ০টি!",
            "trap": "অন্তঃস্পর্শের ক্ষেত্রে কেন্দ্রদ্বয়ের দূরত্ব ব্যাসার্ধদ্বয়ের পরম বিয়োগফলের সমান হয়।",
            "tags": ["circle intersection", "tangents count", "বহিঃস্পর্শ", "অন্তঃস্পর্শ"]
        }
    ])

    # 4. Conics (কণিক)
    entries.extend([
        {
            "id": "v_mat_con_01",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "core_formula",
            "title": "কণিক শনাক্তকরণ শর্ত ও উৎকেন্দ্রিকতা (e)",
            "formula": "e = 1 \\; (\\text{পরাবৃত্ত}), \\quad 0 < e < 1 \\; (\\text{উপবৃত্ত}), \\quad e > 1 \\; (\\text{অধিবৃত্ত}), \\quad e = \\sqrt{2} \\; (\\text{সমপরাবৃত্ত})",
            "concept": "উপকেন্দ্র থেকে দূরত্ব (SP) এবং নিয়ামক রেখা থেকে দূরত্বের (PM) অনুপাত ধ্রুবক e (SP = e PM)।",
            "hack": "2য় মাত্রার সাধারণ সমীকরণ ax^2 + 2hxy + by^2 + ... এ: h^2 = ab (পরাবৃত্ত); h^2 < ab (উপবৃত্ত); h^2 > ab (অধিবৃত্ত)!",
            "trap": "e = 0 হলে তা একটি বৃত্ত নির্দেশ করে (উপবৃত্তের বিশেষ রূপ)।",
            "tags": ["eccentricity", "conics classification", "উৎকেন্দ্রিকতা", "পরাবৃত্ত", "উপবৃত্ত", "অধিবৃত্ত"]
        },
        {
            "id": "v_mat_con_02",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "core_formula",
            "title": "পরাবৃত্তের উপাদান ও সমীকরণ (y^2 = 4ax)",
            "formula": "\\text{শীর্ষ } (0,0), \\; \\text{উপকেন্দ্র } (a,0), \\; \\text{নিয়ামক } x = -a, \\; \\text{লম্ব } = |4a|, \\; \\text{ফোকাল দূরত্ব } = x_1 + a",
            "concept": "নিয়ামক ও উপকেন্দ্রের ঠিক মাঝামাঝি বিন্দু হলো শীর্ষবিন্দু। উপকেন্দ্রিক লম্বের দৈর্ঘ্য সর্বদা |4a|।",
            "hack": "x^2 = 4ay হলে সবকিছু উল্টে y অক্ষে যাবে: উপকেন্দ্র (0, a), নিয়ামক y = -a, ফোকাল দূরত্ব y1 + a!",
            "trap": "শীর্ষবিন্দু মূলবিন্দুতে না থাকলে ক্যালকুলাসে আংশিক অন্তরীকরণ (dy/dx = 0) করে শীর্ষ দ্রুত বের করা যায়।",
            "tags": ["parabola", "focus", "directrix", "পরাবৃত্ত", "উপকেন্দ্র", "নিয়ামক"]
        },
        {
            "id": "v_mat_con_03",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "shortcut",
            "title": "উপবৃত্তের উৎকেন্দ্রিকতা শর্টকাট (e)",
            "formula": "e = \\sqrt{\\frac{\\text{বড় হর} - \\text{ছোট হর}}{\\text{বড় হর}}} = \\sqrt{1 - \\frac{b^2}{a^2}} \\; (a > b)",
            "concept": "উপবৃত্তের প্রমিত রূপ x^2/a^2 + y^2/b^2 = 1।",
            "hack": "9x^2 + 16y^2 = 144 \\implies x^2/16 + y^2/9 = 1 \\implies e = \\sqrt{(16-9)/16} = \\sqrt{7}/4! চার সেকেন্ডে উত্তর!",
            "trap": "যদি b > a হয় তবে হর a^2 এর স্থলে b^2 হবে: e = \\sqrt{1 - a^2/b^2} এবং উপকেন্দ্র y অক্ষে (0, \\pm be) বসবে।",
            "tags": ["ellipse eccentricity", "shortcut", "উপবৃত্ত", "উৎকেন্দ্রিকতা"]
        },
        {
            "id": "v_mat_con_04",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "core_formula",
            "title": "উপবৃত্তের উপকেন্দ্রিক লম্ব ও ফোকাল দূরত্বের যোগফল",
            "formula": "L = \\frac{2b^2}{a} \\; (a > b), \\quad SP + S'P = 2a \\; (\\text{ধ্রুবক})",
            "concept": "উপবৃত্তের পরিধির যেকোনো বিন্দু থেকে দুটি উপকেন্দ্রের দূরত্বের যোগফল সর্বদা বৃহৎ অক্ষের দৈর্ঘ্যের (2a) সমান।",
            "hack": "উপবৃত্তের ক্ষেত্রফল = \\pi ab! বৃত্তের ক্ষেত্রে a = b হলে ক্ষেত্রফল \\pi a^2 হয়।",
            "trap": "b > a হলে লম্ব হবে 2a^2 / b এবং ফোকাল দূরত্বের যোগফল হবে 2b!",
            "tags": ["latus rectum", "focal sum", "উপকেন্দ্রিক লম্ব", "বৃহৎ অক্ষ"]
        },
        {
            "id": "v_mat_con_05",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "core_formula",
            "title": "অধিবৃত্তের উৎকেন্দ্রিকতা ও উপাদান",
            "formula": "e = \\sqrt{1 + \\frac{b^2}{a^2}} = \\frac{\\sqrt{a^2 + b^2}}{a}, \\quad |SP - S'P| = 2a",
            "concept": "অধিবৃত্তে উপকেন্দ্রদ্বয় থেকে দূরত্বের পরম বিয়োগফল আড় অক্ষের দৈর্ঘ্যের (2a) সমান।",
            "hack": "উৎকেন্দ্রিকতা সর্বদা e > 1 হবে; রুটের ভেতরে প্লাস চিহ্ন থাকে।",
            "trap": "অধিবৃত্তে কে বড় (a নাকি b) তা দেখে আড় অক্ষ নির্ধারণ হয় না; যার চিহ্ন প্লাস আড় অক্ষ সেই অক্ষ বরাবর হয়!",
            "tags": ["hyperbola", "eccentricity", "অধিবৃত্ত", "আড় অক্ষ"]
        },
        {
            "id": "v_mat_con_06",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "shortcut",
            "title": "অনুবন্ধী অধিবৃত্তের উৎকেন্দ্রিকতা সম্পর্ক",
            "formula": "\\frac{1}{e_1^2} + \\frac{1}{e_2^2} = 1",
            "concept": "একটি অধিবৃত্ত ও তার অনুবন্ধী অধিবৃত্তের উৎকেন্দ্রিকতার বর্গের বিপরীতের যোগফল সর্বদা ১।",
            "hack": "৩-৪-৫ পাইথাগোরিয়ান ট্রিপলেট: e1 = 5/3 হলে e2 = 5/4; অথবা e1 = 5/4 হলে e2 = 5/3!",
            "trap": "সমপরাবৃত্তের ক্ষেত্রে e1 = \\sqrt{2} এবং e2 = \\sqrt{2} (উভয় সমান)।",
            "tags": ["conjugate hyperbola", "triplet", "অনুবন্ধী অধিবৃত্ত"]
        },
        {
            "id": "v_mat_con_07",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "core_formula",
            "title": "অধিবৃত্তের অসীমটোট (Asymptotes)",
            "formula": "y = \\pm \\frac{b}{a}x \\implies \\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 0",
            "concept": "অসীমটোট হলো এমন সরলরেখা যা অধিবৃত্তকে অসীমে স্পর্শ করে এবং এর কেন্দ্রগামী হয়।",
            "hack": "অধিবৃত্তের সমীকরণের ধ্রুবক ১ এর স্থলে ০ বসালেই একজোড়া অসীমটোটের সমীকরণ পাওয়া যায়!",
            "trap": "সমপরাবৃত্তে a = b হওয়ায় অসীমটোটদ্বয় y = \\pm x, যা পরস্পর লম্ব (90°)।",
            "tags": ["asymptotes", "hyperbola", "অসীমটোট"]
        },
        {
            "id": "v_mat_con_08",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "shortcut",
            "title": "কণিকের নিয়ামক বৃত্ত (Director Circle)",
            "formula": "\\text{বৃত্ত: } x^2 + y^2 = 2a^2, \\quad \\text{উপবৃত্ত: } x^2 + y^2 = a^2 + b^2, \\quad \\text{অধিবৃত্ত: } x^2 + y^2 = a^2 - b^2",
            "concept": "কণিকের ওপর অঙ্কিত পরস্পর লম্ব স্পর্শকদ্বয়ের ছেদবিন্দুর সঞ্চারপথ হলো নিয়ামক বৃত্ত।",
            "hack": "পরাবৃত্তের ক্ষেত্রে নিয়ামক বৃত্ত হলো তার নিয়ামক রেখা নিজেই (x + a = 0)!",
            "trap": "অধিবৃত্তে a < b হলে নিয়ামক বৃত্ত কাল্পনিক হয়।",
            "tags": ["director circle", "locus", "নিয়ামক বৃত্ত", "লম্ব স্পর্শক"]
        },
        {
            "id": "v_mat_con_09",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "core_formula",
            "title": "কণিকের স্পর্শকের শর্ত এক নজরে",
            "formula": "\\text{পরাবৃত্ত: } c = \\frac{a}{m}; \\quad \\text{উপবৃত্ত: } c = \\pm\\sqrt{a^2 m^2 + b^2}; \\quad \\text{অধিবৃত্ত: } c = \\pm\\sqrt{a^2 m^2 - b^2}",
            "concept": "y = mx + c সরলরেখাটি বিভিন্ন কণিকের স্পর্শক হওয়ার শর্ত।",
            "hack": "স্পর্শবিন্দু পরাবৃত্তে (a/m^2, 2a/m); উপবৃত্তে (-a^2 m/c, b^2/c)!",
            "trap": "অধিবৃত্তের ক্ষেত্রে রুটের ভেতর মাইনাস চিহ্ন থাকবে (a^2 m^2 - b^2)।",
            "tags": ["conic tangents", "condition", "স্পর্শকের শর্ত"]
        },
        {
            "id": "v_mat_con_10",
            "subject": "Higher Math",
            "chapter": "Conics",
            "type": "shortcut",
            "title": "উপকেন্দ্র-নিয়ামক দূরত্ব (d) থেকে লম্ব (L)",
            "formula": "L = 2 \\cdot e \\cdot d",
            "concept": "যেকোনো কণিকের উপকেন্দ্র ও অনুরূপ নিয়ামক রেখার লম্ব দূরত্ব d জানা থাকলে লম্বের দৈর্ঘ্য সরাসরি পাওয়া যায়।",
            "hack": "উপবৃত্তে d = 6 এবং e = 1/2 হলে L = 2 * (1/2) * 6 = 6 একক! পরাবৃত্তে e = 1 হলে L = 2d = 4a!",
            "trap": "d হলো উপকেন্দ্র থেকে নিয়ামকের দূরত্ব, শীর্ষ থেকে নয় (শীর্ষ থেকে নিয়ামকের দূরত্ব a)।",
            "tags": ["latus rectum shortcut", "focus-directrix", "উপকেন্দ্রিক লম্ব"]
        }
    ])

    # 5. Complex Numbers
    entries.extend([
        {
            "id": "v_mat_cn_01",
            "subject": "Higher Math",
            "chapter": "Complex Numbers",
            "type": "core_formula",
            "title": "জটিল সংখ্যার মডুলাস ও মুখ্য আর্গুমেন্ট",
            "formula": "z = x + iy \\implies |z| = \\sqrt{x^2 + y^2}, \\quad \\text{মুখ্য আর্গুমেন্ট } \\theta \\in (-\\pi, \\pi]",
            "concept": "১ম চতুর্ভাগে \\theta = \\alpha; ২য় চতুর্ভাগে \\theta = \\pi - \\alpha; ৩য় চতুর্ভাগে \\theta = -\\pi + \\alpha; ৪র্থ চতুর্ভাগে \\theta = -\\alpha (\\alpha = \\tan^{-1}|y/x|)।",
            "hack": "-1 - \\sqrt{3}i (৩য় চতুর্ভাগ): \\alpha = 60^\\circ = \\pi/3 \\implies \\theta = -\\pi + \\pi/3 = -2\\pi/3!",
            "trap": "৩য় চতুর্ভাগে \\pi + \\alpha দাগালে নেগেটিভ মার্কিং হবে, কারণ মুখ্য আর্গুমেন্টের সীমা (-pi, pi] পর্যন্ত।",
            "tags": ["modulus", "argument", "মডুলাস", "মুখ্য আর্গুমেন্ট", "চতুর্ভাগ", "trap"]
        },
        {
            "id": "v_mat_cn_02",
            "subject": "Higher Math",
            "chapter": "Complex Numbers",
            "type": "shortcut",
            "title": "জটিল সংখ্যার দ্রুত বর্গমূল",
            "formula": "\\sqrt{a \\pm ib} = \\pm(p \\pm iq) \\quad \\text{যেখানে } pq = \\frac{b}{2}, \\; p^2 - q^2 = a",
            "concept": "কাল্পনিক সহগকে ২ দিয়ে ভাগ করে এমন দুটি উৎপাদকে ভাঙতে হয় যাদের বর্গের বিয়োগফল বাস্তব অংশ a এর সমান।",
            "hack": "\\sqrt{-8 - 6i}: b/2 = 3 = 1 * 3, 1^2 - 3^2 = -8 \\implies \\pm(1 - 3i)! পাঁচ সেকেন্ডে সমাধান!",
            "trap": "কাল্পনিক অংশের আগে মাইনাস থাকলে উত্তরের মাঝেও মাইনাস বসবে।",
            "tags": ["square root", "complex number", "বর্গমূল", "শর্টকাট"]
        },
        {
            "id": "v_mat_cn_03",
            "subject": "Higher Math",
            "chapter": "Complex Numbers",
            "type": "core_formula",
            "title": "এককের কাল্পনিক ঘনমূল (\\omega)",
            "formula": "1 + \\omega + \\omega^2 = 0, \\quad \\omega^3 = 1, \\quad \\omega = \\frac{-1 + \\sqrt{3}i}{2}, \\quad \\omega^2 = \\frac{-1 - \\sqrt{3}i}{2}",
            "concept": "এককের তিনটি ঘনমূল হলো ১, \\omega, \\omega^2। এদের গুণফল ১ এবং যোগফল শূন্য।",
            "hack": "\\omega^{3k} = 1, \\omega^{3k+1} = \\omega, \\omega^{3k+2} = \\omega^2! সূচককে ৩ দিয়ে ভাগ করে ভাগশেষ নিন।",
            "trap": "যেকোনো ৩টি ক্রমিক ঘাতের যোগফল শূন্য: \\omega^n + \\omega^{n+1} + \\omega^{n+2} = 0।",
            "tags": ["cube roots of unity", "omega", "ঘনমূল", "ওমেগা"]
        },
        {
            "id": "v_mat_cn_04",
            "subject": "Higher Math",
            "chapter": "Complex Numbers",
            "type": "shortcut",
            "title": "ওমেগা সম্বলিত ধারা হ্যাক",
            "formula": "(1 - \\omega + \\omega^2)^n + (1 + \\omega - \\omega^2)^n = -(-2)^n \\quad (3 \\nmid n)",
            "concept": "1 + \\omega^2 = -\\omega এবং 1 + \\omega = -\\omega^2 প্রতিস্থাপন করে সরলীকরণ।",
            "hack": "n = 5 হলে: -(-2)^5 = 32! n = 4 হলে: -(-2)^4 = -16!",
            "trap": "চিহ্ন সতর্কভাবে রক্ষা করুন; ব্র্যাকেটের ভেতরের মাইনাস চিহ্নের ঘাত জোড় না বিজোড় তা দেখুন।",
            "tags": ["omega series", "hack", "ধারা", "ওমেগা"]
        },
        {
            "id": "v_mat_cn_05",
            "subject": "Higher Math",
            "chapter": "Complex Numbers",
            "type": "core_formula",
            "title": "ডি ময়ভারের উপপাদ্য (De Moivre's Theorem)",
            "formula": "(\\cos\\theta + i\\sin\\theta)^n = \\cos(n\\theta) + i\\sin(n\\theta) = e^{in\\theta}",
            "concept": "অয়লারের সূত্র: e^{i\\theta} = \\cos\\theta + i\\sin\\theta। জটিল সংখ্যার গুণনে আর্গুমেন্ট যোগ হয় এবং ভাগে বিয়োগ হয়।",
            "hack": "|z_1 z_2| = |z_1| |z_2|, \\quad \\arg(z_1 z_2) = \\arg(z_1) + \\arg(z_2)!",
            "trap": "ডি ময়ভার সূত্রে মাঝখানে প্লাস চিহ্ন এবং কোণ \\theta একই হতে হবে। \\sin\\theta + i\\cos\\theta থাকলে রূপান্তর করে নিতে হবে।",
            "tags": ["De Moivre", "Euler formula", "ডি ময়ভার", "অয়লার"]
        },
        {
            "id": "v_mat_cn_06",
            "subject": "Higher Math",
            "chapter": "Complex Numbers",
            "type": "shortcut",
            "title": "জটিল সংখ্যার সঞ্চারপথ (Locus)",
            "formula": "|z - z_0| = r \\; (\\text{বৃত্ত}), \\quad |z - z_1| = |z - z_2| \\; (\\text{লম্বদ্বিখণ্ডক সরলরেখা})",
            "concept": "|z - (a+ib)| = r সমীকরণটি (a, b) কেন্দ্র এবং r ব্যাসার্ধের বৃত্ত নির্দেশ করে।",
            "hack": "|z - 3| = |z + 3| হলে সঞ্চারপথ y-অক্ষ (x = 0)! |z - 2| + |z + 2| = 6 হলে উপবৃত্ত!",
            "trap": "|z - z1| + |z - z2| = k সমীকরণে k > |z1 - z2| হলে উপবৃত্ত, কিন্তু k = |z1 - z2| হলে সরলরেখাংশ! k < |z1-z2| হলে অসম্ভব।",
            "tags": ["locus", "circle", "perpendicular bisector", "সঞ্চারপথ"]
        },
        {
            "id": "v_mat_cn_07",
            "subject": "Higher Math",
            "chapter": "Complex Numbers",
            "type": "core_formula",
            "title": "অনুবন্ধী জটিল সংখ্যা ও ধর্ম",
            "formula": "z = x + iy \\implies \\bar{z} = x - iy, \\quad z\\bar{z} = |z|^2 = x^2 + y^2, \\quad z + \\bar{z} = 2x, \\quad z - \\bar{z} = 2iy",
            "concept": "কোনো জটিল সংখ্যা ও তার অনুবন্ধীর গুণফল সর্বদা অ-ঋণাত্মক বাস্তব সংখ্যা।",
            "hack": "1/i = -i, i^2 = -1, i^3 = -i, i^4 = 1! i এর পরপর ৪টি ক্রমিক ঘাতের যোগফল শূন্য (i + i^2 + i^3 + i^4 = 0)।",
            "trap": "হর থেকে i দূর করতে লব ও হরকে হরের অনুবন্ধী দিয়ে গুণ করতে হয়।",
            "tags": ["conjugate", "properties", "অনুবন্ধী", "i এর ঘাত"]
        },
        {
            "id": "v_mat_cn_08",
            "subject": "Higher Math",
            "chapter": "Complex Numbers",
            "type": "shortcut",
            "title": "(1+i)/(1-i) এর সরাসরি মান",
            "formula": "\\frac{1 + i}{1 - i} = i, \\quad \\frac{1 - i}{1 + i} = -i, \\quad (1 + i)^2 = 2i, \\quad (1 - i)^2 = -2i",
            "concept": "লব ও হরকে (1+i) দিয়ে গুণ করলে (1+2i-1)/2 = 2i/2 = i পাওয়া যায়।",
            "hack": "((1+i)/(1-i))^n = 1 হলে n এর ক্ষুদ্রতম ধনাত্মক পূর্ণমান ৪ (যেহেতু i^4 = 1)!",
            "trap": "(1+i)^4 = (2i)^2 = -4; (1+i)^8 = 16 (বাস্তব সংখ্যা)।",
            "tags": ["simplification", "shortcut", "সরল মান"]
        }
    ])

    # 6. Polynomials
    entries.extend([
        {
            "id": "v_mat_poly_01",
            "subject": "Higher Math",
            "chapter": "Polynomials",
            "type": "core_formula",
            "title": "দ্বিঘাত সমীকরণের মূল ও নিশ্চয়ক (Discriminant)",
            "formula": "ax^2 + bx + c = 0 \\implies x = \\frac{-b \\pm \\sqrt{D}}{2a}, \\quad D = b^2 - 4ac",
            "concept": "D > 0 হলে মূলদ্বয় বাস্তব ও অসমান; D = 0 হলে বাস্তব ও সমান; D < 0 হলে জটিল ও অনুবন্ধী; D পূর্ণবর্গ হলে মূলদ্বয় মূলদ।",
            "hack": "মূলদ্বয় সমান হওয়ার শর্ত: D = b^2 - 4ac = 0! k এর মান নির্ণয়ে এটি ভর্তি পরীক্ষায় সবচেয়ে বেশি আসে।",
            "trap": "মূলদ হওয়ার জন্য সহগগুলো (a, b, c) অবশ্যই মূলদ হতে হবে, শুধু D পূর্ণবর্গ হওয়াই যথেষ্ট নয়।",
            "tags": ["quadratic", "discriminant", "নিশ্চয়ক", "মূলের প্রকৃতি"]
        },
        {
            "id": "v_mat_poly_02",
            "subject": "Higher Math",
            "chapter": "Polynomials",
            "type": "core_formula",
            "title": "মূল ও সহগের সম্পর্ক (ভিয়েতার সূত্র)",
            "formula": "\\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha\\beta = \\frac{c}{a}, \\quad x^2 - (\\alpha + \\beta)x + \\alpha\\beta = 0",
            "concept": "ত্রিঘাত সমীকরণে: \\sum\\alpha = -b/a, \\sum\\alpha\\beta = c/a, \\alpha\\beta\\gamma = -d/a।",
            "hack": "মূলদ্বয়ের বর্গের সমষ্টি: \\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha\\beta = \\frac{b^2 - 2ac}{a^2}!",
            "trap": "মূলদ্বয়ের অন্তর |\\alpha - \\beta| = \\frac{\\sqrt{D}}{|a|} = \\frac{\\sqrt{b^2 - 4ac}}{|a|}।",
            "tags": ["Vieta's formula", "roots coefficients", "মূল ও সহগ", "ভিয়েতা"]
        },
        {
            "id": "v_mat_poly_03",
            "subject": "Higher Math",
            "chapter": "Polynomials",
            "type": "shortcut",
            "title": "মূল উল্টে যাওয়া ও চিহ্ন পরিবর্তনের সমীকরণ",
            "formula": "\\text{মূলদ্বয় } 1/\\alpha, 1/\\beta \\implies cx^2 + bx + a = 0; \\quad \\text{মূলদ্বয় } -\\alpha, -\\beta \\implies ax^2 - bx + c = 0",
            "concept": "মূলের বিপরীত রূপান্তরের শর্টকাট।",
            "hack": "মূলদ্বয় বিপরীত হলে শুধু ১ম ও শেষ সহগ সোয়াপ (c ও a অদলবদল); বিপরীত চিহ্ন হলে মাঝের b এর চিহ্ন পরিবর্তন!",
            "trap": "মূলদ্বয় পরস্পর গুণাত্মক বিপরীত (\\alpha ও 1/\\alpha) হওয়ার শর্ত হলো c = a!",
            "tags": ["roots transformation", "reciprocal roots", "মূলের রূপান্তর", "বিপরীত মূল"]
        },
        {
            "id": "v_mat_poly_04",
            "subject": "Higher Math",
            "chapter": "Polynomials",
            "type": "shortcut",
            "title": "একটি মূল অপরটির n গুণ হলে শর্ত",
            "formula": "n b^2 = (n + 1)^2 a c",
            "concept": "ax^2 + bx + c = 0 সমীকরণের একটি মূল অপরটির n গুণ (\\beta = n\\alpha) হওয়ার শর্ত।",
            "hack": "একটি মূল অপরটির দ্বিগুণ (n = 2) হলে: 2 b^2 = (2+1)^2 ac = 9ac! তিন গুণ হলে: 3 b^2 = 16ac!",
            "trap": "একটি মূল অপরটির বর্গের সমান (\\beta = \\alpha^2) হলে a c^2 + a^2 c + b^3 = 3abc।",
            "tags": ["roots ratio", "shortcut", "মূলের অনুপাত"]
        },
        {
            "id": "v_mat_poly_05",
            "subject": "Higher Math",
            "chapter": "Polynomials",
            "type": "core_formula",
            "title": "সাধারণ মূল থাকার শর্ত (Common Root)",
            "formula": "(c_1 a_2 - c_2 a_1)^2 = (a_1 b_2 - a_2 b_1)(b_1 c_2 - b_2 c_1)",
            "concept": "দুটি দ্বিঘাত সমীকরণের একটি সাধারণ মূল থাকলে বজ্রগুণন পদ্ধতির মাধ্যমে শর্ত পাওয়া যায়।",
            "hack": "উভয় মূলই সাধারণ হওয়ার শর্ত: a1/a2 = b1/b2 = c1/c2 (সহগগুলো সমানুপাতিক)!",
            "trap": "বিয়োগ করে x এর মান বের করে যেকোনো সমীকরণে বসালে অজানা ধ্রুবকের মান খুব সহজে পাওয়া যায়।",
            "tags": ["common root", "সাধারণ মূল", "শর্ত"]
        },
        {
            "id": "v_mat_poly_06",
            "subject": "Higher Math",
            "chapter": "Polynomials",
            "type": "shortcut",
            "title": "অনুবন্ধী মূল উপপাদ্য",
            "formula": "\\text{একটি মূল } p + \\sqrt{q} \\implies \\text{অপর মূল } p - \\sqrt{q}; \\quad \\text{একটি মূল } p + iq \\implies \\text{অপর মূল } p - iq",
            "concept": "বাস্তব সহগবিশিষ্ট বহুপদীতে অমূলদ মূল এবং জটিল মূল সর্বদা অনুবন্ধী জোড়ায় থাকে।",
            "hack": "একটি মূল 2 + 3i হলে সমীকরণটি সরাসরি: x^2 - 2(2)x + (2^2 + 3^2) = 0 \\implies x^2 - 4x + 13 = 0!",
            "trap": "অমূলদ মূলের ক্ষেত্রে সহগগুলো অবশ্যই মূলদ হতে হবে, অন্যথায় জোড়ায় না-ও থাকতে পারে।",
            "tags": ["conjugate roots", "complex root", "অনুবন্ধী মূল"]
        },
        {
            "id": "v_mat_poly_07",
            "subject": "Higher Math",
            "chapter": "Polynomials",
            "type": "core_formula",
            "title": "ভাগশেষ উপপাদ্য ও উৎপাদক উপপাদ্য",
            "formula": "P(x) \\div (x - a) \\implies \\text{ভাগশেষ } R = P(a); \\quad P(a) = 0 \\iff (x - a) \\text{ একটি উৎপাদক}",
            "concept": "বহুপদীকে একঘাত রাশি (ax + b) দিয়ে ভাগ করলে ভাগশেষ হয় P(-b/a)।",
            "hack": "ভাগ না করেই সরাসরি x = a বসিয়ে ভাগশেষ নির্ণয় করা যায়!",
            "trap": "ভাজক দ্বিঘাত হলে ভাগশেষ একঘাত (Ax + B) হতে পারে।",
            "tags": ["remainder theorem", "factor theorem", "ভাগশেষ উপপাদ্য"]
        },
        {
            "id": "v_mat_poly_08",
            "subject": "Higher Math",
            "chapter": "Polynomials",
            "type": "shortcut",
            "title": "দ্বিঘাত রাশির সর্বোচ্চ ও সর্বনিম্ন মান",
            "formula": "y = ax^2 + bx + c \\implies x = -\\frac{b}{2a} \\text{ বিন্দুতে } y_{ext} = c - \\frac{b^2}{4a} = \\frac{4ac - b^2}{4a}",
            "concept": "a > 0 হলে পরাবৃত্ত ঊর্ধ্বমুখী এবং সর্বনিম্ন মান থাকে; a < 0 হলে পরাবৃত্ত নিম্নমুখী এবং সর্বোচ্চ মান থাকে।",
            "hack": "ক্যালকুলাসে dy/dx = 2ax + b = 0 ধরলে সরাসরি x = -b/(2a) পাওয়া যায়!",
            "trap": "a এর চিহ্নের ওপর নির্ভর করে মানটি সর্বোচ্চ নাকি সর্বনিম্ন হবে (a ধনাত্মক হলে সর্বনিম্ন মান)।",
            "tags": ["extrema", "quadratic", "সর্বোচ্চ মান", "সর্বনিম্ন মান"]
        }
    ])

    # 7. Trigonometry
    entries.extend([
        {
            "id": "v_mat_tri_01",
            "subject": "Higher Math",
            "chapter": "Trigonometry",
            "type": "core_formula",
            "title": "যৌগিক কোণের মৌলিক সূত্রাবলী",
            "formula": "\\sin(A \\pm B) = \\sin A\\cos B \\pm \\cos A\\sin B, \\quad \\cos(A \\pm B) = \\cos A\\cos B \\mp \\sin A\\sin B",
            "concept": "ত্রিকোণমিতির সকল সূত্রের মূল ভিত্তি। কসের সূত্রে চিহ্নের পরিবর্তন (প্লাসে মাইনাস, মাইনাসে প্লাস) ঘটে।",
            "hack": "\\tan(A + B) = \\frac{\\tan A + \\tan B}{1 - \\tan A\\tan B}! A + B = 45^\\circ \\implies (1 + \\tan A)(1 + \\tan B) = 2!",
            "trap": "\\cos(A + B) এ মাঝখানে মাইনাস চিহ্ন হয়; ভুল করে প্লাস বসানো যাবে না।",
            "tags": ["compound angles", "addition formula", "যৌগিক কোণ", "ত্রিকোণমিতি"]
        },
        {
            "id": "v_mat_tri_02",
            "subject": "Higher Math",
            "chapter": "Trigonometry",
            "type": "shortcut",
            "title": "ম্যাজিক অভেদ: \\sec\\theta + \\tan\\theta = k",
            "formula": "\\sec\\theta + \\tan\\theta = k \\implies \\sec\\theta - \\tan\\theta = \\frac{1}{k}, \\quad \\sin\\theta = \\frac{k^2 - 1}{k^2 + 1}",
            "concept": "\\sec^2\\theta - \\tan^2\\theta = 1 = (\\sec\\theta + \\tan\\theta)(\\sec\\theta - \\tan\\theta)।",
            "hack": "যদি \\sec\\theta + \\tan\\theta = 5 হয়, তবে \\sec\\theta - \\tan\\theta = 1/5 = 0.2 এবং \\sin\\theta = (25-1)/(25+1) = 24/26 = 12/13!",
            "trap": "একই নিয়ম \\csc\\theta + \\cot\\theta = m এর জন্যও প্রযোজ্য, সেক্ষেত্রে \\cos\\theta = (m^2 - 1)/(m^2 + 1)।",
            "tags": ["trig identity", "sec tan shortcut", "ম্যাজিক অভেদ"]
        },
        {
            "id": "v_mat_tri_03",
            "subject": "Higher Math",
            "chapter": "Trigonometry",
            "type": "core_formula",
            "title": "গুণিতক কোণ (2A ও 3A) সূত্র",
            "formula": "\\sin 2A = 2\\sin A\\cos A = \\frac{2\\tan A}{1 + \\tan^2 A}, \\quad \\cos 2A = \\cos^2 A - \\sin^2 A = \\frac{1 - \\tan^2 A}{1 + \\tan^2 A}",
            "concept": "1 + \\cos 2A = 2\\cos^2 A এবং 1 - \\cos 2A = 2\\sin^2 A (ক্যালকুলাসের ইন্টিগ্রেশনে বহুল ব্যবহৃত)।",
            "hack": "\\sin 3A = 3\\sin A - 4\\sin^3 A; \\quad \\cos 3A = 4\\cos^3 A - 3\\cos A (মনে রাখুন: সাইনে ৩৪, কসে ৪৩)!",
            "trap": "\\tan 2A = \\frac{2\\tan A}{1 - \\tan^2 A} (হরে মাইনাস থাকে, সাইনে প্লাস থাকে)।",
            "tags": ["double angle", "multiple angle", "গুণিতক কোণ"]
        },
        {
            "id": "v_mat_tri_04",
            "subject": "Higher Math",
            "chapter": "Trigonometry",
            "type": "shortcut",
            "title": "a\\cos\\theta + b\\sin\\theta + c এর চরম মান",
            "formula": "\\text{সর্বোচ্চ মান } = c + \\sqrt{a^2 + b^2}, \\quad \\text{সর্বনিম্ন মান } = c - \\sqrt{a^2 + b^2}",
            "concept": "রাশিটিকে R\\cos(\\theta - \\alpha) আকারে প্রকাশ করলে এর বিস্তার \\pm\\sqrt{a^2 + b^2} এর মধ্যে থাকে।",
            "hack": "3\\cos\\theta + 4\\sin\\theta + 7 এর সর্বোচ্চ মান = 7 + \\sqrt{9+16} = 7 + 5 = 12; সর্বনিম্ন মান = 7 - 5 = 2!",
            "trap": "ধ্রুবক c না থাকলে সরাসরি \\pm\\sqrt{a^2 + b^2}।",
            "tags": ["max min", "trig extrema", "চরম মান", "সর্বোচ্চ"]
        },
        {
            "id": "v_mat_tri_05",
            "subject": "Higher Math",
            "chapter": "Trigonometry",
            "type": "core_formula",
            "title": "বিপরীত বৃত্তীয় ফাংশন (Inverse Trig) যোগফল",
            "formula": "\\tan^{-1}x + \\tan^{-1}y = \\tan^{-1}\\left(\\frac{x + y}{1 - xy}\\right) \\quad (xy < 1)",
            "concept": "যদি xy > 1 হয় তবে সামনে \\pi যোগ হয়: \\pi + \\tan^{-1}\\left(\\frac{x+y}{1-xy}\\right)।",
            "hack": "2\\tan^{-1}x = \\tan^{-1}\\left(\\frac{2x}{1-x^2}\\right) = \\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right) = \\cos^{-1}\\left(\\frac{1-x^2}{1+x^2}\\right)!",
            "trap": "\\sin^{-1}x + \\cos^{-1}x = \\frac{\\pi}{2}; \\quad \\tan^{-1}x + \\cot^{-1}x = \\frac{\\pi}{2}; \\quad \\sec^{-1}x + \\csc^{-1}x = \\frac{\\pi}{2}।",
            "tags": ["inverse trig", "tan inverse", "বিপরীত ত্রিকোণমিতি"]
        },
        {
            "id": "v_mat_tri_06",
            "subject": "Higher Math",
            "chapter": "Trigonometry",
            "type": "shortcut",
            "title": "ত্রিকোণমিতিক সাধারণ সমাধান",
            "formula": "\\sin\\theta = 0 \\implies \\theta = n\\pi, \\quad \\cos\\theta = 0 \\implies \\theta = (2n+1)\\frac{\\pi}{2}, \\quad \\tan\\theta = 0 \\implies \\theta = n\\pi",
            "concept": "সাধারণ সমাধান যেখানে n যেকোনো পূর্ণসংখ্যা (n \\in \\mathbb{Z})।",
            "hack": "\\sin\\theta = \\sin\\alpha \\implies \\theta = n\\pi + (-1)^n \\alpha; \\quad \\cos\\theta = \\cos\\alpha \\implies \\theta = 2n\\pi \\pm \\alpha!",
            "trap": "\\tan\\theta = \\tan\\alpha এর সমাধানে \\theta = n\\pi + \\alpha (কোনো \\pm বা (-1)^n নেই)।",
            "tags": ["general solution", "trig equations", "সাধারণ সমাধান"]
        },
        {
            "id": "v_mat_tri_07",
            "subject": "Higher Math",
            "chapter": "Trigonometry",
            "type": "core_formula",
            "title": "ত্রিভুজের সাইন সূত্র ও কোসাইন সূত্র",
            "formula": "\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R, \\quad \\cos A = \\frac{b^2 + c^2 - a^2}{2bc}",
            "concept": "R হলো ত্রিভুজের পরিব্যাসার্ধ। ত্রিভুজের ক্ষেত্রফল \\Delta = \\frac{abc}{4R} = rs (r = অন্তর্ব্যাসার্ধ)।",
            "hack": "যদি a^2 = b^2 + c^2 হয় তবে \\cos A = 0 \\implies A = 90^\\circ (পিথাগোরাস)! a^2 = b^2 + c^2 - bc হলে A = 60^\\circ!",
            "trap": "কোসাইন সূত্রে যে কোণ বের করবেন তার বিপরীত বাহু লবে বিয়োগ হয় (-a^2)।",
            "tags": ["sine rule", "cosine rule", "সাইন সূত্র", "কোসাইন সূত্র"]
        },
        {
            "id": "v_mat_tri_08",
            "subject": "Higher Math",
            "chapter": "Trigonometry",
            "type": "shortcut",
            "title": "\\sin\\theta \\sin(60-\\theta) \\sin(60+\\theta) হ্যাক",
            "formula": "\\sin\\theta \\sin(60^\\circ - \\theta) \\sin(60^\\circ + \\theta) = \\frac{1}{4}\\sin 3\\theta",
            "concept": "কসের ক্ষেত্রে: \\cos\\theta \\cos(60^\\circ - \\theta) \\cos(60^\\circ + \\theta) = \\frac{1}{4}\\cos 3\\theta।",
            "hack": "\\sin 20^\\circ \\sin 40^\\circ \\sin 80^\\circ = \\frac{1}{4}\\sin(3 \\times 20^\\circ) = \\frac{1}{4}\\sin 60^\\circ = \\frac{\\sqrt{3}}{8}!",
            "trap": "\\tan এর ক্ষেত্রে 1/4 থাকে না: \\tan\\theta \\tan(60-\\theta) \\tan(60+\\theta) = \\tan 3\\theta।",
            "tags": ["trig product hack", "special angles", "গুণফল হ্যাক"]
        }
    ])

    # 8. Calculus (অন্তরীকরণ ও যৌগিকীকরণ)
    entries.extend([
        {
            "id": "v_mat_calc_01",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "core_formula",
            "title": "ক্যালকুলাসের মৌলিক অন্তরক সূত্র",
            "formula": "\\frac{d}{dx}(x^n) = nx^{n-1}, \\quad \\frac{d}{dx}(e^{ax}) = ae^{ax}, \\quad \\frac{d}{dx}(\\ln x) = \\frac{1}{x}, \\quad \\frac{d}{dx}(a^x) = a^x \\ln a",
            "concept": "অন্তরীকরণ হলো পরিবর্তনের তাৎক্ষণিক হার ও স্পর্শকের ঢাল।",
            "hack": "\\frac{d}{dx}(\\sqrt{x}) = \\frac{1}{2\\sqrt{x}}; \\quad \\frac{d}{dx}\\left(\\frac{1}{x}\\right) = -\\frac{1}{x^2} সরাসরি মেমোরিতে রাখুন!",
            "trap": "a^x এর অন্তরকে ln a গুণ হয়, কিন্তু ইন্টিগ্রেশনে ln a দিয়ে ভাগ হয়।",
            "tags": ["derivative", "differentiation", "অন্তরীকরণ", "মৌলিক সূত্র"]
        },
        {
            "id": "v_mat_calc_02",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "shortcut",
            "title": "লা হসপিটাল নিয়ম (L'Hopital's Rule)",
            "formula": "\\lim_{x \\to a} \\frac{f(x)}{g(x)} = \\lim_{x \\to a} \\frac{f'(x)}{g'(x)} \\quad (\\text{যখন } \\frac{0}{0} \\text{ বা } \\frac{\\infty}{\\infty} \\text{ আকার})",
            "concept": "অনির্ণেয় আকার আসলে লব ও হরকে আলাদা আলাদাভাবে x এর সাপেক্ষে অন্তরীকরণ করতে হয়।",
            "hack": "যতক্ষণ পর্যন্ত 0/0 আকার থাকবে ততক্ষণ অন্তরীকরণ চালিয়ে যাওয়া যায়।",
            "trap": "u/v সূত্রের ভাগ নিয়ম প্রয়োগ করবেন না; লবকে আলাদা এবং হরকে আলাদা অন্তরীকরণ করতে হবে।",
            "tags": ["L'Hopital", "limits", "লা হসপিটাল", "লিমিট"]
        },
        {
            "id": "v_mat_calc_03",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "shortcut",
            "title": "অয়লারের লিমিট শর্টকাট (1 + kx)^(1/x)",
            "formula": "\\lim_{x \\to 0} (1 + ax)^{b/x} = e^{ab}, \\quad \\lim_{x \\to \\infty} \\left(1 + \\frac{a}{x}\\right)^{bx} = e^{ab}",
            "concept": "1^\\infty অনির্ণেয় আকারের স্ট্যান্ডার্ড লিমিট সূত্র।",
            "hack": "\\lim_{x \\to 0} (1 + 4x)^{3/x} = e^{4 \\times 3} = e^{12}! \\lim_{x \\to 0} (1 - 2x)^{1/x} = e^{-2}!",
            "trap": "চিহ্ন মাইনাস থাকলে ঘাতে ঋণাত্মক মান বসবে।",
            "tags": ["Euler limit", "exponential limit", "অয়লার লিমিট"]
        },
        {
            "id": "v_mat_calc_04",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "core_formula",
            "title": "ফাংশনের সর্বোচ্চ ও সর্বনিম্ন মান (গুরুমান ও লঘুমান)",
            "formula": "f'(x) = 0 \\implies x = c; \\quad f''(c) < 0 \\implies \\text{গুরুমান}, \\quad f''(c) > 0 \\implies \\text{লঘুমান}",
            "concept": "১ম ডেরিভেটিভ শূন্য হলে চরম বিন্দু পাওয়া যায়। ২য় ডেরিভেটিভ ঋণাত্মক হলে সর্বোচ্চ এবং ধনাত্মক হলে সর্বনিম্ন মান পাওয়া যায়।",
            "hack": "x + 1/x এর সর্বনিম্ন মান 2 (যখন x = 1); x^x এর সর্বনিম্ন মান ঘটে x = 1/e বিন্দুতে!",
            "trap": "চরম মান বের করতে x = c এর মান মূল ফাংশন f(x) এ বসাতে হবে, f'(x) বা f''(x) এ নয়।",
            "tags": ["maxima minima", "critical point", "গুরুমান", "লঘুমান"]
        },
        {
            "id": "v_mat_calc_05",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "shortcut",
            "title": "অব্যক্ত ফাংশনের দ্রুত অন্তরীকরণ (Partial Derivative Hack)",
            "formula": "\\frac{dy}{dx} = -\\frac{\\frac{\\partial f}{\\partial x}}{\\frac{\\partial f}{\\partial y}} = -\\frac{f_x (y \\text{ ধ্রুবক})}{f_y (x \\text{ ধ্রুবক})}",
            "concept": "f(x, y) = 0 অব্যক্ত সমীকরণে আংশিক অন্তরীকরণের ম্যাজিক শর্টকাট।",
            "hack": "x^3 + y^3 - 3axy = 0 \\implies \\frac{dy}{dx} = -\\frac{3x^2 - 3ay}{3y^2 - 3ax} = -\\frac{x^2 - ay}{y^2 - ax}! ১০ সেকেন্ডে উত্তর!",
            "trap": "সামনের মাইনাস চিহ্নটি ভুলে যাওয়া যাবে না।",
            "tags": ["implicit differentiation", "partial derivative", "অব্যক্ত ফাংশন"]
        },
        {
            "id": "v_mat_calc_06",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "core_formula",
            "title": "ইন্টিগ্রেশন শর্টকাট: f'(x) / f(x)",
            "formula": "\\int \\frac{f'(x)}{f(x)} dx = \\ln|f(x)| + c, \\quad \\int \\frac{f'(x)}{\\sqrt{f(x)}} dx = 2\\sqrt{f(x)} + c",
            "concept": "হরের অন্তরক লবে অবিকল বিদ্যমান থাকলে ইন্টিগ্রেশন সরাসরি হরের লগারিদম হয়।",
            "hack": "\\int \\tan x dx = \\int \\frac{\\sin x}{\\cos x} dx = -\\ln|\\cos x| + c = \\ln|\\sec x| + c!",
            "trap": "ধ্রুবকের ঘাটতি থাকলে বাইরে উপযুক্ত ধ্রুবক দিয়ে গুণ ও ভাগ করে সমন্বয় করতে হবে।",
            "tags": ["integration", "f'/f", "যৌগিকীকরণ", "লগারিদম"]
        },
        {
            "id": "v_mat_calc_07",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "shortcut",
            "title": "ইন্টিগ্রেশন শর্টকাট: e^x (f(x) + f'(x))",
            "formula": "\\int e^x [f(x) + f'(x)] dx = e^x f(x) + c",
            "concept": "e^x এর সাথে একটি ফাংশন ও তার অন্তরকের যোগফল গুণ আকারে থাকলে উত্তর হয় e^x * মূল ফাংশন।",
            "hack": "\\int e^x (\\tan x + \\sec^2 x) dx = e^x \\tan x + c; \\quad \\int e^x \\left(\\frac{1}{x} - \\frac{1}{x^2}\\right) dx = \\frac{e^x}{x} + c!",
            "trap": "কোনটি f(x) আর কোনটি f'(x) তা সঠিকভাবে শনাক্ত করুন; উত্তর সর্বদা মূল f(x) ধারণ করে।",
            "tags": ["e^x integration", "shortcut", "ইন্টিগ্রেশন হ্যাক"]
        },
        {
            "id": "v_mat_calc_08",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "core_formula",
            "title": "নির্দিষ্ট যোগজের ক্ষেত্রফল (Area under Curve)",
            "formula": "\\text{Area} = \\int_a^b y dx = \\int_a^b [y_1(x) - y_2(x)] dx",
            "concept": "বক্ররেখা ও x-অক্ষ দ্বারা আবদ্ধ অঞ্চলের ক্ষেত্রফল নির্দিষ্ট যোগজের মাধ্যমে নির্ণীত হয়।",
            "hack": "y^2 = 4ax এবং x^2 = 4by দ্বারা আবদ্ধ ক্ষেত্রফল = \\frac{16ab}{3}! y^2 = 4ax ও y = mx দ্বারা আবদ্ধ ক্ষেত্রফল = \\frac{8a^2}{3m^3}!",
            "trap": "উপবৃত্তের মোট ক্ষেত্রফল \\pi ab; চতুর্থাংশের ক্ষেত্রফল \\frac{1}{4}\\pi ab।",
            "tags": ["area", "definite integral", "ক্ষেত্রফল", "আবদ্ধ অঞ্চল"]
        },
        {
            "id": "v_mat_calc_09",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "shortcut",
            "title": "ওয়ালিসের সূত্র (Wallis' Formula) নির্দিষ্ট ইন্টিগ্রেশন",
            "formula": "\\int_0^{\\pi/2} \\sin^n x dx = \\int_0^{\\pi/2} \\cos^n x dx = \\frac{n-1}{n} \\cdot \\frac{n-3}{n-2} \\dots \\left(\\times \\frac{\\pi}{2} \\text{ যদি n জোড়}\\right)",
            "concept": "সীমা 0 থেকে pi/2 হলে সাইন বা কসের উচ্চ ঘাতের দ্রুত মান নির্ণয়।",
            "hack": "\\int_0^{\\pi/2} \\sin^4 x dx = \\frac{3}{4} \\times \\frac{1}{2} \\times \\frac{\\pi}{2} = \\frac{3\\pi}{16}! n বিজোড় হলে শেষে ১ দিয়ে শেষ হয় (pi/2 গুণ হয় না)।",
            "trap": "সীমা অবশ্যই 0 থেকে \\pi/2 হতে হবে; অন্য সীমার ক্ষেত্রে এই সূত্র সরাসরি খাটবে না।",
            "tags": ["Wallis formula", "definite integration", "ওয়ালিসের সূত্র"]
        },
        {
            "id": "v_mat_calc_10",
            "subject": "Higher Math",
            "chapter": "Calculus",
            "type": "core_formula",
            "title": "খণ্ডিত যোগজ (Integration by Parts - ILATE)",
            "formula": "\\int u v dx = u \\int v dx - \\int \\left(\\frac{du}{dx} \\int v dx\\right) dx",
            "concept": "u নির্বাচনের অগ্রাধিকার ক্রম: I (Inverse) > L (Log) > A (Algebraic) > T (Trig) > E (Exponential)।",
            "hack": "\\int \\ln x dx = x\\ln x - x + c! \\int x e^x dx = e^x (x - 1) + c!",
            "trap": "ILATE ক্রমানুসারে যেটি আগে আসবে তাকে u ধরতে হবে, অন্যথা ইন্টিগ্রেশন জটিল থেকে জটিলতর হবে।",
            "tags": ["by parts", "ILATE", "খণ্ডিত যোগজ", "ইউ ভি সূত্র"]
        }
    ])

    return entries


def get_bio_entries():
    entries = []

    # 1. Cell & Structure
    entries.extend([
        {
            "id": "v_bio_cs_01",
            "subject": "Biology",
            "chapter": "Cell & Structure",
            "type": "core_formula",
            "title": "কোষ ঝিল্লির ফ্লুইড মোজাইক মডেল (Singer & Nicolson, 1972)",
            "formula": "\\text{উপাদান: ফসফোলিপিড বাইলেয়ার + মেমব্রেন প্রোটিন + গ্লাইকোক্যালিক্স + কোলেস্টেরল}",
            "concept": "সর্বাধিক গ্রহণযোগ্য মডেল। ফসফোলিপিডের সমুদ্রের মাঝে প্রোটিনগুলো মোজাইকের মতো ভাসমান অবস্থায় থাকে।",
            "hack": "ফসফোলিপিড অণু অ্যাম্পিপ্যাথিক: মাথা পোলার (হাইড্রোফিলিক বা পানিস্নেহী) এবং লেজ নন-পোলার (হাইড্রোফোবিক বা পানিবিদ্বেষী)!",
            "trap": "কোলেস্টেরল কেবল প্রাণী কোষের ঝিল্লিতে থাকে, উদ্ভিদ কোষের ঝিল্লিতে থাকে না।",
            "tags": ["fluid mosaic", "cell membrane", "ফসফোলিপিড", "ফ্লুইড মোজাইক"]
        },
        {
            "id": "v_bio_cs_02",
            "subject": "Biology",
            "chapter": "Cell & Structure",
            "type": "shortcut",
            "title": "আবরণীবিহীন কোষ অঙ্গাণু মুখস্থ ছন্দ",
            "formula": "\\text{ছন্দ: 'মামাবাড়ি সেন্ট গিয়ে প্রোটিনের রাইস খেলাম'}",
            "concept": "মাইক্রোটিবিউলস, সেন্ট্রিওল, প্রোটিওজোম, রাইবোসোম হলো ঝিল্লিবিহীন অঙ্গাণু।",
            "hack": "রাইবোসোম (70S/80S) এবং সেন্ট্রিওল (9+0 অনুলম্ব গঠন) উভয়ই পর্দাবিহীন!",
            "trap": "মাইটোকন্ড্রিয়া ও প্লাস্টিড দ্বি-স্তর ঝিল্লিযুক্ত; লাইসোজোম ও গলগি বডি একক ঝিল্লিযুক্ত।",
            "tags": ["non-membranous", "organelles", "রাইবোসোম", "পর্দাবিহীন"]
        },
        {
            "id": "v_bio_cs_03",
            "subject": "Biology",
            "chapter": "Cell & Structure",
            "type": "core_formula",
            "title": "রাইবোসোম (70S বনাম 80S) এর সাবইউনিট",
            "formula": "70S = 50S + 30S \\; (\\text{প্রোক্যারিওটিক}), \\quad 80S = 60S + 40S \\; (\\text{ইউক্যারিওটিক})",
            "concept": "S হলো ভেদবার্গ একক (Svedberg unit), যা অধঃক্ষেপণ গুণাঙ্ক নির্দেশ করে (1S = 10^-13 সেকেন্ড)।",
            "hack": "মাইটোকন্ড্রিয়া ও ক্লোরোপ্লাস্টের নিজস্ব রাইবোসোম 70S ধরনের!",
            "trap": "সাবইউনিটগুলো সাধারণ বীজগণিতীয় যোগফল নয়; সেন্ট্রিফিউগেশনে অধঃক্ষেপণের হার বোঝায় (৫০+৩০=৭০, ৬০+৪০=৮০)।",
            "tags": ["ribosome", "Svedberg", "70S", "80S", "সাবইউনিট"]
        },
        {
            "id": "v_bio_cs_04",
            "subject": "Biology",
            "chapter": "Cell & Structure",
            "type": "trap",
            "title": "DNA বনাম RNA নিউক্লিওটাইড ক্ষারক ও বন্ধন",
            "formula": "A = T \\; (2\\text{ হাইড্রোজেন বন্ধন}), \\quad G \\equiv C \\; (3\\text{ হাইড্রোজেন বন্ধন})",
            "concept": "শারগাফের নিয়ম (Chargaff's rule): A + G = T + C (পিউরিন = পিরিমিডিন)। RNA তে থাইমিনের (T) পরিবর্তে ইউরাসিল (U) থাকে।",
            "hack": "একটি DNA তে সাইটোসিন (C) 20% হলে গুয়ানিন (G) 20%; বাকি 60% এর মধ্যে A = 30% এবং T = 30%!",
            "trap": "G-C বন্ধনে ৩টি হাইড্রোজেন বন্ড থাকায় এটি ভাঙতে A-T বন্ধনের চেয়ে বেশি শক্তি ও তাপমাত্রা (উচ্চ Tm) লাগে।",
            "tags": ["DNA", "hydrogen bonds", "Chargaff", "শারগাফের নিয়ম", "trap"]
        },
        {
            "id": "v_bio_cs_05",
            "subject": "Biology",
            "chapter": "Cell & Structure",
            "type": "core_formula",
            "title": "সেন্ট্রাল ডগমা (Central Dogma)",
            "formula": "\\text{DNA} \\xrightarrow{\\text{Replication}} \\text{DNA} \\xrightarrow{\\text{Transcription}} \\text{mRNA} \\xrightarrow{\\text{Translation}} \\text{Protein}",
            "concept": "জিনগত তথ্যের একমুখী প্রবাহ। রিভার্স ট্রান্সক্রিপশনে (রেট্রোভাইরাস যেমন HIV) RNA থেকে DNA তৈরি হয়।",
            "hack": "ট্রান্সক্রিপশনে প্রধান এনজাইম RNA পলিমারেজ; প্রোটিন তৈরিতে রাইবোসোম হলো সাইট এবং tRNA অ্যামিনো অ্যাসিড বহন করে!",
            "trap": "ট্রান্সলেশনে স্টার্ট কোডন AUG (মেথিওনিন) এবং স্টপ কোডন UAA, UAG, UGA।",
            "tags": ["central dogma", "transcription", "translation", "সেন্ট্রাল ডগমা"]
        },
        {
            "id": "v_bio_cs_06",
            "subject": "Biology",
            "chapter": "Cell & Structure",
            "type": "shortcut",
            "title": "লাইসোজোমের অটোফ্যাগি ও অটলাইসিস",
            "formula": "\\text{লাইসোজোম: 'আত্মঘাতী থলিকা' (Suicidal bag) - প্রায় ৫০ ধরনের হাইড্রোলাইটিক এনজাইম থাকে}",
            "concept": "তীব্র খাদ্য সংকটে নিজস্ব অঙ্গাণু ধ্বংস করাকে অটোফ্যাগি (Autophagy) এবং সম্পূর্ণ কোষ ধ্বংসকে অটোলাইসিস বলে।",
            "hack": "অম্লীয় pH (pH 4.5 - 5.0) এ লাইসোজোমের অ্যাসিড ফসফাটেজ সহ সকল এনজাইম সর্বোচ্চ সক্রিয় থাকে!",
            "trap": "লাইসোজোমের ঝিল্লি ক্ষতিগ্রস্ত হলে লাইটিক এনজাইম বের হয়ে সম্পূর্ণ কোষকে হজম করে ফেলে।",
            "tags": ["lysosome", "autophagy", "লাইসোজোম", "অটোফ্যাগি"]
        },
        {
            "id": "v_bio_cs_07",
            "subject": "Biology",
            "chapter": "Cell & Structure",
            "type": "core_formula",
            "title": "কোষচক্রের সময় বিভাজন (Cell Cycle)",
            "formula": "\\text{ইন্টারফেজ } (90 - 95\\%) + \\text{M-ফেজ } (5 - 10\\%)",
            "concept": "ইন্টারফেজ ৩ ভাগে বিভক্ত: G1 (৩০-৪০%), S দশা (৩০-৫০%, DNA প্রতিলিপন), G2 (১০-২০%, প্রোটিন ও এটিপি তৈরি)।",
            "hack": "DNA এবং হিস্টোন প্রোটিন উভয়ই সংশ্লেষিত হয় S দশায় (Synthesis phase)!",
            "trap": "কোষ বিভাজন প্রস্তুতিতে সবচেয়ে দীর্ঘতম দশা হলো ইন্টারফেজ (বিশেষ করে S ও G1)।",
            "tags": ["cell cycle", "interphase", "S phase", "কোষচক্র", "ইন্টারফেজ"]
        },
        {
            "id": "v_bio_cs_08",
            "subject": "Biology",
            "chapter": "Cell & Structure",
            "type": "shortcut",
            "title": "মিয়োসিস প্রোফেজ-১ উপধাপ ছক",
            "formula": "\\text{জাইগোটিন: সিন্যাপসিস; প্যাকাইটিন: ক্রসিং ওভার; ডিপ্লোটিন: প্রান্তীয়করণ}",
            "concept": "হোমোলোগাস ক্রোমোজোমের নন-সিস্টার ক্রোমাটিডের মধ্যে অংশের বিনিময়কে ক্রসিং ওভার বলে।",
            "hack": "প্যাকাইটিনে টেট্রাড গঠিত হয় এবং এন্ডোনিউক্লিয়েজ ও লাইগেজ এনজাইমের সাহায্যে ক্রসিং ওভার ঘটে!",
            "trap": "সিন্যাপসিসে বাইভ্যালেন্ট গঠিত হয় জাইগোটিনে, প্যাকাইটিনে নয়।",
            "tags": ["meiosis", "crossing over", "synapsis", "মিয়োসিস", "ক্রসিং ওভার"]
        }
    ])

    # 2. Genetics
    entries.extend([
        {
            "id": "v_bio_gen_01",
            "subject": "Biology",
            "chapter": "Genetics",
            "type": "core_formula",
            "title": "মেন্ডেলের সূত্রের আদর্শ ফিনোটাইপিক অনুপাত",
            "formula": "\\text{১ম সূত্র (মনোহাইব্রিড): } 3 : 1, \\quad \\text{২য় সূত্র (ডাইহাইব্রিড): } 9 : 3 : 3 : 1",
            "concept": "মেন্ডেলের ১ম সূত্র হলো পৃথকীকরণ সূত্র এবং ২য় সূত্র হলো স্বাধীন সঞ্চালন সূত্র। টেস্ট ক্রসের অনুপাত মনোহাইব্রিডে ১:১ এবং ডাইহাইব্রিডে ১:১:১:১।",
            "hack": "টেস্ট ক্রস (Test Cross) দ্বারা কোনো জীবের অজানা জিনোটাইপ হোমোজাইগাস নাকি হেটেরোজাইগাস তা নির্ধারণ করা হয়!",
            "trap": "ব্যাক ক্রসের সকল ক্রস টেস্ট ক্রস নয়; কিন্তু সকল টেস্ট ক্রসই ব্যাক ক্রস।",
            "tags": ["Mendel", "phenotype ratio", "টেস্ট ক্রস", "মেন্ডেলের সূত্র"]
        },
        {
            "id": "v_bio_gen_02",
            "subject": "Biology",
            "chapter": "Genetics",
            "type": "shortcut",
            "title": "মেন্ডেলের ১ম সূত্রের ব্যতিক্রমী অনুপাত",
            "formula": "\\text{অসম্পূর্ণ প্রকটতা: } 1:2:1; \\quad \\text{সমপ্রকটতা: } 1:2:1; \\quad \\text{লিথাল জিন: } 2:1",
            "concept": "অসম্পূর্ণ প্রকটতায় মধ্যবর্তী ফিনোটাইপ (গোলাপি ফুল) এবং সমপ্রকটতায় উভয় অ্যালিলের সমান প্রকাশ (আন্দালুসিয়ান মোরগ) ঘটে।",
            "hack": "লিথাল জিনে হোমোজাইগাস প্রচ্ছন্ন বা প্রকট অবস্থায় ভ্রূণাবস্থায় মৃত্যু ঘটে বিধায় ৩:১ অনুপাতটি ২:১ এ পরিবর্তিত হয়!",
            "trap": "মানুষের ব্র্যাকিফ্যালানজি (খাটো আঙুল), হিমোফিলিয়া এবং হলুদ ইঁদুর লিথাল জিনের উদাহরণ।",
            "tags": ["incomplete dominance", "lethal gene", "অসম্পূর্ণ প্রকটতা", "লিথাল জিন"]
        },
        {
            "id": "v_bio_gen_03",
            "subject": "Biology",
            "chapter": "Genetics",
            "type": "shortcut",
            "title": "মেন্ডেলের ২য় সূত্রের ব্যতিক্রমী অনুপাত ছক",
            "formula": "\\text{পরিপূরক জিন: } 9:7; \\quad \\text{প্রকট এপিস্ট্যাসিস: } 13:3; \\quad \\text{দ্বৈত প্রচ্ছন্ন: } 9:7; \\quad \\text{প্রকট বাধা: } 12:3:1",
            "concept": "এপিস্ট্যাসিস প্রক্রিয়ায় একটি নন-অ্যালিলিক জিন অপর জিনের ফিনোটাইপিক প্রকাশকে বাধা দেয়।",
            "hack": "মানুষের জন্মগত মূক-বধিরতা দ্বৈত প্রচ্ছন্ন এপিস্ট্যাসিসের উদাহরণ (৯:৭)! সাদা লেগহর্ন মোরগের প্রকট এপিস্ট্যাসিস (১৩:৩)!",
            "trap": "পলিজেনিক ইনহেরিটেন্সের ক্ষেত্রে ফিনোটাইপিক অনুপাত ১ : ৪ : ৬ : ৪ : ১ (মানুষের গায়ের রঙ ও উচ্চতা)।",
            "tags": ["epistasis", "complementary genes", "এপিস্ট্যাসিস", "পরিপূরক জিন"]
        },
        {
            "id": "v_bio_gen_04",
            "subject": "Biology",
            "chapter": "Genetics",
            "type": "core_formula",
            "title": "সেক্স-লিংকড ইনহেরিটেন্স ও ক্রিস-ক্রস উত্তরাধিকার",
            "formula": "\\text{পিতা থেকে কন্যারা পায় এবং কন্যারা পরবর্তীতে তাদের পুত্রদের প্রদান করে}",
            "concept": "X ক্রোমোজোমে অবস্থিত কিন্তু লিঙ্গ নির্ধারণে ভূমিকা রাখে না এমন জিনকে সেক্স-লিংকড জিন বলে।",
            "hack": "বর্ণান্ধ বা হিমোফিলিক পিতা ও স্বাভাবিক সুস্থ মাতার সকল পুত্র ১০০% সুস্থ হবে এবং সকল কন্যা বাহক (Carrier) হবে!",
            "trap": "পুরুষের কেবল একটি X ক্রোমোজোম থাকায় সে কখনোই সেক্স-লিংকড রিসেসিভ রোগের বাহক হতে পারে না; হয় সুস্থ নতুবা আক্রান্ত।",
            "tags": ["sex-linked", "color blindness", "hemophilia", "বর্ণান্ধতা", "হিমোফিলিয়া", "ক্রিস-ক্রস"]
        },
        {
            "id": "v_bio_gen_05",
            "subject": "Biology",
            "chapter": "Genetics",
            "type": "trap",
            "title": "Rh ফ্যাক্টর ও এরিথ্রোব্লাস্টোসিস ফিটালিস",
            "formula": "\\text{পিতা } Rh^+ + \\text{মাতা } Rh^- \\implies \\text{২য় সন্তান আক্রান্ত (Erythroblastosis Fetalis)}",
            "concept": "Rh- মাতার ১ম গর্ভের Rh+ সন্তান প্রসবের সময় মাতার রক্তে অ্যান্টি-Rh অ্যান্টিবডি তৈরি হয় যা পরবর্তী Rh+ সন্তানের ভ্রূণ ধ্বংস করে।",
            "hack": "১ম সন্তান স্বাভাবিক ও সুস্থ জন্মায়; সমস্যা কেবল ২য় ও পরবর্তী Rh+ সন্তানের ক্ষেত্রে ঘটে!",
            "trap": "মাতা Rh+ হলে পিতা Rh- হলেও কোনো সমস্যা নেই; রোগ কেবল তখনই হয় যখন মাতা নিজে Rh-।",
            "tags": ["Rh factor", "Erythroblastosis", "Rh ফ্যাক্টর", "রক্তের গ্রুপ", "trap"]
        },
        {
            "id": "v_bio_gen_06",
            "subject": "Biology",
            "chapter": "Genetics",
            "type": "core_formula",
            "title": "ABO রক্তের গ্রুপ ও অ্যান্টিজেন-অ্যান্টিবডি",
            "formula": "\\text{গ্রুপ A (অ্যান্টিজেন A, অ্যান্টিবডি b); গ্রুপ B (অ্যান্টিজেন B, অ্যান্টিবডি a); গ্রুপ AB (উভয় অ্যান্টিজেন, কোনো অ্যান্টিবডি নেই); গ্রুপ O (কোনো অ্যান্টিজেন নেই)}",
            "concept": "কার্ল ল্যান্ডস্টেইনার ১৯০১ সালে ABO রক্তের গ্রুপ আবিষ্কার করেন। রক্তের লোহিত কণিকায় অ্যান্টিজেন এবং রক্তরসে অ্যান্টিবডি থাকে।",
            "hack": "AB হলো সর্বজনীন গ্রহীতা (Universal Recipient) এবং O হলো সর্বজনীন দাতা (Universal Donor)!",
            "trap": "O গ্রুপে কোনো অ্যান্টিজেন নেই কিন্তু উভয় অ্যান্টিবডি (a ও b) উপস্থিত থাকে।",
            "tags": ["blood groups", "ABO", "antigen antibody", "সর্বজনীন দাতা"]
        },
        {
            "id": "v_bio_gen_07",
            "subject": "Biology",
            "chapter": "Genetics",
            "type": "shortcut",
            "title": "ক্রোমোজোমীয় অস্বাভাবিকতা ও সিন্ড্রোম",
            "formula": "\\text{ডাউন সিন্ড্রোম: ২১নং ট্রাইসোমি (৪৭); টার্নার: 45,X0; ক্লাইনফেল্টার: 47,XXY; এডওয়ার্ড: ১৮নং ট্রাইসোমি}",
            "concept": "মিয়োসিসে নন-ডিসজাংশনের কারণে ক্রোমোজোম সংখ্যার হ্রাস-বৃদ্ধি ঘটে।",
            "hack": "টার্নার সিন্ড্রোম একমাত্র মনোজোমিক সিন্ড্রোম যা মানবদেহে বেঁচে থাকে (৪৫টি ক্রোমোজোম, মহিলা ফিনোটাইপ)!",
            "trap": "ডাউন সিন্ড্রোম অটোজোমীয় (২১তম ক্রোমোজোম), কিন্তু টার্নার ও ক্লাইনফেল্টার সেক্স ক্রোমোজোমীয় অস্বাভাবিকতা।",
            "tags": ["chromosomal disorders", "Down syndrome", "Turner", "সিন্ড্রোম"]
        },
        {
            "id": "v_bio_gen_08",
            "subject": "Biology",
            "chapter": "Genetics",
            "type": "core_formula",
            "title": "হার্ডি-ওয়াইনবার্গ সাম্যাবস্থা (Hardy-Weinberg Equilibrium)",
            "formula": "p + q = 1, \\quad p^2 + 2pq + q^2 = 1",
            "concept": "মিউটেশন, প্রাকৃতিক নির্বাচন, জিন প্রবাহ না থাকলে কোনো পপুলেশনে অ্যালিল ফ্রিকোয়েন্সি প্রজন্ম পরম্পরায় স্থির থাকে।",
            "hack": "p^2 হলো হোমোজাইগাস প্রকট, 2pq হলো হেটেরোজাইগাস, এবং q^2 হলো হোমোজাইগাস প্রচ্ছন্ন!",
            "trap": "রোগে আক্রান্তের হার মানে q^2 (ফিনোটাইপ), শুধু অ্যালিল ফ্রিকোয়েন্সি q নয়।",
            "tags": ["Hardy-Weinberg", "population genetics", "হার্ডি-ওয়াইনবার্গ", "অ্যালিল ফ্রিকোয়েন্সি"]
        }
    ])

    # 3. Plant Physiology
    entries.extend([
        {
            "id": "v_bio_pp_01",
            "subject": "Biology",
            "chapter": "Plant Physiology",
            "type": "core_formula",
            "title": "C3 বনাম C4 চক্রের তুলনামূলক পার্থক্য",
            "formula": "C_3: \\text{RuBP (5C) } \\to \\text{ 3-PGA (3C)}; \\quad C_4: \\text{PEP (3C) } \\to \\text{ OAA (4C)}",
            "concept": "C3 চক্রের প্রধান এনজাইম রুবিসকো (RuBisCO); C4 চক্রের প্রথম এনজাইম পেপ-কার্বক্সিলেজ (PEP carboxylase)।",
            "hack": "C4 উদ্ভিদে ক্রাঞ্জ অ্যানাটমি (বান্ডল সিথ ঘিরে ঘন বলয়) থাকে এবং ফটোরেস্পিরেশন ঘটে না (ভুট্টা, আখ, মুথা ঘাস)!",
            "trap": "C4 উদ্ভিদেও ক্যালভিন চক্র (C3) ঘটে, তবে তা বান্ডল সিথ কোষে সম্পন্ন হয়।",
            "tags": ["C3", "C4", "photosynthesis", "RuBisCO", "ক্রাঞ্জ অ্যানাটমি"]
        },
        {
            "id": "v_bio_pp_02",
            "subject": "Biology",
            "chapter": "Plant Physiology",
            "type": "shortcut",
            "title": "শ্বসনিক কোশেন্ট (RQ) মুখস্থ মান",
            "formula": "RQ = \\frac{\\text{উৎপন্ন } CO_2}{\\text{গৃহীত } O_2} \\implies \\text{গ্লুকোজ: } 1.0, \\; \\text{ম্যালিক এসিড: } 1.33, \\; \\text{লিপিড: } 0.71, \\; \\text{অবাত: } \\infty",
            "concept": "শ্বসনিক বস্তুর জারণে প্রয়োজনীয় অক্সিজেনের পরিমাণের ওপর RQ নির্ভর করে।",
            "hack": "অর্গানিক এসিডে অক্সিজেনের অনুপাত বেশি থাকায় RQ > 1 হয়; ফ্যাটে অক্সিজেনের ঘাটতি থাকায় RQ < 1 হয়!",
            "trap": "অবাত শ্বসনে কোনো অক্সিজেন ব্যবহৃত হয় না (O2 = 0) বিধায় এর RQ অসীম (\\infty)।",
            "tags": ["RQ", "respiratory quotient", "শ্বসনিক কোশেন্ট", "গ্লুকোজ"]
        },
        {
            "id": "v_bio_pp_03",
            "subject": "Biology",
            "chapter": "Plant Physiology",
            "type": "core_formula",
            "title": "অ্যারোবিক শ্বসনের নিট ATP হিসাব",
            "formula": "\\text{গ্লাইকোলাইসিস (৮ বা ৬)} + \\text{অ্যাসিটাইল কো-এ (৬)} + \\text{ক্রেবস চক্র (২৪)} = 38 \\text{ বা } 36 \\text{ ATP (আধুনিক ৩০ বা ৩২)}",
            "concept": "প্রতিটি NADH+H+ জারণে ৩টি (আধুনিক ২.৫টি) এবং FADH2 জারণে ২টি (আধুনিক ১.৫টি) ATP তৈরি হয়।",
            "hack": "গ্লাইকোলাইসিসে সরাসরি নিট তৈরি হয় ২ ATP এবং ২ NADH+H+! এটি সাইটোপ্লাজমে ঘটে এবং অক্সিজেনের প্রয়োজন হয় না।",
            "trap": "ক্রেবস চক্র ও ইলেকট্রন ট্রান্সপোর্ট চেইন মাইটোকন্ড্রিয়ার ম্যাট্রিক্স ও ক্রিস্টিতে সম্পন্ন হয়।",
            "tags": ["aerobic respiration", "ATP calculation", "গ্লাইকোলাইসিস", "ক্রেবস চক্র"]
        },
        {
            "id": "v_bio_pp_04",
            "subject": "Biology",
            "chapter": "Plant Physiology",
            "type": "shortcut",
            "title": "উদ্ভিদের ম্যাক্রো ও মাইক্রো পুষ্টি উপাদান",
            "formula": "\\text{ম্যাক্রো ৯টি: C, H, O, N, P, K, Ca, Mg, S (ছন্দ: Mg K Cafe for Nice CHO)}",
            "concept": "অত্যাবশ্যকীয় উপাদান ১৭টি। উদ্ভিদের শুষ্ক ওজনের প্রতি গ্রামে ১ মিলিগ্রামের বেশি লাগলে ম্যাক্রোনিউট্রিয়েন্ট।",
            "hack": "ক্লোরোফিল অণুর কেন্দ্রে ম্যাগনেসিয়াম (Mg) পরমাণু এবং হিমোগ্লোবিনে আয়রন (Fe) থাকে!",
            "trap": "C, H, O মাটি থেকে নয়, সরাসরি বায়ু ও পানি থেকে শোষিত হয়।",
            "tags": ["essential elements", "macronutrients", "ম্যাক্রো উপাদান", "ক্লোরোফিল"]
        },
        {
            "id": "v_bio_pp_05",
            "subject": "Biology",
            "chapter": "Plant Physiology",
            "type": "trap",
            "title": "দ্রুততম ও মন্থরতম শোষিত আয়ন",
            "formula": "\\text{দ্রুততম: } K^+, NO_3^-; \\quad \\text{মন্থরতম: } Ca^{2+}, SO_4^{2-}",
            "concept": "আয়ন শোষণ প্রধানত সক্রিয় ও নিষ্ক্রিয় প্রক্রিয়ায় সম্পন্ন হয়। ক্যাটায়নের মধ্যে পটাশিয়াম এবং অ্যানায়নের মধ্যে নাইট্রেট সবচেয়ে দ্রুত শোষিত হয়।",
            "hack": "চার্জের ঘনত্ব বেশি এবং আকার বড় হলে শোষণ ধীরগতির হয় (যেমন Ca2+, SO4 2-)।",
            "trap": "উদ্ভিদ সরাসরি অণু বা লবণ শোষণ করতে পারে না; কেবল ক্যাটায়ন ও অ্যানায়ন আয়ন হিসেবে শোষণ করে।",
            "tags": ["ion absorption", "K+", "Ca2+", "আয়ন শোষণ", "trap"]
        },
        {
            "id": "v_bio_pp_06",
            "subject": "Biology",
            "chapter": "Plant Physiology",
            "type": "core_formula",
            "title": "পত্ররন্ধ্র খোলা ও বন্ধ হওয়ার আধুনিক প্রোটন পাম্প মতবাদ",
            "formula": "\\text{আলোতে: } K^+ \\text{ প্রবেশ} + H^+ \\text{ বের হওয়া} \\implies \\text{রক্ষীকোষ স্ফীত ও রন্ধ্র উন্মুক্ত}",
            "concept": "লেভিট (1974) প্রস্তাবিত সক্রিয় প্রোটন-পটাশিয়াম পাম্প মতবাদ সর্বাধিক গ্রহণযোগ্য।",
            "hack": "নীল আলো রক্ষীকোষের প্রোটন পাম্পকে সক্রিয় করে; অ্যাবসিসিক অ্যাসিড (ABA) হরমোন পত্ররন্ধ্র বন্ধ করে দেয়!",
            "trap": "প্রস্বেদনের ৯০-৯৫% পানি পত্ররন্ধ্রের মাধ্যমে বাষ্পাকারে বের হয় (পত্ররন্ধ্রীয় প্রস্বেদন)।",
            "tags": ["stomata", "potassium pump", "পত্ররন্ধ্র", "প্রস্বেদন"]
        },
        {
            "id": "v_bio_pp_07",
            "subject": "Biology",
            "chapter": "Plant Physiology",
            "type": "shortcut",
            "title": "সালোকসংশ্লেষণে নির্গত অক্সিজেনের উৎস",
            "formula": "2H_2O \\xrightarrow{\\text{আলোক বিশ্লেষণ (ফোটোলাইসিস)}} 4H^+ + 4e^- + O_2",
            "concept": "রবিন হিল এবং ভ্যান নীল তেজস্ক্রিয় আইসোটোপ ও ১৮ (O-18) ব্যবহার করে প্রমাণ করেন নির্গত O2 আসে পানি থেকে, CO2 থেকে নয়।",
            "hack": "পানির ফোটোলাইসিসের জন্য ম্যাঙ্গানিজ (Mn2+) এবং ক্লোরাইড (Cl-) আয়ন অপরিহার্য!",
            "trap": "CO2 বিচারিত হয়ে শর্করা (গ্লুকোজ) তৈরি করে, এটি অক্সিজেনের উৎস নয়।",
            "tags": ["photolysis", "water", "oxygen source", "ফোটোলাইসিস"]
        },
        {
            "id": "v_bio_pp_08",
            "subject": "Biology",
            "chapter": "Plant Physiology",
            "type": "core_formula",
            "title": "চক্রীয় বনাম অচক্রীয় ফটোফসফোরাইলেশন",
            "formula": "\\text{অচক্রীয়: PS-I ও PS-II উভয়ই যুক্ত} \\implies \\text{ATP, } NADPH+H^+ \\text{ ও } O_2 \\text{ তৈরি হয়}",
            "concept": "চক্রীয়তে কেবল PS-I (P700) যুক্ত থাকে এবং শুধুই ATP তৈরি হয় (কোনো NADPH+H+ বা O2 তৈরি হয় না)।",
            "hack": "অচক্রীয় ফটোফসফোরাইলেশনে ইলেকট্রনের প্রবাহ 'Z-স্কিম' নামে পরিচিত!",
            "trap": "ফোটোসিস্টেম-২ (PS-II) এর বিক্রিপাকেন্দ্র হলো P680 এবং ফোটোসিস্টেম-১ এর হলো P700।",
            "tags": ["photophosphorylation", "PS-I", "PS-II", "ফটোফসফোরাইলেশন"]
        }
    ])

    # 4. Human Physiology - Digestion
    entries.extend([
        {
            "id": "v_bio_dig_01",
            "subject": "Biology",
            "chapter": "Human Physiology (Digestion)",
            "type": "core_formula",
            "title": "দাঁতের সংকেত ও দুধদাঁতের অনুপস্থিত দাঁত",
            "formula": "\\text{প্রাপ্তবয়স্ক: } i\\frac{2}{2} c\\frac{1}{1} pm\\frac{2}{2} m\\frac{3}{3} = 32, \\quad \\text{দুধদাঁত: } i\\frac{2}{2} c\\frac{1}{1} pm\\frac{0}{0} m\\frac{2}{2} = 20",
            "concept": "মানুষের দাঁত ডাইফায়োডন্ট (জীবনে দুবার গজায়), থেকোডন্ট (চোয়ালের খাঁজে বসানো) ও হেটেরোডন্ট (ভিন্ন গঠন)।",
            "hack": "দুধদাঁতে প্রিমোলার (অগ্রপেষণ) সম্পূর্ণ অনুপস্থিত এবং মোলার দাঁত কেবল ২টি করে থাকে!",
            "trap": "আক্কেল দাঁত হলো ৩য় মোলার দাঁত যা ১৮-২৫ বছর বয়সে গজায়।",
            "tags": ["dental formula", "milk teeth", "দাঁতের সংকেত", "দুধদাঁত"]
        },
        {
            "id": "v_bio_dig_02",
            "subject": "Biology",
            "chapter": "Human Physiology (Digestion)",
            "type": "shortcut",
            "title": "পাকস্থলীর বিভিন্ন কোষের ক্ষরণ ছক",
            "formula": "\\text{প্যারাইটাল: HCl ও ক্যাসলের ফ্যাক্টর; চিপ/জাইমোজেনিক: পেপসিনোজেন; মিউকাস: মিউসিন; G-কোষ: গ্যাস্ট্রিন}",
            "concept": "পাকস্থলীর গ্যাস্ট্রিক রসের pH প্রায় ১.৫ - ২.০ (তীব্র অম্লীয়)।",
            "hack": "ক্যাসলের ইন্ট্রিনসিক ফ্যাক্টর ক্ষুদ্রান্ত্রে ভিটামিন B12 শোষণে সাহায্য করে (অভাবে পারনিশিয়াস অ্যানিমিয়া হয়)!",
            "trap": "প্যারাইটাল কোষের অপর নাম অক্সিন্টিক কোষ; চিপ কোষ এনজাইম ক্ষরণ করে।",
            "tags": ["gastric cells", "parietal cell", "HCl", "প্যারাইটাল কোষ", "পেপসিনোজেন"]
        },
        {
            "id": "v_bio_dig_03",
            "subject": "Biology",
            "chapter": "Human Physiology (Digestion)",
            "type": "trap",
            "title": "পিত্তরসের উপাদান ও এনজাইমহীনতা",
            "formula": "\\text{পিত্তরসে কোনো পরিপাককারী এনজাইম থাকে না!}",
            "concept": "পিত্তলবণ (সোডিয়াম গ্লাইকোকোলেট ও সোডিয়াম টরোকোলেট) চর্বি জাতীয় খাদ্যের পৃষ্ঠটান কমিয়ে ক্ষুদ্র কণায় রূপান্তর করে (ইমালসিফিকেশন)।",
            "hack": "পিত্তরঞ্জক হলো বিলিরুবিন (হলুদ) ও বিলিভার্ডিন (সবুজ), যা হিমোগ্লোবিনের ভাঙন থেকে তৈরি হয়!",
            "trap": "পিত্তরস ক্ষারীয় (pH 7.6 - 8.6); এতে কোনো এনজাইম না থাকা সত্ত্বেও এটি লাইপেজের কাজকে বহুগুণ ত্বরান্বিত করে।",
            "tags": ["bile", "emulsification", "পিত্তরস", "ইমালসিফিকেশন", "trap"]
        },
        {
            "id": "v_bio_dig_04",
            "subject": "Biology",
            "chapter": "Human Physiology (Digestion)",
            "type": "core_formula",
            "title": "অগ্ন্যাশয় রসের প্রধান এনজাইম ও ভূমিকা",
            "formula": "\\text{প্রোটিন: ট্রিপসিন, কাইমোট্রিপসিন; শর্করা: অ্যামাইলেজ; চর্বি: লাইপেজ}",
            "concept": "অগ্ন্যাশয় একটি মিশ্র গ্রন্থি (উভয় অন্তঃক্ষরা ও বহিঃক্ষরা)। এর বহিঃক্ষরা অংশ এসিনাস ক্ষারীয় অগ্ন্যাশয় রস ক্ষরণ করে।",
            "hack": "নিষ্ক্রিয় ট্রিপসিনোজেনকে সক্রিয় ট্রিপসিনে রূপান্তরিত করে ক্ষুদ্রান্ত্রের এন্টারোকাইনেজ (Enterokinase) এনজাইম!",
            "trap": "অগ্ন্যাশয়ের আইলেটস অব ল্যাঙ্গারহ্যান্স হরমোন (ইনসুলিন, গ্লুকাগন) ক্ষরণ করে, এনজাইম নয়।",
            "tags": ["pancreatic juice", "trypsin", "amylase", "অগ্ন্যাশয় রস", "ট্রিপসিন"]
        },
        {
            "id": "v_bio_dig_05",
            "subject": "Biology",
            "chapter": "Human Physiology (Digestion)",
            "type": "shortcut",
            "title": "ক্ষুদ্রান্ত্রের ভিলি ও ফ্যাট শোষণ (ল্যাকটিয়েল)",
            "formula": "\\text{গ্লুকোজ ও অ্যামিনো অ্যাসিড: রক্ত কৈশিক জালিকা} \\to \\text{হেপাটিক পোর্টাল শিরা}; \\quad \\text{ফ্যাট: ল্যাকটিয়েল (লসিকানালি)}",
            "concept": "ফ্যাটি এসিড ও গ্লিসারল অন্ত্রের কোষে প্রবেশ করে ট্রাইগ্লিসারাইড ও প্রোটিনের আবরণে আবৃত হয়ে কাইলোমাইক্রন তৈরি করে।",
            "hack": "কাইলোমাইক্রন রক্তে সরাসরি প্রবেশ না করে ভিলাইয়ের কেন্দ্রীয় ল্যাকটিয়েলে প্রবেশ করে দুধের মতো সাদা তরল কাইল গঠন করে!",
            "trap": "ল্যাকটিয়েল লসিকা নালি, কোনো রক্তনালি নয়।",
            "tags": ["lacteal", "chylomicron", "villi", "ল্যাকটিয়েল", "কাইলোমাইক্রন"]
        },
        {
            "id": "v_bio_dig_06",
            "subject": "Biology",
            "chapter": "Human Physiology (Digestion)",
            "type": "core_formula",
            "title": "যকৃতের বিপাকীয় কাজ ও জৈব রসায়নাগার",
            "formula": "\\text{গ্লাইকোজেনেসিস (গ্লুকোজ } \\to \\text{ গ্লাইকোজেন)}, \\quad \\text{গ্লাইকোজেনোলাইসিস (গ্লাইকোজেন } \\to \\text{ গ্লুকোজ)}",
            "concept": "যকৃত মানবদেহের বৃহত্তম গ্রন্থি (ওজন ১.৫ - ২ কেজি)। এটি গ্লুকোনিওজেনেসিসের মাধ্যমে নন-কার্বোহাইড্রেট থেকে গ্লুকোজ তৈরি করতে পারে।",
            "hack": "অ্যামিনো অ্যাসিডের ডিঅ্যামিনেশন ঘটিয়ে কিটো এসিড ও বিষাক্ত অ্যামোনিয়া তৈরি করে, যা অনিথিন চক্রে ইউরিয়ায় পরিণত হয়!",
            "trap": "ইনসুলিন রক্তে গ্লুকোজ কমায় (গ্লাইকোজেনেসিস বাড়ায়); গ্লুকাগন রক্তে গ্লুকোজ বাড়ায়।",
            "tags": ["liver", "glycogenesis", "urea cycle", "যকৃত", "অনিথিন চক্র"]
        },
        {
            "id": "v_bio_dig_07",
            "subject": "Biology",
            "chapter": "Human Physiology (Digestion)",
            "type": "shortcut",
            "title": "পরিপাকে অংশগ্রহণকারী প্রধান হরমোন",
            "formula": "\\text{গ্যাস্ট্রিন (HCl বাড়ায়), সিক্রেটিন (অগ্ন্যাশয় রস ক্ষরণ করায়), CCK (পিত্তথলি সংকোচন করায়)}",
            "concept": "সিক্রেটিন (Secretin) হলো চিকিৎসাবিজ্ঞানের ইতিহাসে আবিষ্কৃত সর্বপ্রথম হরমোন (Bayliss & Starling, 1902)।",
            "hack": "কলিসিস্টোকাইনিন (CCK) পিত্তথলিকে সংকুচিত করে পিত্তরস ডুওডেনামে পাঠায় এবং অগ্ন্যাশয় থেকে এনজাইম ক্ষরণ করায়!",
            "trap": "সিক্রেটিন পাকস্থলীর গতিশীলতা ও HCl ক্ষরণ হ্রাস করে (বাধা দেয়)।",
            "tags": ["digestive hormones", "secretin", "CCK", "সিক্রেটিন", "গ্যাস্ট্রিন"]
        },
        {
            "id": "v_bio_dig_08",
            "subject": "Biology",
            "chapter": "Human Physiology (Digestion)",
            "type": "trap",
            "title": "বৃহদান্ত্রের কাজ ও অ্যাপেন্ডিক্স",
            "formula": "\\text{বৃহদান্ত্রে কোনো খাদ্য পরিপাক হয় না; শুধুই পানি, খনিজ লবণ শোষণ ও মল তৈরি হয়}",
            "concept": "সিকামের সাথে যুক্ত আঙ্গুলের মতো প্রবৃদ্ধি হলো ভার্মিফর্ম অ্যাপেন্ডিক্স (একটি নিষ্ক্রিয় বা লুপ্তপ্রায় অঙ্গ)।",
            "hack": "বৃহদান্ত্রের উপকারী কোলোনিক ব্যাকটেরিয়া (যেমন E. coli) ভিটামিন K এবং ভিটামিন B কমপ্লেক্স সংশ্লেষ করে!",
            "trap": "অ্যাপেন্ডিসাইটিসে তলপেটের ডান পাশে তীব্র ব্যথা অনুভূত হয় (ম্যাকবার্নিজ পয়েন্ট)।",
            "tags": ["large intestine", "appendix", "বৃহদান্ত্র", "অ্যাপেন্ডিক্স"]
        }
    ])

    # 5. Human Physiology - Circulation
    entries.extend([
        {
            "id": "v_bio_cir_01",
            "subject": "Biology",
            "chapter": "Human Physiology (Circulation)",
            "type": "core_formula",
            "title": "রক্তের স্বাভাবিক উপাদান ও শতকরা হার",
            "formula": "\\text{রক্তরস (প্লাজমা) ৫৫\\%} + \\text{রক্তকণিকা ৪৫\\%}, \\quad \\text{প্লাজমার ৯১-৯২\\% পানি ও ৮-৯\\% কঠিন বস্তু}",
            "concept": "রক্তদেহের ওজনের প্রায় ৭-৮% (প্রাপ্তবয়স্কের ৫-৬ লিটার)। রক্তের প্রধান প্লাজমা প্রোটিন: অ্যালবুমিন, গ্লোবিউলিন, ফাইব্রিনোজেন, প্রোথ্রম্বিন।",
            "hack": "অ্যালবুমিন রক্তের অসমোটিক চাপ নিয়ন্ত্রণ করে; গ্লোবিউলিন (ইমিউনোগ্লোবুলিন) অ্যান্টিবডি হিসেবে কাজ করে!",
            "trap": "সিরামে ফাইব্রিনোজেন ও প্রোথ্রম্বিন সহ রক্ত জমাট বাঁধার ফ্যাক্টরগুলো থাকে না।",
            "tags": ["blood composition", "plasma", "রক্তরস", "প্লাজমা প্রোটিন"]
        },
        {
            "id": "v_bio_cir_02",
            "subject": "Biology",
            "chapter": "Human Physiology (Circulation)",
            "type": "shortcut",
            "title": "রক্তকণিকার সংখ্যা ও আয়ুষ্কাল ছক",
            "formula": "\\text{RBC: ৫০ লক্ষ (১২০ দিন); WBC: ৪০০০–১১০০০ (১–১৫ দিন); অণুচক্রিকা: ১.৫–৪ লক্ষ (৫–১০ দিন)}",
            "concept": "RBC নিউক্লিয়াসবিহীন দ্বি-অবতল গোল চাকতি; এর ভেতরে হিমোগ্লোবিন থাকে (পুরুষে 14-16 g/dL)।",
            "hack": "শ্বেত রক্তকণিকার মধ্যে নিউট্রোফিল সর্বাধিক (৪০-৭০%), দ্বিতীয় লিম্ফোসাইট (২০-৪০%)!",
            "trap": "স্তন্যপায়ীদের মধ্যে কেবল উটের লোহিত কণিকায় ডিম্বাকার নিউক্লিয়াস থাকে, মানুষের RBC তে নিউক্লিয়াস থাকে না।",
            "tags": ["blood cells", "lifespan", "RBC", "WBC", "আয়ুষ্কাল"]
        },
        {
            "id": "v_bio_cir_03",
            "subject": "Biology",
            "chapter": "Human Physiology (Circulation)",
            "type": "core_formula",
            "title": "হৃদপিণ্ডের কপাটিকা (Valves) ও অবস্থান",
            "formula": "\\text{ডান অলিন্দ-নিলয়: ট্রাইকাস্পিড; বাম অলিন্দ-নিলয়: বাইকাস্পিড (মাইট্রাল); ধমনিতে: সেমিলুনার কপাটিকা}",
            "concept": "কপাটিকাগুলো রক্তকে সর্বদা একমুখী প্রবাহে বাধ্য করে এবং বিপরীতমুখী প্রবাহ রোধ করে।",
            "hack": "করোনারি সাইনাসের মুখে থিবেসিয়ান কপাটিকা এবং নিম্ন মহাশিরায় ইউস্টেশিয়ান কপাটিকা থাকে!",
            "trap": "বাইকাস্পিড কপাটিকার অপর নাম মাইট্রাল কপাটিকা; এটি বাম পাশে অবস্থিত।",
            "tags": ["heart valves", "bicuspid", "tricuspid", "কপাটিকা", "মাইট্রাল"]
        },
        {
            "id": "v_bio_cir_04",
            "subject": "Biology",
            "chapter": "Human Physiology (Circulation)",
            "type": "shortcut",
            "title": "হৃদস্পন্দনের উৎপত্তি ও সঞ্চালন সময়",
            "formula": "\\text{SAN (পেসমেকার) } \\xrightarrow{0.03s} \\text{ AVN } \\xrightarrow{0.09s \\text{ বিলম্ব}} \\text{ বান্ডল অব হিস } \\xrightarrow{0.04s} \\text{ পুরকিঞ্জে তন্তু}",
            "concept": "SAN প্রতি মিনিটে ৭০-৮০ বার সংকেত সৃষ্টি করে স্বয়ংক্রিয়ভাবে হৃদস্পন্দন শুরু করে (মায়োজেনিক নিয়ন্ত্রণ)।",
            "hack": "SAN থেকে সংকেত নিলয়ে পৌঁছাতে মোট সময় ০.১৬ সেকেন্ড! AVN বিলম্বের কারণে অলিন্দ আগে সংকুচিত হতে পারে।",
            "trap": "যদি SAN নষ্ট হয়ে যায় তবে সংরক্ষিত পেসমেকার হিসেবে AVN (৪০-৬০ বার/মিনিট) কাজ শুরু করে।",
            "tags": ["pacemaker", "SAN", "AVN", "হৃদস্পন্দন সঞ্চালন", "মায়োজেনিক"]
        },
        {
            "id": "v_bio_cir_05",
            "subject": "Biology",
            "chapter": "Human Physiology (Circulation)",
            "type": "core_formula",
            "title": "হৃদচক্রের সময় বিভাজন (০.৮ সেকেন্ড)",
            "formula": "\\text{অলিন্দ: সিস্টোল ০.১s, ডায়াস্টোল ০.৭s; নিলয়: সিস্টোল ০.৩s, ডায়াস্টোল ০.৫s}",
            "concept": "হৃদপিণ্ডের একবার সংকোচন (সিস্টোল) ও একবার প্রসারণকে (ডায়াস্টোল) একত্রে একটি হৃদচক্র বলে।",
            "hack": "১ম হৃদধ্বনি 'LUB' হয় নিলয় সিস্টোলে বাইকাস্পিড/ট্রাইকাস্পিড বন্ধের সময়; ২য় শব্দ 'DUB' হয় সেমিলুনার বন্ধের সময়!",
            "trap": "অলিন্দ ও নিলয় কখনোই একসাথে সংকুচিত হয় না; তবে উভয়ই একসাথে ডায়াস্টোলে (০.৪ সেকেন্ড) থাকতে পারে।",
            "tags": ["cardiac cycle", "systole", "diastole", "LUB DUB", "হৃদচক্র"]
        },
        {
            "id": "v_bio_cir_06",
            "subject": "Biology",
            "chapter": "Human Physiology (Circulation)",
            "type": "shortcut",
            "title": "ইসিজি (ECG) তরঙ্গ ও তাৎপর্য",
            "formula": "\\text{P-তরঙ্গ: অলিন্দ ডিলারাইজেশন; QRS কমপ্লেক্স: নিলয় ডিপোলারাইজেশন; T-তরঙ্গ: নিলয় রিপোলারাইজেশন}",
            "concept": "হৃদপিণ্ডের পেশির বৈদ্যুতিক ক্রিয়াকলাপের গ্রাফিক্যাল রেকর্ড। উইলিয়াম আইন্থোভেনকে ECG এর জনক বলা হয়।",
            "hack": "QRS কমপ্লেক্স নিলয়ের শক্তিশালী সিস্টোল ও ডিপোলারাইজেশন নির্দেশ করে; এর সময়কাল প্রায় ০.০৮-০.১০ সেকেন্ড!",
            "trap": "T-তরঙ্গ উল্টে গেলে বা ST-সেগমেন্ট উঁচুতে উঠলে মায়োকার্ডিয়াল ইনফার্কশন (হার্ট অ্যাটাক) নির্দেশ করে।",
            "tags": ["ECG", "P wave", "QRS complex", "ইসিজি", "ডিপোলারাইজেশন"]
        },
        {
            "id": "v_bio_cir_07",
            "subject": "Biology",
            "chapter": "Human Physiology (Circulation)",
            "type": "trap",
            "title": "পালমোনারি ধমনি ও শিরার রক্ত ব্যতিক্রম",
            "formula": "\\text{পালমোনারি ধমনি: } CO_2 \\text{-সমৃদ্ধ রক্ত; পালমোনারি শিরা: } O_2 \\text{-সমৃদ্ধ রক্ত}",
            "concept": "সাধারণত ধমনি অক্সিজেনযুক্ত এবং শিরা কার্বন ডাই-অক্সাইডযুক্ত রক্ত বহন করে।",
            "hack": "ফুসফুসীয় (পালমোনারি) রক্ত সংবহনে এর সম্পূর্ণ ব্যতিক্রম ঘটে!",
            "trap": "ধমনি সর্বদা হৃদপিণ্ড থেকে রক্তের প্রবাহ দেহের দিকে নিয়ে যায় এবং শিরা সর্বদা হৃদপিণ্ডের দিকে রক্ত নিয়ে আসে।",
            "tags": ["pulmonary circulation", "artery vein exception", "পালমোনারি ধমনি", "trap"]
        },
        {
            "id": "v_bio_cir_08",
            "subject": "Biology",
            "chapter": "Human Physiology (Circulation)",
            "type": "core_formula",
            "title": "রক্তনালির প্রাচীরের তিনটি স্তর",
            "formula": "\\text{টিউনিকা এক্সটার্না (বাইরে, যোজক কলা) } + \\text{টিউনিকা মিডিয়া (মাঝে, মসৃণ পেশি) } + \\text{টিউনিকা ইন্টার্না (ভেতরে, এন্ডোথেলিয়াম)}",
            "concept": "ধমনির টিউনিকা মিডিয়া অত্যন্ত পুরু ও স্থিতিস্থাপক; শিরার টিউনিকা মিডিয়া পাতলা এবং এর ভেতরে কপাটিকা থাকে।",
            "hack": "কৈশিক জালিকায় (Capillary) কেবল একক স্তরবিশিষ্ট টিউনিকা ইন্টার্না বা এন্ডোথেলিয়াম থাকে!",
            "trap": "ধমনিতে কোনো কপাটিকা থাকে না (উচ্চ চাপে রক্ত ছোটে); কিন্তু শিরায় রক্তের পশ্চাৎপ্রবাহ রোধে কপাটিকা থাকে।",
            "tags": ["tunica media", "artery vs vein", "রক্তনালি", "কপাটিকা"]
        }
    ])

    # 6. Human Physiology - Excretion
    entries.extend([
        {
            "id": "v_bio_exc_01",
            "subject": "Biology",
            "chapter": "Human Physiology (Excretion)",
            "type": "core_formula",
            "title": "নেফ্রনের গঠন ও ম্যালপিজিয়ান বডি",
            "formula": "\\text{নেফ্রন} = \\text{ম্যালপিজিয়ান বডি (গ্লোমেরুলাস + বোম্যান্স ক্যাপসুল)} + \\text{রেনাল টিউবিউল}",
            "concept": "প্রতিটি মানব বৃক্কে ১০-১২ লক্ষ নেফ্রন থাকে। বোম্যান্স ক্যাপসুলের প্রাচীরে পোডোসাইট (Podocyte) কোষ থাকে।",
            "hack": "অ্যাফারেন্ট ধমনিকা গ্লোমেরুলাসে ৫০টি কৈশিক জালিকা তৈরি করে এবং তুলনামূলক সরু ইফারেন্ট ধমনিকা হিসেবে বের হয়!",
            "trap": "ঘাসফড়িংয়ের রেচন অঙ্গ হলো ম্যালপিজিয়ান নালিকা, আর মানুষের নেফ্রনের অংশ হলো ম্যালপিজিয়ান বডি।",
            "tags": ["nephron", "Malpighian body", "glomerulus", "নেফ্রন", "গ্লোমেরুলাস"]
        },
        {
            "id": "v_bio_exc_02",
            "subject": "Biology",
            "chapter": "Human Physiology (Excretion)",
            "type": "shortcut",
            "title": "GFR ও মূত্র উৎপাদনের অনুপাত",
            "formula": "\\text{GFR} = 125 \\text{ mL min}^{-1} = 180 \\text{ L day}^{-1}; \\quad \\text{দৈনিক মূত্র} = 1.5 \\text{ L}",
            "concept": "গ্লোমেরুলার ফিল্ট্রেটের ৯৯% এর বেশি অংশ রেনাল টিউবিউলে পুনঃশোষিত হয়ে মাত্র ১% এরও কম মূত্র হিসেবে নির্গত হয়।",
            "hack": "ফিল্ট্রেটের ৮৫% পানি প্রক্সিমাল প্যাঁচানো নালিকায় অবাধ্য পুনঃশোষণ (Obligatory reabsorption) ঘটে!",
            "trap": "গ্লোমেরুলার ফিল্ট্রেটে কোনো রক্তকণিকা বা প্লাজমা প্রোটিন থাকে না (প্রোটিনবিহীন আল্ট্রাফিল্ট্রেট)।",
            "tags": ["GFR", "filtration rate", "মূত্র উৎপাদন", "পুনঃশোষণ"]
        },
        {
            "id": "v_bio_exc_03",
            "subject": "Biology",
            "chapter": "Human Physiology (Excretion)",
            "type": "core_formula",
            "title": "মূত্রের উপাদান ও ইউরোক্রোম রঞ্জক",
            "formula": "\\text{পানি ৯৫\\%} + \\text{কঠিন বস্তু ৫\\% (ইউরিয়া ২\\%, ইউরিক এসিড, ক্রিয়েটিনিন, NaCl)}",
            "concept": "মূত্র হালকা অম্লীয় (স্বাভাবিক pH 6.0, পরিসীমা 4.5 - 8.0)। আপেক্ষিক গুরুত্ব 1.008 - 1.030।",
            "hack": "হিমোগ্লোবিনের বিপাকীয় রূপান্তর থেকে সৃষ্ট ইউরোক্রোম (Urochrome) রঞ্জকের কারণে মূত্র হালকা হলুদ রঙের হয়!",
            "trap": "কিডনি রোগের সবচেয়ে নির্ভরযোগ্য সূচক হলো রক্তে ক্রিয়েটিনিনের (Creatinine) মাত্রা বৃদ্ধি (স্বাভাবিক ০.৬ - ১.৪ mg/dL)।",
            "tags": ["urine composition", "Urochrome", "creatinine", "মূত্র", "ক্রিয়েটিনিন"]
        },
        {
            "id": "v_bio_exc_04",
            "subject": "Biology",
            "chapter": "Human Physiology (Excretion)",
            "type": "shortcut",
            "title": "হেনলির লুপ ও কাউন্টার কারেন্ট মেকানিজম",
            "formula": "\\text{অবতরণ বাহু: পানির জন্য ভেদ্য}; \\quad \\text{আরোহণ বাহু: লবণের (Na+) জন্য ভেদ্য কিন্তু পানির জন্য অভেদ্য}",
            "concept": "বৃক্কের মেডুলায় উচ্চ অভিস্রবণিক ঘনত্ব (১২০০ mOsm/L) তৈরি করে ঘনীভূত মূত্র উৎপাদন নিয়ন্ত্রণ করে।",
            "hack": "হেনলির লুপের দৈর্ঘ্য যত দীর্ঘ হয়, প্রাণী তত বেশি ঘনীভূত মূত্র ত্যাগ করতে পারে (যেমন মরুভূমির ক্যাঙ্গারু ইঁদুর)!",
            "trap": "পানির পুনঃশোষণ প্রধানত অবতরণ বাহুতে এবং সোডিয়ামের সক্রিয় পাম্পিং আরোহণ বাহুতে ঘটে।",
            "tags": ["loop of Henle", "counter current", "হেনলির লুপ", "কাউন্টার কারেন্ট"]
        },
        {
            "id": "v_bio_exc_05",
            "subject": "Biology",
            "chapter": "Human Physiology (Excretion)",
            "type": "core_formula",
            "title": "মূত্র নিয়ন্ত্রণে হরমোনের ভূমিকা (ADH ও অ্যালডোস্টেরন)",
            "formula": "\\text{ADH (অ্যান্টিডাইইউরেটিক): দূরবর্তী নালি ও সংগ্রাহী নালিতে পানি পুনঃশোষণ বাড়ায়}",
            "concept": "হাইপোথ্যালামাসে তৈরি এবং পশ্চাৎ পিটুইটারি থেকে ক্ষরিত ভ্যাসোপ্রেসিন বা ADH অ্যাকুয়াপোরিন চ্যানেল বৃদ্ধি করে।",
            "hack": "অ্যালডোস্টেরন Na+ পুনঃশোষণ বাড়ায় এবং K+ ত্যাগ করায়! রেনিন-অ্যাঞ্জিওটেনসিন-অ্যালডোস্টেরন সিস্টেম (RAAS) রক্তচাপ বাড়ায়!",
            "trap": "ADH হরমোনের অভাবে প্রস্রাবের পরিমাণ অস্বাভাবিক বৃদ্ধি পায় (দিনে ১০-১৫ লিটার), একে ডায়াবেটিস ইনসিপিডাস বলে।",
            "tags": ["ADH", "aldosterone", "hormonal control", "ডায়াবেটিস ইনসিপিডাস"]
        },
        {
            "id": "v_bio_exc_06",
            "subject": "Biology",
            "chapter": "Human Physiology (Excretion)",
            "type": "trap",
            "title": "যকৃত ও বৃক্কের ইউরিয়া চক্র বনাম নিঃসরণ",
            "formula": "\\text{ইউরিয়া সংশ্লেষিত হয় যকৃতে (অনিথিন চক্রে); কিন্তু নিষ্কাশিত হয় বৃক্কে}",
            "concept": "অ্যামোনিয়া অত্যন্ত বিষাক্ত হওয়ায় যকৃত একে দ্রুত ইউরিয়ায় রূপান্তর করে রক্তে ছেড়ে দেয়।",
            "hack": "হেপাটিক শিরায় ইউরিয়ার ঘনত্ব সর্বাধিক; কিন্তু রেনাল শিরায় ইউরিয়ার ঘনত্ব সর্বনিম্ন!",
            "trap": "ইউরিয়া তৈরি হয় কিডনিতে ভাবা মারাত্মক ভুল; কিডনি কেবল ইউরিয়া ছেঁকে বের করে, তৈরি করে যকৃত।",
            "tags": ["urea synthesis", "liver vs kidney", "ইউরিয়া", "trap"]
        },
        {
            "id": "v_bio_exc_07",
            "subject": "Biology",
            "chapter": "Human Physiology (Excretion)",
            "type": "shortcut",
            "title": "বৃক্কে পাথর (Kidney Stone) এর প্রধান উপাদান",
            "formula": "\\text{ক্যালসিয়াম অক্সালেট (৭৫–৮০\\% পাথরে পাওয়া যায়)}, \\quad \\text{ইউরিক এসিড, ম্যাগনেসিয়াম অ্যামোনিয়াম ফসফেট}",
            "concept": "মূত্রে লবণের অতিপৃক্ততার কারণে কেলাসন ঘটে এবং ক্যালকুলাস বা পাথর তৈরি হয়।",
            "hack": "শব্দ তরঙ্গের মাধ্যমে পাথর গুঁড়ো করার অ-অস্ত্রোপচার পদ্ধতির নাম এক্সট্রাকর্পোরিয়াল শক ওয়েভ লিথোট্রিপসি (ESWL)!",
            "trap": "অক্সালেটযুক্ত খাবার (টমেটো, পালং শাক) অতিরিক্ত খেলে ক্যালসিয়াম অক্সালেট পাথরের ঝুঁকি বাড়ে।",
            "tags": ["kidney stone", "lithotripsy", "ক্যালসিয়াম অক্সালেট", "লিথোট্রিপসি"]
        },
        {
            "id": "v_bio_exc_08",
            "subject": "Biology",
            "chapter": "Human Physiology (Excretion)",
            "type": "core_formula",
            "title": "ডায়ালাইসিস ও হেমোডায়ালাইজার মেমব্রেন",
            "formula": "\\text{হেমোডায়ালাইসিস: কৃত্রিম ঝিল্লি (সেলোফেন পর্দা) দিয়ে রক্ত পরিশোধন}",
            "concept": "হেপারিন যোগ করে রক্ত জমাট বাঁধা রোধ করা হয় এবং ব্যাপন প্রক্রিয়ায় রক্ত থেকে ইউরিয়া ও বর্জ্য ডায়ালাইসেট তরলে আসে।",
            "hack": "পেরিটনিয়াল ডায়ালাইসিসে রোগীর নিজস্ব পেরিটোনিয়াম ঝিল্লিকে প্রাকৃতিক ফিল্টার হিসেবে ব্যবহার করা হয়!",
            "trap": "পরিশোধিত রক্ত পুনরায় রোগীর দেহে ফেরত পাঠানোর পূর্বে হেপারিন নিষ্ক্রিয় করতে প্রোটাামিন সালফেট মেশানো হয়।",
            "tags": ["dialysis", "hemodialysis", "ডায়ালাইসিস", "সেলোফেন"]
        }
    ])

    return entries


def get_english_entries():
    entries = []

    # 1. Appropriate Prepositions
    entries.extend([
        {
            "id": "v_eng_prep_01",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "core_formula",
            "title": "Die of vs Die from vs Die for vs Die by",
            "formula": "\\text{Die OF (রোগে)}, \\; \\text{Die FROM (ক্ষত/অতিরিক্ত পরিশ্রমে)}, \\; \\text{Die FOR (দেশের জন্য)}, \\; \\text{Die BY (বিষ বা আত্মহত্যাকালে)}",
            "concept": "ভর্তি পরীক্ষায় Die-এর বিভিন্ন Preposition সবচেয়ে বহুল জিজ্ঞাসিত প্রশ্ন।",
            "hack": "He died OF cholera (রোগ); died FROM overeating (অতিরিক্ত খাদ্য); died FOR his motherland (আত্মত্যাগ); died BY poison/hanging (বিষ/আত্মহত্যা)!",
            "trap": "রোগের ক্ষেত্রে 'die from' বা 'die by' ব্যবহার সম্পূর্ণ ভুল।",
            "tags": ["preposition", "die of", "die from", "die for"]
        },
        {
            "id": "v_eng_prep_02",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "core_formula",
            "title": "Blind to vs Blind of",
            "formula": "\\text{Blind TO (দোষের প্রতি অন্ধ)}, \\quad \\text{Blind OF/IN (চক্ষুহীনা/চোখে অন্ধ)}",
            "concept": "শারীরিক দৃষ্টিহীনতা বোঝাতে 'of/in' এবং মানসিক অন্ধত্ব বা সন্তানের দোষত্রুটি অগ্রাহ্য করা বোঝাতে 'to' বসে।",
            "hack": "He is blind OF one eye; but the father is blind TO his son's obvious faults!",
            "trap": "Blind to one's faults (দোষ দেখেও না দেখা); এখানে 'of' বসালে অর্থ সম্পূর্ণ ভুল হয়ে যাবে।",
            "tags": ["blind to", "blind of", "preposition"]
        },
        {
            "id": "v_eng_prep_03",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "core_formula",
            "title": "Angry with vs Angry at",
            "formula": "\\text{Angry WITH a person}, \\quad \\text{Angry AT conduct / behavior / thing}",
            "concept": "ব্যক্তির প্রতি ক্ষুব্ধ হলে 'with' এবং আচরণ বা ঘটনার ওপর ক্ষুব্ধ হলে 'at' বসে।",
            "hack": "I was angry WITH him (ব্যক্তি) AT his rude behavior (আচরণ)!",
            "trap": "ব্যক্তির ক্ষেত্রে 'angry at' ব্যবহার ভুল।",
            "tags": ["angry with", "angry at", "preposition"]
        },
        {
            "id": "v_eng_prep_04",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "shortcut",
            "title": "ল্যাটিন তুলনামূলক বিশেষণ (Junior/Superior TO)",
            "formula": "\\text{Junior, Senior, Superior, Inferior, Prior, Preferable } + \\text{TO (Never THAN)}",
            "concept": "যেসব ল্যাটিন বিশেষণের শেষে '-ior' থাকে তাদের পরে তুলনামূলকভাবে 'than' না বসে সর্বদা 'to' বসে।",
            "hack": "He is senior TO me (not than me); Health is preferable TO wealth!",
            "trap": "'Junior than' বা 'Senior than' ভর্তি পরীক্ষায় দেওয়া সবচেয়ে কমন ভুল অপশন।",
            "tags": ["latin comparatives", "preferable to", "junior to"]
        },
        {
            "id": "v_eng_prep_05",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "core_formula",
            "title": "Part from vs Part with",
            "formula": "\\text{Part FROM a person}, \\quad \\text{Part WITH a thing / possession}",
            "concept": "কোনো ব্যক্তির কাছ থেকে বিদায় নেওয়া বোঝাতে 'part from' এবং কোনো প্রিয় বস্তু ত্যাগ করা বোঝাতে 'part with' বসে।",
            "hack": "She wept to part FROM her sister; but she refused to part WITH her ancestral diamond ring!",
            "trap": "ব্যক্তির ক্ষেত্রে 'with' বা বস্তুর ক্ষেত্রে 'from' বসানো যাবে না।",
            "tags": ["part from", "part with", "preposition"]
        },
        {
            "id": "v_eng_prep_06",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "trap",
            "title": "Cope with (Cope up with সম্পূর্ণ ভুল!)",
            "formula": "\\text{Correct: COPE WITH} \\quad | \\quad \\text{Incorrect: Cope up with}",
            "concept": "প্রতিকূল পরিস্থিতির সাথে মানিয়ে চলা বা পেরে ওঠা বোঝাতে 'cope with' ব্যবহৃত হয়।",
            "hack": "It is difficult to COPE WITH rapid changes in modern medical science!",
            "trap": "বাংলাদেশে বহুল ব্যবহৃত 'cope up with' ব্যাকরণগতভাবে সম্পূর্ণ ভুল; পরীক্ষায় 'up' বাদ দিতে হবে।",
            "tags": ["cope with", "common error", "trap"]
        },
        {
            "id": "v_eng_prep_07",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "shortcut",
            "title": "Accused of vs Charged with",
            "formula": "\\text{Accused OF theft / murder}, \\quad \\text{Charged WITH theft / murder}",
            "concept": "উভয়ের অর্থ আদালতে অপরাধের দায়ে অভিযুক্ত করা।",
            "hack": "Accused OF <-> Charged WITH (জোড়া মনে রাখুন)!",
            "trap": "Accused-এর সাথে 'with' এবং Charged-এর সাথে 'of' মেলানো যাবে না।",
            "tags": ["accused of", "charged with", "preposition"]
        },
        {
            "id": "v_eng_prep_08",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "core_formula",
            "title": "Abide by vs Abide in/at",
            "formula": "\\text{Abide BY (নিয়ম মেনে চলা)}, \\quad \\text{Abide IN/AT (বসবাস করা)}",
            "concept": "Students must abide BY the university code of conduct.",
            "hack": "Abide by the rules / law (নিয়ম মেনে চলা)!",
            "trap": "মেনে চলার ক্ষেত্রে 'abide with' ভুল।",
            "tags": ["abide by", "preposition"]
        },
        {
            "id": "v_eng_prep_09",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "shortcut",
            "title": "Good at vs Weak in",
            "formula": "\\text{Good AT (কোনো বিষয়ে দক্ষ)}, \\quad \\text{Weak IN (কোনো বিষয়ে কাঁচা/দুর্বল)}",
            "concept": "She is remarkably good AT Organic Chemistry, but weak IN Higher Mathematics.",
            "hack": "দক্ষতা প্রকাশে 'Good at' (বা Bad at); বিষয়ে দুর্বলতায় 'Weak in'!",
            "trap": "'Good in English' বলা ভুল; সঠিক প্রয়োগ হলো 'Good at English'।",
            "tags": ["good at", "weak in", "preposition"]
        },
        {
            "id": "v_eng_prep_10",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "core_formula",
            "title": "Congratulate on (Never 'for')",
            "formula": "\\text{Congratulate someone ON success / winning}",
            "concept": "সাফল্যে অভিনন্দন জানাতে সর্বদা 'on' বসে।",
            "hack": "We congratulated Tahsin ON his admission into Dhaka Medical College!",
            "trap": "বাংলায় 'সাফল্যের জন্য' চিন্তা করে অনেকে 'for' বসায় যা মারাত্মক ভুল।",
            "tags": ["congratulate on", "preposition"]
        },
        {
            "id": "v_eng_prep_11",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "trap",
            "title": "Prefer to (Never 'than')",
            "formula": "\\text{Prefer A TO B} \\quad (A \\text{ এবং } B \\text{ উভয়ই Noun বা Gerund})",
            "concept": "দুটির মধ্যে একটিকে অধিক পছন্দ করা বোঝাতে 'prefer ... to' বসে।",
            "hack": "I prefer tea TO coffee; I prefer reading books TO watching television!",
            "trap": "'Prefer than' সম্পূর্ণ ব্যাকরণবিরুদ্ধ।",
            "tags": ["prefer to", "preposition", "trap"]
        },
        {
            "id": "v_eng_prep_12",
            "subject": "English",
            "chapter": "Appropriate Prepositions",
            "type": "shortcut",
            "title": "Prevent from vs Prohibit from + Gerund",
            "formula": "\\text{Prevent / Prohibit / Abstain / Refrain } + \\text{FROM} + \\text{V-ing}",
            "concept": "কোনো কাজ করা থেকে বিরত রাখা বা প্রতিহত করা বোঝাতে 'from' এর পর Gerund বসে।",
            "hack": "Rain prevented him FROM attending the clinical class!",
            "trap": "'Prevent to go' ভুল; সর্বদা 'from going' বসবে।",
            "tags": ["prevent from", "gerund", "preposition"]
        }
    ])

    # 2. Synonyms & Antonyms
    entries.extend([
        {
            "id": "v_eng_voc_01",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "core_formula",
            "title": "Lethal / Fatal (মারাত্মক / প্রাণঘাতী)",
            "formula": "\\text{Syn: Deadly, Mortal, Toxic, Virulent} \\quad | \\quad \\text{Ant: Harmless, Benign, Safe, Curative}",
            "concept": "চিকিৎসাবিজ্ঞানে প্রাণঘাতী রোগ বা বিষাক্ত মাত্রা বোঝাতে ব্যবহৃত হয়।",
            "hack": "Lethal dose (LD50) হলো নমুনার ৫০% প্রাণীর মৃত্যুর জন্য দায়ী মাত্রা!",
            "trap": "Lethal এবং Fatal সমার্থক; এর বিপরীত হলো Benign বা Harmless।",
            "tags": ["vocab", "lethal", "fatal", "synonym", "antonym"]
        },
        {
            "id": "v_eng_voc_02",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "core_formula",
            "title": "Benign vs Malignant (সৌম্য বনাম ক্যান্সারযুক্ত)",
            "formula": "\\text{Benign: Harmless, Mild, Non-cancerous} \\quad | \\quad \\text{Malignant: Cancerous, Virulent, Deadly}",
            "concept": "অনকোলজিতে টিউমারের প্রকৃতি বর্ণনায় বহুল ব্যবহৃত বিপরীতার্থক জোড়া।",
            "hack": "Benign টিউমার এক স্থানে সীমাবদ্ধ থাকে; Malignant টিউমার মেটাস্ট্যাসিস প্রক্রিয়ায় ছড়িয়ে পড়ে!",
            "trap": "Malignant এর সমার্থক Virulent, এবং বিপরীত Benign।",
            "tags": ["vocab", "benign", "malignant"]
        },
        {
            "id": "v_eng_voc_03",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "shortcut",
            "title": "Ephemeral (ক্ষণস্থায়ী)",
            "formula": "\\text{Syn: Transient, Fleeting, Evanescent, Short-lived} \\quad | \\quad \\text{Ant: Eternal, Perpetual, Permanent}",
            "concept": "খুব অল্প সময় স্থায়ী কোনো ঘটনা বা প্রতিক্রিয়া।",
            "hack": "Ephemeral fever = স্বল্পমেয়াদী ক্ষণস্থায়ী জ্বর!",
            "trap": "Permanent বা Perpetual হলো এর বিপরীত শব্দ।",
            "tags": ["vocab", "ephemeral", "transient"]
        },
        {
            "id": "v_eng_voc_04",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "shortcut",
            "title": "Gregarious (দলপ্রিয় / মিশুক)",
            "formula": "\\text{Syn: Sociable, Companionable, Outgoing} \\quad | \\quad \\text{Ant: Reclusive, Solitary, Antisocial, Hermit}",
            "concept": "অন্যের সঙ্গ পছন্দ করে এমন প্রাণী বা মানুষ।",
            "hack": "Honeybees and human beings are naturally gregarious creatures!",
            "trap": "Reclusive বা Solitary (একাকী থাকা পছন্দকারী) হলো এর সরাসরি বিপরীত।",
            "tags": ["vocab", "gregarious", "sociable"]
        },
        {
            "id": "v_eng_voc_05",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "core_formula",
            "title": "Lucid (স্পষ্ট / বোধগম্য)",
            "formula": "\\text{Syn: Clear, Coherent, Transparent, Intelligible} \\quad | \\quad \\text{Ant: Obscure, Vague, Ambiguous, Confusing}",
            "concept": "যা সহজে বোঝা যায় এবং চিন্তা-ভাবনায় পরিষ্কার।",
            "hack": "The physician gave a lucid explanation of the surgical procedure!",
            "trap": "Obscure বা Vague (অস্পষ্ট) হলো এর সাধারণ বিপরীত শব্দ।",
            "tags": ["vocab", "lucid", "clear"]
        },
        {
            "id": "v_eng_voc_06",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "shortcut",
            "title": "Novice (শিক্ষানবিস / অনভিজ্ঞ)",
            "formula": "\\text{Syn: Beginner, Neophyte, Tyro, Greenhorn} \\quad | \\quad \\text{Ant: Veteran, Expert, Master, Professional}",
            "concept": "কোনো পেশা বা বিদ্যায় যে একদম নতুন।",
            "hack": "Tyro ও Neophyte হলো Novice এর উচ্চমানের সমার্থক শব্দ!",
            "trap": "Veteran বা Expert হলো এর বিপরীত শব্দ।",
            "tags": ["vocab", "novice", "beginner", "tyro"]
        },
        {
            "id": "v_eng_voc_07",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "core_formula",
            "title": "Ubiquitous (সর্বব্যাপী)",
            "formula": "\\text{Syn: Omnipresent, Pervasive, Universal} \\quad | \\quad \\text{Ant: Rare, Scarce, Seldom, Infrequent}",
            "concept": "যা একই সাথে সর্বত্র উপস্থিত বা দৃশ্যমান।",
            "hack": "Microorganisms are ubiquitous in nature!",
            "trap": "Rare বা Scarce হলো এর সরাসরি বিপরীত।",
            "tags": ["vocab", "ubiquitous", "omnipresent"]
        },
        {
            "id": "v_eng_voc_08",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "shortcut",
            "title": "Resilient (স্থিতিস্থাপক / আঘাতসহনশীল)",
            "formula": "\\text{Syn: Adaptable, Tough, Buoyant, Flexible} \\quad | \\quad \\text{Ant: Fragile, Vulnerable, Brittle, Weak}",
            "concept": "কঠিন পরিস্থিতি বা আঘাতের পর দ্রুত স্বাভাবিক অবস্থায় ফিরে আসার ক্ষমতা।",
            "hack": "The human immune system is remarkably resilient against pathogens!",
            "trap": "Fragile বা Brittle (ভঙ্গুর) হলো এর বিপরীত শব্দ।",
            "tags": ["vocab", "resilient", "adaptable"]
        },
        {
            "id": "v_eng_voc_09",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "core_formula",
            "title": "Zenith vs Nadir (সর্বোচ্চ চূড়া বনাম সর্বনিম্ন তলানি)",
            "formula": "\\text{Zenith: Peak, Pinnacle, Apex, Acme, Climax} \\quad | \\quad \\text{Nadir: Bottom, Rock bottom, Lowest point}",
            "concept": "সাফল্যের সর্বোচ্চ শিখর ও পতনের সর্বনিম্ন নিম্নবিন্দু।",
            "hack": "Acme ও Pinnacle হলো Zenith এর সমার্থক; Nadir হলো বিপরীত!",
            "trap": "Nadir অর্থ সর্বনিম্ন তলানি, Zenith এর বিপরীত।",
            "tags": ["vocab", "zenith", "nadir", "apex"]
        },
        {
            "id": "v_eng_voc_10",
            "subject": "English",
            "chapter": "Synonyms & Antonyms",
            "type": "shortcut",
            "title": "Obliterate (সম্পূর্ণ ধ্বংস করা)",
            "formula": "\\text{Syn: Annihilate, Eradicate, Extirpate, Destroy} \\quad | \\quad \\text{Ant: Create, Construct, Preserve, Restore}",
            "concept": "কোনো কিছু সম্পূর্ণ মুছে ফেলা বা নিশ্চিহ্ন করা।",
            "hack": "Antibiotics help obliterate virulent bacterial colonies!",
            "trap": "Preserve (সংরক্ষণ করা) বা Construct (নির্মাণ করা) হলো এর বিপরীত।",
            "tags": ["vocab", "obliterate", "annihilate"]
        }
    ])

    return entries

def get_gk_entries():
    entries = []

    # 1. 1971 Liberation War Sector & Bir Sreshtho Matrix
    entries.extend([
        {
            "id": "v_gk_lib_01",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "core_formula",
            "title": "মুক্তিযুদ্ধের ১১টি সেক্টরের ভৌগোলিক মানচিত্র",
            "formula": "\\text{সেক্টর ১: চট্টগ্রাম ও ফেনী}; \\; \\text{সেক্টর ২: ঢাকা ও কুমিল্লা}; \\; \\text{সেক্টর ৩: সিলেট-হবিগঞ্জ}; \\; \\text{সেক্টর ৪: সিলেট পূর্ব}; \\; \\text{সেক্টর ৫: সুনামগঞ্জ}",
            "concept": "১১-১৭ জুলাই ১৯৭১ কলকাতায় অনুষ্ঠিত সেক্টর কমান্ডার্স সম্মেলনে সমগ্র বাংলাদেশকে ১১টি সেক্টরে এবং ৬৪টি সাব-সেক্টরে বিভক্ত করা হয়।",
            "hack": "সেক্টর ৬ (রংপুর-দিনাজপুর), সেক্টর ৭ (রাজশাহী-পাবনা), সেক্টর ৮ (কুষ্টিয়া-যশোর), সেক্টর ৯ (বরিশাল-পটুয়াখালী), সেক্টর ১০ (নৌ), সেক্টর ১১ (ময়মনসিংহ-টাঙ্গাইল)!",
            "trap": "ঢাকা শহর ও আশপাশের অঞ্চল ছিল ২নং সেক্টরের অধীনে (কমান্ডার: মেজর খালেদ মোশাররফ)।",
            "tags": ["liberation war", "11 sectors", "সেক্টর", "মুক্তিযুদ্ধ", "ঢাকা সেক্টর"]
        },
        {
            "id": "v_gk_lib_02",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "shortcut",
            "title": "সেক্টর ১০ এর ব্যতিক্রমী বৈশিষ্ট্য",
            "formula": "\\text{কোনো নিয়মিত সেক্টর কমান্ডার ছিলেন না; সরাসরি সি-ইন-সি এর অধীনে পরিচালিত}",
            "concept": "নৌ-কমান্ডোদের সমন্বয়ে গঠিত এই সেক্টরের অধীনে বিখ্যাত 'অপারেশন জ্যাকপট' (১৫ আগস্ট ১৯৭১) পরিচালিত হয়।",
            "hack": "সমগ্র বাংলাদেশের উপকূলীয় অঞ্চল ও নদীপথ ছিল ১০নং সেক্টরের অধীনে!",
            "trap": "১০নং সেক্টরে কোনো নির্দিষ্ট নিয়মিত কমান্ডার ছিলেন না; সরাসরি জেনারেল ওসমানীর নির্দেশে পরিচালিত হতো।",
            "tags": ["sector 10", "naval commando", "অপারেশন জ্যাকপট", "সেক্টর ১০"]
        },
        {
            "id": "v_gk_lib_03",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "shortcut",
            "title": "একমাত্র বিমানবাহিনী কর্মকর্তা সেক্টর কমান্ডার",
            "formula": "\\text{উইং কমান্ডার এম খাদেমুল বাশার (সেক্টর ৬: রংপুর ও দিনাজপুর)}",
            "concept": "৬নং সেক্টরের হেডকোয়ার্টার ছিল বাংলাদেশের ভূখণ্ডের ভেতরে বুড়িমারীতে।",
            "hack": "১১ জন সেক্টর কমান্ডারের মধ্যে একমাত্র বিমানবাহিনীর কর্মকর্তা ছিলেন এম খাদেমুল বাশার!",
            "trap": "বাকি অধিকাংশ সেক্টরের হেডকোয়ার্টার ছিল সীমান্ত পারের ভারতীয় ভূখণ্ডে।",
            "tags": ["sector 6", "Khademul Bashar", "বিমানবাহিনী", "সেক্টর ৬"]
        },
        {
            "id": "v_gk_lib_04",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "core_formula",
            "title": "তিনটি নিয়মিত ব্রিগেড ফোর্স (জেড, কে, এস)",
            "formula": "\\text{জেড ফোর্স: মেজর জিয়াউর রহমান; কে ফোর্স: মেজর খালেদ মোশাররফ; এস ফোর্স: মেজর কে এম শফিউল্লাহ}",
            "concept": "১৯৭১ সালের জুলাইয়ে প্রথম গঠিত নিয়মিত ব্রিগেড ছিল 'জেড ফোর্স'। পরবর্তীতে কে ফোর্স ও এস ফোর্স গঠিত হয়।",
            "hack": "অধিনায়কদের নামের আদ্যক্ষর (Z, K, S) দিয়েই ফোর্সগুলোর নামকরণ করা হয়!",
            "trap": "জেড ফোর্স গঠিত হয়েছিল ৮ম ইস্ট বেঙ্গল রেজিমেন্টকে কেন্দ্র করে।",
            "tags": ["Z force", "K force", "S force", "ব্রিগেড ফোর্স"]
        },
        {
            "id": "v_gk_lib_05",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "core_formula",
            "title": "৭ জন বীরশ্রেষ্ঠের বাহিনীভিত্তিক বিভাজন",
            "formula": "\\text{সেনাবাহিনী ৩ জন, ইপিআর ২ জন, নৌবাহিনী ১ জন, বিমানবাহিনী ১ জন (মোট ৭ জন)}",
            "concept": "বীরশ্রেষ্ঠ বাংলাদেশের সর্বোচ্চ বীরত্বসূচক সামরিক খেতাব।",
            "hack": "সেনা ৩ (জাহাঙ্গীর, মোস্তফা, হামিদুর); ইপিআর ২ (রউফ, নূর মোহাম্মদ); নৌ ১ (রুহুল আমিন); বিমান ১ (মতিউর রহমান)!",
            "trap": "পুলিশ বা আনসার বাহিনী থেকে কোনো বীরশ্রেষ্ঠ নেই; তবে খেতাবপ্রাপ্ত মুক্তিযোদ্ধা রয়েছেন।",
            "tags": ["7 Bir Sreshtho", "armed forces", "বীরশ্রেষ্ঠ", "বাহিনী বিভাজন"]
        },
        {
            "id": "v_gk_lib_06",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "shortcut",
            "title": "প্রথম ও সর্বশেষ শহীদ বীরশ্রেষ্ঠ",
            "formula": "\\text{সর্বপ্রথম: মুন্সী আব্দুর রউফ (৮ এপ্রিল ১৯৭১); সর্বশেষ: মহিউদ্দিন জাহাঙ্গীর (১৪ ডিসেম্বর ১৯৭১)}",
            "concept": "বীরশ্রেষ্ঠ মুন্সী আব্দুর রউফ রাঙামাটির নানিয়ারচরে এবং ক্যাপ্টেন মহিউদ্দিন জাহাঙ্গীর চাঁপাইনবাবগঞ্জে শহীদ হন।",
            "hack": "মহিউদ্দিন জাহাঙ্গীর শহীদ হন বিজয়ের মাত্র দু'দিন পূর্বে (১৪ ডিসেম্বর)! তাঁর সমাধি ছোট সোনা মসজিদ প্রাঙ্গণে।",
            "trap": "মতিউর রহমান ২০ আগস্ট এবং রুহুল আমিন ১০ ডিসেম্বর শহীদ হন।",
            "tags": ["first and last", "Bir Sreshtho", "শহীদ বীরশ্রেষ্ঠ"]
        },
        {
            "id": "v_gk_lib_07",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "core_formula",
            "title": "বীরশ্রেষ্ঠ ফ্লাইট লেফটেন্যান্ট মতিউর রহমান",
            "formula": "\\text{বিমানবাহিনী; টি-৩৩ ব্লু-বার্ড প্রশিক্ষণ বিমান; ২০ আগস্ট ১৯৭১; সমাধি: মিরপুর বুদ্ধিজীবী কবরস্থান}",
            "concept": "করাচির মৌরিপুর বিমানঘাঁটি থেকে বিমান ছিনতাই করে মুক্তিযুদ্ধে যোগ দিতে এসে ভারতীয় সীমান্তের কাছে থাট্টায় শহীদ হন।",
            "hack": "২০০৬ সালে পাকিস্তান থেকে তাঁর দেহাবশেষ বাংলাদেশে এনে রাষ্ট্রীয় মর্যাদায় মিরপুরে সমাহিত করা হয়!",
            "trap": "তিনি কোনো সেক্টরের নিয়মিত কমান্ডার ছিলেন না; পাকিস্তান বিমানঘাঁটি থেকে একক দুঃসাহসিক অভিযান চালান।",
            "tags": ["Matiur Rahman", "Air Force", "মতিউর রহমান", "টি-৩৩"]
        },
        {
            "id": "v_gk_lib_08",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "shortcut",
            "title": "বীরশ্রেষ্ঠ ইঞ্জিনরুম আর্টিফিসার মোহাম্মদ রুহুল আমিন",
            "formula": "\\text{নৌবাহিনী; গানবোট: বিএনএস পলাশ; ১০ ডিসেম্বর ১৯৭১; সমাধি: রূপসা নদী তীর, খুলনা}",
            "concept": "মোংলা বন্দর মুক্ত অভিযানে মিত্রবাহিনীর যুদ্ধবিমানের ভুল বোমা হামলায় বিএনএস পলাশ ক্ষতিগ্রস্ত হলে তিনি বীরত্বের সাথে শেষ মুহূর্ত পর্যন্ত যুদ্ধ করেন।",
            "hack": "নৌবাহিনীর একমাত্র বীরশ্রেষ্ঠ মোহাম্মদ রুহুল আমিন!",
            "trap": "তিনি সাঁতরে তীরে পৌঁছালে রাজাকাররা তাঁকে নির্মমভাবে বেয়নেট দিয়ে খুঁচিয়ে হত্যা করে।",
            "tags": ["Ruhul Amin", "Navy", "BNS Palash", "রুহুল আমিন", "বিএনএস পলাশ"]
        },
        {
            "id": "v_gk_lib_09",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "core_formula",
            "title": "সর্বকনিষ্ঠ বীরশ্রেষ্ঠ সিপাহী হামিদুর রহমান",
            "formula": "\\text{সেনাবাহিনী (১ম ইস্ট বেঙ্গল); মাত্র ১৮ বছর বয়স; শাহাদাত: ২৮ অক্টোবর ১৯৭১ (ধলাই সীমান্ত)}",
            "concept": "শ্রীমঙ্গলের ধলাই সীমান্তে পাকিস্তানি শত্রু বাংকারে গ্রেনেড ছুড়ে মেশিনগান স্তব্ধ করে দিয়ে বীরত্বের সাথে শহীদ হন।",
            "hack": "২০০৭ সালে ভারতের ত্রিপুরার আমবাসা থেকে তাঁর দেহাবশেষ এনে মিরপুর বুদ্ধিজীবী কবরস্থানে সমাহিত করা হয়!",
            "trap": "বীরশ্রেষ্ঠদের মধ্যে সর্বকনিষ্ঠ হলেন হামিদুর রহমান (মাত্র ১৮ বছর বয়সে শহীদ)।",
            "tags": ["Hamidur Rahman", "youngest", "হামিদুর রহমান", "সর্বকনিষ্ঠ বীরশ্রেষ্ঠ"]
        },
        {
            "id": "v_gk_lib_10",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "shortcut",
            "title": "৪টি রাষ্ট্রীয় বীরত্বসূচক খেতাব ও সংখ্যা",
            "formula": "\\text{বীরশ্রেষ্ঠ: ৭; বীরউত্তম: ৬৮; বীরবিক্রম: ১৭৫; বীরপ্রতীক: ৪২৬ (মোট = ৬৭৬ জন)}",
            "concept": "১৯৭৩ সালের ১৫ ডিসেম্বর সরকারি গেজেট বিজ্ঞপ্তির মাধ্যমে মুক্তিযোদ্ধাদের বীরত্বসূচক রাষ্ট্রীয় খেতাব প্রদান করা হয়।",
            "hack": "একমাত্র বিদেশি বীরপ্রতীক ডব্লিউ এ এস ওডারল্যান্ড (অস্ট্রেলিয়া)! নারী বীরপ্রতীক ২ জন: তারামন বিবি ও ডা. সেতারা বেগম!",
            "trap": "গেজেটভুক্ত মোট খেতাবপ্রাপ্ত মুক্তিযোদ্ধা ৬৭৬ জন (পরবর্তীতে কিছু রদবদল ছাড়া মূল সংখ্যা ৬৭৬)।",
            "tags": ["gallantry awards", "Bir Protik", "বীরউত্তম", "বীরপ্রতীক", "ওডারল্যান্ড"]
        },
        {
            "id": "v_gk_lib_11",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "core_formula",
            "title": "মুজিবনগর সরকার গঠন ও শপথ গ্রহণ",
            "formula": "\\text{গঠন: ১০ এপ্রিল ১৯৭১ (আগরতলা); শপথ: ১৭ এপ্রিল ১৯৭১ (মেহেরপুরের বৈদ্যনাথতলা)}",
            "concept": "স্বাধীন গণপ্রজাতন্ত্রী বাংলাদেশের প্রথম আইনসম্মত সাংবিধানিক সরকার।",
            "hack": "উপ-রাষ্ট্রপতি ও অস্থায়ী রাষ্ট্রপতি: সৈয়দ নজরুল ইসলাম; প্রধানমন্ত্রী: তাজউদ্দীন আহমদ; প্রধান সেনাপতি: এম এ জি ওসমানী!",
            "trap": "স্বাধীনতার ঘোষণাপত্র পাঠ করেন অধ্যাপক এম ইউসুফ আলী; গার্ড অব অনার দেন মাহবুবউদ্দিন আহমেদ বীরবিক্রম।",
            "tags": ["Mujibnagar government", "17 April", "মুজিবনগর সরকার", "তাজউদ্দীন আহমদ"]
        },
        {
            "id": "v_gk_lib_12",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "shortcut",
            "title": "বাংলাদেশ সংবিধানের মৌলিক কাঠামো ও অনুচ্ছেদ ৭(১)",
            "formula": "\\text{অনুচ্ছেদ ৭(১): প্রজাতন্ত্রের সকল ক্ষমতার মালিক জনগণ}",
            "concept": "সংবিধানের তৃতীয় ভাগে (অনুচ্ছেদ ২৭ থেকে ৪৪) মৌলিক অধিকার বর্ণিত হয়েছে। অনুচ্ছেদ ৭(১) অনুযায়ী সংবিধানই রাষ্ট্রের সর্বোচ্চ আইন।",
            "hack": "অনুচ্ছেদ ৭(১): ক্ষমতার মালিক জনগণ; অনুচ্ছেদ ২৭: আইনের দৃষ্টিতে সমতা; অনুচ্ছেদ ৩৬: চলাফেরার স্বাধীনতা; অনুচ্ছেদ ৩৯: চিন্তা ও বাক-স্বাধীনতা!",
            "trap": "মৌলিক রাষ্ট্রপরিচালনার নীতি (দ্বিতীয় ভাগ, অনুচ্ছেদ ৮-২৫) এবং মৌলিক অধিকার (তৃতীয় ভাগ, অনুচ্ছেদ ২৭-৪৪) গুলিয়ে ফেলা।",
            "tags": ["Constitution", "Article 7(1)", "Fundamental Rights", "সংবিধান", "মৌলিক অধিকার"]
        },
        {
            "id": "v_gk_lib_13",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "core_formula",
            "title": "অপারেশন সার্চলাইট ও ২৫শে মার্চ গণহত্যা",
            "formula": "\\text{২৫শে মার্চ রাত ১১:৩০ মিনিট থেকে শুরু হওয়া পাকিস্তানি সামরিক গণহত্যা}",
            "concept": "পরিকল্পনাকারী: লেফটেন্যান্ট জেনারেল টিক্কা খান ও মেজর জেনারেল রাও ফরমান আলী। মূল নিশানা ছিল ঢাকা বিশ্ববিদ্যালয় ও রাজারবাগ।",
            "hack": "২৬শে মার্চ প্রথম প্রহরে রাত ১২:২০ মিনিটে ইপিআর-এর ওয়্যারলেসের মাধ্যমে স্বাধীনতার ঘোষণা দেশজুড়ে সম্প্রচার করা হয়!",
            "trap": "জাতীয় গণহত্যা দিবস পালিত হয় ২৫শে মার্চ।",
            "tags": ["Operation Searchlight", "genocide", "অপারেশন সার্চলাইট", "গণহত্যা দিবস"]
        },
        {
            "id": "v_gk_lib_14",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "shortcut",
            "title": "কনসার্ট ফর বাংলাদেশ (Concert for Bangladesh)",
            "formula": "\\text{১ আগস্ট ১৯৭১; ম্যাডিসন স্কয়ার গার্ডেন, নিউ ইয়র্ক; উদ্যোক্তা: জর্জ হ্যারিসন ও পণ্ডিত রবি শঙ্কর}",
            "concept": "মুক্তিযুদ্ধের সমর্থনে তহবিল ও আন্তর্জাতিক জনমত গঠনের জন্য প্রথম বৈশ্বিক চ্যারিটি কনসার্ট।",
            "hack": "অংশগ্রহণকারী বিখ্যাত শিল্পী: বব ডিলান, এরিক ক্ল্যাপটন, রিঙ্গো স্টার; হ্যারিসনের গান: 'Bangla Desh'!",
            "trap": "কনসার্ট অনুষ্ঠিত হয়েছিল নিউ ইয়র্কে, লন্ডনে নয়।",
            "tags": ["Concert for Bangladesh", "George Harrison", "কনসার্ট ফর বাংলাদেশ", "জর্জ হ্যারিসন"]
        },
        {
            "id": "v_gk_lib_15",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "trap",
            "title": "বাংলাদেশকে প্রথম স্বীকৃতি প্রদানকারী দেশ",
            "formula": "\\text{ভুটান (৬ ডিসেম্বর ১৯৭১ সকালে); ভারত (৬ ডিসেম্বর ১৯৭১ দুপুরে)}",
            "concept": "উভয় দেশই ৬ ডিসেম্বর ১৯৭১ স্বীকৃতি দেয়; তবে সময়ের বিচারে ভুটান ভারতের কয়েক ঘণ্টা পূর্বে তারবার্তা পাঠায়।",
            "hack": "প্রথম স্বীকৃতিদাতা ভুটান; দ্বিতীয় ভারত; আরব দেশের মধ্যে প্রথম ইরাক (৮ জুলাই ১৯৭২)!",
            "trap": "পরীক্ষায় ভুটান ও ভারত দুটিই অপশনে থাকলে ভুটান দাগাতে হবে (পররাষ্ট্র মন্ত্রণালয়ের আনুষ্ঠানিক ঘোষণা মতে)।",
            "tags": ["first recognition", "Bhutan", "India", "স্বীকৃতি প্রদানকারী দেশ", "ভুটান", "trap"]
        },
        {
            "id": "v_gk_lib_16",
            "subject": "GK",
            "chapter": "1971 Liberation War & Bir Sreshtho Matrix",
            "type": "core_formula",
            "title": "১৬ই ডিসেম্বর ঐতিহাসিক আত্মসমর্পণ দলিল",
            "formula": "\\text{রেসকোর্স ময়দানে ৯৩,০০০ সৈন্য নিয়ে লে. জেনারেল এ এ কে নিয়াজীর আত্মসমর্পণ}",
            "concept": "যৌথবাহিনীর পক্ষে দলিল গ্রহণ করেন লে. জেনারেল জগজিৎ সিং অরোরা। সময় বিকেল ৪:৩১ মিনিট।",
            "hack": "আত্মসমর্পণ টেবিলটি বর্তমানে বাংলাদেশ জাতীয় জাদুঘরে সংরক্ষিত রয়েছে!",
            "trap": "আত্মসমর্পণ অনুষ্ঠানে মুক্তিবাহিনী প্রধান জেনারেল এম এ জি ওসমানী উপস্থিত থাকতে পারেননি; উপস্থিত ছিলেন গ্রুপ ক্যাপ্টেন এ কে খন্দকার।",
            "tags": ["surrender document", "16 December", "আত্মসমর্পণ", "বিজয় দিবস", "নিয়াজী"]
        }
    ])

    return entries
