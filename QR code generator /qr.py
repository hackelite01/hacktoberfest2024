import qrcode
from PIL import Image

def generate_qr_code(data, filename, box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_L, fill_color='black', back_color='white'):
    qr = qrcode.QRCode(version=1, box_size=box_size, border=border, error_correction=error_correction)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill=fill_color, back_color=back_color)
    img.save(filename)

def main():
    print("Welcome to the QR Code Generator!")
    data = input("Enter the text or URL for the QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ")
    
    box_size = int(input("Enter the box size (default 10): ") or 10)
    border = int(input("Enter the border size (default 4): ") or 4)
    error_correction = input("Enter the error correction level (L, M, Q, H, default L): ").upper() or 'L'
    
    error_correction_dict = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }

    fill_color = input("Enter the fill color (default black): ") or 'black'
    back_color = input("Enter the background color (default white): ") or 'white'
    
    if error_correction not in error_correction_dict:
        print("Invalid error correction level, defaulting to L.")
        error_correction = 'L'
        
    generate_qr_code(data, filename, box_size, border, error_correction_dict[error_correction], fill_color, back_color)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    main()
