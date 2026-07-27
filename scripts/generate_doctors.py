# -*- coding: utf-8 -*-
"""
Generate 14 individual doctor profile pages from _template.html
Each page has placeholder replaced with doctor-specific data.
"""
import os

TEMPLATE = r"D:\minimax\New folder\website\doctors\_template.html"
OUT_DIR  = r"D:\minimax\New folder\website\doctors"

# All 14 doctors' full data
DOCTORS = [
    {
        "num": "01",
        "name": "ডা. আবু বকর সিদ্দিক",
        "deg_short": "MBBS, BCS, MD (Internal Medicine)",
        "deg_full": "MBBS, BCS, MD (Internal Medicine)",
        "desig": "সহকারী অধ্যাপক, মেডিসিন বিভাগ",
        "desig_short": "সহকারী অধ্যাপক",
        "spec": "মেডিসিন, হৃদরোগ, বক্ষব্যাধি",
        "dept": "মেডিসিন",
        "dept_class": "med",
        "initial": "আ",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুর",
        "years": "১৫",
        "patients": "২০০০০+",
        "rating": "৪.৯",
        "training": "মেডিসিন ও বক্ষব্যাধিতে উচ্চতর প্রশিক্ষণ; হৃদরোগ ব্যবস্থাপনায় বিশেষ দক্ষতা",
        "specialty_list": (
            "<li>মেডিসিন বিশেষজ্ঞ পরামর্শ ও চিকিৎসা</li>"
            "<li>হৃদরোগের চিকিৎসা ও পরামর্শ</li>"
            "<li>বক্ষব্যাধি (যক্ষ্মা, নিউমোনিয়া, হাঁপানি)</li>"
            "<li>উচ্চ রক্তচাপ ও ডায়াবেটিস ব্যবস্থাপনা</li>"
            "<li>জ্বর ও সংক্রামক রোগের চিকিৎসা</li>"
            "<li>কিডনি ও লিভার রোগের পরামর্শ</li>"
        ),
        "disease_list": (
            "<li>ডায়াবেটিস (টাইপ ১ ও ২)</li>"
            "<li>উচ্চ রক্তচাপ ও হৃদরোগ</li>"
            "<li>হাঁপানি ও ব্রংকাইটিস</li>"
            "<li>যক্ষ্মা ও নিউমোনিয়া</li>"
            "<li>কিডনি ও লিভারের সমস্যা</li>"
            "<li>থাইরয়েডের সমস্যা</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">বিকাল ৩টা - সন্ধ্যা ৬টা</span></div>\n"
            "<div class=\"day\"><span>শুক্রবার</span><span class=\"time\">বন্ধ</span></div>"
        ),
    },
    {
        "num": "02",
        "name": "ডা. মোঃ রিয়াদ হোসেন বাপ্পি",
        "deg_short": "MBBS, BCS, CCD, FCPS (মেডিসিন)",
        "deg_full": "MBBS (ঢাকা), BCS (স্বাস্থ্য), CCD (বারডেম), FCPS (মেডিসিন), Trained in Rheumatology",
        "desig": "সহকারী রেজিস্টার, মেডিসিন বিভাগ",
        "desig_short": "সহকারী রেজিস্টার",
        "spec": "মেডিসিন, রিউমাটোলজি, ডায়াবেটিস",
        "dept": "মেডিসিন",
        "dept_class": "med",
        "initial": "রি",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুর",
        "years": "৮",
        "patients": "১২০০০+",
        "rating": "৪.৮",
        "training": "রিউমাটোলজি (বাতরোগ) বিশেষ প্রশিক্ষিত; বারডেম সনদপ্রাপ্ত ডায়াবেটিস বিশেষজ্ঞ",
        "specialty_list": (
            "<li>মেডিসিন বিশেষজ্ঞ পরামর্শ</li>"
            "<li>বাতরোগ ও রিউমাটোলজি চিকিৎসা</li>"
            "<li>ডায়াবেটিস ব্যবস্থাপনা (বারডেম সনদপ্রাপ্ত)</li>"
            "<li>উচ্চ রক্তচাপ ও থাইরয়েডের সমস্যা</li>"
            "<li>জয়েন্ট পেইন ও আর্থ্রাইটিস</li>"
            "<li>রক্তস্বল্পতা ও পুষ্টিজনিত সমস্যা</li>"
        ),
        "disease_list": (
            "<li>রিউমাটয়েড আর্থ্রাইটিস</li>"
            "<li>অস্টিওআর্থ্রাইটিস</li>"
            "<li>টাইপ ২ ডায়াবেটিস</li>"
            "<li>উচ্চ রক্তচাপ</li>"
            "<li>থাইরয়েডের সমস্যা (হাইপো/হাইপার)</li>"
            "<li>লুপাস ও অটোইমিউন রোগ</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">সকাল ১০টা - দুপুর ১টা</span></div>\n"
            "<div class=\"day\"><span>শুক্রবার</span><span class=\"time\">বন্ধ</span></div>"
        ),
    },
    {
        "num": "03",
        "name": "ডা. শ্রাবন্তী এম ইসলাম",
        "deg_short": "MBBS, BCS, MCPS, FCPS, MRCOG (শেষ বর্ষ)",
        "deg_full": "MBBS, BCS (স্বাস্থ্য), MCPS (গাইনি এন্ড অবস), FCPS (গাইনি এন্ড অবস), MRCOG (শেষ বর্ষ)",
        "desig": "কনসালটেন্ট, গাইনি ও প্রসূতি",
        "desig_short": "কনসালটেন্ট",
        "spec": "গাইনি, প্রসূতি, বন্ধ্যাত্ব",
        "dept": "গাইনি ও প্রসূতি",
        "dept_class": "gynae",
        "initial": "শ্রা",
        "affil": "সদর হাসপাতাল, ফরিদপুর",
        "years": "১০",
        "patients": "১৫০০০+",
        "rating": "৪.৯",
        "training": "বন্ধ্যাত্ব চিকিৎসায় বিশেষ প্রশিক্ষিত; MRCOG (লন্ডন) পরীক্ষার্থী",
        "specialty_list": (
            "<li>গাইনি ও প্রসূতি পরামর্শ</li>"
            "<li>নরমাল ও সিজারিয়ান ডেলিভারি</li>"
            "<li>বন্ধ্যাত্ব (ইনফার্টিলিটি) চিকিৎসা</li>"
            "<li>মাসিক সমস্যা ও পলিসিস্টিক ওভারি</li>"
            "<li>জরায়ু টিউমার ও ওভারিয়ান সিস্ট</li>"
            "<li>প্রি-পোস্ট মেনোপজ পরামর্শ</li>"
        ),
        "disease_list": (
            "<li>বন্ধ্যাত্ব (পুরুষ ও নারী)</li>"
            "<li>পলিসিস্টিক ওভারি সিন্ড্রোম (PCOS)</li>"
            "<li>এন্ডোমেট্রিওসিস</li>"
            "<li>জরায়ু ফাইব্রয়েড</li>"
            "<li>অনিয়মিত মাসিক</li>"
            "<li>প্রসবপূর্ব ও প্রসবোত্তর যত্ন</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">সকাল ৯টা - দুপুর ১টা</span></div>\n"
            "<div class=\"day\"><span>বৃহস্পতিবার</span><span class=\"time\">বিকাল ৪টা - সন্ধ্যা ৭টা</span></div>"
        ),
    },
    {
        "num": "04",
        "name": "ডা. মো. মঈন উদ্দিন",
        "deg_short": "MBBS, D-Ortho, FCPS (USA)",
        "deg_full": "MBBS (মিটফোর্ড), D-Ortho (BSMMU), FCPS (আমেরিকা)",
        "desig": "সহযোগী অধ্যাপক ও বিভাগীয় প্রধান, অর্থোপেডিক বিভাগ",
        "desig_short": "সহযোগী অধ্যাপক ও বিভাগীয় প্রধান",
        "spec": "অর্থোপেডিক্স, ট্রমা সার্জারি, বাতব্যথা",
        "dept": "অর্থোপেডিক্স",
        "dept_class": "ortho",
        "initial": "মই",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুর",
        "years": "১৮",
        "patients": "২৫০০০+",
        "rating": "৫.০",
        "training": "BSMMU-তে অর্থোপেডিক সার্জারিতে উচ্চতর প্রশিক্ষণ; আমেরিকা থেকে FCPS সনদপ্রাপ্ত",
        "specialty_list": (
            "<li>হাড় ও জয়েন্ট সার্জারি</li>"
            "<li>ফ্র্যাকচার (হাড় ভাঙা) চিকিৎসা ও অপারেশন</li>"
            "<li>ট্রমা ও দুর্ঘটনা জনিত ক্ষত চিকিৎসা</li>"
            "<li>বাতব্যথা ও আর্থ্রাইটিস</li>"
            "<li>মেরুদণ্ডের সমস্যা</li>"
            "<li>স্পোর্টস ইনজুরি</li>"
        ),
        "disease_list": (
            "<li>হাড় ভাঙা (ফ্র্যাকচার)</li>"
            "<li>ডিসলোকেশন (জয়েন্ট সরে যাওয়া)</li>"
            "<li>অস্টিওআর্থ্রাইটিস</li>"
            "<li>রিউমাটয়েড আর্থ্রাইটিস</li>"
            "<li>মেরুদণ্ডের ব্যথা (স্লিপড ডিস্ক)</li>"
            "<li>টেনিস এলবো ও কাঁধের ব্যথা</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বুধবার</span><span class=\"time\">সকাল ১০টা - দুপুর ২টা</span></div>\n"
            "<div class=\"day\"><span>বৃহস্পতিবার</span><span class=\"time\">বিকাল ৫টা - রাত ৮টা</span></div>\n"
            "<div class=\"day\"><span>শুক্রবার</span><span class=\"time\">বন্ধ</span></div>"
        ),
    },
    {
        "num": "05",
        "name": "ডা. শশাঙ্ক নাগ (সনেট)",
        "deg_short": "MBBS, CCD, DMU, PGT",
        "deg_full": "MBBS (DU), CCD (বারডেম), DMU (DU), PGT",
        "desig": "মেডিসিন, ডায়াবেটিস ও রোগ বিশেষজ্ঞ",
        "desig_short": "মেডিসিন ও ডায়াবেটিস বিশেষজ্ঞ",
        "spec": "মেডিসিন, ডায়াবেটিস, নিউরো মেডিসিন",
        "dept": "মেডিসিন",
        "dept_class": "med",
        "initial": "শ",
        "affil": "হার্ট ফাউন্ডেশন, ফরিদপুর",
        "years": "১২",
        "patients": "১৮০০০+",
        "rating": "৪.৮",
        "training": "বারডেম সনদপ্রাপ্ত ডায়াবেটিস বিশেষজ্ঞ; ঢাকা বিশ্ববিদ্যালয়ের ডায়াবেটিক মেডিসিনে প্রশিক্ষিত",
        "specialty_list": (
            "<li>ডায়াবেটিস রোগ নির্ণয় ও ব্যবস্থাপনা</li>"
            "<li>মেডিসিন বিশেষজ্ঞ পরামর্শ</li>"
            "<li>নিউরো মেডিসিন (মাথা ব্যথা, মাইগ্রেন, স্ট্রোক)</li>"
            "<li>বক্ষব্যাধি ও শ্বাসকষ্ট</li>"
            "<li>পরিপাকতন্ত্রের সমস্যা</li>"
            "<li>হৃদরোগের প্রাথমিক পরামর্শ</li>"
        ),
        "disease_list": (
            "<li>ডায়াবেটিস (টাইপ ১ ও ২, গর্ভকালীন)</li>"
            "<li>উচ্চ রক্তচাপ</li>"
            "<li>মাইগ্রেন ও মাথা ব্যথা</li>"
            "<li>স্ট্রোক ও প্যারালাইসিস</li>"
            "<li>হাঁপানি ও শ্বাসকষ্ট</li>"
            "<li>গ্যাস্ট্রিক ও আলসার</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">বিকাল ৪টা - রাত ৯টা</span></div>\n"
            "<div class=\"day\"><span>শুক্রবার</span><span class=\"time\">সকাল ১০টা - দুপুর ১টা</span></div>"
        ),
    },
    {
        "num": "06",
        "name": "ডা. মোহাম্মদ রফিকুল ইসলাম",
        "deg_short": "MBBS, MPH, CCD, PHD (USA)",
        "deg_full": "MBBS, MPH (রোগ তত্ত্ব), CCD (বারডেম), PHD (USA)",
        "desig": "সহযোগী অধ্যাপক ও বিভাগীয় প্রধান, কমিউনিটি মেডিসিন",
        "desig_short": "সহযোগী অধ্যাপক ও বিভাগীয় প্রধান",
        "spec": "কমিউনিটি মেডিসিন, ডায়াবেটিস, এপিডেমিওলজি",
        "dept": "মেডিসিন",
        "dept_class": "med",
        "initial": "রফ",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুর",
        "years": "২০",
        "patients": "৩০০০০+",
        "rating": "৪.৯",
        "training": "আমেরিকা থেকে PHD ডিগ্রিধারী; বারডেম সনদপ্রাপ্ত ডায়াবেটিস বিশেষজ্ঞ; রোগ তত্ত্ব বিশেষজ্ঞ",
        "specialty_list": (
            "<li>ডায়াবেটিস নিয়ন্ত্রণ ও পরামর্শ</li>"
            "<li>কমিউনিটি মেডিসিন ও জনস্বাস্থ্য</li>"
            "<li>রোগ প্রতিরোধ ও সচেতনতা</li>"
            "<li>টিকা ও ইমিউনাইজেশন পরামর্শ</li>"
            "<li>উচ্চ রক্তচাপ ও কোলেস্টেরল ব্যবস্থাপনা</li>"
            "<li>স্বাস্থ্য সচেতনতা কার্যক্রম</li>"
        ),
        "disease_list": (
            "<li>ডায়াবেটিস</li>"
            "<li>উচ্চ রক্তচাপ</li>"
            "<li>স্থূলতা</li>"
            "<li>খাদ্যজনিত রোগ</li>"
            "<li>সংক্রামক রোগ প্রতিরোধ</li>"
            "<li>ডিসলিপিডেমিয়া</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">সকাল ১১টা - দুপুর ২টা</span></div>\n"
            "<div class=\"day\"><span>রবিবার ও বুধবার</span><span class=\"time\">বিকাল ৫টা - সন্ধ্যা ৭টা</span></div>"
        ),
    },
    {
        "num": "07",
        "name": "ডা. উৎপল নাগ",
        "deg_short": "MBBS, BCS, PGT, FCPS, FRSH",
        "deg_full": "MBBS, BCS (স্বাস্থ্য), PGT (কলোরেক্টাল সার্জারি), FCPS (সার্জারি), FRSH (লন্ডন)",
        "desig": "আর এস সার্জন, জেনারেল ও ল্যাপারোস্কোপিক সার্জারি",
        "desig_short": "আর এস সার্জন",
        "spec": "জেনারেল সার্জারি, ল্যাপারোস্কোপিক, কলোরেক্টাল",
        "dept": "সার্জারি",
        "dept_class": "surg",
        "initial": "উৎ",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুর",
        "years": "১৪",
        "patients": "২২০০০+",
        "rating": "৪.৯",
        "training": "কলোরেক্টাল সার্জারিতে বিশেষ প্রশিক্ষিত; লন্ডন থেকে FRSH সনদপ্রাপ্ত; ল্যাপারোস্কোপিক সার্জারিতে দক্ষ",
        "specialty_list": (
            "<li>জেনারেল সার্জারি (সব ধরনের অপারেশন)</li>"
            "<li>ল্যাপারোস্কোপিক (কম ছিদ্রের) সার্জারি</li>"
            "<li>কলোরেক্টাল সার্জারি (মলদ্বার ও পায়ুপথ)</li>"
            "<li>অ্যাপেন্ডিক্স, হার্নিয়া, গলব্লাডার অপারেশন</li>"
            "<li>পাইলস, ফিস্টুলা, ফিশার চিকিৎসা</li>"
            "<li>থাইরয়েড ও সফট টিস্যু টিউমার</li>"
        ),
        "disease_list": (
            "<li>অ্যাপেন্ডিসাইটিস</li>"
            "<li>হার্নিয়া</li>"
            "<li>পিত্তথলির পাথর (Gall Stone)</li>"
            "<li>পাইলস (অর্শ)</li>"
            "<li>ফিস্টুলা ও ফিশার</li>"
            "<li>কলোরেক্টাল ক্যান্সার</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বুধবার</span><span class=\"time\">বিকাল ৪টা - সন্ধ্যা ৭টা</span></div>\n"
            "<div class=\"day\"><span>বৃহস্পতিবার</span><span class=\"time\">সকাল ১০টা - দুপুর ১টা</span></div>\n"
            "<div class=\"day\"><span>শুক্রবার</span><span class=\"time\">বন্ধ</span></div>"
        ),
    },
    {
        "num": "08",
        "name": "ডা. আবু সালে আহমেদ সৌরভ",
        "deg_short": "MBBS, BCS, FCPS, MRCS",
        "deg_full": "MBBS, BCS (স্বাস্থ্য), FCPS (সার্জারি), MRCS (সার্জারি)",
        "desig": "জেনারেল ও ল্যাপারোস্কোপিক সার্জন",
        "desig_short": "জেনারেল ও ল্যাপারোস্কোপিক সার্জন",
        "spec": "জেনারেল সার্জারি, ল্যাপারোস্কোপিক, ইউরোলজি",
        "dept": "সার্জারি",
        "dept_class": "surg",
        "initial": "সৌ",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুর",
        "years": "১০",
        "patients": "১৬০০০+",
        "rating": "৪.৮",
        "training": "পায়ুপথ সার্জারি ও ইউরোলজিতে বিশেষ প্রশিক্ষিত; MRCS (আন্তর্জাতিক সার্জারি সনদ)",
        "specialty_list": (
            "<li>জেনারেল সার্জারি</li>"
            "<li>ল্যাপারোস্কোপিক (কী-হোল) সার্জারি</li>"
            "<li>পায়ুপথ সার্জারি (পাইলস, ফিস্টুলা, ফিশার)</li>"
            "<li>ইউরোলজিক্যাল সার্জারি</li>"
            "<li>হার্নিয়া ও অ্যাপেন্ডিক্স অপারেশন</li>"
            "<li>গলব্লাডার ও পিত্তথলির অপারেশন</li>"
        ),
        "disease_list": (
            "<li>পাইলস (অর্শ)</li>"
            "<li>ফিস্টুলা-ইন-অ্যানো</li>"
            "<li>অ্যানাল ফিশার</li>"
            "<li>হার্নিয়া</li>"
            "<li>অ্যাপেন্ডিসাইটিস</li>"
            "<li>পিত্তথলির পাথর</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">সকাল ১০টা - দুপুর ১টা</span></div>\n"
            "<div class=\"day\"><span>সোমবার ও বুধবার</span><span class=\"time\">বিকাল ৫টা - রাত ৮টা</span></div>"
        ),
    },
    {
        "num": "09",
        "name": "ডা. নাহিদ বাদশা",
        "deg_short": "MBBS, BCS, MS (অর্থোপেডিক)",
        "deg_full": "MBBS (DU), BCS (স্বাস্স্থ্য), MS (অর্থোপেডিক)",
        "desig": "আবাসিক সার্জন (D-অর্থোপেডিক)",
        "desig_short": "আবাসিক সার্জন",
        "spec": "অর্থোপেডিক্স, ট্রমা, বাতব্যথা",
        "dept": "অর্থোপেডিক্স",
        "dept_class": "ortho",
        "initial": "না",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুর",
        "years": "৮",
        "patients": "১২০০০+",
        "rating": "৪.৭",
        "training": "অর্থোপেডিক সার্জারিতে MS ডিগ্রিধারী; ট্রমা ম্যানেজমেন্টে বিশেষ দক্ষ",
        "specialty_list": (
            "<li>হাড় ও জয়েন্টের চিকিৎসা</li>"
            "<li>ফ্র্যাকচার (হাড় ভাঙা) চিকিৎসা</li>"
            "<li>ট্রমা ও অ্যাক্সিডেন্ট জনিত চিকিৎসা</li>"
            "<li>বাতব্যাথা ও আর্থ্রাইটিস</li>"
            "<li>স্পোর্টস ইনজুরি</li>"
            "<li>প্লাস্টার ও ব্যান্ডেজিং</li>"
        ),
        "disease_list": (
            "<li>হাড় ভাঙা (ফ্র্যাকচার)</li>"
            "<li>জয়েন্ট ডিসলোকেশন</li>"
            "<li>অস্টিওআর্থ্রাইটিস</li>"
            "<li>টেনিস এলবো</li>"
            "<li>কাঁধের ব্যথা (ফ্রোজেন শোল্ডার)</li>"
            "<li>মচকে যাওয়া (স্প্রেইন)</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">বিকাল ৩টা - সন্ধ্যা ৬টা</span></div>\n"
            "<div class=\"day\"><span>শুক্রবার</span><span class=\"time\">বন্ধ</span></div>"
        ),
    },
    {
        "num": "10",
        "name": "ডা. হরিচাঁদ শীল",
        "deg_short": "MBBS, BMC",
        "deg_full": "MBBS, BMC",
        "desig": "অধ্যক্ষ, জেনারেল প্র্যাকটিশনার",
        "desig_short": "অধ্যক্ষ ও জেনারেল প্র্যাকটিশনার",
        "spec": "জেনারেল মেডিসিন, সার্জারি, গাইনি, শিশু, চর্ম",
        "dept": "জেনারেল প্র্যাকটিশনার",
        "dept_class": "gp",
        "initial": "হ",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ, ফরিদপুর",
        "years": "২৫+",
        "patients": "৫০০০০+",
        "rating": "৪.৯",
        "training": "দীর্ঘ ২৫+ বছরের ক্লিনিক্যাল অভিজ্ঞতা; BMC থেকে MBBS; বহুমুখী জেনারেল প্র্যাকটিস",
        "specialty_list": (
            "<li>জেনারেল মেডিসিন (সব ধরনের রোগ)</li>"
            "<li>মাইনর সার্জারি ও ক্ষত ড্রেসিং</li>"
            "<li>স্ত্রী-রোগ ও প্রসূতি পরামর্শ</li>"
            "<li>শিশু রোগ ও টিকা</li>"
            "<li>চর্ম ও যৌন রোগ</li>"
            "<li>বক্ষব্যাধি ও হাঁপানি</li>"
        ),
        "disease_list": (
            "<li>সাধারণ জ্বর ও ঠান্ডা</li>"
            "<li>পেটের সমস্যা ও ডায়রিয়া</li>"
            "<li>উচ্চ রক্তচাপ ও ডায়াবেটিস</li>"
            "<li>এলার্জি ও চুলকানি</li>"
            "<li>শিশুর সাধারণ রোগ</li>"
            "<li>ক্ষত ও ফোড়া</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">সকাল ৯টা - দুপুর ২টা</span></div>\n"
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">বিকাল ৪টা - রাত ৮টা</span></div>"
        ),
    },
    {
        "num": "11",
        "name": "ডা. সৈয়দ ইমতিয়াজ উদ্দিন",
        "deg_short": "MBBS, BCS, DLO",
        "deg_full": "MBBS, BCS (স্বাস্থ্য), DLO (SMMU)",
        "desig": "গলা রোগ বিশেষজ্ঞ ও হেড-নেক সার্জন",
        "desig_short": "ENT বিশেষজ্ঞ ও সার্জন",
        "spec": "ENT, গলা রোগ, হেড-নেক সার্জারি",
        "dept": "ইএনটি",
        "dept_class": "ent",
        "initial": "সৈ",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ, ফরিদপুর",
        "years": "১১",
        "patients": "১৮০০০+",
        "rating": "৪.৯",
        "training": "SMMU (শহীদ সোহরাওয়ার্দী মেডিকেল কলেজ) থেকে DLO সনদ; ১১ বছরের বিশেষজ্ঞ অভিজ্ঞতা",
        "specialty_list": (
            "<li>নাক, কান, গলার সব ধরনের চিকিৎসা</li>"
            "<li>টনসিল ও অ্যাডেনয়েড অপারেশন</li>"
            "<li>সাইনাস ইনফেকশন ও সাইনাস সার্জারি</li>"
            "<li>কানের পর্দা ছিদ্র অপারেশন</li>"
            "<li>হেড-নেক টিউমার সার্জারি</li>"
            "<li>নাকের পলিপ ও ডেভিয়েশন</li>"
        ),
        "disease_list": (
            "<li>টনসিলাইটিস</li>"
            "<li>সাইনাসাইটিস</li>"
            "<li>কানে পানি জমা ও কানের পর্দা ফুটো</li>"
            "<li>নাকের পলিপ</li>"
            "<li>গলাব্যথা ও ভয়েস পরিবর্তন</li>"
            "<li>হেড-নেকের টিউমার</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">বিকাল ৪টা - রাত ৯টা</span></div>\n"
            "<div class=\"day\"><span>শুক্রবার</span><span class=\"time\">সকাল ১০টা - দুপুর ১টা</span></div>"
        ),
    },
    {
        "num": "12",
        "name": "ডা. পাপড়ী সরকার",
        "deg_short": "MBBS, PGT",
        "deg_full": "MBBS (DMC), PGT (গাইনী এন্ড অবস)",
        "desig": "গাইনি ও স্ত্রীরোগ বিশেষজ্ঞ",
        "desig_short": "গাইনি বিশেষজ্ঞ",
        "spec": "গাইনি, প্রসূতি, স্ত্রীরোগ",
        "dept": "গাইনি ও প্রসূতি",
        "dept_class": "gynae",
        "initial": "পা",
        "affil": "প্রাক্তন ট্রেইনার RH Step, বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ ও হাসপাতাল, ফরিদপুর",
        "years": "১৪",
        "patients": "২০০০০+",
        "rating": "৪.৯",
        "training": "DMC থেকে MBBS; গাইনি ও অবসে PGT; RH Step (Reproductive Health) প্রশিক্ষক",
        "specialty_list": (
            "<li>গাইনি ও স্ত্রীরোগ চিকিৎসা</li>"
            "<li>নরমাল ও সিজারিয়ান ডেলিভারি</li>"
            "<li>মাসিক সমস্যা ও হরমোনের সমস্যা</li>"
            "<li>প্রজনন স্বাস্থ্য পরামর্শ</li>"
            "<li>জরায়ু ও ওভারির সমস্যা</li>"
            "<li>মেনোপজ পরবর্তী যত্ন</li>"
        ),
        "disease_list": (
            "<li>অনিয়মিত মাসিক</li>"
            "<li>পলিসিস্টিক ওভারি (PCOS)</li>"
            "<li>যোনি সংক্রমণ (White Discharge)</li>"
            "<li>জরায়ু ফাইব্রয়েড</li>"
            "<li>প্রসবপূর্ব ও প্রসবোত্তর যত্ন</li>"
            "<li>বন্ধ্যাত্ব</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">সকাল ১০টা - দুপুর ১টা</span></div>\n"
            "<div class=\"day\"><span>রবিবার ও মঙ্গলবার</span><span class=\"time\">বিকাল ৫টা - সন্ধ্যা ৮টা</span></div>"
        ),
    },
    {
        "num": "13",
        "name": "ডা. এস এম নূর ই আলম (বিদ্যুৎ)",
        "deg_short": "MBBS, BCS, PGT (চর্ম ও যৌন)",
        "deg_full": "MBBS (ঢাকা), BCS (স্বাস্থ্য), PGT (চর্ম ও যৌন)",
        "desig": "চর্ম, যৌন, সেক্স ও এলার্জি রোগে অভিজ্ঞ",
        "desig_short": "চর্ম ও যৌন বিশেষজ্ঞ",
        "spec": "চর্মরোগ, যৌন রোগ, এলার্জি",
        "dept": "চর্ম ও যৌন",
        "dept_class": "derma",
        "initial": "এস",
        "affil": "বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুর",
        "years": "১০",
        "patients": "১৪০০০+",
        "rating": "৪.৮",
        "training": "চর্ম ও যৌন রোগে PGT প্রশিক্ষিত; এলার্জি ও সেক্সুয়াল হেলথে বিশেষজ্ঞ",
        "specialty_list": (
            "<li>চর্মরোগ (এক্সিমা, সোরিয়াসিস, দাউদ)</li>"
            "<li>যৌন রোগ ও সেক্সুয়াল হেলথ</li>"
            "<li>এলার্জি (ত্বক, শ্বাসকষ্ট, খাদ্য)</li>"
            "<li>ব্রণ ও ত্বকের সমস্যা</li>"
            "<li>চুল পড়া ও নখের সমস্যা</li>"
            "<li>ছত্রাক সংক্রমণ</li>"
        ),
        "disease_list": (
            "<li>এক্সিমা ও ডার্মাটাইটিস</li>"
            "<li>সোরিয়াসিস</li>"
            "<li>ব্রণ (Acne)</li>"
            "<li>দাউদ (Ringworm)</li>"
            "<li>এলার্জি ও আমবাত</li>"
            "<li>যৌনবাহিত রোগ (STI)</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">বিকাল ৫টা - রাত ৯টা</span></div>\n"
            "<div class=\"day\"><span>শুক্রবার</span><span class=\"time\">সকাল ১১টা - দুপুর ২টা</span></div>"
        ),
    },
    {
        "num": "14",
        "name": "ডা. শংকর কুমার দে",
        "deg_short": "MBBS, DNM",
        "deg_full": "MBBS (DMC), DNM",
        "desig": "আল্ট্রাসনোগ্রাফি বিশেষজ্ঞ",
        "desig_short": "আল্ট্রাসনোগ্রাফি বিশেষজ্ঞ",
        "spec": "আল্ট্রাসনোগ্রাফি, ডায়াগনস্টিক ইমেজিং",
        "dept": "আল্ট্রাসনোগ্রাফি",
        "dept_class": "sono",
        "initial": "শং",
        "affil": "প্রাক্তন পরিচালক, পরমাণু শক্তি কেন্দ্র, ফরিদপুর",
        "years": "৩০+",
        "patients": "৪০০০০+",
        "rating": "৫.০",
        "training": "DMC থেকে MBBS; DNM সনদ; পরমাণু শক্তি কেন্দ্রের প্রাক্তন পরিচালক; ৩০+ বছরের ডায়াগনস্টিক অভিজ্ঞতা",
        "specialty_list": (
            "<li>সম্পূর্ণ আল্ট্রাসনোগ্রাফি (USG)</li>"
            "<li>পেট ও কিডনির আল্ট্রাসনো</li>"
            "<li>গর্ভাবস্থায় আল্ট্রাসনো</li>"
            "<li>থাইরয়েড ও ঘাড়ের আল্ট্রাসনো</li>"
            "<li>হার্ট ও বক্ষের ইকো</li>"
            "<li>ডায়াগনস্টিক ইমেজিং পরামর্শ</li>"
        ),
        "disease_list": (
            "<li>পেটের সব ধরনের রোগ নির্ণয়</li>"
            "<li>কিডনি ও লিভারের সমস্যা</li>"
            "<li>গর্ভাবস্থার মনিটরিং</li>"
            "<li>থাইরয়েডের সমস্যা</li>"
            "<li>পিত্তথলির পাথর</li>"
            "<li>ডায়াগনস্টিক ইমেজিং</li>"
        ),
        "schedule": (
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">সকাল ৯টা - দুপুর ২টা</span></div>\n"
            "<div class=\"day\"><span>শনিবার - বৃহস্পতিবার</span><span class=\"time\">বিকাল ৩টা - সন্ধ্যা ৬টা</span></div>"
        ),
    },
]

