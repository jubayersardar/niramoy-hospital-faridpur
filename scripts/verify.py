import os
doc_dir = r'D:\minimax\New folder\website\doctors'
ok = 0; has_img = 0
for i in range(1, 15):
    fn = os.path.join(doc_dir, f'{i:02d}.html')
    if not os.path.exists(fn): continue
    html = open(fn, encoding='utf-8').read()
    has_home = '../index.html' in html
    has_img_path = '../images/doctors/' in html
    has_appt = '#appointment' in html
    has_other_docs = 'other-doc-card' in html
    if has_home and has_img_path and has_appt and has_other_docs:
        ok += 1
    if has_img_path: has_img += 1
print(f'OK: {ok}/14 doctor pages (with all sections)')
print(f'With image: {has_img}/14')
print()
print('Main pages:')
for f in ['index.html','about.html','departments.html','doctors.html','services.html','diagnostic.html','gallery.html','contact.html','appointment.html']:
    p = os.path.join(r'D:\minimax\New folder\website', f)
    if os.path.exists(p):
        size = os.path.getsize(p) // 1024
        html = open(p, encoding='utf-8').read()
        has_css = 'css/style.css' in html
        has_js = 'js/site.js' in html
        has_header = 'class="header"' in html
        has_footer = 'class="footer"' in html
        print(f'  {f:20s}  {size:>3}KB  css={has_css}  js={has_js}  hdr={has_header}  ftr={has_footer}')
