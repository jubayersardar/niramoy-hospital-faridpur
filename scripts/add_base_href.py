import os
import re

def update_all_html_files():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # 1. Main Pages in root
    main_pages = [
        'index.html', 'about.html', 'departments.html', 'doctors.html',
        'services.html', 'diagnostic.html', 'gallery.html', 'contact.html', 'appointment.html'
    ]
    
    for page in main_pages:
        fpath = os.path.join(root_dir, page)
        if not os.path.exists(fpath): continue
        
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Ensure <base href="/"> is right after <head>
        if '<base href="/">' not in content:
            content = re.sub(r'<head(\s*[^>]*)>', r'<head\1>\n<base href="/">', content, count=1)
            
        # Ensure asset paths are clean
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Added base href to {page}")

    # 2. Doctor sub-pages
    doc_dir = os.path.join(root_dir, 'doctors')
    if os.path.exists(doc_dir):
        for fname in os.listdir(doc_dir):
            if fname.endswith('.html'):
                fpath = os.path.join(doc_dir, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if '<base href="/">' not in content:
                    content = re.sub(r'<head(\s*[^>]*)>', r'<head\1>\n<base href="/">', content, count=1)
                
                # Replace relative ../ with clean paths now that base href is set
                content = content.replace('href="../css/style.css', 'href="css/style.css')
                content = content.replace('src="../js/site.js', 'src="js/site.js')
                content = content.replace('src="../images/', 'src="images/')
                content = content.replace('href="../', 'href="')
                
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"[OK] Added base href to doctors/{fname}")

if __name__ == '__main__':
    update_all_html_files()
    print("All HTML files updated with <base href=\"/\">!")
