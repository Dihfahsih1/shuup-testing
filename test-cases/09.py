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
browser.get("http://127.0.0.1:8000/sa/products/new/") 
time.sleep(1)
browser.find_element(By.XPATH,"//*[@id='id_base-name__en']").send_keys('Textile')
browser.find_element(By.XPATH,"//*[@id='id_shop1-default_price_value']").send_keys('12')
browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div/div/button[1]").click()