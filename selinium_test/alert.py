import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service("C:/Users/hp/Desktop/browerDriver/geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Aditya")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
time.sleep(1)
alert1 = driver.switch_to.alert
alertText = alert1.text
print(alertText)
time.sleep(2)
alert1.accept()
# alert1.dismiss()
