
import qrcode
from PIL import Image


# run this script python generate_qr.py

def generate_colored_qr_with_logo(url, logo_path):
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Using highest level of error correction
        box_size=10,
        border=5
    )

    # Add data to QR code object
    qr.add_data(url)
    qr.make(fit=True)

    # Make QR code image with custom colors
    img_qr_big = qr.make_image(fill_color='blue', back_color='white').convert('RGB')  # Blue and white colors

    # Load logo image
    logo = Image.open(logo_path)

    # Add a white border (clear zone) around the logo
    border_size = int(logo.size[0] * 0.1)  # 10% of logo's size
    logo_with_border = Image.new('RGB', (logo.size[0] + 2 * border_size, logo.size[1] + 2 * border_size), 'white')
    logo_with_border.paste(logo, (border_size, border_size))

    # Resize logo image to fit QR code size
    logo_size = int(img_qr_big.size[0] / 5)  # Making the logo smaller
    logo_resized = logo_with_border.resize((logo_size, logo_size))

    # Paste logo on center of QR code image
    pos = ((img_qr_big.size[0] - logo_resized.size[0]) // 2, (img_qr_big.size[1] - logo_resized.size[1]) // 2)
    img_qr_big.paste(logo_resized, pos)

    # Save QR code image
    img_qr_big.save('qrcode_colored.png')
    img_qr_big.show()

# Calling the function
generate_colored_qr_with_logo('https://example.com/', 'logo.png')


