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
    ch_raw = q.get('chapter') or ''
    stem = q.get('question') or q.get('q') or ''
    exp = q.get('explanation') or q.get('exp') or ''
    tag = q.get('tag') or ''
    tref = q.get('type_ref') or ''
    text = f"{ch_raw} {stem} {exp} {tag} {tref}".lower()

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
        # 1st Paper
        if any(k in text for k in ['হ্যাজার্ড', 'ল্যাবরেটরি', 'প্রাইমারি স্ট্যান্ডার্ড', 'সেকেন্ডারি স্ট্যান্ডার্ড', 'ক্রোমিল', 'বুনসেন']):
            return 'chem_1st_01'
        if any(k in text for k in ['কোয়ান্টাম', 'অরবিটাল', 'রিডবার্গ', 'বর্ণালী', 'লাইমেন', 'বামার', 'দ্রাব্যতা', 'ksp', 'kip', 'ক্যাটায়ন', 'শিখা পরীক্ষা', 'নেসলার', 'গুণগত']):
            return 'chem_1st_02'
        if any(k in text for k in ['পর্যায়বৃত্ত', 'আয়নীকরণ', 'ইলেকট্রন আসক্তি', 'তড়িৎ ঋণাত্মকতা', 'সংকরায়ন', 'vsepr', 'ফাজান', 'হাইড্রোজেন বন্ধন', 'মুক্তজোড়', 'মৌলের']):
            return 'chem_1st_03'
        if any(k in text for k in ['লা-শাতেলীয়ার', 'সাম্যাবস্থা', 'kp', 'kc', 'বাফার', 'হেন্ডারসন', 'আরহেনিয়াস', 'সক্রিয়করণ শক্তি', 'রাসায়নিক পরিবর্তন']):
            return 'chem_1st_04'
        if any(k in text for k in ['প্রিজারভেটিভ', 'ভিনেগার', 'কোল্ড ক্রিম', 'টয়লেট্রিজ', 'কর্মমুখী']):
            return 'chem_1st_05'
        
        # 2nd Paper
        if any(k in text for k in ['বয়েল', 'চার্লস', 'গ্রাহাম', 'ব্যাপন', 'বাস্তব গ্যাস', 'ভ্যান ডার ওয়ালস', 'bod', 'cod', 'do', 'অ্যাসিড বৃষ্টি', 'পরিবেশ']):
            return 'chem_2nd_01'
        if any(k in text for k in ['জৈব', 'হাইড্রোকার্বন', 'সমাণুতা', 'হাকেল', 'বেনজিন', 'sn1', 'sn2', 'লুকাস', 'টলেন্স', 'ফেহলিং', 'অ্যালডল', 'ক্যানিজারো', 'আয়োডোফর্ম', 'অ্যামিন', 'ডায়াজোনিয়াম']):
            return 'chem_2nd_02'
        if any(k in text for k in ['স্টয়কিওমেট্রি', 'লিমিটিং', 'মোলারিটি', 'মোল সংখ্যা', 'ppm', 'টাইট্রেশন', 'আয়োডোমিতি', 'বিয়ার-ল্যাম্বার্ট', 'পরিমাণগত']):
            return 'chem_2nd_03'
        if any(k in text for k in ['ফ্যারাডে', 'তড়িৎ বিশ্লেষণ', 'কোষ বিভব', 'নার্নস্ট', 'লেড-অ্যাসিড', 'লিথিয়াম', 'ফুয়েল সেল', 'তড়িৎ রসায়ন']):
            return 'chem_2nd_04'
        if any(k in text for k in ['ইউরিয়া', 'প্রাকৃতিক গ্যাস', 'সিমেন্ট', 'পাল্প', 'কাগজ', 'ট্যানিং', 'অর্থনৈতিক']):
            return 'chem_2nd_05'
        return 'chem_1st_02'

    elif subj == 'Physics':
        # 1st Paper
        if any(k in text for k in ['মাত্রা সমীকরণ', 'ভার্নিয়ার', 'লঘিষ্ঠ গণন', 'স্লাইড ক্যালিপার্স', 'স্ক্রু গজ', 'শতকরা ত্রুটি', 'পরিমাপ']):
            return 'phy_1st_01'
        if any(k in text for k in ['ভেক্টর', 'ডট', 'ক্রস', 'নদী-নৌকা', 'ছাতা', 'আপেক্ষিক বেগ', 'গ্র্যাডিয়েন্ট', 'ডাইভারজেন্স', 'কার্ল', 'সলিনয়ডাল']):
            return 'phy_1st_02'
        if any(k in text for k in ['প্রক্ষেপক', 'পাল্লা', 'উড্ডয়নকাল', 'সর্বোচ্চ উচ্চতা', 'তক্তা', 'স্টপিং ডিসট্যান্স', 'গতিবিদ্যা']):
            return 'phy_1st_03'
        if any(k in text for k in ['জড়তার ভ্রামক', 'চক্রগতির ব্যাসার্ধ', 'ব্যাংকিং', 'রকেট', 'বন্দুক', 'টর্ক', 'ভরবেগ', 'নিউটনের']):
            return 'phy_1st_04'
        if any(k in text for k in ['কৃতকাজ', 'স্প্রিং', 'কুয়া', 'চৌবাচ্চা', 'ক্ষমতা', 'হর্সপাওয়ার', 'কাজ, শক্তি']):
            return 'phy_1st_05'
        if any(k in text for k in ['মহাকর্ষ', 'অভিকর্ষ', 'মুক্তিবেগ', 'উপগ্রহ', 'কেপলার', 'পর্যায়কাল', 'g এর মান']):
            return 'phy_1st_06'
        if any(k in text for k in ['পীড়ন', 'বিকৃতি', 'ইয়ংয়ের', 'হুকের', 'পৃষ্ঠটান', 'সান্দ্রতা', 'স্টোকস', 'প্রান্তিক বেগ', 'পয়সনের']):
            return 'phy_1st_07'
        if any(k in text for k in ['দোলক', 'সরল ছন্দিত', 'shm', 'সেকেন্ড দোলক', 'পাহাড়', 'দোলনকাল', 'পর্যায়বৃত্ত গতি']):
            return 'phy_1st_08'
        if any(k in text for k in ['অগ্রগামী তরঙ্গ', 'বিট', 'স্বরকম্প', 'সুরশলাকা', 'টানা তার', 'স্থির তরঙ্গ', 'তরঙ্গ']):
            return 'phy_1st_09'
        if any(k in text for k in ['আদর্শ গ্যাস', 'rms', 'গতিতত্ত্ব', 'হ্রদের তলদেশ', 'বুদ্বুদ', 'আপেক্ষিক আর্দ্রতা', 'শিশিরাংক', 'গ্লেসিয়ার']):
            return 'phy_1st_10'
        
        # 2nd Paper
        if any(k in text for k in ['তাপগতিবিদ্যা', 'কার্নো', 'এন্ট্রপি', 'সমোষ্ণ', 'রুদ্ধতাপীয়', 'কর্মদক্ষতা']):
            return 'phy_2nd_01'
        if any(k in text for k in ['কুলম্ব', 'স্থির তড়িৎ', 'তড়িৎ প্রাবল্য', 'তড়িৎ বিভব', 'ধারক', 'ধারকত্ব']):
            return 'phy_2nd_02'
        if any(k in text for k in ['চল তড়িৎ', 'তুল্য রোধ', 'কার্শফ', 'হুইটস্টোন', 'মিটার ব্রিজ', 'শান্ট', 'অ্যামিটার', 'ভোল্টমিটার']):
            return 'phy_2nd_03'
        if any(k in text for k in ['বায়ো-সাভার্ট', 'চৌম্বক ক্ষেত্র', 'লরেঞ্জ বল', 'সলিনয়েড', 'ভূ-চৌম্বক', 'বিনতি', 'ডায়াচুম্বক', 'প্যারাচুম্বক']):
            return 'phy_2nd_04'
        if any(k in text for k in ['ফ্যারাডের আবেশ', 'লেনজ', 'ট্রান্সফরমার', 'rms মান', 'পরিবর্তী প্রবাহ', 'আবেশক']):
            return 'phy_2nd_05'
        if any(k in text for k in ['প্রতিসরণ', 'সংকট কোণ', 'পূর্ণ অভ্যন্তরীণ', 'প্রিজম', 'ন্যূনতম বিচ্যুতি', 'লেন্স প্রস্তুতকারক', 'ফোকাস দূরত্ব']):
            return 'phy_2nd_06'
        if any(k in text for k in ['ব্যতিচার', 'ডোরা প্রস্থ', 'অপবর্তন', 'গ্রেটিং', 'সমবর্তন', 'ব্রুস্টার', 'ভৌত আলোকবিজ্ঞান']):
            return 'phy_2nd_07'
        if any(k in text for k in ['আপেক্ষিকতা', 'কাল দীর্ঘায়ন', 'দৈর্ঘ্য সংকোচন', 'ভর বৃদ্ধি', 'ফটোইলেকট্রিক', 'কার্য-অপেক্ষক', 'নিবৃত্তি বিভব', 'কম্পটন']):
            return 'phy_2nd_08'
        if any(k in text for k in ['বোর পরমাণু', 'বোর মডেল', 'কক্ষপথের ব্যাসার্ধ', 'তেজস্ক্রিয়', 'অর্ধায়ু', 'গড় আয়ু', 'ভর ত্রুটি', 'বন্ধন শক্তি', 'ফিশন', 'ফিউশন']):
            return 'phy_2nd_09'
        if any(k in text for k in ['সেমিকন্ডাক্টর', 'ডায়োড', 'রেকটিফায়ার', 'ট্রানজিস্টর', 'লজিক গেট', 'nand', 'nor', 'xor', 'বুলিয়ান']):
            return 'phy_2nd_10'
        if any(k in text for k in ['চন্দ্রশেখর', 'শ্বেত বামন', 'কৃষ্ণগহ্বর', 'ব্ল্যাক হোল', 'সোয়ার্জশিল্ড', 'হাবলের', 'বিগ ব্যাং', 'জ্যোতির্বিজ্ঞান']):
            return 'phy_2nd_11'
        return 'phy_1st_02'

    elif subj == 'Higher Math':
        # 1st Paper
        if any(k in text for k in ['ম্যাট্রিক্স', 'নির্ণায়ক', 'ব্যতিক্রমী', 'ইনভার্স', 'ট্রেস', 'ক্র্যামার']):
            return 'math_1st_01'
        if any(k in text for k in ['ভেক্টর', 'স্কেলার ট্রিপল', 'সমতলীয়', 'অভিক্ষেপ', 'লম্ব একক']):
            return 'math_1st_02'
        if any(k in text for k in ['সরলরেখা', 'কার্তেসীয়', 'পোলার', 'অন্তর্বিভক্ত', 'ঢাল', 'লম্ব দূরত্ব', 'সমান্তরাল রেখা']):
            return 'math_1st_03'
        if any(k in text for k in ['বৃত্ত', 'কেন্দ্র', 'ব্যাসার্ধ', 'ছেদাংশ', 'স্পর্শক', 'স্পর্শ']):
            return 'math_1st_04'
        if any(k in text for k in ['বিন্যাস', 'সমাবেশ', 'শব্দ', 'স্বরবর্ণ', 'গোল টেবিল', 'দল গঠন', 'বহুভুজ']):
            return 'math_1st_05'
        if any(k in text for k in ['বৃত্তচাপ', 's = r', 'ঘড়ির কাঁটা', 'রেডিয়ান']):
            return 'math_1st_06'
        if any(k in text for k in ['সংযুক্ত কোণ', 'গুণিতক কোণ', 'sin 2a', 'cos 2a', 'ত্রিভুজের সাইন', 'ত্রিভুজের ক্ষেত্রফল']):
            return 'math_1st_07'
        if any(k in text for k in ['ফাংশন', 'ডোমেন', 'রেঞ্জ', 'বিপরীত ফাংশন', 'f^-1', 'সংযোজিত']):
            return 'math_1st_08'
        if any(k in text for k in ['লিমিট', 'এল-হসপিটাল', 'অন্তরীকরণ', 'স্পর্শক', 'অভিলম্বের ঢাল', 'গুরুমান', 'লঘুমান']):
            return 'math_1st_09'
        if any(k in text for k in ['ইন্টিগ্রেশন', 'যোগজীকরণ', 'নির্দিষ্ট যোগজ', 'আবদ্ধ ক্ষেত্রফল', 'ক্ষেত্রফল']):
            return 'math_1st_10'
        
        # 2nd Paper
        if any(k in text for k in ['বাস্তব সংখ্যা', 'অসমতা', 'পরম মান', 'সুপ্রিমাম', 'ইনফিমাম']):
            return 'math_2nd_01'
        if any(k in text for k in ['যোগাশ্রয়ী', 'অভিষ্ট', 'সীমাবদ্ধতা', 'প্রান্তিক বিন্দু']):
            return 'math_2nd_02'
        if any(k in text for k in ['জটিল সংখ্যা', 'মডুলাস', 'আর্গুমেন্ট', 'ওমেগা', 'omega', 'ঘনমূল', 'বর্গমূল']):
            return 'math_2nd_03'
        if any(k in text for k in ['বহুপদী', 'দ্বিঘাত', 'নিশ্চয়ক', 'মূলের প্রকৃতি', 'মূল ও সহগ']):
            return 'math_2nd_04'
        if any(k in text for k in ['দ্বিপদী', 'মধ্যপদ', 'x-বর্জিত', 'সাধারণ পদ']):
            return 'math_2nd_05'
        if any(k in text for k in ['কনিক', 'পরাবৃত্ত', 'উপবৃত্ত', 'অধিবৃত্ত', 'উৎকেন্দ্রিকতা', 'উপকেন্দ্র', 'নিয়ামক']):
            return 'math_2nd_06'
        if any(k in text for k in ['বিপরীত ত্রিকোণমিতিক', 'tan^-1', 'সাধারণ সমাধান', 'n\\pi']):
            return 'math_2nd_07'
        if any(k in text for k in ['স্থিতিবিদ্যা', 'লামির', 'বল ত্রিভুজ', 'সদৃশ সমান্তরাল', 'লব্ধি']):
            return 'math_2nd_08'
        if any(k in text for k in ['বস্তু কণার গতি', 'ট্রেনের', 'সমতলে গতি', 'উল্লম্ব তলে গতি']):
            return 'math_2nd_09'
        if any(k in text for k in ['সম্ভাবনা', 'ভেদাঙ্ক', 'পরিমিত ব্যবধান', 'বিভেদাঙ্ক', 'ছক্কা', 'মুদ্রা', 'তাস']):
            return 'math_2nd_10'
        return 'math_1st_01'

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
        # If fewer than 8, generate seed predictors from mega_types
        if len(preds) < 8:
            for i, mt in enumerate(ch['mega_types']):
                core = mt.get('core_rule', '')
                speed = mt.get('speed_elimination', core[:100] or 'অপশন এলিমিনেশন ও ডাইমেনশন যাচাই করুন।')
                p_id = f"pred_{cid}_{i+1:02d}"
                stem = f"[{ch['title'].split('(')[0].strip()}] {mt['name']} এর মূল নীতি নিচের কোনটি?"
                opts = [
                    f"সঠিক নীতি: {core[:90]}...",
                    f"বিপরীত বিবৃতি যা অসম্পূর্ণ ও বিভ্রান্তিকর অনুসিদ্ধান্ত।",
                    f"প্রচলিত সাধারণ ধারণার ভুল প্রয়োগ যেখানে শর্ত লঙ্ঘিত হয়।",
                    f"উপরের কোনটিই সঠিক নয়।"
                ]
                preds.append({
                    "id": p_id,
                    "stem": stem,
                    "options": opts,
                    "answer": "A",
                    "type_ref": mt['name'],
                    "trap_alert": f"সতর্কতা: {speed[:100]}",
                    "speed_hack": speed,
                    "explanation": f"কোর রুল ও বিশ্লেষণ: {core}"
                })
                # Add another calculation/shortcut predictor
                p_id2 = f"pred_{cid}_{i+1:02d}_b"
                stem2 = f"[{ch['chapter_no']}] {mt['name']} সংশ্লিষ্ট দ্রুত সমাধান হ্যাক কোনটি?"
                opts2 = [
                    f"{speed}",
                    f"দীর্ঘায়িত প্রথাগত সমীকরণ সমাধান যেখানে ৩ মিনিটের অধিক সময় প্রয়োজন।",
                    f"অনুপাত বিবেচনা না করে সরাসরি মুখস্থ মানের প্রয়োগ।",
                    f"উভয় পক্ষ বর্গ না করে অপরিবর্তিত রাখা।"
                ]
                preds.append({
                    "id": p_id2,
                    "stem": stem2,
                    "options": opts2,
                    "answer": "A",
                    "type_ref": mt['name'],
                    "trap_alert": "ফর্মুলা প্রয়োগের সময় একক ও চিহ্নের সঠিকতা যাচাই করুন।",
                    "speed_hack": speed,
                    "explanation": f"ব্যাখ্যা ও সূত্র: {core}"
                })

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
            if not old_bp:
                continue
            new_cid = classify_question(item)
            if new_cid in ALL_CHAPTER_METADATA:
                item['blueprint_chapter_id'] = new_cid
                item['chapter'] = ALL_CHAPTER_METADATA[new_cid]['title']
                updated_count += 1
            elif old_bp in ALL_CHAPTER_METADATA:
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

    print("\nData migration and unbundling complete!")

if __name__ == '__main__':
    build_all()
