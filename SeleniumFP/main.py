from selenium import webdriver

# chrome_driver = "D:\Mathi\dev\chromedriver" (direccion donde se descargo el webdriver)
#
# driver = webdriver.Chrome(executable_path=chrome_driver) (se almacena el ejecutable)
#
# driver.get("https://www.amazon.es/amazon-kindle-oasis-8-gb-luz-calida-ajustable-resistente-al-agua-grafito/dp/B07L5GDTYY/ref=sr_1_6_sspa?crid=TRVZ1ES8NIB6&keywords=kindle&qid=1641820303&s=computers&sprefix=kindle%2Ccomputers%2C2047&sr=1-6-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWDBRM0ZISUdVNVhOJmVuY3J5cHRlZElkPUEwNjMxMjgxM04wRUVHUVNSR0VFTyZlbmNyeXB0ZWRBZElkPUEwODE0Nzg2MU5FTFVLVUZJM0c3JndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
# price = driver.find_element_by_class_name("a-offscreen")
# print(price.text)
# driver.quit()

chrome_driver = "D:\Mathi\dev\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.python.org/")
event_time = driver.find_elements_by_css_selector(".event-widget time")
#adentro del event widget buscamos los elementos con la etiqueta time
event_name = driver.find_elements_by_css_selector(".event-widget a")

events = {}

for n in range(len(event_time)):
    events[n]={
        "time": event_time[n].text,
        "name": event_name[n].text
    }
print(events)



