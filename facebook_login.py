# automating browser to login facebook account
# Author: Aashish Sharma
# donejsdf
from selenium import webdriver

url = "https://www.facebook.com/"
browser = webdriver.Firefox()

browser.get(url)

user_email = browser.find_element_by_id("email")
user_email.send_keys("9779840221385")

user_password = browser.find_element_by_id("pass")
user_password.send_keys("71904638930")
user_password.submit()
