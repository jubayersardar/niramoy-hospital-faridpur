import os
import re

NEW_TOPBAR_INNER = '''    <div class="topbar-inner">
      <div class="topbar-track">
        <div class="topbar-left">
          <span class="topbar-item topbar-badge"><i class="fa-solid fa-user-doctor"></i> <strong>১৪+ বিশেষজ্ঞ চিকিৎসক</strong></span>
          <span class="topbar-item"><span class="emergency-badge"><i class="fa-solid fa-circle-exclamation"></i> ২৪/৭ ইমার্জেন্সি</span></span>
          <span class="topbar-item"><i class="fa-solid fa-phone-volume"></i> <a href="tel:+8801729171549"><strong>০১৭২৯-১৭১৫৪৯</strong></a></span>
          <span class="topbar-item"><i class="fa-solid fa-phone"></i> <a href="tel:+8801734089489"><strong>০১৭৩৪-০৮৯৪৮৯</strong></a></span>
        </div>
        <div class="topbar-right">
          <span class="topbar-item"><i class="fa-solid fa-truck-medical"></i> <a href="tel:+8801731827110"><strong>০১৭৩১-৮২৭১১০</strong> (24/7)</a></span>
          <span class="topbar-social">
            <a href="https://www.facebook.com/p/%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A7%9F-%E0%A6%B9%E0%A6%B8%E0%A6%AA%E0%A6%BF%E0%A6%9F%E0%A6%BE%E0%A6%B2-%E0%A6%AB%E0%A6%B0%E0%A6%BF%E0%A6%A6%E0%A6%AA%E0%A7%81%E0%A6%B0-61577130113409/" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="https://wa.me/8801731827110" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
          </span>
        </div>
      </div>
      <div class="topbar-track topbar-track-clone" aria-hidden="true">
        <div class="topbar-left">
          <span class="topbar-item topbar-badge"><i class="fa-solid fa-user-doctor"></i> <strong>১৪+ বিশেষজ্ঞ চিকিৎসক</strong></span>
          <span class="topbar-item"><span class="emergency-badge"><i class="fa-solid fa-circle-exclamation"></i> ২৪/৭ ইমার্জেন্সি</span></span>
          <span class="topbar-item"><i class="fa-solid fa-phone-volume"></i> <a href="tel:+8801729171549"><strong>০১৭২৯-১৭১৫৪৯</strong></a></span>
          <span class="topbar-item"><i class="fa-solid fa-phone"></i> <a href="tel:+8801734089489"><strong>০১৭৩৪-০৮৯৪৮৯</strong></a></span>
        </div>
        <div class="topbar-right">
          <span class="topbar-item"><i class="fa-solid fa-truck-medical"></i> <a href="tel:+8801731827110"><strong>০১৭৩১-৮২৭১১০</strong> (24/7)</a></span>
          <span class="topbar-social">
            <a href="https://www.facebook.com/p/%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A7%9F-%E0%A6%B9%E0%A6%B8%E0%A6%AA%E0%A6%BF%E0%A6%9F%E0%A6%BE%E0%A6%B2-%E0%A6%AB%E0%A6%B0%E0%A6%BF%E0%A6%A6%E0%A6%AA%E0%A7%81%E0%A6%B0-61577130113409/" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="https://wa.me/8801731827110" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
          </span>
        </div>
      </div>
    </div>'''

def update_topbars():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    pattern = re.compile(r'<div class="topbar-inner">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
    # Better pattern: find from <div class="topbar-inner"> to </div>\s*</div>\s*</div> before <header
    
    html_files = []
    for root_dir, _, files in os.walk(root):
        if '.git' in root_dir: continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root_dir, f))
                
    count = 0
    for fpath in html_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '<div class="topbar-inner">' in content:
            # Replace inner topbar
            # Find start of <div class="topbar-inner"> and end before </div>\s*</div>\s*<header
            sub_pattern = r'<div class="topbar-inner">.*?</div>\s*</div>\s*</div>'
            match = re.search(r'<div class="topbar-inner">[\s\S]*?</div>\s*</div>\s*</div>', content)
            if match:
                replacement = f"{NEW_TOPBAR_INNER}\n  </div>\n</div>"
                new_content = content[:match.start()] + replacement + content[match.end():]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                rel = os.path.relpath(fpath, root)
                print(f"[OK] Updated topbar in {rel}")
                
    print(f"\nSuccessfully updated topbar in {count} HTML files!")

if __name__ == '__main__':
    update_topbars()
