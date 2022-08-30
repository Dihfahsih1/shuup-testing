from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000/sa/login/?next=/sa/") 
time.sleep(1)
username = browser.find_element_by_id("id_username")
password = browser.find_element_by_id("id_password")
username.send_keys("palak1")
password.send_keys("palak1")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(1)
browser.get("http://127.0.0.1:8000/sa/discounts_coupon_codes/new/") 
browser.find_element_by_xpath("//*[@id='id_code']").send_keys("NBA13")
browser.find_element_by_xpath("//*[@id='id_usage_limit_customer']").send_keys("10")
browser.find_element_by_xpath("//*[@id='id_usage_limit']").send_keys("1000")
browser.find_element_by_xpath("//*[@id='id_active']").click()
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/div/button[1]").click()



