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
browser.get("http://127.0.0.1:8000/sa/products/")

browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/a[1]").click()
time.sleep(1)

name = browser.find_element_by_id("id_base-name__en")
name.send_keys("Dell Laptop 2")
time.sleep(1)

short = browser.find_element_by_xpath("//*[@id='id_base-short_description__en']")
short.send_keys("Dell Inspiron i5 Personal Laptop")
time.sleep(1)

description = browser.find_element_by_xpath("//*[@id='id_base-description__en-editor-wrap']/div[2]/div[3]/div[2]")
description.send_keys("Dell Inspiron Core i5 8th Gen 8250U 2018 (8 GB RAM /2 TB HDD/Windows 10/MS Office/2 GB Graphics), 3576 Laptop, (15.6 inch, Black)")
time.sleep(1)

price = browser.find_element_by_xpath("//*[@id='id_shop1-default_price_value']")
price.send_keys("50000")
time.sleep(1)

save_attempt = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/div/button[1]")
save_attempt.click()


