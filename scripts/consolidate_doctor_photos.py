# -*- coding: utf-8 -*-
"""Consolidate doctor images: pick the largest from each search folder,
copy to standard filename, and clean up."""
import os, shutil

DOCTORS = [
    ("01", "abu-bakar"),
    ("02", "riyad-bappy"),
    ("03", "shrabanti"),
    ("04", "moin-uddin"),
    ("05", "shashank-nag"),
    ("06", "rafiqul-islam"),
    ("07", "utpal-nag"),
    ("08", "sourav"),
    ("09", "nahid-badsha"),
    ("10", "harichand-shil"),
    ("11", "imtiaz-uddin"),
    ("12", "papri-sarker"),
    ("13", "nurul-alam"),
    ("14", "shankar-dey"),
]

IMG_DIR = r"D:\minimax\New folder\website\images\doctors"
MIN_SIZE = 1024  # 1 KB threshold to skip tiny placeholders

os.makedirs(IMG_DIR, exist_ok=True)

results = []
for num, slug in DOCTORS:
    folder = os.path.join(IMG_DIR, f"{num}-{slug}")
    if not os.path.isdir(folder):
        print(f"[SKIP] {folder} (missing)")
        results.append((num, slug, None, 0))
        continue
    # List all files
    files = [os.path.join(folder, f) for f in os.listdir(folder)
             if os.path.isfile(os.path.join(folder, f))]
    # Filter: image extension and > 1 KB
    valid = [f for f in files
             if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
             and os.path.getsize(f) > MIN_SIZE]
    if not valid:
        print(f"[NONE] {folder} (no valid image)")
        results.append((num, slug, None, 0))
        continue
    # Pick the largest
    best = max(valid, key=os.path.getsize)
    size = os.path.getsize(best)
    # Target filename
    ext = os.path.splitext(best)[1].lower()
    target = os.path.join(IMG_DIR, f"{num}-{slug}{ext}")
    # If target exists with different content, overwrite
    shutil.copy2(best, target)
    # Delete the search folder
    shutil.rmtree(folder)
    print(f"[OK] {num}-{slug}: {os.path.basename(best)} ({size//1024} KB) -> {os.path.basename(target)}")
    results.append((num, slug, target, size))

print()
print("=== Summary ===")
have = sum(1 for r in results if r[2])
print(f"Have image: {have}/14")
print(f"Missing:    {14-have}/14")
print("Missing:", ", ".join(f"#{r[0]}" for r in results if not r[2]))
