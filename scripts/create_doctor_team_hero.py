import os
from PIL import Image, ImageDraw, ImageFilter, ImageOps

def create_doctor_team_banner():
    width = 1600
    height = 900
    
    # 1. Base hospital background (modern consultation room / hospital corridor)
    bg_path = 'images/hero/slide-2.jpg'
    if os.path.exists(bg_path):
        base_bg = Image.open(bg_path).convert('RGB')
        base_bg = ImageOps.fit(base_bg, (width, height), method=Image.Resampling.LANCZOS)
        base_bg = base_bg.filter(ImageFilter.GaussianBlur(radius=6))
    else:
        base_bg = Image.new('RGB', (width, height), color=(10, 35, 60))
        
    # Dark gradient overlay for text readability
    overlay = Image.new('RGBA', (width, height), (0, 18, 38, 150))
    base_bg = base_bg.convert('RGBA')
    combined = Image.alpha_composite(base_bg, overlay)
    
    # 2. Four real specialist doctors of Niramoy Hospital
    doc_files = [
        'images/doctors/01-abu-bakar.jpg',
        'images/doctors/03-shrabanti.png',
        'images/doctors/02-riyad-bappy.jpg',
        'images/doctors/08-sourav.jpg'
    ]
    
    # Render 4 elegant circular portraits with glass glow
    diameter = 240
    spacing = 50
    total_w = (diameter * 4) + (spacing * 3)
    start_x = (width - total_w) // 2
    avatar_y = 390
    
    for i, doc_path in enumerate(doc_files):
        if not os.path.exists(doc_path):
            continue
        doc_img = Image.open(doc_path).convert('RGBA')
        doc_img = ImageOps.fit(doc_img, (diameter, diameter), method=Image.Resampling.LANCZOS)
        
        # Circle mask
        mask = Image.new('L', (diameter, diameter), 0)
        m_draw = ImageDraw.Draw(mask)
        m_draw.ellipse((0, 0, diameter, diameter), fill=255)
        
        card_x = start_x + i * (diameter + spacing)
        
        # Soft shadow
        shadow = Image.new('RGBA', (diameter + 40, diameter + 40), (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(shadow)
        s_draw.ellipse((15, 15, diameter + 25, diameter + 25), fill=(0, 0, 0, 200))
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=12))
        combined.paste(shadow, (card_x - 20, avatar_y - 10), shadow)
        
        # Outer Glowing Ring
        ring = Image.new('RGBA', (diameter + 16, diameter + 16), (0, 0, 0, 0))
        r_draw = ImageDraw.Draw(ring)
        r_draw.ellipse((0, 0, diameter + 16, diameter + 16), outline=(0, 168, 107, 230), width=6)
        combined.paste(ring, (card_x - 8, avatar_y - 8), ring)
        
        # Inner White Border
        border = Image.new('RGBA', (diameter + 4, diameter + 4), (0, 0, 0, 0))
        b_draw = ImageDraw.Draw(border)
        b_draw.ellipse((0, 0, diameter + 4, diameter + 4), outline=(255, 255, 255, 240), width=3)
        combined.paste(border, (card_x - 2, avatar_y - 2), border)
        
        # Paste Doctor Avatar
        combined.paste(doc_img, (card_x, avatar_y), mask)
        
    out_path = 'images/hero/hero-doctors-group.jpg'
    combined.convert('RGB').save(out_path, 'JPEG', quality=92)
    print(f'[OK] Generated {out_path} ({os.path.getsize(out_path)//1024} KB)')

if __name__ == '__main__':
    create_doctor_team_banner()
