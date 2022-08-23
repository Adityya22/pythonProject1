import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service


service_obj=Service("C:/Users/hp/Desktop/browerDriver/msedgedriver.exe")
driver=webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
def select_radio():
    # get_radio=driver.find_elements(By.XPATH,"//input[@type='radio']")
    # print(len(get_radio))
    #
    # for radio in get_radio:
    #     if radio.get_attribute("value")=="radio2":
    #         radio.click()
    #         time.sleep(2)
    #         assert radio.is_selected()
    #         break
    # print(driver.title)
    # driver.close()
 #=====================================================================================
    get_radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
    get_radio[0].click()
    print(driver.title)
    assert get_radio[0].is_selected()
    # driver.close()
#====================================================================================

def disp_hide():
    print(driver.find_element(By.ID,"displayed-text").is_displayed())
    assert driver.find_element(By.ID,"displayed-text").is_displayed()
    driver.find_element(By.ID,"hide-textbox").click()
    time.sleep(2)
    print(driver.find_element(By.ID, "displayed-text").is_displayed())
# select_radio()
disp_hide()