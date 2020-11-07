from selenium import webdriver 
  
from PIL import Image 
  
# Here Chrome  will be used 
driver = webdriver.Chrome("C:\\python37\driver\chromedriver.exe") 
  
# URL of website 
url = "https://www.geeksforgeeks.org/"
  
# Opening the website 
driver.get(url) 
  
driver.save_screenshot("image.png") 
  
# Loading the image 
image = Image.open("image.png") 
  
# Showing the iamge 
image.show()

print("Screen shot captured")
