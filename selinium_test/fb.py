import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/hp/Desktop/browerDriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='email']").send_keys("adityyasingh6010@gmail.com")  # use your mail
driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("$ingh@ditya22")  # use your password
driver.find_element(By.XPATH, "//button[@name='login']").click()
driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Your profile'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Settings & privacy']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='/settings']").click()
time.sleep(2)

# click mobile
driver.find_element(By.XPATH, "//span[normalize-space()='Mobile']").click()
# switch to the iframe
# iframe = driver.find_element(By.XPATH, "(//iframe[@class='mfclru0v kyj84mfa b6ax4al1 js4msrqk ggolc4ur iwso50tu f5m7p0br'])[1]")
# driver.switch_to.frame(iframe)
driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])

time.sleep(2)

num = driver.find_element(By.XPATH, "//ul[@class='uiList _4kg _6-h _704 _6-i']//span[@dir='ltr'][normalize-space()='086208 12140']").text
print(num)

# assert num == '1111'
# switch to the current frame
driver.switch_to.default_content()
# click blocking
driver.find_element(By.XPATH,"(//div[@class='alzwoclg cqf1kptm siwo0mpr gu5uzgus'])[7]").click()
time.sleep(2)
# click edit option in block user
driver.find_element(By.XPATH, "(//div)[352]").click()
# how to capture number of block user???=====>>need help!!
time.sleep(2)
# click close symbol
driver.find_element(By.XPATH, "//i[@class='gneimcpu oee9glnz']").click()
# click profile
driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Your profile'])[1]").click()
time.sleep(2)
# click logout
driver.find_element(By.XPATH, "(//div[@class='qmqpeqxj e7u6y3za qwcclf47 nmlomj2f i85zmo3j frfouenu bonavkto djs4p424 r7bn319e bdao358l fxk3tzhb jcxyg2ei om3e55n1 a5wdgl2o jvc6uz2b g90fjkqk'])[5]").click()
time.sleep(1)
driver.close()
