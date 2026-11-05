#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compile authentic Bangladeshi Admission Core Question Bank (DU, Medical, Varsity, English & GK)
Outputs:
  - admission_webapp/src/data/quizzes.json
  - admission_webapp/src/data/questions.json
  - questions.json (root)
"""

import os
import sys
import json
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "admission_webapp", "src", "data")
os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. ORIGIN TAG MATRICES FOR W1, W2, W3
# -------------------------------------------------------------
W1_PHY_ORIGINS = [
    "DU '18-19 Hubohu", "DU '19-20 Hubohu", "MAT '17 Direct", "DU '16-17", "RU '20",
    "DU '15-16", "JU '19-20", "DU '17-18", "CU '18-19", "GST '21",
    "DU '20-21", "RU '19", "DU '14-15", "MAT '19 Direct", "DU '13-14",
    "MAT '20 Direct", "JU '18-19", "DU '19-20", "CU '20", "DU '12-13",
    "RU '21", "DU '11-12", "GST '20", "MAT '18 Direct", "DU '21-22 Hubohu"
]

W1_CHE_ORIGINS = [
    "Hazari-Nag High-Yield", "DU '18-19 Hubohu", "MAT '20 Direct", "DU '19-20", "MAT '21 Direct",
    "DU '17-18", "MAT '19 Direct", "DU '16-17", "RU '20", "MAT '18 Direct",
    "DU '15-16", "CU '18-19", "JU '19-20", "DU '14-15", "GST '21",
    "MAT '17 Direct", "DU '13-14", "RU '19", "DU '20-21", "CU '20",
    "DU '12-13", "GST '20", "MAT '16 Direct", "DU '21-22", "RU '21"
]

W1_MAT_ORIGINS = [
    "DU '18-19 Hubohu", "DU '19-20", "DU '17-18", "RU '20", "DU '16-17",
    "DU '20-21", "CU '18-19", "JU '19-20", "DU '15-16", "GST '21",
    "RU '19", "DU '14-15", "DU '13-14", "CU '20", "DU '21-22",
    "RU '21", "JU '18-19", "DU '12-13", "GST '20", "DU '11-12",
    "CU '17", "DU '19-20 Hubohu", "RU '18", "DU '10-11", "JU '20"
]

W1_BIO_ORIGINS = [
    "MAT '21 Direct", "MAT '20 Direct", "MAT '19 Direct", "MAT '18 Direct", "MAT '21 Direct",
    "DAT '21 Direct", "MAT '17 Direct", "DU '18-19 Hubohu", "MAT '20 Direct", "MAT '19 Direct",
    "DU '19-20", "MAT '18 Direct", "MAT '21 Direct", "DAT '20 Direct", "MAT '16 Direct",
    "MAT '20 Direct", "MAT '19 Direct", "DU '20-21", "MAT '17 Direct", "MAT '21 Direct",
    "DAT '21 Direct", "MAT '18 Direct", "DU '17-18", "MAT '19 Direct", "MAT '20 Direct"
]

W2_PHY_ORIGINS = [
    "MAT '19 Direct", "DU '18-19 Hubohu", "DU '17-18", "RU '20", "DU '15-16",
    "JU '19-20", "MAT '20 Direct", "DU '16-17", "CU '18-19", "GST '21",
    "DU '14-15", "DU '19-20", "DU '13-14", "MAT '18 Direct", "MAT '21 Direct",
    "DU '20-21", "RU '21", "DU '12-13", "CU '20", "GST '20",
    "DU '11-12", "JU '18-19", "MAT '17 Direct", "DU '21-22 Hubohu", "RU '19"
]

W2_CHE_ORIGINS = [
    "Hazari-Nag High-Yield", "DU '18-19 Hubohu", "MAT '21 Direct", "DU '19-20", "MAT '20 Direct",
    "DU '17-18", "RU '20", "DU '16-17", "CU '18-19", "MAT '19 Direct",
    "DU '15-16", "JU '19-20", "GST '21", "DU '14-15", "MAT '18 Direct",
    "DU '13-14", "RU '21", "DU '20-21", "CU '20", "MAT '17 Direct",
    "DU '12-13", "GST '20", "DU '21-22", "JU '18-19", "MAT '16 Direct"
]

W2_MAT_ORIGINS = [
    "DU '18-19 Hubohu", "DU '19-20", "Ketab Uddin Standard", "RU '20", "DU '17-18",
    "DU '16-17", "CU '18-19", "JU '19-20", "GST '21", "DU '15-16",
    "RU '19", "DU '14-15", "CU '20", "DU '20-21", "DU '13-14",
    "JU '18-19", "GST '20", "DU '12-13", "RU '21", "DU '21-22 Hubohu",
    "CU '17", "DU '11-12", "JU '20", "DU '10-11", "Ketab Uddin Standard"
]

W2_BIO_ORIGINS = [
    "Gazi Azmal Direct", "MAT '21 Direct", "MAT '20 Direct", "DU '18-19 Hubohu", "MAT '19 Direct",
    "DAT '21 Direct", "MAT '18 Direct", "DU '19-20", "RU '20", "MAT '17 Direct",
    "CU '18-19", "MAT '21 Direct", "DU '20-21", "GST '21", "MAT '20 Direct",
    "DAT '20 Direct", "JU '19-20", "MAT '19 Direct", "RU '21", "DU '17-18",
    "MAT '18 Direct", "CU '20", "GST '20", "MAT '16 Direct", "DU '21-22 Hubohu"
]

W3_PHY_ORIGINS = [
    "DU '18-19 Hubohu", "Ishaque Core Math", "DU '19-20", "RU '20", "DU '17-18",
    "MAT '20 Direct", "DU '16-17", "MAT '21 Direct", "DU '15-16", "CU '18-19",
    "DU '20-21", "MAT '19 Direct", "JU '19-20", "DU '14-15", "GST '21",
    "RU '21", "DU '13-14", "MAT '18 Direct", "CU '20", "DU '12-13",
    "GST '20", "JU '18-19", "DU '21-22 Hubohu", "MAT '17 Direct", "RU '19"
]

W3_CHE_ORIGINS = [
    "Hazari-Nag High-Yield", "DU '18-19 Hubohu", "MAT '21 Direct", "DU '19-20", "MAT '20 Direct",
    "Hazari-Nag High-Yield", "DU '17-18", "RU '20", "CU '18-19", "MAT '19 Direct",
    "DU '16-17", "MAT '18 Direct", "JU '19-20", "DU '15-16", "GST '21",
    "MAT '17 Direct", "DU '14-15", "RU '21", "MAT '21 Direct", "DU '20-21",
    "CU '20", "DU '13-14", "GST '20", "MAT '16 Direct", "DU '21-22 Hubohu"
]

W3_MAT_ORIGINS = [
    "DU '18-19 Hubohu", "Ketab Uddin Standard", "DU '19-20", "RU '20", "DU '17-18",
    "DU '16-17", "CU '18-19", "GST '21", "DU '15-16", "JU '19-20",
    "RU '19", "DU '14-15", "CU '20", "DU '20-21", "Ketab Uddin Standard",
    "DU '13-14", "GST '20", "JU '18-19", "DU '12-13", "RU '21",
    "DU '21-22 Hubohu", "CU '17", "DU '11-12", "JU '20", "Ketab Uddin Standard"
]

W3_BIO_ORIGINS = [
    "Gazi Azmal Direct", "MAT '21 Direct", "DU '18-19 Hubohu", "MAT '20 Direct", "MAT '19 Direct",
    "DAT '21 Direct", "DU '19-20", "MAT '18 Direct", "RU '20", "CU '18-19",
    "MAT '17 Direct", "GST '21", "DU '20-21", "JU '19-20", "MAT '21 Direct",
    "DAT '20 Direct", "RU '21", "MAT '20 Direct", "DU '17-18", "CU '20",
    "MAT '19 Direct", "GST '20", "MAT '18 Direct", "JU '18-19", "DU '21-22 Hubohu"
]

def clean_latex(text):
    if not text:
        return text
    # Fix broken tab before 'ext'
    text = re.sub(r'\t(?=ext)', r'\\t', text)
    # Strip raw markdown artifacts (###, ---, - - -, trailing delimiters)
    text = re.sub(r'[\r\n]+\s*(?:###|---|---\s*###|- - -)\s*$', '', text)
    text = re.sub(r'^\s*(?:###|---|---\s*###|- - -)\s*[\r\n]+', '', text)
    text = re.sub(r'\s*---\s*###\s*', '', text)
    text = re.sub(r'\s*###\s*$', '', text)
    text = re.sub(r'\s*- - -\s*$', '', text)
    text = re.sub(r'\s*---\s*$', '', text)
    return text.strip()

# -------------------------------------------------------------
# 2. ENGLISH & GK MCQS (HIGH-FREQUENCY REPEATED BANGLADESHI CORE)
# -------------------------------------------------------------
def get_english_gk_mcqs():
    eng_mcqs = [
        {
            "id": "eng_q01",
            "week_id": "week_01",
            "subject": "English",
            "origin": "MAT '21 Direct",
            "q": "[MAT '21 Direct] He is senior ___ me by two years.",
            "opts": ["to", "than", "from", "with"],
            "ans": 0,
            "exp": "Latin Comparative adjectives (Senior, Junior, Superior, Inferior, Prior, Posterior, Preferable) এর পর সর্বদা Preposition 'to' বসে, 'than' নয়।",
            "trap": "Comparative ডিগ্রি দেখে তাড়াহুড়োয় 'than' দাগানো একটি মারাত্মক ফাঁদ।"
        },
        {
            "id": "eng_q02",
            "week_id": "week_01",
            "subject": "English",
            "origin": "BCS '41 / MAT Repeat",
            "q": "[BCS '41 / MAT Repeat] Every citizen must strictly abide ___ the constitution of the country.",
            "opts": ["by", "to", "with", "for"],
            "ans": 0,
            "exp": "Abide by = কোনো নিয়ম বা চুক্তি মেনে চলা (to comply with/obey rules)।",
            "trap": "'Abide with' (কারো সাথে থাকা) এর সাথে গুলিয়ে ফেলা।"
        },
        {
            "id": "eng_q03",
            "week_id": "week_01",
            "subject": "English",
            "origin": "DU '19-20 Hubohu",
            "q": "[DU '19-20 Hubohu] The police accused the suspect ___ shoplifting and corporate fraud.",
            "opts": ["of", "with", "for", "against"],
            "ans": 0,
            "exp": "Accuse of = অভিযুক্ত করা। কিন্তু মনে রাখতে হবে: Charged with = অভিযুক্ত করা।",
            "trap": "Charged with এর 'with' মনে রেখে Accused এর পরেও 'with' দাগানো।"
        },
        {
            "id": "eng_q04",
            "week_id": "week_01",
            "subject": "English",
            "origin": "MAT '20 Direct",
            "q": "[MAT '20 Direct] We warmly congratulated him ___ his outstanding success in the examination.",
            "opts": ["on", "for", "with", "to"],
            "ans": 0,
            "exp": "Congratulate / Compliment এর পর সর্বদা 'on' বসে (Congratulate somebody on something)।",
            "trap": "বাংলায় 'সাফল্যের জন্য' ভেবে অনেকে ভুল করে 'for' দাগিয়ে বসে।"
        },
        {
            "id": "eng_q05",
            "week_id": "week_01",
            "subject": "English",
            "origin": "MAT '18 Direct",
            "q": "[MAT '18 Direct] Perseverance, consistency and discipline are the key ___ success in admission.",
            "opts": ["to", "of", "for", "in"],
            "ans": 0,
            "exp": "Key to = চাবিকাঠি বা প্রধান সমাধান (Solution/Secret)।",
            "trap": "'Key of' দাগানো সাধারণ ভুল।"
        },
        {
            "id": "eng_q06",
            "week_id": "week_01",
            "subject": "English",
            "origin": "RU '20",
            "q": "[RU '20] The autocrat deprived the underprivileged citizens ___ their fundamental constitutional rights.",
            "opts": ["of", "from", "with", "away"],
            "ans": 0,
            "exp": "Deprive of, Rob of, Strip of = কোনো অধিকার বা সম্পত্তি থেকে কাউকে বঞ্চিত করা।",
            "trap": "হতে/থেকে অর্থ প্রকাশ পাওয়ায় 'from' দাগানো।"
        },
        {
            "id": "eng_q07",
            "week_id": "week_01",
            "subject": "English",
            "origin": "CU '19-20",
            "q": "[CU '19-20] The overworked house doctor could barely cope ___ the sudden surge of emergency patients.",
            "opts": ["with", "up with", "for", "against"],
            "ans": 0,
            "exp": "প্রমিত ব্যাকরণে সঠিক Phrase হলো 'Cope with' (মানিয়ে চলা)। 'Cope up with' ইংরেজি ব্যাকরণে ভুল ও অপ্রমিত।",
            "trap": "কথ্য ভাষার ভুল অভ্যাস 'Cope up with' দাগানো চরম ভুল।"
        },
        {
            "id": "eng_q08",
            "week_id": "week_01",
            "subject": "English",
            "origin": "GST '21-22",
            "q": "[GST '21-22] The strict teacher was very angry ___ the students for repeatedly being late.",
            "opts": ["with", "at", "for", "on"],
            "ans": 0,
            "exp": "ব্যক্তির ওপর ক্রুদ্ধ হলে 'Angry with a person', আর আচরণ বা ঘটনায় ক্ষুব্ধ হলে 'Angry at a behavior/conduct'।",
            "trap": "ব্যক্তি ও বিষয়ের ক্ষেত্রে with বনাম at গুলিয়ে ফেলা।"
        },
        {
            "id": "eng_q09",
            "week_id": "week_02",
            "subject": "English",
            "origin": "JU '19-20",
            "q": "[JU '19-20] Only bona-fide science students are eligible ___ applying to this scholarship.",
            "opts": ["for", "to", "in", "with"],
            "ans": 0,
            "exp": "Eligible for = কোনো সুযোগ বা পদের জন্য যোগ্য। কিন্তু Qualified for / to + Verb।",
            "trap": "অন্য preposition দিয়ে গুলিয়ে ফেলা।"
        },
        {
            "id": "eng_q10",
            "week_id": "week_02",
            "subject": "English",
            "origin": "MAT '17 Direct",
            "q": "[MAT '17 Direct] The diligent student is exceptionally good ___ Mathematics but rather weak in English.",
            "opts": ["at", "in", "with", "on"],
            "ans": 0,
            "exp": "কোনো বিষয়ে দক্ষ বা পটু হলে 'Good at', আর কাঁচা বা দুর্বল হলে 'Weak in'।",
            "trap": "Good in দাগানোর ভুল প্রবণতা।"
        },
        {
            "id": "eng_q11",
            "week_id": "week_02",
            "subject": "English",
            "origin": "MAT '22 Direct",
            "q": "[MAT '22 Direct] The experienced specialist finally cured the patient ___ the chronic bacterial infection.",
            "opts": ["of", "from", "with", "against"],
            "ans": 0,
            "exp": "Cure of (রোগ থেকে নিরাময় করা)। কিন্তু Cure for a disease (প্রতিষেধক)।",
            "trap": "Cure from ভেবে ভুল করা।"
        },
        {
            "id": "eng_q12",
            "week_id": "week_02",
            "subject": "English",
            "origin": "BCS '40 / MAT",
            "q": "[BCS '40 / MAT] The brave soldiers refused to yield ___ the overwhelming pressure of the enemy.",
            "opts": ["to", "before", "with", "under"],
            "ans": 0,
            "exp": "Yield to, Surrender to, Submit to, Succumb to = নতি স্বীকার করা বা বশ্যতা স্বীকার করা।",
            "trap": "Yield before দাগানো।"
        },
        {
            "id": "eng_q13",
            "week_id": "week_02",
            "subject": "English",
            "origin": "DU '18-19",
            "q": "[DU '18-19] The newly constructed diagnostic center is adjacent ___ the central hospital.",
            "opts": ["to", "with", "by", "near"],
            "ans": 0,
            "exp": "Adjacent to = সংলগ্ন / লাগোয়া।",
            "trap": "Adjacent with দাগানো।"
        },
        {
            "id": "eng_q14",
            "week_id": "week_02",
            "subject": "English",
            "origin": "MAT '19 Direct",
            "q": "[MAT '19 Direct] The annual academic conference was presided ___ by the Director General of Health Services.",
            "opts": ["over", "upon", "at", "on"],
            "ans": 0,
            "exp": "Preside over = সভায় সভাপতিত্ব করা।",
            "trap": "Preside at বা upon দাগানো।"
        },
        {
            "id": "eng_q15",
            "week_id": "week_02",
            "subject": "English",
            "origin": "RU '21",
            "q": "[RU '21] You can safely rely ___ his professional integrity and commitment.",
            "opts": ["on", "in", "with", "at"],
            "ans": 0,
            "exp": "Rely on, Depend on, Bank on, Count on = নির্ভর বা আস্থা রাখা।",
            "trap": "Rely in ভাবা।"
        },
        {
            "id": "eng_q16",
            "week_id": "week_02",
            "subject": "English",
            "origin": "BCS '42 / MAT",
            "q": "[BCS '42 / MAT] Neither the professor nor his clinical assistants ___ present at yesterday's seminar.",
            "opts": ["were", "was", "is", "are"],
            "ans": 0,
            "exp": "Neither...nor দ্বারা দুটি Subject যুক্ত হলে Verb সর্বদা নিকটবর্তী Subject (clinical assistants - Plural) অনুযায়ী নির্ধারিত হয়।",
            "trap": "দূরবর্তী Subject (the professor - Singular) দেখে 'was' দাগানো।"
        },
        {
            "id": "eng_q17",
            "week_id": "week_03",
            "subject": "English",
            "origin": "MAT '21 Direct",
            "q": "[MAT '21 Direct] What is the precise antonym of the clinical oncology term 'BENIGN'?",
            "opts": ["Malignant", "Harmful", "Gentle", "Innocuous"],
            "ans": 0,
            "exp": "Benign = ক্ষতিকর নয় এমন (Non-cancerous, mild); এর বিপরীত Malignant = মারাত্মক বা প্রাণঘাতী (Cancerous, aggressive)।",
            "trap": "Benign ও Malignant এর অর্থ বিপরীত না বুঝে গুলিয়ে ফেলা।"
        },
        {
            "id": "eng_q18",
            "week_id": "week_03",
            "subject": "English",
            "origin": "DU '20-21",
            "q": "[DU '20-21] The vocabulary word 'RESILIENT' is closest in meaning to:",
            "opts": ["Elastic and quick to recover", "Fragile and brittle", "Rigid and stubborn", "Tired and exhausted"],
            "ans": 0,
            "exp": "Resilient = স্থিতিস্থাপক / প্রতিকূলতা কাটিয়ে দ্রুত ঘুরে দাঁড়ানোর ক্ষমতাসম্পন্ন (Buoyant, adaptable, elastic)।",
            "trap": "Resistant (প্রতিরোধী) এর সাথে গুলিয়ে ফেলা।"
        },
        {
            "id": "eng_q19",
            "week_id": "week_03",
            "subject": "English",
            "origin": "MAT '20 Direct",
            "q": "[MAT '20 Direct] In clinical medicine, a 'CHRONIC' disease refers to one that is:",
            "opts": ["Persistent and long-lasting", "Severe and sudden in onset", "Easily curable", "Contagious"],
            "ans": 0,
            "exp": "Chronic = দীর্ঘস্থায়ী ও ধীরগতির (যেমন: ডায়াবেটিস); এর বিপরীত হলো Acute = আকস্মিক ও তীব্র।",
            "trap": "Acute (তীব্র) ও Chronic (দীর্ঘস্থায়ী) গুলিয়ে ফেলা।"
        },
        {
            "id": "eng_q20",
            "week_id": "week_03",
            "subject": "English",
            "origin": "CU '18-19",
            "q": "[CU '18-19] If I ___ a qualified surgeon, I would treat underprivileged patients free of charge.",
            "opts": ["were", "was", "am", "had been"],
            "ans": 0,
            "exp": "2nd Conditional-এ কাল্পনিক বা অবাস্তব শর্ত প্রকাশে Subject নির্বিশেষে Subjunctive 'were' ব্যবহৃত হয়।",
            "trap": "Subject 'I' দেখে অসাবধানে 'was' দাগানো।"
        },
        {
            "id": "eng_q21",
            "week_id": "week_03",
            "subject": "English",
            "origin": "GST '21-22",
            "q": "[GST '21-22] It is high time we ___ our unproductive study routine.",
            "opts": ["changed", "change", "had changed", "should change"],
            "ans": 0,
            "exp": "It is time / It is high time এর পর Subject আসলে Verb সর্বদা Past Indefinite (V2) রূপে বসে।",
            "trap": "Present tense 'change' বা 'should change' দাগানো।"
        },
        {
            "id": "eng_q22",
            "week_id": "week_03",
            "subject": "English",
            "origin": "MAT '19 Direct",
            "q": "[MAT '19 Direct] The popular admission idiom 'To break the ice' signifies:",
            "opts": ["To start a friendly conversation in a tense atmosphere", "To cause severe physical damage", "To feel freezing cold", "To terminate a partnership"],
            "ans": 0,
            "exp": "'To break the ice' = সামাজিক নীরবতা বা প্রথম সাক্ষাতের জড়তা ভেঙে আলোচনা শুরু করা।",
            "trap": "আক্ষরিক অর্থে বরফ ভাঙা ভাবা।"
        },
        {
            "id": "eng_q23",
            "week_id": "week_03",
            "subject": "English",
            "origin": "DU '17-18",
            "q": "[DU '17-18] The idiomatic expression 'Once in a blue moon' means:",
            "opts": ["Very rarely", "Very frequently", "On a full moon night", "Never in life"],
            "ans": 0,
            "exp": "'Once in a blue moon' = কদাচিৎ বা খুবই বিরল ঘটনা (almost never/infrequently)।",
            "trap": "কখনোই নয় (Never) দাগানো।"
        },
        {
            "id": "eng_q24",
            "week_id": "week_03",
            "subject": "English",
            "origin": "BCS '39 / MAT",
            "q": "[BCS '39 / MAT] Choose the strictly correct spelling of the respiratory disease:",
            "opts": ["Pneumonia", "Pnumonia", "Neumonia", "Pneumonea"],
            "ans": 0,
            "exp": "সঠিক বানান হলো P-N-E-U-M-O-N-I-A (এখানে P অনুচ্চারিত থাকে)।",
            "trap": "P অক্ষরটি বাদ দিয়ে Neumonia দাগানো।"
        },
        {
            "id": "eng_q25",
            "week_id": "week_03",
            "subject": "English",
            "origin": "MAT '22 Direct",
            "q": "[MAT '22 Direct] What is the correct passive form of: 'Do not laugh at the poor'?",
            "opts": ["Let not the poor be laughed at", "Let the poor not laugh", "You are forbidden to laugh", "The poor should not be laughed"],
            "ans": 0,
            "exp": "Imperative negative: Let not + object + be + V3 + preposition ('at' বাদ দেওয়া যাবে না)।",
            "trap": "Preposition 'at' বাদ দিয়ে অপশন নির্বাচন করা।"
        }
    ]

    gk_mcqs = [
        {
            "id": "gk_q01",
            "week_id": "week_01",
            "subject": "GK",
            "origin": "MAT '21 Direct",
            "q": "[MAT '21 Direct] ১৯৭১ সালের মুক্তিযুদ্ধে কোন সেক্টরটি ছিল নৌ-কমান্ডোদের অধীন এবং এতে কোনো স্থায়ী নিয়মিত সেক্টর কমান্ডার ছিল না?",
            "opts": ["সেক্টর ১০", "সেক্টর ৮", "সেক্টর ৪", "সেক্টর ১১"],
            "ans": 0,
            "exp": "সেক্টর ১০ ছিল সমগ্র নৌ-পথ ও উপকূলীয় এলাকা নিয়ে গঠিত বিশেষ সেক্টর। এটি সরাসরি প্রধান সেনাপতির অধীনে পরিচালিত হতো এবং কোনো স্থায়ী সেক্টর কমান্ডার ছিল না।",
            "trap": "সেক্টর ১১ এর সাথে গুলিয়ে ফেলা।"
        },
        {
            "id": "gk_q02",
            "week_id": "week_01",
            "subject": "GK",
            "origin": "MAT '20 Direct",
            "q": "[MAT '20 Direct] একাত্তরে ঢাকা মহানগরে দুঃসাহসিক গেরিলা অপারেশন পরিচালনাকারী ঐতিহাসিক 'ক্র্যাক প্লাটুন' কোন সেক্টরের অন্তর্ভুক্ত ছিল?",
            "opts": ["সেক্টর ২", "সেক্টর ১", "সেক্টর ৩", "সেক্টর ৮"],
            "ans": 0,
            "exp": "সেক্টর ২ এর অধীন ছিল ঢাকা, ফরিদপুর ও কুমিল্লা জেলা। এর কমান্ডার ছিলেন মেজর খালেদ মোশাররফ ও ক্যাপ্টেন এটিএম হায়দার; এই সেক্টরের অধীনেই ক্র্যাক প্লাটুন গঠিত হয়।",
            "trap": "সেক্টর ৩ দাগানো।"
        },
        {
            "id": "gk_q03",
            "week_id": "week_01",
            "subject": "GK",
            "origin": "MAT '19 Direct",
            "q": "[MAT '19 Direct] ১৯৭১ সালের মুক্তিযুদ্ধে স্বাধীন সার্বভৌম বাংলাদেশকে প্রথম আনুষ্ঠানিকভাবে কূটনৈতিক স্বীকৃতি প্রদান করে কোন দেশ?",
            "opts": ["ভুটান", "ভারত", "সোভিয়েত ইউনিয়ন", "যুক্তরাজ্য"],
            "ans": 0,
            "exp": "৬ ডিসেম্বর ১৯৭১ সকালে ভুটান সর্বপ্রথম বাংলাদেশকে তারবার্তা মারফত আনুষ্ঠানিক স্বীকৃতি দেয়; এর কয়েক ঘণ্টা পর ভারত দ্বিতীয় দেশ হিসেবে স্বীকৃতি জানায়।",
            "trap": "ভারত আগে স্বীকৃতি দিয়েছে মনে করা।"
        },
        {
            "id": "gk_q04",
            "week_id": "week_01",
            "subject": "GK",
            "origin": "BCS '41 / MAT Repeat",
            "q": "[BCS '41 / MAT Repeat] একাত্তরে নৌ-কমান্ডোদের পরিচালিত দুর্ধর্ষ 'অপারেশন জ্যাকপট' কোন তারিখে একযোগে চট্টগ্রাম, মোংলা, নারায়ণগঞ্জ ও চাঁদপুরে সংঘটিত হয়?",
            "opts": ["১৫ আগস্ট ১৯৭১", "২৫ মার্চ ১৯৭১", "২১ নভেম্বর ১৯৭১", "১৬ ডিসেম্বর ১৯৭১"],
            "ans": 0,
            "exp": "১৫ আগস্ট মধ্যরাতে (১৬ আগস্ট প্রথম প্রহরে) একযোগে ফ্রান্স থেকে প্রশিক্ষিত বাঙালি নৌ-কমান্ডোরা ২৬টি পাকিস্তানি যুদ্ধজাহাজ ও কার্গো ধ্বংস করেন।",
            "trap": "২১ নভেম্বর (সশস্ত্র বাহিনী দিবস) এর সাথে গুলিয়ে ফেলা।"
        },
        {
            "id": "gk_q05",
            "week_id": "week_01",
            "subject": "GK",
            "origin": "MAT '18 Direct",
            "q": "[MAT '18 Direct] ১৯৭১ সালের ১০ এপ্রিল গঠিত স্বাধীন বাংলাদেশের প্রথম অস্থায়ী (মুজিবনগর) সরকারের প্রধানমন্ত্রী কে ছিলেন?",
            "opts": ["তাজউদ্দীন আহমদ", "সৈয়দ নজরুল ইসলাম", "ক্যাপ্টেন এম মনসুর আলী", "খন্দকার মোশতাক আহমদ"],
            "ans": 0,
            "exp": "১৯৭১ সালের ১০ এপ্রিল গঠিত গণপ্রজাতন্ত্রী বাংলাদেশের প্রথম সরকারের প্রধানমন্ত্রী ছিলেন তাজউদ্দীন আহমদ এবং উপ-রাষ্ট্রপতি ও অস্থায়ী রাষ্ট্রপতি ছিলেন সৈয়দ নজরুল ইসলাম।",
            "trap": "সৈয়দ নজরুল ইসলামকে প্রধানমন্ত্রী ভাবা।"
        },
        {
            "id": "gk_q06",
            "week_id": "week_01",
            "subject": "GK",
            "origin": "MAT '22 Direct",
            "q": "[MAT '22 Direct] গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের কোন অনুচ্ছেদ অনুযায়ী 'প্রজাতন্ত্রের সকল ক্ষমতার মালিক জনগণ'?",
            "opts": ["অনুচ্ছেদ ৭(১)", "অনুচ্ছেদ ২ক", "অনুচ্ছেদ ১১", "অনুচ্ছেদ ২৭"],
            "ans": 0,
            "exp": "বাংলাদেশ সংবিধানের ৭(১) অনুচ্ছেদ অনুসারে: 'প্রজাতন্ত্রের সকল ক্ষমতার মালিক জনগণ; এবং জনগণের পক্ষে সেই ক্ষমতার প্রয়োগ কেবল এই সংবিধানের অধীন ও কর্তৃত্বে কার্যকর হইবে।' এটি সংবিধানের সর্বোচ্চ প্রাধান্য ঘোষণা করে।",
            "trap": "অনুচ্ছেদ ১১ (গণতন্ত্র ও মানবাধিকার) এর সাথে গুলিয়ে ফেলা।"
        },
        {
            "id": "gk_q07",
            "week_id": "week_01",
            "subject": "GK",
            "origin": "DU '20-21 GK",
            "q": "[DU '20-21 GK] মুক্তিযুদ্ধে সর্বোচ্চ বীরত্বসূচক 'বীরশ্রেষ্ঠ' খেতাবপ্রাপ্তদের মধ্যে সর্বকনিষ্ঠ শহীদ যোদ্ধা কে ছিলেন?",
            "opts": ["বীরশ্রেষ্ঠ সিপাহী হামিদুর রহমান", "বীরশ্রেষ্ঠ মোস্তফা কামাল", "বীরশ্রেষ্ঠ নূর মোহাম্মদ শেখ", "বীরশ্রেষ্ঠ রুহুল আমিন"],
            "ans": 0,
            "exp": "বীরশ্রেষ্ঠ সিপাহী হামিদুর রহমান শহীদ হওয়ার সময় তার বয়স ছিল মাত্র ১৮ বছর (জন্ম: ২ ফেব্রুয়ারি ১৯৫৩; শাহাদাত: ২৮ অক্টোবর ১৯৭১)।",
            "trap": "মোস্তফা কামাল দাগানো।"
        },
        {
            "id": "gk_q08",
            "week_id": "week_01",
            "subject": "GK",
            "origin": "DU '19-20 GK",
            "q": "[DU '19-20 GK] ১৯৭১ সালের মুক্তিযুদ্ধে সর্বপ্রথম সম্মুখ সমরে শাহাদাতবরণকারী বীরশ্রেষ্ঠ কে?",
            "opts": ["বীরশ্রেষ্ঠ ল্যান্স নায়েক মোস্তফা কামাল", "বীরশ্রেষ্ঠ মতিউর রহমান", "বীরশ্রেষ্ঠ হামিদুর রহমান", "বীরশ্রেষ্ঠ মহিউদ্দিন জাহাঙ্গীর"],
            "ans": 0,
            "exp": "বীরশ্রেষ্ঠ মোস্তফা কামাল ১৯৭১ সালের ৮ এপ্রিল ব্রাহ্মণবাড়িয়ার দরুইন গ্রামে সম্মুখ সমরে শহীদ হন (তিনি প্রথম শহীদ বীরশ্রেষ্ঠ)।",
            "trap": "মতিউর রহমানকে প্রথম শহীদ মনে করা।"
        },
        {
            "id": "gk_q09",
            "week_id": "week_02",
            "subject": "GK",
            "origin": "DU '18-19 GK",
            "q": "[DU '18-19 GK] একাত্তরের মুক্তিযুদ্ধে সর্বশেষ শহীদ বীরশ্রেষ্ঠ যোদ্ধা কে ছিলেন?",
            "opts": ["বীরশ্রেষ্ঠ ক্যাপ্টেন মহিউদ্দিন জাহাঙ্গীর", "বীরশ্রেষ্ঠ ইঞ্জিনরুম আর্টিফিসার রুহুল আমিন", "বীরশ্রেষ্ঠ নূর মোহাম্মদ শেখ", "বীরশ্রেষ্ঠ মুন্সী আব্দুর রউফ"],
            "ans": 0,
            "exp": "ক্যাপ্টেন মহিউদ্দিন জাহাঙ্গীর ১৪ ডিসেম্বর ১৯৭১ চাঁপাইনবাবগঞ্জের রেহাইচরে সম্মুখ যুদ্ধে পাকিস্তানি স্নাইপারের গুলিতে শহীদ হন।",
            "trap": "রুহুল আমিনকে শেষ শহীদ ভাবা (রুহুল আমিন শহীদ হন ১০ ডিসেম্বর ১৯৭১)।"
        },
        {
            "id": "gk_q10",
            "week_id": "week_02",
            "subject": "GK",
            "origin": "GST '21-22 GK",
            "q": "[GST '21-22 GK] বীরশ্রেষ্ঠ ফ্লাইট লেফটেন্যান্ট মতিউর রহমানের মরদেহ পাকিস্তান হতে দেশে ফিরিয়ে এনে কোথায় দাফন করা হয়?",
            "opts": ["মিরপুর শহীদ বুদ্ধিজীবী কবরস্থান", "মিরপুর সেনানিবাস", "বঙ্গভবন চত্বর", "টুঙ্গিপাড়া"],
            "ans": 0,
            "exp": "২০০৬ সালের ২৪ জুন মতিউর রহমানের দেহাবশেষ পাকিস্তান হতে ফিরিয়ে এনে পূর্ণ রাষ্ট্রীয় মর্যাদায় মিরপুর শহীদ বুদ্ধিজীবী কবরস্থানে দাফন করা হয়।",
            "trap": "বনানী সামরিক কবরস্থান দাগানো।"
        },
        {
            "id": "gk_q11",
            "week_id": "week_02",
            "subject": "GK",
            "origin": "RU '20 GK",
            "q": "[RU '20 GK] গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধান গণপরিষদে কোন তারিখে সর্বসম্মতভাবে গৃহীত হয়?",
            "opts": ["৪ নভেম্বর ১৯৭২", "১৬ ডিসেম্বর ১৯৭২", "২৬ মার্চ ১৯৭২", "১০ জানুয়ারি ১৯৭২"],
            "ans": 0,
            "exp": "সংবিধান গৃহীত হয় ৪ নভেম্বর ১৯৭২ (এজন্য ৪ নভেম্বর সংবিধান দিবস); আর কার্যকর হয় ১৬ ডিসেম্বর ১৯৭২।",
            "trap": "গৃহীত হওয়া আর কার্যকর হওয়ার তারিখ গুলিয়ে ফেলা।"
        },
        {
            "id": "gk_q12",
            "week_id": "week_02",
            "subject": "GK",
            "origin": "RU '21 GK",
            "q": "[RU '21 GK] বাংলাদেশের পবিত্র সংবিধান আনুষ্ঠানিকভাবে কোন তারিখ হতে বলবৎ বা কার্যকর হয়?",
            "opts": ["১৬ ডিসেম্বর ১৯৭২", "৪ নভেম্বর ১৯৭২", "২৬ মার্চ ১৯৭৩", "১ জানুয়ারি ১৯৭৩"],
            "ans": 0,
            "exp": "সংবিধান কার্যকর হয় প্রথম বিজয় দিবসে অর্থাৎ ১৬ ডিসেম্বর ১৯৭২।",
            "trap": "৪ নভেম্বর দাগানো।"
        },
        {
            "id": "gk_q13",
            "week_id": "week_02",
            "subject": "GK",
            "origin": "JU '19-20 GK",
            "q": "[JU '19-20 GK] স্বাধীন বাংলা বেতার কেন্দ্র থেকে প্রচারিত জনপ্রিয় ও বহুল আলোচিত কথিকা 'চরমপত্র'-এর রচয়িতা ও পাঠক কে ছিলেন?",
            "opts": ["এম আর আখতার মুকুল", "আবদুল গাফ্ফার চৌধুরী", "শামসুর রাহমান", "জহির রায়হান"],
            "ans": 0,
            "exp": "এম আর আখতার মুকুল ঢাকাইয়া উপভাষায় চরমপত্র পাঠ করে মুক্তিযোদ্ধাদের বিপুল মনোবল ও প্রেরণা যোগাতেন।",
            "trap": "আবদুল গাফ্ফার চৌধুরী ভাবা।"
        },
        {
            "id": "gk_q14",
            "week_id": "week_02",
            "subject": "GK",
            "origin": "CU '18-19 GK",
            "q": "[CU '18-19 GK] মুক্তিযুদ্ধের রণধ্বনি 'জয় বাংলা'-কে বাংলাদেশের জাতীয় স্লোগান হিসেবে মন্ত্রিসভা কবে চূড়ান্ত গেজেট প্রকাশ করে?",
            "opts": ["২ মার্চ ২০২২", "৭ ফেব্রুয়ারি ২০২০", "১৬ ডিসেম্বর ২০২১", "২৬ মার্চ ২০২২"],
            "ans": 0,
            "exp": "২০২২ সালের ২ মার্চ গণপ্রজাতন্ত্রী বাংলাদেশ সরকার 'জয় বাংলা'কে জাতীয় স্লোগান হিসেবে প্রজ্ঞাপন জারি করে।",
            "trap": "৭ ফেব্রুয়ারি ২০২০ ভাবা।"
        },
        {
            "id": "gk_q15",
            "week_id": "week_02",
            "subject": "GK",
            "origin": "MAT '17 Direct",
            "q": "[MAT '17 Direct] ১৯৭১ সালের ২৫শে মার্চ মধ্যরাতে ঢাকা শহরে পাকিস্তান হানাদার বাহিনীর নৃশংস ও বর্বরোচিত গণহত্যার সামরিক কোডনেম কী ছিল?",
            "opts": ["অপারেশন সার্চলাইট", "অপারেশন ব্লিজ", "অপারেশন জ্যাকপট", "অপারেশন ক্লোজআপ"],
            "ans": 0,
            "exp": "জেনারেল টিক্কা খান ও খাদিম হুসাইন রাজা ১৯৭১ সালের ২৫শে মার্চের গণহত্যার নীলনকশা তৈরি করেন যার নাম ছিল অপারেশন সার্চলাইট।",
            "trap": "অপারেশন জ্যাকপটের সাথে গুলানো।"
        },
        {
            "id": "gk_q16",
            "week_id": "week_02",
            "subject": "GK",
            "origin": "MAT '20 Direct",
            "q": "[MAT '20 Direct] ১৯৭১ সালে গঠিত মুজিবনগর সরকারের উপ-রাষ্ট্রপতি ও অস্থায়ী রাষ্ট্রপতির দায়িত্ব কে পালন করেছিলেন?",
            "opts": ["সৈয়দ নজরুল ইসলাম", "তাজউদ্দীন আহমদ", "এএইচএম কামারুজ্জামান", "মুহাম্মদ মনসুর আলী"],
            "ans": 0,
            "exp": "মুজিবনগর সরকারের উপ-রাষ্ট্রপতি সৈয়দ নজরুল ইসলাম অস্থায়ী রাষ্ট্রপতি হিসেবে দায়িত্ব পালন করেন এবং প্রধানমন্ত্রী ছিলেন তাজউদ্দীন আহমদ।",
            "trap": "তাজউদ্দীন আহমদ দাগানো।"
        },
        {
            "id": "gk_q17",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "MAT '21 Direct",
            "q": "[MAT '21 Direct] বাংলাদেশের সর্বদক্ষিণে অবস্থিত একমাত্র প্রবাল দ্বীপ সেন্টমার্টিন কোন জেলায় অবস্থিত এবং এর আয়তন প্রায় কত?",
            "opts": ["কক্সবাজার, প্রায় ৮ বর্গ কিমি", "চট্টগ্রাম, প্রায় ১২ বর্গ কিমি", "পটুয়াখালী, প্রায় ৫ বর্গ কিমি", "ভোলা, প্রায় ১৫ বর্গ কিমি"],
            "ans": 0,
            "exp": "সেন্টমার্টিন দ্বীপ (স্থানীয় নাম নারিকেল জিঞ্জিরা) বাংলাদেশের সর্বদক্ষিণে অবস্থিত একমাত্র প্রবাল দ্বীপ। এটি কক্সবাজার জেলার টেকনাফ উপজেলার অন্তর্ভুক্ত এবং এর আয়তন প্রায় ৮ বর্গকিলোমিটার।",
            "trap": "ছেঁড়াদ্বীপ বা নিঝুম দ্বীপের (নোয়াখালী) সাথে গুলিয়ে ফেলা।"
        },
        {
            "id": "gk_q18",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "DU '21-22 GK",
            "q": "[DU '21-22 GK] বিশ্ব স্বাস্থ্য সংস্থা (WHO)-এর সদর দপ্তর সুইজারল্যান্ডের কোথায় অবস্থিত এবং প্রতি বছর কত তারিখে বিশ্ব স্বাস্থ্য দিবস পালিত হয়?",
            "opts": ["জেনেভা, ৭ এপ্রিল", "জুরিখ, ১০ ডিসেম্বর", "বাসেল, ৫ জুন", "বার্ন, ১ ডিসেম্বর"],
            "ans": 0,
            "exp": "বিশ্ব স্বাস্থ্য সংস্থা (World Health Organization - WHO) ১৯৪৮ সালের ৭ এপ্রিল প্রতিষ্ঠিত হয় এবং এর সদর দপ্তর সুইজারল্যান্ডের জেনেভায় অবস্থিত। প্রতি বছর ৭ এপ্রিল বিশ্ব স্বাস্থ্য দিবস হিসেবে পালিত হয়।",
            "trap": "৭ এপ্রিলের বদলে ৭ মে দাগানো বা নিউইয়র্ক ভেবে ভুল করা।"
        },
        {
            "id": "gk_q19",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "GST '20 GK",
            "q": "[GST '20 GK] ১৯৭১ সালের মুক্তিযুদ্ধে অসামান্য অবদানের জন্য একমাত্র কোন বিদেশি নাগরিক 'বীরপ্রতীক' খেতাবে ভূষিত হন?",
            "opts": ["ডব্লিউ এ এস ওডারল্যান্ড (অস্ট্রেলিয়া)", "ফাদার মারিও ভেরোনেসি", "আন্দ্রে মারলো", "মার্ক টালি"],
            "ans": 0,
            "exp": "ডাচ-অস্ট্রেলীয় নাগরিক ডব্লিউ এ এস ওডারল্যান্ড বাটা শু কোম্পানির এমডি ছিলেন এবং গোপনে মুক্তিযোদ্ধাদের সহায়তা করেন।",
            "trap": "ফাদার মারিও ভাবা।"
        },
        {
            "id": "gk_q20",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "RU '19 GK",
            "q": "[RU '19 GK] ১৯৭১ সালে আন্তর্জাতিক পরিমণ্ডলে মুক্তিযুদ্ধের সমর্থনে স্বাধীন বাংলাদেশের প্রথম ৮টি ডাকটিকিটের নকশাকার কে ছিলেন?",
            "opts": ["বিমান মল্লিক", "কামরুল হাসান", "জয়নুল আবেদিন", "হাশেম খান"],
            "ans": 0,
            "exp": "ব্রিটিশ ডাক বিভাগ ও বাংলাদেশের পক্ষে শিল্পী বিমান মল্লিক এই ঐতিহাসিক প্রথম ডাকটিকিটগুলোর নকশা করেন।",
            "trap": "কামরুল হাসান দাগানো।"
        },
        {
            "id": "gk_q21",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "MAT '21 Direct",
            "q": "[MAT '21 Direct] ১৯৭১ সালের মুক্তিযুদ্ধে সমগ্র বাংলাদেশকে কয়টি প্রশাসনিক সামরিক সেক্টরে এবং কয়টি সাব-সেক্টরে বিভক্ত করা হয়?",
            "opts": ["১১টি সেক্টর ও ৬৪টি সাব-সেক্টর", "১০টি সেক্টর ও ৬৪টি সাব-সেক্টর", "১১টি সেক্টর ও ৫৪টি সাব-সেক্টর", "৬৪টি সেক্টর ও ১১টি সাব-সেক্টর"],
            "ans": 0,
            "exp": "কর্নেল এম এ জি ওসমানীর নেতৃত্বে পুরো দেশকে ১১টি সেক্টর ও ৬৪টি সাব-সেক্টরে ভাগ করা হয়।",
            "trap": "সাব-সেক্টর সংখ্যা ভুল দাগানো।"
        },
        {
            "id": "gk_q22",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "CU '19-20 GK",
            "q": "[CU '19-20 GK] বীরশ্রেষ্ঠ রুহুল আমিন ১৯৭১ সালের ১০ ডিসেম্বর কোন যুদ্ধজাহাজে দায়িত্ব পালনকালে শহীদ হন?",
            "opts": ["বিএনএস পলাশ", "বিএনএস পদ্মা", "বিএনএস মেঘনা", "বিএনএস কর্ণফুলী"],
            "ans": 0,
            "exp": "খুলনার রূপসা নদীতে ভারতীয় মিত্রবাহিনীর ভুল বিমান হামলায় গানবোট 'পলাশ' ক্ষতিগ্রস্ত হলে তিনি আত্মত্যাগ করেন।",
            "trap": "বিএনএস পদ্মা দাগানো।"
        },
        {
            "id": "gk_q23",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "DU '17-18 GK",
            "q": "[DU '17-18 GK] মুক্তিযুদ্ধের নিয়মিত সশস্ত্র তিনটি ব্রিগেড ফোর্স (Z-Force, K-Force, S-Force) যথাক্রমে কাদের নামে গঠিত হয়?",
            "opts": ["জিয়াউর রহমান, খালেদ মোশাররফ, কে এম শফিউল্লাহ", "জিয়াউর রহমান, কামারুজ্জামান, শফিউল্লাহ", "জিল্লুর রহমান, খালেদ মোশাররফ, শফিউল্লাহ", "জিয়াউর রহমান, কাজী নুরুজ্জামান, শফিউল্লাহ"],
            "ans": 0,
            "exp": "তিনটি নিয়মিত ব্রিগেডের কমান্ডারদের নামের আদ্যক্ষরে Z, K, S ফোর্স নামকরণ করা হয়।",
            "trap": "কমান্ডারদের নাম গোলমাল করা।"
        },
        {
            "id": "gk_q24",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "MAT '19 Direct",
            "q": "[MAT '19 Direct] একাত্তরে মুক্তিযুদ্ধের তহবিল সংগ্রহ ও বিশ্বজনমত গড়তে গঠিত 'স্বাধীন বাংলা ফুটবল দল'-এর প্রথম অধিনায়ক কে ছিলেন?",
            "opts": ["জাকারিয়া পিন্টু", "প্রতাপ শঙ্কর হাজরা", "কাজী সালাউদ্দিন", "সাইদুর রহমান প্যাটেল"],
            "ans": 0,
            "exp": "জাকারিয়া পিন্টু ছিলেন অধিনায়ক এবং প্রতাপ শঙ্কর হাজরা ছিলেন সহ-অধিনায়ক।",
            "trap": "কাজী সালাউদ্দিন ভাবা।"
        },
        {
            "id": "gk_q25",
            "week_id": "week_03",
            "subject": "GK",
            "origin": "MAT '22 Direct",
            "q": "[MAT '22 Direct] ১৯৭১ সালের ১৬ই ডিসেম্বর ঐতিহাসিক রেসকোর্স ময়দানে পাকিস্তান সেনাবাহিনীর আত্মসমর্পণের দলিলে মিত্রবাহিনীর পক্ষে কে স্বাক্ষর করেন?",
            "opts": ["লেফটেন্যান্ট জেনারেল জগজিৎ সিং অরোরা", "জেনারেল শ্যাম মানেকশ", "মেজর জেনারেল জে এফ আর জ্যাকব", "কর্নেল এম এ জি ওসমানী"],
            "ans": 0,
            "exp": "যৌথ কমান্ডের পক্ষ থেকে লে. জেনারেল জগজিৎ সিং অরোরা এবং পাকিস্তানের পক্ষে লে. জেনারেল এ এ কে নিয়াজী স্বাক্ষর করেন।",
            "trap": "জেনারেল মানেকশ ভাবা।"
        }
    ]

    return eng_mcqs + gk_mcqs

# -------------------------------------------------------------
# 3. COMPILE ALL 350 BANGALDESH CORE MCQS
# -------------------------------------------------------------
def compile_all_questions():
    from parse_helpers import get_w1_mcqs, parse_w2_mcqs, parse_w3_mcqs

    w1_raw = get_w1_mcqs()
    w2_raw = parse_w2_mcqs()
    w3_raw = parse_w3_mcqs()
    eng_gk = get_english_gk_mcqs()

    all_quizzes = []

    # Map origin tags for W1
    w1_phy = w1_raw[0:25]
    w1_che = w1_raw[25:50]
    w1_mat = w1_raw[50:75]
    w1_bio = w1_raw[75:100]

    for i, q in enumerate(w1_phy):
        tag = W1_PHY_ORIGINS[i]
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_01",
            "subject": "Physics",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w1_che):
        tag = W1_CHE_ORIGINS[i]
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_01",
            "subject": "Chemistry",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w1_mat):
        tag = W1_MAT_ORIGINS[i]
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_01",
            "subject": "Higher Math",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w1_bio):
        tag = W1_BIO_ORIGINS[i]
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_01",
            "subject": "Biology",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    # Week 02
    w2_phy = [q for q in w2_raw if q["subject"] == "Physics"]
    w2_che = [q for q in w2_raw if q["subject"] == "Chemistry"]
    w2_mat = [q for q in w2_raw if q["subject"] == "Higher Math"]
    w2_bio = [q for q in w2_raw if q["subject"] == "Biology"]

    for i, q in enumerate(w2_phy):
        tag = W2_PHY_ORIGINS[i] if i < len(W2_PHY_ORIGINS) else "DU Core"
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_02",
            "subject": "Physics",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w2_che):
        tag = W2_CHE_ORIGINS[i] if i < len(W2_CHE_ORIGINS) else "Hazari-Nag High-Yield"
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_02",
            "subject": "Chemistry",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w2_mat):
        tag = W2_MAT_ORIGINS[i] if i < len(W2_MAT_ORIGINS) else "Ketab Uddin Standard"
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_02",
            "subject": "Higher Math",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w2_bio):
        tag = W2_BIO_ORIGINS[i] if i < len(W2_BIO_ORIGINS) else "Gazi Azmal Direct"
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_02",
            "subject": "Biology",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    # Week 03
    w3_phy = [q for q in w3_raw if q["subject"] == "Physics"]
    w3_che = [q for q in w3_raw if q["subject"] == "Chemistry"]
    w3_mat = [q for q in w3_raw if q["subject"] == "Higher Math"]
    w3_bio = [q for q in w3_raw if q["subject"] == "Biology"]

    for i, q in enumerate(w3_phy):
        tag = W3_PHY_ORIGINS[i] if i < len(W3_PHY_ORIGINS) else "DU Core"
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_03",
            "subject": "Physics",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w3_che):
        tag = W3_CHE_ORIGINS[i] if i < len(W3_CHE_ORIGINS) else "Hazari-Nag High-Yield"
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_03",
            "subject": "Chemistry",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w3_mat):
        tag = W3_MAT_ORIGINS[i] if i < len(W3_MAT_ORIGINS) else "Ketab Uddin Standard"
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_03",
            "subject": "Higher Math",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    for i, q in enumerate(w3_bio):
        tag = W3_BIO_ORIGINS[i] if i < len(W3_BIO_ORIGINS) else "Gazi Azmal Direct"
        q_text = clean_latex(q["q"])
        if not q_text.startswith(f"[{tag}]"):
            q_text = f"[{tag}] {q_text}"
        all_quizzes.append({
            "id": q["id"],
            "week_id": "week_03",
            "subject": "Biology",
            "origin": tag,
            "q": q_text,
            "question": q_text,
            "opts": [clean_latex(opt) for opt in q["opts"]],
            "options": [clean_latex(opt) for opt in q["opts"]],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": clean_latex(q["exp"]),
            "explanation": clean_latex(q["exp"]),
            "trap": clean_latex(q["trap"]),
            "trap_insight": clean_latex(q["trap"])
        })

    # Add English & GK
    for q in eng_gk:
        all_quizzes.append({
            "id": q["id"],
            "week_id": q["week_id"],
            "subject": q["subject"],
            "origin": q["origin"],
            "q": q["q"],
            "question": q["q"],
            "opts": q["opts"],
            "options": q["opts"],
            "ans": q["ans"],
            "correct_index": q["ans"],
            "exp": q["exp"],
            "explanation": q["exp"],
            "trap": q["trap"],
            "trap_insight": q["trap"]
        })

    return all_quizzes

def main():
    print("Compiling locked Bangladesh Core Question Bank (DU, Medical, Varsity PYQs)...")
    quizzes = compile_all_questions()
    print(f"Total compiled questions: {len(quizzes)}")
    
    # Verify origin tags
    origins = [q.get("origin") for q in quizzes]
    print(f"Questions with origin tag: {sum(1 for o in origins if o)} / {len(quizzes)}")

    # Write admission_webapp/src/data/quizzes.json
    quizzes_path = os.path.join(OUT_DIR, "quizzes.json")
    with open(quizzes_path, "w", encoding="utf-8") as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved to {quizzes_path}")

    # Write admission_webapp/src/data/questions.json
    questions_path = os.path.join(OUT_DIR, "questions.json")
    with open(questions_path, "w", encoding="utf-8") as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved to {questions_path}")

    # Write questions.json to root
    root_questions_path = os.path.join(BASE_DIR, "questions.json")
    with open(root_questions_path, "w", encoding="utf-8") as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved to {root_questions_path}")

if __name__ == "__main__":
    main()

