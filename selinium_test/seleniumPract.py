from selenium import webdriver
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

servObject=Service("C:/Users/hp/Desktop/browerDriver/msedgedriver.exe")
driver=webdriver.Edge(service=servObject)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(1)
result=driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(result))


for i in result:
    i.find_element(By.XPATH,"div/button").click()       #add to cart all element
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
driver.find_element(By.XPATH,".//button[text()='Place Order']").click()
