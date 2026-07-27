# -*- coding: utf-8 -*-
"""Remove dead modal code from index.html - line-based approach."""
import re

INDEX = r"D:\minimax\New folder\website\index.html"

with open(INDEX, "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================================
# 1) Remove Modal HTML (line-based)
# ============================================================================
lines = html.split('\n')

# Find indexes of modal sections
dept_modal_start = None
diag_modal_start = None
script_start = None

for i, line in enumerate(lines):
    if '<!-- Department Profile Modal -->' in line:
        dept_modal_start = i
    if '<!-- Diagnostic Profile Modal -->' in line:
        diag_modal_start = i
    if '<script src="js/script.js"></script>' in line:
        script_start = i

print(f"Department modal at line: {dept_modal_start}")
print(f"Diagnostic modal at line: {diag_modal_start}")
print(f"Script tag at line: {script_start}")

# Remove in reverse order (so indexes don't shift)
# Remove diagnostic modal first (later in file)
if diag_modal_start is not None and script_start is not None:
    del lines[diag_modal_start:script_start]
    print(f"Removed Diagnostic modal: {script_start - diag_modal_start} lines")

# Re-find script and dept modal
script_start = None
dept_modal_start = None
for i, line in enumerate(lines):
    if '<!-- Department Profile Modal -->' in line:
        dept_modal_start = i
    if '<script src="js/script.js"></script>' in line:
        script_start = i

if dept_modal_start is not None and script_start is not None:
    del lines[dept_modal_start:script_start]
    print(f"Removed Department modal: {script_start - dept_modal_start} lines")

# Clean up consecutive empty lines (max 2 in a row)
cleaned_lines = []
empty_count = 0
for line in lines:
    if line.strip() == '':
        empty_count += 1
        if empty_count <= 1:  # Keep at most 1 blank line
            cleaned_lines.append(line)
    else:
        empty_count = 0
        cleaned_lines.append(line)

lines = cleaned_lines
html = '\n'.join(lines)

# ============================================================================
# 2) Remove modal-related CSS rules
# ============================================================================
modal_css_patterns = [
    r'\.dept-modal[^{]*\{[^}]*\}\s*',
    r'\.dept-info-card[^{]*\{[^}]*\}\s*',
    r'\.dept-service-list[^{]*\{[^}]*\}\s*',
    r'\.dept-tech-list[^{]*\{[^}]*\}\s*',
    r'\.dept-meta-card[^{]*\{[^}]*\}\s*',
    r'\.dept-meta-item[^{]*\{[^}]*\}\s*',
    r'\.dept-modal-doctors-section[^{]*\{[^}]*\}\s*',
    r'\.dept-modal-doctors-grid[^{]*\{[^}]*\}\s*',
    r'\.dept-modal-footer[^{]*\{[^}]*\}\s*',
    r'\.btn-dept-profile[^{]*\{[^}]*\}\s*',
    r'\.btn-dept-doctors[^{]*\{[^}]*\}\s*',
    r'\.dept-card-content[^{]*\{[^}]*\}\s*',
    r'\.dept-card-img[^{]*\{[^}]*\}\s*',
    r'\.dept-card-overlay[^{]*\{[^}]*\}\s*',
    r'\.dept-card-badge[^{]*\{[^}]*\}\s*',
    r'\.dept-card-icon[^{]*\{[^}]*\}\s*',
    r'\.dept-card-media[^{]*\{[^}]*\}\s*',
    r'\.dept-chips[^{]*\{[^}]*\}\s*',
    r'\.dept-card-actions[^{]*\{[^}]*\}\s*',
    r'\.dept-card[^{]*\{[^}]*\}\s*',
    r'\.dept-grid[^{]*\{[^}]*\}\s*',

    r'\.diag-modal[^{]*\{[^}]*\}\s*',
    r'\.diag-info-card[^{]*\{[^}]*\}\s*',
    r'\.diag-test-list[^{]*\{[^}]*\}\s*',
    r'\.diag-prep-list[^{]*\{[^}]*\}\s*',
    r'\.diag-tech-list[^{]*\{[^}]*\}\s*',
    r'\.diag-meta-card[^{]*\{[^}]*\}\s*',
    r'\.diag-meta-item[^{]*\{[^}]*\}\s*',
    r'\.diag-modal-footer[^{]*\{[^}]*\}\s*',
    r'\.btn-diag-profile[^{]*\{[^}]*\}\s*',
    r'\.btn-diag-book[^{]*\{[^}]*\}\s*',
    r'\.diag-card[^{]*\{[^}]*\}\s*',
    r'\.diag-card-content[^{]*\{[^}]*\}\s*',
    r'\.diag-card-img[^{]*\{[^}]*\}\s*',
    r'\.diag-card-overlay[^{]*\{[^}]*\}\s*',
    r'\.diag-card-badge[^{]*\{[^}]*\}\s*',
    r'\.diag-icon[^{]*\{[^}]*\}\s*',
    r'\.diag-card-media[^{]*\{[^}]*\}\s*',
    r'\.diag-chips[^{]*\{[^}]*\}\s*',
    r'\.diag-card-actions[^{]*\{[^}]*\}\s*',
]

for pat in modal_css_patterns:
    html, n = re.subn(pat, '', html)
    if n:
        print(f"  CSS removed: {n} (pattern: {pat[:50]}...)")

# ============================================================================
# 3) Convert modal buttons to simple links + clean duplicates
# ============================================================================
# Department button: <button type="button" class="btn-dept-profile" onclick="openDeptProfile('X')">...বিস্তারিত প্রোফাইল...</button>
dept_btn_pattern = re.compile(
    r'<button[^>]*class="btn-dept-profile"[^>]*>\s*<i[^>]*></i>\s*বিস্তারিত প্রোফাইল\s*</button>',
    re.DOTALL
)
html, n4 = dept_btn_pattern.subn('', html)
print(f"Removed dept modal buttons: {n4}")

# Diagnostic button: similar
diag_btn_pattern = re.compile(
    r'<button[^>]*class="btn-diag-profile"[^>]*>\s*<i[^>]*></i>\s*বিস্তারিত প্রোফাইল\s*</button>',
    re.DOTALL
)
html, n5 = diag_btn_pattern.subn('', html)
print(f"Removed diag modal buttons: {n5}")

# ============================================================================
# 4) Remove img references to missing dept/diag images
# ============================================================================
# These images don't exist: images/departments/dept-*.jpg, images/diagnostic/diag-*.jpg
missing_img_pattern = re.compile(
    r'<img src="images/(departments|department|diagnostic)/[^"]+\.(jpg|jpeg|png|webp)"[^>]*>',
    re.IGNORECASE
)
html, n6 = missing_img_pattern.subn('', html)
print(f"Removed missing img references: {n6}")

# ============================================================================
# 5) Add fallback for missing dept/diag images via JS data URI placeholder
# ============================================================================
# Instead of removing, let's add a placeholder bg color via inline style
# Actually since cards have ::before bg colors, just remove the broken imgs (already done)

# ============================================================================
# 6) Clean up the inline "dept-card-media" and "diag-card-media" empty wrappers
# ============================================================================
# The cards now have empty media wrappers; clean up but keep the structure
# Just leave them - they'll show as empty 200x200 area

# ============================================================================
# 7) Replace broken img tags with onerror fallback avatar
# ============================================================================
# (Already done earlier in patch_doctor_images.py for doctor photos)

# Write back
with open(INDEX, "w", encoding="utf-8") as f:
    f.write(html)

print()
print(f"Done. Final size: {len(html):,} bytes")
print(f"Lines: {html.count(chr(10))}")
