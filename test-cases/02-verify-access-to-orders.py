from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service('C:/Users/Dev/Desktop/chromedriver/chromedriver.exe')
browser=webdriver.Chrome(service=s)
url="http://127.0.0.1:8000/sa/login/?next=/sa/"
browser.get(url)
time.sleep(1)
username = browser.find_element(By.ID,"id_username")
password = browser.find_element(By.ID,"id_password")
username.send_keys("admin@gmail.com")
password.send_keys("1234")
login_attempt = browser.find_element(By.XPATH, "//*[@type='submit']")
login_attempt.submit()
browser.get("http://127.0.0.1:8000/sa/orders/") 

element = browser.find_element(By.TAG_NAME,'h1')
if element.text == 'Orders':
    print("Pass")
else:
    print("Fail")
