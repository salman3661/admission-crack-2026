# -*- coding: utf-8 -*-
"""
generate_vault_full.py
Complete 249+ Formula & Trap Vault entries across all 29 chapters of Week 01, Week 02, Week 03.
Organized strictly by:
Subject -> Chapter -> Card Types ('core_formula', 'shortcut', 'trap')
Also preserves legacy vault collections (triplets, quick_math, magic_fractions, patterns, traps).
"""

import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from generate_vault import get_vault_entries as get_phy_entries
from generate_vault_math_bio_gk import get_math_entries, get_bio_entries, get_english_entries, get_gk_entries

def get_chem_entries():
    # Chemistry 5 Chapters
    entries = []
    
    # Qualitative Analysis
    entries.extend([
        {
            "id": "v_che_qa_01",
            "subject": "Chemistry",
            "chapter": "Qualitative Analysis",
            "type": "core_formula",
            "title": "বোর পরমাণু মডেলের ব্যাসার্ধ ও শক্তি সমীকরণ",
            "formula": "r_n = 0.529\\frac{n^2}{Z} \\text{ \\AA}, \\quad E_n = -13.6\\frac{Z^2}{n^2} \\text{ eV}",
            "concept": "বোর ব্যাসার্ধ প্রধান কোয়ান্টাম সংখ্যার বর্গের সমানুপাতিক এবং শক্তি n^2 এর ব্যস্তানুপাতিক।",
            "hack": "হাইড্রোজেনের জন্য: r_1 = 0.529 \\AA, r_2 = 4 r_1 = 2.116 \\AA! E_1 = -13.6 eV, E_2 = -3.4 eV, E_3 = -1.51 eV!",
            "trap": "কক্ষপথের শক্তি বৃদ্ধির সাথে সাথে দুটি ক্রমিক কক্ষপথের শক্তির পার্থক্য (\\Delta E) ক্রমান্বয়ে হ্রাস পায়।",
            "tags": ["Bohr model", "radius", "energy", "বোর মডেল", "ব্যাসার্ধ", "শক্তি"]
        },
        {
            "id": "v_che_qa_02",
            "subject": "Chemistry",
            "chapter": "Qualitative Analysis",
            "type": "core_formula",
            "title": "রিডবার্গ সমীকরণ ও হাইড্রোজেন বর্ণালি সিরিজ",
            "formula": "\\bar{\\nu} = \\frac{1}{\\lambda} = R_H Z^2 \\left(\\frac{1}{n_1^2} - \\frac{1}{n_2^2}\\right) \\quad (R_H \\approx 109678 \\text{ cm}^{-1})",
            "concept": "লাইম্যান (n1=1, UV), বামার (n1=2, দৃশ্যমান), প্যাসচেন (n1=3, IR), ব্র্যাকেট (n1=4, IR), ফুন্ড (n1=5, IR)।",
            "hack": "\\lambda = \\frac{n_1^2 n_2^2}{n_2^2 - n_1^2} \\times 912 \\text{ \\AA}! বামার ১ম রেখা (3 -> 2): \\lambda = \\frac{36}{5} \\times 912 \\approx 6563 \\text{ \\AA} (লাল)!",
            "trap": "সীমান্ত রেখা (Series limit) বললে n2 = \\infty বসাতে হবে, ফলে \\lambda_{limit} = n_1^2 / R_H।",
            "tags": ["Rydberg", "spectral series", "বর্ণালি", "বামার", "লাইম্যান"]
        },
        {
            "id": "v_che_qa_03",
            "subject": "Chemistry",
            "chapter": "Qualitative Analysis",
            "type": "shortcut",
            "title": "কোয়ান্টাম সংখ্যা ও নোড সংখ্যা গণনা",
            "formula": "\\text{মোট নোড} = n - 1, \\quad \\text{রেডিয়াল নোড} = n - l - 1, \\quad \\text{কৌণিক নোড} = l",
            "concept": "ইলেকট্রন মেঘের যে স্থানে পাওয়ার সম্ভাবনা শূন্য তাকে নোড বলে। শক্তিস্তরে মোট অরবিটাল n^2 এবং মোট ইলেকট্রন 2n^2।",
            "hack": "3p অরবিটালে (n=3, l=1): মোট নোড = 3 - 1 = 2; রেডিয়াল নোড = 3 - 1 - 1 = 1; কৌণিক নোড = 1!",
            "trap": "মোট নোড আর রেডিয়াল নোড এক নয়; প্রশ্নে কোনটি চেয়েছে তা নিশ্চিত হয়ে বৃত্ত ভরাট করুন।",
            "tags": ["quantum numbers", "nodes", "কোয়ান্টাম সংখ্যা", "নোড", "রেডিয়াল নোড"]
        },
        {
            "id": "v_che_qa_04",
            "subject": "Chemistry",
            "chapter": "Qualitative Analysis",
            "type": "core_formula",
            "title": "দ্রাব্যতা গুণফল (Ksp) ও দ্রাব্যতার সম্পর্ক",
            "formula": "A_x B_y \\rightleftharpoons xA^{y+} + yB^{x-} \\implies K_{sp} = x^x y^y S^{(x+y)}",
            "concept": "1:1 লবণ (AgCl): K_sp = S^2; 1:2 লবণ (PbCl2, Mg(OH)2): K_sp = 4S^3; 1:3 লবণ (Fe(OH)3): K_sp = 27S^4; 2:3 লবণ (Al2(SO4)3): K_sp = 108S^5।",
            "hack": "K_sp দেওয়া থাকলে দ্রাব্যতা: 1:1 হলে S = \\sqrt{K_{sp}}; 1:2 হলে S = \\sqrt[3]{K_{sp}/4}; 2:3 হলে S = \\sqrt[5]{K_{sp}/108}!",
            "trap": "অধঃক্ষেপণের শর্ত: K_ip > K_sp (আয়নিক গুণফল দ্রাব্যতা গুণফলকে অতিক্রম করলে কেবল তখনই অধঃক্ষেপ পড়বে)।",
            "tags": ["Ksp", "solubility", "দ্রাব্যতা গুণফল", "অধঃক্ষেপণ"]
        },
        {
            "id": "v_che_qa_05",
            "subject": "Chemistry",
            "chapter": "Qualitative Analysis",
            "type": "trap",
            "title": "শিখা পরীক্ষা ও ব্যতিক্রমী বর্ণহীন মৌল",
            "formula": "\\text{Be ও Mg শিখা পরীক্ষা দেয় না!}",
            "concept": "বেরিলিয়াম ও ম্যাগনেসিয়ামের পরমাণুর আকার ক্ষুদ্র এবং আয়নীকরণ শক্তি অনেক বেশি হওয়ায় বুনসেন শিখার তাপে ইলেকট্রন উত্তেজিত হতে পারে না।",
            "hack": "Na+ সোনালী হলুদ; K+ বেগুনি; Ca2+ ইটের মতো লাল; Cu2+ নীলাভ সবুজ; Ba2+ আপেল সবুজ; Sr2+ টকটকে লাল!",
            "trap": "শিখা পরীক্ষায় উদ্বায়ী ক্লোরাইড লবণ তৈরির জন্য কেবল গাঢ় HCl ব্যবহৃত হয়, অন্য কোনো এসিড নয়।",
            "tags": ["flame test", "Be", "Mg", "শিখা পরীক্ষা", "উদ্বায়ী ক্লোরাইড", "trap"]
        },
        {
            "id": "v_che_qa_06",
            "subject": "Chemistry",
            "chapter": "Qualitative Analysis",
            "type": "shortcut",
            "title": "আয়ন শনাক্তকরণ ও নেসলার বিকারক",
            "formula": "\\text{নেসলার বিকারক: } \\text{K}_2[\\text{HgI}_4] + \\text{KOH}",
            "concept": "অ্যামোনিয়াম আয়ন (NH4+) শনাক্তকরণে নেসলার দ্রবণ যোগ করলে অ্যামিনো মারকিউরিক আয়োডাইডের বাদামি অধঃক্ষেপ পড়ে।",
            "hack": "Fe3+ এ K4[Fe(CN)6] দিলে প্রুশিয়ান ব্লু (গাঢ় নীল); Cu2+ এ দিলে চকলেট বাদামি অধঃক্ষেপ!",
            "trap": "নেসলার বিকারকে KOH বা NaOH ক্ষারীয় মাধ্যম থাকা আবশ্যক; অম্লীয় দ্রবণে এটি কাজ করে না।",
            "tags": ["Nessler's reagent", "cation test", "নেসলার বিকারক", "আয়ন শনাক্তকরণ"]
        },
        {
            "id": "v_che_qa_07",
            "subject": "Chemistry",
            "chapter": "Qualitative Analysis",
            "type": "core_formula",
            "title": "ক্রোমাটোগ্রাফি ও Rf মান",
            "formula": "R_f = \\frac{\\text{দ্রব কর্তৃক অতিক্রান্ত দূরত্ব}}{\\text{দ্রাবক শীর্ষ কর্তৃক অতিক্রান্ত দূরত্ব}} \\quad (0 < R_f < 1)",
            "concept": "পেপার ক্রোমাটোগ্রাফিতে স্থির মাধ্যম হলো ফিল্টার পেপারের সেলুলোজে আবদ্ধ পানি এবং চলমান মাধ্যম হলো উপযুক্ত জৈব দ্রাবক।",
            "hack": "Rf একটি অনুপাত বিধায় এটি সম্পূর্ণ এককহীন। যার Rf মান যত বেশি সে দ্রাবকে তত বেশি দ্রবণীয়!",
            "trap": "Rf এর মান কখনোই ১ এর চেয়ে বেশি বা ঋণাত্মক হতে পারে না (সর্বদা 0 থেকে 1 এর মধ্যে)।",
            "tags": ["chromatography", "Rf value", "ক্রোমাটোগ্রাফি", "স্থির মাধ্যম"]
        },
        {
            "id": "v_che_qa_08",
            "subject": "Chemistry",
            "chapter": "Qualitative Analysis",
            "type": "shortcut",
            "title": "সম-আয়ন প্রভাব (Common Ion Effect) ও দ্রাব্যতা হ্রাস",
            "formula": "S' = \\frac{K_{sp}}{C} \\; (AB \\text{ লবণে}), \\quad S' = \\frac{K_{sp}}{C^2} \\; (AB_2 \\text{ লবণে যখন } B^- \\text{ সম-আয়ন})",
            "concept": "কোনো মৃদু তড়িৎবিশ্লেষ্যের দ্রবণে সম-আয়ন বিশিষ্ট তীব্র তড়িৎবিশ্লেষ্য যোগ করলে মৃদুটির দ্রাব্যতা বহুলাংশে হ্রাস পায়।",
            "hack": "0.1 M NaCl দ্রবণে AgCl এর দ্রাব্যতা S' = K_sp / 0.1 = 10 * K_sp (বিশাল হ্রাস পায়)!",
            "trap": "সম-আয়ন প্রভাবে দ্রাব্যতা (S) হ্রাস পেলেও দ্রাব্যতা গুণফল (K_sp) অপরিবর্তিত থাকে কারণ K_sp কেবল তাপমাত্রার ওপর নির্ভর করে।",
            "tags": ["common ion", "solubility", "সম-আয়ন প্রভাব", "দ্রাব্যতা হ্রাস"]
        }
    ])

    # Periodic Properties
    entries.extend([
        {
            "id": "v_che_pp_01",
            "subject": "Chemistry",
            "chapter": "Periodic Properties",
            "type": "trap",
            "title": "ইলেকট্রন আসক্তির ব্যতিক্রম (Cl > F)",
            "formula": "\\text{ইলেকট্রন আসক্তি: } \\text{Cl} > \\text{F} > \\text{Br} > \\text{I}, \\quad \\text{S} > \\text{O}",
            "concept": "ফ্লোরিনের আকার ২য় শক্তিস্তরে অত্যন্ত ক্ষুদ্র হওয়ায় ইলেকট্রন ঘনত্ব বেশি থাকে এবং আগত ইলেকট্রন তীব্র বিকর্ষণ অনুভব করে, তাই ক্লোরিনের ইলেকট্রন আসক্তি সর্বাধিক।",
            "hack": "তড়িৎ ঋণাত্মকতায় F > O > Cl > N; কিন্তু ইলেকট্রন আসক্তিতে Cl > F > Br > I!",
            "trap": "পরীক্ষায় দ্রুত দাগাতে গিয়ে তড়িৎ ঋণাত্মকতার সাথে ইলেকট্রন আসক্তি গুলিয়ে F দাগালে -0.25 নিশ্চিত।",
            "tags": ["electron affinity", "electronegativity", "ইলেকট্রন আসক্তি", "হ্যালোজেন", "ব্যতিক্রম", "trap"]
        },
        {
            "id": "v_che_pp_02",
            "subject": "Chemistry",
            "chapter": "Periodic Properties",
            "type": "shortcut",
            "title": "আয়নিকরণ শক্তির পর্যায়বৃত্ত ব্যতিক্রম",
            "formula": "\\text{Be} > \\text{B}, \\quad \\text{N} > \\text{O}, \\quad \\text{Mg} > \\text{Al}, \\quad \\text{P} > \\text{S}",
            "concept": "পূর্ণ বা অর্ধপূর্ণ উপস্তরযুক্ত ইলেকট্রন বিন্যাস অধিক সুস্থিত হওয়ায় ইলেকট্রন অপসারণে বেশি শক্তির প্রয়োজন হয়।",
            "hack": "Be (2s^2 পূর্ণ) > B (2p^1); N (2p^3 অর্ধপূর্ণ) > O (2p^4)! সামগ্রিক ২য় পর্যায়: Li < B < Be < C < O < N < F < Ne!",
            "trap": "পর্যায়ে সাধারণত বাম থেকে ডানে বাড়ে, কিন্তু Be-B এবং N-O জোড়ায় ঠিক উল্টো ঘটে।",
            "tags": ["ionization energy", "stability", "আয়নিকরণ শক্তি", "ব্যতিক্রম"]
        },
        {
            "id": "v_che_pp_03",
            "subject": "Chemistry",
            "chapter": "Periodic Properties",
            "type": "core_formula",
            "title": "সংকরায়ন নির্ণয়ের দ্রুত ফর্মুলা",
            "formula": "H = \\frac{1}{2}(V + M - C + A)",
            "concept": "V = কেন্দ্রীয় পরমাণুর যোজ্যতা ইলেকট্রন, M = একযোজী পরমাণু সংখ্যা (H, F, Cl, Br, I), C = ক্যাটায়নের ধনাত্মক চার্জ, A = অ্যানায়নের ঋণাত্মক চার্জ।",
            "hack": "H = 2 (sp, সরলরৈখিক); H = 3 (sp^2, সমতলীয় ত্রিভুজাকার); H = 4 (sp^3, চতুস্তলকীয়); H = 5 (sp^3d, ত্রিকোণীয় দ্বিপিরামিড); H = 6 (sp^3d^2, অষ্টতলকীয়)!",
            "trap": "দ্বিযোজী পরমাণু (যেমন অক্সিজেন O) একযোজী M হিসেবে গণনা করা যাবে না (অক্সিজেনের জন্য M = 0)।",
            "tags": ["hybridization", "VSEPR", "সংকরায়ন", "আণবিক জ্যামিতি"]
        },
        {
            "id": "v_che_pp_04",
            "subject": "Chemistry",
            "chapter": "Periodic Properties",
            "type": "shortcut",
            "title": "ফাজানের পোলারায়ন নীতি ও সমযোজী বৈশিষ্ট্য",
            "formula": "\\text{পোলারায়ন} \\propto \\frac{\\text{ক্যাটায়নের চার্জ}}{\\text{ক্যাটায়নের আকার}} \\times \\text{অ্যানায়নের আকার} \\times (d^{10} \\text{ ক্যাটায়ন})",
            "concept": "পোলারায়ন যত বেশি হয়, যৌগের সমযোজী বৈশিষ্ট্য তত বাড়ে এবং গলনাঙ্ক ও স্ফুটনাঙ্ক তত হ্রাস পায়।",
            "hack": "গলনাঙ্কের ক্রম: NaCl > MgCl2 > AlCl3! সমযোজী বৈশিষ্ট্যের ক্রম: AlCl3 > MgCl2 > NaCl!",
            "trap": "সিউডো-নোবেল গ্যাস ক্যাটায়নের (যেমন Cu+, Ag+, Zn2+) পোলারায়ন ক্ষমতা সাধারণ নিষ্ক্রিয় গ্যাস ক্যাটায়নের (যেমন Na+, K+) চেয়ে বহুগুণ বেশি।",
            "tags": ["Fajan's rule", "polarization", "ফাজানের নীতি", "গলনাঙ্ক", "সমযোজী"]
        },
        {
            "id": "v_che_pp_05",
            "subject": "Chemistry",
            "chapter": "Periodic Properties",
            "type": "core_formula",
            "title": "বন্ধন কোণের ক্রম ও মুক্তজোড় প্রভাব",
            "formula": "CH_4 (109.5^\\circ) > NH_3 (107^\\circ) > H_2O (104.5^\\circ)",
            "concept": "কেন্দ্রীয় পরমাণুর সংকরায়ন sp^3 হলেও মুক্তজোড় ইলেকট্রনের বিকর্ষণের কারণে (lp-lp > lp-bp > bp-bp) বন্ধন কোণ হ্রাস পায়।",
            "hack": "প্রতিটি মুক্তজোড় ইলেকট্রনের জন্য বন্ধন কোণ প্রায় ২° থেকে ২.৫° হ্রাস পায়!",
            "trap": "H2S এর বন্ধন কোণ মাত্র 92° (ড্র্যাগো নীতি মতে সংকরায়ন ঘটে না বললেই চলে)।",
            "tags": ["bond angle", "lone pair", "বন্ধন কোণ", "বিকর্ষণ"]
        },
        {
            "id": "v_che_pp_06",
            "subject": "Chemistry",
            "chapter": "Periodic Properties",
            "type": "trap",
            "title": "জটিল আয়নের সংকরায়ন: [Cu(NH3)4]2+",
            "formula": "[\\text{Cu(NH}_3)_4]^{2+} \\to dsp^2 \\; (\\text{সমতলীয় বর্গাকার}), \\quad [\\text{Ni(CO)}_4] \\to sp^3 \\; (\\text{চতুস্তলকীয়})",
            "concept": "টেট্রাঅ্যামিন কপার(II) আয়নে একটি ইলেকট্রন স্থানান্তরিত হয়ে dsp2 সংকরায়ন ঘটে।",
            "hack": "[Ni(CN)4]2- ও [PtCl4]2- উভয়ই dsp2 সমতলীয় বর্গাকার এবং ডায়াম্যাগনেটিক!",
            "trap": "চারটি লিগ্যান্ড দেখে অন্ধভাবে চতুস্তলকীয় (sp3) ভাববেন না; Cu(NH3)4^2+ নিশ্চিত সমতলীয় বর্গাকার (dsp2)।",
            "tags": ["coordination complex", "dsp2", "জটিল আয়ন", "সংকরায়ন", "trap"]
        },
        {
            "id": "v_che_pp_07",
            "subject": "Chemistry",
            "chapter": "Periodic Properties",
            "type": "core_formula",
            "title": "চৌম্বক ধর্ম ও অযুগ্ম ইলেকট্রন",
            "formula": "\\mu = \\sqrt{n(n + 2)} \\text{ BM} \\quad (n = \\text{অযুগ্ম ইলেকট্রন সংখ্যা})",
            "concept": "অযুগ্ম ইলেকট্রন থাকলে অনুচৌম্বকীয় (প্যারাম্যাগনেটিক); সকল ইলেকট্রন যুগলিত হলে তিরশ্চৌম্বকীয় (ডায়াম্যাগনেটিক)।",
            "hack": "Sc3+, Ti4+, Cu+, Zn2+ এর d উপস্তর শূন্য বা পূর্ণ (d0 বা d10), তাই এরা বর্ণহীন ও ডায়াম্যাগনেটিক!",
            "trap": "Fe3+ এ ৫টি অযুগ্ম ইলেকট্রন থাকে (\\mu = \\sqrt{35} \\approx 5.92 BM); Fe2+ এ ৪টি থাকে (\\mu = \\sqrt{24} \\approx 4.90 BM)।",
            "tags": ["magnetic moment", "paramagnetic", "চৌম্বক ভ্রামক", "বোর ম্যাগনেটন"]
        },
        {
            "id": "v_che_pp_08",
            "subject": "Chemistry",
            "chapter": "Periodic Properties",
            "type": "shortcut",
            "title": "অক্সাইডের অম্ল-ক্ষারক প্রকৃতি",
            "formula": "\\text{ক্ষারীয়} \\to \\text{উভধর্মী} \\to \\text{অম্লীয়} \\quad (\\text{বাম থেকে ডানে})",
            "concept": "পর্যায়ে বামে ক্ষারীয় অক্সাইড (Na2O, MgO), মাঝে উভধর্মী অক্সাইড (Al2O3, ZnO, BeO, PbO) এবং ডানে অম্লীয় অক্সাইড (P4O10, SO3, Cl2O7)।",
            "hack": "উভধর্মী অক্সাইড মনে রাখুন: 'জনাবে আলির বিয়েতে প্রলয় সবারে সানাই বাজাতে দেখলো' (ZnO, Al2O3, BeO, PbO, Sb2O3, SnO)!",
            "trap": "CO, NO, N2O হলো প্রশম অক্সাইড (অম্লীয় বা ক্ষারীয় কোনোটিই নয়)।",
            "tags": ["oxides", "amphoteric", "অক্সাইড", "উভধর্মী", "প্রশম"]
        }
    ])

    # Chemical Changes
    entries.extend([
        {
            "id": "v_che_cc_01",
            "subject": "Chemistry",
            "chapter": "Chemical Changes (Equilibrium/pH)",
            "type": "core_formula",
            "title": "Kp ও Kc এর সাধারণ সম্পর্ক",
            "formula": "K_p = K_c (RT)^{\\Delta n}, \\quad \\Delta n = n_{\\text{products(g)}} - n_{\\text{reactants(g)}}",
            "concept": "যদি \\Delta n = 0 হয় তবে K_p = K_c (যেমন: H2 + I2 <=> 2HI)। K_p এর একক (atm)^{\\Delta n} এবং K_c এর একক (mol L^-1)^{\\Delta n}।",
            "hack": "সমীকরণকে n দিয়ে গুণ করলে নতুন ধ্রুবক K' = K^n; সমীকরণ উল্টে দিলে K' = 1/K!",
            "trap": "শুধুমাত্র গ্যাসীয় পদার্থের মোল সংখ্যা \\Delta n এ অন্তর্ভুক্ত হবে; কঠিন (s) বা বিশুদ্ধ তরল (l) বাদ যাবে।",
            "tags": ["Kp", "Kc", "equilibrium", "সাম্যধ্রুবক", "মোল সংখ্যা"]
        },
        {
            "id": "v_che_cc_02",
            "subject": "Chemistry",
            "chapter": "Chemical Changes (Equilibrium/pH)",
            "type": "shortcut",
            "title": "pH এর দ্রুত শর্টকাট (b - log a)",
            "formula": "[\\text{H}^+] = a \\times 10^{-b} \\text{ M} \\implies \\text{pH} = b - \\log a",
            "concept": "ক্যালকুলেটর ছাড়া লগারিদম ভিত্তিক pH দ্রুত নির্ণয় করার কৌশল।",
            "hack": "[H+] = 2 x 10^-4 M \\implies pH = 4 - 0.30 = 3.70! (\\log 2 = 0.30, \\log 3 = 0.48, \\log 5 = 0.70)!",
            "trap": "10^-8 M HCl দ্রবণের pH 8 দাগানো ভুল; পানির আয়ন যোগ হয়ে সঠিক pH = 6.96!",
            "tags": ["pH shortcut", "logarithm", "লগারিদম", "pH নির্ণয়"]
        },
        {
            "id": "v_che_cc_03",
            "subject": "Chemistry",
            "chapter": "Chemical Changes (Equilibrium/pH)",
            "type": "core_formula",
            "title": "বাফার দ্রবণ ও হেন্ডারসন-হ্যাসেলবাল্ক সমীকরণ",
            "formula": "\\text{অম্লীয়: } \\text{pH} = \\text{p}K_a + \\log\\frac{[\\text{Salt}]}{[\\text{Acid}]}, \\quad \\text{ক্ষারীয়: } \\text{pOH} = \\text{p}K_b + \\log\\frac{[\\text{Salt}]}{[\\text{Base}]}",
            "concept": "মৃদু এসিড ও তার অনুবন্ধী ক্ষারের লবণ মিলে অম্লীয় বাফার গঠন করে। বাফার দ্রবণে সামান্য এসিড বা ক্ষার যোগ করলেও pH প্রায় স্থির থাকে।",
            "hack": "যদি লবণ ও এসিডের মোল সংখ্যা সমান হয়, তবে pH = pKa! বাফারের কার্যকর পরিসীমা: pH = pKa \\pm 1।",
            "trap": "রক্তের বাফার হলো কার্বনিক এসিড-বাইকার্বনেট বাফার (H2CO3 / HCO3^-), যার স্বাভাবিক অনুপাত ১ : ২০ এবং pH = ৭.৪।",
            "tags": ["buffer solution", "Henderson", "বাফার দ্রবণ", "রক্তের বাফার"]
        },
        {
            "id": "v_che_cc_04",
            "subject": "Chemistry",
            "chapter": "Chemical Changes (Equilibrium/pH)",
            "type": "shortcut",
            "title": "দুর্বল এসিডের অসওয়াল্ড লঘুতা সূত্র",
            "formula": "\\alpha = \\sqrt{\\frac{K_a}{C}}, \\quad [\\text{H}^+] = \\sqrt{K_a C} \\implies \\text{pH} = \\frac{1}{2}(\\text{p}K_a - \\log C)",
            "concept": "লঘুতা বৃদ্ধির সাথে সাথে দুর্বল তড়িৎবিশ্লেষ্যের বিয়োজন মাত্রা (\\alpha) বৃদ্ধি পায়।",
            "hack": "যদি ঘনমাত্রা ১০০ গুণ লঘু করা হয় (C/100), তবে বিয়োজন মাত্রা ১০ গুণ বৃদ্ধি পায় (\\alpha \\propto 1/\\sqrt{C})!",
            "trap": "তীব্র এসিডের ক্ষেত্রে বিয়োজন মাত্রা শতভাগ (\\alpha = 1), তাই অসওয়াল্ডের সূত্র কেবল দুর্বল এসিডেই প্রযোজ্য।",
            "tags": ["Ostwald dilution", "weak acid", "লঘুতা সূত্র", "বিয়োজন মাত্রা"]
        },
        {
            "id": "v_che_cc_05",
            "subject": "Chemistry",
            "chapter": "Chemical Changes (Equilibrium/pH)",
            "type": "trap",
            "title": "সাম্যাবস্থায় প্রভাবকের ভূমিকা ও লা শাতেলিয়ার নীতি",
            "formula": "\\text{প্রভাবক কেবল সাম্যাবস্থায় পৌঁছানোর সময় কমায়, Kp বা Kc পরিবর্তন করে না!}",
            "concept": "সাম্যধ্রুবক Kp ও Kc এর মান কেবল এবং কেবলমাত্র তাপমাত্রার পরিবর্তনেই পরিবর্তিত হয়।",
            "hack": "তাপোৎপাদী বিক্রিয়ায় (\\Delta H < 0) তাপমাত্রা বাড়ালে K কমে; তাপহারী বিক্রিয়ায় (\\Delta H > 0) তাপমাত্রা বাড়ালে K বাড়ে!",
            "trap": "চাপ বা ঘনমাত্রা পরিবর্তন করলে সাম্যাবস্থা ডানে বা বাঁয়ে সরে কিন্তু Kp এর মান অপরিবর্তিত থাকে।",
            "tags": ["equilibrium", "catalyst", "Le Chatelier", "লা শাতেলিয়ার নীতি", "সাম্যধ্রুবক", "trap"]
        },
        {
            "id": "v_che_cc_06",
            "subject": "Chemistry",
            "chapter": "Chemical Changes (Equilibrium/pH)",
            "type": "core_formula",
            "title": "প্রশমন তাপ (Heat of Neutralization)",
            "formula": "\\text{তীব্র এসিড + তীব্র ক্ষার: } \\Delta H = -57.34 \\text{ kJ mol}^{-1} = -13.7 \\text{ kcal mol}^{-1}",
            "concept": "এক মোল পানি উৎপন্ন হতে যে পরিমাণ তাপ নির্গত হয়। মূলত H+(aq) + OH-(aq) -> H2O(l) বিক্রিয়ার তাপ।",
            "hack": "ব্যতিক্রম: HF + NaOH এর প্রশমন তাপ -68.6 kJ mol^-1 (ফ্লোরাইড আয়নের উচ্চ হাইড্রেশন তাপের জন্য বেশি)! দুর্বল এসিডের ক্ষেত্রে মান কমে যায় (যেমন অ্যাসিটিক এসিডে -55.2 kJ)।",
            "trap": "H2SO4 তীব্র হলেও প্রতি মোল পানি উৎপন্নে তাপ -57.34 kJ mol^-1; দুই মোল পানি হলে তাপ দ্বিগুণ (-114.68 kJ) হবে।",
            "tags": ["neutralization", "heat", "প্রশমন তাপ", "ব্যতিক্রম"]
        },
        {
            "id": "v_che_cc_07",
            "subject": "Chemistry",
            "chapter": "Chemical Changes (Equilibrium/pH)",
            "type": "shortcut",
            "title": "টাইট্রেশন নির্দেশক নির্বাচন ছক",
            "formula": "\\text{তীব্র এসিড + মৃদু ক্ষার: মিথাইল অরেঞ্জ (৩.১–৪.৪); মৃদু এসিড + তীব্র ক্ষার: ফেনল্ফথ্যালিন (৮.২–৯.৮)}",
            "concept": "তুল্য বিন্দুতে দ্রবণের pH যে নির্দেশকের বর্ণ পরিবর্তনের পরিসরে পড়ে সেটিই উপযুক্ত নির্দেশক।",
            "hack": "তীব্র এসিড তীব্র ক্ষারে যেকোনো নির্দেশক কার্যকর; মৃদু এসিড ও মৃদু ক্ষারে কোনো নির্দেশকই কার্যকর নয়!",
            "trap": "ফেনল্ফথ্যালিন অম্লীয় মাধ্যমে বর্ণহীন কিন্তু ক্ষারীয় মাধ্যমে গোলাপি বর্ণ ধারণ করে।",
            "tags": ["indicators", "titration", "নির্দেশক", "টাইট্রেশন", "pH range"]
        },
        {
            "id": "v_che_cc_08",
            "subject": "Chemistry",
            "chapter": "Chemical Changes (Equilibrium/pH)",
            "type": "core_formula",
            "title": "পানির আয়নিক গুণফল (Kw) ও তাপমাত্রা প্রভাব",
            "formula": "K_w = [\\text{H}^+][\\text{OH}^-] = 10^{-14} \\; (25^\\circ\\text{C} \\text{ এ}), \\quad \\text{pH} + \\text{pOH} = 14",
            "concept": "পানির স্ব-বিয়োজন একটি তাপহারী প্রক্রিয়া, তাই তাপমাত্রা বৃদ্ধিতে Kw এর মান বৃদ্ধি পায়।",
            "hack": "100°C এ Kw \\approx 10^-12, ফলে বিশুদ্ধ পানির pH = 6! কিন্তু পানি তখনও প্রশম থাকে কারণ [H+] = [OH-]।",
            "trap": "100°C এ পানির pH 6 দেখে এটিকে এসিডিক ভাবা ভুল; এটি তখনো সম্পূর্ণ প্রশম।",
            "tags": ["Kw", "ionic product of water", "পানির আয়নিক গুণফল", "তাপমাত্রা"]
        }
    ])

    # Organic Basics
    entries.extend([
        {
            "id": "v_che_ob_01",
            "subject": "Chemistry",
            "chapter": "Organic Basics",
            "type": "core_formula",
            "title": "জৈব যৌগের সংকরায়ন ও বন্ধন কোণ",
            "formula": "\\text{একক বন্ধন: } sp^3 \\; (109.5^\\circ), \\quad \\text{দ্বিবন্ধন: } sp^2 \\; (120^\\circ), \\quad \\text{ত্রিবন্ধন: } sp \\; (180^\\circ)",
            "concept": "সিগমা বন্ধন ও মুক্তজোড় ইলেকট্রন সংখ্যা গুণে সরাসরি সংকরায়ন নির্ণয় করা যায়।",
            "hack": "C=C দ্বিবন্ধনে ১টি সিগমা ও ১টি পাই বন্ধন; C\\equiv C ত্রিবন্ধনে ১টি সিগমা ও ২টি পাই বন্ধন!",
            "trap": "বেনজিন বলয়ে প্রতিটি কার্বন পরমাণু sp2 সংকরায়িত এবং বলয়ে মোট ১২টি সিগমা ও ৩টি পাই বন্ধন থাকে।",
            "tags": ["organic hybridization", "sigma pi", "সংকরায়ন", "বেনজিন", "সিগমা বন্ধন"]
        },
        {
            "id": "v_che_ob_02",
            "subject": "Chemistry",
            "chapter": "Organic Basics",
            "type": "shortcut",
            "title": "জ্যামিতিক সমাণুতার শর্ত ও সিস-ট্রান্স",
            "formula": "abC = Cab \\quad \\text{বা} \\quad abC = Ccd \\quad (a \\neq b, c \\neq d)",
            "concept": "মুক্ত আবর্তন প্রতিহত হওয়া এবং দ্বিবন্ধনযুক্ত কার্বনে দুটি ভিন্ন গ্রুপ যুক্ত থাকা আবশ্যক।",
            "hack": "সিস (Cis) সমাণুর ডাইপোল মোমেন্ট ও স্ফুটনাঙ্ক বেশি; ট্রান্স (Trans) সমাণুর সুষমতার জন্য গলনাঙ্ক ও স্থায়িত্ব বেশি!",
            "trap": "একই কার্বনে দুটি একই গ্রুপ (যেমন CH2=CH-CH3 বা (CH3)2C=CH2) থাকলে জ্যামিতিক সমাণুতা দেখাবে না।",
            "tags": ["geometric isomerism", "cis-trans", "জ্যামিতিক সমাণুতা", "সিস-ট্রান্স"]
        },
        {
            "id": "v_che_ob_03",
            "subject": "Chemistry",
            "chapter": "Organic Basics",
            "type": "core_formula",
            "title": "আলোক সমাণুতা ও কাইরাল কার্বন",
            "formula": "\\text{সম্ভাব্য আলোক সমাণু সংখ্যা} = 2^n \\quad (n = \\text{অপ্রতিসম কাইরাল কার্বন সংখ্যা})",
            "concept": "কাইরাল কেন্দ্রযুক্ত যৌগ যা এক-সমতলীয় আলোর তলকে ডানে (d) বা বামে (l) আবর্তন করে।",
            "hack": "ল্যাকটিক এসিডে (CH3-CH(OH)-COOH) ১টি কাইরাল কার্বন, তাই আলোক সমাণু = 2^1 = 2টি!",
            "trap": "মেসো যৌগ অভ্যন্তরীণ ক্ষতিপূরণের কারণে আলোক নিষ্ক্রিয় হয় (যেমন মেসো-টারটারিক এসিড)।",
            "tags": ["optical isomerism", "chiral carbon", "আলোক সমাণুতা", "কাইরাল কার্বন", "মেসো যৌগ"]
        },
        {
            "id": "v_che_ob_04",
            "subject": "Chemistry",
            "chapter": "Organic Basics",
            "type": "shortcut",
            "title": "হাকেল নিয়ম ও অ্যারোমেটিসিটি (4n + 2)",
            "formula": "\\text{হাকেল পাই ইলেকট্রন} = 4n + 2 \\quad (n = 0, 1, 2, 3, \\dots)",
            "concept": "বলয়াকার, সমতলীয় এবং সম্পূর্ণ সঞ্চারণশীল (4n+2) সংখ্যক পাই ইলেকট্রন থাকতে হবে।",
            "hack": "n=1: ৬টি পাই e- (বেনজিন, পিরিডিন, পিরোল, ফিউরান); n=2: ১০টি পাই e- (ন্যাপথালিন); n=3: ১৪টি পাই e- (অ্যানথ্রাসিন)!",
            "trap": "সাইক্লোঅক্টাটেট্রাইন (৮টি পাই e-) হাকেল নিয়ম মানে না, তাই এটি নন-অ্যারোমেটিক।",
            "tags": ["Huckel's rule", "aromaticity", "হাকেল নিয়ম", "অ্যারোমেটিক"]
        },
        {
            "id": "v_che_ob_05",
            "subject": "Chemistry",
            "chapter": "Organic Basics",
            "type": "trap",
            "title": "কার্বোক্যাটায়নের স্থায়িত্বের ক্রম (3° > 2° > 1°)",
            "formula": "3^\\circ > 2^\\circ > 1^\\circ > \\text{মিথাইল} \\; (\\text{কার্বোক্যাটায়ন ও মুক্ত মূলক}), \\quad 1^\\circ > 2^\\circ > 3^\\circ \\; (\\text{কার্বানায়ন})",
            "concept": "হাইপারকনজুগেশন এবং অ্যালকাইল গ্রুপের ইলেকট্রন দাতা (+I) আবেশীয় ফলের কারণে ৩° কার্বোক্যাটায়ন সর্বাধিক সুস্থিত।",
            "hack": "SN1 ও E1 বিক্রিয়া ৩° হ্যালাইডে দ্রুত ঘটে; আর SN2 বিক্রিয়া ১° হ্যালাইডে সবচেয়ে দ্রুত ঘটে!",
            "trap": "কার্বানায়নের ক্ষেত্রে স্থায়িত্বের ক্রম সম্পূর্ণ উল্টো (1° > 2° > 3°)! মুখস্থ করে গুলিয়ে ফেলবেন না।",
            "tags": ["carbocation", "stability", "কার্বোক্যাটায়ন", "স্থায়িত্ব", "SN1", "SN2"]
        },
        {
            "id": "v_che_ob_06",
            "subject": "Chemistry",
            "chapter": "Organic Basics",
            "type": "shortcut",
            "title": "বেনজিন বলয়ে অর্থো-প্যারা বনাম মেটা নির্দেশক",
            "formula": "\\text{অর্থো-প্যারা: } -\\text{OH}, -\\text{NH}_2, -\\text{R}, -\\text{X}; \\quad \\text{মেটা: } -\\text{NO}_2, -\\text{COOH}, -\\text{CHO}, -\\text{CN}",
            "concept": "যেসব গ্রুপে মুক্তজোড় ইলেকট্রন থাকে বা দ্বিবন্ধন থাকে না তারা সাধারণত অর্থো-প্যারা নির্দেশক (বলয় সক্রিয়কারী)।",
            "hack": "যদি যুক্ত পরমাণুতে দ্বিবন্ধন বা ত্রিবন্ধন থাকে (যেমন -C=O, -N=O, -C\\equiv N) তবে তারা সর্বদা মেটা নির্দেশক (নিষ্ক্রিয়কারী)!",
            "trap": "হ্যালোজেন (-X) অর্থো-প্যারা নির্দেশক হলেও এটি বলয় নিষ্ক্রিয়কারী গ্রুপ (ব্যতিক্রমী বৈশিষ্ট্য)।",
            "tags": ["directing groups", "ortho-para", "meta", "অর্থো-প্যারা", "মেটা নির্দেশক"]
        },
        {
            "id": "v_che_ob_07",
            "subject": "Chemistry",
            "chapter": "Organic Basics",
            "type": "core_formula",
            "title": "মারকনিকভের নীতি ও অ্যান্টি-মারকনিকভ (পার-অক্সাইড ফল)",
            "formula": "\\text{মারকনিকভ: 'তেলে মাথায় তেল দেওয়া'} \\implies \\text{H যুক্ত হবে বেশি H বিশিষ্ট কার্বনে}",
            "concept": "অপ্রতিসম অ্যালকিনে অপ্রতিসম বিকারক (HBr) যুক্ত হলে ঋণাত্মক অংশ (Br-) কম হাইড্রোজেনযুক্ত কার্বনে যুক্ত হয়।",
            "hack": "জৈব পার-অক্সাইডের (R2O2) উপস্থিতিতে কেবল HBr অ্যান্টি-মারকনিকভ নীতি মেনে চলে (HCl বা HI নয়)!",
            "trap": "অ্যান্টি-মারকনিকভ বিক্রিয়া কেবল HBr এর জন্য প্রযোজ্য; HCl দিলে পার-অক্সাইড থাকা সত্ত্বেও মারকনিকভ উৎপাদই হবে।",
            "tags": ["Markovnikov", "peroxide effect", "মারকনিকভের নীতি", "খারাশের নীতি"]
        },
        {
            "id": "v_che_ob_08",
            "subject": "Chemistry",
            "chapter": "Organic Basics",
            "type": "shortcut",
            "title": "টটোমারিজম ও কিটো-ইনল সমাণুতা",
            "formula": "\\text{কিটো রূপ } (-CH_2-CO-) \\rightleftharpoons \\text{ইনল রূপ } (-CH=C(OH)-)",
            "concept": "একটি গতিশীল কার্যকরী মূলক সমাণুতা যেখানে হাইড্রোজেন পরমাণুর স্বতঃস্ফূর্ত স্থানান্তরের মাধ্যমে কিটো ও ইনল কাঠামো তৈরি হয়।",
            "hack": "প্রোপানোন (অ্যাসিটোন) টটোমারিজম প্রদর্শন করে প্রোপ-১-ইন-২-অল তৈরি করে!",
            "trap": "টটোমারিজমে প্রোটন স্থানান্তরের সাথে সাথে পাই বন্ধনের স্থানান্তর ঘটে; রেজোন্যান্সে কোনো পরমাণুর স্থানান্তর ঘটে না।",
            "tags": ["tautomerism", "keto-enol", "টটোমারিজম", "কিটো-ইনল"]
        }
    ])

    # Environmental Chem
    entries.extend([
        {
            "id": "v_che_ec_01",
            "subject": "Chemistry",
            "chapter": "Environmental Chem",
            "type": "core_formula",
            "title": "বায়ুমণ্ডলের স্তরবিন্যাস ও ল্যাপস রেট",
            "formula": "\\text{ল্যাপস রেট} = -6.5^\\circ\\text{C km}^{-1} \\; (\\text{ট্রপোমণ্ডলে প্রতি কিমিতে তাপমাত্রা হ্রাস})",
            "concept": "ট্রপোস্ফিয়ার (ক্ষুব্ধমণ্ডল, 0-12 km), স্ট্র্যাটোস্ফিয়ার (শান্তমণ্ডল ও ওজোনস্তর, 12-50 km), মেসোস্ফিয়ার (-93°C শীতলতম), থার্মোস্ফিয়ার।",
            "hack": "বিমান চলাচল করে স্ট্র্যাটোস্ফিয়ারে কারণ সেখানে মেঘ-বৃষ্টি ও ঝড় থাকে না; ওজোনস্তর অতিবেগুনী রশ্মি (UV) শোষণ করে!",
            "trap": "মেসোস্ফিয়ারে তাপমাত্রা সর্বনিম্ন (-93°C) হয়, স্ট্র্যাটোস্ফিয়ারে নয়।",
            "tags": ["atmosphere", "troposphere", "stratosphere", "বায়ুমণ্ডল", "ওজোনস্তর", "ল্যাপস রেট"]
        },
        {
            "id": "v_che_ec_02",
            "subject": "Chemistry",
            "chapter": "Environmental Chem",
            "type": "shortcut",
            "title": "পানির বিশুদ্ধতার মানদণ্ড (DO, BOD, COD, TDS)",
            "formula": "\\text{আদর্শ DO} = 4 - 6 \\text{ ppm}, \\quad \\text{সর্বদা: } \\text{COD} > \\text{BOD}",
            "concept": "DO = দ্রবীভূত অক্সিজেন; BOD = জৈব বর্জ্য ভাঙতে ব্যাকটেরিয়ার প্রয়োজনীয় অক্সিজেন; COD = জৈব ও অজৈব সকল বর্জ্যের জন্য মোট অক্সিজেন।",
            "hack": "পানীয় জলের আদর্শ pH: 6.5 - 8.5; WHO মতে পানিতে আর্সেনিকের সর্বোচ্চ নিরাপদ মাত্রা 0.01 ppm (বাংলাদেশে 0.05 ppm)!",
            "trap": "পানির দূষণ যত বাড়ে, BOD ও COD তত বাড়ে কিন্তু DO তত হ্রাস পায় (ব্যস্তানুপাতিক সম্পর্ক)।",
            "tags": ["DO", "BOD", "COD", "water pollution", "পানির বিশুদ্ধতা"]
        },
        {
            "id": "v_che_ec_03",
            "subject": "Chemistry",
            "chapter": "Environmental Chem",
            "type": "core_formula",
            "title": "গ্রিনহাউস গ্যাস ও বৈশ্বিক উষ্ণায়ন ক্ষমতা (GWP)",
            "formula": "\\text{অবদান: } \\text{CO}_2 (50\\%) > \\text{CH}_4 (18\\%) > \\text{CFC} (14\\%) > \\text{O}_3 (8\\%) > \\text{N}_2\\text{O} (6\\%)",
            "concept": "গ্রিনহাউস প্রভাবের প্রধান গ্যাস কার্বন ডাই-অক্সাইড। তবে অণু প্রতি ক্ষতিকর বিবেচনায় CFC ও মিথেন অনেক গুণ বেশি মারাত্মক।",
            "hack": "GWP ক্ষমতা: SF6 > CFC > N2O > CH4 > CO2! একক অণু হিসেবে SF6 সর্বাধিক শক্তিশালী গ্রিনহাউস গ্যাস।",
            "trap": "জলীয় বাষ্প প্রাকৃতিক গ্রিনহাউস প্রভাবের ৬০% এর বেশি নিয়ন্ত্রণ করে, তবে মানবসৃষ্ট দূষণে CO2 শীর্ষে।",
            "tags": ["greenhouse gas", "global warming", "GWP", "গ্রিনহাউস গ্যাস"]
        },
        {
            "id": "v_che_ec_04",
            "subject": "Chemistry",
            "chapter": "Environmental Chem",
            "type": "shortcut",
            "title": "CFC এর সংকেত ও ওজন ক্ষয় কৌশল",
            "formula": "\\text{CFC-xyz}: \\quad x = \\text{কার্বন}-1, \\; y = \\text{হাইড্রোজেন}+1, \\; z = \\text{ফ্লোরিন}",
            "concept": "ক্লোরোফ্লোরোকার্বন সূর্যের অতিবেগুনী আলোতে বিয়োজিত হয়ে মুক্ত ক্লোরিন পরমাণু (Cl*) তৈরি করে যা হাজার হাজার ওজোন অণু ধ্বংস করে।",
            "hack": "CFC-11 (CFCl3), CFC-12 (CF2Cl2), CFC-113 (C2F3Cl3)! যেমন CFC-11: C-1=0, H+1=1, F=1 -> নাম 11!",
            "trap": "১টি সক্রিয় ক্লোরিন মুক্ত মূলক প্রায় ১ লক্ষ ওজোন (O3) অণুকে ভেঙে অক্সিজেনে পরিণত করতে পারে।",
            "tags": ["CFC", "ozone depletion", "ওজোন ক্ষয়", "মুক্ত মূলক"]
        },
        {
            "id": "v_che_ec_05",
            "subject": "Chemistry",
            "chapter": "Environmental Chem",
            "type": "trap",
            "title": "এসিড বৃষ্টি (Acid Rain) ও pH সীমা",
            "formula": "\\text{বৃষ্টির পানির pH } < 5.6 \\implies \\text{এসিড বৃষ্টি}",
            "concept": "স্বাভাবিক বৃষ্টির পানিতে দ্রবীভূত CO2 থাকার কারণে এর pH প্রায় 5.6 থাকে। কিন্তু SO2 ও NOx গ্যাস বৃষ্টির পানির সাথে মিশে H2SO4 ও HNO3 তৈরি করলে pH 5.6 এর নিচে নেমে যায়।",
            "hack": "এসিড বৃষ্টির প্রধান গ্যাস SO2 (প্রায় ৬০-৭০%) এবং দ্বিতীয়টি NO2 (প্রায় ৩০%)!",
            "trap": "স্বাভাবিক বৃষ্টির পানিও কিছুটা অম্লীয় (pH 5.6); তাই pH 7 এর নিচে নামলেই এসিড বৃষ্টি বলা যাবে না, 5.6 এর নিচে হতে হবে।",
            "tags": ["acid rain", "pH limit", "এসিড বৃষ্টি", "SO2", "trap"]
        },
        {
            "id": "v_che_ec_06",
            "subject": "Chemistry",
            "chapter": "Environmental Chem",
            "type": "core_formula",
            "title": "ভারী ধাতু দূষণ ও মানবদেহের ক্ষতি",
            "formula": "\\text{Pb (লেড), Cd (ক্যাডমিয়াম), Hg (পারদ), As (আর্সেনিক), Cr (ক্রোমিয়াম)}",
            "concept": "ভারী ধাতু মানবদেহে এনজাইমের সাথে আবদ্ধ হয়ে বিষক্রিয়া তৈরি করে এবং খাদ্যশৃঙ্খলে বায়োম্যাগনিফিকেশন ঘটায়।",
            "hack": "পারদ (Hg) দূষণে মিনামাটা রোগ; ক্যাডমিয়াম (Cd) দূষণে ইতাই-ইতাই বা অউচ-অউচ রোগ; আর্সেনিক (As) দূষণে ব্ল্যাক ফুট রোগ!",
            "trap": "লেড রক্তের হিমোগ্লোবিন তৈরিতে বাধা দেয় এবং শিশুদের মস্তিষ্কের বিকাশ ব্যাহত করে।",
            "tags": ["heavy metals", "Minamata", "Itai-Itai", "ভারী ধাতু", "মিনামাটা"]
        },
        {
            "id": "v_che_ec_07",
            "subject": "Chemistry",
            "chapter": "Environmental Chem",
            "type": "shortcut",
            "title": "লুইস এসিড ও ক্ষারক অম্ল-ক্ষার মতবাদ",
            "formula": "\\text{লুইস এসিড: ইলেকট্রন জোড় গ্রহীতা (অষ্টক অপূর্ণ)}; \\quad \\text{লুইস ক্ষার: ইলেকট্রন জোড় দাতা}",
            "concept": "BF3, AlCl3, FeCl3, ক্যাটায়ন (H+, Ag+) হলো লুইস এসিড। NH3, H2O, অ্যালকোহল, অ্যানায়ন (Cl-, OH-) হলো লুইস ক্ষার।",
            "hack": "BF3 + :NH3 -> F3B <- NH3 সন্নিবেশ বন্ধন তৈরি করে, যেখানে NH3 লুইস ক্ষার এবং BF3 লুইস এসিড!",
            "trap": "অক্সিজেন বা নাইট্রোজেনের মুক্তজোড় থাকা সত্ত্বেও যদি ধনাত্মক চার্জ থাকে (যেমন H3O+, NH4+) তবে তারা লুইস ক্ষার নয়।",
            "tags": ["Lewis acid", "base", "লুইস এসিড", "লুইস ক্ষার"]
        }
    ])

    return entries

