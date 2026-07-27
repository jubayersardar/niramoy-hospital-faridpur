# -*- coding: utf-8 -*-
"""Build remaining 5 pages: services, diagnostic, gallery, contact, appointment."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_site import (
    TOPBAR, FOOTER, FAB, HEAD_BASE, SCRIPTS, NAV,
    make_header, make_page, WEB, PAGES
)

# =====================================================================
# services.html
# =====================================================================
SERVICES_CSS = r"""
.services-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}
.service-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:30px 24px;transition:all var(--transition);position:relative;overflow:hidden}
.service-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:rgba(0,102,164,0.30)}
.service-icon{width:60px;height:60px;border-radius:16px;background:linear-gradient(135deg,var(--primary) 0%,var(--primary-dark) 100%);color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.5rem;margin-bottom:16px}
.service-card h3{font-size:1.15rem;margin-bottom:10px}
.service-card p{color:var(--text-muted);font-size:0.92rem;margin-bottom:14px}
.service-features{list-style:none;padding:0;margin:0}
.service-features li{padding:6px 0 6px 22px;position:relative;color:var(--text-muted);font-size:0.88rem}
.service-features li::before{content:"\f00c";font-family:"Font Awesome 6 Free";font-weight:900;color:var(--accent);position:absolute;left:0;top:6px;font-size:0.78rem}
"""

SERVICES_DATA = [
    {"icon":"fa-procedures","name":"আউটডোর (OPD) সেবা","desc":"বিশেষজ্ঞ চিকিৎসকদের সাথে সরাসরি পরামর্শ — নিয়মিত ও নির্ধারিত সময়ে।","features":["বিশেষজ্ঞ চিকিৎসক পরামর্শ","নিয়মিত চেকআপ","ওষুধ সেবা","রেকর্ড সংরক্ষণ"]},
    {"icon":"fa-bed-pulse","name":"ইনডোর (IPD) সেবা","desc":"মানসম্মত ওয়ার্ড ও কেবিনে ভর্তি রোগীদের চিকিৎসা ও পরিচর্যা।","features":["সাধারণ ওয়ার্ড","AC/Non-AC কেবিন","অভিজ্ঞ নার্সিং","24/7 ডাক্তার মনিটরিং"]},
    {"icon":"fa-truck-medical","name":"২৪/৭ ইমার্জেন্সি","desc":"সার্বক্ষণিক জরুরি সেবা ও অ্যাম্বুলেন্স — যেকোনো সময় কল করুন।","features":["24/7 ইমার্জেন্সি বিভাগ","অ্যাম্বুলেন্স সেবা","প্রাথমিক চিকিৎসা","দ্রুত রেফারেল"]},
    {"icon":"fa-scalpel","name":"অপারেশন থিয়েটার","desc":"আধুনিক ওটি কমপ্লেক্সে সব ধরনের সার্জারি — ল্যাপারোস্কোপিকসহ।","features":["আধুনিক ওটি","ল্যাপারোস্কোপিক সার্জারি","অ্যানেস্থেসিয়া","পোস্ট-অপ কেয়ার"]},
    {"icon":"fa-truck-fast","name":"অ্যাম্বুলেন্স সেবা","desc":"ফরিদপুর ও আশেপাশের এলাকায় অ্যাম্বুলেন্স সেবা — ২৪ ঘণ্টা।","features":["24/7 অ্যাম্বুলেন্স","ICU অ্যাম্বুলেন্স","অক্সিজেন সুবিধা","প্রশিক্ষিত কর্মী"]},
    {"icon":"fa-pills","name":"ফার্মেসি","desc":"হাসপাতালের নিজস্ব ফার্মেসি — সাশ্রয়ী মূল্যে ওষুধ।","features":["সকল ওষুধ পাওয়া যায়","সাশ্রয়ী মূল্য","অভিজ্ঞ ফার্মাসিস্ট","লাইসেন্সপ্রাপ্ত"]},
    {"icon":"fa-stethoscope","name":"চেকআপ প্যাকেজ","desc":"সাশ্রয়ী মূল্যে সম্পূর্ণ স্বাস্থ্য পরীক্ষা প্যাকেজ।","features":["রক্ত পরীক্ষা","ECG ও ইকো","X-ray ও USG","ডাক্তার পরামর্শ"]},
    {"icon":"fa-shield-virus","name":"ভ্যাকসিনেশন","desc":"শিশু ও প্রাপ্তবয়স্কদের জন্য সব ধরনের টিকা।","features":["EPI টিকা","ভ্রমণ টিকা","ফ্লু ভ্যাকসিন","HPV ভ্যাকসিন"]},
]

def build_services():
    cards = "\n".join(
        f'''      <div class="service-card reveal">
        <div class="service-icon"><i class="fa-solid {s["icon"]}"></i></div>
        <h3>{s["name"]}</h3>
        <p>{s["desc"]}</p>
        <ul class="service-features">
{chr(10).join(f'          <li>{f}</li>' for f in s["features"])}
        </ul>
      </div>
'''
        for s in SERVICES_DATA
    )
    body = f'''
<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <span class="hero-eyebrow"><i class="fa-solid fa-hand-holding-medical"></i> হাসপাতাল সেবা</span>
      <h1>আমাদের সেবাসমূহ</h1>
      <p>আউটডোর, ইনডোর, ইমার্জেন্সি, অপারেশন, ফার্মেসি — সব এক ছাদের নিচে</p>
    </div>
  </div>
</section>

<div class="breadcrumb">
  <div class="container">
    <a href="index.html">হোম</a> <span class="sep">›</span>
    <span class="current">সেবাসমূহ</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">হাসপাতাল সেবা</span>
      <h2 class="section-title">আমাদের <span class="gradient-text">সেবাসমূহ</span></h2>
      <p class="section-subtitle">রোগীর সুবিধা ও স্বাচ্ছন্দ্যে সব ধরনের চিকিৎসা সেবা এক ছাদের নিচে</p>
    </div>
    <div class="services-grid">
{cards}
    </div>
  </div>
</section>
'''
    return make_page(
        title="সেবাসমূহ",
        description="নিরাময় হাসপাতালের সেবাসমূহ — আউটডোর, ইনডোর, ২৪/৭ ইমার্জেন্সি, অপারেশন থিয়েটার, অ্যাম্বুলেন্স, ফার্মেসি ও চেকআপ।",
        active_page="services",
        body=body,
        page_css=SERVICES_CSS
    )

# =====================================================================
# diagnostic.html
# =====================================================================
DIAGNOSTIC_CSS = r"""
.diag-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}
.diag-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:30px 24px;transition:all var(--transition);position:relative;overflow:hidden}
.diag-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:rgba(0,102,164,0.30)}
.diag-icon{width:64px;height:64px;border-radius:18px;background:linear-gradient(135deg,var(--accent) 0%,var(--accent-dark) 100%);color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.6rem;margin-bottom:16px}
.diag-card h3{font-size:1.15rem;margin-bottom:8px}
.diag-card .diag-lead{color:var(--text-muted);font-size:0.92rem;margin-bottom:14px}
.diag-tests{list-style:none;padding:0;margin:0 0 14px 0;border-top:1px dashed var(--border);padding-top:14px}
.diag-tests li{padding:5px 0 5px 22px;position:relative;color:var(--text-muted);font-size:0.86rem}
.diag-tests li::before{content:"\\f46b";font-family:"Font Awesome 6 Free";font-weight:900;color:var(--accent);position:absolute;left:0;top:5px;font-size:0.72rem}
.diag-tech{font-size:0.78rem;color:var(--text-muted);background:var(--bg-soft);padding:8px 12px;border-radius:8px;margin-top:10px}
"""

DIAG_DATA = [
    {"icon":"fa-microscope","name":"ক্লিনিক্যাল প্যাথলজি","lead":"রক্ত, প্রস্রাব, কফ, স্টুল ও সিবিসি সহ সকল প্যাথলজিক্যাল পরীক্ষা।","tests":["CBC ও ESR","Urine R/E","Blood Grouping","Sugar Profile","Liver Function Test (LFT)","Kidney Function Test (KFT)","Lipid Profile","Electrolytes"]},
    {"icon":"fa-wave-square","name":"আল্ট্রাসনোগ্রাফি (USG)","lead":"৪ডি কালার ডপলার মেশিনে সম্পূর্ণ আল্ট্রাসাউন্ড সেবা।","tests":["Whole Abdomen USG","Pelvis USG","TVS (Transvaginal)","Pregnancy Profile","Thyroid/ Neck","Echocardiography","Doppler Study","Renal USG"]},
    {"icon":"fa-heart-pulse","name":"ইসিজি (ECG)","lead":"হৃদরোগ নির্ণয়ের জন্য ডিজিটাল ইসিজি।","tests":["Resting ECG","Stress ECG (TMT)","Holter Monitoring","Rhythm Analysis","Ischemia Detection","Pre-op ECG"]},
    {"icon":"fa-x-ray","name":"ডিজিটাল এক্স-রে","lead":"হাড়, বক্ষ ও অন্যান্য এক্স-রে — দ্রুত রিপোর্ট সহ।","tests":["Chest X-ray","Abdomen X-ray","Bone X-ray","Spine X-ray","Skull X-ray","Joint X-ray"]},
    {"icon":"fa-droplet","name":"বায়োকেমিস্ট্রি","lead":"Automated Analyzer দিয়ে সব বায়োকেমিক্যাল পরীক্ষা।","tests":["Glucose (F/R/2HR)","HbA1c","Lipid Profile","LFT","KFT","Electrolytes","Uric Acid","Calcium/Magnesium"]},
    {"icon":"fa-vial-virus","name":"হরমোন ও সেরোলজি","lead":"থাইরয়েড, ডায়াবেটিস ও অন্যান্য হরমোন টেস্ট।","tests":["T3, T4, TSH","Anti-TPO","Insulin","Cortisol","Vitamin D","Vitamin B12","Ferritin","PSA"]},
]

def build_diagnostic():
    cards = "\n".join(
        f'''      <div class="diag-card reveal">
        <div class="diag-icon"><i class="fa-solid {d["icon"]}"></i></div>
        <h3>{d["name"]}</h3>
        <p class="diag-lead">{d["lead"]}</p>
        <ul class="diag-tests">
{chr(10).join(f'          <li>{t}</li>' for t in d["tests"])}
        </ul>
      </div>
'''
        for d in DIAG_DATA
    )
    body = f'''
<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <span class="hero-eyebrow"><i class="fa-solid fa-microscope"></i> ডায়াগনস্টিক সেবা</span>
      <h1>আধুনিক ডায়াগনস্টিক ল্যাব</h1>
      <p>সঠিক রোগ নির্ণয়ের জন্য সর্বাধুনিক যন্ত্রপাতি ও প্রযুক্তি</p>
    </div>
  </div>
</section>

<div class="breadcrumb">
  <div class="container">
    <a href="index.html">হোম</a> <span class="sep">›</span>
    <span class="current">ডায়াগনস্টিক</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">ডায়াগনস্টিক</span>
      <h2 class="section-title">আমাদের <span class="gradient-text">ডায়াগনস্টিক সেবা</span></h2>
      <p class="section-subtitle">৬টি বিভাগে সম্পূর্ণ ডায়াগনস্টিক সেবা — দ্রুত রিপোর্ট সহ</p>
    </div>
    <div class="diag-grid">
{cards}
    </div>
  </div>
</section>
'''
    return make_page(
        title="ডায়াগনস্টিক",
        description="নিরাময় হাসপাতালের আধুনিক ডায়াগনস্টিক সেবা — প্যাথলজি, আল্ট্রাসনোগ্রাফি, ইসিজি, এক্স-রে, বায়োকেমিস্ট্রি ও হরমোন টেস্ট।",
        active_page="diagnostic",
        body=body,
        page_css=DIAGNOSTIC_CSS
    )

# =====================================================================
# gallery.html
# =====================================================================
GALLERY_CSS = r"""
.gallery-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
.gallery-grid img{width:100%;height:240px;object-fit:cover;border-radius:var(--radius);transition:transform 0.4s ease;cursor:pointer}
.gallery-grid img:hover{transform:scale(1.03)}
.lightbox-backdrop{position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:9999;display:none;align-items:center;justify-content:center;padding:20px}
.lightbox-backdrop.show{display:flex}
.lightbox-backdrop img{max-width:90vw;max-height:90vh;border-radius:var(--radius);box-shadow:0 30px 80px rgba(0,0,0,0.5)}
.lightbox-close{position:absolute;top:20px;right:30px;width:50px;height:50px;background:rgba(255,255,255,0.15);color:#fff;border-radius:50%;font-size:1.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,0.30)}
.lightbox-close:hover{background:rgba(255,255,255,0.25)}
"""

def build_gallery():
    images = [
        ("niramoy-aidfast-cover.jpg", "হাসপাতাল ভবন"),
        ("niramaya-banner-official.jpg", "NIRAMAYA অফিসিয়াল ব্যানার"),
        ("niramoy-building-night.jpg", "সন্ধ্যার আলোয়"),
        ("niramoy-archhms-header.jpg", "ভেতরের অংশ"),
        ("niramoy-archhms-gallery2.jpg", "হাসপাতাল সুবিধা"),
        ("niramoy-aidfast-profile.jpg", "নিরাময় হাসপাতাল"),
    ]
    img_html = "\n".join(
        f'      <img src="{src}" alt="{alt}" loading="lazy" />' for src, alt in images
    )
    body = f'''
<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <span class="hero-eyebrow"><i class="fa-solid fa-images"></i> গ্যালারি</span>
      <h1>হাসপাতালের ছবি</h1>
      <p>পরিচ্ছন্ন ও আরামদায়ক পরিবেশে আধুনিক সেবা</p>
    </div>
  </div>
</section>

<div class="breadcrumb">
  <div class="container">
    <a href="index.html">হোম</a> <span class="sep">›</span>
    <span class="current">গ্যালারি</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">আমাদের পরিবেশ</span>
      <h2 class="section-title">হাসপাতালের <span class="gradient-text">ছবি</span></h2>
      <p class="section-subtitle">ছবিতে ক্লিক করে বড় করে দেখুন</p>
    </div>
    <div class="gallery-grid">
{img_html}
    </div>
  </div>
</section>

<div class="lightbox-backdrop" id="lightbox">
  <button class="lightbox-close" aria-label="বন্ধ"><i class="fa-solid fa-xmark"></i></button>
  <img src="" alt="Gallery image" />
</div>
'''
    return make_page(
        title="গ্যালারি",
        description="নিরাময় হাসপাতালের ছবি — ভবন, ভেতরের অংশ, সুবিধা, সন্ধ্যার আলো।",
        active_page="gallery",
        body=body,
        page_css=GALLERY_CSS
    )

# =====================================================================
# contact.html
# =====================================================================
CONTACT_CSS = r"""
.contact-grid{display:grid;grid-template-columns:1fr 1.4fr;gap:30px;align-items:start}
.contact-cards{display:flex;flex-direction:column;gap:16px}
.contact-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:20px;display:flex;gap:14px;align-items:flex-start;transition:all var(--transition);box-shadow:var(--shadow-sm)}
.contact-card:hover{box-shadow:var(--shadow-md);transform:translateY(-2px)}
.contact-card .ic{width:46px;height:46px;background:var(--primary-light);color:var(--primary);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0}
.contact-card h4{font-size:1rem;margin-bottom:4px}
.contact-card p,.contact-card a{font-size:0.88rem;color:var(--text-muted)}
.contact-card a:hover{color:var(--primary)}
.contact-form{background:#fff;border:1px solid var(--border);border-radius:var(--radius-lg);padding:36px;box-shadow:var(--shadow-md)}
.contact-form h3{font-size:1.3rem;margin-bottom:8px}
.contact-form > p{color:var(--text-muted);margin-bottom:24px;font-size:0.95rem}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.form-group{display:flex;flex-direction:column;gap:6px}
.form-group.full{grid-column:1 / -1}
.form-group label{font-size:0.88rem;font-weight:500}
.form-group label .req{color:#e74c3c}
.form-group input,.form-group select,.form-group textarea{padding:12px 14px;border:1.5px solid var(--border);border-radius:10px;font-size:0.95rem;background:#fff;transition:all var(--transition)}
.form-group input:focus,.form-group select:focus,.form-group textarea:focus{outline:none;border-color:var(--primary);box-shadow:0 0 0 3px rgba(0,102,164,0.10)}
.form-group textarea{resize:vertical;min-height:120px}
.form-success{display:none;background:var(--accent-light);color:var(--accent-dark);padding:14px 18px;border-radius:10px;margin-top:16px;font-size:0.9rem;border-left:4px solid var(--accent)}
.form-success.show{display:block}
.map-wrap{border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-md);min-height:520px}
.map-wrap iframe{width:100%;height:100%;min-height:520px;border:0;display:block}
.hours-list{list-style:none;padding:0;margin:0}
.hours-list li{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px dashed var(--border);font-size:0.92rem}
.hours-list li:last-child{border-bottom:none}
.hours-list .day{color:var(--text)}
.hours-list .time{color:var(--primary);font-weight:600}
@media (max-width:768px){.contact-grid{grid-template-columns:1fr}.form-grid{grid-template-columns:1fr}}
"""

def build_contact():
    body = '''
<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <span class="hero-eyebrow"><i class="fa-solid fa-location-dot"></i> যোগাযোগ</span>
      <h1>আমাদের সাথে যোগাযোগ</h1>
      <p>যেকোনো প্রয়োজনে যোগাযোগ করুন — আমরা সবসময় আপনার পাশে</p>
    </div>
  </div>
</section>

<div class="breadcrumb">
  <div class="container">
    <a href="index.html">হোম</a> <span class="sep">›</span>
    <span class="current">যোগাযোগ</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-cards">
        <div class="contact-card">
          <div class="ic"><i class="fa-solid fa-location-dot"></i></div>
          <div>
            <h4>ঠিকানা</h4>
            <p>নিরাময় ভবন, পশ্চিম খাবাসপুর, ফরিদপুর</p>
          </div>
        </div>
        <div class="contact-card">
          <div class="ic"><i class="fa-solid fa-phone"></i></div>
          <div>
            <h4>ফোন</h4>
            <p>
              <a href="tel:+8801729171549">+৮৮০১৭২৯-১৭১৫৪৯</a> (মূল)<br/>
              <a href="tel:+8801734089489">+৮৮০১৭৩৪-০৮৯৪৮৯</a><br/>
              <a href="tel:+8801720003699">+৮৮০১৭২০-০০৩৬৯৯</a>
            </p>
          </div>
        </div>
        <div class="contact-card">
          <div class="ic" style="background:#ffeaa7;color:#d35400"><i class="fa-solid fa-truck-medical"></i></div>
          <div>
            <h4>ইমার্জেন্সি (২৪/৭)</h4>
            <p><a href="tel:+8801731827110"><strong>+৮৮০১৭৩১-৮২৭১১০</strong></a></p>
          </div>
        </div>
        <div class="contact-card">
          <div class="ic" style="background:#d4edda;color:var(--accent)"><i class="fa-brands fa-whatsapp"></i></div>
          <div>
            <h4>WhatsApp</h4>
            <p><a href="https://wa.me/8801731827110" target="_blank" rel="noopener">+৮৮০১৭৩১-৮২৭১১০</a></p>
          </div>
        </div>
        <div class="contact-card">
          <div class="ic" style="background:#dbeafe;color:#1877f2"><i class="fa-brands fa-facebook"></i></div>
          <div>
            <h4>Facebook</h4>
            <p><a href="https://www.facebook.com/p/%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A7%9F-%E0%A6%B9%E0%A6%B8%E0%A6%AA%E0%A6%BF%E0%A6%9F%E0%A6%BE%E0%A6%B2-%E0%A6%AB%E0%A6%B0%E0%A6%BF%E0%A6%A6%E0%A6%AA%E0%A7%81%E0%A6%B0-61577130113409/" target="_blank" rel="noopener">নিরাময় হাসপাতাল, ফরিদপুর</a></p>
          </div>
        </div>
        <div class="contact-card">
          <div class="ic" style="background:#fef3c7;color:#d97706"><i class="fa-regular fa-clock"></i></div>
          <div>
            <h4>সেবার সময়সূচি</h4>
            <ul class="hours-list">
              <li><span class="day">আউটডোর (OPD)</span><span class="time">সকাল ৯টা - রাত ৯টা</span></li>
              <li><span class="day">শনি-বৃহস্পতি</span><span class="time">সকাল ৯টা - রাত ৮টা</span></li>
              <li><span class="day">শুক্রবার</span><span class="time">সকাল ১০টা - বিকাল ৫টা</span></li>
              <li><span class="day">ইমার্জেন্সি</span><span class="time">২৪/৭</span></li>
            </ul>
          </div>
        </div>
      </div>
      <div>
        <div class="map-wrap">
          <iframe src="https://www.google.com/maps?q=নিরাময়+হাসপাতাল+ফরিদপুর&output=embed" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="NIRAMAYA Hospital Location"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="contact-form" style="max-width:780px;margin:0 auto">
      <h3>আমাদের একটি বার্তা পাঠান</h3>
      <p>আপনার প্রশ্ন বা মতামত আমাদের জানান — আমরা শীঘ্রই উত্তর দিব।</p>
      <form class="form-grid contact-form" novalidate>
        <div class="form-group">
          <label>আপনার নাম <span class="req">*</span></label>
          <input type="text" name="name" placeholder="পূর্ণ নাম" required />
        </div>
        <div class="form-group">
          <label>মোবাইল নম্বর <span class="req">*</span></label>
          <input type="tel" name="phone" placeholder="01XXXXXXXXX" required />
        </div>
        <div class="form-group">
          <label>ইমেইল</label>
          <input type="email" name="email" placeholder="example@mail.com" />
        </div>
        <div class="form-group">
          <label>বিষয় <span class="req">*</span></label>
          <select name="subject" required>
            <option value="">— বিষয় বাছাই করুন —</option>
            <option>অ্যাপয়েন্টমেন্ট সংক্রান্ত</option>
            <option>ডাক্তার সংক্রান্ত</option>
            <option>ডায়াগনস্টিক সংক্রান্ত</option>
            <option>অভিযোগ/পরামর্শ</option>
            <option>অন্যান্য</option>
          </select>
        </div>
        <div class="form-group full">
          <label>আপনার বার্তা <span class="req">*</span></label>
          <textarea name="message" placeholder="আপনার প্রশ্ন বা মতামত লিখুন..." required></textarea>
        </div>
        <div class="form-group full">
          <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;padding:14px;">
            <i class="fa-solid fa-paper-plane"></i> বার্তা পাঠান
          </button>
          <div class="form-success">
            <i class="fa-solid fa-circle-check"></i> ধন্যবাদ! আমরা শীঘ্রই আপনার সাথে যোগাযোগ করব।
          </div>
        </div>
      </form>
    </div>
  </div>
</section>
'''
    return make_page(
        title="যোগাযোগ",
        description="নিরাময় হাসপাতালের ঠিকানা, ফোন, ইমেইল, WhatsApp ও Facebook — ফরিদপুর। ২৪/৭ ইমার্জেন্সি সেবা।",
        active_page="contact",
        body=body,
        page_css=CONTACT_CSS
    )

# =====================================================================
# appointment.html
# =====================================================================
APPT_CSS = r"""
.appointment-wrap{display:grid;grid-template-columns:1fr 1.4fr;gap:0;background:#fff;border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-md);margin-bottom:60px}
.appointment-info{background:linear-gradient(135deg,var(--primary) 0%,var(--primary-dark) 100%);color:#fff;padding:50px 40px}
.appointment-info h2{color:#fff;margin-bottom:14px;font-size:1.5rem}
.appointment-info > p{color:rgba(255,255,255,0.85);margin-bottom:30px;font-size:0.95rem}
.info-list{display:flex;flex-direction:column;gap:18px}
.info-item{display:flex;align-items:flex-start;gap:14px}
.info-item .ic{width:42px;height:42px;background:rgba(255,255,255,0.15);border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:1rem}
.info-item h5{color:#fff;font-size:0.95rem;margin-bottom:2px}
.info-item p{color:rgba(255,255,255,0.85);font-size:0.85rem;margin:0}
.appointment-form-wrap{padding:50px 40px}
.appointment-form-wrap h3{margin-bottom:8px;font-size:1.3rem}
.appointment-form-wrap > p{margin-bottom:30px;font-size:0.95rem;color:var(--text-muted)}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.form-group{display:flex;flex-direction:column;gap:6px}
.form-group.full{grid-column:1 / -1}
.form-group label{font-size:0.88rem;font-weight:500}
.form-group label .req{color:#e74c3c}
.form-group input,.form-group select,.form-group textarea{padding:12px 14px;border:1.5px solid var(--border);border-radius:10px;font-size:0.95rem;background:#fff;transition:all var(--transition)}
.form-group input:focus,.form-group select:focus,.form-group textarea:focus{outline:none;border-color:var(--primary);box-shadow:0 0 0 3px rgba(0,102,164,0.10)}
.form-group textarea{resize:vertical;min-height:100px}
.form-success{display:none;background:var(--accent-light);color:var(--accent-dark);padding:14px 18px;border-radius:10px;margin-top:16px;font-size:0.9rem;border-left:4px solid var(--accent)}
.form-success.show{display:block}
.help-text{font-size:0.85rem;color:var(--text-muted);margin-top:4px}
.quick-options{margin-top:30px;text-align:center}
.quick-options p{color:var(--text-muted);margin-bottom:12px;font-size:0.9rem}
.quick-actions{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
@media (max-width:768px){.appointment-wrap{grid-template-columns:1fr}.appointment-info,.appointment-form-wrap{padding:30px 24px}.form-grid{grid-template-columns:1fr}}
"""

# Use imported DOCTORS for the dropdown
from generate_doctors import DOCTORS as ALL_DOCS

def build_appointment():
    doctor_options = "\n".join(
        f'              <option value="{d["num"]}">{d["name"]} — {d["dept"]}</option>'
        for d in ALL_DOCS
    )
    body = f'''
<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <span class="hero-eyebrow"><i class="fa-regular fa-calendar-check"></i> অ্যাপয়েন্টমেন্ট</span>
      <h1>অনলাইন অ্যাপয়েন্টমেন্ট</h1>
      <p>২ মিনিটে ফর্ম পূরণ করুন — ফোনে কনফার্মেশন ১০ মিনিটের মধ্যে</p>
    </div>
  </div>
</section>

<div class="breadcrumb">
  <div class="container">
    <a href="index.html">হোম</a> <span class="sep">›</span>
    <span class="current">অ্যাপয়েন্টমেন্ট</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="appointment-wrap">
      <div class="appointment-info">
        <h2>অ্যাপয়েন্টমেন্ট নিন</h2>
        <p>আপনার পছন্দের ডাক্তার ও সময় বেছে নিয়ে নিচের ফর্মটি পূরণ করুন — আমরা ফোনে নিশ্চিত করব।</p>
        <div class="info-list">
          <div class="info-item">
            <div class="ic"><i class="fa-solid fa-phone"></i></div>
            <div>
              <h5>মূল ফোন</h5>
              <p><a href="tel:+8801729171549" style="color:rgba(255,255,255,0.85);">+৮৮০১৭২৯-১৭১৫৪৯</a></p>
            </div>
          </div>
          <div class="info-item">
            <div class="ic"><i class="fa-solid fa-truck-medical"></i></div>
            <div>
              <h5>ইমার্জেন্সি (২৪/৭)</h5>
              <p><a href="tel:+8801731827110" style="color:rgba(255,255,255,0.85);">+৮৮০১৭৩১-৮২৭১১০</a></p>
            </div>
          </div>
          <div class="info-item">
            <div class="ic"><i class="fa-brands fa-whatsapp"></i></div>
            <div>
              <h5>WhatsApp-এ বুক করুন</h5>
              <p><a href="https://wa.me/8801729171549" style="color:rgba(255,255,255,0.85);">দ্রুত অ্যাপয়েন্টমেন্ট</a></p>
            </div>
          </div>
          <div class="info-item">
            <div class="ic"><i class="fa-solid fa-location-dot"></i></div>
            <div>
              <h5>ঠিকানা</h5>
              <p>নিরাময় ভবন, পশ্চিম খাবাসপুর, ফরিদপুর</p>
            </div>
          </div>
        </div>
      </div>
      <div class="appointment-form-wrap">
        <h3>অনলাইন অ্যাপয়েন্টমেন্ট ফর্ম</h3>
        <p>আপনার তথ্য দিন — আমরা ফোনে নিশ্চিত করব।</p>
        <form class="form-grid appointment-form" id="appointmentForm" novalidate>
          <div class="form-group">
            <label>আপনার নাম <span class="req">*</span></label>
            <input type="text" name="name" placeholder="পূর্ণ নাম" required />
          </div>
          <div class="form-group">
            <label>মোবাইল নম্বর <span class="req">*</span></label>
            <input type="tel" name="phone" placeholder="01XXXXXXXXX" required />
          </div>
          <div class="form-group">
            <label>বয়স</label>
            <input type="number" name="age" placeholder="বয়স" min="0" max="120" />
          </div>
          <div class="form-group">
            <label>লিঙ্গ</label>
            <select name="gender">
              <option value="">— বাছাই করুন —</option>
              <option>পুরুষ</option>
              <option>মহিলা</option>
              <option>অন্যান্য</option>
            </select>
          </div>
          <div class="form-group">
            <label>বিভাগ <span class="req">*</span></label>
            <select name="department" required>
              <option value="">— বিভাগ বাছাই করুন —</option>
              <option>মেডিসিন</option>
              <option>সার্জারি</option>
              <option>গাইনি ও প্রসূতি</option>
              <option>অর্থোপেডিক্স</option>
              <option>ইএনটি</option>
              <option>চর্ম ও যৌন</option>
              <option>জেনারেল প্র্যাকটিশনার</option>
              <option>আল্ট্রাসনোগ্রাফি</option>
            </select>
          </div>
          <div class="form-group">
            <label>পছন্দের ডাক্তার <span class="req">*</span></label>
            <select name="doctor" id="doctorSelect" required>
              <option value="">— ডাক্তার বাছাই করুন —</option>
{doctor_options}
            </select>
          </div>
          <div class="form-group">
            <label>পছন্দের তারিখ <span class="req">*</span></label>
            <input type="date" name="date" required />
          </div>
          <div class="form-group">
            <label>পছন্দের সময়</label>
            <select name="time">
              <option>সকাল (৯টা - দুপুর ১টা)</option>
              <option>বিকাল (৩টা - সন্ধ্যা ৬টা)</option>
              <option>সন্ধ্যা (৬টা - রাত ৯টা)</option>
            </select>
          </div>
          <div class="form-group full">
            <label>অতিরিক্ত তথ্য / সমস্যা</label>
            <textarea name="message" placeholder="আপনার সমস্যা সংক্ষেপে লিখুন (ঐচ্ছিক)"></textarea>
          </div>
          <div class="form-group full">
            <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;padding:14px;">
              <i class="fa-solid fa-paper-plane"></i> অ্যাপয়েন্টমেন্ট জমা দিন
            </button>
            <div class="form-success" id="formSuccess">
              <i class="fa-solid fa-circle-check"></i> ধন্যবাদ! আমরা শীঘ্রই যোগাযোগ করব।
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="quick-options">
      <p>অথবা সরাসরি যোগাযোগ করুন</p>
      <div class="quick-actions">
        <a href="tel:+8801729171549" class="btn btn-primary"><i class="fa-solid fa-phone"></i> ০১৭২৯-১৭১৫৪৯</a>
        <a href="tel:+8801731827110" class="btn btn-accent"><i class="fa-solid fa-truck-medical"></i> ০১৭৩১-৮২৭১১০ (২৪/৭)</a>
        <a href="https://wa.me/8801729171549" target="_blank" rel="noopener" class="btn btn-outline"><i class="fa-brands fa-whatsapp"></i> WhatsApp</a>
        <a href="doctors.html" class="btn btn-ghost"><i class="fa-solid fa-user-doctor"></i> ডাক্তারগণ দেখুন</a>
      </div>
    </div>
  </div>
</section>
'''
    return make_page(
        title="অ্যাপয়েন্টমেন্ট",
        description="নিরাময় হাসপাতালে অনলাইন অ্যাপয়েন্টমেন্ট নিন — ২ মিনিটে ফর্ম পূরণ করুন, ১০ মিনিটে ফোনে কনফার্মেশন।",
        active_page="appointment",
        body=body,
        page_css=APPT_CSS
    )

# =====================================================================
# Build all 5
# =====================================================================

builds = [
    ("services.html",    build_services),
    ("diagnostic.html",  build_diagnostic),
    ("gallery.html",     build_gallery),
    ("contact.html",     build_contact),
    ("appointment.html", build_appointment),
]

for filename, fn in builds:
    out = os.path.join(WEB, filename)
    with open(out, "w", encoding="utf-8") as f:
        f.write(fn())
    print(f"  [OK] {out} ({os.path.getsize(out):,} bytes)")
