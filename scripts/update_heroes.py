import os
import re

hero_map = {
    'about.html': 'hero-about.jpg',
    'departments.html': 'hero-departments.jpg',
    'doctors.html': 'hero-doctors.jpg',
    'services.html': 'hero-services.jpg',
    'diagnostic.html': 'hero-diagnostic.jpg',
    'gallery.html': 'hero-gallery.jpg',
    'contact.html': 'hero-contact.jpg',
    'appointment.html': 'hero-appointment.jpg'
}

for page, img_name in hero_map.items():
    if not os.path.exists(page):
        print(f"Skipping missing: {page}")
        continue
        
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Update css link for cache busting
    content = re.sub(r'href="css/style\.css(\?[^"]*)?"', 'href="css/style.css?v=2.2"', content)
    
    # 2. Update page-hero section tag with class and inline style
    hero_cls = f"page-hero--{page.replace('.html', '')}"
    new_tag = f'<section class="page-hero has-bg {hero_cls}" style="background-image: url(\'images/hero/{img_name}\');">'
    
    # Replace existing page-hero section tag
    content = re.sub(r'<section class="page-hero[^>]*>', new_tag, content)
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"[UPDATED] {page} -> {new_tag}")

print("\nDone updating all hero sections!")
