from PIL import Image
import qrcode
import os

# Define the directory to save the images
directory = 'qr_codes'
if not os.path.exists(directory):
    os.makedirs(directory)

# Taking UPI ID as an input
upi_id = input("Enter your UPI ID = ")

# Define the payment URLs based on the UPI ID and the payment app
phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR codes for each payment app
phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR codes to image files
phonepay_path = os.path.join(directory, 'phonepay_qr.png')
paytm_path = os.path.join(directory, 'paytm_qr.png')
google_pay_path = os.path.join(directory, 'google_pay_qr.png')

# Save images
phonepay_qr.save(phonepay_path)
paytm_qr.save(paytm_path)
google_pay_qr.save(google_pay_path)

print(f"QR codes have been generated and saved as:\n{phonepay_path}\n{paytm_path}\n{google_pay_path}")


# Open images using PIL
def open_image(file_path):
    with Image.open(file_path) as img:
        img.show()
        
        
# Open the images
open_image(phonepay_path)
open_image(paytm_path)
open_image(google_pay_path)
