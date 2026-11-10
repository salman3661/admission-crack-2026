#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curate_math_p4b.py: Chapters math_2nd_08, math_2nd_09, math_2nd_10
"""

def get_math_2nd_08():
    """স্থিতিবিদ্যা (18 MCQs)"""
    return {
        "chapter_id": "math_2nd_08",
        "chapter_title": "স্থিতিবিদ্যা",
        "subject": "Higher Mathematics",
        "paper": "2nd",
        "chapter_no": 8,
        "predictors": [
            {
                "id": "pred_math_2nd_08_01",
                "stem": "কোনো বিন্দুতে ক্রিয়ারত দুটি সমান বল $P$ এর মধ্যবর্তী কোণ কত হলে তাদের লব্ধির মানও $P$ হবে?",
                "options": ["$120^\\circ$", "$60^\\circ$", "$90^\\circ$", "$180^\\circ$"],
                "answer": "A",
                "type_ref": "দুটি সমান বলের লব্ধি",
                "trap_alert": "লব্ধি সমান হলে কোণ $120^\\circ$।",
                "speed_hack": "বল সমান ও লব্ধি সমান $\implies \\alpha = 120^\\circ$।",
                "explanation": "$P^2 = 2P^2(1 + \\cos\\alpha) \implies 1 + \\cos\\alpha = 1/2 \implies \\cos\\alpha = -1/2 \implies \\alpha = 120^\\circ$।"
            },
            {
                "id": "pred_math_2nd_08_02",
                "stem": "একটি বিন্দুতে ক্রিয়াশীল তিনটি বলের সাম্যাবস্থার জন্য লামির উপপাদ্য কোনটি?",
                "options": [
                    "$\\frac{P}{\\sin\\alpha} = \\frac{Q}{\\sin\\beta} = \\frac{R}{\\sin\\gamma}$",
                    "$\\frac{P}{\\cos\\alpha} = \\frac{Q}{\\cos\\beta} = \\frac{R}{\\cos\\gamma}$",
                    "$P\\sin\\alpha = Q\\sin\\beta = R\\sin\\gamma$",
                    "$\\frac{P}{\\sin\\beta} = \\frac{Q}{\\sin\\alpha} = \\frac{R}{\\sin\\gamma}$"
                ],
                "answer": "A",
                "type_ref": "লামির উপপাদ্যের বিবৃতি",
                "trap_alert": "প্রতিটি বল অপর দুটির মধ্যবর্তী কোণের সাইনের সমানুপাতিক।",
                "speed_hack": "Lami: $\\frac{F_i}{\\sin\\theta_i} = \\text{ধ্রুবক}$।",
                "explanation": "লামির উপপাদ্য অনুসারে $\\frac{P}{\\sin\\alpha} = \\frac{Q}{\\sin\\beta} = \\frac{R}{\\sin\\gamma}$।"
            },
            {
                "id": "pred_math_2nd_08_03",
                "stem": "দুটি বলের সর্বোচ্চ ও সর্বনিম্ন লব্ধির মান যথাক্রমে $14\\text{ N}$ এবং $2\\text{ N}$ হলে বল দুটির মান কত?",
                "options": ["$8\\text{ N}$ এবং $6\\text{ N}$", "$10\\text{ N}$ এবং $4\\text{ N}$", "$9\\text{ N}$ এবং $5\\text{ N}$", "$12\\text{ N}$ এবং $2\\text{ N}$"],
                "answer": "A",
                "type_ref": "সর্বোচ্চ ও সর্বনিম্ন লব্ধি",
                "trap_alert": "$P+Q = 14, P-Q = 2$।",
                "speed_hack": "$P = (14+2)/2 = 8, Q = (14-2)/2 = 6$।",
                "explanation": "$P + Q = 14$ এবং $P - Q = 2$। সমাধান করে $P = 8\\text{ N}$ এবং $Q = 6\\text{ N}$।"
            },
            {
                "id": "pred_math_2nd_08_04",
                "stem": "একই বিন্দুতে ক্রিয়ারত $3\\text{ N}$ এবং $4\\text{ N}$ মানের দুটি বলের মধ্যবর্তী কোণ $90^\\circ$ হলে লব্ধির মান কত?",
                "options": ["$5\\text{ N}$", "$7\\text{ N}$", "$1\\text{ N}$", "$25\\text{ N}$"],
                "answer": "A",
                "type_ref": "পরস্পর লম্ব বলের লব্ধি",
                "trap_alert": "$R = \\sqrt{3^2 + 4^2} = 5$।",
                "speed_hack": "পিথাগোরাস: $3, 4, 5$।",
                "explanation": "$R = \\sqrt{3^2 + 4^2 + 2(3)(4)\\cos 90^\\circ} = \\sqrt{25} = 5\\text{ N}$।"
            },
            {
                "id": "pred_math_2nd_08_05",
                "stem": "দুটি সমমুখী সমান্তরাল বল $P$ এবং $Q$ যথাক্রমে $A$ ও $B$ তে ক্রিয়ারত। লব্ধি $C$ তে ক্রিয়া করলে কোনটি সঠিক?",
                "options": ["$P \\cdot AC = Q \\cdot BC$", "$P \\cdot BC = Q \\cdot AC$", "$\\frac{P}{AC} = \\frac{Q}{BC}$", "$P + AC = Q + BC$"],
                "answer": "A",
                "type_ref": "সমান্তরাল বলের লব্ধির অবস্থান",
                "trap_alert": "$C$ বিন্দুর সাপেক্ষে মোমেন্ট সমান: $P \\cdot AC = Q \\cdot BC$।",
                "speed_hack": "$P \\cdot AC = Q \\cdot BC$।",
                "explanation": "সমান্তরাল বলের সূত্র অনুসারে লব্ধির ক্রিয়াবিন্দুতে $P \\cdot AC = Q \\cdot BC$।"
            },
            {
                "id": "pred_math_2nd_08_06",
                "stem": "কোনো বিন্দুতে ক্রিয়াশীল $P$ এবং $2P$ মানের বলদ্বয়ের লব্ধি $P$ বলটির ওপর লম্ব হলে মধ্যবর্তী কোণ কত?",
                "options": ["$120^\\circ$", "$150^\\circ$", "$135^\\circ$", "$90^\\circ$"],
                "answer": "A",
                "type_ref": "লব্ধি ক্ষুদ্রতর বলের ওপর লম্ব",
                "trap_alert": "$P + 2P\\cos\\alpha = 0 \implies \\cos\\alpha = -1/2$।",
                "speed_hack": "$\\cos\\alpha = -P/(2P) = -1/2 \implies 120^\\circ$।",
                "explanation": "$\\tan 90^\\circ = \\infty \implies P + 2P\\cos\\alpha = 0 \implies \\cos\\alpha = -1/2 \implies \\alpha = 120^\\circ$।"
            },
            {
                "id": "pred_math_2nd_08_07",
                "stem": "একটি বিন্দুতে ক্রিয়ারত তিনটি বল $P, Q, R$ সাম্যাবস্থায় আছে এবং মধ্যবর্তী কোণগুলো পরস্পর সমান হলে বলগুলোর অনুপাত কত?",
                "options": ["$1 : 1 : 1$", "$1 : 2 : 3$", "$\\sqrt{3} : 1 : 2$", "$1 : \\sqrt{2} : 1$"],
                "answer": "A",
                "type_ref": "সমান কোণে সাম্যাবস্থা",
                "trap_alert": "কোণগুলো $120^\\circ$ করে।",
                "speed_hack": "লামির সূত্রে হর সমান $\implies P = Q = R$।",
                "explanation": "প্রতিটি কোণ $120^\\circ$। লামির উপপাদ্য মতে $\\frac{P}{\\sin 120^\\circ} = \\frac{Q}{\\sin 120^\\circ} = \\frac{R}{\\sin 120^\\circ} \implies P : Q : R = 1 : 1 : 1$।"
            },
            {
                "id": "pred_math_2nd_08_08",
                "stem": "দুটি বিপরীতমুখী সমান্তরাল বল $12\\text{ N}$ এবং $8\\text{ N}$ এর লব্ধির মান কত?",
                "options": ["$4\\text{ N}$", "$20\\text{ N}$", "$96\\text{ N}$", "$\\sqrt{208}\\text{ N}$"],
                "answer": "A",
                "type_ref": "বিসদৃশ সমান্তরাল বলের লব্ধি",
                "trap_alert": "বিসদৃশ বলের লব্ধি $|P - Q|$।",
                "speed_hack": "$12 - 8 = 4\\text{ N}$।",
                "explanation": "বিসদৃশ সমান্তরাল বলের লব্ধি $R = |P - Q| = 12 - 8 = 4\\text{ N}$।"
            },
            {
                "id": "pred_math_2nd_08_09",
                "stem": "একটি বল যুগলের ভ্রামক কিসের ওপর নির্ভর করে না?",
                "options": ["ঘূর্ণন অক্ষ বা মূলবিন্দুর অবস্থানের ওপর", "বলদ্বয়ের মানের ওপর", "বলদ্বয়ের মধ্যবর্তী লম্ব দূরত্বের ওপর", "বলের অভিমুখের ওপর"],
                "answer": "A",
                "type_ref": "যুগলের ভ্রামকের বৈশিষ্ট্য",
                "trap_alert": "যুগলের ভ্রামক সমতলের যে কোনো বিন্দুর সাপেক্ষে ধ্রুবক।",
                "speed_hack": "বিন্দুর অবস্থানের ওপর নিরপেক্ষ।",
                "explanation": "যুগলের ভ্রামক $M = F \\times d$, যা মূলবিন্দু বা ঘূর্ণন অক্ষের অবস্থানের ওপর নির্ভর করে না।"
            },
            {
                "id": "pred_math_2nd_08_10",
                "stem": "$P$ এবং $Q$ মানের দুটি বলের স্থান বিনিময় করলে লব্ধির দিক পরিবর্তিত হয় না। কোনটি সত্য?",
                "options": ["$P = Q$", "$\\alpha = 90^\\circ$", "$P + Q = 0$", "$\\alpha = 180^\\circ$"],
                "answer": "A",
                "type_ref": "লব্ধির প্রতিসাম্য ধর্ম",
                "trap_alert": "বলদ্বয় সমান হলেই দিক সমদ্বিখণ্ডক বরাবর অপরিবর্তিত থাকে।",
                "speed_hack": "$P = Q$।",
                "explanation": "$P = Q$ হলে লব্ধি মধ্যবর্তী কোণের সমদ্বিখণ্ডক বরাবর ক্রিয়া করে, তাই স্থান পরিবর্তনে দিক বদলায় না।"
            },
            {
                "id": "pred_math_2nd_08_11",
                "stem": "একটি কণার ওপর ক্রিয়ারত $5\\text{ N}, 12\\text{ N}, 13\\text{ N}$ বল তিনটি সাম্যাবস্থায় থাকলে প্রথম দুটি বলের মধ্যবর্তী কোণ কত?",
                "options": ["$90^\\circ$", "$60^\\circ$", "$120^\\circ$", "$180^\\circ$"],
                "answer": "A",
                "type_ref": "বল ত্রিভুজ ও সমকোণী সাম্যাবস্থা",
                "trap_alert": "$5^2 + 12^2 = 13^2 \\implies R = 13$ হতে কোণ $90^\\circ$ হতে হবে।",
                "speed_hack": "পিথাগোরাস সম্পর্ক $\implies \\alpha = 90^\\circ$।",
                "explanation": "$5^2 + 12^2 + 2(5)(12)\\cos\\alpha = 13^2 \implies 169 + 120\\cos\\alpha = 169 \implies \\cos\\alpha = 0 \implies \\alpha = 90^\\circ$।"
            },
            {
                "id": "pred_math_2nd_08_12",
                "stem": "$AB$ একটি সুষম তক্তা যার ওজন $W$ এবং দৈর্ঘ্য $4\\text{ m}$। তক্তাটির ভরকেন্দ্র কোথায় অবস্থিত?",
                "options": ["মধ্যবিন্দুতে (প্রান্ত হতে $2\\text{ m}$ দূরে)", "প্রান্ত হতে $1\\text{ m}$ দূরে", "প্রান্ত হতে $3\\text{ m}$ দূরে", "যে কোনো অবস্থানে"],
                "answer": "A",
                "type_ref": "ভরকেন্দ্রের অবস্থান",
                "trap_alert": "সুষম বস্তুর ভরকেন্দ্র জ্যামিতিক মধ্যবিন্দুতে থাকে।",
                "speed_hack": "$L/2 = 2\\text{ m}$।",
                "explanation": "সুষম কাঠামোর ভর সুষমভাবে বিন্যস্ত থাকে বিধায় এর ভরকেন্দ্র মধ্যবিন্দুতে ($2\\text{ m}$) অবস্থান করে।"
            },
            {
                "id": "pred_math_2nd_08_13",
                "stem": "একটি বিন্দুতে ক্রিয়াশীল দুটি বলের বৃহত্তম লব্ধি ক্ষুদ্রতম লব্ধির তিনগুণ হলে বলদ্বয়ের অনুপাত কত?",
                "options": ["$2 : 1$", "$3 : 1$", "$4 : 1$", "$3 : 2$"],
                "answer": "A",
                "type_ref": "লব্ধির গুণিতক হতে বলের অনুপাত",
                "trap_alert": "$P + Q = 3(P - Q) \implies 2P = 4Q$।",
                "speed_hack": "$\\frac{P}{Q} = \\frac{3+1}{3-1} = \\frac{2}{1}$।",
                "explanation": "$P + Q = 3(P - Q) \implies P + Q = 3P - 3Q \implies 2P = 4Q \implies P/Q = 2/1$।"
            },
            {
                "id": "pred_math_2nd_08_14",
                "stem": "$P$ এবং $Q$ বলদ্বয়ের লব্ধি $R$। $Q$ কে দ্বিগুণ করলে লব্ধি দ্বিগুণ হয় এবং দিক উল্টালেও দ্বিগুণ হয়। $P : Q$ কত?",
                "options": ["$\\sqrt{2} : \\sqrt{3}$", "$1 : 1$", "$2 : 3$", "$\\sqrt{3} : \\sqrt{2}$"],
                "answer": "A",
                "type_ref": "বল ও লব্ধির সম্পর্ক প্রতিপাদন",
                "trap_alert": "ভার্সিটি ও ইঞ্জিনিয়ারিং স্ট্যান্ডার্ড প্রবলেম।",
                "speed_hack": "$P : Q = \\sqrt{2} : \\sqrt{3}$।",
                "explanation": "শর্তসমূহ সমাধান করলে পাওয়া যায় $P^2 / Q^2 = 2/3 \implies P : Q = \\sqrt{2} : \\sqrt{3}$।"
            },
            {
                "id": "pred_math_2nd_08_15",
                "stem": "$60^\\circ$ কোণে ক্রিয়ারত $P$ ও $Q$ বলদ্বয়ের লব্ধি $\\sqrt{3}Q$ হলে, $P$ ও $Q$ এর সম্পর্ক কোনটি?",
                "options": ["$P = Q$", "$P = 2Q$", "$Q = 2P$", "$P = 3Q$"],
                "answer": "A",
                "type_ref": "নির্দিষ্ট কোণে বলের সম্পর্ক",
                "trap_alert": "$3Q^2 = P^2 + Q^2 + PQ$।",
                "speed_hack": "$P^2 + PQ - 2Q^2 = 0 \implies (P-Q)(P+2Q)=0 \implies P = Q$।",
                "explanation": "$3Q^2 = P^2 + Q^2 + 2PQ(1/2) \implies P^2 + PQ - 2Q^2 = 0 \implies P = Q$।"
            },
            {
                "id": "pred_math_2nd_08_16",
                "stem": "একটি সমবাহু ত্রিভুজের তিনটি শীর্ষবিন্দুতে তিনটি সমান সদৃশ সমান্তরাল বল $P$ ক্রিয়ারত। লব্ধির ক্রিয়াবিন্দু কোনটি?",
                "options": ["ত্রিভুজটির ভরকেন্দ্র (Centroid)", "ত্রিভুজটির পরিকেন্দ্র (Circumcenter)", "ত্রিভুজটির অন্তঃকেন্দ্র (Incenter)", "একটি শীর্ষবিন্দু"],
                "answer": "A",
                "type_ref": "বহুভুজের শীর্ষে সমান্তরাল বল",
                "trap_alert": "সমান বলের ক্ষেত্রে লব্ধি ভরকেন্দ্রে অবস্থান করে।",
                "speed_hack": "লব্ধি ভরকেন্দ্রে (মান $3P$)।",
                "explanation": "শীর্ষবিন্দুতে সমান বল প্রযুক্ত হলে লব্ধি সর্বদা ত্রিভুজটির ভরকেন্দ্রে ক্রিয়া করে।"
            },
            {
                "id": "pred_math_2nd_08_17",
                "stem": "দুটি বলের লব্ধির মান সর্বোচ্চ হয় যখন তাদের অন্তর্ভুক্ত কোণ—",
                "options": ["$0^\\circ$", "$90^\\circ$", "$180^\\circ$", "$45^\\circ$"],
                "answer": "A",
                "type_ref": "সর্বোচ্চ লব্ধির কোণ",
                "trap_alert": "কোণ $0^\\circ$ হলে $\\cos\\alpha = 1$।",
                "speed_hack": "$\\alpha = 0^\\circ \implies R_{\\max} = P + Q$।",
                "explanation": "$\\cos\\alpha$ এর সর্বোচ্চ মান $+1$ যখন $\\alpha = 0^\\circ$। তখন লব্ধি সর্বোচ্চ $P + Q$ হয়।"
            },
            {
                "id": "pred_math_2nd_08_18",
                "stem": "কোনো বিন্দুতে ক্রিয়াশীল তিনটি বল $\\vec{P}, \\vec{Q}, \\vec{R}$ সাম্যাবস্থায় থাকলে নিচের কোনটি সত্য?",
                "options": ["$\\vec{P} + \\vec{Q} + \\vec{R} = \\vec{0}$", "$\\vec{P} + \\vec{Q} = \\vec{R}$", "$P + Q + R = 0$", "$\\vec{P} \\times \\vec{Q} = \\vec{R}$"],
                "answer": "A",
                "type_ref": "ভেক্টর রূপে সাম্যাবস্থার শর্ত",
                "trap_alert": "লব্ধি ভেক্টর শূন্য ভেক্টর হবে।",
                "speed_hack": "$\\vec{P} + \\vec{Q} + \\vec{R} = \\vec{0}$।",
                "explanation": "কণার সাম্যাবস্থার ভেক্টরীয় শর্ত হলো বলসমূহের ভেক্টর যোগফল শূন্য ভেক্টর হতে হবে।"
            }
        ]
    }

def get_math_2nd_09():
    """সমতলে বস্তুকণার গতি (18 MCQs)"""
    return {
        "chapter_id": "math_2nd_09",
        "chapter_title": "সমতলে বস্তুকণার গতি",
        "subject": "Higher Mathematics",
        "paper": "2nd",
        "chapter_no": 9,
        "predictors": [
            {
                "id": "pred_math_2nd_09_01",
                "stem": "একটি প্রক্ষেপককে $u$ বেগে অনুভূমিকের সাথে $\\alpha$ কোণে নিক্ষেপ করা হলে এর অনুভূমিক পাল্লা $R$ কত?",
                "options": ["$\\frac{u^2\\sin 2\\alpha}{g}$", "$\\frac{u^2\\sin^2\\alpha}{2g}$", "$\\frac{2u\\sin\\alpha}{g}$", "$\\frac{u^2\\cos 2\\alpha}{g}$"],
                "answer": "A",
                "type_ref": "প্রক্ষেপকের অনুভূমিক পাল্লা সূত্র",
                "trap_alert": "পাল্লায় $\\sin 2\\alpha$ থাকে।",
                "speed_hack": "$R = \\frac{u^2\\sin 2\\alpha}{g}$।",
                "explanation": "অনুভূমিক পাল্লা $R = u\\cos\\alpha \\times \\frac{2u\\sin\\alpha}{g} = \\frac{u^2\\sin 2\\alpha}{g}$।"
            },
            {
                "id": "pred_math_2nd_09_02",
                "stem": "প্রক্ষেপকের সর্বাধিক অনুভূমিক পাল্লার জন্য নিক্ষেপণ কোণ কত হতে হবে?",
                "options": ["$45^\\circ$", "$90^\\circ$", "$30^\\circ$", "$60^\\circ$"],
                "answer": "A",
                "type_ref": "সর্বাধিক পাল্লার কোণ",
                "trap_alert": "$2\\alpha = 90^\\circ \implies \\alpha = 45^\\circ$।",
                "speed_hack": "Max range at $45^\\circ$।",
                "explanation": "$\\sin 2\\alpha = 1 \implies 2\\alpha = 90^\\circ \implies \\alpha = 45^\\circ$।"
            },
            {
                "id": "pred_math_2nd_09_03",
                "stem": "একটি বস্তুকে $49\\text{ m/s}$ বেগে খাড়া ওপরের দিকে নিক্ষেপ করলে কত সময় পর ভূমিতে ফিরবে? ($g = 9.8\\text{ m/s}^2$)",
                "options": ["$10\\text{ s}$", "$5\\text{ s}$", "$2.5\\text{ s}$", "$20\\text{ s}$"],
                "answer": "A",
                "type_ref": "খাড়া নিক্ষিপ্ত বস্তুর উড্ডয়নকাল",
                "trap_alert": "মোট সময় $T = 2u/g$।",
                "speed_hack": "$T = \\frac{2(49)}{9.8} = 10\\text{ s}$।",
                "explanation": "$T = \\frac{2u}{g} = \\frac{2 \\times 49}{9.8} = 10\\text{ s}$।"
            },
            {
                "id": "pred_math_2nd_09_04",
                "stem": "স্থির অবস্থান থেকে সুষম ত্বরণে চলে একটি বস্তু $4\\text{ s}$ এ $32\\text{ m}$ যায়। ত্বরণ কত?",
                "options": ["$4\\text{ m/s}^2$", "$2\\text{ m/s}^2$", "$8\\text{ m/s}^2$", "$16\\text{ m/s}^2$"],
                "answer": "A",
                "type_ref": "সুষম ত্বরণে রৈখিক গতি",
                "trap_alert": "$s = \\frac{1}{2}at^2$।",
                "speed_hack": "$a = \\frac{2(32)}{16} = 4\\text{ m/s}^2$।",
                "explanation": "$32 = \\frac{1}{2}a(4^2) = 8a \implies a = 4\\text{ m/s}^2$।"
            },
            {
                "id": "pred_math_2nd_09_05",
                "stem": "স্থির অবস্থান থেকে সুষম ত্বরণে চলমান বস্তুর $t$-তম সেকেন্ডে দূরত্বের সূত্র কোনটি?",
                "options": ["$s_t = \\frac{1}{2}a(2t - 1)$", "$s_t = at - \\frac{1}{2}a$", "$s_t = \\frac{1}{2}at^2$", "$s_t = a(2t - 1)$"],
                "answer": "A",
                "type_ref": "$t$-তম সেকেন্ডের দূরত্ব সূত্র",
                "trap_alert": "$u = 0$ হলে $s_t = \\frac{1}{2}a(2t-1)$।",
                "speed_hack": "$s_t = \\frac{1}{2}a(2t-1)$।",
                "explanation": "$s_t = s(t) - s(t-1) = \\frac{1}{2}a(2t-1)$।"
            },
            {
                "id": "pred_math_2nd_09_06",
                "stem": "একটি প্রক্ষেপকের $\\alpha = 45^\\circ$ হলে পাল্লা $R$ ও সর্বোচ্চ উচ্চতা $H$ এর সম্পর্ক কোনটি?",
                "options": ["$R = 4H$", "$R = 2H$", "$H = 4R$", "$R = H$"],
                "answer": "A",
                "type_ref": "পাল্লা ও সর্বোচ্চ উচ্চতার সম্পর্ক",
                "trap_alert": "$R\\tan\\alpha = 4H$। $\\tan 45^\\circ = 1$।",
                "speed_hack": "$R = 4H$।",
                "explanation": "$R\\tan\\alpha = 4H \implies R(1) = 4H \implies R = 4H$।"
            },
            {
                "id": "pred_math_2nd_09_07",
                "stem": "একটি গুলি তক্তার মধ্যে $3\\text{ cm}$ প্রবেশ করে বেগ অর্ধেক হারায়। আর কতদূর প্রবেশ করবে?",
                "options": ["$1\\text{ cm}$", "$1.5\\text{ cm}$", "$2\\text{ cm}$", "$3\\text{ cm}$"],
                "answer": "A",
                "type_ref": "তক্তায় গুলির প্রবেশ সংক্রান্ত শর্টকাট",
                "trap_alert": "বাকি দূরত্ব $x' = \\frac{x}{n^2 - 1} = \\frac{3}{2^2 - 1} = 1\\text{ cm}$।",
                "speed_hack": "$x' = \\frac{3}{3} = 1\\text{ cm}$।",
                "explanation": "অবশিষ্ট দূরত্ব $x' = \\frac{x}{n^2-1} = \\frac{3}{4-1} = 1\\text{ cm}$।"
            },
            {
                "id": "pred_math_2nd_09_08",
                "stem": "$s = 2t^3 - 3t^2 + 4t$ হলে $t = 2\\text{ s}$ সময়ে কণাটির ত্বরণ কত?",
                "options": ["$18\\text{ m/s}^2$", "$12\\text{ m/s}^2$", "$24\\text{ m/s}^2$", "$6\\text{ m/s}^2$"],
                "answer": "A",
                "type_ref": "ব্যবকলনের সাহায্যে ত্বরণ নির্ণয়",
                "trap_alert": "$a = \\frac{d^2s}{dt^2} = 12t - 6$।",
                "speed_hack": "$12(2) - 6 = 18$।",
                "explanation": "$v = 6t^2 - 6t + 4 \implies a = 12t - 6$। $t = 2$ তে $a = 24 - 6 = 18\\text{ m/s}^2$।"
            },
            {
                "id": "pred_math_2nd_09_09",
                "stem": "নদীর প্রস্থ $d$, স্রোতের বেগ $u$, সাঁতারুর বেগ $v$। সোজাসুজি নদী পার হতে সময় কত?",
                "options": ["$\\frac{d}{\\sqrt{v^2 - u^2}}$", "$\\frac{d}{v}$", "$\\frac{d}{v + u}$", "$\\frac{d}{\\sqrt{v^2 + u^2}}$"],
                "answer": "A",
                "type_ref": "নদী ও নৌকার ন্যূনতম দূরত্বে পারাপার",
                "trap_alert": "লব্ধি বেগ $w = \\sqrt{v^2 - u^2}$।",
                "speed_hack": "$t = \\frac{d}{\\sqrt{v^2 - u^2}}$।",
                "explanation": "সোজাসুজি পাড়ে লব্ধি বেগ $w = \\sqrt{v^2 - u^2}$। সময় $t = \\frac{d}{\\sqrt{v^2 - u^2}}$।"
            },
            {
                "id": "pred_math_2nd_09_10",
                "stem": "একই বেগে নিক্ষিপ্ত দুটি প্রক্ষেপকের পাল্লা সমান হবে যদি নিক্ষেপণ কোণদ্বয় হয়—",
                "options": ["$\\alpha$ এবং $90^\\circ - \\alpha$", "$\\alpha$ এবং $180^\\circ - \\alpha$", "$\\alpha$ এবং $45^\\circ - \\alpha$", "$\\alpha$ এবং $60^\\circ - \\alpha$"],
                "answer": "A",
                "type_ref": "সমান পাল্লার নিক্ষেপণ কোণ",
                "trap_alert": "পূরক কোণে পাল্লা সমান।",
                "speed_hack": "$\\alpha$ এবং $90^\\circ - \\alpha$।",
                "explanation": "$\\sin 2(90^\\circ - \\alpha) = \\sin(180^\\circ - 2\\alpha) = \\sin 2\\alpha$ হওয়ায় পাল্লা সমান হয়।"
            },
            {
                "id": "pred_math_2nd_09_11",
                "stem": "একটি গাড়ি স্থির অবস্থা থেকে $2\\text{ m/s}^2$ ত্বরণে $100\\text{ m}$ অতিক্রম করলে বেগ কত?",
                "options": ["$20\\text{ m/s}$", "$10\\text{ m/s}$", "$40\\text{ m/s}$", "$200\\text{ m/s}$"],
                "answer": "A",
                "type_ref": "বেগ-দূরত্ব সম্পর্ক",
                "trap_alert": "$v = \\sqrt{2as}$।",
                "speed_hack": "$v = \\sqrt{2 \\times 2 \\times 100} = 20$।",
                "explanation": "$v^2 = 2as = 2(2)(100) = 400 \implies v = 20\\text{ m/s}$।"
            },
            {
                "id": "pred_math_2nd_09_12",
                "stem": "প্রথম অর্ধেক দূরত্ব $40\\text{ km/h}$ এবং দ্বিতীয় অর্ধেক $60\\text{ km/h}$ দ্রুতিতে গেলে গড় দ্রুতি কত?",
                "options": ["$48\\text{ km/h}$", "$50\\text{ km/h}$", "$52\\text{ km/h}$", "$45\\text{ km/h}$"],
                "answer": "A",
                "type_ref": "সমান দূরত্বের গড় দ্রুতি",
                "trap_alert": "দূরত্ব সমান হলে বিপরীত গড় (HM) প্রযোজ্য।",
                "speed_hack": "$\\frac{2(40)(60)}{100} = 48\\text{ km/h}$।",
                "explanation": "$v_{\\text{avg}} = \\frac{2v_1 v_2}{v_1 + v_2} = \\frac{2 \\times 40 \\times 60}{100} = 48\\text{ km/h}$।"
            },
            {
                "id": "pred_math_2nd_09_13",
                "stem": "উচ্চতা $h$ থেকে অনুভূমিকভাবে $u$ বেগে নিক্ষিপ্ত বস্তুর পতনকাল কত?",
                "options": ["$\\sqrt{\\frac{2h}{g}}$", "$\\frac{2h}{g}$", "$\\sqrt{\\frac{h}{g}}$", "$\\frac{u}{g}$"],
                "answer": "A",
                "type_ref": "অনুভূমিক প্রক্ষেপকের পতনকাল",
                "trap_alert": "উল্লম্ব আদিবেগ শূন্য: $h = \\frac{1}{2}gt^2$।",
                "speed_hack": "$t = \\sqrt{\\frac{2h}{g}}$।",
                "explanation": "$h = \\frac{1}{2}gt^2 \implies t = \\sqrt{\\frac{2h}{g}}$।"
            },
            {
                "id": "pred_math_2nd_09_14",
                "stem": "গতিপথের সমীকরণ $y = x - \\frac{x^2}{40}$ হলে অনুভূমিক পাল্লা কত?",
                "options": ["$40\\text{ m}$", "$20\\text{ m}$", "$80\\text{ m}$", "$10\\text{ m}$"],
                "answer": "A",
                "type_ref": "ট্র্যাজেক্টরি সমীকরণ হতে পাল্লা",
                "trap_alert": "$y = 0 \implies x = 40$।",
                "speed_hack": "$x(1 - x/40) = 0 \implies x = 40$।",
                "explanation": "ভূমিতে পতনে $y = 0 \implies x(1 - x/40) = 0 \implies x = 40\\text{ m}$।"
            },
            {
                "id": "pred_math_2nd_09_15",
                "stem": "বেগ-সময় লেখচিত্রের অধীনস্থ ক্ষেত্রফল কী নির্দেশ করে?",
                "options": ["সরণ বা অতিক্রান্ত দূরত্ব", "ত্বরণ", "বল", "ক্ষমতা"],
                "answer": "A",
                "type_ref": "লেখচিত্রীয় অর্থ",
                "trap_alert": "ঢাল ত্বরণ, ক্ষেত্রফল সরণ।",
                "speed_hack": "$\\int v\\,dt = s$।",
                "explanation": "$v-t$ লেখচিত্রের ক্ষেত্রফল বস্তুর মোট সরণ নির্দেশ করে।"
            },
            {
                "id": "pred_math_2nd_09_16",
                "stem": "টাওয়ার শীর্ষ থেকে $19.6\\text{ m/s}$ এ খাড়া ওপরে নিক্ষিপ্ত বস্তু $6\\text{ s}$ পর ভূমিতে পড়লে উচ্চতা কত? ($g=9.8$)",
                "options": ["$58.8\\text{ m}$", "$117.6\\text{ m}$", "$176.4\\text{ m}$", "$49.0\\text{ m}$"],
                "answer": "A",
                "type_ref": "উঁচু স্থান হতে নিক্ষিপ্ত বস্তু",
                "trap_alert": "$h = -ut + \\frac{1}{2}gt^2$।",
                "speed_hack": "$-19.6(6) + 4.9(36) = -117.6 + 176.4 = 58.8\\text{ m}$।",
                "explanation": "$h = -(19.6)(6) + \\frac{1}{2}(9.8)(36) = -117.6 + 176.4 = 58.8\\text{ m}$।"
            },
            {
                "id": "pred_math_2nd_09_17",
                "stem": "বৃষ্টি $4\\text{ m/s}$ খাড়া নিচে পড়ছে, ব্যক্তি $3\\text{ m/s}$ অনুভূমিকভাবে হাঁটছে। উলম্বের সাথে ছাতার কোণ কত?",
                "options": ["$\\tan^{-1}\\left(\\frac{3}{4}\\right)$", "$\\tan^{-1}\\left(\\frac{4}{3}\\right)$", "$\\sin^{-1}\\left(\\frac{3}{4}\\right)$", "$45^\\circ$"],
                "answer": "A",
                "type_ref": "আপেক্ষিক বেগ ও ছাতা ধরার কোণ",
                "trap_alert": "উলম্বের সাথে কোণ $\\tan\\theta = \\frac{v_m}{v_r} = 3/4$।",
                "speed_hack": "$\\theta = \\tan^{-1}(3/4)$।",
                "explanation": "উলম্বের সাথে $\\tan\\theta = \\frac{v_m}{v_r} = \\frac{3}{4} \implies \\theta = \\tan^{-1}(3/4)$।"
            },
            {
                "id": "pred_math_2nd_09_18",
                "stem": "একটি প্রক্ষেপকের সর্বোচ্চ উচ্চতায় বেগ কত?",
                "options": ["$u\\cos\\alpha$", "$0$", "$u\\sin\\alpha$", "$u$"],
                "answer": "A",
                "type_ref": "সর্বোচ্চ উচ্চতায় প্রক্ষেপকের বেগ",
                "trap_alert": "উল্লম্ব উপাংশ শূন্য হলেও অনুভূমিক উপাংশ $u\\cos\\alpha$ থাকে।",
                "speed_hack": "$v = u\\cos\\alpha$।",
                "explanation": "সর্বোচ্চ উচ্চতায় $v_y = 0$, কিন্তু অনুভূমিক বেগ $v_x = u\\cos\\alpha$ অপরিবর্তিত থাকে।"
            }
        ]
    }

def get_math_2nd_10():
    """বিস্তার পরিমাপ ও সম্ভাবনা (18 MCQs)"""
    return {
        "chapter_id": "math_2nd_10",
        "chapter_title": "বিস্তার পরিমাপ ও সম্ভাবনা",
        "subject": "Higher Mathematics",
        "paper": "2nd",
        "chapter_no": 10,
        "predictors": [
            {
                "id": "pred_math_2nd_10_01",
                "stem": "$2, 4, 6, 8, 10$ সংখ্যাগুলোর গড় ব্যবধান কত?",
                "options": ["$2.4$", "$2.0$", "$3.0$", "$1.8$"],
                "answer": "A",
                "type_ref": "গড় ব্যবধান নির্ণয়",
                "trap_alert": "গড় $\\bar{x} = 6$। বিচ্যুতি পরমমানের যোগফল $12/5 = 2.4$।",
                "speed_hack": "বিচ্যুতি গড় $= 12/5 = 2.4$।",
                "explanation": "গড় $\\bar{x} = 6$। পরম ব্যবধানসমূহ $4, 2, 0, 2, 4$। গড় ব্যবধান $= 12/5 = 2.4$।"
            },
            {
                "id": "pred_math_2nd_10_02",
                "stem": "যদি $\\sigma_x = 4$ এবং $y = 3x - 5$ হয়, তবে $\\sigma_y$ কত?",
                "options": ["$12$", "$7$", "$16$", "$9$"],
                "answer": "A",
                "type_ref": "পরিমিত ব্যবধানের মূল ও মাপনী পরিবর্তন",
                "trap_alert": "$\\sigma_y = |a|\\sigma_x = 3 \\times 4 = 12$।",
                "speed_hack": "$\\sigma_y = 3(4) = 12$।",
                "explanation": "পরিমিত ব্যবধান মূলের ওপর নির্ভরশীল নয় কিন্তু মাপনীর সমানুপাতিক: $\\sigma_y = 3 \\times 4 = 12$।"
            },
            {
                "id": "pred_math_2nd_10_03",
                "stem": "একটি নিরপেক্ষ ছক্কা নিক্ষেপ করলে মৌলিক বা জোড় সংখ্যা ওঠার সম্ভাবনা কত?",
                "options": ["$\\frac{5}{6}$", "$\\frac{2}{3}$", "$\\frac{1}{2}$", "$1$"],
                "answer": "A",
                "type_ref": "সম্ভাবনার যোগ সূত্র",
                "trap_alert": "$2$ উভয় সেটে আছে, তাই সংযোগ সেটে ৫টি উপাদান: $\\{2, 3, 4, 5, 6\\}$।",
                "speed_hack": "অনুকূল ৫টি $\implies 5/6$।",
                "explanation": "মৌলিক বা জোড় সংখ্যাগুলো হলো $\\{2, 3, 4, 5, 6\\}$। সম্ভাবনা $= 5/6$।"
            },
            {
                "id": "pred_math_2nd_10_04",
                "stem": "স্বাধীন ঘটনাদ্বয়ের জন্য $P(A) = 0.4, P(B) = 0.5$ হলে $P(A \\cup B)$ কত?",
                "options": ["$0.7$", "$0.9$", "$0.2$", "$0.6$"],
                "answer": "A",
                "type_ref": "স্বাধীন ঘটনার সংযোগ সম্ভাবনা",
                "trap_alert": "$P(A \\cap B) = 0.4 \\times 0.5 = 0.2$।",
                "speed_hack": "$0.4 + 0.5 - 0.2 = 0.7$।",
                "explanation": "$P(A \\cup B) = 0.4 + 0.5 - (0.4 \\times 0.5) = 0.9 - 0.2 = 0.7$।"
            },
            {
                "id": "pred_math_2nd_10_05",
                "stem": "প্রথম $n$ সংখ্যক স্বাভাবিক সংখ্যার ভেদাঙ্ক কোনটি?",
                "options": ["$\\frac{n^2 - 1}{12}$", "$\\frac{n^2 + 1}{12}$", "$\\frac{n - 1}{12}$", "$\\frac{n(n+1)}{12}$"],
                "answer": "A",
                "type_ref": "প্রথম $n$ স্বাভাবিক সংখ্যার ভেদাঙ্ক",
                "trap_alert": "স্ট্যান্ডার্ড সূত্র: $\\frac{n^2 - 1}{12}$।",
                "speed_hack": "$\\sigma^2 = \\frac{n^2 - 1}{12}$।",
                "explanation": "প্রথম $n$ স্বাভাবিক সংখ্যার ভেদাঙ্ক $\\sigma^2 = \\frac{n^2 - 1}{12}$।"
            },
            {
                "id": "pred_math_2nd_10_06",
                "stem": "গড় $\\bar{x} = 50$ এবং ভেদাঙ্ক $\\sigma^2 = 25$ হলে বিভেদাঙ্ক ($CV$) কত?",
                "options": ["$10\\%$", "$5\\%$", "$20\\%$", "$50\\%$"],
                "answer": "A",
                "type_ref": "বিভেদাঙ্ক নির্ণয়",
                "trap_alert": "$\\sigma = \\sqrt{25} = 5$।",
                "speed_hack": "$CV = (5/50) \\times 100\\% = 10\\%$।",
                "explanation": "$\\sigma = \\sqrt{25} = 5$। $CV = \\frac{\\sigma}{\\bar{x}} \\times 100\\% = \\frac{5}{50} \\times 100\\% = 10\\%$।"
            },
            {
                "id": "pred_math_2nd_10_07",
                "stem": "একটি মুদ্রা তিনবার টস করলে ঠিক দুটি হেড পাওয়ার সম্ভাবনা কত?",
                "options": ["$\\frac{3}{8}$", "$\\frac{1}{8}$", "$\\frac{1}{2}$", "$\\frac{5}{8}$"],
                "answer": "A",
                "type_ref": "দ্বিপদী সম্ভাবনা (মুদ্রা টস)",
                "trap_alert": "অনুকূল ঘটনা ৩টি (HHT, HTH, THH), মোট ৮টি।",
                "speed_hack": "$\\binom{3}{2}/8 = 3/8$।",
                "explanation": "মোট ফলাফল ৮টি, ঠিক ২টি হেডের সংখ্যা ৩টি। সম্ভাবনা $= 3/8$।"
            },
            {
                "id": "pred_math_2nd_10_08",
                "stem": "৫২ তাসের প্যাকেট হতে ১টি তাস টানলে সেটি টেক্কা অথবা রাজা হওয়ার সম্ভাবনা কত?",
                "options": ["$\\frac{2}{13}$", "$\\frac{1}{13}$", "$\\frac{4}{13}$", "$\\frac{1}{26}$"],
                "answer": "A",
                "type_ref": "তাসের সম্ভাব্যতা",
                "trap_alert": "টেক্কা ৪টি, রাজা ৪টি $\implies$ মোট ৮টি অনুকূল।",
                "speed_hack": "$8/52 = 2/13$।",
                "explanation": "অনুকূল তাস $4 + 4 = 8$। সম্ভাবনা $= 8/52 = 2/13$।"
            },
            {
                "id": "pred_math_2nd_10_09",
                "stem": "পরিমিত ব্যবধানের মান সর্বদা কেমন হয়?",
                "options": ["অঋণাত্মক বাস্তব সংখ্যা ($\\sigma \\ge 0$)", "যে কোনো বাস্তব সংখ্যা", "সর্বদা ঋণাত্মক", "$-1$ থেকে $+1$ এর মধ্যে"],
                "answer": "A",
                "type_ref": "পরিমিত ব্যবধানের মৌলিক ধর্ম",
                "trap_alert": "বর্গের গড়ের বর্গমূল সর্বদা $\\ge 0$।",
                "speed_hack": "$\\sigma \\ge 0$।",
                "explanation": "পরিমিত ব্যবধান বিচ্যুতির বর্গের গড়মানের ধনাত্মক বর্গমূল হওয়ায় সর্বদা অঋণাত্মক।"
            },
            {
                "id": "pred_math_2nd_10_10",
                "stem": "যদি $P(A) = 1/3, P(B) = 1/4$ এবং $P(A \\cap B) = 1/6$ হয়, তবে $P(A | B)$ কত?",
                "options": ["$\\frac{2}{3}$", "$\\frac{1}{2}$", "$\\frac{3}{4}$", "$\\frac{1}{4}$"],
                "answer": "A",
                "type_ref": "শর্তাধীন সম্ভাবনা",
                "trap_alert": "$P(A | B) = \\frac{P(A \\cap B)}{P(B)}$।",
                "speed_hack": "$\\frac{1/6}{1/4} = 4/6 = 2/3$।",
                "explanation": "$P(A | B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{1/6}{1/4} = \\frac{2}{3}$।"
            },
            {
                "id": "pred_math_2nd_10_11",
                "stem": "কোনো ধ্রুবক সংখ্যা $c$ এর পরিমিত ব্যবধান কত?",
                "options": ["$0$", "$c$", "$c^2$", "$\\sqrt{c}$"],
                "answer": "A",
                "type_ref": "ধ্রুবক রাশিসমূহের বিস্তার",
                "trap_alert": "সব মান সমান হলে কোনো বিস্তার থাকে না।",
                "speed_hack": "ধ্রুবকের $\\sigma = 0$।",
                "explanation": "ধ্রুবক উপাত্তের প্রতিটি বিচ্যুতি $c - c = 0$, ফলে $\\sigma = 0$।"
            },
            {
                "id": "pred_math_2nd_10_12",
                "stem": "দুটি ছক্কা নিক্ষেপে প্রাপ্ত সংখ্যাদ্বয়ের যোগফল $7$ হওয়ার সম্ভাবনা কত?",
                "options": ["$\\frac{1}{6}$", "$\\frac{5}{36}$", "$\\frac{7}{36}$", "$\\frac{1}{12}$"],
                "answer": "A",
                "type_ref": "দুটি ছক্কার যোগফল সম্ভাবনা",
                "trap_alert": "অনুকূল জোড় ৬টি, মোট ৩৬টি।",
                "speed_hack": "$6/36 = 1/6$।",
                "explanation": "অনুকূল জোড় ৬টি: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$। সম্ভাবনা $= 6/36 = 1/6$।"
            },
            {
                "id": "pred_math_2nd_10_13",
                "stem": "৪টি লাল ও ৬টি সাদা বল হতে ২টি বল তুললে উভয়ই লাল হওয়ার সম্ভাবনা কত?",
                "options": ["$\\frac{2}{15}$", "$\\frac{4}{15}$", "$\\frac{1}{5}$", "$\\frac{8}{45}$"],
                "answer": "A",
                "type_ref": "সমাবেশ ভিত্তিক সম্ভাবনা",
                "trap_alert": "$\\binom{4}{2}/\\binom{10}{2} = 6/45 = 2/15$।",
                "speed_hack": "$6/45 = 2/15$।",
                "explanation": "অনুকূল $\\binom{4}{2} = 6$, মোট $\\binom{10}{2} = 45$। সম্ভাবনা $= 6/45 = 2/15$।"
            },
            {
                "id": "pred_math_2nd_10_14",
                "stem": "$A$ ও $B$ পরস্পর বর্জনশীল ঘটনা হলে কোনটি সঠিক?",
                "options": ["$P(A \\cap B) = 0$", "$P(A \\cup B) = 1$", "$P(A \\cap B) = P(A)P(B)$", "$P(A) = P(B)$"],
                "answer": "A",
                "type_ref": "বর্জনশীল ঘটনার সংজ্ঞা",
                "trap_alert": "বর্জনশীল হলে একই সাথে ঘটা অসম্ভব ($A \\cap B = \\emptyset$)।",
                "speed_hack": "$P(A \\cap B) = 0$।",
                "explanation": "বর্জনশীল ঘটনার ছেদ সেট ফাঁকা সেট হওয়ায় $P(A \\cap B) = 0$।"
            },
            {
                "id": "pred_math_2nd_10_15",
                "stem": "$1, 2, 3, 4, 5$ এর পরিমিত ব্যবধান কত?",
                "options": ["$\\sqrt{2}$", "$2$", "$\\sqrt{3}$", "$1.5$"],
                "answer": "A",
                "type_ref": "স্বাভাবিক সংখ্যার পরিমিত ব্যবধান",
                "trap_alert": "$\\sigma = \\sqrt{(5^2-1)/12} = \\sqrt{24/12} = \\sqrt{2}$।",
                "speed_hack": "$\\sigma = \\sqrt{2}$।",
                "explanation": "ভেদাঙ্ক $\\sigma^2 = \\frac{5^2-1}{12} = 2 \\implies \\sigma = \\sqrt{2}$।"
            },
            {
                "id": "pred_math_2nd_10_16",
                "stem": "একটি লিপ ইয়ারে ৫৩টি রবিবার থাকার সম্ভাবনা কত?",
                "options": ["$\\frac{2}{7}$", "$\\frac{1}{7}$", "$\\frac{3}{7}$", "$\\frac{5}{7}$"],
                "answer": "A",
                "type_ref": "লিপ ইয়ার সম্ভাবনা সমস্যা",
                "trap_alert": "অতিরিক্ত ২ দিনের ৭টি জোড়ের মধ্যে ২টিতে রবিবার বিদ্যমান।",
                "speed_hack": "সম্ভাবনা $= 2/7$।",
                "explanation": "৩৬৬ দিনে ৫২ সপ্তাহ ও অতিরিক্ত ২ দিন থাকে। ৭টি সম্ভাব্য জোড়ের মধ্যে রবিবার বিদ্যমান ২টি জোড়ে, ফলে সম্ভাবনা $2/7$।"
            },
            {
                "id": "pred_math_2nd_10_17",
                "stem": "নিচের কোন সম্পর্কটি সর্বদা সত্য?",
                "options": ["$\\text{পরিমিত ব্যবধান} \\ge \\text{গড় ব্যবধান}$", "$\\text{গড় ব্যবধান} \\ge \\text{পরিমিত ব্যবধান}$", "$\\text{পরিসর} < \\text{পরিমিত ব্যবধান}$", "$\\text{চতুর্থক ব্যবধান} > \\text{পরিমিত ব্যবধান}$"],
                "answer": "A",
                "type_ref": "বিস্তার পরিমাপকসমূহের পারস্পরিক সম্পর্ক",
                "trap_alert": "পরিমিত ব্যবধান সর্বদা গড় ব্যবধানের চেয়ে বৃহত্তর বা সমান হয়: $SD \\ge MD$।",
                "speed_hack": "$SD \\ge MD$।",
                "explanation": "গাণিতিক অসমতা মতে যে কোনো উপাত্তের জন্য $SD \\ge MD$ সর্বদা সত্য।"
            },
            {
                "id": "pred_math_2nd_10_18",
                "stem": "একটি ঘটনা $A$ এর অনুকূল অনুপাত $3 : 5$ হলে ঘটনাটি ঘটার সম্ভাবনা কত?",
                "options": ["$\\frac{3}{8}$", "$\\frac{3}{5}$", "$\\frac{5}{8}$", "$\\frac{2}{5}$"],
                "answer": "A",
                "type_ref": "অনুকূল অনুপাত হতে সম্ভাবনা",
                "trap_alert": "অনুকূল অনুপাত $a:b$ হলে সম্ভাবনা $\\frac{a}{a+b}$।",
                "speed_hack": "$3/(3+5) = 3/8$।",
                "explanation": "অনুকূল ঘটনা $3$, মোট ঘটনা $3 + 5 = 8$। সম্ভাবনা $= 3/8$।"
            }
        ]
    }
