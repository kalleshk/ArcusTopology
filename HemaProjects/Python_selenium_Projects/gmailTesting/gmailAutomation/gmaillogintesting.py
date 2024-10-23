import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzA2Mjk3NzgxLCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D")
driver.find_element(By.NAME, "email").send_keys("example@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("example1234")
driver.implicitly_wait(4)

driver.find_element(By.ID,"loginbutton").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M9.464 1.2')]").send_keys(Keys.ENTER)
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//*[name()='g' and contains(@mask,'url(#:Rqir')]//*[name()='image' and contains(@x,'0')]").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Log out']")
driver.implicitly_wait(4)
print("test pass")
driver.quit()