import pytesseract
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #exe file for using ocr 

img=Image.open('1.jpg') #to get image from our pc 
text=pytesseract.image_to_string(img) 
print(text)
