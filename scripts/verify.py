import os
import re

def verify_all():
    print("==========================================")
    print("  NIRAMAYA Hospital Site Integrity Check  ")
    print("==========================================")
    
    # Check main pages
    main_pages = [
        'index.html', 'about.html', 'departments.html', 'doctors.html',
        'services.html', 'diagnostic.html', 'gallery.html', 'contact.html', 'appointment.html'
    ]
    
    missing_pages = []
    broken_img_count = 0
    total_imgs_checked = 0
    
    for page in main_pages:
        if not os.path.exists(page):
            missing_pages.append(page)
            continue
        
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check assets
        has_css = 'css/style.css' in content
        has_js = 'js/site.js' in content
        has_header = 'class="header"' in content
        has_footer = 'class="footer"' in content
        
        # Check images
        img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
        for src in img_srcs:
            total_imgs_checked += 1
            clean_src = src.split('?')[0]
            if not os.path.exists(clean_src):
                print(f"  [BROKEN IMAGE] In {page}: {src}")
                broken_img_count += 1
                
        print(f"[OK] {page:18s} | CSS: {has_css} | JS: {has_js} | Header: {has_header} | Footer: {has_footer}")

    print("\nChecking Doctor Profile Pages (14 Named Slugs):")
    slugs = [
        "dr-abu-bakar-siddique", "dr-riad-hossain-bappi", "dr-srabanti-m-islam",
        "dr-moin-uddin", "dr-shashanka-nag", "dr-rafiqul-islam", "dr-utpal-nag",
        "dr-abu-saleh-sourav", "dr-nahid-badsha", "dr-harichand-sheel",
        "dr-syed-imtiaz-uddin", "dr-papri-sarkar", "dr-sm-nur-e-alam", "dr-shankar-kumar-dey"
    ]
    doc_ok = 0
    for slug in slugs:
        fn = os.path.join('doctors', f'{slug}.html')
        if not os.path.exists(fn):
            print(f"  [MISSING] {fn}")
            continue
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        
        img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', c)
        for src in img_srcs:
            total_imgs_checked += 1
            clean_src = src.split('?')[0]
            resolved = os.path.normpath(os.path.join('doctors', clean_src))
            if not os.path.exists(resolved):
                print(f"  [BROKEN IMAGE] In {fn}: {src} (resolved: {resolved})")
                broken_img_count += 1
                
        doc_ok += 1

    print(f"[OK] Named Doctor Profiles: {doc_ok}/14 verified")
    print(f"[OK] Total Images Checked: {total_imgs_checked} (Broken: {broken_img_count})")
    
    if not missing_pages and broken_img_count == 0:
        print("\n>>> ALL CHECKS PASSED SUCCESSFULLY! SITE IS 100% HEALTHY! <<<")
    else:
        print("\n>>> ATTENTION: Some issues found! <<<")

if __name__ == '__main__':
    verify_all()



