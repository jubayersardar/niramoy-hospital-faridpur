# -*- coding: utf-8 -*-
"""Build remaining 8 pages of NIRAMAYA site."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

# Reuse common partials & helpers from build_site
from build_site import (
    TOPBAR, FOOTER, FAB, HEAD_BASE, SCRIPTS, NAV,
    make_header, make_page, WEB, PAGES, DOCTORS
)

ABOUT_CSS = r"""
.about-hero-image{margin-top:40px}
.about-section{margin-bottom:60px}
.about-section h2{font-size:1.6rem;margin-bottom:18px;color:var(--primary)}
.about-section p{color:var(--text-muted);margin-bottom:14px;font-size:1rem;line-height:1.8}
.about-section ul{margin:14px 0;padding-left:0;list-style:none}
.about-section ul li{padding:8px 0 8px 28px;position:relative;color:var(--text-muted);font-size:0.98rem}
.about-section ul li::before{content:"\f00c";font-family:"Font Awesome 6 Free";font-weight:900;color:var(--accent);position:absolute;left:0;top:8px}
.mv-grid{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:30px}
.mv-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:30px;box-shadow:var(--shadow-sm);position:relative;overflow:hidden}
.mv-card::before{content:"";position:absolute;top:0;left:0;width:4px;height:100%;background:linear-gradient(180deg,var(--primary),var(--accent))}
.mv-card .mv-icon{width:50px;height:50px;border-radius:14px;background:var(--primary-light);color:var(--primary);display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:14px}
.mv-card h3{font-size:1.3rem;margin-bottom:10px;color:var(--primary)}
.mv-card p{color:var(--text-muted);font-size:0.95rem;margin:0}
.founder-card{background:linear-gradient(135deg,var(--bg-soft) 0%,#fff 100%);border:1px solid var(--border);border-radius:var(--radius-lg);padding:40px;display:grid;grid-template-columns:200px 1fr;gap:30px;align-items:center;box-shadow:var(--shadow-sm)}
.founder-image{width:200px;height:200px;border-radius:50%;background:linear-gradient(135deg,var(--primary) 0%,var(--primary-dark) 100%);display:flex;align-items:center;justify-content:center;font-size:5rem;color:#fff;font-weight:700;flex-shrink:0;box-shadow:var(--shadow-md)}
.founder-card h3{font-size:1.4rem;margin-bottom:6px}
.founder-card .founder-role{color:var(--accent);font-weight:600;font-size:0.92rem;margin-bottom:14px}
.founder-card p{color:var(--text-muted);font-size:0.95rem;margin:0}
.stats-grid-2{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px;margin-top:30px}
.stat-block{background:linear-gradient(135deg,var(--primary-light) 0%,#fff 100%);border-radius:var(--radius);padding:24px;text-align:center;border:1px solid var(--border)}
.stat-block .n{font-size:2rem;font-weight:800;color:var(--primary);line-height:1}
.stat-block p{color:var(--text-muted);font-size:0.88rem;margin:8px 0 0}
.timeline{position:relative;margin:40px 0;padding-left:30px}
.timeline::before{content:"";position:absolute;left:8px;top:0;bottom:0;width:2px;background:linear-gradient(180deg,var(--primary),var(--accent))}
.timeline-item{position:relative;padding-bottom:30px}
.timeline-item::before{content:"";position:absolute;left:-26px;top:6px;width:14px;height:14px;border-radius:50%;background:var(--accent);border:3px solid #fff;box-shadow:0 0 0 3px var(--accent)}
.timeline-year{color:var(--primary);font-weight:700;font-size:1.05rem;margin-bottom:6px}
.timeline-content h4{font-size:1.05rem;margin-bottom:6px}
.timeline-content p{color:var(--text-muted);font-size:0.92rem;margin:0}
@media (max-width:768px){.mv-grid,.founder-card{grid-template-columns:1fr}.founder-image{margin:0 auto}}
"""

def build_about():
    body = '''
<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <span class="hero-eyebrow"><i class="fa-solid fa-hospital"></i> আমাদের সম্পর্কে</span>
      <h1>নিরাময় হাসপাতালের গল্প</h1>
      <p>১৯৯৯ সাল থেকে ফরিদপুরবাসীর সেবায় নিবেদিত — আধুনিক চিকিৎসা, অভিজ্ঞ বিশেষজ্ঞ ও নির্ভরযোগ্য ডায়াগনস্টিক সেবা।</p>
    </div>
  </div>
</section>

<div class="breadcrumb">
  <div class="container">
    <a href="index.html">হোম</a> <span class="sep">›</span>
    <span class="current">আমাদের সম্পর্কে</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="about-section">
      <h2>আমাদের পরিচয়</h2>
      <p><strong>নিরাময় হাসপাতাল এন্ড ডায়াগনস্টিক সেন্টার (প্রা:)</strong> ফরিদপুর শহরের নিরাময় ভবন, পশ্চিম খাবাসপুরে অবস্থিত একটি স্বনামধন্য স্বয়ংসম্পূর্ণ বেসরকারি হাসপাতাল। ১৯৯৯ সালে প্রতিষ্ঠিত এই প্রতিষ্ঠানটি প্রায় ২৫ বছর ধরে ফরিদপুর ও আশেপাশের জেলার মানুষের স্বাস্থ্যসেবায় নিয়োজিত।</p>
      <p>বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুরের মতো প্রতিষ্ঠানের স্বনামধন্য বিশেষজ্ঞ চিকিৎসকগণ আমাদের এখানে নিয়মিত রোগী দেখেন। আমাদের ১৪+ বিশেষজ্ঞ চিকিৎসক সব বিভাগে সেবা দিচ্ছেন এবং ২৪/৭ ইমার্জেন্সি সেবা চালু রয়েছে।</p>
      <ul>
        <li>অভিজ্ঞ বিশেষজ্ঞ চিকিৎসক ও সার্জন</li>
        <li>আধুনিক ডায়াগনস্টিক ও প্যাথলজি ল্যাব</li>
        <li>২৪/৭ ইমার্জেন্সি ও অ্যাম্বুলেন্স</li>
        <li>সাশ্রয়ী মূল্যে মানসম্মত চিকিৎসা</li>
        <li>পরিচ্ছন্ন ও রোগী-বান্ধব পরিবেশ</li>
        <li>সরকার অনুমোদিত প্রতিষ্ঠান</li>
      </ul>
    </div>

    <div class="stats-grid-2">
      <div class="stat-block reveal"><div class="n">১৯৯৯</div><p>প্রতিষ্ঠাকাল</p></div>
      <div class="stat-block reveal"><div class="n">২৫+</div><p>বছরের অভিজ্ঞতা</p></div>
      <div class="stat-block reveal"><div class="n">১৪+</div><p>বিশেষজ্ঞ চিকিৎসক</p></div>
      <div class="stat-block reveal"><div class="n">১,০০,০০০+</div><p>সেবা প্রাপ্ত রোগী</p></div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">আমাদের লক্ষ্য</span>
      <h2 class="section-title">মিশন ও <span class="gradient-text">ভিশন</span></h2>
    </div>
    <div class="mv-grid">
      <div class="mv-card reveal">
        <div class="mv-icon"><i class="fa-solid fa-bullseye"></i></div>
        <h3>আমাদের মিশন</h3>
        <p>ফরিদপুর ও আশেপাশের এলাকার মানুষের কাছে সাশ্রয়ী মূল্যে আধুনিক ও মানসম্মত স্বাস্থ্যসেবা পৌঁছে দেওয়া। রোগীর প্রতি সহমর্মিতা, সঠিক রোগ নির্ণয় ও সময়মত চিকিৎসাই আমাদের মূল লক্ষ্য।</p>
      </div>
      <div class="mv-card reveal">
        <div class="mv-icon"><i class="fa-solid fa-eye"></i></div>
        <h3>আমাদের ভিশন</h3>
        <p>ফরিদপুর বিভাগের সেরা স্বাস্থ্যসেবা প্রতিষ্ঠান হিসেবে নিজেদের প্রতিষ্ঠিত করা — যেখানে প্রতিটি রোগী পাবেন বিশ্বমানের চিকিৎসা, সহানুভূতিশীল সেবা এবং সম্মানজনক পরিবেশ।</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">প্রতিষ্ঠাতা</span>
      <h2 class="section-title">আমাদের <span class="gradient-text">প্রতিষ্ঠাতা</span></h2>
    </div>
    <div class="founder-card reveal">
      <div class="founder-image">কু</div>
      <div>
        <h3>মোহাম্মদ কুব্বাত বিশ্বাস</h3>
        <p class="founder-role"><i class="fa-solid fa-user-tie"></i> প্রতিষ্ঠাতা, নিরাময় হাসপাতাল</p>
        <p>ফরিদপুরের স্বাস্থ্যসেবার উন্নয়নে দীর্ঘদিনের স্বপ্ন বাস্তবায়নে ১৯৯৯ সালে প্রতিষ্ঠা করেন নিরাময় হাসপাতাল। তাঁর দূরদর্শী নেতৃত্ব ও অদম্য পরিশ্রমের ফলে আজ এটি ফরিদপুরের অন্যতম বিশ্বস্ত স্বাস্থ্যসেবা প্রতিষ্ঠান। তিনি বিশ্বাস করেন, মানসম্মত চিকিৎসা সবার অধিকার এবং সেটা সবার আওতায় পৌঁছে দেওয়াই একটি স্বাস্থ্যসেবা প্রতিষ্ঠানের মূল দায়িত্ব।</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">যাত্রা</span>
      <h2 class="section-title">আমাদের <span class="gradient-text">যাত্রা</span></h2>
      <p class="section-subtitle">১৯৯৯ সাল থেকে আজ পর্যন্ত ফরিদপুরবাসীর সেবায়</p>
    </div>
    <div class="timeline">
      <div class="timeline-item">
        <div class="timeline-year">১৯৯৯</div>
        <div class="timeline-content">
          <h4>প্রতিষ্ঠা</h4>
          <p>মোহাম্মদ কুব্বাত বিশ্বাস নিরাময় হাসপাতাল প্রতিষ্ঠা করেন ফরিদপুরের পশ্চিম খাবাসপুরে।</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">২০০৫</div>
        <div class="timeline-content">
          <h4>ডায়াগনস্টিক সেবা সম্প্রসারণ</h4>
          <p>আধুনিক প্যাথলজি ও ডায়াগনস্টিক ল্যাব যোগ করা হয়।</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">২০১০</div>
        <div class="timeline-content">
          <h4>বিশেষজ্ঞ চিকিৎসক যোগদান</h4>
          <p>বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতালের বিশেষজ্ঞ চিকিৎসকগণ নিয়মিত রোগী দেখা শুরু করেন।</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">২০১৮</div>
        <div class="timeline-content">
          <h4>ইমার্জেন্সি ২৪/৭ চালু</h4>
          <p>সার্বক্ষণিক ইমার্জেন্সি ও অ্যাম্বুলেন্স সেবা চালু হয়।</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">২০২৪</div>
        <div class="timeline-content">
          <h4>১৪+ বিশেষজ্ঞ</h4>
          <p>আজ আমাদের ১৪+ বিশেষজ্ঞ চিকিৎসক ৮+ বিভাগে নিয়মিত সেবা দিচ্ছেন।</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">পরবর্তী</span>
      <h2 class="section-title">আরও <span class="gradient-text">জানুন</span></h2>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center">
      <a href="doctors.html" class="btn btn-primary"><i class="fa-solid fa-user-doctor"></i> ডাক্তারগণ</a>
      <a href="departments.html" class="btn btn-outline"><i class="fa-solid fa-th-large"></i> বিভাগসমূহ</a>
      <a href="services.html" class="btn btn-outline"><i class="fa-solid fa-hand-holding-medical"></i> সেবাসমূহ</a>
      <a href="contact.html" class="btn btn-outline"><i class="fa-solid fa-location-dot"></i> যোগাযোগ</a>
    </div>
  </div>
</section>
'''
    return make_page(
        title="আমাদের সম্পর্কে",
        description="নিরাময় হাসপাতালের ইতিহাস, মিশন, ভিশন ও প্রতিষ্ঠাতার গল্প। ১৯৯৯ সাল থেকে ফরিদপুরবাসীর সেবায়।",
        active_page="about",
        body=body,
        page_css=ABOUT_CSS
    )


print("Building about.html...")
out = os.path.join(WEB, "about.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(build_about())
print(f"  [OK] {out} ({os.path.getsize(out):,} bytes)")
