from pyzbar.pyzbar import decode
from PIL import Image
a=decode(Image.open('soosai.png'))
print(a)
