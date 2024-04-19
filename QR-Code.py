import qrcode
from PIL import Image
import io

urls = [
"https://os1-1.vercel.app/",
"https://os1-1.vercel.app/prototype/prototype-1",
"https://os1-1.vercel.app/prototype/prototype-2",
"https://os1-1.vercel.app/prototype/prototype-3",
"https://os1-1.vercel.app/prototype/prototype-4",
"https://os1-1.vercel.app/prototype/prototype-5"
]


qr_color = '#39FF14'
# qr_color = '#000000'


def generate_qr_code(url, color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,  # Higher error correction
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="transparent")
    # img = qr.make_image(fill_color=color, back_color="white")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

# Generate QR codes for each URL
qr_images = [generate_qr_code(url, qr_color) for url in urls]

# Save or display the QR codes
for idx, img_data in enumerate(qr_images):
    with open(f"qr_code_{idx+1}.png", "wb") as img_file:
        img_file.write(img_data)
