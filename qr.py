import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "https://www.youtube.com/@cbsee-zone665"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale=8)
url.png('myqr.png', scale=6)