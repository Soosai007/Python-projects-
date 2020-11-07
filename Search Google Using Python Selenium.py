
# import webdriver 
from selenium import webdriver 
  
# create webdriver object 
driver = webdriver.Chrome("C:\\python37\driver\chromedriver.exe")
  
  
# get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 
  
# get element  
element = driver.find_element_by_id("gsc-i-id2") 
  
# send keys  
element.send_keys("python")