# Department color CSS for other-doctor avatars
DEPT_COLOR = {
    "med": "linear-gradient(135deg,#0066a4,#004a7a)",
    "surg": "linear-gradient(135deg,#34495e,#1a2530)",
    "gynae": "linear-gradient(135deg,#c2185b,#880e4f)",
    "ortho": "linear-gradient(135deg,#e67e22,#a04000)",
    "pediatric": "linear-gradient(135deg,#8e44ad,#5b2c6f)",
    "ent": "linear-gradient(135deg,#16a085,#0e6655)",
    "derma": "linear-gradient(135deg,#d35400,#a04000)",
    "cardio": "linear-gradient(135deg,#e74c3c,#922b21)",
    "neuro": "linear-gradient(135deg,#2c3e50,#1a252f)",
    "gp": "linear-gradient(135deg,#00a86b,#008755)",
    "sono": "linear-gradient(135deg,#2980b9,#1a5276)",
}

def make_other_doctors_html(self_num):
    """Generate 5 'other doctor' cards (excluding self)."""
    others = [d for d in DOCTORS if d["num"] != self_num][:5]
    html_parts = []
    for d in others:
        color = DEPT_COLOR.get(d["dept_class"], DEPT_COLOR["med"])
        html_parts.append(
            f'<a href="{d["num"]}.html" class="other-doc-card">\n'
            f'  <div class="other-doc-avatar" style="background:{color}">{d["initial"]}</div>\n'
            f'  <h4>{d["name"]}</h4>\n'
            f'  <p>{d["dept"]}</p>\n'
            f'</a>'
        )
    return "\n".join(html_parts)


