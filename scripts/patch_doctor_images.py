# -*- coding: utf-8 -*-
"""Patch all doctor profile pages and main index.html:
- Add <img> tag in profile-photo with onerror fallback to avatar
- Avatar (initial) span stays as fallback when image is missing
"""
import os, re

DOCTORS = [
    ("01", "abu-bakar",   "jpg", "আ"),
    ("02", "riyad-bappy", "jpg", "রি"),
    ("03", "shrabanti",   "png", "শ্রা"),
    ("04", "moin-uddin",  "jpg", "মই"),
    ("05", "shashank-nag","jpg", "শ"),
    ("06", "rafiqul-islam","jpg", "রফ"),
    ("07", "utpal-nag",   "jpg", "উৎ"),
    ("08", "sourav",      "jpg", "সৌ"),
    ("09", "nahid-badsha","png", "না"),
    ("10", "harichand-shil","png", "হ"),
    ("11", "imtiaz-uddin","png", "সৈ"),
    ("12", "papri-sarker","png", "পা"),
    ("13", "nurul-alam",  "jpg", "এস"),
    ("14", "shankar-dey", "jpg", "শং"),
]

DOC_DIR  = r"D:\minimax\New folder\website\doctors"
INDEX    = r"D:\minimax\New folder\website\index.html"

# --- Patch each profile page ---
print("=== Patching profile pages ===")
for num, slug, ext, initial in DOCTORS:
    path = os.path.join(DOC_DIR, f"{num}.html")
    if not os.path.exists(path):
        print(f"[SKIP] {path} missing")
        continue
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    img_filename = f"{num}-{slug}.{ext}"
    # Build the new profile-photo div with image + fallback avatar
    new_block = (
        f'      <div class="profile-photo" data-initial="{initial}">\n'
        f'        <img src="../images/doctors/{img_filename}" alt="{initial} - ডাক্তারের ছবি" '
        f'onerror="this.style.display=\'none\';var s=this.nextElementSibling;if(s)s.style.display=\'flex\';" '
        f'style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />\n'
        f'        <span class="avatar-fallback" style="font-size:5rem;display:flex;align-items:center;justify-content:center;width:100%;height:100%;">{initial}</span>\n'
        f'      </div>'
    )
    # Old pattern: <div class="profile-photo">\n  <span style="font-size:5rem;">INITIAL</span>\n  </div>
    old_pattern = re.compile(
        r'<div class="profile-photo">\s*<span style="font-size:5rem;">[^<]+</span>\s*</div>',
        re.MULTILINE
    )
    new_html, n = old_pattern.subn(new_block, html)
    if n == 0:
        print(f"[WARN] {num}: pattern not found")
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"[OK] {num}: -> {img_filename}")

# --- Patch main index.html ---
print()
print("=== Patching index.html ===")
with open(INDEX, "r", encoding="utf-8") as f:
    idx_html = f.read()

for num, slug, ext, initial in DOCTORS:
    img_filename = f"{num}-{slug}.{ext}"
    # Pattern: <div class="doctor-photo bg-CLASS">\n  <span class="dept-tag">DEPT</span>\n  <div class="avatar">INITIAL</div>\n  </div>
    # Replace avatar div with img + fallback avatar
    old = f'<div class="avatar">{initial}</div>'
    new = (
        f'<img src="images/doctors/{img_filename}" alt="{initial} - ডাক্তারের ছবি" '
        f'style="width:160px;height:160px;border-radius:50%;object-fit:cover;border:5px solid rgba(255,255,255,0.30);box-shadow:0 12px 30px rgba(0,0,0,0.20);" '
        f'onerror="this.style.display=\'none\';var n=this.nextElementSibling;if(n)n.style.display=\'flex\';" />'
        f'<div class="avatar" style="display:none;">{initial}</div>'
    )
    # Replace only first occurrence per file (each card has unique initial)
    if old not in idx_html:
        print(f"[WARN] {num}: avatar div not found")
        continue
    idx_html = idx_html.replace(old, new, 1)
    print(f"[OK] {num}: -> {img_filename}")

with open(INDEX, "w", encoding="utf-8") as f:
    f.write(idx_html)
print()
print("Done. All 14 doctor pages + main index.html updated.")