def get_all_vault_entries():
    all_entries = []
    all_entries.extend(get_phy_entries())
    all_entries.extend(get_chem_entries())
    all_entries.extend(get_math_entries())
    all_entries.extend(get_bio_entries())
    all_entries.extend(get_english_entries())
    all_entries.extend(get_gk_entries())
    return all_entries

def build_vault_file():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OUT_DIR = os.path.join(BASE_DIR, "admission_webapp", "src", "data")
    os.makedirs(OUT_DIR, exist_ok=True)

    entries = get_all_vault_entries()

    # Legacy datasets for backward compatibility
    triplets = [
        {"sides": "(3, 4)", "result": "5", "app": "বেগ $v_x=4, v_y=3 \\Rightarrow v=5\\text{ ms}^{-1}$; সরলরেখা $3x+4y+c=0$-এর লম্ব দূরত্বের হর $=5$; অনুবন্ধী অধিবৃত্ত $e_1=5/3 \\implies e_2=5/4$"},
        {"sides": "(5, 12)", "result": "13", "app": "সরলরেখা $5x+12y+c=0$-এর হর $=13$; $\\sin\\theta = 5/13 \\Rightarrow \\cos\\theta = 12/13$"},
        {"sides": "(6, 8)", "result": "10", "app": "নদী-নৌকায় $\\sqrt{10^2 - 6^2} = 8\\text{ ms}^{-1}$ (ন্যূনতম দূরত্বে নদী পারাপার)"},
        {"sides": "(8, 15)", "result": "17", "app": "ত্রিভুজ ও ভেক্টর মান নির্ণয়"},
        {"sides": "(7, 24)", "result": "25", "app": "ত্রিকোণমিতিক অনুপাত ও সরলরেখার দূরত্ব"},
        {"sides": "(1, 2, 2)", "result": "3", "app": "ত্রিমাত্রিক ভেক্টর $\\vec{A} = \\hat{i} + 2\\hat{j} + 2\\hat{k} \\Rightarrow |\\vec{A}| = 3$"},
        {"sides": "(2, 3, 6)", "result": "7", "app": "ত্রিমাত্রিক ভেক্টর $\\vec{B} = 2\\hat{i} - 3\\hat{j} + 6\\hat{k} \\Rightarrow |\\vec{B}| = 7$ (অভিক্ষেপ প্রশ্নে সবচেয়ে বেশি আসে!)"},
        {"sides": "(1, 4, 8)", "result": "9", "app": "একক ভেক্টর ও দিক কোসাইন নির্ণয়"}
    ]

    quick_math = [
        {"type": "বর্গমূল", "item": "$\\sqrt{2} \\approx 1.414, \\; \\sqrt{3} \\approx 1.732, \\; \\sqrt{5} \\approx 2.236, \\; \\sqrt{10} \\approx \\pi \\approx 3.16$"},
        {"type": "অমসৃণ বর্গমূল সূত্র", "item": "$\\sqrt{N^2 \\pm d} \\approx N \\pm \\frac{d}{2N} \\quad (\\text{যেমন: } \\sqrt{45} = \\sqrt{36+9} \\approx 6 + \\frac{9}{12} = 6.75)$"},
        {"type": "লগারিদম (pH)", "item": "$\\log 2 \\approx 0.30, \\; \\log 3 \\approx 0.48, \\; \\log 5 \\approx 0.70, \\; \\log 7 \\approx 0.85$"},
        {"type": "pH সুপার শর্টকাট", "item": "$[\\text{H}^+] = a \\times 10^{-b}\\text{ M} \\implies \\text{pH} = b - \\log a$"},
        {"type": "জটিল সংখ্যার বর্গমূল", "item": "$\\sqrt{a \\pm ib} = \\pm(p \\pm iq) \\quad \\text{যেখানে } p \\times q = \\frac{b}{2} \\text{ এবং } p^2 - q^2 = a$"},
        {"type": "কৌণিক বেগ rpm", "item": "$\\omega = \\frac{2\\pi N}{60} = \\frac{\\pi N}{30}\\text{ rad s}^{-1} \\quad (30\\text{ rpm}=\\pi, \\; 60\\text{ rpm}=2\\pi, \\; 300\\text{ rpm}=10\\pi)$"},
        {"type": "গ্যাস ধ্রুবক RT", "item": "$0^\\circ\\text{C}: 22.4\\text{ L atm}; \\; 25^\\circ\\text{C}: 24.46\\text{ L atm}; \\; 27^\\circ\\text{C}: 24.63\\text{ L atm} \\approx 2500\\text{ J}$"},
        {"type": "মুক্তিবেগ ও কক্ষীয় বেগ", "item": "$v_e = \\sqrt{2}v_o \\approx 1.414 v_o \\implies 41.4\\% \\text{ বৃদ্ধি (পৃথিবী } v_e=11.2, \\; v_o=7.92\\text{ km s}^{-1})$"},
        {"type": "শোয়ার্জশিল্ড ব্যাসার্ধ", "item": "$R_s = \\frac{2GM}{c^2} \\quad (\\text{পৃথিবী: } \\approx 8.86\\text{ mm} \\approx 0.9\\text{ cm}; \\; \\text{সূর্য: } \\approx 3\\text{ km})$"},
        {"type": "বোর ব্যাসার্ধ ও শক্তি", "item": "$r_n = 0.529 n^2\\text{ \\AA}, \\; v_n = \\frac{2.18\\times 10^6}{n}\\text{ m s}^{-1}, \\; E_n = -\\frac{13.6}{n^2}\\text{ eV}$"},
        {"type": "Ksp ও দ্রাব্যতা শর্টকাট", "item": "$AB \\to s=\\sqrt{K_{sp}}; \\; AB_2 \\to s=\\sqrt[3]{\\frac{K_{sp}}{4}}; \\; AB_3 \\to s=\\sqrt[4]{\\frac{K_{sp}}{27}}; \\; A_2B_3 \\to s=\\sqrt[5]{\\frac{K_{sp}}{108}}$"},
        {"type": "উপবৃত্তের উৎকেন্দ্রিকতা", "item": "$e = \\sqrt{1 - \\frac{\\text{ছোট হর}}{\\text{বড় হর}}} \\quad (\\text{যেমন: } \\frac{x^2}{25}+\\frac{y^2}{16}=1 \\implies e = \\frac{3}{5})$"},
        {"type": "অনুবন্ধী অধিবৃত্ত", "item": "$\\frac{1}{e_1^2} + \\frac{1}{e_2^2} = 1 \\quad (\\text{৩-৪-৫ ট্রিপলেট: } e_1=\\frac{5}{3} \\implies e_2=\\frac{5}{4})$"},
        {"type": "পরমমান কেন্দ্র-ব্যাসার্ধ", "item": "$a < x < b \\iff |x - m| < r \\quad \\text{যেখানে } m = \\frac{a+b}{2}, \\; r = \\frac{b-a}{2}$"}
    ]

    magic_fractions = [
        {"compound": "$\\text{Na}_2\\text{CO}_3$", "mw": "106", "trick": "$13.25\\text{ g} = \\frac{1}{8}\\text{ mol} = 0.125\\text{ mol}; \\quad 26.5\\text{ g} = \\frac{1}{4}\\text{ mol} = 0.25\\text{ mol}$"},
        {"compound": "$\\text{CaCO}_3$", "mw": "100", "trick": "$444.44\\text{ g} \\text{ নমুনায় } 90\\% \\text{ বিশুদ্ধতা } \\Rightarrow 400\\text{ g} = 4\\text{ mol}$"},
        {"compound": "$\\text{MgCO}_3$", "mw": "84", "trick": "$1\\text{ kg} \\Rightarrow \\text{STP-তে CO}_2 = \\frac{1000}{84} \\times 22.4 = \\frac{800}{3} \\approx 266.67\\text{ L}$"},
        {"compound": "$\\text{KClO}_3$", "mw": "122.5", "trick": "$122.5\\text{ g} = 1\\text{ mol} \\Rightarrow 1.5\\text{ mol O}_2 = 1.5 \\times 22.4 = 33.6\\text{ L}$"},
        {"compound": "$\\text{K}_2\\text{Cr}_2\\text{O}_7$", "mw": "294", "trick": "$M = 294 = 3 \\times 98; \\quad 1\\text{ mol} \\equiv 6e^- (\\text{অম্লীয় মাধ্যমে})$"},
        {"compound": "$\\text{KMnO}_4$", "mw": "158", "trick": "$1\\text{ mol} \\equiv 5e^- (\\text{অম্লীয়}), \\equiv 3e^- (\\text{ক্ষারীয়/প্রশম})$"},
        {"compound": "$\\text{Ag}_2\\text{CrO}_4$", "mw": "332", "trick": "$K_{sp} = 4s^3 \\implies 3\\text{টি আয়ন তৈরি হয়}$"},
        {"compound": "$\\text{BaSO}_4$", "mw": "233", "trick": "গ্রুপ-২ এর মধ্যে সর্বনিম্ন দ্রবণীয় ($K_{sp} \\approx 1.1\\times 10^{-10}$)"},
        {"compound": "$\\text{Ca(OH)}_2$", "mw": "74", "trick": "গ্রুপ-২ হাইড্রোক্সাইডের দ্রাব্যতা নিচে বৃদ্ধি পায়"}
    ]

    patterns = [
        {"code": "PHY-W01-P1", "week": "week_01", "subject": "Physics", "title": "লম্ব ও সমান্তরাল ভেক্টর", "formula": "লম্ব: $\\vec{A}\\cdot\\vec{B}=0$; সমান্তরাল: $\\frac{A_x}{B_x}=\\frac{A_y}{B_y}=\\frac{A_z}{B_z}$"},
        {"code": "PHY-W01-P2", "week": "week_01", "subject": "Physics", "title": "অভিক্ষেপ বনাম উপাংশ", "formula": "স্কেলার অভিক্ষেপ: $\\frac{\\vec{A}\\cdot\\vec{B}}{|\\vec{B}|}$; ভেক্টর উপাংশ: $\\left(\\frac{\\vec{A}\\cdot\\vec{B}}{|\\vec{B}|^2}\\right)\\vec{B}$"},
        {"code": "CHE-W01-P1", "week": "week_01", "subject": "Chemistry", "title": "ঘনমাত্রা রূপান্তর", "formula": "$M = \\frac{10x}{M_w}$; $\\text{ppm} = M \\times M_w \\times 1000 = \\%(w/v) \\times 10^4$"},
        {"code": "MAT-W01-P1", "week": "week_01", "subject": "Higher Math", "title": "৪র্থ শীর্ষ ও ইউলার রেখা", "formula": "সামান্তরিক ৪র্থ শীর্ষ: $D = A + C - B$; ইউলার রেখা: $HG : GO = 2 : 1$"}
    ]

    traps = [
        {"id": 1, "week": "week_01", "subject": "Physics", "trap": "কর্ণ ভেক্টর দেওয়া থাকলে সামান্তরিকের ক্ষেত্রফল ||A×B|| লিখে ফেলা", "fix": "কর্ণ হলে অবশ্যই সামনে 1/2 গুণ হবে: Area = (1/2)|d1 × d2|।"},
        {"id": 2, "week": "week_01", "subject": "Chemistry", "trap": "হ্যালোজেনের ইলেকট্রন আসক্তির ক্রমে F > Cl দাগানো", "fix": "তড়িৎ ঋণাত্মকতায় F > Cl, কিন্তু ইলেকট্রন আসক্তিতে Cl > F > Br > I।"},
        {"id": 3, "week": "week_01", "subject": "Higher Math", "trap": "ax^2 + ay^2 + ... বৃত্তে a দিয়ে ভাগ না করে কেন্দ্র ও ব্যাসার্ধ লেখা", "fix": "আগে সমীকরণকে a দিয়ে ভাগ করে x^2 ও y^2-এর সহগ 1 বানিয়ে নেবে।"}
    ]

    vault_data = {
        "entries": entries,
        "triplets": triplets,
        "quick_math": quick_math,
        "magic_fractions": magic_fractions,
        "patterns": patterns,
        "traps": traps
    }

    out_file = os.path.join(OUT_DIR, "vault.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(vault_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] {len(entries)} Formula & Trap Vault entries saved to {out_file}")
    return vault_data

if __name__ == "__main__":
    build_vault_file()
