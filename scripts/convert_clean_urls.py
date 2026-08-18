import os
import re

def convert_main_pages():
    main_files = [
        'index.html', 'about.html', 'departments.html', 'doctors.html',
        'services.html', 'diagnostic.html', 'gallery.html', 'contact.html', 'appointment.html'
    ]
    
    replacements = [
        (r'href="index\.html"', 'href="./"'),
        (r'href="about\.html"', 'href="about"'),
        (r'href="departments\.html"', 'href="departments"'),
        (r'href="doctors\.html"', 'href="doctors"'),
        (r'href="services\.html"', 'href="services"'),
        (r'href="diagnostic\.html"', 'href="diagnostic"'),
        (r'href="gallery\.html"', 'href="gallery"'),
        (r'href="contact\.html"', 'href="contact"'),
        (r'href="appointment\.html"', 'href="appointment"'),
        (r'href="appointment\.html\?', 'href="appointment?'),
        (r'href="departments\.html#', 'href="departments#'),
        (r'href="doctors/(\d+)\.html"', r'href="doctors/\1"'),
    ]
    
    for fn in main_files:
        if not os.path.exists(fn): continue
        with open(fn, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for pat, rep in replacements:
            content = re.sub(pat, rep, content)
            
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Converted clean links in {fn}")

def convert_doctor_pages():
    doc_replacements = [
        (r'href="\.\./index\.html"', 'href="../"'),
        (r'href="\.\./about\.html"', 'href="../about"'),
        (r'href="\.\./departments\.html"', 'href="../departments"'),
        (r'href="\.\./doctors\.html"', 'href="../doctors"'),
        (r'href="\.\./services\.html"', 'href="../services"'),
        (r'href="\.\./diagnostic\.html"', 'href="../diagnostic"'),
        (r'href="\.\./gallery\.html"', 'href="../gallery"'),
        (r'href="\.\./contact\.html"', 'href="../contact"'),
        (r'href="\.\./appointment\.html"', 'href="../appointment"'),
        (r'href="\.\./appointment\.html\?', 'href="../appointment?'),
        (r'href="\.\./departments\.html#', 'href="../departments#'),
        (r'href="(\d+)\.html"', r'href="\1"'),
    ]
    
    for i in range(1, 15):
        fn = os.path.join('doctors', f'{i:02d}.html')
        if not os.path.exists(fn): continue
        with open(fn, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for pat, rep in doc_replacements:
            content = re.sub(pat, rep, content)
            
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Converted clean links in {fn}")

if __name__ == '__main__':
    convert_main_pages()
    convert_doctor_pages()
    print("\nAll internal links converted to Clean URLs without .html!")