def main():
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    for d in DOCTORS:
        other_docs = make_other_doctors_html(d["num"])
        page = template
        page = page.replace("{{DOCTOR_NAME}}", d["name"])
        page = page.replace("{{DEGREE_SHORT}}", d["deg_short"])
        page = page.replace("{{DEGREE_FULL}}", d["deg_full"])
        page = page.replace("{{DESIGNATION}}", d["desig"])
        page = page.replace("{{DESIGNATION_SHORT}}", d["desig_short"])
        page = page.replace("{{SPECIALTY}}", d["spec"])
        page = page.replace("{{DEPARTMENT}}", d["dept"])
        page = page.replace("{{AVATAR_INITIAL}}", d["initial"])
        page = page.replace("{{AFFILIATION}}", d["affil"])
        page = page.replace("{{YEARS}}", d["years"])
        page = page.replace("{{PATIENTS}}", d["patients"])
        page = page.replace("{{RATING}}", d["rating"])
        page = page.replace("{{TRAINING}}", d["training"])
        page = page.replace("{{SPECIALTY_LIST}}", d["specialty_list"])
        page = page.replace("{{DISEASE_LIST}}", d["disease_list"])
        page = page.replace("{{SCHEDULE_LIST}}", d["schedule"])
        page = page.replace("{{OTHER_DOCTORS}}", other_docs)

        out_path = os.path.join(OUT_DIR, f"{d['num']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"[OK] {out_path}  ({len(page):,} bytes)")

    print(f"\nDone. Generated {len(DOCTORS)} doctor profile pages.")


if __name__ == "__main__":
    main()
