

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service

# def a1():
servobj = Service("C:/Users/hp/Desktop/browerDriver/chromedriver.exe")
driver = webdriver.Chrome(service=servobj)

serv_obj = Service("C:/Users/hp/Desktop/browerDriver/msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
# driver.maximize_window()
driver.get("https://www.youtube.com/")
# print(driver.title)
# print(driver.current_url)
# driver.minimize_window()
driver.quit()
# driver.forward()

# a1()