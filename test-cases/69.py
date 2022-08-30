from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000/sa/login/?next=/sa/") 
time.sleep(1)