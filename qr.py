import qrcode
import argparse

def generate_qr_code(text, file_name):
    """Generate QR code from input text and save it to file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def main():
    parser = argparse.ArgumentParser(description='Generate QR code from text.')
    parser.add_argument('text', type=str, help='Text to encode into QR code')
    parser.add_argument('filename', type=str, help='Filename to save QR code image (without extension)')
    args = parser.parse_args()

    file_name = args.filename + ".png"
    generate_qr_code(args.text, file_name)
    print(f"QR code successfully generated and saved to: {file_name}")

if __name__ == '__main__':
    main()
