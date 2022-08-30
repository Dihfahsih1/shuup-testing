
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
browser.get("http://127.0.0.1:8000/sa/users/")

browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/a[1]").click()
time.sleep(1)

name = browser.find_element_by_id("id_username")
name.send_keys("richie")
time.sleep(1)

name = browser.find_element_by_id("id_email")
name.send_keys("richie@gmail.com")
time.sleep(1)

name = browser.find_element_by_id("id_first_name")
name.send_keys("Richa")
time.sleep(1)

name = browser.find_element_by_id("id_last_name")
name.send_keys("Chadda")
time.sleep(1)

name = browser.find_element_by_id("id_password")
name.send_keys("12345")
time.sleep(1)

save_attempt = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/button")
save_attempt.click()


