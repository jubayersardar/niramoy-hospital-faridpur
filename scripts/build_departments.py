# -*- coding: utf-8 -*-
"""Build departments.html — 8 departments with full details."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_site import (
    TOPBAR, FOOTER, FAB, HEAD_BASE, SCRIPTS, NAV,
    make_header, make_page, WEB, PAGES, DOCTORS, DEPT_COLOR
)

DEPARTMENTS_CSS = r"""
.dept-detail{padding:80px 0;border-bottom:1px solid var(--border);scroll-margin-top:80px}
.dept-detail:nth-child(even){background:var(--bg-soft)}
.dept-detail-head{display:grid;grid-template-columns:auto 1fr;gap:30px;align-items:center;margin-bottom:36px}
.dept-detail-icon{width:90px;height:90px;border-radius:22px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:2.4rem;flex-shrink:0;box-shadow:var(--shadow-md)}
.dept-detail h2{font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:8px}
.dept-detail .tagline{color:var(--accent);font-weight:600;font-size:0.95rem;margin-bottom:14px}
.dept-detail .lead{color:var(--text-muted);font-size:1.02rem;line-height:1.7;margin-bottom:24px}
.dept-detail-grid{display:grid;grid-template-columns:1.5fr 1fr;gap:30px}
.dept-services{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:24px;box-shadow:var(--shadow-sm)}
.dept-services h3,.dept-doctors-mini h3{font-size:1.1rem;margin-bottom:14px;display:flex;align-items:center;gap:8px;color:var(--primary)}
.dept-services h3 i,.dept-doctors-mini h3 i{color:var(--accent)}
.dept-services ul{list-style:none;padding:0;margin:0}
.dept-services ul li{padding:8px 0 8px 26px;position:relative;color:var(--text-muted);font-size:0.92rem;border-bottom:1px dashed var(--border)}
.dept-services ul li:last-child{border-bottom:none}
.dept-services ul li::before{content:"\f00c";font-family:"Font Awesome 6 Free";font-weight:900;color:var(--accent);position:absolute;left:0;top:8px;font-size:0.78rem}
.dept-doctors-mini{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:24px;box-shadow:var(--shadow-sm)}
.dept-doc-list{display:flex;flex-direction:column;gap:12px}
.dept-doc-item{display:flex;align-items:center;gap:12px;padding:10px;border-radius:10px;background:var(--bg-soft);text-decoration:none;color:inherit;transition:all var(--transition)}
.dept-doc-item:hover{background:var(--primary-light);transform:translateX(4px)}
.dept-doc-avatar{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1rem;font-weight:700;color:#fff;flex-shrink:0}
.dept-doc-info h4{font-size:0.92rem;margin-bottom:2px;line-height:1.2}
.dept-doc-info p{font-size:0.78rem;color:var(--text-muted);margin:0}
.dept-tech-pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.dept-tech-pill{padding:5px 12px;background:var(--primary-light);color:var(--primary);border-radius:50px;font-size:0.78rem;font-weight:600}
@media (max-width:768px){.dept-detail-head{grid-template-columns:1fr;text-align:center}.dept-detail-icon{margin:0 auto}.dept-detail-grid{grid-template-columns:1fr}}
"""

# Doctor mapping by department class
DEPT_DOCS = {
    "med":   [d for d in DOCTORS if d["dept_class"] == "med"],
    "surg":  [d for d in DOCTORS if d["dept_class"] == "surg"],
    "gynae": [d for d in DOCTORS if d["dept_class"] == "gynae"],
    "ortho": [d for d in DOCTORS if d["dept_class"] == "ortho"],
    "ent":   [d for d in DOCTORS if d["dept_class"] == "ent"],
    "derma": [d for d in DOCTORS if d["dept_class"] == "derma"],
    "gp":    [d for d in DOCTORS if d["dept_class"] == "gp"],
    "sono":  [d for d in DOCTORS if d["dept_class"] == "sono"],
}

DEPT_DATA = [
    {
        "class": "med", "anchor": "med", "icon": "fa-stethoscope",
        "name": "মেডিসিন বিভাগ",
        "tagline": "অভ্যন্তরীণ রোগের সমন্বিত চিকিৎসা",
        "lead": "মেডিসিন বিভাগ ডায়াবেটিস, উচ্চ রক্তচাপ, হৃদরোগ, বক্ষব্যাধি, কিডনি-লিভারের সমস্যাসহ সব ধরনের অভ্যন্তরীণ রোগের সমন্বিত চিকিৎসা প্রদান করে। অভিজ্ঞ মেডিসিন বিশেষজ্ঞগণ আধুনিক চিকিৎসা পদ্ধতি ও প্রযুক্তি ব্যবহার করে রোগীদের সেবা দেন।",
        "services": [
            "মেডিসিন বিশেষজ্ঞ পরামর্শ ও চিকিৎসা",
            "ডায়াবেটিস নিয়ন্ত্রণ ও ব্যবস্থাপনা",
            "হৃদরোগের চিকিৎসা ও পরামর্শ",
            "বক্ষব্যাধি (হাঁপানি, ব্রংকাইটিস, নিউমোনিয়া)",
            "উচ্চ রক্তচাপ ব্যবস্থাপনা",
            "কিডনি ও লিভার রোগ",
            "থাইরয়েড ও হরমোনজনিত সমস্যা",
            "রক্তস্বল্পতা ও পুষ্টিজনিত সমস্যা",
        ],
        "tech": ["ECG", "ইকো", "রক্ত পরীক্ষা", "HbA1c", "Lipid Profile"],
    },
    {
        "class": "surg", "anchor": "surg", "icon": "fa-user-md",
        "name": "সার্জারি বিভাগ",
        "tagline": "জেনারেল ও ল্যাপারোস্কোপিক সার্জারি",
        "lead": "সার্জারি বিভাগ জেনারেল ও ল্যাপারোস্কোপিক সার্জারি, কলোরেক্টাল সার্জারি ও ইউরোলজিক্যাল সার্জারি সেবা প্রদান করে। আধুনিক অপারেশন থিয়েটার ও অভিজ্ঞ সার্জন দিয়ে সজ্জিত।",
        "services": [
            "জেনারেল সার্জারি (সব ধরনের অপারেশন)",
            "ল্যাপারোস্কোপিক (কী-হোল) সার্জারি",
            "কলোরেক্টাল সার্জারি",
            "পাইলস, ফিস্টুলা, ফিশার চিকিৎসা",
            "অ্যাপেন্ডিক্স, হার্নিয়া, গলব্লাডার অপারেশন",
            "পিত্তথলির পাথর অপারেশন",
            "থাইরয়েড ও সফট টিস্যু টিউমার",
            "ইউরোলজিক্যাল সার্জারি",
        ],
        "tech": ["আধুনিক ওটি", "ল্যাপারোস্কোপিক সেট", "Anaesthesia", "C-arm"],
    },
    {
        "class": "gynae", "anchor": "gynae", "icon": "fa-venus",
        "name": "গাইনি ও প্রসূতি বিভাগ",
        "tagline": "নারীর স্বাস্থ্য ও মাতৃত্বকালীন সেবা",
        "lead": "গাইনি ও প্রসূতি বিভাগ নারীর প্রজনন স্বাস্থ্য, গর্ভাবস্থা, সন্তান প্রসব ও বন্ধ্যাত্ব চিকিৎসায় বিশেষজ্ঞ সেবা প্রদান করে। নিরাপদ মাতৃত্ব ও নবজাতকের যত্নে আমরা প্রতিশ্রুতিবদ্ধ।",
        "services": [
            "গাইনি ও প্রসূতি পরামর্শ",
            "নরমাল ও সিজারিয়ান ডেলিভারি",
            "বন্ধ্যাত্ব (ইনফার্টিলিটি) চিকিৎসা",
            "মাসিক সমস্যা ও হরমোনের সমস্যা",
            "পলিসিস্টিক ওভারি সিন্ড্রোম (PCOS)",
            "জরায়ু টিউমার ও ওভারিয়ান সিস্ট",
            "প্রি-পোস্ট মেনোপজ পরামর্শ",
            "প্রসবপূর্ব ও প্রসবোত্তর যত্ন",
        ],
        "tech": ["USG", "NST", "Labour Room", "Neo-natal Care"],
    },
    {
        "class": "ortho", "anchor": "ortho", "icon": "fa-bone",
        "name": "অর্থোপেডিক্স বিভাগ",
        "tagline": "হাড়, জয়েন্ট ও ট্রমা সার্জারি",
        "lead": "অর্থোপেডিক্স বিভাগ হাড় ও জয়েন্টের সমস্যা, ফ্র্যাকচার, ট্রমা, বাতব্যথা, স্পোর্টস ইনজুরি ও মেরুদণ্ডের সমস্যার চিকিৎসা প্রদান করে। আধুনিক অপারেশন থিয়েটার ও অর্থো-সার্জারি সরঞ্জাম দিয়ে সজ্জিত।",
        "services": [
            "হাড় ও জয়েন্ট সার্জারি",
            "ফ্র্যাকচার (হাড় ভাঙা) চিকিৎসা",
            "ট্রমা ও অ্যাক্সিডেন্ট জনিত চিকিৎসা",
            "বাতব্যথা ও আর্থ্রাইটিস",
            "মেরুদণ্ডের সমস্যা",
            "স্পোর্টস ইনজুরি",
            "প্লাস্টার ও ব্যান্ডেজিং",
            "জয়েন্ট রিপ্লেসমেন্ট",
        ],
        "tech": ["C-arm", "Ortho Instruments", "Plaster Room", "X-ray"],
    },
    {
        "class": "ent", "anchor": "ent", "icon": "fa-ear-listen",
        "name": "ইএনটি বিভাগ",
        "tagline": "নাক-কান-গলা ও হেড-নেক সার্জারি",
        "lead": "ইএনটি বিভাগ নাক, কান, গলা, সাইনাস, টনসিল ও হেড-নেক সম্পর্কিত সব ধরনের রোগ নির্ণয় ও চিকিৎসা প্রদান করে। দীর্ঘদিনের অভিজ্ঞতাসম্পন্ন ইএনটি বিশেষজ্ঞ দ্বারা পরিচালিত।",
        "services": [
            "নাক, কান, গলার সব ধরনের চিকিৎসা",
            "টনসিল ও অ্যাডেনয়েড অপারেশন",
            "সাইনাস ইনফেকশন ও সাইনাস সার্জারি",
            "কানের পর্দা ছিদ্র অপারেশন",
            "হেড-নেক টিউমার সার্জারি",
            "নাকের পলিপ ও ডেভিয়েশন",
            "গলার ভয়েস ও ল্যারিংজিয়াল সমস্যা",
            "কানে শোনা সমস্যা",
        ],
        "tech": ["Endoscope", "Microscope", "Audiometry", "ENT Set"],
    },
    {
        "class": "derma", "anchor": "derma", "icon": "fa-hand-dots",
        "name": "চর্ম ও যৌন বিভাগ",
        "tagline": "চর্মরোগ, এলার্জি ও যৌন স্বাস্থ্য",
        "lead": "চর্ম ও যৌন বিভাগ চর্মরোগ, এক্সিমা, সোরিয়াসিস, ব্রণ, এলার্জি, যৌনবাহিত রোগ ও চুল-নখের সমস্যার চিকিৎসা প্রদান করে। আধুনিক চর্মরোগ চিকিৎসায় বিশেষজ্ঞ পরামর্শ।",
        "services": [
            "এক্সিমা ও ডার্মাটাইটিস চিকিৎসা",
            "সোরিয়াসিস ও অন্যান্য দীর্ঘমেয়াদী চর্মরোগ",
            "ব্রণ ও ত্বকের সমস্যা",
            "দাউদ (Ringworm) ও ছত্রাক সংক্রমণ",
            "এলার্জি ও আমবাত",
            "যৌনবাহিত রোগ (STI)",
            "চুল পড়া ও নখের সমস্যা",
            "ভিটিলিগো ও স্কিন ডিসঅর্ডার",
        ],
        "tech": ["Wood's Lamp", "Dermatoscope", "Skin Biopsy", "Patch Test"],
    },
    {
        "class": "gp", "anchor": "gp", "icon": "fa-user-doctor",
        "name": "জেনারেল প্র্যাকটিশনার",
        "tagline": "সাধারণ রোগের সমন্বিত চিকিৎসা",
        "lead": "জেনারেল প্র্যাকটিশনার বিভাগ সব ধরনের সাধারণ রোগ, শিশু রোগ, মাইনর সার্জারি ও সাধারণ স্বাস্থ্য পরামর্শ প্রদান করে। অভিজ্ঞ চিকিৎসক দীর্ঘ ২৫+ বছরের ক্লিনিক্যাল অভিজ্ঞতা নিয়ে সেবা দিচ্ছেন।",
        "services": [
            "সাধারণ রোগের চিকিৎসা ও পরামর্শ",
            "মাইনর সার্জারি ও ক্ষত ড্রেসিং",
            "স্ত্রী-রোগ ও প্রসূতি পরামর্শ",
            "শিশু রোগ ও টিকা",
            "চর্ম ও যৌন রোগ",
            "বক্ষব্যাধি ও হাঁপানি",
            "পরিপাকতন্ত্রের সমস্যা",
            "সাধারণ স্বাস্থ্য চেকআপ",
        ],
        "tech": ["X-ray", "ECG", "Lab Tests", "Vaccination"],
    },
    {
        "class": "sono", "anchor": "sono", "icon": "fa-wave-square",
        "name": "আল্ট্রাসনোগ্রাফি বিভাগ",
        "tagline": "সম্পূর্ণ USG ও ইকো",
        "lead": "আল্ট্রাসনোগ্রাফি বিভাগ ৪ডি কালার ডপলার মেশিন দিয়ে সম্পূর্ণ পেটের USG, গর্ভাবস্থার USG, কিডনি-লিভার, থাইরয়েড, হার্ট ও বক্ষের ইকো সেবা প্রদান করে। ৩০+ বছরের অভিজ্ঞ রেডিওলজিস্ট দ্বারা পরিচালিত।",
        "services": [
            "সম্পূর্ণ আল্ট্রাসনোগ্রাফি (USG)",
            "গর্ভাবস্থায় আল্ট্রাসনো (ANC)",
            "কিডনি ও লিভারের USG",
            "থাইরয়েড ও ঘাড়ের USG",
            "হার্ট ও বক্ষের ইকো",
            "পেলভিস ও লোয়ার অ্যাবডোমেন",
            "ডপলার স্টাডি",
            "রিয়েল-টাইম রিপোর্ট",
        ],
        "tech": ["4D Color Doppler", "Echocardiography", "TVS Probe", "Convex Probe"],
    },
]

def build_departments():
    sections = []
    for d in DEPT_DATA:
        doc_cards = "\n".join(
            f'          <a href="doctors/{doc["num"]}.html" class="dept-doc-item">\n'
            f'            <div class="dept-doc-avatar" style="background:{DEPT_COLOR.get(d["class"], DEPT_COLOR["med"])}">{doc["initial"]}</div>\n'
            f'            <div class="dept-doc-info"><h4>{doc["name"]}</h4><p>{doc["deg_short"]}</p></div>\n'
            f'          </a>'
            for doc in DEPT_DOCS.get(d["class"], [])
        )
        services_html = "\n".join(f'          <li>{s}</li>' for s in d["services"])
        tech_pills = "\n".join(f'          <span class="dept-tech-pill">{t}</span>' for t in d["tech"])
        sections.append(f'''
<section class="dept-detail" id="{d["anchor"]}">
  <div class="container">
    <div class="dept-detail-head">
      <div class="dept-detail-icon bg-{d["class"]}"><i class="fa-solid {d["icon"]}"></i></div>
      <div>
        <span class="section-eyebrow">বিভাগ</span>
        <h2>{d["name"]}</h2>
        <p class="tagline">{d["tagline"]}</p>
      </div>
    </div>
    <p class="lead">{d["lead"]}</p>
    <div class="dept-detail-grid">
      <div>
        <div class="dept-services">
          <h3><i class="fa-solid fa-hand-holding-medical"></i> প্রধান সেবাসমূহ</h3>
          <ul>
{services_html}
          </ul>
          <h3 style="margin-top:24px"><i class="fa-solid fa-microscope"></i> আধুনিক প্রযুক্তি ও সরঞ্জাম</h3>
          <div class="dept-tech-pills">
{tech_pills}
          </div>
        </div>
      </div>
      <div>
        <div class="dept-doctors-mini">
          <h3><i class="fa-solid fa-user-doctor"></i> বিভাগের বিশেষজ্ঞ</h3>
          <div class="dept-doc-list">
{doc_cards}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
''')
    body = f'''
<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <span class="hero-eyebrow"><i class="fa-solid fa-th-large"></i> বিশেষায়িত বিভাগ</span>
      <h1>আমাদের বিভাগসমূহ</h1>
      <p>৮টি বিশেষায়িত বিভাগে ১৪+ বিশেষজ্ঞ চিকিৎসক — সব ধরনের রোগের সমন্বিত চিকিৎসা</p>
    </div>
  </div>
</section>

<div class="breadcrumb">
  <div class="container">
    <a href="index.html">হোম</a> <span class="sep">›</span>
    <span class="current">বিভাগসমূহ</span>
  </div>
</div>

{''.join(sections)}
'''
    return make_page(
        title="বিভাগসমূহ",
        description="নিরাময় হাসপাতালের ৮টি বিশেষায়িত বিভাগ — মেডিসিন, সার্জারি, গাইনি, অর্থোপেডিক্স, ইএনটি, চর্ম, জেনারেল প্র্যাকটিশনার ও আল্ট্রাসনোগ্রাফি।",
        active_page="departments",
        body=body,
        page_css=DEPARTMENTS_CSS
    )


print("Building departments.html...")
out = os.path.join(WEB, "departments.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(build_departments())
print(f"  [OK] {out} ({os.path.getsize(out):,} bytes)")
