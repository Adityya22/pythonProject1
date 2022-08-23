import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

servobj = Service("C:/Users/hp/Desktop/browerDriver/chromedriver.exe")
driver = webdriver.Chrome(service=servobj)
class Yatra():

    def get_element_by_id(self):
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        # driver.get("https://www.google.com/")
        # driver.find_element_by_id("login-input").send_keys('test@test.com')
        driver.find_element(by=By.ID,value="login-input").send_keys('test@test.com')
        driver.find_element(byBy.ID,value="login-continue-btn").click()
        # driver.find_element_by_xpath("//input[@title='Search']").send_keys("youtube")
        time.sleep(4)

a = Yatra()
a.get_element_by_id()