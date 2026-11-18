import { BANK_INDEX, type ChapterIndexEntry } from './library';

export interface CanonicalChapterGroup {
  key: string;
  subject: string;
  paper: '১ম পত্র' | '২য় পত্র' | 'কমন';
  order: number;
  chapter_name: string;
  primary_chapter_id: string;
  merged_chapter_ids: string[];
  /** Additional Bengali keywords for matching paper_final / master / varsity_bank chapters */
  match_keywords: string[];
  count: number;
  years_hit: number;
  papers_hit: number;
  predicted_pct: number;
  expected_mcq_du_ka: number;
  expected_mcq_mat: number;
}

interface CanonicalRule {
  key: string;
  subject: string;
  paper: '১ম পত্র' | '২য় পত্র' | 'কমন';
  order: number;
  name: string;
  ids: string[];
  keywords: string[];
}

const CANONICAL_RULES: CanonicalRule[] = [
  // ================= PHYSICS (1st Paper -> 2nd Paper) =================
  { key: 'phy_1_01', subject: 'Physics', paper: '১ম পত্র', order: 1, name: 'ভৌতজগৎ ও পরিমাপ', ids: ['ভ_তজগৎ_ও_পর_ম_প'], keywords: ['ভৌতজগৎ', 'পরিমাপ', 'স্ক্রু গজ', 'ভার্নিয়ার', 'ত্রুটি'] },
  { key: 'phy_1_02', subject: 'Physics', paper: '১ম পত্র', order: 2, name: 'ভেক্টর', ids: ['ভ_ক_টর'], keywords: ['ভেক্টর', 'vector'] },
  { key: 'phy_1_03', subject: 'Physics', paper: '১ম পত্র', order: 3, name: 'গতিবিদ্যা ও প্রক্ষেপক', ids: ['গত_ব_দ_য_ও_প_রক_ষ_পক'], keywords: ['গতিবিদ্যা', 'প্রক্ষেপক', 'প্রাস'] },
  { key: 'phy_1_04', subject: 'Physics', paper: '১ম পত্র', order: 4, name: 'নিউটনীয় বলবিদ্যা', ids: ['ন_উটন_য_বলব_দ_য'], keywords: ['নিউটনীয় বলবিদ্যা', 'টর্ক', 'জড়তার ভ্রামক', 'কৌণিক'] },
  { key: 'phy_1_05', subject: 'Physics', paper: '১ম পত্র', order: 5, name: 'কাজ, শক্তি ও ক্ষমতা', ids: ['ক_জ_শক_ত_ও_ক_ষমত'], keywords: ['কাজ', 'শক্তি', 'ক্ষমতা'] },
  { key: 'phy_1_06', subject: 'Physics', paper: '১ম পত্র', order: 6, name: 'মহাকর্ষ ও অভিকর্ষ', ids: ['মহ_কর_ষ_ও_অভ_কর_ষ'], keywords: ['মহাকর্ষ', 'অভিকর্ষ', 'মুক্তিবেগ', 'স্যাটেলাইট'] },
  { key: 'phy_1_07', subject: 'Physics', paper: '১ম পত্র', order: 7, name: 'পদার্থের গাঠনিক ধর্ম', ids: ['পদ_র_থ_র_গ_ঠন_ক_ধর_ম'], keywords: ['গাঠনিক ধর্ম', 'স্থিতিস্থাপক', 'পীড়ন', 'সান্দ্রতা', 'পৃষ্ঠটান'] },
  { key: 'phy_1_08', subject: 'Physics', paper: '১ম পত্র', order: 8, name: 'পর্যায়বৃত্ত গতি', ids: ['পর_য_য_ব_ত_ত_গত'], keywords: ['পর্যায়বৃত্ত গতি', 'সরল দোলক', 'সরল ছন্দিত'] },
  { key: 'phy_1_09', subject: 'Physics', paper: '১ম পত্র', order: 9, name: 'তরঙ্গ', ids: ['তরঙ_গ'], keywords: ['তরঙ্গ', 'শব্দ', 'স্থির তরঙ্গ', 'বীট'] },
  { key: 'phy_1_10', subject: 'Physics', paper: '১ম পত্র', order: 10, name: 'আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব', ids: ['আদর_শ_গ_য_স_ও_গ_য_স_র_গত_তত_ত_ব'], keywords: ['আদর্শ গ্যাস', 'গতিতত্ত্ব', 'শিশিরাঙ্ক'] },
  { key: 'phy_2_01', subject: 'Physics', paper: '২য় পত্র', order: 11, name: 'তাপগতিবিদ্যা', ids: ['ত_পগত_ব_দ_য'], keywords: ['তাপগতিবিদ্যা', 'কার্নো', 'এনট্রপি'] },
  { key: 'phy_2_02', subject: 'Physics', paper: '২য় পত্র', order: 12, name: 'স্থির তড়িৎ', ids: ['স_থ_র_তড_ৎ'], keywords: ['স্থির তড়িৎ', 'ধারক', 'গাউস'] },
  { key: 'phy_2_03', subject: 'Physics', paper: '২য় পত্র', order: 13, name: 'চল তড়িৎ', ids: ['চল_তড_ৎ'], keywords: ['চল তড়িৎ', 'ওহম', 'কার্শফ', 'হুইটস্টোন'] },
  { key: 'phy_2_04', subject: 'Physics', paper: '২য় পত্র', order: 14, name: 'তড়িৎ প্রবাহের চৌম্বক ক্রিয়া ও চুম্বকত্ব', ids: ['তড_ৎ_প_রব_হ_র_চ_ম_বক_ক_র_য_ও_চ_ম_বকত_ব'], keywords: ['চৌম্বক ক্রিয়া', 'চুম্বকত্ব', 'বায়ো-স্যাভার্ট'] },
  { key: 'phy_2_05', subject: 'Physics', paper: '২য় পত্র', order: 15, name: 'তাড়িৎচৌম্বকীয় আবেশ ও পরিবর্তী প্রবাহ', ids: ['ত_ড_ৎচ_ম_বক_য_আব_শ_ও_পর_বর_ত_প_রব_হ'], keywords: ['তাড়িৎচৌম্বকীয় আবেশ', 'পরিবর্তী প্রবাহ', 'ট্রান্সফরমার'] },
  { key: 'phy_2_08', subject: 'Physics', paper: '২য় পত্র', order: 18, name: 'আধুনিক পদার্থবিজ্ঞানের সূচনা', ids: ['আধ_ন_ক_পদ_র_থব_জ_ঞ_ন_র_স_চন'], keywords: ['আধুনিক পদার্থবিজ্ঞান', 'ফটোতড়িৎ', 'আপেক্ষিকতা'] },
  { key: 'phy_2_09', subject: 'Physics', paper: '২য় পত্র', order: 19, name: 'পরমাণুর মডেল ও নিউক্লিয়ার পদার্থবিজ্ঞান', ids: ['পরম_ণ_র_মড_ল_ও_ন_উক_ল_য_র_পদ_র_থব_জ_ঞ_ন'], keywords: ['পরমাণুর মডেল', 'নিউক্লিয়ার', 'তেজস্ক্রিয়'] },
  { key: 'phy_2_10', subject: 'Physics', paper: '২য় পত্র', order: 20, name: 'সেমিকন্ডাক্টর ও ইলেকট্রনিক্স', ids: ['স_ম_কন_ড_ক_টর_ও_ইল_কট_রন_ক_স'], keywords: ['সেমিকন্ডাক্টর', 'ইলেকট্রনিক্স', 'ডায়োড', 'ট্রানজিস্টর'] },
  { key: 'phy_2_11', subject: 'Physics', paper: '২য় পত্র', order: 21, name: 'জ্যোতির্বিজ্ঞান', ids: ['জ_য_ত_র_ব_জ_ঞ_ন'], keywords: ['জ্যোতির্বিজ্ঞান', 'কৃষ্ণবিবর'] },

  // ================= CHEMISTRY (1st Paper -> 2nd Paper) =================
  { key: 'che_1_01', subject: 'Chemistry', paper: '১ম পত্র', order: 1, name: 'ল্যাবরেটরির নিরাপদ ব্যবহার', ids: ['ল_য_বর_টর_র_ন_র_পদ_ব_যবহ_র'], keywords: ['ল্যাবরেটরি', 'নিরাপদ ব্যবহার'] },
  { key: 'che_1_02', subject: 'Chemistry', paper: '১ম পত্র', order: 2, name: 'গুণগত রসায়ন', ids: ['গ_ণগত_রস_যন'], keywords: ['গুণগত রসায়ন', 'কোয়ান্টাম', 'দ্রাব্যতা'] },
  { key: 'che_1_03', subject: 'Chemistry', paper: '১ম পত্র', order: 3, name: 'মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন', ids: ['ম_ল_র_পর_য_যব_ত_ত_ধর_ম_ও_র_স_যন_ক_বন_ধন'], keywords: ['পর্যায়বৃত্ত ধর্ম', 'রাসায়নিক বন্ধন', 'সংকরায়ন'] },
  { key: 'che_1_04', subject: 'Chemistry', paper: '১ম পত্র', order: 4, name: 'রাসায়নিক পরিবর্তন', ids: ['র_স_যন_ক_পর_বর_তন'], keywords: ['রাসায়নিক পরিবর্তন', 'সাম্যাবস্থা', 'Kp', 'pH'] },
  { key: 'che_2_01', subject: 'Chemistry', paper: '২য় পত্র', order: 11, name: 'পরিবেশ রসায়ন', ids: ['পর_ব_শ_রস_যন'], keywords: ['পরিবেশ রসায়ন', 'গ্যাস সূত্র', 'অম্ল-ক্ষার'] },
  { key: 'che_2_02', subject: 'Chemistry', paper: '২য় পত্র', order: 12, name: 'জৈব রসায়ন', ids: ['জ_ব_রস_যন'], keywords: ['জৈব রসায়ন', 'অ্যালকেন', 'বেনজিন', 'অ্যালকোহল'] },
  { key: 'che_2_03', subject: 'Chemistry', paper: '২য় পত্র', order: 13, name: 'পরিমাণগত রসায়ন', ids: ['পর_ম_ণগত_রস_যন'], keywords: ['পরিমাণগত রসায়ন', 'টাইট্রেশন', 'মোলারিটি'] },
  { key: 'che_2_04', subject: 'Chemistry', paper: '২য় পত্র', order: 14, name: 'তড়িৎ রসায়ন', ids: ['তড_ৎ_রস_যন'], keywords: ['তড়িৎ রসায়ন', 'ফ্যারাডে', 'তড়িৎদ্বার'] },
  { key: 'che_2_05', subject: 'Chemistry', paper: '২য় পত্র', order: 15, name: 'অর্থনৈতিক রসায়ন', ids: ['অর_থন_ত_ক_রস_যন'], keywords: ['অর্থনৈতিক রসায়ন', 'সিমেন্ট', 'কাচ'] },

  // ================= HIGHER MATH (1st Paper -> 2nd Paper) =================
  { key: 'math_1_01', subject: 'Higher Math', paper: '১ম পত্র', order: 1, name: 'ম্যাট্রিক্স ও নির্ণায়ক', ids: ['ম_য_ট_র_ক_স_ও_ন_র_ণ_য_ক', 'math_1st_01', 'math_2nd_10'], keywords: ['ম্যাট্রিক্স', 'নির্ণায়ক', 'ক্রেমার'] },
  { key: 'math_1_02', subject: 'Higher Math', paper: '১ম পত্র', order: 2, name: 'ভেক্টর', ids: ['math_1st_02'], keywords: ['ভেক্টর', 'ডট গুণন'] },
  { key: 'math_1_03', subject: 'Higher Math', paper: '১ম পত্র', order: 3, name: 'সরলরেখা', ids: ['সরলর_খ', 'math_1st_03', 'math_2nd_02'], keywords: ['সরলরেখা', 'ঢাল', 'লম্ব', 'সমান্তরাল'] },
  { key: 'math_1_04', subject: 'Higher Math', paper: '১ম পত্র', order: 4, name: 'বৃত্ত', ids: ['ব_ত_ত'], keywords: ['বৃত্ত', 'স্পর্শক'] },
  { key: 'math_1_05', subject: 'Higher Math', paper: '১ম পত্র', order: 5, name: 'বিন্যাস ও সমাবেশ', ids: ['ব_ন_য_স_ও_সম_ব_শ'], keywords: ['বিন্যাস', 'সমাবেশ'] },
  { key: 'math_1_06', subject: 'Higher Math', paper: '১ম পত্র', order: 6, name: 'ত্রিকোণমিতিক অনুপাত ও বৃত্তচাপ', ids: ['স_য_ক_ত_ক_ণ_র_ত_র_ক_ণম_ত_ক_অন_প_ত', 'math_1st_06'], keywords: ['ত্রিকোণমিতিক অনুপাত', 'সংযুক্ত কোণ', 'বৃত্তচাপ'] },
  { key: 'math_1_08', subject: 'Higher Math', paper: '১ম পত্র', order: 8, name: 'ফাংশন ও ফাংশনের লেখচিত্র', ids: ['ফ_শন_ও_ফ_শন_র_ল_খচ_ত_র'], keywords: ['ফাংশন', 'ডোমেন', 'রেঞ্জ'] },
  { key: 'math_1_09', subject: 'Higher Math', paper: '১ম পত্র', order: 9, name: 'অন্তরীকরণ', ids: ['অন_তর_করণ'], keywords: ['অন্তরীকরণ', 'লিমিট', 'গুরুমান'] },
  { key: 'math_1_10', subject: 'Higher Math', paper: '১ম পত্র', order: 10, name: 'যোগজীকরণ', ids: ['য_গজ_করণ'], keywords: ['যোগজীকরণ', 'ক্ষেত্রফল'] },
  { key: 'math_2_01', subject: 'Higher Math', paper: '২য় পত্র', order: 11, name: 'বাস্তব সংখ্যা ও অসমতা', ids: ['ব_স_তব_স_খ_য_ও_অসমত'], keywords: ['বাস্তব সংখ্যা', 'অসমতা'] },
  { key: 'math_2_02', subject: 'Higher Math', paper: '২য় পত্র', order: 12, name: 'যোগাশ্রয়ী প্রোগ্রাম', ids: ['য_গ_শ_রয_প_র_গ_র_ম'], keywords: ['যোগাশ্রয়ী প্রোগ্রাম'] },
  { key: 'math_2_03', subject: 'Higher Math', paper: '২য় পত্র', order: 13, name: 'জটিল সংখ্যা', ids: ['জট_ল_স_খ_য'], keywords: ['জটিল সংখ্যা', 'আর্গুমেন্ট'] },
  { key: 'math_2_04', subject: 'Higher Math', paper: '২য় পত্র', order: 14, name: 'বহুপদী ও বহুপদী সমীকরণ', ids: ['বহ_পদ_ও_বহ_পদ_সম_করণ', 'math_2nd_04'], keywords: ['বহুপদী', 'দ্বিঘাত'] },
  { key: 'math_2_05', subject: 'Higher Math', paper: '২য় পত্র', order: 15, name: 'দ্বিপদী বিস্তৃতি', ids: ['দ_ব_পদ_ব_স_ত_ত'], keywords: ['দ্বিপদী বিস্তৃতি'] },
  { key: 'math_2_06', subject: 'Higher Math', paper: '২য় পত্র', order: 16, name: 'কনিক্স', ids: ['কন_ক_স', 'math_2nd_06'], keywords: ['কনিক্স', 'পরাবৃত্ত', 'উপবৃত্ত', 'অধিবৃত্ত'] },
  { key: 'math_2_07', subject: 'Higher Math', paper: '২য় পত্র', order: 17, name: 'বিপরীত ত্রিকোণমিতিক ফাংশন ও সমীকরণ', ids: ['ব_পর_ত_ত_র_ক_ণম_ত_ক_ফ_শন_ও_সম_করণ'], keywords: ['বিপরীত ত্রিকোণমিতিক'] },
  { key: 'math_2_08', subject: 'Higher Math', paper: '২য় পত্র', order: 18, name: 'স্থিতিবিদ্যা', ids: ['স_থ_ত_ব_দ_য', 'math_2nd_08'], keywords: ['স্থিতিবিদ্যা', 'লব্ধি', 'লামির উপপাদ্য'] },
  { key: 'math_2_09', subject: 'Higher Math', paper: '২য় পত্র', order: 19, name: 'সমতলে বস্তুকণার গতি', ids: ['math_2nd_09'], keywords: ['প্রক্ষেপকের', 'সমতলে বস্তুকণার গতি'] },
  { key: 'math_2_10', subject: 'Higher Math', paper: '২য় পত্র', order: 20, name: 'বিস্তার পরিমাপ ও সম্ভাবনা', ids: ['ব_স_ত_র_পর_ম_প_ও_সম_ভ_বন'], keywords: ['সম্ভাবনা', 'বিস্তার পরিমাপ'] },

  // ================= BIOLOGY (Botany 1st -> Zoology 2nd, deduplicated) =================
  { key: 'bio_1_02', subject: 'Biology', paper: '১ম পত্র', order: 1, name: 'কোষ বিভাজন (মায়োসিস ও মাইটোসিস)', ids: ['bio_bot_05', 'bio_bot_02'], keywords: ['কোষ বিভাজন', 'মায়োসিস', 'প্রোফেজ'] },
  { key: 'bio_1_04', subject: 'Biology', paper: '১ম পত্র', order: 2, name: 'অণুজীব (ভাইরাস ও ব্যাকটেরিয়া)', ids: ['bio_bot_04', 'অণ_জ_ব'], keywords: ['অণুজীব', 'ভাইরাস', 'ব্যাকটেরিয়া'] },
  { key: 'bio_1_05', subject: 'Biology', paper: '১ম পত্র', order: 3, name: 'শৈবাল ও ছত্রাক', ids: ['শ_ব_ল_ও_ছত_র_ক'], keywords: ['শৈবাল', 'ছত্রাক'] },
  { key: 'bio_1_06', subject: 'Biology', paper: '১ম পত্র', order: 4, name: 'ব্রায়োফাইটা ও টেরিডোফাইটা', ids: ['bio_bot_06', 'ব_র_য_ফ_ইট_ও_ট_র_ড_ফ_ইট'], keywords: ['ব্রায়োফাইটা', 'রিকসিয়া', 'টেরিডোফাইটা'] },
  { key: 'bio_1_07', subject: 'Biology', paper: '১ম পত্র', order: 5, name: 'নগ্নবীজী ও আবৃতবীজী উদ্ভিদ', ids: ['bio_bot_07', 'bio_bot_10', 'bio_zoo_06'], keywords: ['নগ্নবীজী', 'সাইকাস', 'অমরাবিন্যাস', 'মালভেসি', 'পোয়াসি'] },
  { key: 'bio_1_08', subject: 'Biology', paper: '১ম পত্র', order: 6, name: 'টিস্যু ও টিস্যুতন্ত্র', ids: ['bio_bot_08'], keywords: ['ভাজক টিস্যু', 'টিস্যুতন্ত্র'] },
  { key: 'bio_1_09', subject: 'Biology', paper: '১ম পত্র', order: 7, name: 'উদ্ভিদ শারীরতত্ত্ব (প্রস্বেদন, সালোকসংশ্লেষণ, শ্বসন)', ids: ['bio_bot_09', 'bio_zoo_04', 'bio_zoo_01'], keywords: ['প্রস্বেদন', 'সালোকসংশ্লেষণ', 'শ্বসন', 'গ্লাইকোলাইসিস'] },
  { key: 'bio_1_11', subject: 'Biology', paper: '১ম পত্র', order: 8, name: 'জীবপ্রযুক্তি ও জেনেটিক কোড', ids: ['bio_bot_11', 'bio_bot_03', 'bio_bot_01'], keywords: ['টিস্যু কালচার', 'জেনেটিক কোড', 'জীবপ্রযুক্তি'] },
  { key: 'bio_1_12', subject: 'Biology', paper: '১ম পত্র', order: 9, name: 'জীবের পরিবেশ, বিস্তার ও সংরক্ষণ', ids: ['bio_bot_12'], keywords: ['বাস্তুতন্ত্র', 'শক্তির প্রবাহ'] },
  { key: 'bio_2_01', subject: 'Biology', paper: '২য় পত্র', order: 11, name: 'প্রাণীর বিভিন্নতা ও শ্রেণিবিন্যাস', ids: ['bio_zoo_07', 'bio_zoo_09'], keywords: ['নন-কর্ডাটা', 'শ্রেণিবিন্যাস'] },
  { key: 'bio_2_02', subject: 'Biology', paper: '২য় পত্র', order: 12, name: 'প্রাণীর পরিচিতি (হাইড্রা, ঘাসফড়িং, রুই)', ids: ['bio_zoo_02'], keywords: ['হাইড্রা', 'নেমাটোসিস্ট'] },
  { key: 'bio_2_04', subject: 'Biology', paper: '২য় পত্র', order: 13, name: 'রক্ত ও সঞ্চালন (হৃদপিণ্ড)', ids: ['bio_zoo_10'], keywords: ['হৃদপিণ্ড', 'কপাটিকা', 'রক্ত সঞ্চালন'] },
  { key: 'bio_2_05', subject: 'Biology', paper: '২য় পত্র', order: 14, name: 'শ্বসন ও শ্বাসক্রিয়া (গ্যাসীয় পরিবহন)', ids: ['bio_zoo_05'], keywords: ['গ্যাসীয় পরিবহন', 'ক্লোরাইড শিফট'] },
  { key: 'bio_2_08', subject: 'Biology', paper: '২য় পত্র', order: 15, name: 'সমন্বয় ও নিয়ন্ত্রণ (স্নায়ু ও হরমোন)', ids: ['bio_zoo_12', 'bio_zoo_03', 'bio_zoo_08'], keywords: ['করোটিক স্নায়ু', 'অন্তক্ষরা গ্রন্থি', 'হরমোন'] },
  { key: 'bio_2_11', subject: 'Biology', paper: '২য় পত্র', order: 16, name: 'জিনতত্ত্ব ও বিবর্তন (মেন্ডেলের সূত্র)', ids: ['bio_zoo_11'], keywords: ['মেন্ডেলের সূত্র', 'জিনতত্ত্ব'] },

  // ================= ENGLISH =================
  { key: 'eng_gram', subject: 'English', paper: 'কমন', order: 1, name: 'Grammar, Clauses, Voice & Modifiers', ids: ['unclassified', 'Dangling_Modifiers_Conditionals', 'Subjunctive_Inversion', 'Grammar_Synthesis_Voice_Clause', 'Grammar_Parallelism', 'Modifiers', 'Phrases_Clauses', 'DU_Kha_Grammar_Final', 'MAT_English_Core_Final'], keywords: ['grammar', 'voice', 'clause', 'modifier', 'subjunctive'] },
  { key: 'eng_prep', subject: 'English', paper: 'কমন', order: 2, name: 'Prepositions & Idioms', ids: ['Appropriate_Preposition', 'Appropriate_Prepositions', 'Idioms_Phrases'], keywords: ['preposition', 'idioms'] },
  { key: 'eng_vocab', subject: 'English', paper: 'কমন', order: 3, name: 'Vocabulary, Spelling & Synonyms', ids: ['Vocabulary_Synonyms', 'Spelling_Vocabulary', 'Medical_Spelling_Synonym_Trap'], keywords: ['vocabulary', 'synonym', 'spelling'] },
  { key: 'eng_lit', subject: 'English', paper: 'কমন', order: 4, name: 'Literature & Figurative Language', ids: ['Literature_Figurative_Language'], keywords: ['literature', 'figurative'] },

  // ================= GK =================
  { key: 'gk_bd', subject: 'GK', paper: 'কমন', order: 1, name: 'বাংলাদেশ বিষয়াবলি, সংবিধান ও মুক্তিযুদ্ধ', ids: ['unclassified', 'স_ব_ধ_ন_ও_শ_সনব_যবস_থ', 'ম_ক_ত_য_দ_ধ_ও_ইত_হ_স', 'Bangladesh_Constitution', 'Liberation_War_1971', 'Megaprojects_of_Bangladesh', 'ব_ল_দ_শ_পর_চ_ত'], keywords: ['সংবিধান', 'মুক্তিযুদ্ধ', 'বাংলাদেশ'] },
  { key: 'gk_intl', subject: 'GK', paper: 'কমন', order: 2, name: 'আন্তর্জাতিক বিষয়াবলি, অর্থনীতি ও সাধারণ জ্ঞান', ids: ['আন_তর_জ_ত_ক_স_স_থ_ও_ভ_-র_জন_ত', 'অর_থন_ত_ও_ভ_গ_ল_ক_তথ_য', 'স_ব_স_থ_য_ও_আন_তর_জ_ত_ক_দ_বস', 'DU_Kha_GK_Final', 'MAT_GK_Core_Final'], keywords: ['আন্তর্জাতিক', 'অর্থনীতি', 'দিবস'] },
];

