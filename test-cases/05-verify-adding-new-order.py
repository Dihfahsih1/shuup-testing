from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome('C:/Users/Dev/Desktop/chromedriver/chromedriver.exe')
browser.get("http://127.0.0.1:8000/sa/login/?next=/sa/") 
time.sleep(1)
username = browser.find_element(By.ID,"id_username")
password = browser.find_element(By.ID,"id_password")
username.send_keys("admin@gmail.com")
password.send_keys("1234")
login_attempt = browser.find_element(By.XPATH,"//*[@type='submit']")
login_attempt.submit()
browser.get("http://127.0.0.1:8000/sa/orders/new/") 

element = browser.find_element(By.TAG_NAME,'h1')
if element.text == 'New order':
    print("Pass")
else:
    print("Fail")
    
    
# try:
#     login_attempt = browser.find_element(By.XPATH,"//*[@type='Submit']")
#     login_attempt.submit()
#     browser.get("http://127.0.0.1:8000/sa/orders/new/") 
# except Exception as e:
#     print(e)

# element = browser.find_element(By.TAG_NAME,'h1')
# if element.text == 'New order':
#     print("Pass")
# else:
#     print("Fail")