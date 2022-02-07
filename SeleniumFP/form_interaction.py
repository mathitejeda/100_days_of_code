from selenium import webdriver
from selenium.webdriver.common.keys import Keys

NAME = "name"
LAST_NAME = "lastname"
EMAIL = "name.lastname@dummy.com"

chrome_driver = "D:\Mathi\dev\chromedriver"

driver = webdriver.Chrome(chrome_driver)

driver.get("https://secure-retreat-92358.herokuapp.com/")

form_name = driver.find_element_by_name("fName")
form_last_name = driver.find_element_by_name("lName")
form_mail = driver.find_element_by_name("email")

submit_btn = driver.find_element_by_tag_name("button")

form_name.send_keys(NAME)
form_last_name.send_keys(LAST_NAME)
form_mail.send_keys(EMAIL)

submit_btn.click()
