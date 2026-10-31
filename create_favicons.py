import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\hk-travels-kolkata\assets\images"
os.makedirs(output_dir, exist_ok=True)

# 1. logo.svg
logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 100" width="480" height="100">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE68A" />
      <stop offset="50%" stop-color="#D4AF37" />
      <stop offset="100%" stop-color="#B45309" />
    </linearGradient>
    <linearGradient id="navyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F284E" />
      <stop offset="100%" stop-color="#051022" />
    </linearGradient>
  </defs>
  <!-- Sleek Winged Compass Crest -->
  <rect x="10" y="10" width="80" height="80" rx="18" fill="url(#navyGrad)" stroke="url(#goldGrad)" stroke-width="2.5" />
  <path d="M 28 50 C 35 34, 65 34, 72 50 C 65 66, 35 66, 28 50 Z" fill="none" stroke="url(#goldGrad)" stroke-width="2.5" />
  <polygon points="50,26 55,46 50,42 45,46" fill="#FDE68A" />
  <polygon points="50,74 55,54 50,58 45,54" fill="#D4AF37" />
  <circle cx="50" cy="50" r="5" fill="#D4AF37" stroke="#051022" stroke-width="1.5" />

  <!-- Typography -->
  <text x="106" y="52" font-family="'Plus Jakarta Sans', 'Inter', system-ui, sans-serif" font-size="34" font-weight="800" letter-spacing="2" fill="#FFFFFF">HK TRAVELS</text>
  <text x="108" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="600" letter-spacing="4" fill="#D4AF37">LUXURY FLEET &amp; CAR RENTAL</text>
</svg>'''

with open(os.path.join(output_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)

# 2. favicon.svg
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="favGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE68A" />
      <stop offset="50%" stop-color="#D4AF37" />
      <stop offset="100%" stop-color="#B45309" />
    </linearGradient>
    <linearGradient id="favNavy" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F284E" />
      <stop offset="100%" stop-color="#051022" />
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="100" height="100" rx="20" fill="url(#favNavy)" />
  <rect x="2" y="2" width="96" height="96" rx="18" fill="none" stroke="url(#favGold)" stroke-width="3" />
  <path d="M 22 50 C 30 30, 70 30, 78 50 C 70 70, 30 70, 22 50 Z" fill="none" stroke="url(#favGold)" stroke-width="3.5" />
  <polygon points="50,22 56,45 50,40 44,45" fill="#FDE68A" />
  <polygon points="50,78 56,55 50,60 44,55" fill="#D4AF37" />
  <circle cx="50" cy="50" r="6" fill="#D4AF37" />
</svg>'''

with open(os.path.join(output_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(favicon_svg)

# 3. Render PNGs using Pillow
size = 512
img = Image.new("RGBA", (size, size), (5, 16, 34, 255))
draw = ImageDraw.Draw(img)

# Outer metallic gold border
draw.rounded_rectangle([16, 16, size-16, size-16], radius=70, outline=(212, 175, 55, 255), width=14)

# Dynamic Highway Curves & Monogram
draw.arc([70, 160, 442, 350], start=0, end=360, fill=(212, 175, 55, 255), width=16)
# Center Compass
draw.polygon([(256, 80), (285, 230), (256, 205), (227, 230)], fill=(253, 230, 138, 255))
draw.polygon([(256, 432), (285, 282), (256, 307), (227, 282)], fill=(180, 83, 9, 255))
draw.ellipse([230, 230, 282, 282], fill=(212, 175, 55, 255), outline=(5, 16, 34, 255), width=6)

# Monogram HK
try:
    font = ImageFont.truetype("arialbd.ttf", 68)
    draw.text((256, 435), "HK TRAVELS", fill=(255, 255, 255, 255), font=font, anchor="mm")
except Exception:
    draw.text((200, 420), "HK TRAVELS", fill=(255, 255, 255, 255))

img.save(os.path.join(output_dir, "logo-512.png"))

img_180 = img.resize((180, 180), Image.Resampling.LANCZOS)
img_180.save(os.path.join(output_dir, "apple-touch-icon.png"))

img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
img_32.save(os.path.join(output_dir, "favicon-32x32.png"))

img.save(os.path.join(output_dir, "favicon.ico"), format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

print("HK Travels favicons and logos generated successfully!")
