from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains
serviceObj=Service("C:/Users/hp/Desktop/browerDriver/geckodriver.exe")
driver=webdriver.Firefox(service=serviceObj)
driver.implicitly_wait(2)
def window():
    driver.get("https://www.yatra.com/")
    print(driver.title)
    print(driver.current_url)
    driver.maximize_window()
    action=ActionChains(driver)
    current_window=driver.current_window_handle
    print(current_window)
    driver.find_element(By.XPATH,"//a[@title='Bahrain Packages']//img[@class='conta iner large-banner']").click()
    all_windows=driver.window_handles
    driver.switch_to.window(all_windows[1])
    driver.find_element(By.XPATH,"//div[@id='srpRoot']//div[1]//div[2]//div[2]//div[1]//button[1]").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Book Now']").click()

    # driver.find_element(By.XPATH,"//button[normalize-space()='Book Now']").click()
    # driver.find_element(By.XPATH,"//button[normalize-space()='Select Another Flight']").click()
    driver.close()
    driver.switch_to.window(current_window)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    driver.get_screenshot_as_file("pic1.jpg")
window()