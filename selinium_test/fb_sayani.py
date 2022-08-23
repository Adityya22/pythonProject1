import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/hp/Desktop/browerDriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sayanii.sengupta.6@gmail.com")#use your mail
driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("Sayani@6")#use your password
driver.find_element(By.XPATH, "//button[@name='login']").click()
driver.find_element(By.XPATH, "(//div[@class='q9uorilb l9j0dhe7 pzggbiyp du4w35lb'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Settings & privacy']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='/settings']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//div[@data-visualcompletion='ignore-dynamic'])[14]").click()
time.sleep(2)
# phone = driver.find_element(By.XPATH, "//ul[@class='uiList _4kg _6-h _704 _6-i']//span[@dir='ltr'][normalize-space()='079981 62391']").text
# assert "079981 62391" in phone

# print(phone)
driver.find_element(By.XPATH, "//span[normalize-space()='Blocking']").click
time.sleep(2)
driver.find_element(By.XPATH, "(//div[@aria-label='Edit'])[1]").click()
time.sleep(2)