from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "D:\Mathi\dev\chromedriver"

driver = webdriver.Chrome(chrome_driver)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

magic_number = driver.find_element_by_css_selector("#articlecount a")
print(magic_number.text)

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)