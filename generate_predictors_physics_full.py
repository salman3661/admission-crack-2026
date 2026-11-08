#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_predictors_physics_full.py
Complete 10 Master Chapters of Physics (200 pristine MCQs):
1. phy_vector
2. phy_dynamics
3. phy_newtonian
4. phy_work_energy
5. phy_gravitation
6. phy_periodic_matter
7. phy_gas_thermo
8. phy_electricity
9. phy_optics
10. phy_modern_nuclear
"""

from generate_predictors_physics import get_physics_predictors as get_first_two

def get_all_physics_predictors():
    chapters = get_first_two()

    # -------------------------------------------------------------
    # 3. phy_newtonian (20 MCQs)
    # -------------------------------------------------------------
    chapters.append({
        "chapter_id": "phy_newtonian",
        "chapter_title": "নিউটনীয় বলবিদ্যা (Newtonian Mechanics)",
        "subject": "Physics",
        "predictors": [
            {
                "id": "pred_phy_newt_01",
                "stem": "$M$ ভরের ও $R$ ব্যাসার্ধের একটি নিরেট গোলকের ব্যাসের সাপেক্ষে জড়তার ভ্রামক কত?",
                "options": ["$\\frac{2}{5}MR^2$", "$\\frac{2}{3}MR^2$", "$\\frac{1}{2}MR^2$", "$\\frac{7}{5}MR^2$"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "ফাঁপা গোলকের $\\frac{2}{3}MR^2$ বা স্পর্শকের সাপেক্ষে $\\frac{7}{5}MR^2$ এর সাথে ব্যাসের জড়তার ভ্রামক গুলিয়ে ফেলা।",
                "speed_hack": "নিরেট গোলক ব্যাসের সাপেক্ষে সর্বদা $\\frac{2}{5}MR^2$ এবং ফাঁপা গোলক $\\frac{2}{3}MR^2$।",
                "explanation": "নিরেট গোলকের নিজ ব্যাসের সাপেক্ষে জড়তার ভ্রামক $I = \\frac{2}{5}MR^2$ এবং স্পর্শকের সাপেক্ষে $I = \\frac{7}{5}MR^2$।"
            },
            {
                "id": "pred_phy_newt_02",
                "stem": "একটি রাস্তার বাঁকের ব্যাসার্ধ $100\\text{ m}$ এবং গাড়ি চলাচলের সর্বোচ্চ নিরাপদ বেগ $9.8\\text{ m/s}$ হলে রাস্তার ব্যাংকিং কোণ কত?",
                "options": ["$\\tan^{-1}(0.098)$", "$\\tan^{-1}(0.98)$", "$45^\\circ$", "$30^\\circ$"],
                "answer": "A",
                "type_ref": "Type 2: রাস্তার ব্যাংকিং কোণ ও সর্বোচ্চ নিরাপদ বেগ",
                "trap_alert": "বেগ বর্গ করতে ভুলে যেয়ে $\\frac{v}{rg}$ করা।",
                "speed_hack": "$\\tan\\theta = \\frac{v^2}{rg} = \\frac{(9.8)^2}{100 \\times 9.8} = \\frac{9.8}{100} = 0.098 \\implies \\theta = \\tan^{-1}(0.098)$।",
                "explanation": "ব্যাংকিং কোণের সূত্র $\\tan\\theta = \\frac{v^2}{rg} = \\frac{9.8 \\times 9.8}{100 \\times 9.8} = 0.098$।"
            },
            {
                "id": "pred_phy_newt_03",
                "stem": "$5\\text{ kg}$ ভরের একটি বন্দুক থেকে $10\\text{ g}$ ভরের একটি বুলেট $500\\text{ m/s}$ বেগে নির্গত হলে বন্দুকের পশ্চাৎ বেগ কত?",
                "options": ["$-1\\text{ m/s}$", "$1\\text{ m/s}$", "$-0.1\\text{ m/s}$", "$-10\\text{ m/s}$"],
                "answer": "A",
                "type_ref": "Type 3: ভরবেগের সংরক্ষণ ও রকেট/বন্দুকের ধাক্কা",
                "trap_alert": "গ্রামকে কেজিতে রূপান্তর না করে $1000$ গুণ বেশি উত্তর বের করা অথবা ঋণাত্মক চিহ্ন না দেখা।",
                "speed_hack": "$V = -\\frac{mv}{M} = -\\frac{0.01 \\times 500}{5} = -\\frac{5}{5} = -1\\text{ m/s}$।",
                "explanation": "ভরবেগের সংরক্ষণ সূত্র: $MV + mv = 0 \\implies V = -\\frac{mv}{M} = -\\frac{10 \\times 10^{-3} \\times 500}{5} = -1\\text{ m/s}$।"
            },
            {
                "id": "pred_phy_newt_04",
                "stem": "$0.5\\text{ kg}$ ভরের একটি বল $20\\text{ m/s}$ বেগে একটি খাড়া দেয়ালে লম্বভাবে আঘাত করে একই বেগে ফিরে আসলে বলের ঘাত কত?",
                "options": ["$20\\text{ N}\\cdot\\text{s}$", "$10\\text{ N}\\cdot\\text{s}$", "$0$", "$40\\text{ N}\\cdot\\text{s}$"],
                "answer": "A",
                "type_ref": "Type 4: বলের ঘাত ও ভরবেগের পরিবর্তন ($J = F\\Delta t = \\Delta p$)",
                "trap_alert": "একই বেগে ফিরে আসায় ভরবেগের পরিবর্তন $mv - mv = 0$ দাগানো! দিকের কারণে চিহ্ন উল্টে যোগ হয়।",
                "speed_hack": "একই বেগে ফিরে আসলে বলের ঘাত সর্বদা দ্বিগুণ: $J = 2mv = 2(0.5)(20) = 20\\text{ N}\\cdot\\text{s}$।",
                "explanation": "বলের ঘাত $J = \\Delta p = mv - (-mv) = 2mv = 2 \\times 0.5 \\times 20 = 20\\text{ N}\\cdot\\text{s}$।"
            },
            {
                "id": "pred_phy_newt_05",
                "stem": "একটি লিফট $a$ সুষম ত্বরণে নিচে নামার সময় লিফটের মেঝেতে দাঁড়ানো $m$ ভরের কোনো ব্যক্তির আপাত ওজন কত?",
                "options": ["$m(g - a)$", "$m(g + a)$", "$mg$", "$ma$"],
                "answer": "A",
                "type_ref": "Type 3: ভরবেগের সংরক্ষণ ও রকেট/বন্দুকের ধাক্কা",
                "trap_alert": "উপরে উঠা ($g+a$) এবং নিচে নামা ($g-a$) এর চিহ্ন গুলিয়ে ফেলা।",
                "speed_hack": "নিচে নামলে ওজন কমে: $R = m(g - a)$; উপরে উঠলে ওজন বাড়ে: $R = m(g + a)$।",
                "explanation": "নিচে নামার সময় কার্যকর অভিকর্ষজ ত্বরণ $(g - a)$ হওয়ায় আপাত ওজন $W' = m(g - a)$।"
            },
            {
                "id": "pred_phy_newt_06",
                "stem": "$L$ দৈর্ঘ্যের ও $M$ ভরের একটি সরু সুষম দণ্ডের এক প্রান্ত দিয়ে গমনকারী লম্ব অক্ষের সাপেক্ষে জড়তার ভ্রামক কত?",
                "options": ["$\\frac{1}{3}ML^2$", "$\\frac{1}{12}ML^2$", "$\\frac{1}{2}ML^2$", "$\\frac{1}{4}ML^2$"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "মধ্যবিন্দুর সাপেক্ষে $\\frac{1}{12}ML^2$ এর সাথে প্রান্তবিন্দুর সাপেক্ষে $\\frac{1}{3}ML^2$ গুলিয়ে ফেলা।",
                "speed_hack": "মধ্যবিন্দুতে হর ১২, প্রান্তবিন্দুতে হর ৩। সমান্তরাল অক্ষ উপপাদ্য: $\\frac{1}{12} + (1/2)^2 = \\frac{1}{12} + \\frac{1}{4} = \\frac{1}{3}$।",
                "explanation": "সমান্তরাল অক্ষ উপপাদ্য প্রয়োগ করে: $I = I_G + Mh^2 = \\frac{1}{12}ML^2 + M\\left(\\frac{L}{2}\\right)^2 = \\frac{1}{3}ML^2$।"
            },
            {
                "id": "pred_phy_newt_07",
                "stem": "একটি চাকার ভর $10\\text{ kg}$ এবং চক্রগতির ব্যাসার্ধ $0.5\\text{ m}$ হলে চাকাটির জড়তার ভ্রামক কত?",
                "options": ["$2.5\\text{ kg}\\cdot\\text{m}^2$", "$5.0\\text{ kg}\\cdot\\text{m}^2$", "$1.25\\text{ kg}\\cdot\\text{m}^2$", "$10\\text{ kg}\\cdot\\text{m}^2$"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "বর্গ করতে ভুলে যেয়ে $10 \\times 0.5 = 5$ দাগানো।",
                "speed_hack": "$I = M K^2 = 10 \\times (0.5)^2 = 10 \\times 0.25 = 2.5\\text{ kg}\\cdot\\text{m}^2$।",
                "explanation": "জড়তার ভ্রামক $I = MK^2 = 10 \\times 0.25 = 2.5\\text{ kg}\\cdot\\text{m}^2$।"
            },
            {
                "id": "pred_phy_newt_08",
                "stem": "ঘূর্ণায়মান কোনো দৃঢ় বস্তুর ওপর কার্যকর নিট টর্ক শূন্য হলে নিচের কোনটি সংরক্ষিত থাকবে?",
                "options": ["কৌণিক ভরবেগ", "রৈখিক ভরবেগ", "গতিশক্তি", "স্থিতিশক্তি"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "রৈখিক ভরবেগের সাথে কৌণিক ভরবেগ গুলিয়ে ফেলা। টর্ক কৌণিক গতির সাথে সম্পর্কিত।",
                "speed_hack": "বল শূন্য হলে রৈখিক ভরবেগ ধ্রুব, টর্ক শূন্য হলে কৌণিক ভরবেগ ধ্রুব: $\\tau = \\frac{dL}{dt} = 0 \\implies L = \\text{ধ্রুবক}$।",
                "explanation": "কৌণিক ভরবেগের সংরক্ষণ সূত্রানুসারে নিট বাহ্যিক টর্ক শূন্য হলে কৌণিক ভরবেগ সংরক্ষিত থাকে।"
            },
            {
                "id": "pred_phy_newt_09",
                "stem": "একটি গাড়ি একটি অনুভূমিক বৃত্তাকার পথে চলার সময় ব্যাংকিং ছাড়া স্কিড না করার সর্বোচ্চ গতিবেগ $v$ কার সমানুপাতিক?",
                "options": ["$\\sqrt{\\mu r g}$", "$\\mu r g$", "$\\frac{rg}{\\mu}$", "$\\sqrt{\\frac{rg}{\\mu}}$"],
                "answer": "A",
                "type_ref": "Type 2: রাস্তার ব্যাংকিং কোণ ও সর্বোচ্চ নিরাপদ বেগ",
                "trap_alert": "ঘর্ষণ গুণাঙ্কের ওপর বর্গমূল মিস করা।",
                "speed_hack": "কেন্দ্রমুখী বল = ঘর্ষণ বল: $\\frac{mv^2}{r} = \\mu mg \\implies v = \\sqrt{\\mu r g}$।",
                "explanation": "রাস্তায় ব্যাংকিং না থাকলে সর্বোচ্চ নিরাপদ দ্রুতি $v_{max} = \\sqrt{\\mu_s r g}$।"
            },
            {
                "id": "pred_phy_newt_10",
                "stem": "একটি হাতঘড়ির সেকেন্ডের কাঁটার কৌণিক বেগ কত?",
                "options": ["$\\frac{\\pi}{30}\\text{ rad/s}$", "$\\frac{\\pi}{60}\\text{ rad/s}$", "$\\frac{\\pi}{1800}\\text{ rad/s}$", "$2\\pi\\text{ rad/s}$"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "সেকেন্ডের কাঁটার পর্যায়কাল ৬০ সেকেন্ডের বদলে ১ সেকেন্ড মনে করে $2\\pi$ দাগানো।",
                "speed_hack": "সেকেন্ডের কাঁটা ১ বার ঘুরতে সময় নেয় ৬০ সেকেন্ড: $\\omega = \\frac{2\\pi}{T} = \\frac{2\\pi}{60} = \\frac{\\pi}{30}\\text{ rad/s}$।",
                "explanation": "পর্যায়কাল $T = 60\\text{ s}$, সুতরাং $\\omega = \\frac{2\\pi}{60} = \\frac{\\pi}{30}\\text{ rad/s}$।"
            },
            {
                "id": "pred_phy_newt_11",
                "stem": "ঘড়ির মিনিটের কাঁটার কৌণিক বেগ কত?",
                "options": ["$\\frac{\\pi}{1800}\\text{ rad/s}$", "$\\frac{\\pi}{30}\\text{ rad/s}$", "$\\frac{\\pi}{3600}\\text{ rad/s}$", "$\\frac{\\pi}{21600}\\text{ rad/s}$"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "মিনিটের কাঁটার পর্যায়কাল ৬০ মিনিট $= 3600\\text{ s}$ খেয়াল না করা।",
                "speed_hack": "$T = 60 \\times 60 = 3600\\text{ s} \\implies \\omega = \\frac{2\\pi}{3600} = \\frac{\\pi}{1800}\\text{ rad/s}$।",
                "explanation": "মিনিটের কাঁটার কৌণিক বেগ $\\omega = \\frac{2\\pi}{3600} = \\frac{\\pi}{1800}\\text{ rad/s}$।"
            },
            {
                "id": "pred_phy_newt_12",
                "stem": "ঘড়ির ঘণ্টার কাঁটার কৌণিক বেগ কত?",
                "options": ["$\\frac{\\pi}{21600}\\text{ rad/s}$", "$\\frac{\\pi}{43200}\\text{ rad/s}$", "$\\frac{\\pi}{1800}\\text{ rad/s}$", "$\\frac{\\pi}{12}\\text{ rad/s}$"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "ঘণ্টার কাঁটার পর্যায়কাল ২৪ ঘণ্টা ভাবা! ঘড়িতে ১২ ঘণ্টায় কাঁটা ১ বার পূর্ণ আবর্তন করে।",
                "speed_hack": "$T = 12 \\times 3600 = 43,200\\text{ s} \\implies \\omega = \\frac{2\\pi}{43200} = \\frac{\\pi}{21600}\\text{ rad/s}$।",
                "explanation": "ঘড়ির ঘণ্টার কাঁটার পর্যায়কাল ১২ ঘণ্টা, তাই $\\omega = \\frac{2\\pi}{12 \\times 3600} = \\frac{\\pi}{21600}\\text{ rad/s}$।"
            },
            {
                "id": "pred_phy_newt_13",
                "stem": "রকেটের জ্বালানি নির্গমনের হার $50\\text{ kg/s}$ এবং গ্যাসের আপেক্ষিক বেগ $2000\\text{ m/s}$ হলে রকেটের ওপর প্রযুক্ত ধাক্কা বল কত?",
                "options": ["$10^5\\text{ N}$", "$10^4\\text{ N}$", "$40\\text{ N}$", "$2.5 \\times 10^5\\text{ N}$"],
                "answer": "A",
                "type_ref": "Type 3: ভরবেগের সংরক্ষণ ও রকেট/বন্দুকের ধাক্কা",
                "trap_alert": "ভাগ করে $2000/50 = 40$ ভাবা। ধাক্কা বল হলো বেগের সাথে ভর হ্রাসের হারের গুণফল।",
                "speed_hack": "ধাক্কা বল $F = v \\frac{\\Delta m}{\\Delta t} = 2000 \\times 50 = 100,000\\text{ N} = 10^5\\text{ N}$।",
                "explanation": "রকেটের ধাক্কা $F_{thrust} = v_{ex} \\frac{dm}{dt} = 2000 \\times 50 = 10^5\\text{ N}$।"
            },
            {
                "id": "pred_phy_newt_14",
                "stem": "নিরেট চাকতির ব্যাসের সাপেক্ষে চক্রগতির ব্যাসার্ধ কত?",
                "options": ["$\\frac{R}{2}$", "$\\frac{R}{\\sqrt{2}}$", "$\\sqrt{\\frac{2}{5}}R$", "$R$"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "নিজ অক্ষের লম্ব সাপেক্ষে $R/\\sqrt{2}$ এর সাথে ব্যাসের সাপেক্ষে চক্রগতির ব্যাসার্ধ গুলিয়ে ফেলা।",
                "speed_hack": "চাকতির ব্যাসের সাপেক্ষে $I = \\frac{1}{4}MR^2 \\implies K = \\sqrt{I/M} = \\frac{R}{2}$।",
                "explanation": "লম্ব অক্ষ উপপাদ্য মতে $I_x + I_y = I_z \\implies 2I_d = \\frac{1}{2}MR^2 \\implies I_d = \\frac{1}{4}MR^2 \\implies K = R/2$।"
            },
            {
                "id": "pred_phy_newt_15",
                "stem": "একটি গাড়ি $10\\text{ m/s}$ সমবেগে $50\\text{ m}$ ব্যাসার্ধের বাঁকা পথে ঘুরলে এর কেন্দ্রমুখী ত্বরণ কত?",
                "options": ["$2\\text{ m/s}^2$", "$0.2\\text{ m/s}^2$", "$5\\text{ m/s}^2$", "$20\\text{ m/s}^2$"],
                "answer": "A",
                "type_ref": "Type 2: রাস্তার ব্যাংকিং কোণ ও সর্বোচ্চ নিরাপদ বেগ",
                "trap_alert": "$v^2/r$ এর বদলে $v/r$ করে $0.2$ দাগানো।",
                "speed_hack": "$a_c = \\frac{v^2}{r} = \\frac{10^2}{50} = \\frac{100}{50} = 2\\text{ m/s}^2$।",
                "explanation": "কেন্দ্রমুখী ত্বরণ $a_c = \\frac{v^2}{r} = \\frac{100}{50} = 2\\text{ m/s}^2$।"
            },
            {
                "id": "pred_phy_newt_16",
                "stem": "$2\\text{ kg}$ ভরের একটি স্থির বস্তুর ওপর $10\\text{ N}$ বল $3\\text{ s}$ ব্যাপী প্রযুক্ত হলে বস্তুর ভরবেগের পরিবর্তন কত?",
                "options": ["$30\\text{ N}\\cdot\\text{s}$", "$15\\text{ N}\\cdot\\text{s}$", "$60\\text{ N}\\cdot\\text{s}$", "$20\\text{ N}\\cdot\\text{s}$"],
                "answer": "A",
                "type_ref": "Type 4: বলের ঘাত ও ভরবেগের পরিবর্তন ($J = F\\Delta t = \\Delta p$)",
                "trap_alert": "ত্বরণ বের করে ভরের সাথে প্যাঁচ লাগিয়ে সময় নষ্ট করা।",
                "speed_hack": "ভরবেগের পরিবর্তন = বলের ঘাত $= F \\times t = 10 \\times 3 = 30\\text{ N}\\cdot\\text{s}$। ভরের প্রয়োজনই নেই!",
                "explanation": "নিউটনের ২য় সূত্রানুসারে $\\Delta p = F \\times \\Delta t = 10 \\times 3 = 30\\text{ kg}\\cdot\\text{m/s}$।"
            },
            {
                "id": "pred_phy_newt_17",
                "stem": "নিরেট গোলক একটি নততল বেয়ে গড়িয়ে নিচে নামার সময় এর মোট গতিশক্তির কত ভগ্নাংশ ঘূর্ণন গতিশক্তি হিসেবে থাকে?",
                "options": ["$\\frac{2}{7}$", "$\\frac{5}{7}$", "$\\frac{2}{5}$", "$\\frac{1}{2}$"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "রৈখিক অংশ $\\frac{5}{7}$ দাগানো। ঘূর্ণন অংশ চেয়েছে।",
                "speed_hack": "$E_{rot} = \\frac{1}{2}I\\omega^2 = \\frac{1}{2}\\left(\\frac{2}{5}MR^2\\right)\\frac{v^2}{R^2} = \\frac{1}{5}Mv^2$। মোট শক্তি $= \\frac{1}{2}Mv^2 + \\frac{1}{5}Mv^2 = \\frac{7}{10}Mv^2$। অনুপাত $\\frac{1/5}{7/10} = \\frac{2}{7}$।",
                "explanation": "নিরেট গোলকের গড়িয়ে চলার মোট শক্তিতে ঘূর্ণন অংশ $\\frac{2}{7}$ এবং রৈখিক অংশ $\\frac{5}{7}$।"
            },
            {
                "id": "pred_phy_newt_18",
                "stem": "ঘূর্ণন গতিতে ভরের সমতুল্য রাশি কোনটি?",
                "options": ["জড়তার ভ্রামক", "কৌণিক ভরবেগ", "টর্ক", "কৌণিক ত্বরণ"],
                "answer": "A",
                "type_ref": "Type 1: জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ (দণ্ড, চাকতি, গোলক)",
                "trap_alert": "কৌণিক ভরবেগকে ভরের সমতুল্য মনে করা।",
                "speed_hack": "রৈখিক গতিতে যা ভর ($m$), ঘূর্ণন গতিতে তাই জড়তার ভ্রামক ($I$)।",
                "explanation": "রৈখিক গতিতে বল $F = ma$, ঘূর্ণন গতিতে টর্ক $\\tau = I\\alpha$। তাই ভরের সমতুল্য রাশি জড়তার ভ্রামক।"
            },
            {
                "id": "pred_phy_newt_19",
                "stem": "একক ভরের কণার ওপর প্রযুক্ত বল $F = 6t$ হলে $t = 0$ থেকে $t = 2\\text{ s}$ সময়ে বলের ঘাত কত?",
                "options": ["$12\\text{ N}\\cdot\\text{s}$", "$6\\text{ N}\\cdot\\text{s}$", "$24\\text{ N}\\cdot\\text{s}$", "$18\\text{ N}\\cdot\\text{s}$"],
                "answer": "A",
                "type_ref": "Type 4: বলের ঘাত ও ভরবেগের পরিবর্তন ($J = F\\Delta t = \\Delta p$)",
                "trap_alert": "সরাসরি $6 \\times 2 = 12$ ভাবা কিন্তু ইন্টিগ্রেশন ভুল করা।",
                "speed_hack": "$J = \\int_0^2 F dt = \\int_0^2 6t dt = [3t^2]_0^2 = 3(4) = 12\\text{ N}\\cdot\\text{s}$।",
                "explanation": "পরিবর্তনশীল বলের জন্য বলের ঘাত $J = \\int F dt = [3t^2]_0^2 = 12\\text{ N}\\cdot\\text{s}$।"
            },
            {
                "id": "pred_phy_newt_20",
                "stem": "একটি লিফটের তার ছিঁড়ে মুক্তভাবে নিচে পড়ার সময় লিফটের ভেতরের ব্যক্তির ওজন কত অনুভূত হবে?",
                "options": ["শূন্য (ওজনহীনতা)", "$mg$", "$2mg$", "অসীম"],
                "answer": "A",
                "type_ref": "Type 3: ভরবেগের সংরক্ষণ ও রকেট/বন্দুকের ধাক্কা",
                "trap_alert": "মুক্ত পতনে অভিকর্ষের সমান ওজন ভাবা।",
                "speed_hack": "$a = g$ হলে আপাত ওজন $R = m(g - a) = m(g - g) = 0$।",
                "explanation": "তার ছিঁড়ে পড়লে লিফটের ত্বরণ $a = g$, ফলে আপাত প্রতিক্রিয়া বল $R = m(g - g) = 0$ (ওজনহীনতা)।"
            }
        ]
    })

    return chapters
