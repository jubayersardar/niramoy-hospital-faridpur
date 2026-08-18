import os
import re
import shutil

DOCTOR_SLUGS = {
    "01": "dr-abu-bakar-siddique",
    "02": "dr-riad-hossain-bappi",
    "03": "dr-srabanti-m-islam",
    "04": "dr-moin-uddin",
    "05": "dr-shashanka-nag",
    "06": "dr-rafiqul-islam",
    "07": "dr-utpal-nag",
    "08": "dr-abu-saleh-sourav",
    "09": "dr-nahid-badsha",
    "10": "dr-harichand-sheel",
    "11": "dr-syed-imtiaz-uddin",
    "12": "dr-papri-sarkar",
    "13": "dr-sm-nur-e-alam",
    "14": "dr-shankar-kumar-dey"
}

def create_named_doctor_html_files():
    doc_dir = 'doctors'
    for num_id, slug in DOCTOR_SLUGS.items():
        src_file = os.path.join(doc_dir, f"{num_id}.html")
        dst_file = os.path.join(doc_dir, f"{slug}.html")
        if not os.path.exists(src_file):
            print(f"Missing source: {src_file}")
            continue
            
        with open(src_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update "Other Doctors" cards links inside the doctor page
        for other_num, other_slug in DOCTOR_SLUGS.items():
            content = re.sub(rf'href="{other_num}"', f'href="{other_slug}"', content)
            content = re.sub(rf'href="{other_num}\.html"', f'href="{other_slug}"', content)
            content = re.sub(rf'href="\.\./appointment\?doc={other_num}"', f'href="../appointment?doc={other_slug}"', content)
            
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        # Also update the 01.html to 14.html files so both work
        with open(src_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"[OK] Created doctors/{slug}.html (and updated {num_id}.html)")

def update_site_doctor_links():
    pages = [
        'index.html', 'about.html', 'departments.html', 'doctors.html',
        'services.html', 'diagnostic.html', 'gallery.html', 'contact.html', 'appointment.html'
    ]
    
    for page in pages:
        if not os.path.exists(page): continue
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for num_id, slug in DOCTOR_SLUGS.items():
            # Replace doctors/01 or doctors/01.html with doctors/slug
            content = re.sub(rf'href="doctors/{num_id}(\.html)?"', f'href="doctors/{slug}"', content)
            # Replace appointment?doc=01 or appointment.html?doc=01 with appointment?doc=slug
            content = re.sub(rf'href="appointment(\.html)?\?doc={num_id}"', f'href="appointment?doc={slug}"', content)
            
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated doctor links in {page}")

if __name__ == '__main__':
    create_named_doctor_html_files()
    update_site_doctor_links()
    print("\nSuccessfully updated all doctor URLs to name-based clean slugs!")
