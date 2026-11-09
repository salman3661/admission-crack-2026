#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_unbundled_dataset.py
1. Assembles all 75 unbundled PCMB chapters from:
   - blueprint_chapters_biology.py (24 chapters)
   - blueprint_chapters_chemistry.py (10 chapters)
   - blueprint_chapters_physics.py (21 chapters)
   - blueprint_chapters_math.py (20 chapters)
2. Builds synthetic predictors for all 75 chapters into chapter_synthetic_predictors.json
3. Re-indexes and redistributes questions in questions.json, varsity_bank.json, medical_bank.json, quizzes.json, weekly_exams.json
4. Syncs to src/data/ and admission_webapp/src/data/
"""

import os
import sys
import json
import shutil
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DATA_DIR = os.path.join(BASE_DIR, "src", "data")
APP_DATA_DIR = os.path.join(BASE_DIR, "admission_webapp", "src", "data")

import blueprint_chapters_biology
import blueprint_chapters_chemistry
import blueprint_chapters_physics
import blueprint_chapters_math

# Complete mapping table of all 75 chapters
ALL_CHAPTER_METADATA = {}

def get_all_75_chapters():
    bio = blueprint_chapters_biology.get_biology_chapters()
    chem = blueprint_chapters_chemistry.get_chemistry_chapters()
    phy = blueprint_chapters_physics.get_physics_chapters()
    math = blueprint_chapters_math.get_math_chapters()

    all_ch = []
    all_ch.extend(phy)
    all_ch.extend(chem)
    all_ch.extend(math)
    all_ch.extend(bio)

    for ch in all_ch:
        ALL_CHAPTER_METADATA[ch['id']] = ch
        for alias in ch.get('aliases', []):
            ALL_CHAPTER_METADATA[alias] = ch

    return all_ch

# Question classifier for existing banks
def classify_question(q):
    subj = q.get('subject')
    old_bp = q.get('blueprint_chapter_id') or ''
    stem = q.get('question') or q.get('q') or ''
    exp = q.get('explanation') or q.get('exp') or ''
    opts_str = ' '.join(q.get('options') or q.get('opts') or [])
    tag = q.get('tag') or ''
    # Content text takes precedence to prevent legacy erroneous chapter titles from misleading classification
    text = f"{stem} {opts_str} {exp}".lower()
    full_text = f"{q.get('chapter') or ''} {stem} {opts_str} {exp} {tag} {q.get('type_ref') or ''}".lower()

    if subj == 'Biology':
        # Botany
        if any(k in text for k in ['প্লাজমা মেমব্রেন', 'মেমব্রেন', 'রাইবোসোম', 'মাইটোকন্ড্রিয়া', 'ক্লোরোপ্লাস্ট', 'ডিএনএ', 'dna', 'rna', 'জেনেটিক কোড', 'ট্রান্সক্রিপশন', 'ট্রান্সলেশন', 'নিউক্লিয়াস', 'ক্রোমোজোম', 'লাইসোজোম', 'গলগি', 'কোষ প্রাচীর', 'ফ্লুইড মোজাইক', 'সেন্ট্রিওল']) and not any(k in text for k in ['বিভাজন', 'মাইটোসিস', 'মায়োসিস', 'কায়াজমা', 'ক্রসিং']):
            return 'bio_bot_01'
        if any(k in text for k in ['বিভাজন', 'মাইটোসিস', 'মায়োসিস', 'ইন্টারফেজ', 'মেটাফেজ', 'ক্রসিং ওভার', 'কায়াজমা', 'প্যাকাইটিন', 'ডিপ্লোটিন', 'সাইটোকাইনেসিস', 'লেপ্টোটিন', 'জাইগোটিন', 'সাইন্যাপসিস', 'বাইভ্যালেন্ট', 'বোকে']):
            return 'bio_bot_02'
        if any(k in text for k in ['গ্লুকোজ', 'ফ্রুক্টোজ', 'সুক্রোজ', 'মল্টোজ', 'ল্যাকটোজ', 'সেলুলোজ', 'অ্যামিনো অ্যাসিড', 'পেপটাইড', 'লিপিড', 'এনজাইম', 'কো-এনজাইম', 'রিডিউসিং সুগার', 'লক অ্যান্ড কি']):
            return 'bio_bot_03'
        if any(k in text for k in ['ভাইরাস', 'ব্যাকটেরিয়া', 't2', 'ফাজ', 'hiv', 'ম্যালেরিয়া', 'প্লাজমোডিয়াম', 'স্পোরোজয়েট', 'হেপাটিক', 'সাইজোগনি', 'অণুজীব', 'গ্রাম পজিটিভ', 'গ্রাম নেগেটিভ', 'লাইটিক', 'লাইসোজেনিক', 'ক্যাপসিড']):
            return 'bio_bot_04'
        if any(k in text for k in ['শৈবাল', 'ছত্রাক', 'ইউলোথ্রিক্স', 'স্পাইরোগাইরা', 'অ্যাগারিকাস', 'লাইকেন', 'হাইফি', 'পেনিসিলিয়াম', 'ঈস্ট', 'দাদ']):
            return 'bio_bot_05'
        if any(k in text for k in ['ব্রায়োফাইটা', 'টেরিডোফাইটা', 'রিক্সিয়া', 'ফার্ন', 'ড্রায়োপ্টেরিস', 'সোরাস', 'প্রোথ্যালাস', 'সারসিনেট', 'ক্রোজিয়ার']):
            return 'bio_bot_06'
        if any(k in text for k in ['নগ্নবীজী', 'আবৃতবীজী', 'সাইকাস', 'cycas', 'কোরালয়েড', 'পুষ্পপত্রবিন্যাস', 'এস্টিভেশন', 'অমরাবিন্যাস', 'প্লাসেন্টেশন', 'মালভেসি', 'পোয়াসি', 'জবা', 'ধান', 'গম', 'টুইস্টেড', 'ভেক্সিলারি']):
            return 'bio_bot_07'
        if any(k in text for k in ['টিস্যু', 'ভাজক টিস্যু', 'জাইলেম', 'ফ্লোয়েম', 'ভাস্কুলার বান্ডল', 'ক্যাম্বিয়াম', 'মজ্জা', 'সমপার্শ্বীয়', 'অরীয়', 'প্যারেনকাইমা']):
            return 'bio_bot_08'
        if any(k in text for k in ['সালোকসংশ্লেষণ', 'প্রস্বেদন', 'ক্যালভিন', 'ক্র্যাঞ্জ', 'c3', 'c4', 'গ্লাইকোলাইসিস', 'ক্রেবস', 'সাইটোক্রোম পাম্প', 'পত্ররন্ধ্র', 'খনিজ লবণ পরিশোষণ', 'atp']):
            return 'bio_bot_09'
        if any(k in text for k in ['পরাগরেণু', 'পরাগায়ন', 'ডিম্বক', 'ভ্রূণথলি', 'দ্বিনিষেক', 'ত্রিমিলন', 'এন্ডোস্পার্ম', 'পার্থেনোজেনেসিস', 'উদ্ভিদের প্রজনন']):
            return 'bio_bot_10'
        if any(k in text for k in ['জীবপ্রযুক্তি', 'প্লাজমিড', 'রিকম্বিন্যান্ট', 'রেস্ট্রিকশন', 'কাঁচি', 'লাইগেজ', 'টিস্যু কালচার', 'ক্যালাস', 'pcr', 'ট্রান্সজেনিক', 'গোল্ডেন রাইস', 'বিটি বেগুন']):
            return 'bio_bot_11'
        if any(k in text for k in ['বাস্তুতন্ত্র', 'ম্যানগ্রোভ', 'সুন্দরবন', 'শ্বাসমূল', 'নিউমাটোফোর', 'ইন-সিটু', 'এক্স-সিটু', 'অভয়ারণ্য', 'জাতীয় উদ্যান', 'রেড ডাটা', 'হ্যালোফাইট']):
            return 'bio_bot_12'
        
        # Zoology
        if any(k in text for k in ['শ্রেণিবিন্যাস', 'পর্ব', 'সিলোম', 'প্রতিসাম্য', 'পরিফেরা', 'নিডারিয়া', 'প্লাটিহেলমিন্থেস', 'নেমাটোডা', 'অ্যানেলিডা', 'আর্থ্রোপোডা', 'মলাস্কা', 'একাইনোডার্মাটা', 'কর্ডাটা', 'অস্টিকথিস']):
            return 'bio_zoo_01'
        if any(k in text for k in ['হাইড্রা', 'hydra', 'নেমাটোসিস্ট', 'নিডোসাইট', 'ঘাসফড়িং', 'ওমাটিডিয়াম', 'রুই মাছ', 'পটকা', 'বার্ব', 'স্টিনোটিল', 'লুপিং', 'সমারসল্টিং']):
            return 'bio_zoo_02'
        if any(k in text for k in ['পরিপাক', 'পাকস্থলী', 'পেপসিন', 'ট্রিপসিন', 'যকৃত', 'পিত্ত', 'ক্ষুদ্রান্ত্র', 'ভিলাই', 'গ্লাইকোজেনেসিস', 'লালারস', 'টায়ালিন', 'গ্যাস্ট্রিন', 'সিক্রেটিন']):
            return 'bio_zoo_03'
        if any(k in text for k in ['রক্ত', 'হৃদপিণ্ড', 'হার্ট', 'সিস্টোল', 'ডায়াস্টোল', 'পেসমেকার', 'sa নোড', 'av নোড', 'রক্তকণিকা', 'rbc', 'wbc', 'হিমোগ্লোবিন', 'তঞ্চন', 'ক্লটিং ফ্যাক্টর', 'করোনারি']):
            return 'bio_zoo_04'
        if any(k in text for k in ['ফুসফুস', 'অ্যালভিওলাই', 'সারফ্যাক্ট্যান্ট', 'প্রশ্বাস', 'নিঃশ্বাস', 'অক্সিজেন পরিবহন', 'কার্বন ডাই-অক্সাইড পরিবহন', 'হ্যামবার্গার', 'ক্লোরাইড শিফট', 'বোর প্রভাব', 'ব্রঙ্কাস']):
            return 'bio_zoo_05'
        if any(k in text for k in ['বৃক্ক', 'কিডনি', 'নেফ্রন', 'মূত্র', 'ইউরিয়া', 'বোম্যান্স', 'গ্লোমেরুলাস', 'ডায়ালাইসিস', 'adh', 'অস্মোরেগুলেশন', 'বর্জ্য', 'নিষ্কাশন']):
            return 'bio_zoo_06'
        if any(k in text for k in ['অস্থি', 'কঙ্কাল', 'কশেরুকা', 'করোটিকা', 'পেশি', 'সাইনোভিয়াল', 'হিউমেরাস', 'ফিমার', 'প্যাটেলা', 'টেনডন', 'লিগামেন্ট', 'সারকোমিয়ার', 'অ্যাকটিন', 'মায়োসিন']):
            return 'bio_zoo_07'
        if any(k in text for k in ['মস্তিষ্ক', 'স্নায়ু', 'নিউরন', 'সাইন্যাপস', 'করোটিক', 'হরমোন', 'পিটুইটারি', 'থাইরয়েড', 'অ্যাড্রেনাল', 'চোখ', 'রেটিনা', 'রড কোষ', 'কোন কোষ', 'কান', 'ককলিয়া', 'সেরিবেলাম']):
            return 'bio_zoo_08'
        if any(k in text for k in ['শুক্রাণু', 'ডিম্বাণু', 'স্পার্মাটোজেনেসিস', 'ওওজেনেসিস', 'ঋতুচক্র', 'মেনস্ট্রুয়াল', 'কর্পাস লুটিয়াম', 'প্রোজেস্টেরন', 'hcg', 'অমরা', 'ব্লাস্টোসিস্ট', 'ভ্রূণ']):
            return 'bio_zoo_09'
        if any(k in text for k in ['প্রতিরক্ষা', 'ইমিউনিটি', 'অ্যান্টিবডি', 'igg', 'iga', 'igm', 'ige', 'ভ্যাকসিন', 'টিকা', 'ইন্টারফেরন', 'ম্যাক্রোফেজ', 'বিসিজি']):
            return 'bio_zoo_10'
        if any(k in text for k in ['মেন্ডেল', 'লিথাল জিন', 'সেক্স-লিংকড', 'হিমোফিলিয়া', 'বর্ণান্ধতা', 'ব্লাড গ্রুপ', 'rh ফ্যাক্টর', 'এরিথ্রোব্লাস্টোসিস', 'বিবর্তন', 'সমসংস্থ', 'ডারউইন', 'জিনতত্ত্ব']):
            return 'bio_zoo_11'
        if any(k in text for k in ['আচরণ', 'ট্যাক্সিস', 'রিফ্লেক্স', 'সহজাত', 'শিখন', 'মৌমাছি', 'নৃত্য', 'fap', 'ইমপ্রিন্টিং']):
            return 'bio_zoo_12'
        return 'bio_bot_01'

    elif subj == 'Chemistry':
        # 1st Paper: Safe Lab
        if any(k in text for k in ['কাচপাত্র পরিষ্কার', 'ক্রোমিক অ্যাসিড', 'অ্যাকোয়া রেজিয়া', 'হ্যাজার্ড', 'ল্যাবরেটরি', 'প্রাইমারি স্ট্যান্ডার্ড', 'সেকেন্ডারি স্ট্যান্ডার্ড', 'বুনসেন']):
            return 'chem_1st_01'
        # 2nd Paper: Organic Chemistry
        if any(k in text for k in ['জৈব', 'হাইড্রোকার্বন', 'সমাণু', 'কাইরাল', 'বেনজিন', 'টলুইন', 'ফেনল', 'অ্যালকেন', 'অ্যালকিন', 'অ্যালকাইন', 'ইথিন', 'ইথাইন', 'অ্যালকোহল', 'ইথানল', 'অ্যালডিহাইড', 'কিটোন', 'অ্যামিন', 'টলেন', 'ফেহলিং', 'লুকাস', 'সাইজেফ', 'মারকনিকভ', 'উর্টজ', 'ক্যানিজারো', 'কার্বোক্যাটায়ন', 'ইলেকট্রোফাইল', 'নিউক্লিওফাইল', 'হাকেল', 'হিউকেল', 'অ্যারোমেটিক', 'ক্লোরোফর্ম', 'ফসজিন', 'টটোমারিজম', 'ডায়াজোনিয়াম', 'হোমোলিটিক', 'লিন্ডেন', 'গ্যামাক্সিন', 'সোডা লাইম', '২-ব্রোমো', 'but-1-ene']):
            return 'chem_2nd_02'
        # 2nd Paper: Quantitative Chemistry
        if any(k in text for k in ['মোলারিটি', 'মোল সংখ্যা', 'মোলালিটি', 'স্টয়কিওমেট্রি', 'লিমিটিং বিকারক', 'ppm', 'ppb', 'টাইট্রেশন', 'প্রশমন', 'অক্সালিক এসিড', 'kmno4', 'ইলেকট্রন গ্রহণ', 'জারণ সংখ্যা', 'জারণ-বিজারণ', 'আয়োডোমিতি', 'আয়োডিমেট্রি', 'বিয়ার-ল্যাম্বার্ট', 'w/v', '% (w/v)', 'প্রমাণ দ্রবণ']):
            return 'chem_2nd_03'
        # 2nd Paper: Electrochemistry
        if any(k in text for k in ['ফ্যারাডে', 'তড়িৎ বিশ্লেষণ', 'কোষ বিভব', 'নার্নস্ট', 'লেড-অ্যাসিড', 'লিথিয়াম', 'ফুয়েল সেল', 'তড়িৎ রসায়ন', 'অ্যানোড', 'ক্যাথোড']):
            return 'chem_2nd_04'
        # 1st Paper: Chemical changes & Equilibrium
        if any(k in text for k in ['লা-শাতেলীয়ার', 'সাম্যাবস্থা', 'kp', 'kc', 'বাফার', 'হেন্ডারসন', 'আরহেনিয়াস', 'সক্রিয়করণ শক্তি', 'রাসায়নিক পরিবর্তন', 'ph']):
            return 'chem_1st_04'
        # 2nd Paper: Environmental Chemistry
        if any(k in text for k in ['বয়েল', 'চার্লস', 'গ্রাহাম', 'ব্যাপন', 'বাস্তব গ্যাস', 'ভ্যান ডার ওয়ালস', 'bod', 'cod', 'do', 'অ্যাসিড বৃষ্টি', 'পরিবেশ']):
            return 'chem_2nd_01'
        # 1st Paper: Periodic Properties & Bonds
        if any(k in text for k in ['পর্যায়বৃত্ত', 'আয়নীকরণ', 'ইলেকট্রন আসক্তি', 'তড়িৎ ঋণাত্মকতা', 'সংকরায়ন', 'vsepr', 'ফাজান', 'হাইড্রোজেন বন্ধন', 'মুক্তজোড়', 'মৌলের']):
            return 'chem_1st_03'
        # 2nd Paper: Economic Chemistry
        if any(k in text for k in ['ইউরিয়া', 'প্রাকৃতিক গ্যাস', 'সিমেন্ট', 'পাল্প', 'কাগজ', 'ট্যানিং', 'অর্থনৈতিক']):
            return 'chem_2nd_05'
        # 1st Paper: Applied Chemistry
        if any(k in text for k in ['প্রিজারভেটিভ', 'ভিনেগার', 'কোল্ড ক্রিম', 'টয়লেট্রিজ', 'কর্মমুখী']):
            return 'chem_1st_05'
        # 1st Paper: Qualitative Chemistry
        if any(k in text for k in ['কোয়ান্টাম', 'অরবিটাল', 'রিডবার্গ', 'বর্ণালী', 'লাইমেন', 'বামার', 'দ্রাব্যতা', 'ksp', 'kip', 'ক্যাটায়ন', 'শিখা পরীক্ষা', 'নেসলার', 'গুণগত']):
            return 'chem_1st_02'
        return 'chem_1st_02'

    elif subj == 'Physics':
        # 2nd Paper: Current Electricity (handle electrical power specifically first)
        if any(k in text for k in ['বৈদ্যুতিক কেটলি', 'বাল্ব', 'প্রবাহমাত্রা', 'তুল্য রোধ', 'কার্শফ', 'হুইটস্টোন', 'মিটার ব্রিজ', 'শান্ট', 'অ্যামিটার', 'ভোল্টমিটার', 'ব্যয়িত বৈদ্যুতিক ক্ষমতা', 'চল তড়িৎ', 'ওহম', '\\omega']):
            return 'phy_2nd_03'
        # 2nd Paper: Atomic & Nuclear Physics
        if any(k in text for k in ['হাইড্রোজেন পরমাণু', 'বোর মডেল', 'শক্তিস্তর', 'তেজস্ক্রিয়', 'অর্ধায়ু', 'গড় আয়ু', 'ভর ত্রুটি', 'বন্ধন শক্তি', 'ফিশন', 'ফিউশন']):
            return 'phy_2nd_09'
        # 1st Paper: Periodic Motion / SHM
        if any(k in text for k in ['সরল দোলক', 'সেকেন্ড দোলক', 'দোলনকাল', 'সরল ছন্দিত', 'shm', 'পর্যায়বৃত্ত গতি', 'সেকেন্ডে']):
            return 'phy_1st_08'
        # 1st Paper: Gravitation & Gravity (phy_1st_06 / phy_p1_ch06)
        if any(k in text for k in ['মহাকর্ষ', 'অভিকর্ষ', 'অভিকর্ষজ ত্বরণ', 'g এর মান', 'মুক্তিবেগ', 'উপগ্রহ', 'কৃত্রিম উপগ্রহ', 'ভূ-স্থির উপগ্রহ', 'কেপলার', 'গ্রহের']):
            return 'phy_1st_06'
        # 1st Paper: Work, Power & Energy (phy_1st_05 / phy_p1_ch05)
        if any(k in text for k in ['কৃতকাজ', 'গতিশক্তি', 'বিভব শক্তি', 'স্প্রিং', 'স্প্রিং ধ্রুবক', 'কুয়া', 'চৌবাচ্চা', 'পাম্প', 'হর্সপাওয়ার', 'অশ্বক্ষমতা', 'ভারকেন্দ্রের সরণ', 'কাজ, শক্তি']):
            return 'phy_1st_05'
        # 1st Paper: Newtonian Mechanics
        if any(k in text for k in ['জড়তার ভ্রামক', 'চক্রগতির ব্যাসার্ধ', 'ব্যাংকিং', 'রকেট', 'বন্দুক', 'টর্ক', 'ভরবেগ', 'ঘর্ষণ']):
            return 'phy_1st_04'
        # 1st Paper: Dynamics / Kinematics
        if any(k in text for k in ['প্রক্ষেপক', 'পাল্লা', 'উড্ডয়নকাল', 'সর্বোচ্চ উচ্চতা', 'তক্তা', 'স্টপিং ডিসট্যান্স', 'গতিবিদ্যা', 'ত্বরণ']):
            return 'phy_1st_03'
        # 1st Paper: Vectors
        if any(k in text for k in ['ভেক্টর', 'ডট গুণন', 'ক্রস গুণন', 'নদী-নৌকা', 'ছাতা', 'আপেক্ষিক বেগ', 'ডাইভারজেন্স', 'কার্ল', 'সলিনয়ডাল']):
            return 'phy_1st_02'
        # 1st Paper: Structural Properties of Matter
        if any(k in text for k in ['পীড়ন', 'বিকৃতি', 'ইয়ংয়ের', 'হুকের', 'পৃষ্ঠটান', 'সান্দ্রতা', 'স্টোকস', 'প্রান্তিক বেগ', 'পয়সনের']):
            return 'phy_1st_07'
        # 1st Paper: Waves
        if any(k in text for k in ['অগ্রগামী তরঙ্গ', 'বিট', 'স্বরকম্প', 'সুরশলাকা', 'টানা তার', 'স্থির তরঙ্গ', 'শব্দ তরঙ্গ']):
            return 'phy_1st_09'
        # 1st Paper: Ideal Gas
        if any(k in text for k in ['আদর্শ গ্যাস', 'rms', 'গতিতত্ত্ব', 'হ্রদের তলদেশ', 'বুদ্বুদ', 'আপেক্ষিক আর্দ্রতা', 'শিশিরাংক']):
            return 'phy_1st_10'
        # 2nd Paper: Thermodynamics
        if any(k in text for k in ['তাপগতিবিদ্যা', 'কার্নো', 'এন্ট্রপি', 'সমোষ্ণ', 'রুদ্ধতাপীয়', 'কর্মদক্ষতা']):
            return 'phy_2nd_01'
        # 2nd Paper: Electrostatics
        if any(k in text for k in ['কুলম্ব', 'স্থির তড়িৎ', 'তড়িৎ প্রাবল্য', 'তড়িৎ বিভব', 'ধারক', 'ধারকত্ব']):
            return 'phy_2nd_02'
        # 2nd Paper: Magnetism
        if any(k in text for k in ['বায়ো-সাভার্ট', 'চৌম্বক ক্ষেত্র', 'লরেঞ্জ বল', 'সলিনয়েড', 'ভূ-চৌম্বক', 'বিনতি']):
            return 'phy_2nd_04'
        # 2nd Paper: Induction & AC
        if any(k in text for k in ['ফ্যারাডের আবেশ', 'লেনজ', 'ট্রান্সফরমার', 'rms মান', 'পরিবর্তী প্রবাহ', 'আবেশক']):
            return 'phy_2nd_05'
        # 2nd Paper: Optics
        if any(k in text for k in ['প্রতিসরণ', 'সংকট কোণ', 'পূর্ণ অভ্যন্তরীণ', 'প্রিজম', 'ন্যূনতম বিচ্যুতি', 'লেন্স প্রস্তুতকারক']):
            return 'phy_2nd_06'
        if any(k in text for k in ['ব্যতিচার', 'ডোরা প্রস্থ', 'অপবর্তন', 'গ্রেটিং', 'সমবর্তন', 'ব্রুস্টার']):
            return 'phy_2nd_07'
        # 2nd Paper: Modern Physics
        if any(k in text for k in ['আপেক্ষিকতা', 'কাল দীর্ঘায়ন', 'দৈর্ঘ্য সংকোচন', 'ভর বৃদ্ধি', 'ফটোইলেকট্রিক', 'কার্য-অপেক্ষক', 'নিবৃত্তি বিভব', 'কম্পটন']):
            return 'phy_2nd_08'
        # 2nd Paper: Semiconductor & Electronics
        if any(k in text for k in ['সেমিকন্ডাক্টর', 'ডায়োড', 'রেকটিফায়ার', 'ট্রানজিস্টর', 'লজিক গেট', 'nand', 'nor', 'xor']):
            return 'phy_2nd_10'
        # 2nd Paper: Astronomy
        if any(k in text for k in ['চন্দ্রশেখর', 'শ্বেত বামন', 'কৃষ্ণগহ্বর', 'ব্ল্যাক হোল', 'সোয়ার্জশিল্ড', 'হাবলের', 'বিগ ব্যাং']):
            return 'phy_2nd_11'
        # 1st Paper: Measurement
        if any(k in text for k in ['মাত্রা সমীকরণ', 'ভার্নিয়ার', 'লঘিষ্ঠ গণন', 'স্লাইড ক্যালিপার্স', 'স্ক্রু গজ', 'শতকরা ত্রুটি', 'পরিমাপ']):
            return 'phy_1st_01'
        return 'phy_1st_02'

    elif subj == 'Higher Math':
        # 1st Paper: Integration (math_1st_10 / math_p1_ch10)
        if any(k in text for k in ['\\int', 'যোগজীকরণ', 'ইন্টিগ্রেশন', 'নির্দিষ্ট যোগজ', 'আবদ্ধ ক্ষেত্রের ক্ষেত্রফল', 'দ্বারা আবদ্ধ', 'দ্বারা সীমাবদ্ধ', 'সীমাবদ্ধ ক্ষেত্রের', 'আবদ্ধ অংশের ক্ষেত্রফল', 'আবদ্ধ অঞ্চলের']):
            return 'math_1st_10'
        # 1st Paper: Differentiation (math_1st_09 / math_p1_ch09)
        if any(k in text for k in ['\\lim', 'lim_', 'লিমিট', '\\frac{dy}{dx}', '\\frac{d}{d', 'dy/dx', 'অন্তরীকরণ', 'অন্তরক সহগ', 'লঘুমান', 'গুরুমান', 'সর্বোচ্চ মান', 'সর্বনিম্ন মান', 'বক্ররেখার স্পর্শক', 'অভিলম্বের ঢাল', 'বৃদ্ধির হার', 'সরণের সমীকরণ']):
            return 'math_1st_09'
        # 2nd Paper: Linear Programming
        if any(k in text for k in ['যোগাশ্রয়ী', 'শর্তাধীনে', 'অভিষ্ট']):
            return 'math_2nd_02'
        # 2nd Paper: Conics
        if any(k in text for k in ['পরাবৃত্ত', 'উপবৃত্ত', 'অধিবৃত্ত', 'কনিক', 'উৎকেন্দ্রিকতা', 'উপকেন্দ্র', 'দ্বিকাক্ষ', 'অসীমতট', 'উপকেন্দ্রিক']):
            return 'math_2nd_06'
        # 2nd Paper: Binomial Expansion
        if any(k in text for k in ['দ্বিপদী', 'বিস্তৃতিতে']):
            return 'math_2nd_05'
        # 1st Paper: Permutations & Combinations
        if any(k in text for k in ['বিন্যাস', 'সমাবেশ', 'শব্দে', 'কতভাবে সাজানো', 'কতভাবে বিন্যাস', 'কত প্রকারে', 'গোল টেবিল', 'দল গঠন', 'বহুভুজ', '^{15}c', '^{n}c', 'স্বাভাবিক সংখ্যার', 'করমর্দন', 'অঙ্কগুলো প্রতিবার', 'বিন্দু সমরেখ']):
            return 'math_1st_05'
        # 2nd Paper: Probability & Dispersion
        if any(k in text for k in ['সম্ভাবনা', 'ভেদাঙ্ক', 'পরিমিত ব্যবধান', 'পরিসরাঙ্ক', 'বিভেদাঙ্ক', 'ছক্কা', 'মুদ্রা', 'মার্বেল', 'লিপইয়ার', 'নিবেশনের']):
            return 'math_2nd_10'
        # 2nd Paper: Polynomials
        if any(k in text for k in ['বহুপদী', 'দ্বিঘাত সমীকরণ', 'ত্রিঘাত সমীকরণ', 'নিশ্চয়ক', 'মূলের প্রকৃতি', 'মূলদ্বয়', 'মূল তিনটি']):
            return 'math_2nd_04'
        # 2nd Paper: Complex Numbers
        if any(k in text for k in ['জটিল সংখ্যা', 'মডুলাস', 'আর্গুমেন্ট', 'কাল্পনিক ঘনমূল', '\\omega', 'i^{-', '\\sqrt{-1}', '|z -', '|z +']):
            return 'math_2nd_03'
        # 2nd Paper: Inverse Trig
        if any(k in text for k in ['\\sin^{-1}', '\\cos^{-1}', '\\tan^{-1}', '\\cot^{-1}', 'বিপরীত ত্রিকোণমিতিক']):
            return 'math_2nd_07'
        # 1st Paper: Associated Angles & Trig
        if any(k in text for k in ['\\sin', '\\cos', '\\tan', '\\cot', '\\sec', '\\csc', 'ত্রিকোণমিতি', 'বৃত্তচাপ']):
            return 'math_1st_07'
        # 1st Paper: Circles
        if any(k in text for k in ['বৃত্ত', 'বৃত্তের', 'ব্যাসার্ধের বৃত্ত']):
            return 'math_1st_04'
        # 1st Paper: Straight Lines
        if any(k in text for k in ['সরলরেখা', 'বিন্দুদ্বয়ের', 'মূলবিন্দু', 'লম্ব দূরত্ব', 'সমান্তরাল রেখা', 'ছেদবিন্দুগামী', 'পোলার', 'কার্তেসীয়', 'সমরেখ', 'লম্ববিন্দু', 'ভরকেন্দ্র']):
            return 'math_1st_03'
        # 1st Paper: Matrices & Determinants
        if any(k in text for k in ['ম্যাট্রিক্স', 'নির্ণায়ক', 'ব্যতিক্রমী', 'ইনভার্স', 'ট্রেস', 'ক্র্যামার', 'ক্রেমার']):
            return 'math_1st_01'
        # 2nd Paper: Real Numbers & Inequalities
        if any(k in text for k in ['বাস্তব সংখ্যা', 'অসমতা', 'পরম মান', 'সুপ্রিমাম', 'ইনফিমাম']):
            return 'math_2nd_01'
        # 2nd Paper: Statics
        if any(k in text for k in ['স্থিতিবিদ্যা', 'লামির', 'বল ত্রিভুজ', 'সদৃশ সমান্তরাল', 'লব্ধি']):
            return 'math_2nd_08'
        # 2nd Paper: Dynamics in Plane
        if any(k in text for k in ['বস্তু কণার গতি', 'ট্রেনের', 'সমতলে গতি', 'উল্লম্ব তলে গতি']):
            return 'math_2nd_09'
        # 1st Paper: Functions
        if any(k in text for k in ['ফাংশন', 'ডোমেন', 'রেঞ্জ', 'বিপরীত ফাংশন', 'f^-1', 'সংযোজিত']):
            return 'math_1st_08'
        return 'math_1st_08'

    return old_bp

def build_all():
    print("--- 1. Assembling 75 Unbundled Chapters ---")
    chapters = get_all_75_chapters()
    print(f"Total canonical chapters assembled: {len(chapters)}")

    bp_output = {
        "metadata": {
            "title": "Master QB Full-Syllabus Unbundled Blueprint 2026",
            "source_banks": ["VAR Master QB (22,800+ Questions)", "MAD Master QB & Medical Bank"],
            "total_chapters": len(chapters),
            "subjects": ["Physics", "Chemistry", "Higher Math", "Biology"],
            "version": "2026.2"
        },
        "chapters": chapters
    }

    # Save blueprint
    for p in [os.path.join(SRC_DATA_DIR, "master_chapter_blueprint.json"),
              os.path.join(APP_DATA_DIR, "master_chapter_blueprint.json")]:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(bp_output, f, indent=2, ensure_ascii=False)
        print(f"Saved blueprint: {p}")

    print("\n--- 2. Building Synthetic Predictors for all 75 Chapters ---")
    # Load existing predictors
    orig_pred_file = os.path.join(SRC_DATA_DIR, "chapter_synthetic_predictors.json")
    with open(orig_pred_file, "r", encoding="utf-8") as f:
        old_pred_data = json.load(f)

    # Distribute existing predictors by new chapter IDs
    unbundled_predictors = {ch['id']: [] for ch in chapters}
    for old_ch in old_pred_data.get('chapters', []):
        old_id = old_ch.get('chapter_id')
        for q in old_ch.get('predictors', []):
            mapped_ch_id = classify_question({
                'subject': ALL_CHAPTER_METADATA.get(old_id, {}).get('subject', ''),
                'blueprint_chapter_id': old_id,
                'chapter': old_ch.get('chapter_title', ''),
                'question': q.get('stem', ''),
                'explanation': q.get('explanation', ''),
                'type_ref': q.get('type_ref', '')
            })
            if mapped_ch_id in unbundled_predictors:
                unbundled_predictors[mapped_ch_id].append(q)

    # Seed predictors for any chapter lacking questions
    final_pred_chapters = []
    total_preds = 0
    for ch in chapters:
        cid = ch['id']
        preds = unbundled_predictors.get(cid, [])
        # Preserve existing predictors without generating dummy template MCQs
        if not preds and cid in {c['chapter_id'] for c in old_pred_data.get('chapters', [])}:
            for c in old_pred_data.get('chapters', []):
                if c.get('chapter_id') == cid:
                    preds = c.get('predictors', [])
                    break


        final_pred_chapters.append({
            "chapter_id": cid,
            "chapter_title": ch['title'],
            "subject": ch['subject'],
            "paper": ch['paper'],
            "chapter_no": ch['chapter_no'],
            "predictors": preds
        })
        total_preds += len(preds)

    pred_output = {
        "metadata": {
            "title": "Master QB Synthetic Predictors (75 Unbundled Chapters)",
            "description": "High-Yield Predictors per individual chapter for DU Ka Unit, Medical MAT & Engineering",
            "total_chapters": len(final_pred_chapters),
            "total_predictors": total_preds,
            "version": "2026.2"
        },
        "chapters": final_pred_chapters
    }

    for p in [os.path.join(SRC_DATA_DIR, "chapter_synthetic_predictors.json"),
              os.path.join(APP_DATA_DIR, "chapter_synthetic_predictors.json")]:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(pred_output, f, indent=2, ensure_ascii=False)
        print(f"Saved synthetic predictors: {p} ({total_preds} MCQs)")

    print("\n--- 3. Re-indexing & Migrating Question Banks ---")
    q_files = [
        os.path.join(SRC_DATA_DIR, "questions.json"),
        os.path.join(SRC_DATA_DIR, "varsity_bank.json"),
        os.path.join(SRC_DATA_DIR, "medical_bank.json"),
        os.path.join(SRC_DATA_DIR, "quizzes.json"),
        os.path.join(SRC_DATA_DIR, "weekly_exams.json"),
        os.path.join(BASE_DIR, "questions.json"),
        os.path.join(BASE_DIR, "varsity_bank.json"),
        os.path.join(BASE_DIR, "medical_bank.json"),
        os.path.join(BASE_DIR, "weekly_exams.json")
    ]

    for qf in q_files:
        if not os.path.exists(qf):
            continue
        with open(qf, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        updated_count = 0
        for item in data:
            old_bp = item.get('blueprint_chapter_id')
            subj = item.get('subject')
            if subj in ['Biology', 'Chemistry', 'Physics', 'Higher Math']:
                new_cid = classify_question(item)
                if new_cid in ALL_CHAPTER_METADATA:
                    item['blueprint_chapter_id'] = new_cid
                    item['chapter'] = ALL_CHAPTER_METADATA[new_cid]['title']
                    updated_count += 1
                elif old_bp in ALL_CHAPTER_METADATA:
                    item['blueprint_chapter_id'] = ALL_CHAPTER_METADATA[old_bp]['id']
                    item['chapter'] = ALL_CHAPTER_METADATA[old_bp]['title']
                    updated_count += 1
            elif old_bp and old_bp in ALL_CHAPTER_METADATA:
                item['blueprint_chapter_id'] = ALL_CHAPTER_METADATA[old_bp]['id']
                item['chapter'] = ALL_CHAPTER_METADATA[old_bp]['title']
                updated_count += 1

        with open(qf, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {qf}: re-indexed {updated_count}/{len(data)} items")

        # Sync to admission_webapp
        bname = os.path.basename(qf)
        webapp_copy = os.path.join(APP_DATA_DIR, bname)
        if os.path.dirname(qf) == SRC_DATA_DIR:
            shutil.copyfile(qf, webapp_copy)
            print(f"  -> Mirrored to {webapp_copy}")

    print("\n--- 4. Updating Blueprint with True Available Counts ---")
    ch_q_counts = {ch['id']: 0 for ch in chapters}
    with open(os.path.join(SRC_DATA_DIR, "questions.json"), "r", encoding="utf-8") as f:
        primary_qs = json.load(f)
    for q in primary_qs:
        cid = q.get('blueprint_chapter_id')
        if cid in ch_q_counts:
            ch_q_counts[cid] += 1

    pred_counts = {ch['chapter_id']: len(ch.get('predictors', [])) for ch in final_pred_chapters}

    for ch in chapters:
        cid = ch['id']
        q_count = ch_q_counts.get(cid, 0)
        p_count = pred_counts.get(cid, 0)
        ch['question_count'] = q_count
        ch['mcq_count'] = q_count + p_count
        ch['total_questions'] = q_count + p_count

    bp_output["chapters"] = chapters

    for p in [os.path.join(SRC_DATA_DIR, "master_chapter_blueprint.json"),
              os.path.join(APP_DATA_DIR, "master_chapter_blueprint.json")]:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(bp_output, f, indent=2, ensure_ascii=False)
        print(f"Updated blueprint with counts: {p}")

    print("\nData migration and unbundling complete!")

if __name__ == '__main__':
    build_all()
