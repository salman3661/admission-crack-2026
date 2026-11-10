#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_du_math_curation.py
Comprehensive injection of Udvash DU Higher Math 1st Paper Repeated Questions & Speed Hacks.
"""

import json
import re
import os

import curate_math_p1
import curate_math_p2

# 1. Precise DU 1st Paper updates map: (question_id -> dict of field overrides)
DU_OVERHAUL_MAP = {
    # ---------------- CHAPTER 1: ম্যাট্রিক্স ও নির্ণায়ক ----------------
    "pred_math_1st_01_01": {
        "stem": "$A = \\begin{pmatrix} k - 2 & 4 \\\\ 3 & k + 2 \\end{pmatrix}$ ম্যাট্রিক্সটি ব্যতিক্রমী (Singular) হলে $k$ এর মান কত?",
        "options": ["$\\pm 4$", "$\\pm 2$", "$16$", "$\\pm \\sqrt{10}$"],
        "answer": "A",
        "type_ref": "Type 1: ব্যতিক্রমী ম্যাট্রিক্সের শর্ত ও অজ্ঞাত রাশির মান (DU Repeated)",
        "trap_alert": "কোণাকুণি বিয়োগে চিহ্নের ভুল করে $k^2 + 4$ ভাবা। $(k-2)(k+2) = k^2 - 4$!",
        "speed_hack": "ব্যতিক্রমী হলে $|A| = 0 \\implies (k-2)(k+2) - 12 = 0 \\implies k^2 - 16 = 0 \\implies k = \\pm 4$। ৩ সেকেন্ডে নির্ণয়!",
        "explanation": "ব্যতিক্রমী ম্যাট্রিক্সের নির্ণায়ক শূন্য: $|A| = (k-2)(k+2) - (3)(4) = k^2 - 4 - 12 = k^2 - 16 = 0 \\implies k = \\pm 4$。",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_01_02": {
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
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_01_03": {
        "stem": "যদি $A$ ম্যাট্রিক্সের ক্রম $3 \\times 4$, $B$ ম্যাট্রিক্সের ক্রম $4 \\times 3$ এবং $C$ ম্যাট্রিক্সের ক্রম $3 \\times 2$ হয়, তবে $(A^T + B) \\times C$ ম্যাট্রিক্সের আকার (Order) কত?",
        "options": ["$4 \\times 2$", "$3 \\times 2$", "$4 \\times 3$", "$3 \\times 4$"],
        "answer": "A",
        "type_ref": "Type 3: ম্যাট্রিক্সের গুণন ও মাত্রার শর্ত (DU Speed-Hack)",
        "trap_alert": "যোগের জন্য আকার অভিন্ন হতে হয়। $A$ এর আকার $3 \\times 4$ হলে $A^T$ হয় $4 \\times 3$!",
        "speed_hack": "ডাইমেনশন রুল: $A$ এর আকার $3 \\times 4 \\implies A^T$ হয় $4 \\times 3$। তাই $(A^T + B)$ হলো $4 \\times 3$। এবার $(A^T + B)_{4 \\times 3} \\times C_{3 \\times 2} = 4 \\times 2$! মান হিসাব ছাড়াই সরাসরি নির্ণয়!",
        "explanation": "যোগফল $(A^T + B)$ এর ক্রম $4 \\times 3$ এবং $C$ এর ক্রম $3 \\times 2$। গুণফলের ক্রম হবে $4 \\times 2$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_01_05": {
        "stem": "$\\begin{vmatrix} 1 & a & b+c \\\\ 1 & b & c+a \\\\ 1 & c & a+b \\end{vmatrix}$ নির্ণায়কটির মান কত?",
        "options": ["$0$", "$a+b+c$", "$1$", "$(a-b)(b-c)(c-a)$"],
        "answer": "A",
        "type_ref": "Type 3: নির্ণায়কের ধর্মাবলী ও $|A|=0$ ট্রিক (DU Speed-Hack)",
        "trap_alert": "বড় উৎপাদক বিশ্লেষণ করতে যাওয়া। ২য় ও ৩য় কলাম যোগ করলেই মান শূন্য!",
        "speed_hack": "নির্ণায়কের ধর্মাবলী ও $|A|=0$ ট্রিক: $C_3' = C_2 + C_3$ করলে ৩য় কলামে $(a+b+c)$ কমন এসে ১ম ও ৩য় কলাম অভিন্ন ($1, 1, 1$) হয়ে যায়, ফলে বিস্তার ছাড়াই মান $0$!",
        "explanation": "দুটি কলাম বা সারি অভিন্ন হলে নির্ণায়কের মান সর্বদা শূন্য হয়।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 2: ভেক্টর ----------------
    "pred_math_1st_02_03": {
        "stem": "$\\vec{A} = 2\\hat{i} - \\hat{j} + \\hat{k}$ ভেক্টরের ওপর $\\vec{B} = \\hat{i} - 2\\hat{j} + \\hat{k}$ ভেক্টরের স্কেলার অভিক্ষেপ (Scalar Projection) কত?",
        "options": ["$\\frac{5}{\\sqrt{6}}$", "$\\frac{5}{6}$", "$\\frac{\\sqrt{6}}{5}$", "$\\frac{4}{\\sqrt{6}}$"],
        "answer": "A",
        "type_ref": "Type 1: ভেক্টরের স্কেলার অভিক্ষেপ (DU Speed-Hack)",
        "trap_alert": "যার ওপর অভিক্ষেপ তার মান দিয়ে ভাগ করতে হবে, অর্থাৎ $|\vec{A}|$ দ্বারা ভাগ।",
        "speed_hack": "স্কেলার অভিক্ষেপ শর্টকাট: $X$ এর ওপর $Y$ এর অভিক্ষেপ = $\\frac{X \\cdot Y}{|X|}$। এখানে $\\vec{A} \\cdot \\vec{B} = 2(1) + (-1)(-2) + 1(1) = 5$ এবং $|\\vec{A}| = \\sqrt{4+1+1} = \\sqrt{6}$। তাই মান $\\frac{5}{\\sqrt{6}}$!",
        "explanation": "$\\vec{A}$ এর ওপর $\\vec{B}$ এর স্কেলার অভিক্ষেপ $= \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{A}|} = \\frac{5}{\\sqrt{6}}$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_02_06": {
        "stem": "$\\vec{A} = 2\\hat{i} + \\hat{j} - \\hat{k}$, $\\vec{B} = 3\\hat{i} - 2\\hat{j} + 4\\hat{k}$ এবং $\\vec{C} = \\hat{i} - 3\\hat{j} + a\\hat{k}$ ভেক্টর তিনটি সমতলীয় (Coplanar) হলে $a$ এর মান কত?",
        "options": ["$5$", "$3$", "$-5$", "$7$"],
        "answer": "A",
        "type_ref": "Type 2: সমতলীয় ভেক্টর ও রৈখিক নির্ভরশীলতা (DU Speed-Hack)",
        "trap_alert": "৩য় ক্রমের নির্ণায়ক বিস্তার না করে লিনিয়ার ডিপেনডেন্স লক্ষ্য করুন!",
        "speed_hack": "সমতলীয় ভেক্টর শর্টকাট: নির্ণায়ক $= 0$ অথবা রৈখিক নির্ভরশীলতা পরীক্ষণ! লক্ষ্য করুন $\\vec{C} = \\vec{B} - \\vec{A} \\implies 3-2 = 1, -2-1 = -3$, তাই $a = 4 - (-1) = 5$! নির্ণায়ক না ভেঙেই ৩ সেকেন্ডে মুখে মুখে সমাধান!",
        "explanation": "ভেক্টরত্রয় সমতলীয় হলে তাদের গঠিত নির্ণায়ক শূন্য হয়। অথবা $\\vec{C} = \\vec{B} - \\vec{A}$ হওয়ায় $a = 4 - (-1) = 5$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_02_15": {
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
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_02_17": {
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
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 3: সরলরেখা ----------------
    "pred_math_1st_03_04": {
        "stem": "$2x - 3y + 5 = 0$ রেখার ওপর লম্ব এবং $(1, 2)$ বিন্দুগামী সরলরেখার সমীকরণ কোনটি?",
        "options": ["$3x + 2y - 7 = 0$", "$3x - 2y + 1 = 0$", "$2x + 3y - 8 = 0$", "$3x + 2y + 7 = 0$"],
        "answer": "A",
        "type_ref": "Type 2: লম্ব রেখার সমীকরণ ও ঢাল ইনভার্সন (DU Speed-Hack)",
        "trap_alert": "সহগ বদল ও মাঝের চিহ্ন পরিবর্তনের সময় ভুল চিহ্নে মাইনাস দেওয়া।",
        "speed_hack": "লম্ব রেখার ঢাল ইনভার্সন: $m_1 = \\frac{2}{3} \\implies m_2 = -\\frac{3}{2}$। সমীকরণ: $3x + 2y - (3(1) + 2(2)) = 3x + 2y - 7 = 0$। ৩ সেকেন্ডে সমাধান!",
        "explanation": "$ax + by + c = 0$ এর লম্ব রেখা $bx - ay + k = 0$। এখানে $3x + 2y + k = 0$। $(1, 2)$ বসালে $k = -7$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_03_05": {
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
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_03_06": {
        "stem": "$A(1, 4)$ এবং $B(9, -12)$ বিন্দুদ্বয়ের সংযোগ রেখাংশকে $X$-অক্ষ কোন অনুপাতে বিভক্ত করে?",
        "options": ["$1 : 3$ অন্তর্বিভক্ত", "$1 : 3$ বহির্বিভক্ত", "$3 : 1$ অন্তর্বিভক্ত", "$2 : 3$ অন্তর্বিভক্ত"],
        "answer": "A",
        "type_ref": "Type 1: রেখাংশের অনুপাত স্টেপ-কাউন্টিং (DU Speed-Hack)",
        "trap_alert": "চিহ্ন বিপরীত হলে সর্বদা অন্তর্বিভক্ত হয়; একই চিহ্ন হলে বহির্বিভক্ত হয়।",
        "speed_hack": "স্টেপ-কাউন্টিং অনুপাত ট্রিক: $X$-অক্ষ বিভক্ত করলে অনুপাত $k = |y_1| : |y_2| = 4 : 12 = 1 : 3$। কোটিদ্বয়ের চিহ্ন বিপরীত হওয়ায় সরাসরি অন্তর্বিভক্ত! কোনো সূত্র বা ক্যালকুলেশন ছাড়াই ২ সেকেন্ডে!",
        "explanation": "$X$-অক্ষ দ্বারা বিভাজন অনুপাত $m_1 : m_2 = -y_1 : y_2 = -4 : (-12) = 1 : 3$ (ধনাত্মক মান হওয়ায় অন্তর্বিভক্ত)।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_03_13": {
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
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_03_15": {
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
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_03_18": {
        "stem": "একটি ত্রিভুজের শীর্ষবিন্দুসমূহ $(1, 2), (4, 6)$ এবং $(3, 8)$ হলে ত্রিভুজটির ক্ষেত্রফল কত বর্গ একক?",
        "options": ["$5$", "$10$", "$7.5$", "$6$"],
        "answer": "A",
        "type_ref": "Type 1: ত্রিভুজ ক্ষেত্রফল মূলবিন্দু শিফটিং ট্রিক (DU Speed-Hack)",
        "trap_alert": "বড় নির্ণায়ক বিস্তার না করে একটি বিন্দুকে $(0, 0)$ তে শিফট করুন।",
        "speed_hack": "মূলবিন্দু শিফটিং ট্রিক (Origin Shift Shortcut): শীর্ষ $(1, 2)$ কে $(0, 0)$ করতে $(1, 2)$ বিয়োগ করুন $\\to (0, 0), (3, 4), (2, 6)$। ক্ষেত্রফল $= \\frac{1}{2}|x_1 y_2 - x_2 y_1| = \\frac{1}{2}|(3)(6) - (4)(2)| = \\frac{1}{2}|18 - 8| = 5$ বর্গ একক!",
        "explanation": "মূলবিন্দু স্থানান্তরের পর ক্ষেত্রফল $= \\frac{1}{2}|(3)(6) - (4)(2)| = \\frac{1}{2}(10) = 5$ বর্গ একক।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 4: বৃত্ত ----------------
    "pred_math_1st_04_03": {
        "stem": "$x^2 + y^2 - 6x + 8y + c = 0$ বৃত্তটি $X$-অক্ষকে স্পর্শ করলে $c$ এর মান কত?",
        "options": ["$9$", "$16$", "$-9$", "$25$"],
        "answer": "A",
        "type_ref": "Type 2: অক্ষদ্বয়কে স্পর্শ করার শর্ত ($g^2 = c, f^2 = c$) (DU Speed-Hack)",
        "trap_alert": "$X$-অক্ষ স্পর্শে $g^2 = c$ এবং $Y$-অক্ষ স্পর্শে $f^2 = c$। গোলমাল করা যাবে না!",
        "speed_hack": "$X$-অক্ষকে স্পর্শ করার শর্ত: $g^2 = c$। এখানে $2g = -6 \\implies g = -3$, তাই $c = (-3)^2 = 9$। ১ সেকেন্ডে সমাধান!",
        "explanation": "$X$-অক্ষকে স্পর্শ করার শর্ত $g^2 = c \\implies (-3)^2 = c \\implies c = 9$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_04_05": {
        "stem": "$y = mx + c$ সরলরেখাটি $x^2 + y^2 = a^2$ বৃত্তের স্পর্শক হওয়ার শর্ত কোনটি?",
        "options": ["$c = \\pm a\\sqrt{1 + m^2}$", "$c = \\pm a(1 + m^2)$", "$c = \\pm \\frac{a}{\\sqrt{1 + m^2}}$", "$c^2 = a^2 + m^2$"],
        "answer": "A",
        "type_ref": "Type 3: স্পর্শক হওয়ার শর্ত ও লম্ব দূরত্ব $d=r$ (DU Speed-Hack)",
        "trap_alert": "রুটের বাইরে $\\pm a$ থাকে, এবং রুটের ভেতর $1+m^2$ থাকে।",
        "speed_hack": "স্পর্শকের মূল শর্ত $d = r$: কেন্দ্র $(0,0)$ হতে রেখার লম্ব দূরত্ব $\\frac{|c|}{\\sqrt{1+m^2}} = a \\implies c = \\pm a\\sqrt{1+m^2}$!",
        "explanation": "কেন্দ্র থেকে রেখার লম্ব দূরত্ব ব্যাসার্ধের সমান ($d = r$) হলে রেখাটি স্পর্শক হয়।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_04_11": {
        "stem": "$x^2 + y^2 = 9$ এবং $x^2 + y^2 - 8x - 6y + 21 = 0$ বৃত্তদ্বয় পরস্পরের সাথে কীভাবে অবস্থান করে?",
        "options": ["বহিঃস্থভাবে স্পর্শ করে", "অন্তঃস্থভাবে স্পর্শ করে", "পরস্পরকে ছেদ করে", "স্পর্শ বা ছেদ করে না"],
        "answer": "A",
        "type_ref": "Type 1: বৃত্তদ্বয়ের পারস্পরিক অবস্থান ও স্পর্শবিন্দু (DU Speed-Hack)",
        "trap_alert": "কেন্দ্রদ্বয়ের দূরত্ব $C_1 C_2 = r_1 + r_2$ হলে বহিঃস্পর্শ, আর $|r_1 - r_2|$ হলে অন্তঃস্পর্শ!",
        "speed_hack": "বৃত্তদ্বয়ের স্পর্শ শর্ত: ১ম বৃত্তের কেন্দ্র $C_1(0, 0), r_1 = 3$; ২য় বৃত্তের কেন্দ্র $C_2(4, 3), r_2 = \\sqrt{16+9-21} = 2$। কেন্দ্রদ্বয়ের দূরত্ব $C_1 C_2 = \\sqrt{4^2+3^2} = 5$। যেহেতু $C_1 C_2 = r_1 + r_2 = 3 + 2 = 5$, বৃত্ত দুটি বহিঃস্থভাবে স্পর্শ করে এবং স্পর্শবিন্দু $C_1 C_2$ কে $3 : 2$ অনুপাতে অন্তর্বিভক্ত করে!",
        "explanation": "$C_1 C_2 = \\sqrt{4^2 + 3^2} = 5$ এবং $r_1 + r_2 = 3 + 2 = 5$। দূরত্ব ব্যাসার্ধের যোগফলের সমান হওয়ায় বহিঃস্থভাবে স্পর্শ করে।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_04_13": {
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
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_04_20": {
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
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 5: বিন্যাস ও সমাবেশ ----------------
    "pred_math_1st_05_14": {
        "stem": "$1, 2, 3, 4, 5$ অঙ্কগুলো প্রতিবার কেবল একবার ব্যবহার করে $100$ থেকে $500$-এর মধ্যবর্তী কতগুলো সংখ্যা গঠন করা যায়?",
        "options": ["$48$", "$60$", "$36$", "$24$"],
        "answer": "A",
        "type_ref": "Type 1: রেঞ্জ সীমাবদ্ধ সংখ্যা গঠন (DU Speed-Hack)",
        "trap_alert": "$100$ থেকে $500$-এর মধ্যবর্তী সংখ্যা ৩ অঙ্কের হতে হবে এবং ১ম অংক কেবল $1, 2, 3, 4$ হতে পারবে ($5$ হতে পারবে না)।",
        "speed_hack": "$100$ থেকে $500$-এর মধ্যে ৩ অঙ্কের সংখ্যা: শতকের ঘরে $1, 2, 3, 4$ এর যেকোনো ১টি বসবে (৪ উপায়)। বাকি ২টি ঘর অবশিষ্ট ৪টি অঙ্ক হতে পূরণ করা যাবে $^4P_2 = 4 \\times 3 = 12$ উপায়ে। মোট সংখ্যা $= 4 \\times 12 = 48$!",
        "explanation": "১ম স্থানে ৪টি অপশন এবং পরবর্তী ২টি স্থানে ৪টি অঙ্ক হতে $^4P_2 = 12$ উপায়। মোট সংখ্যা $4 \\times 12 = 48$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_05_16": {
        "stem": "'CALCULUS' শব্দটির প্রথম ও শেষ বর্ণ 'C' নির্দিষ্ট রেখে বাকি বর্ণগুলোকে কতভাবে সাজানো যায়?",
        "options": ["$180$", "$360$", "$720$", "$90$"],
        "answer": "A",
        "type_ref": "Type 1: নির্দিষ্ট বর্ণ স্থির রেখে বিন্যাস (DU Speed-Hack)",
        "trap_alert": "দুই প্রান্তের দুটি 'C' ফিক্সড, বাকি ৬টি বর্ণের মধ্যে 'L' ও 'U' দুটি করে আছে!",
        "speed_hack": "নির্দিষ্ট প্রান্তিক বর্ণ ফিক্সড ট্রিক: প্রথম ও শেষ স্থানে দুটি 'C' স্থির রাখলে মাঝে অবশিষ্ট থাকে ৬টি বর্ণ (A, L, U, L, U, S)। এদের মধ্যে L আছে ২টি, U আছে ২টি। সাজানোর উপায় $= \\frac{6!}{2! 2!} = \\frac{720}{4} = 180$!",
        "explanation": "দুই প্রান্তে C স্থির রেখে মাঝের ৬টি বর্ণকে সাজানোর মোট সংখ্যা $\\frac{6!}{2! 2!} = 180$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_05_18": {
        "stem": "৪ জন পুরুষ ও ৪ জন মহিলার মধ্য থেকে অন্তত ১ জন মহিলা অন্তর্ভুক্ত রেখে কত প্রকারে ৪ জনের একটি কমিটি গঠন করা যায়?",
        "options": ["$69$", "$70$", "$65$", "$56$"],
        "answer": "A",
        "type_ref": "Type 2: অ্যাট-লিস্ট-ওয়ান কমিটি সিলেকশন (DU Speed-Hack)",
        "trap_alert": "আলাদা করে ১, ২, ৩, ৪ জন মহিলা নিয়ে যোগ করার চেয়ে মোট থেকে শূন্য মহিলার কেস বাদ দেওয়া ১০ গুণ দ্রুত!",
        "speed_hack": "অ্যাট-লিস্ট-ওয়ান ট্রিক (At Least One Shortcut): মোট বাছাই $-$ কোনো মহিলা না নিয়ে বাছাই $= ^8C_4 - ^4C_4 = 70 - 1 = 69$! ৩ সেকেন্ডে সমাধান!",
        "explanation": "কমপক্ষে ১ জন মহিলা থাকার উপায় = মোট কমিটি - কোনো মহিলা না থাকার কমিটি $= ^8C_4 - ^4C_4 = 70 - 1 = 69$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 6: ত্রিকোণমিতিক অনুপাত ----------------
    "pred_math_1st_06_11": {
        "stem": "$\\frac{1 - \\tan^2 30^\\circ}{1 + \\tan^2 30^\\circ}$ এর মান কত?",
        "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{1}{\\sqrt{3}}$", "$1$"],
        "answer": "A",
        "type_ref": "Type 2: ত্রিকোণমিতিক দ্বিগুণ কোণ রূপান্তর (DU Speed-Hack)",
        "trap_alert": "মান বসিয়ে জটিল ভগ্নাংশ সমাধান করতে গিয়ে সময় নষ্ট করা।",
        "speed_hack": "দ্বিগুণ কোণের সূত্র: $\\frac{1-\\tan^2\\theta}{1+\\tan^2\\theta} = \\cos 2\\theta$। এখানে $\\theta = 30^\\circ$, তাই $\\cos(2 \\times 30^\\circ) = \\cos 60^\\circ = \\frac{1}{2}$! ২ সেকেন্ডে উত্তর!",
        "explanation": "$\\frac{1-\\tan^2 30^\\circ}{1+\\tan^2 30^\\circ} = \\cos(2 \\times 30^\\circ) = \\cos 60^\\circ = 1/2$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 7: সংযুক্ত কোণের ত্রিকোণমিতিক অনুপাত ----------------
    "pred_math_1st_07_02": {
        "stem": "$\\cos 20^\\circ \\cos 40^\\circ \\cos 80^\\circ$ এর মান কত?",
        "options": ["$\\frac{1}{8}$", "$\\frac{1}{16}$", "$\\frac{\\sqrt{3}}{8}$", "$\\frac{1}{4}$"],
        "answer": "A",
        "type_ref": "Type 1: ঢাবি স্পেশাল কোসাইন গুণন সিরিজ (DU Speed-Hack)",
        "trap_alert": "দীর্ঘ ২ দিয়ে গুণ ও যোগ-বিয়োগ না করে সরাসরি গুণন ট্রিক মনে রাখুন।",
        "speed_hack": "ঢাবি স্পেশাল কোসাইন গুণন শর্টকাট: $\\cos\\theta \\cos 2\\theta \\dots \\cos(2^n\\theta) = \\frac{\\sin(2^{n+1}\\theta)}{2^{n+1}\\sin\\theta}$। এখানে $\\theta = 20^\\circ, n = 2 \\implies \\frac{\\sin(8 \\times 20^\\circ)}{8\\sin 20^\\circ} = \\frac{\\sin 160^\\circ}{8\\sin 20^\\circ} = \\frac{1}{8}$!",
        "explanation": "কোসাইন সিরিজের সরাসরি সূত্রানুসারে মান $\\frac{1}{2^3} = \\frac{1}{8}$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_07_05": {
        "stem": "$\\frac{\\cos 8^\\circ + \\sin 8^\\circ}{\\cos 8^\\circ - \\sin 8^\\circ}$ এর মান কোনটির সমান?",
        "options": ["$\\tan 53^\\circ$", "$\\tan 37^\\circ$", "$\\cot 53^\\circ$", "$\\tan 45^\\circ$"],
        "answer": "A",
        "type_ref": "Type 1: ট্যান কোণ রূপান্তর ট্রিক (DU Speed-Hack)",
        "trap_alert": "লবে প্লাস থাকলে কোণ $45^\\circ + \\theta$ হয়; লবে মাইনাস থাকলে $45^\\circ - \\theta$ হয়!",
        "speed_hack": "ট্যান রূপান্তর ট্রিক: $\\frac{\\cos\\theta + \\sin\\theta}{\\cos\\theta - \\sin\\theta} = \\tan(45^\\circ + \\theta)$। এখানে $\\theta = 8^\\circ$, তাই $\\tan(45^\\circ + 8^\\circ) = \\tan 53^\\circ$! মুখে মুখে ১ সেকেন্ডে সমাধান!",
        "explanation": "লব ও হরকে $\\cos 8^\\circ$ দ্বারা ভাগ করলে $\\frac{1 + \\tan 8^\\circ}{1 - \\tan 8^\\circ} = \\tan(45^\\circ + 8^\\circ) = \\tan 53^\\circ$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_07_10": {
        "stem": "$\\triangle ABC$-তে $A+B+C = \\pi$ হলে $\\sin 2A + \\sin 2B + \\sin 2C$ এর মান কোনটির সমান?",
        "options": ["$4\\sin A \\sin B \\sin C$", "$2\\sin A \\sin B \\sin C$", "$4\\cos A \\cos B \\cos C$", "$\\sin A + \\sin B + \\sin C$"],
        "answer": "A",
        "type_ref": "Type 2: ৭.৬ রূপান্তর ফ্লো ও কোণ প্রতিস্থাপন ট্রিক (DU Speed-Hack)",
        "trap_alert": "কোসাইন নাকি সাইন গুণফল তা নিয়ে বিভ্রান্ত হওয়া। $\\sin 2A + \\sin 2B + \\sin 2C = 4\\sin A \\sin B \\sin C$!",
        "speed_hack": "৭.৬ ট্রান্সফর্মেশন ফ্লো ট্রিক: সমকোণী ত্রিভুজ অ্যাঙ্গেল সাবস্টিটিউশন ($A = 90^\\circ, B = 45^\\circ, C = 45^\\circ$) বসালে বামপক্ষ $= \\sin 180^\\circ + \\sin 90^\\circ + \\sin 90^\\circ = 0 + 1 + 1 = 2$। ডানপক্ষে $4\\sin 90^\\circ \\sin 45^\\circ \\sin 45^\\circ = 4(1)(1/\\sqrt{2})(1/\\sqrt{2}) = 2$! ম্যাজিক সমাধান!",
        "explanation": "ত্রিকোণমিতিক রূপান্তর প্রক্রিয়ায় $\\sin 2A + \\sin 2B + \\sin 2C = 4\\sin A \\sin B \\sin C$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_07_20": {
        "stem": "$\\triangle ABC$-তে $\\cos^2 A + \\cos^2 B + \\cos^2 C + 2\\cos A \\cos B \\cos C$ এর মান কত?",
        "options": ["$1$", "$0$", "$2$", "$-1$"],
        "answer": "A",
        "type_ref": "Type 2: সমকোণী ত্রিভুজ অ্যাঙ্গেল সাবস্টিটিউশন ট্রিক (DU Speed-Hack)",
        "trap_alert": "দীর্ঘ ত্রিকোণমিতিক প্রমাণের পেছনে সময় নষ্ট করা।",
        "speed_hack": "সমকোণী ত্রিভুজ অ্যাঙ্গেল সাবস্টিটিউশন ট্রিক: $A = 90^\\circ, B = 60^\\circ, C = 30^\\circ$ ধরলে $\\cos 90^\\circ = 0$! রাশিটি দাঁড়ায় $0 + \\cos^2 60^\\circ + \\cos^2 30^\\circ + 0 = 0 + \\frac{1}{4} + \\frac{3}{4} = 1$! ২ সেকেন্ডে ম্যাজিক সমাধান!",
        "explanation": "যেকোনো ত্রিভুজের জন্য $\\cos^2 A + \\cos^2 B + \\cos^2 C + 2\\cos A \\cos B \\cos C = 1$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 8: ফাংশন ও ফাংশনের লেখচিত্র ----------------
    "pred_math_1st_08_10": {
        "stem": "$f(x) = 3x - 5$ হলে $f^{-1}(4)$ এর মান কত?",
        "options": ["$3$", "$7$", "$1$", "$\\frac{1}{7}$"],
        "answer": "A",
        "type_ref": "Type 2: ফাস্ট ইনভার্স মান নির্ণয় (DU Speed-Hack)",
        "trap_alert": "আগে সম্পূর্ণ ইনভার্স ফাংশন $f^{-1}(x)$ সমীকরণ বের করতে গিয়ে অতিরিক্ত সময় নষ্ট করা।",
        "speed_hack": "ফাস্ট ইনভার্স ট্রিক: সমীকরণ উল্টো করে ইনভার্স ফাংশন না বের করে সরাসরি $f(x) = 4$ বসিয়ে সমাধান করুন: $3x - 5 = 4 \\implies 3x = 9 \\implies x = 3$! ৩ সেকেন্ডে সমাধান!",
        "explanation": "$f^{-1}(4) = x \\implies f(x) = 4 \\implies 3x - 5 = 4 \\implies 3x = 9 \\implies x = 3$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_08_11": {
        "stem": "$f(x) = \\frac{1}{\\sqrt{4 - x^2}}$ ফাংশনটির বাস্তব ডোমেন (Domain) কোনটি?",
        "options": ["$(-2, 2)$", "$[-2, 2]$", "$(-\\infty, -2) \\cup (2, \\infty)$", "$[0, 2)$"],
        "answer": "A",
        "type_ref": "Type 1: ভগ্নাংশ মূলের ডোমেন ও সাইন অল্টারনেশন (DU Speed-Hack)",
        "trap_alert": "হর শূন্য হতে পারে না, তাই খোলা ব্যবধি $(-2, 2)$ হবে, বন্ধ ব্যবধি $[-2, 2]$ নয়!",
        "speed_hack": "ভগ্নাংশ মূলের ডোমেন ও সাইন অল্টারনেশন: হরের বর্গমূলের ভেতর $4 - x^2 > 0 \\implies x^2 < 4 \\implies -2 < x < 2$ (খোলা ব্যবধি $(-2, 2)$)। হর শূন্য হতে পারে না তাই প্রান্তবিন্দু বাদ!",
        "explanation": "বাস্তব মানের জন্য $4 - x^2 > 0 \\implies x^2 < 4 \\implies -2 < x < 2$ বা ডোমেন $(-2, 2)$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_08_19": {
        "stem": "$f(x) = \\sqrt{x^2 - 5x + 6}$ ফাংশনটির বাস্তব ডোমেন (Domain) কোনটি?",
        "options": ["$(-\\infty, 2] \\cup [3, \\infty)$", "$[2, 3]$", "$(2, 3)$", "$(-\\infty, 2) \\cup (3, \\infty)$"],
        "answer": "A",
        "type_ref": "Type 1: দ্বিপদী দ্বিঘাত মূলের ডোমেন ও অঞ্চল সাইন পদ্ধতি (DU Speed-Hack)",
        "trap_alert": "অসমতায় $\\ge 0$ থাকলে বাইরের অঞ্চল হয়, ভেতরের অঞ্চল নয়।",
        "speed_hack": "নাম্বার লাইন সাইন অল্টারনেশন ট্রিক: $(x-2)(x-3) \\ge 0$। যেহেতু অসমতায় $\\ge 0$ (বৃহত্তর), সমাধান হবে প্রান্তিক দুই বাইরের অঞ্চল ($x \\le 2$ অথবা $x \\ge 3$), অর্থাৎ $(-\\infty, 2] \\cup [3, \\infty)$! মাঝের অঞ্চল $[2, 3]$ হতো যদি $< 0$ থাকতো!",
        "explanation": "বর্গমূলের ভেতরের রাশি অশূন্য বা অঋণাত্মক হতে হবে: $x^2 - 5x + 6 \\ge 0 \\implies (x-2)(x-3) \\ge 0 \\implies x \\le 2$ অথবা $x \\ge 3$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 9: অন্তরীকরণ ----------------
    "pred_math_1st_09_01": {
        "stem": "$\\lim_{x \\to 0} \\frac{\\sin 3x}{\\tan^{-1} 2x}$ এর মান কত?",
        "options": ["$\\frac{3}{2}$", "$\\frac{2}{3}$", "$1$", "$6$"],
        "answer": "A",
        "type_ref": "Type 1: ত্রিকোণমিতিক লিমিট সহগ অনুপাত শর্টকাট (DU Speed-Hack)",
        "trap_alert": "ব্যস্তানুপাতিক ভেবে $2/3$ দাগানো। লব ও হরের চলকের সহগের সরাসরি ভাগফল হয়।",
        "speed_hack": "ত্রিকোণমিতিক লিমিট শর্টকাট: $\\lim_{x \\to 0} \\frac{\\sin ax}{\\tan^{-1} bx} = \\frac{a}{b}$। এখানে $a = 3, b = 2$, তাই মান $\\frac{3}{2}$! সরাসরি ১ সেকেন্ডে টিক!",
        "explanation": "$\\lim_{x \\to 0} \\frac{\\sin 3x}{\\tan^{-1} 2x} = \\frac{3}{2} \\times \\lim \\frac{\\sin 3x}{3x} \\times \\frac{2x}{\\tan^{-1} 2x} = \\frac{3}{2}$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_09_10": {
        "stem": "যদি $(1 - x^2)y_2 - x y_1 = 2$ হয়, তবে নিচের কোনটি $y$ এর সঠিক মান?",
        "options": ["$(\\cos^{-1} x)^2$", "$\\cos^{-1} x$", "$\\sin^{-1} x$", "$\\tan^{-1} x$"],
        "answer": "A",
        "type_ref": "Type 1: সাকসেসিভ ডিফারেনশিয়েশন পাওয়ার ট্রিক (DU Speed-Hack)",
        "trap_alert": "ডানপক্ষে শূন্য থাকলে $y = \\cos^{-1}x$ হতো, কিন্তু ডানপক্ষে ২ থাকলে ঘাত ২ হয়!",
        "speed_hack": "ঢাবি সাকসেসিভ ডিফারেনশিয়েশন পাওয়ার ট্রিক: ডানপক্ষে অশূন্য ধ্রুবক $2$ থাকা মানে ইনভার্স ফাংশনের ঘাত ছিল ২! অর্থাৎ $y = (\\cos^{-1}x)^2$। অপশন দেখে ১ সেকেন্ডে নিশ্চিত টিক!",
        "explanation": "$y = (\\cos^{-1}x)^2 \\implies y_1 = 2\\cos^{-1}x \\cdot \\frac{-1}{\\sqrt{1-x^2}} \\implies (1-x^2)y_1^2 = 4y$। পুনরায় অন্তরীকরণ করলে $(1-x^2)y_2 - x y_1 = 2$ পাওয়া যায়।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_09_12": {
        "stem": "$x^3 + y^3 - 3axy = 0$ বক্ররেখার ক্ষেত্রে $\\frac{dy}{dx}$ এর মান কোনটি?",
        "options": ["$-\\frac{x^2 - ay}{y^2 - ax}$", "$\\frac{x^2 - ay}{y^2 - ax}$", "$-\\frac{y^2 - ax}{x^2 - ay}$", "$-\\frac{x^2 + ay}{y^2 + ax}$"],
        "answer": "A",
        "type_ref": "Type 1: অব্যক্ত ফাংশনের আংশিক অন্তরক শর্টকাট (DU Speed-Hack)",
        "trap_alert": "সূত্রের বাইরের মাইনাস চিহ্ন দিতে ভুলে যাওয়া।",
        "speed_hack": "অব্যক্ত ফাংশনের শর্টকাট: $\\frac{dy}{dx} = -\\frac{\\partial f / \\partial x}{\\partial f / \\partial y} = -\\frac{3x^2 - 3ay}{3y^2 - 3ax} = -\\frac{x^2 - ay}{y^2 - ax}$! ৩ সেকেন্ডে সমাধান!",
        "explanation": "অব্যক্ত ফাংশনের অন্তরক নির্ণয়ে $\\frac{dy}{dx} = -\\frac{f_x}{f_y} = -\\frac{3x^2 - 3ay}{3y^2 - 3ax} = -\\frac{x^2 - ay}{y^2 - ax}$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_09_14": {
        "stem": "$\\lim_{x \\to 0} \\frac{\\ln(1 + 5x)}{x}$ এর মান কত?",
        "options": ["$5$", "$1$", "$\\frac{1}{5}$", "$0$"],
        "answer": "A",
        "type_ref": "Type 1: L'Hôpital ট্রিগার ও স্ট্যান্ডার্ড লিমিট (DU Speed-Hack)",
        "trap_alert": "সহগ ৫ কে উপেক্ষা করে ১ দাগানো।",
        "speed_hack": "L'Hôpital ট্রিগার ($0/0$ আকার): লব ও হরকে অন্তরীকরণ করলে $\\frac{5/(1+5x)}{1} \\to 5$। ১ সেকেন্ডে উত্তর!",
        "explanation": "$\\lim_{x \\to 0} \\frac{\\ln(1 + 5x)}{5x} \\times 5 = 1 \\times 5 = 5$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_09_20": {
        "stem": "$\\lim_{x \\to -\\infty} \\left(\\sqrt{x^2 + 5x} + x\\right)$ এর মান কত?",
        "options": ["$-\\frac{5}{2}$", "$\\frac{5}{2}$", "$5$", "$-5$"],
        "answer": "A",
        "type_ref": "Type 1: ঋণাত্মক অসীম লিমিট ও সাইন ট্র্যাপ (DU Trap-Alert)",
        "trap_alert": "$x < 0$ এর জন্য $\\sqrt{x^2} = |x| = -x$ বিবেচনা না করলে চিহ্নে ভুল হয়ে $+\\frac{5}{2}$ উত্তর আসবে!",
        "speed_hack": "ঋণাত্মক অসীম লিমিট ট্র্যাপ: $x \\to -\\infty$ হলে $x = -t$ (যেখানে $t \\to \\infty$)। $\\sqrt{x^2} = |x| = -x$ বিবেচনায় $\\sqrt{t^2 - 5t} - t = \\frac{-5t}{\\sqrt{t^2 - 5t} + t} \\to -\\frac{5}{2}$। চিহ্নের ট্র্যাপে পড়বেন না!",
        "explanation": "অনুবন্ধী দ্বারা গুণ ও ভাগ করে পাই: $\\frac{(x^2+5x)-x^2}{\\sqrt{x^2+5x}-x} = \\frac{5x}{-x\\sqrt{1+5/x}-x} = \\frac{5}{-2} = -\\frac{5}{2}$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },

    # ---------------- CHAPTER 10: যোগজীকরণ ----------------
    "pred_math_1st_10_05": {
        "stem": "$y^2 = 4x$ পরাবৃত্ত এবং $y = x$ সরলরেখা দ্বারা সীমাবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?",
        "options": ["$\\frac{8}{3}$", "$\\frac{16}{3}$", "$\\frac{4}{3}$", "$8$"],
        "answer": "A",
        "type_ref": "Type 3: পরাবৃত্ত ও সরলরেখার আবদ্ধ ক্ষেত্রফল (DU Speed-Hack)",
        "trap_alert": "ইন্টিগ্রেশন করে সীমা বসানোর দরকার নেই, সরাসরি অনুসিদ্ধান্ত ব্যবহার করুন!",
        "speed_hack": "পরাবৃত্ত ও সরলরেখার আবদ্ধ ক্ষেত্রফল শর্টকাট: $y^2 = 4ax$ এবং $y = mx$ এর আবদ্ধ ক্ষেত্রফল $= \\frac{8}{3}\\frac{a^2}{m^3}$। এখানে $4a = 4 \\implies a = 1$ এবং $m = 1$। ক্ষেত্রফল $= \\frac{8}{3}\\frac{1^2}{1^3} = \\frac{8}{3}$ বর্গ একক!",
        "explanation": "ক্ষেত্রফল $= \\int_0^4 (\\sqrt{4x} - x) dx = [\\frac{4}{3}x^{3/2} - \\frac{x^2}{2}]_0^4 = \\frac{32}{3} - 8 = \\frac{8}{3}$ বর্গ একক।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_10_09": {
        "stem": "$\\int_{-1}^3 |x - 1| dx$ এর মান কত?",
        "options": ["$4$", "$2$", "$8$", "$6$"],
        "answer": "A",
        "type_ref": "Type 2: মডুলাস ফাংশন ও ত্রিভুজ ক্ষেত্রফল শর্টকাট (DU Speed-Hack)",
        "trap_alert": "মডুলাস সীমা ভেঙে দুই খণ্ডে যোগজীকরণ করতে গেলে ৩ মিনিট ব্যয় হবে। গ্রাফ আঁকুন!",
        "speed_hack": "মডুলাস যোগজ গ্রাফ শর্টকাট: $V$-আকৃতির গ্রাফের নিচে দুটি সমদ্বিবাহু ত্রিভুজের ক্ষেত্রফল $= \\frac{1}{2}(1 - (-1))^2 + \\frac{1}{2}(3 - 1)^2 = \\frac{1}{2}(4) + \\frac{1}{2}(4) = 2 + 2 = 4$! মুখে মুখে ২ সেকেন্ডে সমাধান!",
        "explanation": "$x=1$ বিন্দুতে শীর্ষ। বাম পাশের ত্রিভুজের ভূমি ২, উচ্চতা ২ (ক্ষেত্রফল ২) এবং ডান পাশের ত্রিভুজের ভূমি ২, উচ্চতা ২ (ক্ষেত্রফল ২)। মোট ক্ষেত্রফল $২+২=৪$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_10_13": {
        "stem": "$y = x^2$ এবং $x = y^2$ বক্ররেখাদ্বয় দ্বারা আবদ্ধ অংশের ক্ষেত্রফল কত বর্গ একক?",
        "options": ["$\\frac{1}{3}$", "$\\frac{2}{3}$", "$\\frac{1}{6}$", "$1$"],
        "answer": "A",
        "type_ref": "Type 3: দ্বৈত পরাবৃত্তের আবদ্ধ ক্ষেত্রফল শর্টকাট (DU Speed-Hack)",
        "trap_alert": "দ্বৈত পরাবৃত্ত $y^2 = 4ax$ ও $x^2 = 4by$ এর ক্ষেত্রফল $\\frac{16ab}{3}$। এখানে $4a = 1 \\implies a = 1/4$!",
        "speed_hack": "দ্বৈত পরাবৃত্তের আবদ্ধ ক্ষেত্রফল শর্টকাট: $y = x^2$ এবং $x = y^2$ এর আবদ্ধ ক্ষেত্রফল সর্বদা $\\frac{1}{3}$ বর্গ একক! (সূত্র: $\\frac{16(1/4)(1/4)}{3} = \\frac{1}{3}$)।",
        "explanation": "ক্ষেত্রফল $= \\int_0^1 (\\sqrt{x} - x^2) dx = [\\frac{2}{3}x^{3/2} - \\frac{x^3}{3}]_0^1 = \\frac{2}{3} - \\frac{1}{3} = \\frac{1}{3}$ বর্গ একক।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    },
    "pred_math_1st_10_18": {
        "stem": "যদি $\\int_0^4 f(x) dx = 12$ হয়, তবে $\\int_0^2 f(2x) dx$ এর মান কত?",
        "options": ["$6$", "$24$", "$12$", "$3$"],
        "answer": "A",
        "type_ref": "Type 2: নির্দিষ্ট যোগজের বাড়া-কমা নিয়ম (BARA-KOMA Rule) (DU Speed-Hack)",
        "trap_alert": "সহগ ২ দিয়ে গুণ করে ২৪ দাগানো! চলকের সহগ ২ দ্বারা ভাগ হবে!",
        "speed_hack": "নির্দিষ্ট যোগজের বাড়া-কমা নিয়ম (BARA-KOMA Rule): $\\int_a^b f(x) dx = k \\implies \\int_{a/m}^{b/m} f(mx) dx = \\frac{k}{m}$। এখানে $m = 2$, তাই মান $\\frac{12}{2} = 6$! মুখে মুখে ১ সেকেন্ডে!",
        "explanation": "ধরি $2x = u \\implies 2dx = du \\implies dx = du/2$। সীমা $x=0 \\to u=0$, $x=2 \\to u=4$। $\\int_0^4 f(u) \\frac{du}{2} = \\frac{12}{2} = 6$।",
        "is_du_repeated": True,
        "is_du_speed_hack": True,
        "source_tag": "🔥 DU Most Repeated | ⚡ DU Speed-Hack"
    }
}

def apply_updates():
    print("1. Updating Part 1 chapters...")
    p1_chaps = curate_math_p1.get_part1_chapters()
    updated_p1 = 0
    for ch in p1_chaps:
        for q in ch["predictors"]:
            qid = q["id"]
            if qid in DU_OVERHAUL_MAP:
                q.update(DU_OVERHAUL_MAP[qid])
                updated_p1 += 1
            else:
                # Ensure all math 1st paper questions have valid DU tags
                q.setdefault("is_du_repeated", True)
                q.setdefault("is_du_speed_hack", True)
                q.setdefault("source_tag", "🔥 DU Most Repeated | ⚡ DU Speed-Hack")
    print(f"  -> Applied {updated_p1} DU overrides in Part 1.")

    # Write back curate_math_p1.py
    with open("curate_math_p1.py", "w", encoding="utf-8") as f:
        f.write("#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n")
        f.write('"""curate_math_p1.py - Curated with DU Most Repeated & Speed-Hacks"""\n\n')
        f.write("true = True\nfalse = False\nnull = None\n\n")
        f.write("def get_part1_chapters():\n")
        f.write("    return " + json.dumps(p1_chaps, ensure_ascii=False, indent=4) + "\n")

    print("2. Updating Part 2 chapters...")
    p2_chaps = curate_math_p2.get_part2_chapters()
    updated_p2 = 0
    for ch in p2_chaps:
        for q in ch["predictors"]:
            qid = q["id"]
            if qid in DU_OVERHAUL_MAP:
                q.update(DU_OVERHAUL_MAP[qid])
                updated_p2 += 1
            else:
                q.setdefault("is_du_repeated", True)
                q.setdefault("is_du_speed_hack", True)
                q.setdefault("source_tag", "🔥 DU Most Repeated | ⚡ DU Speed-Hack")
    print(f"  -> Applied {updated_p2} DU overrides in Part 2.")

    # Write back curate_math_p2.py
    with open("curate_math_p2.py", "w", encoding="utf-8") as f:
        f.write("#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n")
        f.write('"""curate_math_p2.py - Curated with DU Most Repeated & Speed-Hacks"""\n\n')
        f.write("true = True\nfalse = False\nnull = None\n\n")
        f.write("def get_part2_chapters():\n")
        f.write("    return " + json.dumps(p2_chaps, ensure_ascii=False, indent=4) + "\n")

    print("3. Updating master_chapter_blueprint.json mega-types with DU Udvash hacks...")
    bp_files = [
        "src/data/master_chapter_blueprint.json",
        "admission_webapp/src/data/master_chapter_blueprint.json"
    ]

    BLUEPRINT_DU_HACKS = {
        "math_1st_01": [
            ("math_m01_t1", "ব্যতিক্রমী ম্যাট্রিক্সের নির্ণায়ক শূন্য ($|A| = 0$)। $2 \\times 2$ ম্যাট্রিক্সের ক্ষেত্রে $ad - bc = 0$। অজানা চলকের মান নির্ণয়ে অপশন টেস্ট বা মুখে মুখে ৩ সেকেন্ডে সমাধান।"),
            ("math_m01_t2", "$2 \\times 2$ ইনভার্স ম্যাট্রিক্স ট্রিক: প্রধান কর্ণের ভুক্তি বিনিময়, গৌণ কর্ণের চিহ্নের পরিবর্তন এবং নির্ণায়ক দ্বারা ভাগ। কর্ণ ম্যাট্রিক্স $\\text{diag}(a,b,c)$ এর বিপরীত $\\text{diag}(1/a, 1/b, 1/c)$।"),
            ("math_m01_t3", "গুণন আকার রুল: $(A^T + B) \\times C$ নির্ণয়ে $(m \\times n)^T = (n \\times m)$ ও যোগফলের আকার অপরিবর্তিত থাকে। $|A|=0$ ট্রিক: দুটি সারি বা কলাম অভিন্ন বা আনুপাতিক হলে বিস্তার ছাড়াই মান শূন্য।")
        ],
        "math_1st_02": [
            ("math_m02_t1", "স্কেলার অভিক্ষেপ: $X$ এর ওপর $Y$ এর অভিক্ষেপ $= (X \\cdot Y)/|X|$। ভেক্টর উপাংশ: $((A \\cdot B)/|B|^2)\\vec{B}$। ত্রিভুজ মধ্যবিন্দু উপপাদ্য: $\\vec{AB} + \\vec{AC} = 2\\vec{AD}$।"),
            ("math_m02_t2", "সমতলীয় ভেক্টর শর্টকাট: নির্ণায়ক $= 0$ অথবা রৈখিক নির্ভরশীলতা পরীক্ষণ ($V_3 = V_2 - V_1$)। সামান্তরিকের ক্ষেত্রফল $= |\\vec{a} \\times \\vec{b}|$ বা $\\frac{1}{2}|\\vec{d}_1 \\times \\vec{d}_2|$।")
        ],
        "math_1st_03": [
            ("math_m03_t1", "পোলার স্থানাঙ্ক সাইন টেস্ট: কোণের চতুর্ভাগ ($150^\\circ \\implies x<0, y>0$) দেখে ক্যালকুলেটর ছাড়া ১ সেকেন্ডে অপশন নির্বাচন। বিভক্তিকরণ স্টেপ-কাউন্টিং: অনুপাত $k = |y_1|:|y_2|$।"),
            ("math_m03_t2", "লম্ব রেখার ঢাল ইনভার্সন: $m_2 = -1/m_1$। চার রেখা বর্গের ব্লুপ্রিন্ট ($x=2, x=4, y=4, y=6$): কেন্দ্র $(3, 5)$, কর্ণ $2\\sqrt{2}$ একক। ছেদবিন্দুগামী রেখাগুচ্ছ: $L_1 + k L_2 = 0$।"),
            ("math_m03_t3", "ত্রিভুজ ক্ষেত্রফল মূলবিন্দু শিফটিং ট্রিক: একটি শীর্ষ $(0,0)$ করে নিয়ে $\\frac{1}{2}|x_1 y_2 - x_2 y_1|$ দিয়ে মুখে মুখে সমাধান।")
        ],
        "math_1st_04": [
            ("math_m04_t1", "মূলবিন্দুগামী অক্ষছেদী বৃত্ত: $x^2 + y^2 - hx - ky = 0$। কেন্দ্র $(h/2, k/2)$। পোলার রূপান্তর: $r^2 - 2r\\sin\\theta = 3 \\implies x^2 + (y-1)^2 = 4$।"),
            ("math_m04_t2", "অক্ষ স্পর্শের শর্ত: $x$-অক্ষ স্পর্শ করলে $g^2 = c$; $y$-অক্ষ স্পর্শ করলে $f^2 = c$। উভয় অক্ষ স্পর্শ করলে $g^2 = f^2 = c$।"),
            ("math_m04_t3", "স্পর্শকের মূল শর্ত $d = r$: লম্ব দূরত্ব ব্যাসার্ধের সমান ($c = \\pm a\\sqrt{1+m^2}$)। বৃত্তদ্বয়ের বহিঃস্পর্শ: $C_1 C_2 = r_1 + r_2$ এবং স্পর্শবিন্দুতে অন্তর্বিভক্ত অনুপাত $r_1 : r_2$।")
        ],
        "math_1st_05": [
            ("math_m05_t1", "নির্দিষ্ট বর্ণ স্থির বিন্যাস (GEOMETRY, CALCULUS): প্রান্তিক বর্ণ ফিক্সড রেখে মাঝের বর্ণগুলোর ফ্যাক্টোরিয়াল। পুনরাবৃত্তিহীন সংখ্যা গঠন: রেঞ্জ সীমাবদ্ধতায় ১ম অঙ্ক বাছাই ও পারমিউটেশন।"),
            ("math_m05_t2", "অ্যাট-লিস্ট-ওয়ান ট্রিক (At Least One Shortcut): অন্তত ১ জন অন্তর্ভুক্তির বাছাই $= \\text{মোট বাছাই} - \\text{শূন্য অন্তর্ভুক্তির বাছাই}$। তিন সেকেন্ডে মুখে মুখে সমাধান।")
        ],
        "math_1st_06": [
            ("math_m06_t1", "ঘড়ির কাঁটার কোণ: $\\theta = |30H - 5.5M|$। বৃত্তচাপ ও কোণ: $s = r\\theta$ (যেখানে $\\theta$ অবশ্যই রেডিয়ান)। চাকার ঘূর্ণন সংখ্যা $= \\text{দূরত্ব}/(2\\pi r)$।"),
            ("math_m06_t2", "দ্বিগুণ কোণ রূপান্তর: $\\frac{1-\\tan^2\\theta}{1+\\tan^2\\theta} = \\cos 2\\theta$। চতুর্ভাগে চিহ্নের পরিবর্তন এবং $\\sec^2\\theta - \\tan^2\\theta = 1$ গুণাত্মক বিপরীত ট্রিক।")
        ],
        "math_1st_07": [
            ("math_m07_t1", "ঢাবি স্পেশাল কোসাইন গুণন সিরিজ: $\\cos\\theta \\cos 2\\theta \\cos 4\\theta = \\frac{\\sin(8\\theta)}{8\\sin\\theta} = 1/8$। ট্যান রূপান্তর: $\\frac{\\cos\\theta + \\sin\\theta}{\\cos\\theta - \\sin\\theta} = \\tan(45^\\circ + \\theta)$।"),
            ("math_m07_t2", "সমকোণী ত্রিভুজ অ্যাঙ্গেল সাবস্টিটিউশন ট্রিক: $A = 90^\\circ, B = 60^\\circ, C = 30^\\circ$ ধরে $\\cos^2 A + \\cos^2 B + \\cos^2 C = 1$ তাৎক্ষণিক সমাধান। ৭.৬ রূপান্তর ফ্লো: $\\sin 2A + \\sin 2B + \\sin 2C = 4\\sin A \\sin B \\sin C$।")
        ],
        "math_1st_08": [
            ("math_m08_t1", "ভগ্নাংশ মূলের ডোমেন: $f(x) = \\frac{1}{\\sqrt{a^2-x^2}} \\implies (-a, a)$। দ্বিঘাত মূলের ডোমেন: $(x-a)(x-b) \\ge 0 \\implies$ প্রান্তিক দুই বাইরের অঞ্চল $(-\\infty, a] \\cup [b, \\infty)$।"),
            ("math_m08_t2", "ফাস্ট ইনভার্স ট্রিক: ইনভার্স সমীকরণ বের না করে সরাসরি $f(x) = k$ বসিয়ে সমাধান করুন। লিনিয়ার ভগ্নাংশ ইনভার্স: প্রধান কর্ণের সহগের চিহ্ন উল্টে অদলবদল।")
        ],
        "math_1st_09": [
            ("math_m09_t1", "ত্রিকোণমিতিক লিমিট শর্টকাট: $\\lim_{x\\to 0} \\frac{\\sin ax}{\\tan^{-1} bx} = \\frac{a}{b}$। ঋণাত্মক অসীম লিমিট ট্র্যাপ: $x \\to -\\infty$ হলে $\\sqrt{x^2} = |x| = -x$। L'Hôpital ট্রিগার: $0/0$ ও $\\infty/\\infty$।"),
            ("math_m09_t2", "অব্যক্ত ফাংশনের শর্টকাট: $\\frac{dy}{dx} = -\\frac{\\partial f / \\partial x}{\\partial f / \\partial y}$। সাকসেসিভ ডিফারেনশিয়েশন পাওয়ার ট্রিক: $(1-x^2)y_2 - x y_1 = 2 \\implies y = (\\cos^{-1}x)^2$।"),
            ("math_m09_t3", "গুরুমান ও লঘুমান নির্ণয়ে ১ম অন্তরক শূন্য ধরে টার্নিং পয়েন্ট নির্ণয়।")
        ],
        "math_1st_10": [
            ("math_m10_t1", "আদর্শ ফর্মুলা: $\\int \\frac{f'(x)}{\\sqrt{f(x)}} dx = 2\\sqrt{f(x)}$ এবং $\\int \\frac{dx}{x^2+a^2} = \\frac{1}{a}\\tan^{-1}\\frac{x}{a}$। $\\int e^x [f(x) + f'(x)] dx = e^x f(x)$।"),
            ("math_m10_t2", "নির্দিষ্ট যোগজের বাড়া-কমা রুল (BARA-KOMA Rule): $\\int_a^b f(x)dx = k \\implies \\int f(mx+c)dx = k/m$। মডুলাস গ্রাফ ট্রিক: $V$-আকৃতির গ্রাফের দুটি সমদ্বিবাহু ত্রিভুজের ক্ষেত্রফল।"),
            ("math_m10_t3", "পরাবৃত্ত ও সরলরেখা আবদ্ধ ক্ষেত্রফল: $\\frac{8}{3}\\frac{a^2}{m^3}$ ($y^2 = 4ax, y = mx$)। দুই পরাবৃত্ত আবদ্ধ ক্ষেত্রফল: $y=x^2$ ও $x=y^2$ এর জন্য সর্বদা $1/3$ বর্গ একক।")
        ]
    }

    for bpath in bp_files:
        if os.path.exists(bpath):
            with open(bpath, "r", encoding="utf-8") as f:
                bp_data = json.load(f)
            
            for ch in bp_data.get("chapters", []):
                cid = ch.get("id")
                if cid in BLUEPRINT_DU_HACKS:
                    types_to_update = {t[0]: t[1] for t in BLUEPRINT_DU_HACKS[cid]}
                    for mt in ch.get("mega_types", []):
                        tid = mt.get("type_id")
                        if tid in types_to_update:
                            mt["speed_elimination"] = types_to_update[tid]
            
            with open(bpath, "w", encoding="utf-8") as f:
                json.dump(bp_data, f, ensure_ascii=False, indent=2)
            print(f"  -> Successfully updated blueprint: {bpath}")



    # 5. Add DU Higher Math 1st Paper Flashcards
    print("5. Enriching Flashcards with DU 1st Paper Speed Hacks...")
    fc_files = [
        "src/data/flashcards.json",
        "admission_webapp/src/data/flashcards.json"
    ]
    du_math_flashcards = [
        {
            "id": "du_m1st_fc_01",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_01",
            "subject": "Higher Math",
            "topic": "ম্যাট্রিক্স গুণন মাত্রা শর্টকাট",
            "front": "যদি $A$ এর আকার $3 \\times 4$, $B$ এর আকার $4 \\times 3$ এবং $C$ এর আকার $3 \\times 2$ হয়, তবে $(A^T + B) \\times C$ এর আকার কত?",
            "back": "মান হিসাব না করেই মাত্রা বের করুন: $A^T$ হলো $4 \\times 3$, তাই $(A^T + B)$ হলো $4 \\times 3$। এবার $(4 \\times 3) \\times (3 \\times 2) = 4 \\times 2$!",
            "concept": "ম্যাট্রিক্স যোগে মাত্রা অপরিবর্তিত থাকে এবং গুণনে ভেতরের মাত্রা বিলুপ্ত হয়ে প্রান্তিক মাত্রায় গুণফল গঠিত হয়।",
            "hack": "ডাইমেনশন রুল: $(A^T + B)_{4 \\times 3} \\times C_{3 \\times 2} \\implies 4 \\times 2$!",
            "trap": "যোগের সময় আগে ট্রান্সপোজ করতে ভুলে যাওয়া।"
        },
        {
            "id": "du_m1st_fc_02",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_01",
            "subject": "Higher Math",
            "topic": "২×২ ইনভার্স ম্যাট্রিক্স ট্রিক",
            "front": "$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ এর ইনভার্স ম্যাট্রিক্স নির্ণয়ের দ্রুততম নিয়ম কী?",
            "back": "প্রধান কর্ণের ভুক্তি বিনিময় ($a \\leftrightarrow d$), গৌণ কর্ণের চিহ্ন পরিবর্তন ($-b, -c$), এবং পুরোটাকে নির্ণায়ক $(ad-bc)$ দিয়ে ভাগ।",
            "concept": "অ্যাডজয়েন্ট ম্যাট্রিক্স বের করার সময় কোফ্যাক্টর না বের করে ২×২ ম্যাট্রিক্সে সরাসরি স্থান ও চিহ্ন পরিবর্তন করা যায়।",
            "hack": "$A^{-1} = \\frac{1}{ad-bc}\\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$!",
            "trap": "নির্ণায়ক $|A| = 0$ হলে বিপরীত ম্যাট্রিক্স বিদ্যমান থাকে না (ব্যতিক্রমী ম্যাট্রিক্স)।"
        },
        {
            "id": "du_m1st_fc_03",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_01",
            "subject": "Higher Math",
            "topic": "ভেক্টর ত্রিভুজ মধ্যবিন্দু উপপাদ্য",
            "front": "$\\triangle ABC$-এর $BC$ বাহুর মধ্যবিন্দু $D$ হলে $\\vec{AB} + \\vec{AC}$ সমান কত?",
            "back": "শীর্ষগামী মধ্যমার দ্বিগুণের সমান: $\\vec{AB} + \\vec{AC} = 2\\vec{AD}$।",
            "concept": "ভেক্টর ত্রিভুজ সূত্রানুযায়ী $\\vec{AB} = \\vec{AD} + \\vec{DB}$ এবং $\\vec{AC} = \\vec{AD} + \\vec{DC}$। যেহেতু $\\vec{DB} + \\vec{DC} = \\vec{0}$, তাই যোগফল $2\\vec{AD}$।",
            "hack": "সাধারণ শীর্ষ হতে বাহুদ্বয়ের ভেক্টর সমষ্টি = মধ্যমার দ্বিগুণ ($2\\vec{AD}$)!",
            "trap": "চিহ্নে ভুল করে বিয়োগ দাগানো।"
        },
        {
            "id": "du_m1st_fc_04",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_01",
            "subject": "Higher Math",
            "topic": "ভেক্টরের স্কেলার অভিক্ষেপ বনাম উপাংশ",
            "front": "$\\vec{A}$ এর ওপর $\\vec{B}$ এর স্কেলার অভিক্ষেপ এবং ভেক্টর উপাংশের সূত্র কী?",
            "back": "স্কেলার অভিক্ষেপ $= \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{A}|}$ (একটি সংখ্যা); ভেক্টর উপাংশ $= \\left(\\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{A}|^2}\\right)\\vec{A}$ (একটি ভেক্টর)।",
            "concept": "অভিক্ষেপ হলো ছায়ার দৈর্ঘ্য, আর উপাংশ হলো ঐ দিকের ভেক্টর রূপ। যার ওপর অভিক্ষেপ তার মান দিয়ে ভাগ।",
            "hack": "উপাংশ = অভিক্ষেপ $\\times \\hat{A}$!",
            "trap": "যার ওপর অভিক্ষেপ তার মান দ্বারা ভাগ না করে অন্য ভেক্টরের মান দিয়ে ভাগ করা।"
        },
        {
            "id": "du_m1st_fc_05",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_01",
            "subject": "Higher Math",
            "topic": "সমতলীয় ভেক্টর রৈখিক নির্ভরশীলতা",
            "front": "তিনটি ভেক্টর সমতলীয় (Coplanar) কিনা ক্যালকুলেটর ছাড়া কীভাবে যাচাই করবেন?",
            "back": "সহগগুলোর নির্ণায়ক $= 0$ হওয়া আবশ্যক। অথবা যেকোনো একটি ভেক্টর বাকি দুটির যোগফল বা বিয়োগফল কিনা পরীক্ষা করুন ($V_3 = V_2 - V_1$)।",
            "concept": "সমতলীয় ভেক্টরসমূহ পরস্পর রৈখিকভাবে নির্ভরশীল (Linearly Dependent) হয়।",
            "hack": "$V_3 = V_2 - V_1$ মেলানো গেলে কোনো বিস্তার ছাড়াই ৩ সেকেন্ডে সহগের মান বের করা যায়!",
            "trap": "ডট ও ক্রস গুণনের মিশ্রণে শূন্য না এসে অন্য মান আসলে তা সমতলীয় নয়।"
        },
        {
            "id": "du_m1st_fc_06",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_01",
            "subject": "Higher Math",
            "topic": "পোলার স্থানাঙ্ক সাইন টেস্ট",
            "front": "পোলার কোণ $\\theta = 150^\\circ$ হলে কার্তেসীয় স্থানাঙ্কের চিহ্নের বৈশিষ্ট্য কী?",
            "back": "কোণ $150^\\circ$ দ্বিতীয় চতুর্ভাগে অবস্থিত $\\implies x < 0$ এবং $y > 0$।",
            "concept": "পোলার রূপান্তরের ক্ষেত্রে অপশনের সাইন দেখেই ৭৫% ভুল অপশন বাদ দেওয়া যায়।",
            "hack": "২য় চতুর্ভাগ $\\implies (-x, +y)$; অপশনে কেবল একটি ঋণাত্মক ও ধনাত্মক জোড়া থাকলে ১ সেকেন্ডে টিক!",
            "trap": "ক্যালকুলেটরে ডিগ্রি মোডের জায়গায় রেডিয়ান মোড রাখা।"
        },
        {
            "id": "du_m1st_fc_07",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_01",
            "subject": "Higher Math",
            "topic": "ত্রিভুজ ক্ষেত্রফল মূলবিন্দু শিফটিং",
            "front": "$(x_1, y_1), (x_2, y_2), (x_3, y_3)$ ত্রিভুজের ক্ষেত্রফল নির্ণয়ের দ্রুততম শর্টকাট কী?",
            "back": "যেকোনো একটি শীর্ষকে $(0,0)$ করতে তার মান বাকি দুটি শীর্ষ থেকে বিয়োগ করুন $\\to (0,0), (x_2', y_2'), (x_3', y_3')$। ক্ষেত্রফল $= \\frac{1}{2}|x_2' y_3' - x_3' y_2'|$।",
            "concept": "স্থানাঙ্ক মূলবিন্দুতে স্থানান্তর করলেও আবদ্ধ ক্ষেত্রের ক্ষেত্রফল অপরিবর্তিত থাকে।",
            "hack": "৩×৩ নির্ণায়ক না লিখে সরাসরি কোণাকুণি গুণ বিয়োগ: $\\frac{1}{2}|x_1 y_2 - x_2 y_1|$!",
            "trap": "বিয়োগ করার সময় উভয় স্থানাঙ্ক থেকে সঠিকভাবে সমপরিমাণ না বাদ দেওয়া।"
        },
        {
            "id": "du_m1st_fc_08",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_02",
            "subject": "Higher Math",
            "topic": "বৃত্তের অক্ষ স্পর্শ ও স্পর্শক শর্ত",
            "front": "বৃত্ত $x$-অক্ষ ও $y$-অক্ষকে স্পর্শ করার শর্ত এবং রেখা স্পর্শকের শর্ত কী?",
            "back": "$x$-অক্ষ স্পর্শে $g^2 = c$; $y$-অক্ষ স্পর্শে $f^2 = c$। সরলরেখা স্পর্শকে কেন্দ্র হতে লম্ব দূরত্ব ব্যাসার্ধের সমান ($d = r$) $\\implies c = \\pm a\\sqrt{1+m^2}$।",
            "concept": "অক্ষ স্পর্শকালে অক্ষের ছেদাংশ শূন্য হয় ($2\\sqrt{g^2-c}=0$)।",
            "hack": "$x$-অক্ষে স্পর্শ $\\implies g^2 = c$; $y$-অক্ষে স্পর্শ $\\implies f^2 = c$!",
            "trap": "সাধারণ সমীকরণে $2g$ ও $2f$ এর জায়গায় সরাসরি সহগের বর্গ করা।"
        },
        {
            "id": "du_m1st_fc_09",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_02",
            "subject": "Higher Math",
            "topic": "অ্যাট-লিস্ট-ওয়ান সমাবেশ ট্রিক",
            "front": "'অন্তত ১ জন' অন্তর্ভুক্ত করে দল গঠনের দ্রুততম কৌশল কী?",
            "back": "অন্তত ১ জন $= \\text{মোট দল} - \\text{কাউকে না নিয়ে গঠিত দল}$।",
            "concept": "পরিপূরক নীতি (Complementary Counting) প্রয়োগ করলে বহু শর্তযুক্ত সমীকরণ একটি বিয়োগে নেমে আসে।",
            "hack": "$^8C_4 - ^4C_4 = 70 - 1 = 69$! ৩ সেকেন্ডে সমাধান!",
            "trap": "১, ২, ৩, ৪ জনের আলাদা আলাদা সমাবেশ বের করে যোগ করতে গিয়ে সময় অপচয় করা।"
        },
        {
            "id": "du_m1st_fc_10",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_02",
            "subject": "Higher Math",
            "topic": "ঢাবি স্পেশাল কোসাইন গুণন ধারা",
            "front": "$\\cos 20^\\circ \\cos 40^\\circ \\cos 80^\\circ$ এর মান কত?",
            "back": "সরাসরি মান $\\frac{1}{8}$। সাধারণ সূত্র: $\\cos\\theta \\cos 2\\theta \\dots \\cos(2^n\\theta) = \\frac{\\sin(2^{n+1}\\theta)}{2^{n+1}\\sin\\theta}$।",
            "concept": "দ্বিগুণ কোণের গুণন ধারায় প্রতিটি পদ পূর্ববর্তী কোণের দ্বিগুণ হলে এই অনুসিদ্ধান্ত প্রযোজ্য।",
            "hack": "কোণ ২০, ৪০, ৮০ হলে উত্তর ফিক্সড: $1/8$!",
            "trap": "সাইন ধারার সাথে গোলমাল করা; $\\sin 20^\\circ \\sin 40^\\circ \\sin 80^\\circ = \\frac{\\sqrt{3}}{8}$।"
        },
        {
            "id": "du_m1st_fc_11",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_02",
            "subject": "Higher Math",
            "topic": "সমকোণী ত্রিভুজ কোণ সাবস্টিটিউশন",
            "front": "$\\triangle ABC$-তে $\\cos^2 A + \\cos^2 B + \\cos^2 C + 2\\cos A \\cos B \\cos C$ এর মান কত?",
            "back": "মান সর্বদা $1$। শর্টকাট: $A = 90^\\circ, B = 60^\\circ, C = 30^\\circ$ ধরুন।",
            "concept": "ত্রিভুজের অভেদাবলী যেকোনো ত্রিভুজের জন্য সত্য, তাই সুবিধাজনক সমকোণী ত্রিভুজ বেছে নিয়ে সরাসরি মান বের করা যায়।",
            "hack": "$A = 90^\\circ$ ধরলে $\\cos 90^\\circ = 0$ হয়ে জটিল পদগুলো শূন্য হয়ে যায়: $0 + 1/4 + 3/4 = 1$!",
            "trap": "কোণ তিনটির যোগফল $180^\\circ$ না রেখে произвольный কোণ ধরা।"
        },
        {
            "id": "du_m1st_fc_12",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_03",
            "subject": "Higher Math",
            "topic": "ফাস্ট ইনভার্স ফাংশন ট্রিক",
            "front": "$f(x) = 3x - 5$ হলে $f^{-1}(4)$ এর মান বের করার দ্রুততম উপায় কী?",
            "back": "ইনভার্স ফাংশন না বের করে সরাসরি $f(x) = 4$ বসিয়ে সমাধান করুন: $3x - 5 = 4 \\implies x = 3$!",
            "concept": "$f^{-1}(y) = x \\iff f(x) = y$। ইনভার্স প্রক্রিয়ার সংজ্ঞা প্রয়োগে সমীকরণ উল্টানোর প্রয়োজন হয় না।",
            "hack": "$f^{-1}(k) \\implies f(x) = k$ সমাধান করুন ৩ সেকেন্ডে!",
            "trap": "পুরো সমীকরণ প্রতিস্থাপন করে $f^{-1}(x) = (x+5)/3$ বের করতে অতিরিক্ত সময় ব্যয় করা।"
        },
        {
            "id": "du_m1st_fc_13",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_03",
            "subject": "Higher Math",
            "topic": "অব্যক্ত ফাংশনের অন্তরক শর্টকাট",
            "front": "$f(x, y) = 0$ অব্যক্ত ফাংশনের $\\frac{dy}{dx}$ বের করার সুপার ট্রিক কী?",
            "back": "$\\frac{dy}{dx} = -\\frac{\\partial f / \\partial x}{\\partial f / \\partial y}$ (লবে $y$ কে ধ্রুবক ধরে $x$ এর সাপেক্ষে এবং হরে $x$ কে ধ্রুবক ধরে $y$ এর সাপেক্ষে আংশিক অন্তরীকরণ)।",
            "concept": "দ্বি-চলকের চেইন রুল প্রয়োগে প্রথাগত লাইনের পর লাইন অন্তরীকরণ এক লাইনে শেষ হয়।",
            "hack": "সামনে মাইনাস দিন, লবে $x$ এর ডেরিভেটিভ / হরে $y$ এর ডেরিভেটিভ!",
            "trap": "সামনের মাইনাস চিহ্ন দিতে ভুলে যাওয়া।"
        },
        {
            "id": "du_m1st_fc_14",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_03",
            "subject": "Higher Math",
            "topic": "সাকসেসিভ ডিফারেনশিয়েশন পাওয়ার ট্রিক",
            "front": "$(1-x^2)y_2 - x y_1 = 2$ সমীকরণটি কোন ফাংশন থেকে আসে?",
            "back": "$y = (\\cos^{-1}x)^2$ অথবা $y = (\\sin^{-1}x)^2$। ডানপক্ষে ২ থাকা মানে ইনভার্স ফাংশনের ঘাত ছিল ২!",
            "concept": "$y = \\cos^{-1}x$ হলে ডানপক্ষ শূন্য হয়; ঘাত ২ হলে ডানপক্ষে ২ আসে।",
            "hack": "ডানপক্ষে $2 \\implies$ ঘাত ২! অপশনে $(\\cos^{-1}x)^2$ দেখে সরাসরি টিক!",
            "trap": "$y = \\cos^{-1}x$ এর সাথে ঘাত ২ এর পার্থক্য না বোঝা।"
        },
        {
            "id": "du_m1st_fc_15",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_03",
            "subject": "Higher Math",
            "topic": "নির্দিষ্ট যোগজের বাড়া-কমা রুল (BARA-KOMA Rule)",
            "front": "$\\int_0^4 f(x) dx = 12$ হলে $\\int_0^2 f(2x) dx$ এর মান কত?",
            "back": "চলকের সহগ ২ দ্বারা ভাগ হবে: $\\frac{12}{2} = 6$!",
            "concept": "সীমা এবং চলকের স্কেলিং রুল: $\\int_a^b f(x)dx = k \\implies \\int_{a/m}^{b/m} f(mx)dx = \\frac{k}{m}$।",
            "hack": "ভেতরে $m$ দিয়ে গুণ হলে মোট মান $m$ দিয়ে ভাগ হয়!",
            "trap": "উত্তরে ২ দিয়ে গুণ করে ২৪ দাগানো।"
        },
        {
            "id": "du_m1st_fc_16",
            "deck_id": "du_speed",
            "deck_title": "🎯 DU No-Calculator Speed Tricks",
            "week_id": "week_03",
            "subject": "Higher Math",
            "topic": "পরাবৃত্ত ও সরলরেখার সীমাবদ্ধ ক্ষেত্রফল",
            "front": "$y^2 = 4ax$ এবং $y = mx$ দ্বারা সীমাবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত?",
            "back": "$\\text{Area} = \\frac{8}{3}\\frac{a^2}{m^3}$। আর দুই পরাবৃত্ত $y = x^2, x = y^2$ এর আবদ্ধ ক্ষেত্রফল সর্বদা $1/3$!",
            "concept": "আর্কিমিডিসের পরাবৃত্ত ক্ষেত্রফল অনুসিদ্ধান্তের ক্যালকুলাস রূপ।",
            "hack": "$y^2 = 4x$ ও $y = x$ এর ক্ষেত্রফল $= \\frac{8}{3}\\frac{1^2}{1^3} = \\frac{8}{3}$ বর্গ একক!",
            "trap": "$x^2 = 4ay$ এবং $y = mx$ হলে ক্ষেত্রফল $\\frac{8}{3}a^2 m^3$ হয়।"
        }
    ]

    for fpath in fc_files:
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                all_fc = json.load(f)
            # Remove any existing duplicates of these IDs
            existing_ids = {c["id"] for c in du_math_flashcards}
            filtered_fc = [c for c in all_fc if c["id"] not in existing_ids]
            filtered_fc.extend(du_math_flashcards)
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(filtered_fc, f, ensure_ascii=False, indent=2)
            print(f"  -> Added {len(du_math_flashcards)} flashcards to {fpath} (Total now: {len(filtered_fc)})")

if __name__ == "__main__":
    apply_updates()
