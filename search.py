from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("sample test case started")  
driver = webdriver.Chrome("C:\\python37\driver\chromedriver.exe")  
 
#maximize the window size  
driver.maximize_window()  
#navigate to the url  
driver.get("https://www.google.com/")  
#identify the Google search text box and enter the value  
driver.find_element_by_name("q").send_keys("Falcon infomatic")  
time.sleep(3)  
#click on the Google search button  
driver.find_element_by_name("btnK").click()  
time.sleep(3)  
#close the browser  
driver.close()  
  