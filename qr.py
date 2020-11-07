import pyqrcode

qr = pyqrcode.create('75')
qr.png('soosai.png', scale=12)
