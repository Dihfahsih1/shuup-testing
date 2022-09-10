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
time.sleep(1)
browser.get("http://127.0.0.1:8000/sa/discounts/")
browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div/a[1]").click()
time.sleep(1)
browser.find_element(By.XPATH,"//*[@id='id_name']").send_keys('notebook')
browser.find_element(By.XPATH,"//*[@id='id_start_datetime']").send_keys('2019-10-18 17:18')
browser.find_element(By.XPATH,"//*[@id='id_end_datetime']").send_keys('2019-10-31 17:18')
browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div/div/button[1]").click()
browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div/div/button[1]").click()