export function buildCanonicalChapters(): CanonicalChapterGroup[] {
  const bySubjAndId = new Map<string, ChapterIndexEntry>();
  for (const c of BANK_INDEX.chapters) {
    bySubjAndId.set(`${c.subject}||${c.chapter_id.toLowerCase()}`, c);
  }

  const usedKeys = new Set<string>();
  const groups: CanonicalChapterGroup[] = [];

  for (const rule of CANONICAL_RULES) {
    const matchedEntries: ChapterIndexEntry[] = [];
    for (const id of rule.ids) {
      const k = `${rule.subject}||${id.toLowerCase()}`;
      const found = bySubjAndId.get(k);
      if (found) {
        matchedEntries.push(found);
        usedKeys.add(k);
      }
    }

    if (matchedEntries.length === 0) continue;

    const count = matchedEntries.reduce((acc, e) => acc + e.count, 0);
    const years_hit = Math.max(...matchedEntries.map((e) => e.years_hit));
    const papers_hit = matchedEntries.reduce((acc, e) => acc + e.papers_hit, 0);
    const predicted_pct = Number(
      Math.min(99, matchedEntries.reduce((acc, e) => acc + e.predicted_pct, 0)).toFixed(2)
    );
    const expected_mcq_du_ka = Number(
      matchedEntries.reduce((acc, e) => acc + e.expected_mcq_du_ka, 0).toFixed(2)
    );
    const expected_mcq_mat = Number(
      matchedEntries.reduce((acc, e) => acc + e.expected_mcq_mat, 0).toFixed(2)
    );

    groups.push({
      key: rule.key,
      subject: rule.subject,
      paper: rule.paper,
      order: rule.order,
      chapter_name: rule.name,
      primary_chapter_id: matchedEntries[0].chapter_id,
      merged_chapter_ids: matchedEntries.map((e) => e.chapter_id),
      match_keywords: rule.keywords,
      count,
      years_hit,
      papers_hit,
      predicted_pct,
      expected_mcq_du_ka,
      expected_mcq_mat,
    });
  }

  // Include any remaining subjects/chapters (Bangla, ICT, etc.) cleanly without any undefined/UNCLASSIFIED
  let extraOrder = 100;
  for (const c of BANK_INDEX.chapters) {
    const k = `${c.subject}||${c.chapter_id.toLowerCase()}`;
    if (usedKeys.has(k)) continue;
    const cleanName =
      !c.chapter_name || /undefined|unclassified/i.test(c.chapter_name)
        ? `${c.subject} সাধারণ অধ্যায়`
        : c.chapter_name;
    groups.push({
      key: `${c.subject}_${c.chapter_id}`,
      subject: c.subject,
      paper: 'কমন',
      order: extraOrder++,
      chapter_name: cleanName,
      primary_chapter_id: c.chapter_id,
      merged_chapter_ids: [c.chapter_id],
      match_keywords: [cleanName],
      count: c.count,
      years_hit: c.years_hit,
      papers_hit: c.papers_hit,
      predicted_pct: c.predicted_pct,
      expected_mcq_du_ka: c.expected_mcq_du_ka,
      expected_mcq_mat: c.expected_mcq_mat,
    });
  }

  const subjectRank: Record<string, number> = {
    Physics: 1,
    Chemistry: 2,
    'Higher Math': 3,
    Biology: 4,
    English: 5,
    GK: 6,
    Bangla: 7,
    ICT: 8,
  };

  return groups.sort(
    (a, b) =>
      (subjectRank[a.subject] ?? 99) - (subjectRank[b.subject] ?? 99) ||
      a.order - b.order
  );
}
