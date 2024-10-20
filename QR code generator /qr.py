import qrcode
from PIL import Image, ImageDraw
import os

def generate_qr_code(data, filename, box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_L, fill_color='black', back_color='white', logo_path=None):
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(version=1, box_size=box_size, border=border, error_correction=error_correction)
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create the QR code image
        img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
        
        # Optionally add a logo to the center of the QR code
        if logo_path and os.path.exists(logo_path):
            logo = Image.open(logo_path)
            # Resize logo
            logo_size = (img.size[0] // 4, img.size[1] // 4)
            logo = logo.resize(logo_size, Image.ANTIALIAS)
            
            # Calculate position to paste the logo
            pos = ((img.size[0] - logo_size[0]) // 2, (img.size[1] - logo_size[1]) // 2)
            img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
        
        # Save the QR code
        img.save(filename)
        print(f"QR code saved as {filename}")
    
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to generate QR code. Please check your input and try again.")
    
def get_error_correction_level(level):
    error_correction_dict = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }
    return error_correction_dict.get(level.upper(), qrcode.constants.ERROR_CORRECT_L)

def main():
    print("Welcome to the QR Code Generator!")
    
    data = input("Enter the text or URL for the QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ")
    
    # Validate filename
    if not filename.endswith(('.png', '.jpg', '.jpeg')):
        print("Invalid file format. Defaulting to qr_code.png")
        filename = 'qr_code.png'
    
    # Collect and validate optional inputs
    try:
        box_size = int(input("Enter the box size (default 10): ") or 10)
        border = int(input("Enter the border size (default 4): ") or 4)
    except ValueError:
        print("Invalid input. Using default values for box size (10) and border (4).")
        box_size, border = 10, 4
    
    error_correction = input("Enter the error correction level (L, M, Q, H, default L): ").upper() or 'L'
    error_correction = get_error_correction_level(error_correction)
    
    fill_color = input("Enter the fill color (default black): ") or 'black'
    back_color = input("Enter the background color (default white): ") or 'white'
    
    # Logo embedding option
    logo_path = input("Enter the logo file path (optional, leave blank if not needed): ").strip()
    if logo_path and not os.path.exists(logo_path):
        print("Logo file not found, proceeding without logo.")
        logo_path = None
    
    generate_qr_code(data, filename, box_size, border, error_correction, fill_color, back_color, logo_path)

if __name__ == "__main__":
    main()
