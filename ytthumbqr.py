import qrcode
from PIL import Image
import requests
from io import BytesIO
import re

def extract_video_id(youtube_url):
    """Extraheert de video-ID uit een standaard- of embed-YouTube-link."""
    match = re.search(r"(?:v=|\/embed\/|\/vi\/|youtu\.be\/)([A-Za-z0-9_-]{11})", youtube_url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Geen geldige YouTube-link gevonden.")

def get_youtube_thumbnail(youtube_url):
    """Haalt de thumbnail op van een YouTube-video."""
    video_id = extract_video_id(youtube_url)
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    
    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception("Thumbnail niet gevonden.")

def generate_qr_code(url, size=150):
    """Genereert een QR-code voor de YouTube-link."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Hoge foutcorrectie
        box_size=10,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill="black", back_color="white")
    return qr_img.resize((size, size))

def combine_thumbnail_and_qr(youtube_url, output_file="output.png", qr_size_ratio=0.3):
    """Plaatst een QR-code in het midden van de YouTube-thumbnail."""
    try:
        thumbnail = get_youtube_thumbnail(youtube_url)
        
        # Bepaal de grootte van de QR-code als een percentage van de thumbnail
        qr_size = int(min(thumbnail.width, thumbnail.height) * qr_size_ratio)
        qr_code = generate_qr_code(youtube_url, qr_size)

        # Bereken de positie om de QR-code in het midden te plaatsen
        x_offset = (thumbnail.width - qr_code.width) // 2
        y_offset = (thumbnail.height - qr_code.height) // 2

        # Plak de QR-code op de thumbnail
        thumbnail.paste(qr_code, (x_offset, y_offset), qr_code.convert("RGBA"))  # Transparante achtergrond
        thumbnail.save(output_file)
        
        print(f"Afbeelding opgeslagen als {output_file}")

    except Exception as e:
        print(f"Fout: {e}")

# Gebruik de functie met een YouTube-embed-link
youtube_embed_link = "https://www.youtube.com/embed/AF8d72mA41M?si=-2jLw0ajdfY6VGUG"
combine_thumbnail_and_qr(youtube_embed_link, "youtube_qr_centered.png")
