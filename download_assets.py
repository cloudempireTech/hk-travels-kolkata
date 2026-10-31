import os
import urllib.request
from PIL import Image

output_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\hk-travels-kolkata\assets\images"
os.makedirs(output_dir, exist_ok=True)

images = [
    ("hero-fallback.jpg", "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1600&q=80"),
    ("fleet-innova-crysta.jpg", "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=1200&q=80"),
    ("fleet-luxury-sedan.jpg", "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&w=1200&q=80"),
    ("fleet-tempo-traveller.jpg", "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?auto=format&fit=crop&w=1200&q=80"),
    ("airport-transfer-vip.jpg", "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80"),
    ("outstation-highway-drive.jpg", "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1200&q=80"),
    ("corporate-executive-cab.jpg", "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80"),
    ("wedding-convoy-luxury.jpg", "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80"),
    ("digha-beach-trip.jpg", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80"),
    ("chauffeur-professional.jpg", "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&w=1200&q=80"),
]

for filename, url in images:
    filepath = os.path.join(output_dir, filename)
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        
        with Image.open(filepath) as img:
            img = img.convert('RGB')
            if img.width > 1600:
                h = int(img.height * (1600 / img.width))
                img = img.resize((1600, h), Image.Resampling.LANCZOS)
            img.save(filepath, "JPEG", quality=85, optimize=True)
            print(f"Optimized {filename} ({img.width}x{img.height})")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("HK Travels image download and optimization complete!")
