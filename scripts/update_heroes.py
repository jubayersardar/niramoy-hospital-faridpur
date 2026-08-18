import os

pages = {
    'about.html': 'page-hero--about',
    'departments.html': 'page-hero--departments',
    'doctors.html': 'page-hero--doctors',
    'services.html': 'page-hero--services',
    'diagnostic.html': 'page-hero--diagnostic',
    'gallery.html': 'page-hero--gallery',
    'contact.html': 'page-hero--contact',
    'appointment.html': 'page-hero--appointment'
}

for page, hero_class in pages.items():
    if not os.path.exists(page):
        print(f'Missing: {page}')
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('<section class="page-hero">', f'<section class="page-hero has-bg {hero_class}">')
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {page} with {hero_class}')
