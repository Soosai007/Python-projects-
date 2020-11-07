from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\python37\driver\chromedriver.exe")

driver.maximize_window()

# Step 2) Navigate to Facebook
driver.get("http://www.facebook.com")

# Step 3) Search & Enter the Email or Phone field & Enter Password

username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit   = driver.find_element_by_id("loginbutton")
username.send_keys("9677275126")
password.send_keys("falconsubash")
# Step 4) Click Login
submit.click()
