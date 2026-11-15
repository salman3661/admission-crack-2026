#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""curate_math_p1.py - Curated with DU Most Repeated & Speed-Hacks"""

true = True
false = False
null = None

def get_part1_chapters():
    return [
    {
        "chapter_id": "math_1st_01",
        "chapter_title": "ম্যাট্রিক্স ও নির্ণায়ক (Matrices & Determinants)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০১",
        "predictors": [
            {
                "id": "pred_math_1st_01_01",
                "stem": "$A = \\begin{pmatrix} k - 2 & 4 \\\\ 3 & k + 2 \\end{pmatrix}$ ম্যাট্রিক্সটি ব্যতিক্রমী (Singular) হলে $k$ এর মান কত?",
                "options": [
                    "$\\pm 4$",
                    "$\\pm 2$",
                    "$16$",
                    "$\\pm \\sqrt{10}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ব্যতিক্রমী ম্যাট্রিক্সের শর্ত ও অজ্ঞাত রাশির মান (DU Repeated)",
                "trap_alert": "কোণাকুণি বিয়োগে চিহ্নের ভুল করে $k^2 + 4$ ভাবা। $(k-2)(k+2) = k^2 - 4$!",
                "speed_hack": "ব্যতিক্রমী হলে $|A| = 0 \\implies (k-2)(k+2) - 12 = 0 \\implies k^2 - 16 = 0 \\implies k = \\pm 4$। ৩ সেকেন্ডে নির্ণয়!",
                "explanation": "ব্যতিক্রমী ম্যাট্রিক্সের নির্ণায়ক শূন্য: $|A| = (k-2)(k+2) - (3)(4) = k^2 - 4 - 12 = k^2 - 16 = 0 \\implies k = \\pm 4$。",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_02",
                "stem": "$A = \\begin{pmatrix} 3 & 5 \\\\ 1 & 2 \\end{pmatrix}$ হলে $A^{-1}$ ম্যাট্রিক্সটি কোনটি?",
                "options": [
                    "$\\begin{pmatrix} 2 & -5 \\\\ -1 & 3 \\end{pmatrix}$",
                    "$\\begin{pmatrix} -2 & 5 \\\\ 1 & -3 \\end{pmatrix}$",
                    "$\\begin{pmatrix} 3 & -5 \\\\ -1 & 2 \\end{pmatrix}$",
                    "$\\begin{pmatrix} 2 & 5 \\\\ 1 & 3 \\end{pmatrix}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বিপরীত ম্যাট্রিক্স নির্ণয় ($2 \\times 2$ ফাস্ট ট্রিক)",
                "trap_alert": "নির্ণায়কের মান $6 - 5 = 1$ হলেও চিহ্নের পরিবর্তনের নিয়ম ভুল করা।",
                "speed_hack": "২×২ শর্টকাট: প্রধান কর্ণের স্থান বদল ($3 \\leftrightarrow 2$) এবং গৌণ কর্ণের চিহ্ন বদল ($-5, -1$), তারপর $|A| = 1$ দিয়ে ভাগ!",
                "explanation": "$A^{-1} = \\frac{1}{ad-bc}\\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix} = \\frac{1}{6-5}\\begin{pmatrix} 2 & -5 \\\\ -1 & 3 \\end{pmatrix} = \\begin{pmatrix} 2 & -5 \\\\ -1 & 3 \\end{pmatrix}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_03",
                "stem": "যদি $A$ ম্যাট্রিক্সের ক্রম $3 \\times 4$, $B$ ম্যাট্রিক্সের ক্রম $4 \\times 3$ এবং $C$ ম্যাট্রিক্সের ক্রম $3 \\times 2$ হয়, তবে $(A^T + B) \\times C$ ম্যাট্রিক্সের আকার (Order) কত?",
                "options": [
                    "$4 \\times 2$",
                    "$3 \\times 2$",
                    "$4 \\times 3$",
                    "$3 \\times 4$"
                ],
                "answer": "A",
                "type_ref": "Type 3: ম্যাট্রিক্সের গুণন ও মাত্রার শর্ত (DU Speed-Hack)",
                "trap_alert": "যোগের জন্য আকার অভিন্ন হতে হয়। $A$ এর আকার $3 \\times 4$ হলে $A^T$ হয় $4 \\times 3$!",
                "speed_hack": "ডাইমেনশন রুল: $A$ এর আকার $3 \\times 4 \\implies A^T$ হয় $4 \\times 3$। তাই $(A^T + B)$ হলো $4 \\times 3$। এবার $(A^T + B)_{4 \\times 3} \\times C_{3 \\times 2} = 4 \\times 2$! মান হিসাব ছাড়াই সরাসরি নির্ণয়!",
                "explanation": "যোগফল $(A^T + B)$ এর ক্রম $4 \\times 3$ এবং $C$ এর ক্রম $3 \\times 2$। গুণফলের ক্রম হবে $4 \\times 2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_04",
                "stem": "একটি $3 \\times 3$ ক্রমের বর্গ ম্যাট্রিক্স $A$ এর নির্ণায়ক $|A| = 5$ হলে $|2A|$ এর মান কত?",
                "options": [
                    "$40$",
                    "$10$",
                    "$30$",
                    "$20$"
                ],
                "answer": "A",
                "type_ref": "Type 3: নির্ণায়কের ধর্মাবলী ও স্কেলার গুণিতক",
                "trap_alert": "সরাসরি $2 \\times 5 = 10$ দাগানো! $n$ মাত্রার জন্য স্কেলার গুণিতক $k^n$ আকারে বের হয়।",
                "speed_hack": "শর্টকাট: $|kA| = k^n |A|$। এখানে $n = 3$, তাই $|2A| = 2^3 \\times 5 = 8 \\times 5 = 40$।",
                "explanation": "$3 \\times 3$ ম্যাট্রিক্সের ৩টি সারি থেকেই ২ সাধারণ নেওয়া যায়, ফলে $|2A| = 2^3 |A| = 8 \\times 5 = 40$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_05",
                "stem": "$\\begin{vmatrix} 1 & a & b+c \\\\ 1 & b & c+a \\\\ 1 & c & a+b \\end{vmatrix}$ নির্ণায়কটির মান কত?",
                "options": [
                    "$0$",
                    "$a+b+c$",
                    "$1$",
                    "$(a-b)(b-c)(c-a)$"
                ],
                "answer": "A",
                "type_ref": "Type 3: নির্ণায়কের ধর্মাবলী ও $|A|=0$ ট্রিক (DU Speed-Hack)",
                "trap_alert": "বড় উৎপাদক বিশ্লেষণ করতে যাওয়া। ২য় ও ৩য় কলাম যোগ করলেই মান শূন্য!",
                "speed_hack": "নির্ণায়কের ধর্মাবলী ও $|A|=0$ ট্রিক: $C_3' = C_2 + C_3$ করলে ৩য় কলামে $(a+b+c)$ কমন এসে ১ম ও ৩য় কলাম অভিন্ন ($1, 1, 1$) হয়ে যায়, ফলে বিস্তার ছাড়াই মান $0$!",
                "explanation": "দুটি কলাম বা সারি অভিন্ন হলে নির্ণায়কের মান সর্বদা শূন্য হয়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_06",
                "stem": "$A$ একটি প্রতিসম (Symmetric) ম্যাট্রিক্স হলে নিচের কোনটি সর্বদা সঠিক?",
                "options": [
                    "$A^T = A$",
                    "$A^T = -A$",
                    "$A^2 = A$",
                    "$A^{-1} = A$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বিশেষ ধরনের ম্যাট্রিক্স",
                "trap_alert": "বক্র-প্রতিসম ($A^T = -A$) এর সাথে প্রতিসমের সংজ্ঞা গুলিয়ে ফেলা।",
                "speed_hack": "প্রতিসম $\\implies A^T = A$; বক্র-প্রতিসম (Skew-Symmetric) $\\implies A^T = -A$ এবং এর প্রধান কর্ণের ভুক্তিগুলো শূন্য।",
                "explanation": "কোনো ম্যাট্রিক্সকে ট্রান্সপোজ করলে মূল ম্যাট্রিক্স ফিরে এলে তাকে প্রতিসম ম্যাট্রিক্স বলে।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_07",
                "stem": "$A = \\begin{pmatrix} 2 & 0 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 5 \\end{pmatrix}$ হলে $A^{-1}$ ম্যাট্রিক্সটি কোনটি?",
                "options": [
                    "$\\begin{pmatrix} 1/2 & 0 & 0 \\\\ 0 & 1/3 & 0 \\\\ 0 & 0 & 1/5 \\end{pmatrix}$",
                    "$\\begin{pmatrix} 5 & 0 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 2 \\end{pmatrix}$",
                    "$\\frac{1}{30}\\begin{pmatrix} 2 & 0 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 5 \\end{pmatrix}$",
                    "$\\begin{pmatrix} -2 & 0 & 0 \\\\ 0 & -3 & 0 \\\\ 0 & 0 & -5 \\end{pmatrix}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বিপরীত ম্যাট্রিক্স",
                "trap_alert": "কর্ণ ম্যাট্রিক্সের ক্ষেত্রে বড় অ্যাডজয়েন্ট ম্যাট্রিক্স বের করতে গিয়ে সময় নষ্ট করা।",
                "speed_hack": "কর্ণ ম্যাট্রিক্স $\\text{diag}(a, b, c)$ এর বিপরীত ম্যাট্রিক্স হলো কর্ণের ভুক্তিগুলোর উল্টো মান $\\text{diag}(1/a, 1/b, 1/c)$।",
                "explanation": "কর্ণ ম্যাট্রিক্সের জন্য $A^{-1}$ সরাসরি প্রতিটি কর্ণের ভুক্তির গুণাত্মক বিপরীত $1/a_{ii}$ নিয়ে গঠিত।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_08",
                "stem": "$A$ একটি $3 \\times 3$ বর্গ ম্যাট্রিক্স এবং $|A| = 4$ হলে $|\\text{adj}(A)|$ এর মান কত?",
                "options": [
                    "$16$",
                    "$4$",
                    "$64$",
                    "$8$"
                ],
                "answer": "A",
                "type_ref": "Type 2: অ্যাডজয়েন্ট ম্যাট্রিক্সের ধর্ম",
                "trap_alert": "সূত্রে ভুল করে $|A|^n = 4^3 = 64$ দাগানো। সূত্র হলো $|\\text{adj}(A)| = |A|^{n-1}$!",
                "speed_hack": "$|\\text{adj}(A)| = |A|^{n-1}$। এখানে $n=3$, তাই $|\\text{adj}(A)| = 4^{3-1} = 4^2 = 16$।",
                "explanation": "যে কোনো $n \\times n$ ম্যাট্রিক্সের জন্য $|\\text{adj}(A)| = |A|^{n-1}$। এখানে $4^{3-1} = 16$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_09",
                "stem": "ক্র্যামারের নিয়মে সমীকরণ জোট সমাধানের ক্ষেত্রে যদি $D = 0$ কিন্তু অন্তত একটি $D_x, D_y, D_z \\ne 0$ হয়, তবে সমীকরণ জোটের:",
                "options": [
                    "কোনো সমাধান থাকবে না (অসামঞ্জস্য)",
                    "একটি অনন্য সমাধান থাকবে",
                    "অসংখ্য সমাধান থাকবে",
                    "সর্বদা শূন্য সমাধান থাকবে"
                ],
                "answer": "A",
                "type_ref": "Type 3: ক্র্যামারের নিয়ম ও সমাধানের শর্ত",
                "trap_alert": "অসংখ্য সমাধানের সাথে কোনো সমাধান না থাকার শর্ত গুলিয়ে ফেলা।",
                "speed_hack": "$D \\ne 0 \\implies$ অনন্য সমাধান; $D = D_x = D_y = D_z = 0 \\implies$ অসংখ্য সমাধান; $D = 0$ কিন্তু কোনো $D_i \\ne 0 \\implies$ কোনো সমাধান নেই।",
                "explanation": "হরে শূন্য এবং লবে অশূন্য সংখ্যা এলে মান অসংজ্ঞায়িত হয়, অর্থাৎ কোনো বাস্তব সমাধান নেই।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_10",
                "stem": "$A = \\begin{pmatrix} 1 & 2 & 3 \\\\ 0 & 4 & 5 \\\\ 0 & 0 & 6 \\end{pmatrix}$ ম্যাট্রিক্সটির ট্রেস (Trace) কত?",
                "options": [
                    "$11$",
                    "$24$",
                    "$6$",
                    "$18$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ম্যাট্রিক্সের ট্রেস ও নির্ণায়ক",
                "trap_alert": "ট্রেস বের করতে গিয়ে গুণ করে ফেলা ($1 \\times 4 \\times 6 = 24$ হলো নির্ণায়ক, ট্রেস নয়!)।",
                "speed_hack": "ট্রেস = প্রধান কর্ণের ভুক্তিগুলোর যোগফল $= 1 + 4 + 6 = 11$।",
                "explanation": "ম্যাট্রিক্সের ট্রেস $\\text{Tr}(A) = a_{11} + a_{22} + a_{33} = 1 + 4 + 6 = 11$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_11",
                "stem": "$A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}$ হলে $A + A^T$ ম্যাট্রিক্সটি কোন প্রকৃতির?",
                "options": [
                    "প্রতিসম ম্যাট্রিক্স",
                    "বক্র-প্রতিসম ম্যাট্রিক্স",
                    "শূন্য ম্যাট্রিক্স",
                    "অভেদক ম্যাট্রিক্স"
                ],
                "answer": "A",
                "type_ref": "Type 1: প্রতিসম ও বক্র-প্রতিসম ম্যাট্রিক্স",
                "trap_alert": "$A - A^T$ হলো বক্র-প্রতিসম, কিন্তু $A + A^T$ সর্বদা প্রতিসম!",
                "speed_hack": "যেকোনো বর্গ ম্যাট্রিক্স $A$ এর জন্য $(A + A^T)^T = A^T + A = A + A^T$, তাই এটি সর্বদা প্রতিসম।",
                "explanation": "বর্গ ম্যাট্রিক্স $A$ এর ক্ষেত্রে $A + A^T$ সর্বদা প্রতিসম এবং $A - A^T$ সর্বদা বক্র-প্রতিসম।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_12",
                "stem": "$A = \\begin{pmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{pmatrix}$ হলে $|A|$ এর মান কত?",
                "options": [
                    "$1$",
                    "$0$",
                    "$\\cos 2\\theta$",
                    "$-1$"
                ],
                "answer": "A",
                "type_ref": "Type 1: লম্ব ম্যাট্রিক্স ও নির্ণায়ক",
                "trap_alert": "কোণাকুণি গুণ করার সময় চিহ্নের গোলমাল করে $\\cos^2\\theta - \\sin^2\\theta = \\cos 2\\theta$ দাগানো।",
                "speed_hack": "$|A| = \\cos^2\\theta - (-\\sin^2\\theta) = \\cos^2\\theta + \\sin^2\\theta = 1$। এটি একটি লম্ব (Orthogonal) ম্যাট্রিক্স।",
                "explanation": "নির্ণায়ক $|A| = \\cos\\theta \\cdot \\cos\\theta - (-\\sin\\theta \\cdot \\sin\\theta) = \\cos^2\\theta + \\sin^2\\theta = 1$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_13",
                "stem": "$A = \\begin{pmatrix} 2 & 1 \\\\ 3 & 4 \\end{pmatrix}$ এবং $B = \\begin{pmatrix} 1 & 0 \\\\ 0 & 2 \\end{pmatrix}$ হলে $AB$ ম্যাট্রিক্সের মান কত?",
                "options": [
                    "$\\begin{pmatrix} 2 & 2 \\\\ 3 & 8 \\end{pmatrix}$",
                    "$\\begin{pmatrix} 2 & 0 \\\\ 0 & 8 \\end{pmatrix}$",
                    "$\\begin{pmatrix} 3 & 1 \\\\ 3 & 6 \\end{pmatrix}$",
                    "$\\begin{pmatrix} 2 & 1 \\\\ 6 & 8 \\end{pmatrix}$"
                ],
                "answer": "A",
                "type_ref": "Type 3: ম্যাট্রিক্স গুণন",
                "trap_alert": "অনুরূপ ভুক্তি সরাসরি গুণ করে $\\begin{pmatrix} 2 & 0 \\\\ 0 & 8 \\end{pmatrix}$ ভাবা। ম্যাট্রিক্স গুণন সারি $\\times$ কলামে হয়!",
                "speed_hack": "১ম সারি $\\times$ কলাম: $2(1)+1(0)=2, 2(0)+1(2)=2$; ২য় সারি: $3(1)+4(0)=3, 3(0)+4(2)=8$।",
                "explanation": "সারি ও কলামের উপাদান গুণ করে যোগ করলে পাওয়া যায় $\\begin{pmatrix} 2 & 2 \\\\ 3 & 8 \\end{pmatrix}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_14",
                "stem": "$\\begin{vmatrix} 1 & \\omega & \\omega^2 \\\\ \\omega & \\omega^2 & 1 \\\\ \\omega^2 & 1 & \\omega \\end{vmatrix}$ নির্ণায়কটির মান কত? (যেখানে $\\omega$ এককের কাল্পনিক ঘনমূল)",
                "options": [
                    "$0$",
                    "$1$",
                    "$\\omega$",
                    "$-1$"
                ],
                "answer": "A",
                "type_ref": "Type 3: নির্ণায়কের বৈশিষ্ট্য ও জটিল সংখ্যা",
                "trap_alert": "বিস্তার করতে গিয়ে সময় নষ্ট করা। $1 + \\omega + \\omega^2 = 0$ মনে রাখুন!",
                "speed_hack": "$C_1' = C_1 + C_2 + C_3$ করলে ১ম কলামের প্রতিটি ভুক্তি $1 + \\omega + \\omega^2 = 0$ হয়ে যায় $\\implies$ মান $0$।",
                "explanation": "১ম কলামের সব ভুক্তির মান শূন্য হওয়ায় সম্পূর্ণ নির্ণায়কের মান শূন্য।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_15",
                "stem": "যদি $A^2 - 5A + 6I = 0$ হয়, তবে $A^{-1}$ সমান কোনটি?",
                "options": [
                    "$\\frac{1}{6}(5I - A)$",
                    "$\\frac{1}{6}(A - 5I)$",
                    "$5I - A$",
                    "$\\frac{1}{5}(6I - A)$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ক্যালি-হ্যামিল্টন ও ইনভার্স ম্যাট্রিক্স",
                "trap_alert": "উভয় পাশে $A^{-1}$ গুণ করার পর চিহ্নে ভুল করা। $6I = 5A - A^2 \\implies 6A^{-1} = 5I - A$!",
                "speed_hack": "$A^2 - 5A + 6I = 0 \\implies 6I = 5A - A^2 \\implies 6A^{-1} = 5I - A \\implies A^{-1} = \\frac{1}{6}(5I - A)$।",
                "explanation": "সমীকরণের উভয়পাশে $A^{-1}$ দ্বারা গুণ করলে $A - 5I + 6A^{-1} = 0 \\implies A^{-1} = \\frac{1}{6}(5I - A)$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_16",
                "stem": "একটি ৩য় ক্রমের ত্রিভুজাকার (Triangular) ম্যাট্রিক্সের প্রধান কর্ণের ভুক্তিগুলো $2, -3, 4$ হলে তার নির্ণায়কের মান কত?",
                "options": [
                    "$-24$",
                    "$3$",
                    "$24$",
                    "$0$"
                ],
                "answer": "A",
                "type_ref": "Type 3: ত্রিভুজাকার ম্যাট্রিক্সের নির্ণায়ক",
                "trap_alert": "কর্ণের নিচের ভুক্তি শূন্য হলেও সাধারণ বিস্তারের পেছনে অযথা সময় দেওয়া।",
                "speed_hack": "যেকোনো ঊর্ধ্ব বা নিম্ন ত্রিভুজাকার ম্যাট্রিক্সের নির্ণায়ক = প্রধান কর্ণের উপাদানগুলোর গুণফল $= 2 \\times (-3) \\times 4 = -24$।",
                "explanation": "ত্রিভুজাকার ম্যাট্রিক্সের নির্ণায়কের মান সর্বদা প্রধান কর্ণের ভুক্তিগুলোর গুণফলের সমান।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_17",
                "stem": "যদি $A$ একটি $n \\times n$ ইনভার্টিবল ম্যাট্রিক্স হয়, তবে $|A^{-1}|$ এর মান নিচের কোনটির সমান?",
                "options": [
                    "$\\frac{1}{|A|}$",
                    "$|A|$",
                    "$-|A|$",
                    "$|A|^n$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বিপরীত ম্যাট্রিক্সের নির্ণায়ক",
                "trap_alert": "$|A^{-1}| = -|A|$ ভাবা। এটি গুণাত্মক বিপরীত, যোগাত্মক নয়!",
                "speed_hack": "$A A^{-1} = I \\implies |A| |A^{-1}| = |I| = 1 \\implies |A^{-1}| = \\frac{1}{|A|}$।",
                "explanation": "ম্যাট্রিক্সের গুণের নির্ণায়ক সূত্রানুসারে $|A A^{-1}| = |A||A^{-1}| = 1 \\implies |A^{-1}| = 1/|A|$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_18",
                "stem": "$A = \\begin{pmatrix} 0 & 2 \\\\ -2 & 0 \\end{pmatrix}$ ম্যাট্রিক্সটি কোন প্রকৃতির?",
                "options": [
                    "বক্র-প্রতিসম ম্যাট্রিক্স",
                    "প্রতিসম ম্যাট্রিক্স",
                    "অভেদক ম্যাট্রিক্স",
                    "ব্যতিক্রমী ম্যাট্রিক্স"
                ],
                "answer": "A",
                "type_ref": "Type 1: বিশেষ ধরনের ম্যাট্রিক্স",
                "trap_alert": "প্রধান কর্ণ শূন্য হলেও ট্রান্সপোজের চিহ্ন পরিবর্তন খেয়াল না করা।",
                "speed_hack": "$A^T = \\begin{pmatrix} 0 & -2 \\\\ 2 & 0 \\end{pmatrix} = -A$, এবং প্রধান কর্ণের ভুক্তি শূন্য $\\implies$ বক্র-প্রতিসম (Skew-Symmetric)।",
                "explanation": "$A^T = -A$ এবং প্রধান কর্ণের ভুক্তি শূন্য হওয়ায় এটি একটি বক্র-প্রতিসম ম্যাট্রিক্স।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_19",
                "stem": "$\\begin{vmatrix} 1 & 1 & 1 \\\\ a & b & c \\\\ a^2 & b^2 & c^2 \\end{vmatrix}$ ভ্যান্ডারমন্ড (Vandermonde) নির্ণায়কটির মান কত?",
                "options": [
                    "$(a-b)(b-c)(c-a)$",
                    "$(a+b)(b+c)(c+a)$",
                    "$(b-a)(c-b)(a-c)$",
                    "$a^2 + b^2 + c^2$"
                ],
                "answer": "A",
                "type_ref": "Type 3: স্ট্যান্ডার্ড চক্র-ক্রমিক নির্ণায়ক",
                "trap_alert": "চিহ্নের দিক বদলে $(b-a)(c-b)(a-c) = -(a-b)(b-c)(c-a)$ এর সাথে প্যাঁচ লাগানো।",
                "speed_hack": "স্ট্যান্ডার্ড সাইক্লিক ফলাফল: $(a-b)(b-c)(c-a)$। মান বসিয়ে যাচাই: $a=1, b=2, c=3$ বসালে মান $-2$।",
                "explanation": "এটি ভ্যান্ডারমন্ড নির্ণায়ক যার বিস্তার $(a-b)(b-c)(c-a)$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_01_20",
                "stem": "যদি কোনো ম্যাট্রিক্স $A$ এর জন্য $A^2 = A$ হয়, তবে ম্যাট্রিক্সটিকে কী বলা হয়?",
                "options": [
                    "সমঘাতি (Idempotent)",
                    "শূন্যঘাতি (Nilpotent)",
                    "অভেদঘাতি (Involutory)",
                    "লম্ব (Orthogonal)"
                ],
                "answer": "A",
                "type_ref": "Type 1: বিশেষ ধরনের ম্যাট্রিক্সের সংজ্ঞা",
                "trap_alert": "$A^2 = I$ হলো অভেদঘাতি, আর $A^2 = A$ হলো সমঘাতি!",
                "speed_hack": "$A^2 = A \\implies$ সমঘাতি (Idempotent); $A^2 = I \\implies$ অভেদঘাতি (Involutory); $A^k = 0 \\implies$ শূন্যঘাতি (Nilpotent)।",
                "explanation": "যে ম্যাট্রিক্সের বর্গ করলে মূল ম্যাট্রিক্সের সমান হয় তাকে সমঘাতি (Idempotent) ম্যাট্রিক্স বলে।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    },
    {
        "chapter_id": "math_1st_02",
        "chapter_title": "ভেক্টর (Vectors)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০২",
        "predictors": [
            {
                "id": "pred_math_1st_02_01",
                "stem": "$\\vec{A} = 2\\hat{i} + 3\\hat{j} - \\hat{k}$ এবং $\\vec{B} = m\\hat{i} - 2\\hat{j} + 4\\hat{k}$ ভেক্টরদ্বয় পরস্পর লম্ব হলে $m$ এর মান কত?",
                "options": [
                    "$5$",
                    "$3$",
                    "$-5$",
                    "$2$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ডট গুণন ও লম্ব হওয়ার শর্ত",
                "trap_alert": "ডট গুণনে $-4$ ও $-\\hat{k}$ গুণ করার সময় চিহ্নের ভুল করে $+4$ ভাবা।",
                "speed_hack": "লম্ব $\\implies \\vec{A} \\cdot \\vec{B} = 0 \\implies 2m - 6 - 4 = 0 \\implies 2m = 10 \\implies m = 5$।",
                "explanation": "ভেক্টরদ্বয় পরস্পর লম্ব হলে ডট গুণন শূন্য: $2(m) + 3(-2) + (-1)(4) = 0 \\implies 2m - 10 = 0 \\implies m = 5$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_02",
                "stem": "$\\vec{P} = 2\\hat{i} - 3\\hat{j} + 6\\hat{k}$ ভেক্টরের সমান্তরাল একক ভেক্টর কোনটি?",
                "options": [
                    "$\\frac{1}{7}(2\\hat{i} - 3\\hat{j} + 6\\hat{k})$",
                    "$\\frac{1}{49}(2\\hat{i} - 3\\hat{j} + 6\\hat{k})$",
                    "$\\frac{1}{\\sqrt{7}}(2\\hat{i} - 3\\hat{j} + 6\\hat{k})$",
                    "$\\frac{1}{5}(2\\hat{i} - 3\\hat{j} + 6\\hat{k})$"
                ],
                "answer": "A",
                "type_ref": "Type 1: একক ভেক্টর নির্ণয়",
                "trap_alert": "বর্গমূল না করে হরে মান $49$ বসিয়ে ভুল অপশন দাগানো।",
                "speed_hack": "মান $|\\vec{P}| = \\sqrt{2^2 + (-3)^2 + 6^2} = \\sqrt{4 + 9 + 36} = \\sqrt{49} = 7$। একক ভেক্টর $\\frac{\\vec{P}}{|\\vec{P}|}$।",
                "explanation": "সমান্তরাল একক ভেক্টর $\\hat{u} = \\frac{\\vec{P}}{|\\vec{P}|} = \\frac{2\\hat{i}-3\\hat{j}+6\\hat{k}}{7}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_03",
                "stem": "$\\vec{A} = 2\\hat{i} - \\hat{j} + \\hat{k}$ ভেক্টরের ওপর $\\vec{B} = \\hat{i} - 2\\hat{j} + \\hat{k}$ ভেক্টরের স্কেলার অভিক্ষেপ (Scalar Projection) কত?",
                "options": [
                    "$\\frac{5}{\\sqrt{6}}$",
                    "$\\frac{5}{6}$",
                    "$\\frac{\\sqrt{6}}{5}$",
                    "$\\frac{4}{\\sqrt{6}}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ভেক্টরের স্কেলার অভিক্ষেপ (DU Speed-Hack)",
                "trap_alert": "যার ওপর অভিক্ষেপ তার মান দিয়ে ভাগ করতে হবে, অর্থাৎ $|\u000bec{A}|$ দ্বারা ভাগ।",
                "speed_hack": "স্কেলার অভিক্ষেপ শর্টকাট: $X$ এর ওপর $Y$ এর অভিক্ষেপ = $\\frac{X \\cdot Y}{|X|}$। এখানে $\\vec{A} \\cdot \\vec{B} = 2(1) + (-1)(-2) + 1(1) = 5$ এবং $|\\vec{A}| = \\sqrt{4+1+1} = \\sqrt{6}$। তাই মান $\\frac{5}{\\sqrt{6}}$!",
                "explanation": "$\\vec{A}$ এর ওপর $\\vec{B}$ এর স্কেলার অভিক্ষেপ $= \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{A}|} = \\frac{5}{\\sqrt{6}}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_04",
                "stem": "$\\vec{A} = 2\\hat{i} + 4\\hat{j} - 5\\hat{k}$ এবং $\\vec{B} = \\hat{i} + 2\\hat{j} + m\\hat{k}$ ভেক্টর দুটি সমান্তরাল হলে $m$ এর মান কত?",
                "options": [
                    "$-\\frac{5}{2}$",
                    "$\\frac{5}{2}$",
                    "$-5$",
                    "$\\frac{2}{5}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সমান্তরাল ভেক্টরের শর্ত",
                "trap_alert": "অনুপাত নেওয়ার সময় চিহ্নের মাইনাস ছেড়ে দেওয়া।",
                "speed_hack": "সমান্তরাল হলে সহগগুলোর অনুপাত সমান: $\\frac{2}{1} = \\frac{4}{2} = \\frac{-5}{m} \\implies 2 = \\frac{-5}{m} \\implies m = -\\frac{5}{2}$।",
                "explanation": "ভেক্টরদ্বয় সমান্তরাল হলে $\\frac{A_x}{B_x} = \\frac{A_y}{B_y} = \\frac{A_z}{B_z} \\implies 2 = \\frac{-5}{m} \\implies m = -\\frac{5}{2}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_05",
                "stem": "একটি সামান্তরিকের দুটি সন্নিহিত বাহু $\\vec{a} = 3\\hat{i} + \\hat{j} - 2\\hat{k}$ এবং $\\vec{b} = \\hat{i} - 3\\hat{j} + 4\\hat{k}$ হলে তার ক্ষেত্রফল কত বর্গ একক?",
                "options": [
                    "$10\\sqrt{3}$",
                    "$5\\sqrt{3}$",
                    "$300$",
                    "$20$"
                ],
                "answer": "A",
                "type_ref": "Type 2: ক্রস গুণন ও জ্যামিতিক ক্ষেত্রফল",
                "trap_alert": "কর্ণ দেওয়া থাকলে $\\frac{1}{2}|\\vec{d}_1 \\times \\vec{d}_2|$, কিন্তু সন্নিহিত বাহু দেওয়া থাকলে সরাসরি $|\\vec{a} \\times \\vec{b}|$!",
                "speed_hack": "$\\vec{a} \\times \\vec{b} = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ 3 & 1 & -2 \\\\ 1 & -3 & 4 \\end{vmatrix} = -2\\hat{i} - 14\\hat{j} - 10\\hat{k}$। মান $= \\sqrt{4 + 196 + 100} = \\sqrt{300} = 10\\sqrt{3}$।",
                "explanation": "সামান্তরিকের ক্ষেত্রফল $= |\\vec{a} \\times \\vec{b}| = \\sqrt{(-2)^2 + (-14)^2 + (-10)^2} = \\sqrt{300} = 10\\sqrt{3}$ বর্গ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_06",
                "stem": "$\\vec{A} = 2\\hat{i} + \\hat{j} - \\hat{k}$, $\\vec{B} = 3\\hat{i} - 2\\hat{j} + 4\\hat{k}$ এবং $\\vec{C} = \\hat{i} - 3\\hat{j} + a\\hat{k}$ ভেক্টর তিনটি সমতলীয় (Coplanar) হলে $a$ এর মান কত?",
                "options": [
                    "$5$",
                    "$3$",
                    "$-5$",
                    "$7$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সমতলীয় ভেক্টর ও রৈখিক নির্ভরশীলতা (DU Speed-Hack)",
                "trap_alert": "৩য় ক্রমের নির্ণায়ক বিস্তার না করে লিনিয়ার ডিপেনডেন্স লক্ষ্য করুন!",
                "speed_hack": "সমতলীয় ভেক্টর শর্টকাট: নির্ণায়ক $= 0$ অথবা রৈখিক নির্ভরশীলতা পরীক্ষণ! লক্ষ্য করুন $\\vec{C} = \\vec{B} - \\vec{A} \\implies 3-2 = 1, -2-1 = -3$, তাই $a = 4 - (-1) = 5$! নির্ণায়ক না ভেঙেই ৩ সেকেন্ডে মুখে মুখে সমাধান!",
                "explanation": "ভেক্টরত্রয় সমতলীয় হলে তাদের গঠিত নির্ণায়ক শূন্য হয়। অথবা $\\vec{C} = \\vec{B} - \\vec{A}$ হওয়ায় $a = 4 - (-1) = 5$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_07",
                "stem": "$|\\vec{A} + \\vec{B}| = |\\vec{A} - \\vec{B}|$ হলে $\\vec{A}$ ও $\\vec{B}$ এর মধ্যবর্তী কোণ কত?",
                "options": [
                    "$90^\\circ$",
                    "$0^\\circ$",
                    "$60^\\circ$",
                    "$180^\\circ$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ভেক্টরের মধ্যবর্তী কোণ",
                "trap_alert": "উভয় পাশে বর্গ না করে শুধু মান সমান ভেবে $0^\\circ$ দাগানো।",
                "speed_hack": "বর্গ করলে: $A^2 + B^2 + 2\\vec{A}\\cdot\\vec{B} = A^2 + B^2 - 2\\vec{A}\\cdot\\vec{B} \\implies 4\\vec{A}\\cdot\\vec{B} = 0 \\implies \\vec{A} \\perp \\vec{B}$ (কোণ $90^\\circ$)।",
                "explanation": "$|\\vec{A}+\\vec{B}|^2 = |\\vec{A}-\\vec{B}|^2 \\implies 4\\vec{A}\\cdot\\vec{B} = 0 \\implies \\cos\\theta = 0 \\implies \\theta = 90^\\circ$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_08",
                "stem": "$\\vec{A} = 2\\hat{i} + 2\\hat{j} - \\hat{k}$ ভেক্টরটি $x$-অক্ষের সাথে কত কোণ উৎপন্ন করে?",
                "options": [
                    "$\\cos^{-1}(2/3)$",
                    "$\\cos^{-1}(1/3)$",
                    "$\\sin^{-1}(2/3)$",
                    "$\\cos^{-1}(2/9)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: দিক কোসাইন (Direction Cosines)",
                "trap_alert": "ভেক্টরের মান হিসাব করতে গিয়ে বর্গমূল ভুল করে ৯ দিয়ে ভাগ করা।",
                "speed_hack": "দিক কোসাইন: $\\cos\\alpha = \\frac{A_x}{|\\vec{A}|} = \\frac{2}{\\sqrt{4+4+1}} = \\frac{2}{3} \\implies \\alpha = \\cos^{-1}(2/3)$।",
                "explanation": "$x$-অক্ষের সাথে উৎপন্ন কোণ $\\alpha$ হলে $\\cos\\alpha = \\frac{A_x}{|\\vec{A}|} = \\frac{2}{\\sqrt{4+4+1}} = \\frac{2}{3}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_09",
                "stem": "কোনো সমতলে অবস্থিত দুটি ভেক্টর $\\vec{A}$ ও $\\vec{B}$ এর উভয়ের ওপর লম্ব একক ভেক্টর কোনটি?",
                "options": [
                    "$\\pm \\frac{\\vec{A} \\times \\vec{B}}{|\\vec{A} \\times \\vec{B}|}$",
                    "$\\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{A} \\cdot \\vec{B}|}$",
                    "$\\pm \\frac{\\vec{A} + \\vec{B}}{|\\vec{A} + \\vec{B}|}$",
                    "$\\frac{\\vec{A} - \\vec{B}}{|\\vec{A} \\times \\vec{B}|}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: লম্ব একক ভেক্টর",
                "trap_alert": "উভয় দিক হতে পারে বলে $\\pm$ চিহ্ন খেয়াল না করা।",
                "speed_hack": "ক্রস গুণনের দিক সর্বদা উভয় ভেক্টরের সমতলের ওপর লম্ব। একক ভেক্টরের জন্য মান দিয়ে ভাগ এবং উভয় পাশের জন্য $\\pm$।",
                "explanation": "দুটি ভেক্টরের উভয়ের ওপর লম্ব একক ভেক্টর $\\hat{\\eta} = \\pm \\frac{\\vec{A} \\times \\vec{B}}{|\\vec{A} \\times \\vec{B}|}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_10",
                "stem": "যদি $|\\vec{A} \\times \\vec{B}| = \\sqrt{3}(\\vec{A} \\cdot \\vec{B})$ হয়, তবে ভেক্টরদ্বয়ের মধ্যবর্তী কোণ $\\theta$ কত?",
                "options": [
                    "$60^\\circ$",
                    "$30^\\circ$",
                    "$45^\\circ$",
                    "$90^\\circ$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ডট ও ক্রস গুণনের সম্পর্ক",
                "trap_alert": "$\\tan\\theta = \\sqrt{3}$ কে ভুল করে $30^\\circ$ ভাবা। $\\tan 60^\\circ = \\sqrt{3}$!",
                "speed_hack": "$AB\\sin\\theta = \\sqrt{3} AB\\cos\\theta \\implies \\tan\\theta = \\sqrt{3} \\implies \\theta = 60^\\circ$। ৩ সেকেন্ডে সমাধান!",
                "explanation": "$\\frac{|\\vec{A} \\times \\vec{B}|}{\\vec{A} \\cdot \\vec{B}} = \\tan\\theta = \\sqrt{3} \\implies \\theta = 60^\\circ$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_11",
                "stem": "একটি সামান্তরিকের কর্ণদ্বয় যথাক্রমে $\\vec{d}_1 = 2\\hat{i} + 4\\hat{j} - 4\\hat{k}$ এবং $\\vec{d}_2 = 4\\hat{i} - 2\\hat{j} - 2\\hat{k}$ হলে তার ক্ষেত্রফল কত?",
                "options": [
                    "$10\\sqrt{2}$",
                    "$20\\sqrt{2}$",
                    "$12$",
                    "$18$"
                ],
                "answer": "A",
                "type_ref": "Type 2: কর্ণ দ্বারা সামান্তরিকের ক্ষেত্রফল",
                "trap_alert": "কর্ণের ক্ষেত্রফলে হাফ ($1/2$) গুণ করতে ভুলে যাওয়া!",
                "speed_hack": "কর্ণদ্বয় থাকলে ক্ষেত্রফল $= \\frac{1}{2}|\\vec{d}_1 \\times \\vec{d}_2|$। $\\vec{d}_1 \\times \\vec{d}_2 = -16\\hat{i} - 12\\hat{j} - 20\\hat{k}$। মান $= \\sqrt{256+144+400} = \\sqrt{800} = 20\\sqrt{2}$। হাফ গুণ করলে $10\\sqrt{2}$।",
                "explanation": "কর্ণ দেওয়া থাকলে সামান্তরিকের ক্ষেত্রফল $= \\frac{1}{2}|\\vec{d}_1 \\times \\vec{d}_2| = \\frac{1}{2}(20\\sqrt{2}) = 10\\sqrt{2}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_12",
                "stem": "$\\hat{i} \\cdot (\\hat{j} \\times \\hat{k}) + \\hat{j} \\cdot (\\hat{i} \\times \\hat{k}) + \\hat{k} \\cdot (\\hat{i} \\times \\hat{j})$ এর মান কত?",
                "options": [
                    "$1$",
                    "$3$",
                    "$0$",
                    "$-1$"
                ],
                "answer": "A",
                "type_ref": "Type 2: স্কেলার ট্রিপল প্রোডাক্ট ও একক ভেক্টর",
                "trap_alert": "ঘড়ির কাঁটার বিপরীত নিয়ম না মানলে মাঝের রাশিতে চিহ্নের গোলমাল হবে: $\\hat{i} \\times \\hat{k} = -\\hat{j}$!",
                "speed_hack": "১ম পদ: $\\hat{i}\\cdot\\hat{i} = 1$; ২য় পদ: $\\hat{j}\\cdot(-\\hat{j}) = -1$; ৩য় পদ: $\\hat{k}\\cdot\\hat{k} = 1$। মোট $= 1 - 1 + 1 = 1$।",
                "explanation": "$\\hat{j} \\times \\hat{k} = \\hat{i}$, $\\hat{i} \\times \\hat{k} = -\\hat{j}$, $\\hat{i} \\times \\hat{j} = \\hat{k}$। সুতরাং $1 + (-1) + 1 = 1$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_13",
                "stem": "কোনো কণার ওপর $\\vec{F} = 3\\hat{i} + 2\\hat{j} - 4\\hat{k}$ বল প্রয়োগে কণাটির সরণ $\\vec{r} = 2\\hat{i} - 3\\hat{j} + \\hat{k}$ হলে কৃতকাজের পরিমাণ কত একক?",
                "options": [
                    "$-4$",
                    "$4$",
                    "$16$",
                    "$0$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বল ও সরণের ডট গুণন দ্বারা কাজ",
                "trap_alert": "ঋণাত্মক চিহ্ন বাদ দিয়ে সরাসরি পরমমান দাগানো। কাজ একটি স্কেলার রাশি এবং এটি ঋণাত্মক হতে পারে!",
                "speed_hack": "$W = \\vec{F} \\cdot \\vec{r} = 3(2) + 2(-3) + (-4)(1) = 6 - 6 - 4 = -4$ একক।",
                "explanation": "কাজ $W = \\vec{F}\\cdot\\vec{r} = 6 - 6 - 4 = -4$ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_14",
                "stem": "বিন্দু $O$ এর সাপেক্ষে $\\vec{r} = 2\\hat{i} - \\hat{j} + 3\\hat{k}$ বিন্দুতে ক্রিয়াশীল বল $\\vec{F} = 3\\hat{i} + 4\\hat{j} - 2\\hat{k}$ হলে বলের ভ্রামক (Torque) এর সঠিক ভেক্টর রাশি কোনটি?",
                "options": [
                    "$\\vec{\\tau} = \\vec{r} \\times \\vec{F}$",
                    "$\\vec{\\tau} = \\vec{F} \\cdot \\vec{r}$",
                    "$\\vec{\\tau} = \\vec{F} \\times \\vec{r}$",
                    "$\\vec{\\tau} = |\\vec{F}| |\\vec{r}|$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বলের ভ্রামক ও ক্রস গুণন",
                "trap_alert": "বলের ভ্রামক স্কেলার ডট গুণন নয়, এটি ভেক্টর ক্রস গুণন $\\vec{\\tau} = \\vec{r} \\times \\vec{F}$!",
                "speed_hack": "ভ্রামক (Torque) একটি ভেক্টর রাশি যা ব্যাসার্ধ ভেক্টর ও বল ভেক্টরের ক্রস গুণফল দ্বারা সংজ্ঞায়িত হয়।",
                "explanation": "ঘূর্ণন অক্ষের সাপেক্ষে বলের ভ্রামক $\\vec{\\tau} = \\vec{r} \\times \\vec{F}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_15",
                "stem": "$\\triangle ABC$-এর $BC$ বাহুর মধ্যবিন্দু $D$ হলে নিচের কোন ভেক্টর সম্পর্কটি সর্বদা সঠিক?",
                "options": [
                    "$\\vec{AB} + \\vec{AC} = 2\\vec{AD}$",
                    "$\\vec{AB} + \\vec{AC} = \\vec{AD}$",
                    "$\\vec{AB} - \\vec{AC} = 2\\vec{AD}$",
                    "$\\vec{AB} + \\vec{AD} = 2\\vec{AC}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ভেক্টর ত্রিভুজ সূত্র ও মধ্যবিন্দু উপপাদ্য (DU Written & MCQ)",
                "trap_alert": "চিহ্নে ভুল করে মাইনাস দাগানো। সাধারণ শীর্ষবিন্দু থেকে দুই বাহুর যোগফল মধ্যমার দ্বিগুণ!",
                "speed_hack": "ভেক্টর ত্রিভুজ মধ্যমা শর্টকাট (Midpoint Theorem): $\\vec{AB} = \\vec{AD} + \\vec{DB}$ এবং $\\vec{AC} = \\vec{AD} + \\vec{DC}$। যেহেতু $D$ মধ্যবিন্দু $\\implies \\vec{DB} + \\vec{DC} = \\vec{0}$, তাই $\\vec{AB} + \\vec{AC} = 2\\vec{AD}$!",
                "explanation": "ত্রিভুজের যে কোনো শীর্ষ থেকে অঙ্কিত দুই বাহুর ভেক্টর সমষ্টি ঐ শীর্ষগামী মধ্যমা ভেক্টরের দ্বিগুণের সমান।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_16",
                "stem": "ভেক্টর ত্রয় $\\vec{a}, \\vec{b}, \\vec{c}$ দ্বারা গঠিত একটি সামান্তরিকীয় ঘনবস্তুর আয়তন কত?",
                "options": [
                    "$|\\vec{a} \\cdot (\\vec{b} \\times \\vec{c})|$",
                    "$\\frac{1}{6}|\\vec{a} \\cdot (\\vec{b} \\times \\vec{c})|$",
                    "$\\frac{1}{2}|\\vec{a} \\times \\vec{b}|$",
                    "$|\\vec{a} \\times \\vec{b} \\times \\vec{c}|$"
                ],
                "answer": "A",
                "type_ref": "Type 2: স্কেলার ট্রিপল প্রোডাক্ট ও আয়তন",
                "trap_alert": "চতুস্তলকের (Tetrahedron) আয়তন $\\frac{1}{6}$ কিন্তু সামান্তরিকীয় ঘনবস্তুর আয়তন সরাসরি স্কেলার ট্রিপল প্রোডাক্ট!",
                "speed_hack": "সামান্তরিকীয় ঘনবস্তু $\\implies [\\vec{a} \\ \\vec{b} \\ \\vec{c}]$; চতুস্তলক (Tetrahedron) $\\implies \\frac{1}{6}[\\vec{a} \\ \\vec{b} \\ \\vec{c}]$।",
                "explanation": "ভূমি সামান্তরিকের ক্ষেত্রফল $|\\vec{b} \\times \\vec{c}|$ এবং উচ্চতা সহ আয়তন $= |\\vec{a} \\cdot (\\vec{b} \\times \\vec{c})|$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_17",
                "stem": "$\\vec{B} = 2\\hat{i} - 2\\hat{j} + \\hat{k}$ এর দিকে $\\vec{A} = 3\\hat{i} + \\hat{j} - \\hat{k}$ ভেক্টরের ভেক্টর উপাংশ (Vector Component) কোনটি?",
                "options": [
                    "$\\frac{1}{3}(2\\hat{i} - 2\\hat{j} + \\hat{k})$",
                    "$\\frac{1}{9}(2\\hat{i} - 2\\hat{j} + \\hat{k})$",
                    "$2\\hat{i} - 2\\hat{j} + \\hat{k}$",
                    "$\\frac{1}{3}(3\\hat{i} + \\hat{j} - \\hat{k})$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ভেক্টর উপাংশ ও অভিক্ষেপ (DU Speed-Hack)",
                "trap_alert": "স্কেলার অভিক্ষেপ আর ভেক্টর উপাংশের পার্থক্য না বোঝা। উপাংশ হলো অভিক্ষেপের সাথে একক ভেক্টরের গুণফল!",
                "speed_hack": "ভেক্টর উপাংশ ফর্মুলা: $\\left(\\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{B}|^2}\\right)\\vec{B} = \\left(\\frac{6 - 2 - 1}{4 + 4 + 1}\\right)\\vec{B} = \\frac{3}{9}\\vec{B} = \\frac{1}{3}(2\\hat{i} - 2\\hat{j} + \\hat{k})$!",
                "explanation": "$\\vec{B}$ বরাবর $\\vec{A}$ এর উপাংশ $= \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{B}|^2}\\vec{B} = \\frac{3}{9}\\vec{B} = \\frac{1}{3}(2\\hat{i} - 2\\hat{j} + \\hat{k})$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_02_18",
                "stem": "কোনো ভেক্টর $\\vec{r}$ এর দিক কোসাইনসমূহ $l, m, n$ হলে নিচের কোনটি সঠিক?",
                "options": [
                    "$l^2 + m^2 + n^2 = 1$",
                    "$l^2 + m^2 + n^2 = 0$",
                    "$l + m + n = 1$",
                    "$l^2 + m^2 - n^2 = 1$"
                ],
                "answer": "A",
                "type_ref": "Type 1: দিক কোসাইন সংক্রান্ত উপপাদ্য",
                "trap_alert": "বর্গ না করে সরাসরি যোগফল ১ ভাবা।",
                "speed_hack": "দিক কোসাইনগুলোর বর্গের যোগফল সর্বদা ১: $\\cos^2\\alpha + \\cos^2\\beta + \\cos^2\\gamma = 1$।",
                "explanation": "$l^2 + m^2 + n^2 = \\frac{x^2+y^2+z^2}{r^2} = \\frac{r^2}{r^2} = 1$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    },
    {
        "chapter_id": "math_1st_03",
        "chapter_title": "সরলরেখা (Straight Lines)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০৩",
        "predictors": [
            {
                "id": "pred_math_1st_03_01",
                "stem": "$3x + 4y - 7 = 0$ এবং $6x + 8y + 16 = 0$ সমান্তরাল রেখাদ্বয়ের মধ্যবর্তী দূরত্ব কত একক?",
                "options": [
                    "$3$",
                    "$2.3$",
                    "$1.5$",
                    "$4.6$"
                ],
                "answer": "A",
                "type_ref": "Type 3: সমান্তরাল সরলরেখাদ্বয়ের মধ্যবর্তী দূরত্ব",
                "trap_alert": "২য় সমীকরণকে ২ দিয়ে ভাগ না করে সরাসরি ধ্রুবক বিয়োগ করা ($16 - (-7) = 23$)।",
                "speed_hack": "২য় রেখাকে ২ দিয়ে ভাগ করুন: $3x + 4y + 8 = 0$। দূরত্ব $= \\frac{|8 - (-7)|}{\\sqrt{3^2 + 4^2}} = \\frac{15}{5} = 3$ একক। ৩ সেকেন্ডে সমাধান!",
                "explanation": "সহগ সমান করে $d = \\frac{|c_1 - c_2|}{\\sqrt{a^2 + b^2}} = \\frac{|8 - (-7)|}{5} = 3$ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_02",
                "stem": "$4x + 3y - 24 = 0$ সরলরেখাটি অক্ষদ্বয়ের সাথে যে ত্রিভুজ গঠন করে তার ক্ষেত্রফল কত বর্গ একক?",
                "options": [
                    "$24$",
                    "$48$",
                    "$12$",
                    "$36$"
                ],
                "answer": "A",
                "type_ref": "Type 1: সরলরেখার ছেদাংশ ও ত্রিভুজের ক্ষেত্রফল",
                "trap_alert": "ছেদাংশ দ্বয় গুণ করে হাফ করতে ভুলে যাওয়া।",
                "speed_hack": "শর্টকাট: ক্ষেত্রফল $= \\frac{c^2}{2|ab|} = \\frac{24^2}{2 \\times 4 \\times 3} = \\frac{576}{24} = 24$ বর্গ একক।",
                "explanation": "$x$-ছেদাংশ $a = 24/4 = 6$, $y$-ছেদাংশ $b = 24/3 = 8$। ক্ষেত্রফল $= \\frac{1}{2} \\times 6 \\times 8 = 24$ বর্গ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_03",
                "stem": "$(2, -3)$ বিন্দু হতে $5x - 12y + 6 = 0$ সরলরেখার লম্ব দূরত্ব কত একক?",
                "options": [
                    "$4$",
                    "$3$",
                    "$5$",
                    "$2$"
                ],
                "answer": "A",
                "type_ref": "Type 3: বিন্দু হতে রেখার লম্ব দূরত্ব",
                "trap_alert": "হরে পিথাগোরাস ট্রিপলেট $(5, 12, 13)$ এর বর্গমূল না নিয়ে সরাসরি হিসাব করা।",
                "speed_hack": "লবে মান বসান: $|5(2) - 12(-3) + 6| = |10 + 36 + 6| = 52$। হরে $\\sqrt{25 + 144} = 13$। দূরত্ব $= 52/13 = 4$ একক।",
                "explanation": "লম্ব দূরত্ব $d = \\frac{|ax_1 + by_1 + c|}{\\sqrt{a^2 + b^2}} = \\frac{|10 + 36 + 6|}{13} = \\frac{52}{13} = 4$ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_04",
                "stem": "$2x - 3y + 5 = 0$ রেখার ওপর লম্ব এবং $(1, 2)$ বিন্দুগামী সরলরেখার সমীকরণ কোনটি?",
                "options": [
                    "$3x + 2y - 7 = 0$",
                    "$3x - 2y + 1 = 0$",
                    "$2x + 3y - 8 = 0$",
                    "$3x + 2y + 7 = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 2: লম্ব রেখার সমীকরণ ও ঢাল ইনভার্সন (DU Speed-Hack)",
                "trap_alert": "সহগ বদল ও মাঝের চিহ্ন পরিবর্তনের সময় ভুল চিহ্নে মাইনাস দেওয়া।",
                "speed_hack": "লম্ব রেখার ঢাল ইনভার্সন: $m_1 = \\frac{2}{3} \\implies m_2 = -\\frac{3}{2}$। সমীকরণ: $3x + 2y - (3(1) + 2(2)) = 3x + 2y - 7 = 0$। ৩ সেকেন্ডে সমাধান!",
                "explanation": "$ax + by + c = 0$ এর লম্ব রেখা $bx - ay + k = 0$। এখানে $3x + 2y + k = 0$। $(1, 2)$ বসালে $k = -7$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_05",
                "stem": "পোলার স্থানাঙ্ক $(r, \\theta) = (3, 150^\\circ)$ এর কার্তেসীয় স্থানাঙ্ক $(x, y)$ কোনটি?",
                "options": [
                    "$(-\\frac{3\\sqrt{3}}{2}, \\frac{3}{2})$",
                    "$(\\frac{3\\sqrt{3}}{2}, \\frac{3}{2})$",
                    "$(-\\frac{3\\sqrt{3}}{2}, -\\frac{3}{2})$",
                    "$(\\frac{3}{2}, -\\frac{3\\sqrt{3}}{2})$"
                ],
                "answer": "A",
                "type_ref": "Type 1: পোলার স্থানাঙ্ক ও চতুর্ভাগ এলিমিনেশন (DU Speed-Hack)",
                "trap_alert": "ক্যালকুলেটরে মান না বের করে সরাসরি চতুর্ভাগ চিহ্নের ট্রিক ব্যবহার করুন!",
                "speed_hack": "চতুর্ভাগ ও চিহ্নের ট্রিক: $\\theta = 150^\\circ$ ২য় চতুর্ভাগে অবস্থিত, যেখানে $x < 0$ এবং $y > 0$। অপশন দেখেই একমাত্র A-তে $x$ ঋণাত্মক ও $y$ ধনাত্মক! ক্যালকুলেটর ছাড়াই ১ সেকেন্ডে নিশ্চিত উত্তর!",
                "explanation": "$x = 3\\cos 150^\\circ = 3(-\\sqrt{3}/2) = -\\frac{3\\sqrt{3}}{2}$, $y = 3\\sin 150^\\circ = 3(1/2) = \\frac{3}{2}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_06",
                "stem": "$A(1, 4)$ এবং $B(9, -12)$ বিন্দুদ্বয়ের সংযোগ রেখাংশকে $X$-অক্ষ কোন অনুপাতে বিভক্ত করে?",
                "options": [
                    "$1 : 3$ অন্তর্বিভক্ত",
                    "$1 : 3$ বহির্বিভক্ত",
                    "$3 : 1$ অন্তর্বিভক্ত",
                    "$2 : 3$ অন্তর্বিভক্ত"
                ],
                "answer": "A",
                "type_ref": "Type 1: রেখাংশের অনুপাত স্টেপ-কাউন্টিং (DU Speed-Hack)",
                "trap_alert": "চিহ্ন বিপরীত হলে সর্বদা অন্তর্বিভক্ত হয়; একই চিহ্ন হলে বহির্বিভক্ত হয়।",
                "speed_hack": "স্টেপ-কাউন্টিং অনুপাত ট্রিক: $X$-অক্ষ বিভক্ত করলে অনুপাত $k = |y_1| : |y_2| = 4 : 12 = 1 : 3$। কোটিদ্বয়ের চিহ্ন বিপরীত হওয়ায় সরাসরি অন্তর্বিভক্ত! কোনো সূত্র বা ক্যালকুলেশন ছাড়াই ২ সেকেন্ডে!",
                "explanation": "$X$-অক্ষ দ্বারা বিভাজন অনুপাত $m_1 : m_2 = -y_1 : y_2 = -4 : (-12) = 1 : 3$ (ধনাত্মক মান হওয়ায় অন্তর্বিভক্ত)।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_07",
                "stem": "$kx - 2y + 1 = 0$ এবং $6x - 4y + 5 = 0$ রেখাদ্বয় পরস্পর সমান্তরাল হলে $k$ এর মান কত?",
                "options": [
                    "$3$",
                    "$-3$",
                    "$6$",
                    "$12$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সমান্তরাল সরলরেখার শর্ত",
                "trap_alert": "ঢাল দুটি সমান না করে উল্টো গুণ করা।",
                "speed_hack": "সমান্তরাল $\\implies \\frac{k}{6} = \\frac{-2}{-4} = \\frac{1}{2} \\implies k = 3$। মুখে মুখে উত্তর!",
                "explanation": "দুটি রেখা সমান্তরাল হওয়ার শর্ত $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\implies \\frac{k}{6} = \\frac{-2}{-4} \\implies k = 3$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_08",
                "stem": "মূলবিন্দু হতে $x\\cos\\alpha + y\\sin\\alpha = p$ সরলরেখার ওপর অঙ্কিত লম্বের দৈর্ঘ্য কত?",
                "options": [
                    "$p$",
                    "$p^2$",
                    "$\\sqrt{p}$",
                    "$2p$"
                ],
                "answer": "A",
                "type_ref": "Type 3: সরলরেখার অভিলম্ব আকার",
                "trap_alert": "$p$ কে সরাসরি দূরত্ব না ভেবে জটিল হিসাব করা। সমীকরণটি নিজেই লম্ব আকার!",
                "speed_hack": "অভিলম্ব আকার $x\\cos\\alpha + y\\sin\\alpha = p$ এ $p$ সর্বদা মূলবিন্দু থেকে লম্ব দূরত্ব নির্দেশ করে।",
                "explanation": "মূলবিন্দু $(0, 0)$ থেকে লম্ব দূরত্ব $d = \\frac{|0 + 0 - p|}{\\sqrt{\\cos^2\\alpha + \\sin^2\\alpha}} = \\frac{p}{1} = p$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_09",
                "stem": "একটি ত্রিভুজের তিনটি শীর্ষবিন্দু $(0, 0), (0, 4)$ এবং $(6, 0)$ হলে ত্রিভুজটির পরিকেন্দ্রের (Circumcenter) স্থানাঙ্ক কত?",
                "options": [
                    "$(3, 2)$",
                    "$(2, 4/3)$",
                    "$(0, 0)$",
                    "$(6, 4)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ত্রিভুজের কেন্দ্রসমূহ (ভরকেন্দ্র, পরিকেন্দ্র, লম্ববিন্দু)",
                "trap_alert": "সমকোণী ত্রিভুজের পরিকেন্দ্র যে অতিভুজের মধ্যবিন্দু তা ভুলে গিয়ে বড় বৃত্তের সমীকরণ বের করা।",
                "speed_hack": "সমকোণী ত্রিভুজের পরিকেন্দ্র সর্বদা অতিভুজের মধ্যবিন্দু! $(6, 0)$ ও $(0, 4)$ এর মধ্যবিন্দু $= (3, 2)$।",
                "explanation": "শীর্ষবিন্দুগুলো অক্ষদ্বয়ে থাকায় ত্রিভুজটি সমকোণী। সমকোণী ত্রিভুজের পরিকেন্দ্র হলো অতিভুজের মধ্যবিন্দু $(3, 2)$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_10",
                "stem": "$y = \\sqrt{3}x + 5$ এবং $y = \\frac{1}{\\sqrt{3}}x - 2$ সরলরেখাদ্বয়ের মধ্যবর্তী সূক্ষ্মকোণ কত?",
                "options": [
                    "$30^\\circ$",
                    "$45^\\circ$",
                    "$60^\\circ$",
                    "$90^\\circ$"
                ],
                "answer": "A",
                "type_ref": "Type 2: দুটি সরলরেখার মধ্যবর্তী কোণ",
                "trap_alert": "ঢালদ্বয়ের কোণ $60^\\circ$ ও $30^\\circ$ বিয়োগ না করে বড় সূত্রে ভুল করা।",
                "speed_hack": "$m_1 = \\sqrt{3} \\implies \\theta_1 = 60^\\circ$, $m_2 = 1/\\sqrt{3} \\implies \\theta_2 = 30^\\circ$। মধ্যবর্তী কোণ $= 60^\\circ - 30^\\circ = 30^\\circ$!",
                "explanation": "দুই রেখার ঢালের আনতি কোণদ্বয় $60^\\circ$ এবং $30^\\circ$, তাই মধ্যবর্তী সূক্ষ্মকোণ $\\theta_1 - \\theta_2 = 30^\\circ$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_11",
                "stem": "$(3, 4)$ বিন্দুর $y = x$ রেখার সাপেক্ষে প্রতিবিম্ব (Reflection) বিন্দু কোনটি?",
                "options": [
                    "$(4, 3)$",
                    "$(-3, -4)$",
                    "$(-4, -3)$",
                    "$(3, -4)$"
                ],
                "answer": "A",
                "type_ref": "Type 3: সরলরেখার সাপেক্ষে বিন্দুর প্রতিবিম্ব",
                "trap_alert": "চিহ্ন বদল করে $(-3, -4)$ দাগানো। $y=x$ রেখার সাপেক্ষে কেবল ভুজ ও কোটি স্থান বিনিময় করে!",
                "speed_hack": "$y = x$ রেখার সাপেক্ষে প্রতিবিম্ব শর্টকাট: $(x, y) \\to (y, x)$। তাই $(3, 4) \\to (4, 3)$।",
                "explanation": "$y = x$ রেখার সাপেক্ষে কোনো বিন্দুর প্রতিবিম্ব নির্ণয়ে ভুজ ও কোটির মান স্থান অদলবদল করে।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_12",
                "stem": "একটি সামান্তরিকের তিনটি শীর্ষবিন্দু $(1, 2), (4, 6)$ এবং $(5, 7)$ হলে ৪র্থ শীর্ষবিন্দুর স্থানাঙ্ক কোনটি?",
                "options": [
                    "$(2, 3)$",
                    "$(8, 11)$",
                    "$(0, 1)$",
                    "$(3, 4)$"
                ],
                "answer": "A",
                "type_ref": "Type 1: সামান্তরিকের ৪র্থ শীর্ষবিন্দু নির্ণয়",
                "trap_alert": "কর্ণের মধ্যবিন্দু সমান না করে ভুল ক্রমে যোগ-বিয়োগ করা।",
                "speed_hack": "শর্টকাট: ৪র্থ শীর্ষ $= (x_1 + x_3 - x_2, y_1 + y_3 - y_2) = (1 + 5 - 4, 2 + 7 - 6) = (2, 3)$।",
                "explanation": "সামান্তরিকের কর্ণদ্বয় পরস্পরকে সমদ্বিখণ্ডিত করে, ফলে ১ম ও ৩য় শীর্ষের যোগফল থেকে ২য় শীর্ষ বিয়োগ করলেই ৪র্থ শীর্ষ পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_13",
                "stem": "$2x + 3y - 5 = 0$ এবং $3x - 2y + 1 = 0$ সরলরেখাদ্বয়ের ছেদবিন্দুগামী রেখাগুচ্ছের সাধারণ সমীকরণ কোনটি?",
                "options": [
                    "$(2x + 3y - 5) + k(3x - 2y + 1) = 0$",
                    "$2x + 3y + k(3x - 2y) = 0$",
                    "$(2x + 3y - 5)(3x - 2y + 1) = k$",
                    "$(2x + 3y) - k(3x - 2y) = 5$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সমান্তরাল ও ছেদবিন্দুগামী রেখাগুচ্ছ (DU Repeated)",
                "trap_alert": "$L_1$ ও $L_2$ সমীকরণের ধ্রুবক বাদ দিয়ে $k$ যুক্ত করা ভুল। পুরো সমীকরণ রাখতে হবে।",
                "speed_hack": "ছেদবিন্দুগামী রেখাগুচ্ছ (Line System): $L_1 + k L_2 = 0$ আকারে সরাসরি প্রকাশ করা যায়।",
                "explanation": "দুটি রেখার ছেদবিন্দুগামী যেকোনো সরলরেখার সমীকরণ $L_1 + k L_2 = 0$ আকারে প্রকাশিত হয়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_14",
                "stem": "উভয় অক্ষ থেকে সমান কিন্তু বিপরীত চিহ্নযুক্ত অংশ ছেদ করে এবং $(2, 3)$ বিন্দুগামী সরলরেখার সমীকরণ কোনটি?",
                "options": [
                    "$x - y + 1 = 0$",
                    "$x + y - 5 = 0$",
                    "$x - y - 1 = 0$",
                    "$2x - 3y = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 1: সরলরেখার ছেদাংশ আকার",
                "trap_alert": "সমান ও বিপরীত চিহ্নযুক্ত মানে $\\frac{x}{a} + \\frac{y}{-a} = 1 \\implies x - y = a$!",
                "speed_hack": "$x - y = a$ তে $(2, 3)$ বসালে $a = 2 - 3 = -1 \\implies x - y = -1 \\implies x - y + 1 = 0$।",
                "explanation": "ছেদাংশ সমীকরণ $\\frac{x}{a} + \\frac{y}{-a} = 1 \\implies x - y = a$। $(2, 3)$ বিন্দুগামী হওয়ায় $2 - 3 = a \\implies a = -1$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_15",
                "stem": "$x = 2, x = 4, y = 4, y = 6$ সরলরেখা চারটি দ্বারা গঠিত বর্গের কর্ণদ্বয়ের ছেদবিন্দুর স্থানাঙ্ক ও কর্ণের দৈর্ঘ্য কত?",
                "options": [
                    "$(3, 5)$ ও $2\\sqrt{2}$ একক",
                    "$(3, 5)$ ও $2$ একক",
                    "$(2, 4)$ ও $2\\sqrt{2}$ একক",
                    "$(3, 5)$ ও $4$ একক"
                ],
                "answer": "A",
                "type_ref": "Type 2: ঢাবি লিখিত ব্লুপ্রিন্ট ও বর্গক্ষেত্রের কর্ণ (DU Written Blueprint)",
                "trap_alert": "বাহুর দৈর্ঘ্য $a = 4 - 2 = 2$ একক; কর্ণের দৈর্ঘ্য $a\\sqrt{2} = 2\\sqrt{2}$ একক, শুধু $2$ নয়।",
                "speed_hack": "ঢাবি লিখিত ব্লুপ্রিন্ট ও শর্টকাট: রেখা চারটি দ্বারা গঠিত বর্গের কেন্দ্র $(x_{mid}, y_{mid}) = (\\frac{2+4}{2}, \\frac{4+6}{2}) = (3, 5)$। বাহু $a = 4 - 2 = 2$ একক, তাই কর্ণের দৈর্ঘ্য $a\\sqrt{2} = 2\\sqrt{2}$ একক!",
                "explanation": "বর্গের বাহুর দৈর্ঘ্য $4-2 = 2$ একক। কর্ণদ্বয়ের ছেদবিন্দু হলো বিপরীত বাহুগুলোর মধ্যবিন্দুর সংযোগের ছেদবিন্দু $(3, 5)$ এবং কর্ণের দৈর্ঘ্য $2\\sqrt{2}$ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_16",
                "stem": "মূলবিন্দুগামী এবং $x$-অক্ষের ধনাত্মক দিকের সাথে $135^\\circ$ কোণ উৎপন্নকারী সরলরেখার সমীকরণ কোনটি?",
                "options": [
                    "$x + y = 0$",
                    "$x - y = 0$",
                    "$\\sqrt{3}x - y = 0$",
                    "$x + \\sqrt{3}y = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 1: মূলবিন্দুগামী রেখা ও ঢাল",
                "trap_alert": "$\\tan 135^\\circ = -1$ এর বদলে $+1$ ভেবে $x - y = 0$ দাগানো।",
                "speed_hack": "ঢাল $m = \\tan 135^\\circ = -1$। মূলবিন্দুগামী রেখা $y = mx \\implies y = -x \\implies x + y = 0$।",
                "explanation": "ঢাল $m = \\tan(180^\\circ - 45^\\circ) = -1$, সুতরাং মূলবিন্দুগামী সমীকরণ $y = -1(x) \\implies x + y = 0$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_17",
                "stem": "$A(2, 3), B(4, 5)$ এবং $C(6, k)$ বিন্দু তিনটি সমরেখ (Collinear) হলে $k$ এর মান কত?",
                "options": [
                    "$7$",
                    "$6$",
                    "$5$",
                    "$8$"
                ],
                "answer": "A",
                "type_ref": "Type 1: সমরেখ বিন্দুর শর্ত",
                "trap_alert": "ত্রিভুজের ক্ষেত্রফল শূন্য করার চেয়ে ঢাল সমান করা অনেক বেশি দ্রুত!",
                "speed_hack": "ঢাল $m_{AB} = \\frac{5 - 3}{4 - 2} = 1$। সমরেখ হতে $m_{BC} = \\frac{k - 5}{6 - 4} = 1 \\implies k - 5 = 2 \\implies k = 7$।",
                "explanation": "বিন্দু তিনটি একই রেখায় অবস্থিত হলে $AB$ ও $BC$ এর ঢাল সমান হবে: $\\frac{2}{2} = \\frac{k-5}{2} \\implies k = 7$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_18",
                "stem": "একটি ত্রিভুজের শীর্ষবিন্দুসমূহ $(1, 2), (4, 6)$ এবং $(3, 8)$ হলে ত্রিভুজটির ক্ষেত্রফল কত বর্গ একক?",
                "options": [
                    "$5$",
                    "$10$",
                    "$7.5$",
                    "$6$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ত্রিভুজ ক্ষেত্রফল মূলবিন্দু শিফটিং ট্রিক (DU Speed-Hack)",
                "trap_alert": "বড় নির্ণায়ক বিস্তার না করে একটি বিন্দুকে $(0, 0)$ তে শিফট করুন।",
                "speed_hack": "মূলবিন্দু শিফটিং ট্রিক (Origin Shift Shortcut): শীর্ষ $(1, 2)$ কে $(0, 0)$ করতে $(1, 2)$ বিয়োগ করুন $\\to (0, 0), (3, 4), (2, 6)$। ক্ষেত্রফল $= \\frac{1}{2}|x_1 y_2 - x_2 y_1| = \\frac{1}{2}|(3)(6) - (4)(2)| = \\frac{1}{2}|18 - 8| = 5$ বর্গ একক!",
                "explanation": "মূলবিন্দু স্থানান্তরের পর ক্ষেত্রফল $= \\frac{1}{2}|(3)(6) - (4)(2)| = \\frac{1}{2}(10) = 5$ বর্গ একক।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_19",
                "stem": "$ax^2 + 2hxy + by^2 = 0$ সমীকরণটি একজোড়া লম্ব সরলরেখা নির্দেশ করার শর্ত কী?",
                "options": [
                    "$a + b = 0$",
                    "$h^2 - ab = 0$",
                    "$a = b$",
                    "$h = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 2: জোড়া সরলরেখা ও লম্বের শর্ত",
                "trap_alert": "সমাপতিত (Coincident) হওয়ার শর্ত $h^2 - ab = 0$ এর সাথে লম্বের শর্ত গুলিয়ে ফেলা।",
                "speed_hack": "জোড়া সরলরেখা লম্ব $\\implies a + b = 0$ ($x^2$ ও $y^2$ এর সহগের যোগফল শূন্য); সমাপতিত $\\implies h^2 = ab$।",
                "explanation": "মূলবিন্দুগামী যুগল সরলরেখার মধ্যবর্তী কোণ $\\tan\\theta = \\frac{2\\sqrt{h^2-ab}}{a+b}$। লম্ব হলে হর $a+b = 0$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_03_20",
                "stem": "পোলার সমীকরণ $r = 4\\cos\\theta$ কার্তেসীয় স্থানাঙ্কে কী নির্দেশ করে?",
                "options": [
                    "$(2, 0)$ কেন্দ্রবিশিষ্ট বৃত্ত",
                    "$(0, 2)$ কেন্দ্রবিশিষ্ট বৃত্ত",
                    "মূলবিন্দুগামী একটি পরাবৃত্ত",
                    "$x$-অক্ষের সমান্তরাল সরলরেখা"
                ],
                "answer": "A",
                "type_ref": "Type 1: পোলার সমীকরণের কার্তেসীয় রূপান্তর",
                "trap_alert": "উভয় পাশে $r$ দ্বারা গুণ করতে ভুলে গিয়ে সরাসরি সরলরেখা ভাবা।",
                "speed_hack": "উভয় পাশে $r$ গুণ করুন: $r^2 = 4r\\cos\\theta \\implies x^2 + y^2 = 4x \\implies (x-2)^2 + y^2 = 4$। এটি $(2, 0)$ কেন্দ্রবিশিষ্ট বৃত্ত!",
                "explanation": "$r = 4\\cos\\theta \\implies r^2 = 4(r\\cos\\theta) \\implies x^2 + y^2 - 4x = 0$, যা $(2, 0)$ কেন্দ্র ও ব্যাসার্ধ $2$ বিশিষ্ট একটি বৃত্ত।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    },
    {
        "chapter_id": "math_1st_04",
        "chapter_title": "বৃত্ত (Circles)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০৪",
        "predictors": [
            {
                "id": "pred_math_1st_04_01",
                "stem": "$x^2 + y^2 - 4x + 6y - 12 = 0$ বৃত্তটির কেন্দ্র ও ব্যাসার্ধ যথাক্রমে কোনটি?",
                "options": [
                    "$(2, -3)$ এবং $5$",
                    "$(-2, 3)$ এবং $5$",
                    "$(2, -3)$ এবং $25$",
                    "$(-4, 6)$ এবং $\\sqrt{12}$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বৃত্তের সাধারণ সমীকরণ ও কেন্দ্র-ব্যাসার্ধ",
                "trap_alert": "中心的 চিহ্ন ভুল করা। $x$ ও $y$ এর সহগকে $-2$ দ্বারা ভাগ করতে হয়!",
                "speed_hack": "কেন্দ্র: $(-4/-2, 6/-2) = (2, -3)$। ব্যাসার্ধ $r = \\sqrt{2^2 + (-3)^2 - (-12)} = \\sqrt{4 + 9 + 12} = \\sqrt{25} = 5$।",
                "explanation": "বৃত্তের সাধারণ সমীকরণ $x^2+y^2+2gx+2fy+c=0$ এর সাথে তুলনা করে কেন্দ্র $(-g, -f) = (2, -3)$ এবং $r = \\sqrt{g^2+f^2-c} = 5$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_02",
                "stem": "$2x^2 + 2y^2 - 8x + 12y - 10 = 0$ বৃত্তটির ব্যাসার্ধ কত একক?",
                "options": [
                    "$3\\sqrt{2}$",
                    "$\\sqrt{18}$",
                    "$\\sqrt{14}$",
                    "$5$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বৃত্তের প্রমিতকরণ ও ব্যাসার্ধ",
                "trap_alert": "শুরুতেই ২ দিয়ে সমীকরণটিকে ভাগ না করে সরাসরি সূত্র বসিয়ে ভুল ব্যাসার্ধ বের করা।",
                "speed_hack": "আগে ২ দিয়ে ভাগ: $x^2 + y^2 - 4x + 6y - 5 = 0$। কেন্দ্র $(2, -3)$। ব্যাসার্ধ $r = \\sqrt{4 + 9 - (-5)} = \\sqrt{18} = 3\\sqrt{2}$।",
                "explanation": "$x^2$ ও $y^2$ এর সহগ ১ বানিয়ে কেন্দ্র $(2, -3), c = -5$ নিয়ে $r = \\sqrt{4+9+5} = \\sqrt{18} = 3\\sqrt{2}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_03",
                "stem": "$x^2 + y^2 - 6x + 8y + c = 0$ বৃত্তটি $X$-অক্ষকে স্পর্শ করলে $c$ এর মান কত?",
                "options": [
                    "$9$",
                    "$16$",
                    "$-9$",
                    "$25$"
                ],
                "answer": "A",
                "type_ref": "Type 2: অক্ষদ্বয়কে স্পর্শ করার শর্ত ($g^2 = c, f^2 = c$) (DU Speed-Hack)",
                "trap_alert": "$X$-অক্ষ স্পর্শে $g^2 = c$ এবং $Y$-অক্ষ স্পর্শে $f^2 = c$। গোলমাল করা যাবে না!",
                "speed_hack": "$X$-অক্ষকে স্পর্শ করার শর্ত: $g^2 = c$। এখানে $2g = -6 \\implies g = -3$, তাই $c = (-3)^2 = 9$। ১ সেকেন্ডে সমাধান!",
                "explanation": "$X$-অক্ষকে স্পর্শ করার শর্ত $g^2 = c \\implies (-3)^2 = c \\implies c = 9$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_04",
                "stem": "$x^2 + y^2 - 8x - 6y + 9 = 0$ বৃত্তটি দ্বারা $Y$-অক্ষ হতে কর্তিত অংশের (জ্যা-এর) দৈর্ঘ্য কত?",
                "options": [
                    "$0$",
                    "$4$",
                    "$8$",
                    "$2\\sqrt{7}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: অক্ষদ্বয় হতে কর্তিত অংশের দৈর্ঘ্য",
                "trap_alert": "কর্তিতাংশের দৈর্ঘ্য $2\\sqrt{f^2 - c} = 2\\sqrt{9 - 9} = 0$, অর্থাৎ এটি $Y$-অক্ষকে স্পর্শ করে!",
                "speed_hack": "$Y$-অক্ষ হতে কর্তিত দৈর্ঘ্য $= 2\\sqrt{f^2 - c} = 2\\sqrt{(-3)^2 - 9} = 2\\sqrt{0} = 0$। স্পর্শ করে বিধায় ছেদাংশ শূন্য।",
                "explanation": "ছেদাংশের দৈর্ঘ্য $2\\sqrt{f^2-c} = 2\\sqrt{9-9} = 0$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_05",
                "stem": "$y = mx + c$ সরলরেখাটি $x^2 + y^2 = a^2$ বৃত্তের স্পর্শক হওয়ার শর্ত কোনটি?",
                "options": [
                    "$c = \\pm a\\sqrt{1 + m^2}$",
                    "$c = \\pm a(1 + m^2)$",
                    "$c = \\pm \\frac{a}{\\sqrt{1 + m^2}}$",
                    "$c^2 = a^2 + m^2$"
                ],
                "answer": "A",
                "type_ref": "Type 3: স্পর্শক হওয়ার শর্ত ও লম্ব দূরত্ব $d=r$ (DU Speed-Hack)",
                "trap_alert": "রুটের বাইরে $\\pm a$ থাকে, এবং রুটের ভেতর $1+m^2$ থাকে।",
                "speed_hack": "স্পর্শকের মূল শর্ত $d = r$: কেন্দ্র $(0,0)$ হতে রেখার লম্ব দূরত্ব $\\frac{|c|}{\\sqrt{1+m^2}} = a \\implies c = \\pm a\\sqrt{1+m^2}$!",
                "explanation": "কেন্দ্র থেকে রেখার লম্ব দূরত্ব ব্যাসার্ধের সমান ($d = r$) হলে রেখাটি স্পর্শক হয়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_06",
                "stem": "$(1, 2)$ ও $(3, 4)$ বিন্দুদ্বয়ের সংযোগ রেখাকে ব্যাস ধরে অঙ্কিত বৃত্তের সমীকরণ কোনটি?",
                "options": [
                    "$x^2 + y^2 - 4x - 6y + 11 = 0$",
                    "$x^2 + y^2 + 4x + 6y + 11 = 0$",
                    "$x^2 + y^2 - 4x - 6y - 11 = 0$",
                    "$x^2 + y^2 - 2x - 3y + 5 = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 1: ব্যাসের প্রান্তবিন্দু দেওয়া থাকলে বৃত্তের সমীকরণ",
                "trap_alert": "ব্যাস আকারের সমীকরণ $(x-x_1)(x-x_2) + (y-y_1)(y-y_2) = 0$ মনে রাখুন।",
                "speed_hack": "$(x-1)(x-3) + (y-2)(y-4) = 0 \\implies x^2 - 4x + 3 + y^2 - 6y + 8 = 0 \\implies x^2 + y^2 - 4x - 6y + 11 = 0$।",
                "explanation": "ব্যাসের প্রান্তবিন্দুর সূত্র: $(x-x_1)(x-x_2) + (y-y_1)(y-y_2) = 0$ বিস্তার করলে উদ্দিষ্ট বৃত্ত পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_07",
                "stem": "$x^2 + y^2 = 25$ বৃত্তের $(3, 4)$ বিন্দুতে অঙ্কিত স্পর্শকের সমীকরণ কোনটি?",
                "options": [
                    "$3x + 4y = 25$",
                    "$4x - 3y = 25$",
                    "$3x - 4y = 25$",
                    "$4x + 3y = 25$"
                ],
                "answer": "A",
                "type_ref": "Type 3: স্পর্শকের সমীকরণ নির্ণয়",
                "trap_alert": "স্পর্শকের জায়গায় অভিলম্বের সমীকরণ বের করে $4x - 3y = 0$ দাগানো।",
                "speed_hack": "বৃত্তের পরিধিস্থ বিন্দুতে স্পর্শক শর্টকাট: $x^2 \\to xx_1, y^2 \\to yy_1$। সরাসরি $3x + 4y = 25$!",
                "explanation": "বৃত্তের স্পর্শকের সূত্র $xx_1 + yy_1 = a^2$। এখানে $(3, 4)$ বসালে $3x + 4y = 25$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_08",
                "stem": "$x^2 + y^2 = 16$ বৃত্তের $(2, 2\\sqrt{3})$ বিন্দুতে অভিলম্বের (Normal) সমীকরণ কোনটি?",
                "options": [
                    "$\\sqrt{3}x - y = 0$",
                    "$x - \\sqrt{3}y = 0$",
                    "$x + \\sqrt{3}y = 8$",
                    "$\\sqrt{3}x + y = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 3: অভিলম্বের সমীকরণ",
                "trap_alert": "মনে রাখবেন, বৃত্তের যেকোনো অভিলম্ব সর্বদা বৃত্তটির কেন্দ্রগামী হয়!",
                "speed_hack": "বৃত্তের কেন্দ্র $(0, 0)$। অভিলম্ব মূলবিন্দুগামী হওয়ায় $y = mx$। ঢাল $m = \\frac{2\\sqrt{3}}{2} = \\sqrt{3} \\implies y = \\sqrt{3}x \\implies \\sqrt{3}x - y = 0$।",
                "explanation": "বৃত্তের যেকোনো স্পর্শবিন্দুতে অভিলম্ব অবশ্যই কেন্দ্রগামী। কেন্দ্র $(0, 0)$ ও $(2, 2\\sqrt{3})$ এর সংযোগ রেখা $\\sqrt{3}x - y = 0$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_09",
                "stem": "$(5, 6)$ বিন্দু হতে $x^2 + y^2 - 4x + 6y - 12 = 0$ বৃত্তে অঙ্কিত স্পর্শকের দৈর্ঘ্য কত একক?",
                "options": [
                    "$\\sqrt{65}$",
                    "$8$",
                    "$9$",
                    "$\\sqrt{53}$"
                ],
                "answer": "A",
                "type_ref": "Type 3: বহিঃস্থ বিন্দু হতে স্পর্শকের দৈর্ঘ্য",
                "trap_alert": "বিন্দুর মান সমীকরণে বসিয়ে বর্গমূল করতে ভুলে যাওয়া।",
                "speed_hack": "স্পর্শকের দৈর্ঘ্য $L = \\sqrt{S_1} = \\sqrt{5^2 + 6^2 - 4(5) + 6(6) - 12} = \\sqrt{25 + 36 - 20 + 36 - 12} = \\sqrt{65}$ একক।",
                "explanation": "বহিঃস্থ বিন্দু $(x_1, y_1)$ থেকে স্পর্শকের দৈর্ঘ্য $L = \\sqrt{x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c} = \\sqrt{65}$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_10",
                "stem": "$x^2 + y^2 - 4x - 6y + c = 0$ এবং $x^2 + y^2 - 2x - 4y + 1 = 0$ বৃত্তদ্বয় পরস্পরকে লম্বভাবে ছেদ (Orthogonal) করার শর্ত কী?",
                "options": [
                    "$2g_1 g_2 + 2f_1 f_2 = c_1 + c_2$",
                    "$g_1 g_2 + f_1 f_2 = c_1 c_2$",
                    "$r_1^2 + r_2^2 = d$",
                    "$c_1 + c_2 = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 2: দুটি বৃত্ত লম্বভাবে ছেদ করার শর্ত",
                "trap_alert": "সূত্রে ২ গুণ করতে ভুলে গিয়ে $g_1 g_2 + f_1 f_2 = c_1 + c_2$ ভাবা।",
                "speed_hack": "অর্থোগোনাল ছেদের শর্ত: $2g_1 g_2 + 2f_1 f_2 = c_1 + c_2$।",
                "explanation": "দুটি বৃত্ত পরস্পর লম্বভাবে ছেদ করলে কেন্দ্রদ্বয়ের দূরত্বের বর্গ ব্যাসার্ধদ্বয়ের বর্গের সমষ্টির সমান হয়, যা $2g_1g_2 + 2f_1f_2 = c_1 + c_2$ তৈরি করে।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_11",
                "stem": "$x^2 + y^2 = 9$ এবং $x^2 + y^2 - 8x - 6y + 21 = 0$ বৃত্তদ্বয় পরস্পরের সাথে কীভাবে অবস্থান করে?",
                "options": [
                    "বহিঃস্থভাবে স্পর্শ করে",
                    "অন্তঃস্থভাবে স্পর্শ করে",
                    "পরস্পরকে ছেদ করে",
                    "স্পর্শ বা ছেদ করে না"
                ],
                "answer": "A",
                "type_ref": "Type 1: বৃত্তদ্বয়ের পারস্পরিক অবস্থান ও স্পর্শবিন্দু (DU Speed-Hack)",
                "trap_alert": "কেন্দ্রদ্বয়ের দূরত্ব $C_1 C_2 = r_1 + r_2$ হলে বহিঃস্পর্শ, আর $|r_1 - r_2|$ হলে অন্তঃস্পর্শ!",
                "speed_hack": "বৃত্তদ্বয়ের স্পর্শ শর্ত: ১ম বৃত্তের কেন্দ্র $C_1(0, 0), r_1 = 3$; ২য় বৃত্তের কেন্দ্র $C_2(4, 3), r_2 = \\sqrt{16+9-21} = 2$। কেন্দ্রদ্বয়ের দূরত্ব $C_1 C_2 = \\sqrt{4^2+3^2} = 5$। যেহেতু $C_1 C_2 = r_1 + r_2 = 3 + 2 = 5$, বৃত্ত দুটি বহিঃস্থভাবে স্পর্শ করে এবং স্পর্শবিন্দু $C_1 C_2$ কে $3 : 2$ অনুপাতে অন্তর্বিভক্ত করে!",
                "explanation": "$C_1 C_2 = \\sqrt{4^2 + 3^2} = 5$ এবং $r_1 + r_2 = 3 + 2 = 5$। দূরত্ব ব্যাসার্ধের যোগফলের সমান হওয়ায় বহিঃস্থভাবে স্পর্শ করে।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_12",
                "stem": "$x^2 + y^2 + 4x - 6y - 12 = 0$ এবং $x^2 + y^2 - 2x + 8y + 4 = 0$ বৃত্তদ্বয়ের সাধারণ জ্যা-এর (Common Chord) সমীকরণ কোনটি?",
                "options": [
                    "$6x - 14y - 16 = 0$",
                    "$2x + 2y - 8 = 0$",
                    "$3x - 7y - 8 = 0$",
                    "$6x + 2y - 8 = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সাধারণ জ্যা এর সমীকরণ",
                "trap_alert": "সাধারণ জ্যা বের করতে গিয়ে বৃত্তের ছেদবিন্দু বের করার জটিল পথে যাওয়া।",
                "speed_hack": "দুটি বৃত্তের সাধারণ জ্যা সমীকরণ সরাসরি: $S_1 - S_2 = 0$। $(4 - (-2))x + (-6 - 8)y + (-12 - 4) = 0 \\implies 6x - 14y - 16 = 0$।",
                "explanation": "দুটি বৃত্তের সাধারণ জ্যা এর সমীকরণ $S_1 - S_2 = 0$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_13",
                "stem": "মূলবিন্দুগামী এবং অক্ষদ্বয় হতে ধনাত্মক $h$ ও $k$ অংশ ছেদকারী বৃত্তের সমীকরণ কোনটি?",
                "options": [
                    "$x^2 + y^2 - hx - ky = 0$",
                    "$x^2 + y^2 + hx + ky = 0$",
                    "$x^2 + y^2 - 2hx - 2ky = 0$",
                    "$x^2 + y^2 - hx - ky = h^2 + k^2$"
                ],
                "answer": "A",
                "type_ref": "Type 1: মূলবিন্দুগামী অক্ষছেদী বৃত্তের ফর্মুলা (DU Speed-Hack)",
                "trap_alert": "সমীকরণে $2hx$ হবে না; কেন্দ্র হলো $(h/2, k/2)$ তাই সমীকরণে সহগ শুধুই $-hx$ এবং $-ky$!",
                "speed_hack": "মূলবিন্দুগামী অক্ষছেদী বৃত্তের শর্টকাট ফর্মুলা: $x^2 + y^2 - hx - ky = 0$। কেন্দ্র $(h/2, k/2)$ ও ব্যাসার্ধ $\\frac{1}{2}\\sqrt{h^2+k^2}$। ২ সেকেন্ডে অপশন নির্বাচন!",
                "explanation": "মূলবিন্দু এবং $(h, 0), (0, k)$ বিন্দুগামী বৃত্তের সমীকরণ সরাসরি $x^2 + y^2 - hx - ky = 0$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_14",
                "stem": "$x^2 + y^2 - 4x + 6y + c = 0$ সমীকরণটি একটি বিন্দু বৃত্ত (Point circle) নির্দেশ করলে $c$ এর মান কত?",
                "options": [
                    "$13$",
                    "$-13$",
                    "$25$",
                    "$5$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বিন্দু বৃত্তের শর্ত",
                "trap_alert": "বিন্দু বৃত্তের ব্যাসার্ধ শূন্য ($r = 0$) হয়, এটি খেয়াল না করা।",
                "speed_hack": "বিন্দু বৃত্ত $\\implies r = 0 \\implies g^2 + f^2 - c = 0 \\implies c = g^2 + f^2 = 2^2 + (-3)^2 = 13$।",
                "explanation": "বিন্দু বৃত্তের ক্ষেত্রে ব্যাসার্ধ শূন্য হওয়ায় $g^2 + f^2 - c = 0 \\implies c = 4 + 9 = 13$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_15",
                "stem": "$x^2 + y^2 = 25$ বৃত্তের যে জ্যা $(1, 2)$ বিন্দুতে সমদ্বিখণ্ডিত হয় তার সমীকরণ কোনটি?",
                "options": [
                    "$x + 2y - 5 = 0$",
                    "$x + 2y - 25 = 0$",
                    "$2x - y = 0$",
                    "$x - 2y + 3 = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 3: নির্দিষ্ট বিন্দুতে সমদ্বিখণ্ডিত জ্যা এর সমীকরণ ($T = S_1$)",
                "trap_alert": "স্পর্শকের সূত্রের সাথে প্যাঁচ লাগানো। সমদ্বিখণ্ডিত জ্যা এর সমীকরণ $T = S_1$!",
                "speed_hack": "$T = S_1 \\implies xx_1 + yy_1 = x_1^2 + y_1^2 \\implies x(1) + y(2) = 1^2 + 2^2 \\implies x + 2y = 5 \\implies x + 2y - 5 = 0$।",
                "explanation": "মধ্যবিন্দু $(x_1, y_1)$ বিশিষ্ট জ্যা-এর সমীকরণ $T = S_1$ প্রয়োগ করে $x(1) + y(2) = 1 + 4 = 5$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_16",
                "stem": "উভয় অক্ষকে স্পর্শ করে এবং $(1, 2)$ বিন্দুগামী বৃত্তের সংখ্যা কয়টি?",
                "options": [
                    "$2$ টি",
                    "$1$ টি",
                    "$4$ টি",
                    "অসংখ্য"
                ],
                "answer": "A",
                "type_ref": "Type 2: উভয় অক্ষকে স্পর্শকারী বৃত্ত",
                "trap_alert": "শুধু ১টি বৃত্ত ভেবে ভুল করা। একটি ছোট বৃত্ত এবং একটি বড় বৃত্ত উভয়ই অক্ষদ্বয় স্পর্শ করে ওই বিন্দু দিয়ে যেতে পারে!",
                "speed_hack": "$(r-1)^2 + (r-2)^2 = r^2 \\implies r^2 - 6r + 5 = 0 \\implies r = 1, 5$। দুটি বাস্তব ব্যাসার্ধ পাওয়া যায় $\\implies ২$টি বৃত্ত।",
                "explanation": "$r$ এর মান দ্বিঘাত সমীকরণ হতে দুটি ভিন্ন ধনাত্মক মান দেয়, ফলে ২টি বাস্তব বৃত্ত পাওয়া যায়।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_17",
                "stem": "$x^2 + y^2 - 8x - 10y + 37 = 0$ বৃত্তটির সাপেক্ষে $(2, 3)$ বিন্দুর অবস্থান কোথায়?",
                "options": [
                    "বৃত্তের অভ্যন্তরে",
                    "বৃত্তের পরিধির ওপর",
                    "বৃত্তের বাইরে",
                    "বৃত্তের কেন্দ্রে"
                ],
                "answer": "A",
                "type_ref": "Type 1: বৃত্তের সাপেক্ষে বিন্দুর অবস্থান",
                "trap_alert": "সমীকরণে মান বসানোর পর চিহ্নের মান শূন্যের চেয়ে ছোট না বড় তা উল্টো বিবেচনা করা।",
                "speed_hack": "কেন্দ্র $(4, 5)$, $r = \\sqrt{16+25-37} = 2$। কেন্দ্র হতে $(2, 3)$ এর দূরত্ব $d = \\sqrt{(4-2)^2+(5-3)^2} = \\sqrt{8} \\approx 2.83 > r$ (বা মান ঋণাত্মক হলে ভেতরে)।",
                "explanation": "সমীকরণে $(2, 3)$ বসালে মান ঋনাত্মক বা কেন্দ্র দূরত্বের তুলনায় ব্যাসার্ধ বড় হলে অভ্যন্তরে থাকে।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_18",
                "stem": "$x^2 + y^2 = 25$ বৃত্তের ওপরিস্থ $(3, -4)$ বিন্দুতে অভিলম্বের ঢাল কত?",
                "options": [
                    "$-\\frac{4}{3}$",
                    "$\\frac{3}{4}$",
                    "$\\frac{4}{3}$",
                    "$-\\frac{3}{4}$"
                ],
                "answer": "A",
                "type_ref": "Type 3: স্পর্শক ও অভিলম্বের ঢাল",
                "trap_alert": "স্পর্শকের ঢাল ($3/4$) এর সাথে অভিলম্বের ঢাল উল্টো করা।",
                "speed_hack": "অভিলম্ব কেন্দ্র $(0, 0)$ ও স্পর্শবিন্দু $(3, -4)$ সংযোগকারী রেখা, তাই তার ঢাল সরাসরি $m = \\frac{-4 - 0}{3 - 0} = -\\frac{4}{3}$!",
                "explanation": "বৃত্তের অভিলম্ব সর্বদা কেন্দ্রগামী হওয়ায় কেন্দ্র ও স্পর্শবিন্দুর সংযোগ রেখার ঢালই অভিলম্বের ঢাল।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_19",
                "stem": "$x^2 + y^2 - 2x + 4y = 0$ বৃত্তের কেন্দ্রগামী এবং $x$-অক্ষের সমান্তরাল রেখার সমীকরণ কোনটি?",
                "options": [
                    "$y + 2 = 0$",
                    "$x - 1 = 0$",
                    "$y - 2 = 0$",
                    "$x + 1 = 0$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বৃত্তের কেন্দ্র ও সরলরেখা",
                "trap_alert": "$x$-অক্ষের সমান্তরাল মানে $y = k$ হবে, $x = k$ নয়!",
                "speed_hack": "কেন্দ্র $(1, -2)$। $x$-অক্ষের সমান্তরাল রেখা $y = -2 \\implies y + 2 = 0$।",
                "explanation": "কেন্দ্র $(1, -2)$ দিয়ে অতিক্রমকারী $x$-অক্ষের সমান্তরাল রেখার সমীকরণ $y = -2$ বা $y + 2 = 0$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_04_20",
                "stem": "পোলার সমীকরণ $r^2 - 2r\\sin\\theta = 3$ কার্তেসীয় সমীকরণে রূপান্তর করলে কী নির্দেশ করে?",
                "options": [
                    "কেন্দ্র $(0, 1)$ ও ব্যাসার্ধ $2$ বিশিষ্ট বৃত্ত",
                    "কেন্দ্র $(1, 0)$ ও ব্যাসার্ধ $2$ বিশিষ্ট বৃত্ত",
                    "একটি অধিবৃত্ত",
                    "একটি সরলরেখা"
                ],
                "answer": "A",
                "type_ref": "Type 1: পোলার সমীকরণ হতে কার্তেসীয় বৃত্ত রূপান্তর (DU Speed-Hack)",
                "trap_alert": "$r\\sin\\theta = y$ এবং $r^2 = x^2+y^2$ সাবধানে রূপান্তর করতে হবে।",
                "speed_hack": "পোলার বৃত্ত রূপান্তর: $r^2 = x^2 + y^2$ এবং $r\\sin\\theta = y$ বসালে $x^2 + y^2 - 2y - 3 = 0 \\implies x^2 + (y-1)^2 = 4$। এটি কেন্দ্র $(0, 1)$ ও ব্যাসার্ধ $\\sqrt{4} = 2$ বিশিষ্ট একটি বৃত্ত!",
                "explanation": "প্রদত্ত পোলার সমীকরণকে রূপান্তর করলে $x^2 + y^2 - 2y - 3 = 0$ পাওয়া যায়, যার কেন্দ্র $(0, 1)$ এবং ব্যাসার্ধ $\\sqrt{0^2 + 1^2 - (-3)} = 2$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    },
    {
        "chapter_id": "math_1st_05",
        "chapter_title": "বিন্যাস ও সমাবেশ (Permutations & Combinations)",
        "subject": "Higher Math",
        "paper": "১ম পত্র",
        "chapter_no": "অধ্যায় ০৫",
        "predictors": [
            {
                "id": "pred_math_1st_05_01",
                "stem": "'ENGINEERING' শব্দের সবকটি বর্ণকে একত্রে নিয়ে কত প্রকারে সাজানো যায়?",
                "options": [
                    "$277,200$",
                    "$138,600$",
                    "$554,400$",
                    "$11!$"
                ],
                "answer": "A",
                "type_ref": "Type 1: পুনরাবৃত্তিযুক্ত শব্দের বর্ণ বিন্যাস",
                "trap_alert": "বর্ণগুলোর পুনরাবৃত্তি সংখ্যা ঠিকমতো না গোনা। E আছে ৩টি, N আছে ৩টি, G আছে ২টি, I আছে ২টি!",
                "speed_hack": "মোট বর্ণ ১১টি। বিন্যাস $= \\frac{11!}{3! \\times 3! \\times 2! \\times 2!} = \\frac{39,916,800}{6 \\times 6 \\times 2 \\times 2} = 277,200$।",
                "explanation": "$n! / (p! q! r! s!)$ সূত্রানুসারে $11! / (3! 3! 2! 2!) = 277,200$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_02",
                "stem": "১২ বাহুবিশিষ্ট একটি সুষম বহুভুজের কর্ণের সংখ্যা কতটি?",
                "options": [
                    "$54$",
                    "$66$",
                    "$12$",
                    "$48$"
                ],
                "answer": "A",
                "type_ref": "Type 2: বহুভুজের কর্ণের সংখ্যা ও জ্যামিতিক সমাবেশ",
                "trap_alert": "কর্ণের সূত্রে বাহুর সংখ্যা $n$ বিয়োগ করতে ভুলে $^n C_2 = ^{12}C_2 = 66$ দাগানো।",
                "speed_hack": "কর্ণের সংখ্যা $= \\frac{n(n-3)}{2} = \\frac{12 \\times 9}{2} = 54$। ২ সেকেন্ডে সমাধান!",
                "explanation": "বহুভুজের শীর্ষবিন্দুগুলো দিয়ে গঠিত মোট রেখাংশ $^{12}C_2 = 66$, তার মধ্যে বাহু ১২টি বাদ দিলে কর্ণের সংখ্যা $66 - 12 = 54$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_03",
                "stem": "'TRIANGLE' শব্দটির স্বরবর্ণগুলোকে (Vowels) সর্বদা একত্রে রেখে কত প্রকারে সাজানো যায়?",
                "options": [
                    "$4320$",
                    "$720$",
                    "$5040$",
                    "$1440$"
                ],
                "answer": "A",
                "type_ref": "Type 1: স্বরবর্ণ একত্রে রাখার শর্ত",
                "trap_alert": "স্বরবর্ণগুলোকে নিজেদের মধ্যে ৩! প্রকারে সাজাতে ভুলে যাওয়া।",
                "speed_hack": "স্বরবর্ণ (I, A, E) ৩টি কে ১টি ধরলে মোট উপাদান $5 + 1 = 6$ টি। সাজানো যায় $6! \\times 3! = 720 \\times 6 = 4320$।",
                "explanation": "ব্যঞ্জনবর্ণ ৫টি ও স্বরবর্ণের বান্ডিল ১টি মিলিয়ে $6! = 720$ এবং স্বরবর্ণ নিজেদের মধ্যে $3! = 6$, মোট $720 \\times 6 = 4320$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_04",
                "stem": "যদি $^n C_{12} = ^n C_8$ হয়, তবে $^n C_{18}$ এর মান কত?",
                "options": [
                    "$190$",
                    "$20$",
                    "$380$",
                    "$1$"
                ],
                "answer": "A",
                "type_ref": "Type 2: সম্পূরক সমাবেশ ও মান নির্ণয়",
                "trap_alert": "$n$ এর মান $12 + 8 = 20$ বের করতে ভুল করা।",
                "speed_hack": "$^n C_x = ^n C_y \\implies n = x + y = 12 + 8 = 20$। সুতরাং $^{20}C_{18} = ^{20}C_2 = \\frac{20 \\times 19}{2} = 190$।",
                "explanation": "সম্পূরক সমাবেশের সূত্রমতে $n = 12 + 8 = 20$, অতএব $^{20}C_{18} = ^{20}C_2 = 190$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_05",
                "stem": "৭ জন ব্যক্তি একটি গোল টেবিলে কত বিভিন্ন উপায়ে বসতে পারেন?",
                "options": [
                    "$720$",
                    "$5040$",
                    "$120$",
                    "$2520$"
                ],
                "answer": "A",
                "type_ref": "Type 1: চক্র-বিন্যাস (Circular Permutation)",
                "trap_alert": "রৈখিক বিন্যাস ভেবে $7! = 5040$ দাগানো। গোল টেবিলে চক্রবিন্যাস $(n-1)!$ হয়!",
                "speed_hack": "চক্রাকার বিন্যাস $= (n-1)! = (7-1)! = 6! = 720$।",
                "explanation": "গোল টেবিলে কোনো নির্দিষ্ট প্রান্ত না থাকায় একজনের সাপেক্ষে সাজাতে হয়, ফলে বিন্যাস সংখ্যা $(7-1)! = 720$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_06",
                "stem": "একটি সমতলে ১০টি বিন্দু আছে যার মধ্যে ৪টি বিন্দু সমরেখ। এই বিন্দুগুলো দ্বারা কতটি ত্রিভুজ গঠন করা যায়?",
                "options": [
                    "$116$",
                    "$120$",
                    "$114$",
                    "$108$"
                ],
                "answer": "A",
                "type_ref": "Type 2: জ্যামিতিক সমাবেশ ও সমরেখ বিন্দুর শর্ত",
                "trap_alert": "সমরেখ ৪টি বিন্দু দিয়ে গঠিত হতে না পারা $^4 C_3 = 4$ টি ত্রিভুজ বিয়োগ করতে ভুলে যাওয়া।",
                "speed_hack": "মোট ত্রিভুজ $= ^{10}C_3 - ^4 C_3 = 120 - 4 = 116$।",
                "explanation": "১০টি বিন্দু হতে মোট ত্রিভুজ $^{10}C_3 = 120$। কিন্তু সমরেখ ৪টি বিন্দু দ্বারা কোনো ত্রিভুজ গঠিত হয় না, তাই $^4C_3 = 4$ বাদ দিলে $120 - 4 = 116$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_07",
                "stem": "একটি অনুষ্ঠানে উপস্থিত ১০ জন ব্যক্তি প্রত্যেকে প্রত্যেকের সাথে করমর্দন (Handshake) করলে মোট করমর্দন সংখ্যা কত হবে?",
                "options": [
                    "$45$",
                    "$90$",
                    "$100$",
                    "$20$"
                ],
                "answer": "A",
                "type_ref": "Type 2: করমর্দন ও রাউন্ড-রবিন ম্যাচ সংখ্যা",
                "trap_alert": "প্রতি করমর্দনে ২ জন ব্যক্তি লাগে, তাই এটি বিন্যাস নয়, সমাবেশ $^{10}C_2$!",
                "speed_hack": "করমর্দন সংখ্যা $= ^n C_2 = \\frac{n(n-1)}{2} = \\frac{10 \\times 9}{2} = 45$।",
                "explanation": "যেকোনো দুজন ব্যক্তির মধ্যে ১টি করমর্দন হয়, সুতরাং মোট করমর্দন $^{10}C_2 = 45$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_08",
                "stem": "৭টি বিভিন্ন রঙের মুক্তা দিয়ে কতভাবে একটি মালা তৈরি করা যায়?",
                "options": [
                    "$360$",
                    "$720$",
                    "$5040$",
                    "$2520$"
                ],
                "answer": "A",
                "type_ref": "Type 1: মুক্তার মালা ও চক্র-বিন্যাস",
                "trap_alert": "মালা উল্টানো যায় বিধায় $(n-1)!$ কে ২ দিয়ে ভাগ করতে ভুলে যাওয়া!",
                "speed_hack": "মুক্তার মালা/ফুলের মালা $\\implies \\frac{(n-1)!}{2} = \\frac{6!}{2} = \\frac{720}{2} = 360$।",
                "explanation": "মালাকে উল্টালে ক্লকওয়াইজ ও অ্যান্টি-ক্লকওয়াইজ অভিন্ন হয়ে যায়, তাই বিন্যাস সংখ্যা $\\frac{(7-1)!}{2} = 360$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_09",
                "stem": "$^{15}C_8 + ^{15}C_7$ এর মান নিচের কোনটির সমান?",
                "options": [
                    "$^{16}C_8$",
                    "$^{16}C_7$",
                    "$^{15}C_{15}$",
                    "$^{30}C_{15}$"
                ],
                "answer": "A",
                "type_ref": "Type 2: প্যাসকেলের সমাবেশ সূত্র",
                "trap_alert": "প্যাসকেলের সূত্রে উপরের ঘাত ১ বৃদ্ধি পায় এবং নিচের বড় সংখ্যাটি থাকে ($^n C_r + ^n C_{r-1} = ^{n+1}C_r$)!",
                "speed_hack": "প্যাসকেল রুল: $^{15}C_8 + ^{15}C_7 = ^{15+1}C_8 = ^{16}C_8$।",
                "explanation": "প্যাসকেলের সূত্র মতে $^n C_r + ^n C_{r-1} = ^{n+1}C_r$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_10",
                "stem": "$0, 1, 2, 3, 4$ অঙ্কগুলো প্রতিবার একবার ব্যবহার করে ৫ অঙ্কের কতগুলো অর্থপূর্ণ সংখ্যা গঠন করা যায়?",
                "options": [
                    "$96$",
                    "$120$",
                    "$24$",
                    "$48$"
                ],
                "answer": "A",
                "type_ref": "Type 1: অঙ্ক দ্বারা সংখ্যা গঠন",
                "trap_alert": "প্রথমে শূন্য বসলে সংখ্যাটি ৪ অঙ্কের হয়ে যায়, তাই ১ম স্থানে শূন্য বাদে ৪টি অপশন থাকে!",
                "speed_hack": "১ম স্থান পূর্ণ করা যায় ৪ উপায়ে (০ বাদে), বাকি ৪টি স্থান $4!$ উপায়ে। মোট $= 4 \\times 4! = 4 \\times 24 = 96$।",
                "explanation": "৫ অঙ্কের সংখ্যার ১ম ঘরে ০ বসতে পারবে না। ফলে ১ম ঘরে ৪টি এবং অবশিষ্ট ঘরে $4! = 24$ প্রকারে সাজালে $4 \\times 24 = 96$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_11",
                "stem": "৬ জন গণিত ও ৪ জন পদার্থবিজ্ঞানের শিক্ষক হতে ৫ জনের একটি কমিটি গঠন করতে হবে যাতে অন্তত ৩ জন গণিতের শিক্ষক থাকেন। কত প্রকারে কমিটি গঠন করা যায়?",
                "options": [
                    "$186$",
                    "$120$",
                    "$252$",
                    "$150$"
                ],
                "answer": "A",
                "type_ref": "Type 2: শর্তযুক্ত কমিটি গঠন",
                "trap_alert": "অন্তত ৩ জন মানে ৩ জন, ৪ জন অথবা ৫ জন গণিত শিক্ষক হতে পারেন, সব কয়টি কেস যোগ করতে হবে!",
                "speed_hack": "কেস ১: $^6 C_3 \\times ^4 C_2 = 20 \\times 6 = 120$; কেস ২: $^6 C_4 \\times ^4 C_1 = 15 \\times 4 = 60$; কেস ৩: $^6 C_5 \\times ^4 C_0 = 6 \\times 1 = 6$। মোট $= 120 + 60 + 6 = 186$।",
                "explanation": "সম্ভাব্য সমাবেশ: $(3M, 2P) + (4M, 1P) + (5M, 0P) = 120 + 60 + 6 = 186$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_12",
                "stem": "৮ জন ব্যক্তির মধ্য থেকে ৩ জনকে একটি গোল টেবিলে এবং ৫ জনকে একটি লাইনে কত উপায়ে সাজানো যায়?",
                "options": [
                    "$^{8}C_3 \\times 2! \\times 5!$",
                    "$8!$",
                    "$^{8}C_3 \\times 3! \\times 5!$",
                    "$2! \\times 5!$"
                ],
                "answer": "A",
                "type_ref": "Type 1: মিশ্র বিন্যাস ও সমাবেশ",
                "trap_alert": "আগে বাছাই $^{8}C_3$, তারপর গোল টেবিলে $(3-1)! = 2!$ এবং লাইনে $5!$ সাজানো!",
                "speed_hack": "৮ জন হতে ৩ জন নির্বাচন: $^8 C_3$। গোল টেবিলে সাজানো: $(3-1)! = 2!$। অবশিষ্ট ৫ জনের সরলরৈখিক বিন্যাস: $5!$। মোট $= ^8 C_3 \\times 2! \\times 5!$।",
                "explanation": "নির্বাচন ও উভয় ধরণের বিন্যাসের গুণন বিধির সঠিক প্রয়োগ।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_13",
                "stem": "৫টি বিভিন্ন রঙের মার্বেল হতে অন্তত ১টি মার্বেল কত প্রকারে বাছাই করা যায়?",
                "options": [
                    "$31$",
                    "$32$",
                    "$30$",
                    "$25$"
                ],
                "answer": "A",
                "type_ref": "Type 2: অন্তত একটি নির্বাচনের সংখ্যা",
                "trap_alert": "$2^n$ থেকে ১ বিয়োগ করতে ভুলে ৩২ দাগানো। কোনোটিই না নেওয়ার ১টি উপায় বাদ দিতে হয়!",
                "speed_hack": "অন্তত ১টি নেওয়ার মোট উপায় $= 2^n - 1 = 2^5 - 1 = 32 - 1 = 31$।",
                "explanation": "প্রতিটি মার্বেল নেয়া বা না নেয়ার উপায় ২টি। ফলে $2^5 = 32$ উপায় হতে কোনোটি না নেয়ার ১টি বাদ দিলে থাকে ৩১।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_14",
                "stem": "$1, 2, 3, 4, 5$ অঙ্কগুলো প্রতিবার কেবল একবার ব্যবহার করে $100$ থেকে $500$-এর মধ্যবর্তী কতগুলো সংখ্যা গঠন করা যায়?",
                "options": [
                    "$48$",
                    "$60$",
                    "$36$",
                    "$24$"
                ],
                "answer": "A",
                "type_ref": "Type 1: রেঞ্জ সীমাবদ্ধ সংখ্যা গঠন (DU Speed-Hack)",
                "trap_alert": "$100$ থেকে $500$-এর মধ্যবর্তী সংখ্যা ৩ অঙ্কের হতে হবে এবং ১ম অংক কেবল $1, 2, 3, 4$ হতে পারবে ($5$ হতে পারবে না)।",
                "speed_hack": "$100$ থেকে $500$-এর মধ্যে ৩ অঙ্কের সংখ্যা: শতকের ঘরে $1, 2, 3, 4$ এর যেকোনো ১টি বসবে (৪ উপায়)। বাকি ২টি ঘর অবশিষ্ট ৪টি অঙ্ক হতে পূরণ করা যাবে $^4P_2 = 4 \\times 3 = 12$ উপায়ে। মোট সংখ্যা $= 4 \\times 12 = 48$!",
                "explanation": "১ম স্থানে ৪টি অপশন এবং পরবর্তী ২টি স্থানে ৪টি অঙ্ক হতে $^4P_2 = 12$ উপায়। মোট সংখ্যা $4 \\times 12 = 48$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_15",
                "stem": "১০টি বাহুবিশিষ্ট বহুভুজের কৌণিক বিন্দুগুলোর সংযোগে গঠিত সরলরেখার সংখ্যা কতটি?",
                "options": [
                    "$45$",
                    "$35$",
                    "$90$",
                    "$10$"
                ],
                "answer": "A",
                "type_ref": "Type 2: জ্যামিতিক সমাবেশ",
                "trap_alert": "সরলরেখার সংখ্যা চেয়েছে, কর্ণের সংখ্যা নয়! কর্ণের সংখ্যা বললে $n$ বিয়োগ হতো।",
                "speed_hack": "যে কোনো দুটি বিন্দু যোগ করলেই একটি সরলরেখা হয়: $^{10}C_2 = \\frac{10 \\times 9}{2} = 45$।",
                "explanation": "১০টি অসমরেখ শীর্ষবিন্দু দ্বারা গঠিত মোট সরলরেখা $^{10}C_2 = 45$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_16",
                "stem": "'CALCULUS' শব্দটির প্রথম ও শেষ বর্ণ 'C' নির্দিষ্ট রেখে বাকি বর্ণগুলোকে কতভাবে সাজানো যায়?",
                "options": [
                    "$180$",
                    "$360$",
                    "$720$",
                    "$90$"
                ],
                "answer": "A",
                "type_ref": "Type 1: নির্দিষ্ট বর্ণ স্থির রেখে বিন্যাস (DU Speed-Hack)",
                "trap_alert": "দুই প্রান্তের দুটি 'C' ফিক্সড, বাকি ৬টি বর্ণের মধ্যে 'L' ও 'U' দুটি করে আছে!",
                "speed_hack": "নির্দিষ্ট প্রান্তিক বর্ণ ফিক্সড ট্রিক: প্রথম ও শেষ স্থানে দুটি 'C' স্থির রাখলে মাঝে অবশিষ্ট থাকে ৬টি বর্ণ (A, L, U, L, U, S)। এদের মধ্যে L আছে ২টি, U আছে ২টি। সাজানোর উপায় $= \\frac{6!}{2! 2!} = \\frac{720}{4} = 180$!",
                "explanation": "দুই প্রান্তে C স্থির রেখে মাঝের ৬টি বর্ণকে সাজানোর মোট সংখ্যা $\\frac{6!}{2! 2!} = 180$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_17",
                "stem": "যদি $^n P_4 = 12 \\times ^n P_2$ হয়, তবে $n$ এর মান কত?",
                "options": [
                    "$6$",
                    "$5$",
                    "$8$",
                    "$4$"
                ],
                "answer": "A",
                "type_ref": "Type 1: বিন্যাস সমীকরণ সমাধান",
                "trap_alert": "উভয় পাশ থেকে $n(n-1)$ বাদ দেওয়ার পর দ্বিঘাত সমীকরণ ভুল সমাধান করা।",
                "speed_hack": "$n(n-1)(n-2)(n-3) = 12n(n-1) \\implies (n-2)(n-3) = 12 = 4 \\times 3 \\implies n - 2 = 4 \\implies n = 6$। ৩ সেকেন্ডে!",
                "explanation": "$(n-2)(n-3) = 12 \\implies n^2 - 5n - 6 = 0 \\implies (n-6)(n+1) = 0 \\implies n = 6$ ($n$ ঋণাত্মক হতে পারে না)।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            },
            {
                "id": "pred_math_1st_05_18",
                "stem": "৪ জন পুরুষ ও ৪ জন মহিলার মধ্য থেকে অন্তত ১ জন মহিলা অন্তর্ভুক্ত রেখে কত প্রকারে ৪ জনের একটি কমিটি গঠন করা যায়?",
                "options": [
                    "$69$",
                    "$70$",
                    "$65$",
                    "$56$"
                ],
                "answer": "A",
                "type_ref": "Type 2: অ্যাট-লিস্ট-ওয়ান কমিটি সিলেকশন (DU Speed-Hack)",
                "trap_alert": "আলাদা করে ১, ২, ৩, ৪ জন মহিলা নিয়ে যোগ করার চেয়ে মোট থেকে শূন্য মহিলার কেস বাদ দেওয়া ১০ গুণ দ্রুত!",
                "speed_hack": "অ্যাট-লিস্ট-ওয়ান ট্রিক (At Least One Shortcut): মোট বাছাই $-$ কোনো মহিলা না নিয়ে বাছাই $= ^8C_4 - ^4C_4 = 70 - 1 = 69$! ৩ সেকেন্ডে সমাধান!",
                "explanation": "কমপক্ষে ১ জন মহিলা থাকার উপায় = মোট কমিটি - কোনো মহিলা না থাকার কমিটি $= ^8C_4 - ^4C_4 = 70 - 1 = 69$।",
                "is_du_repeated": true,
                "is_du_speed_hack": true,
                "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
            }
        ]
    }
]
