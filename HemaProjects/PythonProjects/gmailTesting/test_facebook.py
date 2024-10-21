import time
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.facebook.com/login/")
driver.find_element(By.NAME, "email").send_keys("hemashiva957@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("Hemashiva9579606224671")


driver.implicitly_wait(4)

driver.find_element(By.ID,"loginbutton").send_keys(Keys.ENTER)

print("test pass")
driver.quit()
