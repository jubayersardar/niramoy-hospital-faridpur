# -*- coding: utf-8 -*-
"""Build doctors.html — all 14 doctors with filter pills."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_site import (
    TOPBAR, FOOTER, FAB, HEAD_BASE, SCRIPTS, NAV,
    make_header, make_page, WEB, PAGES, DOCTORS, DEPT_COLOR
)
# Reuse doctor_card_v2 by importing from build_site if available; otherwise inline
try:
    from build_site import doctor_card_v2
except ImportError:
    DOCTOR_SLUGS = {
        "01": "abu-bakar",   "02": "riyad-bappy", "03": "shrabanti",
        "04": "moin-uddin",  "05": "shashank-nag","06": "rafiqul-islam",
        "07": "utpal-nag",   "08": "sourav",      "09": "nahid-badsha",
        "10": "harichand-shil","11": "imtiaz-uddin","12": "papri-sarker",
        "13": "nurul-alam",  "14": "shankar-dey",
    }
    def doctor_card_v2(d):
        n = d["num"]; name = d["name"]; deg = d["deg_short"]
        desig = d["desig"]; spec = d["spec"]
        initial = d["initial"]; dept_class = d["dept_class"]; dept = d["dept"]
        slug = DOCTOR_SLUGS.get(n, "")
        import os
        img_path = f"images/doctors/{n}-{slug}.jpg"
        for ext in ('jpg', 'png', 'jpeg', 'webp'):
            p = os.path.join(WEB, "images", "doctors", f"{n}-{slug}.{ext}")
            if os.path.isfile(p):
                img_path = f"images/doctors/{n}-{slug}.{ext}"
                break
        return f'''      <div class="doctor-card reveal">
        <a href="doctors/{n}.html" class="doctor-photo-link" aria-label="প্রোফাইল দেখুন">
          <div class="doctor-photo bg-{dept_class}">
            <span class="dept-tag">{dept}</span>
            <img src="{img_path}" alt="{name}" style="width:160px;height:160px;border-radius:50%;object-fit:cover;border:5px solid rgba(255,255,255,0.30);" onerror="this.style.display='none';var n=this.nextElementSibling;if(n)n.style.display='flex';" />
            <div class="avatar" style="display:none;">{initial}</div>
          </div>
        </a>
        <div class="doctor-info">
          <h3>{name}</h3>
          <p class="deg">{deg}</p>
          <p class="designation">{desig}</p>
          <p class="affiliation">বিশেষজ্ঞ: {spec}</p>
          <div class="doctor-actions">
            <a href="doctors/{n}.html" class="btn btn-ghost"><i class="fa-solid fa-user-doctor"></i> প্রোফাইল</a>
            <a href="appointment.html?doctor={n}" class="btn btn-primary"><i class="fa-regular fa-calendar-check"></i> অ্যাপয়েন্টমেন্ট</a>
          </div>
        </div>
      </div>
'''

DOCTORS_CSS = r"""
.doctors-section{background:#fff}
.doctors-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}
.doctor-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;transition:all var(--transition);display:flex;flex-direction:column}
.doctor-card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);border-color:rgba(0,102,164,0.25)}
.doctor-photo{position:relative;height:240px;display:flex;align-items:center;justify-content:center;overflow:hidden;color:#fff}
.doctor-photo .dept-tag{position:absolute;top:14px;left:14px;background:rgba(255,255,255,0.95);color:var(--text);padding:5px 12px;border-radius:50px;font-size:0.72rem;font-weight:600;box-shadow:var(--shadow-sm)}
.doctor-photo .avatar{width:160px;height:160px;border-radius:50%;background:rgba(255,255,255,0.15);border:5px solid rgba(255,255,255,0.30);display:flex;align-items:center;justify-content:center;font-size:3.5rem;font-weight:700;color:#fff;backdrop-filter:blur(4px);box-shadow:0 12px 30px rgba(0,0,0,0.20)}
.doctor-info{padding:22px;flex:1;display:flex;flex-direction:column}
.doctor-info h3{font-size:1.12rem;margin-bottom:6px;line-height:1.35}
.doctor-info .deg{color:var(--primary);font-size:0.82rem;font-weight:600;margin-bottom:8px;line-height:1.4}
.doctor-info .designation{color:var(--text);font-size:0.86rem;font-weight:500;margin-bottom:6px}
.doctor-info .affiliation{color:var(--text-muted);font-size:0.82rem;margin-bottom:14px;line-height:1.5;padding-bottom:14px;border-bottom:1px dashed var(--border);flex:1}
.doctor-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:auto}
.doctor-actions .btn{margin-top:0;flex:1;min-width:120px;padding:10px 14px;font-size:0.82rem}
.doctor-photo-link{display:block;position:relative;color:inherit}
.doctor-photo-link:hover{color:inherit}
.doctor-photo-link::after{content:"\f0f4";font-family:"Font Awesome 6 Free";font-weight:900;position:absolute;top:14px;right:14px;width:36px;height:36px;background:rgba(255,255,255,0.95);color:var(--primary);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.9rem;box-shadow:0 2px 8px rgba(0,0,0,0.15);transition:all var(--transition)}
.doctor-photo-link:hover::after{background:var(--primary);color:#fff;transform:scale(1.08) rotate(-8deg)}
.filter-pills{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:36px}
.filter-pill{padding:8px 18px;border-radius:50px;background:#fff;border:1.5px solid var(--border);color:var(--text-muted);font-weight:600;font-size:0.88rem;cursor:pointer;transition:all var(--transition)}
.filter-pill:hover{border-color:var(--primary);color:var(--primary)}
.filter-pill.active{background:var(--primary);color:#fff;border-color:var(--primary);box-shadow:0 4px 12px rgba(0,102,164,0.25)}
.bg-med{background:linear-gradient(135deg,#0066a4 0%,#004a7a 100%)}
.bg-surg{background:linear-gradient(135deg,#34495e 0%,#1a2530 100%)}
.bg-gynae{background:linear-gradient(135deg,#c2185b 0%,#880e4f 100%)}
.bg-ortho{background:linear-gradient(135deg,#e67e22 0%,#a04000 100%)}
.bg-ent{background:linear-gradient(135deg,#16a085 0%,#0e6655 100%)}
.bg-derma{background:linear-gradient(135deg,#d35400 0%,#a04000 100%)}
.bg-gp{background:linear-gradient(135deg,#00a86b 0%,#008755 100%)}
.bg-sono{background:linear-gradient(135deg,#2980b9 0%,#1a5276 100%)}
@media (max-width:768px){.doctor-photo{height:200px}.doctor-photo .avatar{width:130px;height:130px;font-size:3rem}}
"""

def build_doctors():
    cards = "\n".join(doctor_card_v2(d) for d in DOCTORS)
    body = f'''
<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <span class="hero-eyebrow"><i class="fa-solid fa-user-doctor"></i> ১৪+ বিশেষজ্ঞ চিকিৎসক</span>
      <h1>আমাদের ডাক্তারগণ</h1>
      <p>ফরিদপুরের স্বনামধন্য প্রতিষ্ঠানের অভিজ্ঞ বিশেষজ্ঞ চিকিৎসক — সব বিভাগে</p>
    </div>
  </div>
</section>

<div class="breadcrumb">
  <div class="container">
    <a href="index.html">হোম</a> <span class="sep">›</span>
    <span class="current">ডাক্তারগণ</span>
  </div>
</div>

<section class="doctors-section section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">বিশেষজ্ঞ</span>
      <h2 class="section-title">আমাদের <span class="gradient-text">১৪ জন বিশেষজ্ঞ</span></h2>
      <p class="section-subtitle">কার্ডে ক্লিক করে প্রোফাইল দেখুন, সরাসরি অ্যাপয়েন্টমেন্ট নিন</p>
    </div>
    <div class="filter-pills" id="filterPills">
      <span class="filter-pill active" data-filter="all">সকল ({len(DOCTORS)})</span>
      <span class="filter-pill" data-filter="med">মেডিসিন</span>
      <span class="filter-pill" data-filter="surg">সার্জারি</span>
      <span class="filter-pill" data-filter="gynae">গাইনি</span>
      <span class="filter-pill" data-filter="ortho">অর্থোপেডিক্স</span>
      <span class="filter-pill" data-filter="ent">ইএনটি</span>
      <span class="filter-pill" data-filter="derma">চর্ম ও যৌন</span>
      <span class="filter-pill" data-filter="gp">জেনারেল</span>
      <span class="filter-pill" data-filter="sono">আল্ট্রাসনোগ্রাফি</span>
    </div>
    <div class="doctors-grid" id="doctorsGrid">
{cards}
    </div>
  </div>
</section>
'''
    return make_page(
        title="ডাক্তারগণ",
        description="নিরাময় হাসপাতালের ১৪+ বিশেষজ্ঞ চিকিৎসক — মেডিসিন, সার্জারি, গাইনি, অর্থোপেডিক্স, ইএনটি, চর্ম ও যৌন, জেনারেল প্র্যাকটিশনার ও আল্ট্রাসনোগ্রাফি বিশেষজ্ঞ।",
        active_page="doctors",
        body=body,
        page_css=DOCTORS_CSS
    )


print("Building doctors.html...")
out = os.path.join(WEB, "doctors.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(build_doctors())
print(f"  [OK] {out} ({os.path.getsize(out):,} bytes)")
