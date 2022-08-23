import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

serviceObj = Service("C:/Users/hp/Desktop/browerDriver/chromedriver.exe")
driver = webdriver.Chrome(service=serviceObj)
driver.implicitly_wait(10)
action = ActionChains(driver)
driver.get("https://www.amazon.in/")
# driver.get("https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1_sspa?crid=UG16UDJQT2FA&keywords=iphone13&qid=1660644564&sprefix=iphone13%2Caps%2C609&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0pPR0JVREQ3UkhaJmVuY3J5cHRlZElkPUEwMTM0MTQxMzZYSlM4NFdOWEZJTyZlbmNyeXB0ZWRBZElkPUEwNzAwODIyMVRDV1hPWU04TlUwRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


def search_iphone():
    driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("iphone13")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    # action.move_to_element(driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")).perform()
    time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "div.s-result-item.s-asin:nth-child(3) h2 a").click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-asin="B09G9BL5CP"] h2 a').click()
    windowsopened2 = driver.window_handles
    print(len(windowsopened2))
    driver.switch_to.window(windowsopened2[1])
    # driver.execute_script("window.scrollTo(0,700);")
    driver.find_element(By.XPATH, "//input[@id='buy-now-button']").click()
    driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys('test')
    driver.find_element(By.XPATH, "//input[@id='continue']").click()
    # driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys('12345')
    # driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
    resp = driver.find_element(By.TAG_NAME, "h4").text
    print(resp)
    assert resp == "There was a problem", "something went wrong"
    driver.close()
    driver.switch_to.window(windowsopened2[0])


driver.find_element(By.XPATH, "//select[@id='searchDropdownBox']").click()
time.sleep(2)
options = driver.find_elements(By.XPATH, "//select[@id='searchDropdownBox']/option")
for option in options:
    if option.text == "Electronics":
        option.click()
        search_iphone()
        break
driver.close()
