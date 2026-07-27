# -*- coding: utf-8 -*-
"""Patch index.html: make doctor cards clickable + add 'View Profile' button.
Safe approach: process each doctor card block separately.
"""
import re
import os

INDEX = r"D:\minimax\New folder\website\index.html"

with open(INDEX, "r", encoding="utf-8") as f:
    html = f.read()

# First, add CSS for the new elements
css_old = ".doctor-info .btn{margin-top:auto;width:100%;justify-content:center;padding:10px 18px;font-size:0.88rem}"
css_new = """\
.doctor-info .btn{margin-top:auto;width:100%;justify-content:center;padding:10px 18px;font-size:0.88rem}
.doctor-photo-link{display:block;position:relative;color:inherit}
.doctor-photo-link:hover{color:inherit}
.doctor-photo-link::after{content:'\\f0f4';font-family:'Font Awesome 6 Free';font-weight:900;position:absolute;top:14px;right:14px;width:36px;height:36px;background:rgba(255,255,255,0.95);color:var(--primary);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.9rem;box-shadow:0 2px 8px rgba(0,0,0,0.15);transition:all var(--transition)}
.doctor-photo-link:hover::after{background:var(--primary);color:#fff;transform:scale(1.08) rotate(-8deg)}
.doctor-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:auto}
.doctor-actions .btn{margin-top:0;flex:1;min-width:120px;padding:10px 14px;font-size:0.82rem}"""
html = html.replace(css_old, css_new, 1)
print("CSS injected.")

# Find all doctor card blocks.
# Each block: starts with "      <!-- Doctor N: ..." and ends at the closing </div> after the appointment button.
# We will find the START of each card, then find the matching doctor-photo div, then the appointment button.

# Use a simpler approach: split html by "<!-- Doctor N:" markers
# For each card, apply targeted replacements

parts = re.split(r'(      <!-- Doctor \d+: [^\n]+-->\n)', html)
# parts alternates: [pre-text, marker1, card1, marker2, card2, ...]
# But re.split with capturing group keeps the delimiter; in this case each marker is followed by a card chunk

result = []
result.append(parts[0])  # text before first marker

i = 1
count = 0
while i < len(parts):
    marker = parts[i]            # "      <!-- Doctor N: ... -->\n"
    card_chunk = parts[i+1]      # everything from "<div class=\"doctor-card reveal\">" to the next marker or end

    # Extract doctor number from marker
    m_num = re.search(r'Doctor (\d+):', marker)
    n = m_num.group(1)

    # Pad with two-digit zero
    n_padded = f"{int(n):02d}"

    # 1) Wrap doctor-photo div in <a>
    # Find: <div class="doctor-photo bg-XXX">  ...  </div>
    # The photo block spans 5 lines: opening + dept-tag + optional exp-badge + avatar + closing
    photo_pattern = re.compile(
        r'(        )(<div class="doctor-photo bg-[a-z]+">\n'
        r'          <span class="dept-tag">[^<]+</span>\n'
        r'(?:          <span class="exp-badge">[^<]+</span>\n)?'
        r'          <div class="avatar">[^<]+</div>\n'
        r'        </div>)',
        re.MULTILINE
    )
    card_chunk_new, n_photo = photo_pattern.subn(
        lambda mm: (
            f'{mm.group(1)}<a href="doctors/{n_padded}.html" class="doctor-photo-link" aria-label="প্রোফাইল দেখুন">\n'
            f'{mm.group(2)}\n'
            f'{mm.group(1)}</a>'
        ),
        card_chunk
    )
    if n_photo != 1:
        print(f"WARNING: doctor {n_padded} photo wrap count = {n_photo}")

    # 2) Replace single appointment button with actions group
    btn_pattern = re.compile(
        r'(        )(<a href="#appointment" class="btn btn-primary"><i class="fa-regular fa-calendar-check"></i> অ্যাপয়েন্টমেন্ট</a>)',
        re.MULTILINE
    )
    card_chunk_new, n_btn = btn_pattern.subn(
        lambda mm: (
            f'{mm.group(1)}<div class="doctor-actions">\n'
            f'{mm.group(1)}  <a href="#appointment" class="btn btn-primary"><i class="fa-regular fa-calendar-check"></i> অ্যাপয়েন্টমেন্ট</a>\n'
            f'{mm.group(1)}  <a href="doctors/{n_padded}.html" class="btn btn-ghost"><i class="fa-solid fa-user-doctor"></i> প্রোফাইল</a>\n'
            f'{mm.group(1)}</div>'
        ),
        card_chunk_new
    )
    if n_btn != 1:
        print(f"WARNING: doctor {n_padded} button wrap count = {n_btn}")

    result.append(marker)
    result.append(card_chunk_new)
    count += 1
    i += 2

new_html = "".join(result)

# Make sure doctor link in profile pages uses ../index.html - actually main page links should be doctors/01.html from index.html
# Already done above with href="doctors/{n_padded}.html"

# Sanity check: count doctor-photo-link occurrences (should be 14)
link_count = new_html.count('class="doctor-photo-link"')
print(f"doctor-photo-link count: {link_count} (expected 14)")

# Write file
with open(INDEX, "w", encoding="utf-8") as f:
    f.write(new_html)
print(f"Done. Processed {count} cards.")
