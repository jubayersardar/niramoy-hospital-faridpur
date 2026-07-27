# -*- coding: utf-8 -*-
"""Build complete NIRAMAYA Hospital index.html from scratch."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from generate_doctors import DOCTORS, DEPT_COLOR

OUT = r"D:\minimax\New folder\website\index.html"

DEPT_LIST = [
    ("med",    "মেডিসিন",      "মেডিসিন বিশেষজ্ঞ পরামর্শ, ডায়াবেটিস, উচ্চ রক্তচাপ, হৃদরোগ"),
    ("surg",   "সার্জারি",     "জেনারেল ও ল্যাপারোস্কোপিক সার্জারি, কলোরেক্টাল, ইউরোলজি"),
    ("gynae",  "গাইনি ও প্রসূতি", "বন্ধ্যাত্ব, নরমাল ও সিজারিয়ান ডেলিভারি, মাসিক সমস্যা"),
    ("ortho",  "অর্থোপেডিক্স",   "হাড়-জোড়া, ফ্র্যাকচার, ট্রমা, বাতব্যথা, স্পোর্টস ইনজুরি"),
    ("ent",    "ইএনটি",         "নাক-কান-গলা, টনসিল, সাইনাস, হেড-নেক সার্জারি"),
    ("derma",  "চর্ম ও যৌন",   "এক্সিমা, সোরিয়াসিস, এলার্জি, যৌন রোগ, ব্রণ"),
    ("gp",     "জেনারেল প্র্যাকটিশনার", "সব ধরনের সাধারণ রোগ, শিশু, মাইনর সার্জারি"),
    ("sono",   "আল্ট্রাসনোগ্রাফি", "সম্পূর্ণ USG, গর্ভাবস্থা, কিডনি-লিভার"),
]

def render_doctor_card(d):
    n = d["num"]; name = d["name"]; deg = d["deg_short"]
    desig = d["desig"]; affil = d["affil"]; spec = d["spec"]
    initial = d["initial"]; dept_class = d["dept_class"]; dept = d["dept"]
    return f'''      <div class="doctor-card reveal">
        <a href="doctors/{n}.html" class="doctor-photo-link" aria-label="প্রোফাইল দেখুন">
          <div class="doctor-photo bg-{dept_class}">
            <span class="dept-tag">{dept}</span>
            <div class="avatar">{initial}</div>
          </div>
        </a>
        <div class="doctor-info">
          <h3>{name}</h3>
          <p class="deg">{deg}</p>
          <p class="designation">{desig}</p>
          <p class="affiliation">{affil}<br/>বিশেষজ্ঞ: {spec}</p>
          <div class="doctor-actions">
            <a href="#appointment" class="btn btn-primary"><i class="fa-regular fa-calendar-check"></i> অ্যাপয়েন্টমেন্ট</a>
            <a href="doctors/{n}.html" class="btn btn-ghost"><i class="fa-solid fa-user-doctor"></i> প্রোফাইল</a>
          </div>
        </div>
      </div>
'''

DOCTOR_CARDS = "\n".join(render_doctor_card(d) for d in DOCTORS)

def render_dept_card(cls, name, desc):
    return f'''      <a href="#doctors" class="dept-card" data-aos="zoom-in" data-aos-delay="50">
        <div class="dept-icon bg-{cls}"><i class="fa-solid fa-stethoscope"></i></div>
        <h3>{name}</h3>
        <p>{desc}</p>
        <span class="dept-link">বিশেষজ্ঞ দেখুন <i class="fas fa-arrow-right"></i></span>
      </a>
'''
DEPT_CARDS = "\n".join(render_dept_card(*d) for d in DEPT_LIST)

# Use plain string with % format for substitution to avoid f-string brace conflicts
CSS_BLOCK = r"""
:root{--primary:#0066a4;--primary-dark:#004a7a;--primary-light:#e6f1f9;--accent:#00a86b;--accent-dark:#008755;--accent-light:#e6f7ef;--text:#1a2b3c;--text-muted:#5a6b7b;--bg:#fff;--bg-soft:#f4f8fc;--border:#e2eaf2;--shadow-sm:0 2px 8px rgba(0,80,130,0.06);--shadow-md:0 8px 24px rgba(0,80,130,0.10);--shadow-lg:0 18px 48px rgba(0,80,130,0.14);--radius:12px;--radius-lg:20px;--transition:0.3s ease;--container:1240px}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Hind Siliguri','Poppins',sans-serif;color:var(--text);background:var(--bg);line-height:1.7;-webkit-font-smoothing:antialiased}
img,svg{max-width:100%;display:block}
a{color:inherit;text-decoration:none;transition:color var(--transition)}
a:hover{color:var(--primary)}
button{font-family:inherit;cursor:pointer;border:none;background:none}
ul{list-style:none}
input,select,textarea{font-family:inherit;font-size:1rem}
h1,h2,h3,h4,h5,h6{font-weight:700;line-height:1.3;color:var(--text)}
.container{width:100%;max-width:var(--container);margin:0 auto;padding:0 20px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:50px;font-weight:600;font-size:0.95rem;transition:all var(--transition);white-space:nowrap;cursor:pointer}
.btn-primary{background:var(--primary);color:#fff;box-shadow:0 6px 18px rgba(0,102,164,0.30)}
.btn-primary:hover{background:var(--primary-dark);color:#fff;transform:translateY(-2px)}
.btn-accent{background:var(--accent);color:#fff;box-shadow:0 6px 18px rgba(0,168,107,0.30)}
.btn-accent:hover{background:var(--accent-dark);color:#fff;transform:translateY(-2px)}
.btn-ghost{background:var(--primary-light);color:var(--primary)}
.btn-ghost:hover{background:var(--primary);color:#fff}
.btn-outline{background:transparent;border:2px solid var(--primary);color:var(--primary)}
.btn-outline:hover{background:var(--primary);color:#fff}

.topbar{background:linear-gradient(90deg,var(--primary-dark) 0%,var(--primary) 100%);color:#fff;font-size:0.88rem;padding:8px 0}
.topbar-inner{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
.topbar-left,.topbar-right{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.topbar-item{display:inline-flex;align-items:center;gap:6px}
.topbar-item a{color:#fff}
.emergency-badge{background:var(--accent);color:#fff;padding:4px 12px;border-radius:50px;font-weight:600;font-size:0.8rem;display:inline-flex;align-items:center;gap:6px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(0,168,107,0.5)}50%{box-shadow:0 0 0 8px rgba(0,168,107,0)}}
.topbar-badge{background:rgba(255,255,255,0.15);padding:4px 14px;border-radius:50px;font-size:0.85rem;border:1px solid rgba(255,255,255,0.20)}
.topbar-badge strong{color:#fff}
.topbar-item a strong{color:#fff;font-weight:700}
.topbar-social{display:inline-flex;gap:8px}
.topbar-social a{width:28px;height:28px;display:inline-flex;align-items:center;justify-content:center;background:rgba(255,255,255,0.12);border-radius:50%;color:#fff;font-size:0.85rem}
.topbar-social a:hover{background:var(--accent)}

.header{background:#fff;position:sticky;top:0;z-index:1000;box-shadow:var(--shadow-sm)}
.header-inner{display:flex;align-items:center;justify-content:space-between;padding:14px 0;gap:24px}
.logo{display:flex;align-items:center;gap:12px;font-weight:700}
.logo-mark{width:54px;height:54px;background:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:var(--shadow-sm);flex-shrink:0;overflow:hidden;border:1px solid var(--border)}
.logo-mark img{width:48px;height:48px;object-fit:contain}
.logo-text{display:flex;flex-direction:column;line-height:1.15}
.logo-text .bn{font-size:1.05rem;font-weight:700;color:var(--text)}
.logo-text .en{font-size:0.75rem;color:var(--text-muted);letter-spacing:0.5px;text-transform:uppercase}
.nav-list{display:flex;align-items:center;gap:4px}
.nav-item{position:relative}
.nav-link{display:inline-block;padding:10px 16px;font-weight:500;color:var(--text);font-size:0.95rem;border-radius:8px;transition:all var(--transition)}
.nav-link:hover,.nav-link.active{color:var(--primary);background:var(--primary-light)}
.menu-toggle{display:none;width:44px;height:44px;background:var(--primary-light);color:var(--primary);border-radius:8px;font-size:1.2rem;align-items:center;justify-content:center}

.hero-clean {
  position: relative;
  background: #001a33;
  color: #fff;
  overflow: hidden;
  padding: 85px 0 115px;
  text-align: center;
}
.hero-bg-slides {
  position: absolute;
  inset: 0;
  z-index: 0;
}
.hero-bg-slide {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transition: opacity 1.2s cubic-bezier(0.4, 0, 0.2, 1), transform 8s ease-out;
  transform: scale(1.05);
}
.hero-bg-slide.active {
  opacity: 1;
  transform: scale(1);
}
.hero-bg-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, 
    rgba(0, 18, 36, 0.48) 0%, 
    rgba(0, 24, 46, 0.30) 50%, 
    rgba(0, 18, 36, 0.58) 100%
  );
  z-index: 1;
}
.hero-clean-container {
  position: relative;
  z-index: 2;
  max-width: 920px;
  margin: 0 auto;
}
.hero-top-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.18);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.35);
  color: #ffffff;
  padding: 8px 22px;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
}
.hero-clean-title {
  font-size: clamp(2.2rem, 5vw, 3.4rem);
  font-weight: 800;
  color: #ffffff;
  line-height: 1.2;
  margin-bottom: 18px;
  letter-spacing: -0.5px;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.7), 0 4px 25px rgba(0, 0, 0, 0.5);
}
.hero-clean-lead {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: rgba(255, 255, 255, 0.95);
  line-height: 1.7;
  max-width: 780px;
  margin: 0 auto 32px;
  font-weight: 500;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
}
.hero-clean-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 35px;
}
.btn-phone-pill {
  background: rgba(255, 255, 255, 0.95);
  color: var(--text);
  border-radius: 50px;
  font-weight: 700;
  padding: 13px 26px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}
.btn-phone-pill:hover {
  background: #ffffff;
  color: var(--primary);
  transform: translateY(-2px);
}
.hero-nav-arrow {
  position: absolute;
  top: 45%;
  transform: translateY(-50%);
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.20);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.35);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  z-index: 5;
  cursor: pointer;
  transition: all 0.3s ease;
}
.hero-nav-arrow:hover {
  background: var(--accent);
  border-color: var(--accent);
}
.hero-nav-arrow.prev { left: 25px; }
.hero-nav-arrow.next { right: 25px; }
.hero-clean-dots {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}
.hero-clean-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.35);
  cursor: pointer;
  transition: all 0.3s ease;
}
.hero-clean-dot.active {
  width: 32px;
  border-radius: 10px;
  background: var(--accent);
}

.hero-quick-bar-wrap {
  position: relative;
  margin-top: -55px;
  z-index: 10;
  margin-bottom: 40px;
}
.hero-quick-bar {
  background: #ffffff;
  border-radius: 20px;
  padding: 24px 28px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  box-shadow: 0 15px 45px rgba(0, 50, 90, 0.12);
  border: 1px solid var(--border);
}
.quick-bar-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 14px;
  border-radius: 14px;
  transition: all 0.3s ease;
  text-decoration: none;
  color: inherit;
}
.quick-bar-item:hover {
  background: var(--bg-soft);
  transform: translateY(-3px);
}
.quick-bar-icon {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: var(--accent-light);
  color: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  flex-shrink: 0;
}
.quick-bar-text h4 {
  font-size: 0.98rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 2px;
}
.quick-bar-text p {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin: 0;
}

@media (max-width: 992px) {
  .hero-quick-bar { grid-template-columns: repeat(2, 1fr); gap: 16px; }
  .hero-nav-arrow { display: none; }
}
@media (max-width: 576px) {
  .hero-quick-bar { grid-template-columns: 1fr; }
  .hero-clean { padding: 60px 0 80px; }
}

.section{padding:80px 0}
.section-soft{background:var(--bg-soft)}
.section-head{text-align:center;max-width:720px;margin:0 auto 50px}
.section-eyebrow{display:inline-block;background:var(--primary-light);color:var(--primary);padding:5px 16px;border-radius:50px;font-size:0.82rem;font-weight:600;margin-bottom:12px}
.section-title{font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:12px;line-height:1.25}
.section-title .gradient-text{background:linear-gradient(135deg,var(--primary) 0%,var(--accent) 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.section-subtitle{font-size:1.02rem;color:var(--text-muted)}

.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center}
.about-image{position:relative}
.about-image-main{position:relative;border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-lg)}
.about-image img{width:100%;height:380px;object-fit:cover}
.about-image-badge{position:absolute;bottom:18px;left:18px;background:rgba(255,255,255,0.95);padding:10px 18px;border-radius:12px;display:flex;align-items:center;gap:12px;box-shadow:var(--shadow-md)}
.about-image-badge i{color:var(--accent);font-size:1.5rem}
.about-image-badge strong{display:block;font-size:0.95rem;color:var(--text)}
.about-image-badge span{font-size:0.78rem;color:var(--text-muted)}
.about-content h2{font-size:1.6rem;margin-bottom:14px}
.about-content p{color:var(--text-muted);margin-bottom:14px}
.about-features{margin:18px 0 24px}
.about-features li{display:flex;align-items:center;gap:10px;padding:6px 0;font-size:0.95rem}
.about-features i{color:var(--accent);font-size:0.9rem}
.about-cta{display:flex;flex-wrap:wrap;gap:14px;align-items:center}

.dept-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
.dept-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:24px 20px;text-align:center;transition:all var(--transition);display:flex;flex-direction:column}
.dept-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:rgba(0,102,164,0.30)}
.dept-icon{width:60px;height:60px;border-radius:16px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.5rem;margin:0 auto 14px}
.dept-card h3{font-size:1.05rem;margin-bottom:6px}
.dept-card p{font-size:0.86rem;color:var(--text-muted);margin-bottom:14px;flex:1}
.dept-link{color:var(--primary);font-weight:600;font-size:0.88rem;display:inline-flex;align-items:center;gap:6px}
.dept-link:hover{gap:10px}

.bg-med{background:linear-gradient(135deg,#0066a4 0%,#004a7a 100%)}
.bg-surg{background:linear-gradient(135deg,#34495e 0%,#1a2530 100%)}
.bg-gynae{background:linear-gradient(135deg,#c2185b 0%,#880e4f 100%)}
.bg-ortho{background:linear-gradient(135deg,#e67e22 0%,#a04000 100%)}
.bg-pediatric{background:linear-gradient(135deg,#8e44ad 0%,#5b2c6f 100%)}
.bg-ent{background:linear-gradient(135deg,#16a085 0%,#0e6655 100%)}
.bg-derma{background:linear-gradient(135deg,#d35400 0%,#a04000 100%)}
.bg-cardio{background:linear-gradient(135deg,#e74c3c 0%,#922b21 100%)}
.bg-neuro{background:linear-gradient(135deg,#2c3e50 0%,#1a252f 100%)}
.bg-gp{background:linear-gradient(135deg,#00a86b 0%,#008755 100%)}
.bg-sono{background:linear-gradient(135deg,#2980b9 0%,#1a5276 100%)}

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
.doctor-info .affiliation{color:var(--text-muted);font-size:0.82rem;margin-bottom:14px;line-height:1.5;padding-bottom:14px;border-bottom:1px dashed var(--border)}
.doctor-info .btn{margin-top:auto;width:100%;justify-content:center;padding:10px 18px;font-size:0.88rem}
.doctor-photo-link{display:block;position:relative;color:inherit}
.doctor-photo-link:hover{color:inherit}
.doctor-photo-link::after{content:"\f0f4";font-family:"Font Awesome 6 Free";font-weight:900;position:absolute;top:14px;right:14px;width:36px;height:36px;background:rgba(255,255,255,0.95);color:var(--primary);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.9rem;box-shadow:0 2px 8px rgba(0,0,0,0.15);transition:all var(--transition)}
.doctor-photo-link:hover::after{background:var(--primary);color:#fff;transform:scale(1.08) rotate(-8deg)}
.doctor-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:auto}
.doctor-actions .btn{margin-top:0;flex:1;min-width:120px;padding:10px 14px;font-size:0.82rem}

.filter-pills{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:36px}
.filter-pill{padding:8px 18px;border-radius:50px;background:#fff;border:1.5px solid var(--border);color:var(--text-muted);font-weight:600;font-size:0.88rem;cursor:pointer;transition:all var(--transition)}
.filter-pill:hover{border-color:var(--primary);color:var(--primary)}
.filter-pill.active{background:var(--primary);color:#fff;border-color:var(--primary);box-shadow:0 4px 12px rgba(0,102,164,0.25)}

.stats-section{position:relative;background:linear-gradient(135deg,var(--primary-dark) 0%,var(--primary) 100%);color:#fff;padding:60px 0}
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:30px;text-align:center;position:relative;z-index:1}
.stat-item .n{font-size:clamp(2rem,4vw,2.8rem);font-weight:800;line-height:1;color:#fff}
.stat-item p{color:rgba(255,255,255,0.85);font-size:0.95rem;margin-top:8px}

.diagnostic-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px}
.diag-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:20px;text-align:center;transition:all var(--transition)}
.diag-card:hover{transform:translateY(-3px);box-shadow:var(--shadow-md)}
.diag-icon{width:54px;height:54px;border-radius:14px;background:var(--primary-light);color:var(--primary);display:flex;align-items:center;justify-content:center;font-size:1.4rem;margin:0 auto 12px}
.diag-card h4{font-size:0.98rem;margin-bottom:4px}
.diag-card p{font-size:0.82rem;color:var(--text-muted)}

.partners-section{background:linear-gradient(135deg,#f8fbff 0%,#e8f2fb 100%)}
.partners-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:18px}
.partner-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:22px 16px;text-align:center;transition:all var(--transition);box-shadow:0 2px 8px rgba(0,80,130,0.05)}
.partner-card:hover{transform:translateY(-3px);box-shadow:var(--shadow-md);border-color:rgba(0,102,164,0.25)}
.partner-icon{width:50px;height:50px;border-radius:12px;background:linear-gradient(135deg,var(--accent) 0%,var(--accent-dark) 100%);color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin:0 auto 10px}
.partner-card h4{font-size:0.95rem;margin-bottom:4px}
.partner-card p{font-size:0.78rem;color:var(--text-muted)}

.cta-banner{background:linear-gradient(135deg,var(--primary-dark) 0%,var(--primary) 50%,var(--accent) 100%);color:#fff;padding:50px 0;position:relative;overflow:hidden}
.cta-banner::before{content:"";position:absolute;top:-100px;right:-100px;width:300px;height:300px;background:radial-gradient(circle,rgba(255,255,255,0.10) 0%,transparent 70%);border-radius:50%}
.cta-banner::after{content:"";position:absolute;bottom:-100px;left:-100px;width:300px;height:300px;background:radial-gradient(circle,rgba(0,168,107,0.20) 0%,transparent 70%);border-radius:50%}
.cta-banner-inner{position:relative;z-index:1;display:grid;grid-template-columns:1.4fr 1fr;gap:40px;align-items:center}
.cta-banner h2{color:#fff;font-size:clamp(1.4rem,3vw,1.9rem);margin-bottom:12px}
.cta-banner p{color:rgba(255,255,255,0.92);font-size:1rem;margin-bottom:20px}
.cta-actions{display:flex;flex-wrap:wrap;gap:10px}
.cta-actions .btn-light{background:rgba(255,255,255,0.15);color:#fff;border:1px solid rgba(255,255,255,0.30);backdrop-filter:blur(8px)}
.cta-actions .btn-light:hover{background:rgba(255,255,255,0.25);color:#fff;transform:translateY(-2px)}
.cta-bullets{display:grid;gap:10px;font-size:0.95rem}
.cta-bullet{display:flex;align-items:center;gap:10px}
.cta-bullet i{color:#6fe6a6;font-size:1rem}

.gallery-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
.gallery-grid img{width:100%;height:200px;object-fit:cover;border-radius:var(--radius);transition:transform 0.5s ease;cursor:pointer}
.gallery-grid img:hover{transform:scale(1.04)}

.appointment-section{background:var(--bg-soft)}
.appointment-wrap{display:grid;grid-template-columns:1fr 1.4fr;gap:0;background:#fff;border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-md)}
.appointment-info{background:linear-gradient(135deg,var(--primary) 0%,var(--primary-dark) 100%);color:#fff;padding:50px 40px}
.appointment-info h2{color:#fff;margin-bottom:14px;font-size:1.6rem}
.appointment-info > p{color:rgba(255,255,255,0.85);margin-bottom:30px}
.info-list{display:flex;flex-direction:column;gap:18px}
.info-item{display:flex;align-items:flex-start;gap:14px}
.info-item .ic{width:42px;height:42px;background:rgba(255,255,255,0.15);border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:1rem}
.info-item h5{color:#fff;font-size:0.95rem;margin-bottom:2px}
.info-item p{color:rgba(255,255,255,0.85);font-size:0.85rem;margin:0}
.appointment-form-wrap{padding:50px 40px}
.appointment-form-wrap h3{margin-bottom:8px}
.appointment-form-wrap > p{margin-bottom:30px;font-size:0.95rem}
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

.contact-grid{display:grid;grid-template-columns:1fr 1.4fr;gap:30px;align-items:start}
.contact-cards{display:flex;flex-direction:column;gap:16px}
.contact-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:20px;display:flex;gap:14px;align-items:flex-start;transition:all var(--transition)}
.contact-card:hover{box-shadow:var(--shadow-md);transform:translateY(-2px)}
.contact-card .ic{width:46px;height:46px;background:var(--primary-light);color:var(--primary);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0}
.contact-card h4{font-size:1rem;margin-bottom:4px}
.contact-card p,.contact-card a{font-size:0.88rem;color:var(--text-muted)}
.contact-card a:hover{color:var(--primary)}
.map-wrap{border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-md);height:100%;min-height:420px}
.map-wrap iframe{width:100%;height:100%;border:0;display:block}

.footer{background:linear-gradient(180deg,#002e54 0%,#001a30 100%);color:rgba(255,255,255,0.78);padding-top:50px}
.footer-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.2fr;gap:40px;padding-bottom:40px;border-bottom:1px solid rgba(255,255,255,0.10)}
.footer-col h4{color:#fff;font-size:1.05rem;margin-bottom:18px;position:relative;padding-bottom:8px}
.footer-col h4::after{content:"";position:absolute;left:0;bottom:0;width:30px;height:2px;background:var(--accent)}
.footer-col p{font-size:0.88rem;color:rgba(255,255,255,0.65);margin-bottom:12px}
.footer-col ul li{margin-bottom:8px}
.footer-col ul li a{color:rgba(255,255,255,0.65);font-size:0.88rem;transition:all var(--transition)}
.footer-col ul li a:hover{color:var(--accent);padding-left:4px}
.footer-col .footer-logo{display:flex;align-items:center;gap:12px;margin-bottom:14px}
.footer-col .footer-logo .logo-mark{width:48px;height:48px;border-color:rgba(255,255,255,0.15)}
.footer-col .footer-logo .bn{color:#fff;font-weight:700;font-size:1.05rem}
.footer-col .footer-logo .en{color:rgba(255,255,255,0.6);font-size:0.72rem}
.footer-social{display:flex;gap:10px;margin-top:14px}
.footer-social a{width:36px;height:36px;background:rgba(255,255,255,0.08);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;transition:all var(--transition)}
.footer-social a:hover{background:var(--accent);transform:translateY(-3px)}
.footer-bottom{padding:18px 0;text-align:center;font-size:0.85rem;color:rgba(255,255,255,0.55)}

.fab-wrap{position:fixed;right:20px;bottom:20px;z-index:999;display:flex;flex-direction:column;gap:10px}
.fab{width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.3rem;box-shadow:var(--shadow-md);transition:all var(--transition);cursor:pointer}
.fab:hover{transform:translateY(-3px) scale(1.05);color:#fff}
.fab-call{background:var(--primary)}
.fab-whatsapp{background:#25d366}
.fab-top{background:var(--text);opacity:0;visibility:hidden;transform:translateY(20px)}
.fab-top.show{opacity:1;visibility:visible;transform:translateY(0)}

.reveal{opacity:0;transform:translateY(30px);transition:opacity 0.7s ease,transform 0.7s ease}
.reveal.visible{opacity:1;transform:translateY(0)}

@media (max-width:1024px){
  .hero-grid,.about-grid,.cta-banner-inner,.contact-grid,.appointment-wrap{grid-template-columns:1fr;gap:30px}
  .footer-grid{grid-template-columns:repeat(2,1fr)}
  .stats-grid{grid-template-columns:repeat(2,1fr);gap:24px}
}
@media (max-width:768px){
  .nav-list{display:none}
  .menu-toggle{display:inline-flex}
  .topbar-inner{flex-direction:column;align-items:flex-start;gap:8px}
  .hero{padding:40px 0 50px}
  .hero-stats{grid-template-columns:1fr 1fr}
  .appointment-info,.appointment-form-wrap{padding:30px 24px}
  .form-grid{grid-template-columns:1fr}
  .footer-grid{grid-template-columns:1fr;gap:30px}
  .section{padding:50px 0}
  .doctor-photo{height:200px}
  .doctor-photo .avatar{width:130px;height:130px;font-size:3rem}
}
"""

JS_BLOCK = r"""
(function(){
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
  }
  const st = document.getElementById('scrollTop');
  if (st) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) st.classList.add('show'); else st.classList.remove('show');
    });
  }
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
  const di = document.querySelector('input[type="date"]');
  if (di) di.setAttribute('min', new Date().toISOString().split('T')[0]);
  const pills = document.querySelectorAll('#filterPills .filter-pill');
  const grid = document.getElementById('doctorsGrid');
  if (pills.length && grid) {
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const filter = pill.getAttribute('data-filter');
        grid.querySelectorAll('.doctor-card').forEach(card => {
          if (filter === 'all') { card.style.display = ''; }
          else {
            const photo = card.querySelector('.doctor-photo');
            if (photo && photo.classList.contains('bg-' + filter)) { card.style.display = ''; }
            else { card.style.display = 'none'; }
          }
        });
      });
    });
  }
  const form = document.getElementById('appointmentForm');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const req = form.querySelectorAll('[required]');
      let ok = true;
      req.forEach(f => { if (!f.value.trim()) { f.style.borderColor='#e74c3c'; ok=false; } else f.style.borderColor=''; });
      if (!ok) return;
      const success = document.getElementById('formSuccess');
      if (success) {
        success.classList.add('show');
        setTimeout(() => success.classList.remove('show'), 6000);
      }
      form.reset();
    });
  }
  const menuBtn = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.nav-list');
  if (menuBtn && navList) {
    menuBtn.addEventListener('click', () => {
      const isOpen = navList.style.display === 'flex';
      navList.style.display = isOpen ? '' : 'flex';
      navList.style.flexDirection = 'column';
      navList.style.position = 'absolute';
      navList.style.top = '100%';
      navList.style.left = '0';
      navList.style.right = '0';
      navList.style.background = '#fff';
      navList.style.padding = '14px 20px';
      navList.style.boxShadow = '0 8px 24px rgba(0,80,130,0.10)';
    });
  }
})();
"""

HTML_HEAD = '''<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>নিরাময় হাসপাতাল | NIRAMAYA Hospital &amp; Diagnostic Center - ফরিদপুর</title>
<meta name="description" content="নিরাময় হাসপাতাল এন্ড ডায়াগনস্টিক সেন্টার, ফরিদপুর। ১৪+ বিশেষজ্ঞ চিকিৎসক, ২৪/৭ ইমার্জেন্সি, আধুনিক ডায়াগনস্টিক।" />
<meta name="keywords" content="NIRAMAYA Hospital, নিরাময় হাসপাতাল, ফরিদপুর হাসপাতাল, ডাক্তার ফরিদপুর" />
<meta name="robots" content="index, follow" />
<meta property="og:title" content="নিরাময় হাসপাতাল | NIRAMAYA Hospital & Diagnostic Center" />
<meta property="og:description" content="ফরিদপুরের স্বনামধন্য বেসরকারি হাসপাতাল — ১৪+ বিশেষজ্ঞ চিকিৎসক" />
<meta property="og:type" content="website" />
<link rel="icon" type="image/png" href="niramoy-logo.png" />
<link rel="apple-touch-icon" href="niramoy-logo.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
<style>
'''

HTML_BODY = r'''
</style>
</head>
<body>

<!-- Topbar -->
<div class="topbar">
  <div class="container">
    <div class="topbar-inner">
      <div class="topbar-left">
        <span class="topbar-item topbar-badge"><i class="fa-solid fa-user-doctor"></i> <strong>১৪+ বিশেষজ্ঞ চিকিৎসক</strong></span>
        <span class="topbar-item"><span class="emergency-badge"><i class="fa-solid fa-circle-exclamation"></i> ২৪/৭ ইমার্জেন্সি</span></span>
        <span class="topbar-item"><i class="fa-solid fa-phone-volume"></i> <a href="tel:+8801729171549"><strong>০১৭২৯-১৭১৫৪৯</strong></a></span>
        <span class="topbar-item"><i class="fa-solid fa-phone"></i> <a href="tel:+8801734089489"><strong>০১৭৩৪-০৮৯৪৮৯</strong></a></span>
      </div>
      <div class="topbar-right">
        <span class="topbar-item"><i class="fa-solid fa-truck-medical"></i> <a href="tel:+8801731827110"><strong>০১৭৩১-৮২৭১১০</strong> (24/7)</a></span>
        <span class="topbar-social">
          <a href="https://www.facebook.com/p/%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A7%9F-%E0%A6%B9%E0%A6%B8%E0%A6%AA%E0%A6%BF%E0%A6%9F%E0%A6%BE%E0%A6%B2-%E0%A6%AB%E0%A6%B0%E0%A6%BF%E0%A6%A6%E0%A6%AA%E0%A7%81%E0%A6%B0-61577130113409/" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="https://wa.me/8801731827110" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
        </span>
      </div>
    </div>
  </div>
</div>

<!-- Header -->
<header class="header">
  <div class="container">
    <div class="header-inner">
      <a href="#home" class="logo">
        <div class="logo-mark">
          <img src="niramoy-logo.png" alt="নিরাময় হাসপাতাল লোগো" />
        </div>
        <div class="logo-text">
          <span class="bn">নিরাময় হাসপাতাল</span>
          <span class="en">NIRAMAYA Hospital &amp; Diagnostic Center</span>
        </div>
      </a>
      <nav class="nav">
        <ul class="nav-list">
          <li class="nav-item"><a class="nav-link active" href="#home">হোম</a></li>
          <li class="nav-item"><a class="nav-link" href="#about">আমাদের সম্পর্কে</a></li>
          <li class="nav-item"><a class="nav-link" href="#departments">বিভাগসমূহ</a></li>
          <li class="nav-item"><a class="nav-link" href="#doctors">ডাক্তারগণ</a></li>
          <li class="nav-item"><a class="nav-link" href="#diagnostic">ডায়াগনস্টিক</a></li>
          <li class="nav-item"><a class="nav-link" href="#contact">যোগাযোগ</a></li>
        </ul>
        <button class="menu-toggle" aria-label="Menu"><i class="fa-solid fa-bars"></i></button>
      </nav>
    </div>
  </div>
</header>

<!-- Hero -->
<section class="hero-clean" id="home">
  <!-- Background Image Slides (Indoor Medical Rooms & Equipment) -->
  <div class="hero-bg-slides" id="heroBgSlides">
    <div class="hero-bg-slide active" style="background-image: url('images/hero/slide-1.jpg')"></div>
    <div class="hero-bg-slide" style="background-image: url('images/hero/slide-2.jpg')"></div>
    <div class="hero-bg-slide" style="background-image: url('images/hero/slide-3-v2.jpg')"></div>
    <div class="hero-bg-slide" style="background-image: url('images/hero/slide-4.jpg')"></div>
  </div>
  <div class="hero-bg-overlay"></div>

  <!-- Navigation Controls -->
  <button class="hero-nav-arrow prev" id="heroPrevBtn" aria-label="Previous"><i class="fa-solid fa-chevron-left"></i></button>
  <button class="hero-nav-arrow next" id="heroNextBtn" aria-label="Next"><i class="fa-solid fa-chevron-right"></i></button>

  <div class="container hero-clean-container">
    <span class="hero-top-badge"><i class="fa-solid fa-hospital"></i> ১৯৯৯ সাল থেকে ফরিদপুরবাসীর সেবায়</span>
    <h1 class="hero-clean-title">নিরাময় হাসপাতাল ও ডায়াগনস্টিক সেন্টার (প্রা:)</h1>
    <p class="hero-clean-lead">ফরিদপুরে ১৪+ বিশেষজ্ঞ চিকিৎসক, ২৪/৭ ইমার্জেন্সি সেবা এবং আধুনিক ডায়াগনস্টিক — সব এক জায়গায়। অভিজ্ঞ বিশেষজ্ঞদের কাছ থেকে মানসম্মত চিকিৎসা নিন।</p>
    
    <div class="hero-clean-actions">
      <a href="appointment.html" class="btn btn-accent"><i class="fa-regular fa-calendar-check"></i> অনলাইন অ্যাপয়েন্টমেন্ট <i class="fa-solid fa-arrow-right"></i></a>
      <a href="tel:+8801731827110" class="btn btn-phone-pill"><i class="fa-solid fa-phone"></i> ০১৭৩১-৮২৭১১০</a>
    </div>

    <!-- Dots -->
    <div class="hero-clean-dots" id="heroCleanDots">
      <span class="hero-clean-dot active" data-slide="0"></span>
      <span class="hero-clean-dot" data-slide="1"></span>
      <span class="hero-clean-dot" data-slide="2"></span>
      <span class="hero-clean-dot" data-slide="3"></span>
    </div>
  </div>
</section>

<!-- Floating Quick Feature Bar -->
<div class="hero-quick-bar-wrap">
  <div class="container">
    <div class="hero-quick-bar">
      <a href="services.html" class="quick-bar-item">
        <div class="quick-bar-icon"><i class="fa-solid fa-bed-pulse"></i></div>
        <div class="quick-bar-text">
          <h4>২৪/৭ ইমার্জেন্সি</h4>
          <p>সার্বক্ষণিক জরুরি সেবা</p>
        </div>
      </a>
      <a href="tel:+8801731827110" class="quick-bar-item">
        <div class="quick-bar-icon"><i class="fa-solid fa-truck-medical"></i></div>
        <div class="quick-bar-text">
          <h4>অ্যাম্বুলেন্স সার্ভিস</h4>
          <p>২৪ ঘণ্টা দ্রুত রেসপন্স</p>
        </div>
      </a>
      <a href="#doctors" class="quick-bar-item">
        <div class="quick-bar-icon"><i class="fa-solid fa-user-doctor"></i></div>
        <div class="quick-bar-text">
          <h4>১৪+ বিশেষজ্ঞ চিকিৎসক</h4>
          <p>অভিজ্ঞ কনসালটেন্টগণ</p>
        </div>
      </a>
      <a href="#diagnostic" class="quick-bar-item">
        <div class="quick-bar-icon"><i class="fa-solid fa-microscope"></i></div>
        <div class="quick-bar-text">
          <h4>আধুনিক ডায়াগনস্টিক</h4>
          <p>নির্ভুল ল্যাব রিপোর্ট</p>
        </div>
      </a>
    </div>
  </div>
</div>

<!-- About -->
<section class="about section" id="about">
  <div class="container">
    <div class="about-grid">
      <div class="about-image">
        <div class="about-image-main">
          <img src="niramoy-aidfast-cover.jpg" alt="নিরাময় হাসপাতাল ভবন" loading="lazy" />
          <span class="about-image-badge">
            <i class="fa-solid fa-award"></i>
            <div>
              <strong>১৯৯৯ সাল থেকে</strong>
              <span>ফরিদপুরবাসীর সেবায়</span>
            </div>
          </span>
        </div>
      </div>
      <div class="about-content">
        <span class="section-eyebrow"><i class="fa-solid fa-hospital"></i> আমাদের সম্পর্কে</span>
        <h2>স্বাস্থ্যসেবায় নির্ভরযোগ্য প্রতিষ্ঠান</h2>
        <p><strong>নিরাময় হাসপাতাল এন্ড ডায়াগনস্টিক সেন্টার (প্রা:)</strong> — ১৯৯৯ সাল থেকে ফরিদপুরের নিরাময় ভবন, পশ্চিম খাবাসপুরে স্বনামধন্য স্বয়ংসম্পূর্ণ বেসরকারি হাসপাতাল হিসেবে সেবা দিয়ে আসছে।</p>
        <p>প্রতিষ্ঠাতা মোহাম্মদ কুব্বাত বিশ্বাস-এর ঐকান্তিক প্রচেষ্টায় গড়ে ওঠা এই প্রতিষ্ঠানে বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল, ফরিদপুরের মতো প্রতিষ্ঠানের স্বনামধন্য বিশেষজ্ঞ চিকিৎসকগণ নিয়মিত রোগী দেখেন।</p>
        <ul class="about-features">
          <li><i class="fa-solid fa-check-circle"></i> ১৪+ বিশেষজ্ঞ চিকিৎসক সব বিভাগে</li>
          <li><i class="fa-solid fa-check-circle"></i> ২৪/৭ ইমার্জেন্সি ও অ্যাম্বুলেন্স সেবা</li>
          <li><i class="fa-solid fa-check-circle"></i> আধুনিক ডায়াগনস্টিক ও প্যাথলজি ল্যাব</li>
          <li><i class="fa-solid fa-check-circle"></i> সাশ্রয়ী মূল্যে মানসম্মত চিকিৎসা</li>
          <li><i class="fa-solid fa-check-circle"></i> সরকার অনুমোদিত প্রতিষ্ঠান</li>
        </ul>
        <div class="about-cta">
          <a href="#doctors" class="btn btn-primary"><i class="fa-solid fa-user-doctor"></i> ডাক্তারগণ দেখুন</a>
          <a href="#contact" class="btn btn-outline"><i class="fa-solid fa-location-dot"></i> যোগাযোগ</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Departments -->
<section class="section section-soft" id="departments">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">বিশেষায়িত বিভাগ</span>
      <h2 class="section-title">আমাদের <span class="gradient-text">বিভাগসমূহ</span></h2>
      <p class="section-subtitle">সব বিভাগে অভিজ্ঞ বিশেষজ্ঞ চিকিৎসক ও আধুনিক সেবা</p>
    </div>
    <div class="dept-grid">
__DEPT_CARDS__
    </div>
  </div>
</section>

<!-- Doctors -->
<section class="doctors-section section" id="doctors">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">বিশেষজ্ঞ ডাক্তারগণ</span>
      <h2 class="section-title">আমাদের অভিজ্ঞ <span class="gradient-text">কনসালটেন্ট</span></h2>
      <p class="section-subtitle">ফরিদপুরের বঙ্গবন্ধু শেখ মুজিব মেডিকেল কলেজ হাসপাতাল ও ঢাকার বিভিন্ন প্রতিষ্ঠানের স্বনামধন্য বিশেষজ্ঞ চিকিৎসকগণ নিয়মিত রোগী দেখছেন।</p>
    </div>
    <div class="filter-pills" id="filterPills">
      <span class="filter-pill active" data-filter="all">সকল</span>
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
__DOCTOR_CARDS__
    </div>
  </div>
</section>

<!-- Stats -->
<section class="stats-section">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-item">
        <div class="n">১৪+</div>
        <p>বিশেষজ্ঞ ডাক্তার</p>
      </div>
      <div class="stat-item">
        <div class="n">২৫+</div>
        <p>বছরের অভিজ্ঞতা</p>
      </div>
      <div class="stat-item">
        <div class="n">১,০০,০০০+</div>
        <p>সেবা প্রাপ্ত রোগী</p>
      </div>
      <div class="stat-item">
        <div class="n">২৪/৭</div>
        <p>ইমার্জেন্সি সেবা</p>
      </div>
    </div>
  </div>
</section>

<!-- Diagnostic -->
<section class="section" id="diagnostic">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">ডায়াগনস্টিক সেবা</span>
      <h2 class="section-title">আধুনিক <span class="gradient-text">ডায়াগনস্টিক ল্যাব</span></h2>
      <p class="section-subtitle">সঠিক রোগ নির্ণয়ের জন্য সর্বাধুনিক যন্ত্রপাতি ও প্রযুক্তি</p>
    </div>
    <div class="diagnostic-grid">
      <div class="diag-card"><div class="diag-icon"><i class="fa-solid fa-microscope"></i></div><h4>প্যাথলজি ল্যাব</h4><p>রক্ত, প্রস্রাব ও অন্যান্য পরীক্ষা</p></div>
      <div class="diag-card"><div class="diag-icon"><i class="fa-solid fa-wave-square"></i></div><h4>আল্ট্রাসনোগ্রাফি (USG)</h4><p>সম্পূর্ণ USG ও ইকো</p></div>
      <div class="diag-card"><div class="diag-icon"><i class="fa-solid fa-heart-pulse"></i></div><h4>ইসিজি (ECG)</h4><p>হৃদরোগ নির্ণয়</p></div>
      <div class="diag-card"><div class="diag-icon"><i class="fa-solid fa-x-ray"></i></div><h4>ডিজিটাল এক্স-রে</h4><p>হাড় ও বক্ষের এক্স-রে</p></div>
      <div class="diag-card"><div class="diag-icon"><i class="fa-solid fa-droplet"></i></div><h4>বায়োকেমিস্ট্রি</h4><p>লিপিড প্রোফাইল, লিভার, কিডনি</p></div>
      <div class="diag-card"><div class="diag-icon"><i class="fa-solid fa-vial-virus"></i></div><h4>হরমোন টেস্ট</h4><p>থাইরয়েড, ডায়াবেটিস</p></div>
    </div>
  </div>
</section>

<!-- Insurance Partners -->
<section class="section partners-section">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">ইন্সুরেন্স পার্টনার</span>
      <h2 class="section-title">আমাদের <span class="gradient-text">ইন্সুরেন্স পার্টনার</span></h2>
      <p class="section-subtitle">নিচের ইন্সুরেন্স কোম্পানিগুলোর কার্ডধারীরা আমাদের হাসপাতাল থেকে সেবা নিতে পারবেন</p>
    </div>
    <div class="partners-grid">
      <div class="partner-card"><div class="partner-icon"><i class="fa-solid fa-shield-halved"></i></div><h4>স্বাস্থ্য বীমা</h4><p>বাংলাদেশ সরকার</p></div>
      <div class="partner-card"><div class="partner-icon"><i class="fa-solid fa-building-columns"></i></div><h4>মেটলাইফ</h4><p>MetLife Bangladesh</p></div>
      <div class="partner-card"><div class="partner-icon"><i class="fa-solid fa-hand-holding-medical"></i></div><h4>প্রগ্রেসিভ লাইফ</h4><p>Progressive Life</p></div>
      <div class="partner-card"><div class="partner-icon"><i class="fa-solid fa-heart-circle-check"></i></div><h4>ন্যাশনাল লাইফ</h4><p>National Life Insurance</p></div>
      <div class="partner-card"><div class="partner-icon"><i class="fa-solid fa-staff-snake"></i></div><h4>গ্রিন ডেল্টা</h4><p>Green Delta Insurance</p></div>
      <div class="partner-card"><div class="partner-icon"><i class="fa-solid fa-handshake"></i></div><h4>অন্যান্য পার্টনার</h4><p>আরো বিস্তারিত জানতে কল করুন</p></div>
    </div>
  </div>
</section>

<!-- Appointment CTA Banner -->
<section class="cta-banner">
  <div class="container">
    <div class="cta-banner-inner">
      <div>
        <h2><i class="fa-regular fa-calendar-check"></i> অনলাইনে অ্যাপয়েন্টমেন্ট নিন — ২ মিনিটেই</h2>
        <p>আপনার পছন্দের ডাক্তার ও সময় বেছে নিয়ে ঘরে বসে অ্যাপয়েন্টমেন্ট কনফার্ম করুন। ফোনে কনফার্মেশন পাবেন ১০ মিনিটের মধ্যে।</p>
        <div class="cta-actions">
          <a href="#appointment" class="btn btn-accent"><i class="fa-regular fa-calendar-check"></i> এখনই অ্যাপয়েন্টমেন্ট নিন</a>
          <a href="tel:+8801731827110" class="btn btn-light"><i class="fa-solid fa-phone"></i> ০১৭৩১-৮২৭১১০</a>
        </div>
      </div>
      <div class="cta-bullets">
        <div class="cta-bullet"><i class="fa-solid fa-circle-check"></i> কনফার্মেশন ফোনে ১০ মিনিটে</div>
        <div class="cta-bullet"><i class="fa-solid fa-circle-check"></i> সপ্তাহে ৭ দিন চালু</div>
        <div class="cta-bullet"><i class="fa-solid fa-circle-check"></i> ইমার্জেন্সি ২৪/৭</div>
        <div class="cta-bullet"><i class="fa-solid fa-circle-check"></i> বিনামূল্যে পরামর্শ ফোনে</div>
      </div>
    </div>
  </div>
</section>

<!-- Gallery -->
<section class="section section-soft">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">হাসপাতালের ছবি</span>
      <h2 class="section-title">আমাদের <span class="gradient-text">পরিবেশ</span></h2>
      <p class="section-subtitle">পরিচ্ছন্ন ও আরামদায়ক পরিবেশে আধুনিক সেবা</p>
    </div>
    <div class="gallery-grid">
      <img src="niramoy-aidfast-cover.jpg" alt="নিরাময় হাসপাতাল ভবন" loading="lazy" />
      <img src="niramaya-banner-official.jpg" alt="NIRAMAYA Hospital and Diagnostic Center - Official Banner" loading="lazy" />
      <img src="niramoy-building-night.jpg" alt="নিরাময় হাসপাতাল ভবন — সন্ধ্যার আলোয়" loading="lazy" />
      <img src="niramoy-archhms-header.jpg" alt="হাসপাতালের ভেতরের অংশ" loading="lazy" />
      <img src="niramoy-archhms-gallery2.jpg" alt="হাসপাতালের সুবিধা" loading="lazy" />
      <img src="niramoy-aidfast-profile.jpg" alt="নিরাময় হাসপাতাল" loading="lazy" />
    </div>
  </div>
</section>

<!-- Appointment Form -->
<section class="section appointment-section" id="appointment">
  <div class="container">
    <div class="appointment-wrap reveal">
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
        <form class="form-grid" id="appointmentForm" novalidate>
          <div class="form-group">
            <label>আপনার নাম <span class="req">*</span></label>
            <input type="text" name="name" placeholder="পূর্ণ নাম" required />
          </div>
          <div class="form-group">
            <label>মোবাইল নম্বর <span class="req">*</span></label>
            <input type="tel" name="phone" placeholder="01XXXXXXXXX" required />
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
            <select name="doctor" required>
              <option value="">— ডাক্তার বাছাই করুন —</option>
              <option>ডা. আবু বকর সিদ্দিক</option>
              <option>ডা. মোঃ রিয়াদ হোসেন বাপ্পি</option>
              <option>ডা. শ্রাবন্তী এম ইসলাম</option>
              <option>ডা. মো. মঈন উদ্দিন</option>
              <option>ডা. শশাঙ্ক নাগ (সনেট)</option>
              <option>ডা. মোহাম্মদ রফিকুল ইসলাম</option>
              <option>ডা. উৎপল নাগ</option>
              <option>ডা. আবু সালে আহমেদ সৌরভ</option>
              <option>ডা. নাহিদ বাদশা</option>
              <option>ডা. হরিচাঁদ শীল</option>
              <option>ডা. সৈয়দ ইমতিয়াজ উদ্দিন</option>
              <option>ডা. পাপড়ী সরকার</option>
              <option>ডা. এস এম নূর ই আলম (বিদ্যুৎ)</option>
              <option>ডা. শংকর কুমার দে</option>
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
  </div>
</section>

<!-- Contact -->
<section class="section section-soft" id="contact">
  <div class="container">
    <div class="section-head">
      <span class="section-eyebrow">যোগাযোগ</span>
      <h2 class="section-title">আমাদের সাথে <span class="gradient-text">যোগাযোগ</span></h2>
      <p class="section-subtitle">যেকোনো প্রয়োজনে যোগাযোগ করুন — আমরা সবসময় আপনার পাশে</p>
    </div>
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
            <p><a href="tel:+8801729171549">+৮৮০১৭২৯-১৭১৫৪৯</a> (মূল)<br/>
               <a href="tel:+8801734089489">+৮৮০১৭৩৪-০৮৯৪৮৯</a><br/>
               <a href="tel:+8801720003699">+৮৮০১৭২০-০০৩৬৯৯</a></p>
          </div>
        </div>
        <div class="contact-card">
          <div class="ic"><i class="fa-solid fa-truck-medical"></i></div>
          <div>
            <h4>ইমার্জেন্সি (২৪/৭)</h4>
            <p><a href="tel:+8801731827110">+৮৮০১৭৩১-৮২৭১১০</a></p>
          </div>
        </div>
        <div class="contact-card">
          <div class="ic"><i class="fa-brands fa-facebook"></i></div>
          <div>
            <h4>Facebook</h4>
            <p><a href="https://www.facebook.com/p/%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A7%9F-%E0%A6%B9%E0%A6%B8%E0%A6%AA%E0%A6%BF%E0%A6%9F%E0%A6%BE%E0%A6%B2-%E0%A6%AB%E0%A6%B0%E0%A6%BF%E0%A6%A6%E0%A6%AA%E0%A7%81%E0%A6%B0-61577130113409/" target="_blank" rel="noopener">নিরাময় হাসপাতাল, ফরিদপুর</a></p>
          </div>
        </div>
      </div>
      <div class="map-wrap">
        <iframe src="https://www.google.com/maps?q=নিরাময়+হাসপাতাল+ফরিদপুর&output=embed" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="NIRAMAYA Hospital Location"></iframe>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <div class="footer-logo">
          <div class="logo-mark">
            <img src="niramoy-logo.png" alt="NIRAMAYA Hospital" />
          </div>
          <div>
            <div class="bn">নিরাময় হাসপাতাল</div>
            <div class="en">NIRAMAYA Hospital &amp; Diagnostic Center</div>
          </div>
        </div>
        <p>১৯৯৯ সাল থেকে ফরিদপুরবাসীর সেবায় নিবেদিত — আধুনিক চিকিৎসা, অভিজ্ঞ বিশেষজ্ঞ ও নির্ভরযোগ্য ডায়াগনস্টিক সেবা।</p>
        <div class="footer-social">
          <a href="https://www.facebook.com/p/%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A7%9F-%E0%A6%B9%E0%A6%B8%E0%A6%AA%E0%A6%BF%E0%A6%9F%E0%A6%BE%E0%A6%B2-%E0%A6%AB%E0%A6%B0%E0%A6%BF%E0%A6%A6%E0%A6%AA%E0%A7%81%E0%A6%B0-61577130113409/" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="https://wa.me/8801731827110" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
      </div>
      <div class="footer-col">
        <h4>কুইক লিংক</h4>
        <ul>
          <li><a href="#home">হোম</a></li>
          <li><a href="#about">আমাদের সম্পর্কে</a></li>
          <li><a href="#departments">বিভাগসমূহ</a></li>
          <li><a href="#doctors">ডাক্তারগণ</a></li>
          <li><a href="#diagnostic">ডায়াগনস্টিক</a></li>
          <li><a href="#contact">যোগাযোগ</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>বিভাগসমূহ</h4>
        <ul>
          <li><a href="#doctors">মেডিসিন</a></li>
          <li><a href="#doctors">সার্জারি</a></li>
          <li><a href="#doctors">গাইনী ও প্রসূতি</a></li>
          <li><a href="#doctors">অর্থোপেডিক্স</a></li>
          <li><a href="#doctors">ইএনটি</a></li>
          <li><a href="#doctors">চর্ম ও যৌন</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>যোগাযোগ</h4>
        <p><i class="fa-solid fa-location-dot" style="color:var(--accent);margin-right:6px;"></i> নিরাময় ভবন, পশ্চিম খাবাসপুর, ফরিদপুর</p>
        <p><i class="fa-solid fa-phone" style="color:var(--accent);margin-right:6px;"></i> <a href="tel:+8801729171549" style="color:rgba(255,255,255,0.65);">+৮৮০১৭২৯-১৭১৫৪৯</a></p>
        <p><i class="fa-solid fa-truck-medical" style="color:var(--accent);margin-right:6px;"></i> <a href="tel:+8801731827110" style="color:rgba(255,255,255,0.65);">+৮৮০১৭৩১-৮২৭১১০ (24/7)</a></p>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year">2026</span> নিরাময় হাসপাতাল এন্ড ডায়াগনস্টিক সেন্টার (প্রা:)। সকল অধিকার সংরক্ষিত।</p>
    </div>
  </div>
</footer>

<!-- FAB -->
<div class="fab-wrap">
  <a class="fab fab-top" id="scrollTop" href="#top" aria-label="উপরে যান"><i class="fa-solid fa-chevron-up"></i></a>
  <a class="fab fab-whatsapp" href="https://wa.me/8801731827110" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
  <a class="fab fab-call" href="tel:+8801731827110" aria-label="কল করুন"><i class="fa-solid fa-phone"></i></a>
</div>

<script>
__JS__
</script>
</body>
</html>
'''

# Combine: head + css + body template, then substitute
body = HTML_BODY.replace("__DEPT_CARDS__", DEPT_CARDS)
body = body.replace("__DOCTOR_CARDS__", DOCTOR_CARDS)
body = body.replace("__JS__", JS_BLOCK)

html = HTML_HEAD + CSS_BLOCK + body

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"[OK] {OUT}  ({len(html):,} bytes)")
print(f"  - Doctor cards: 14")
print(f"  - Department cards: {len(DEPT_LIST)}")
