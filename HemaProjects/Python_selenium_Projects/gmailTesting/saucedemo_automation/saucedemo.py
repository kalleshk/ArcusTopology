import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(100)
driver.get("https://www.orangehrm.com/en/contact-sales/")

# driver.find_element(By.NAME, "user-name").send_keys("standard_user")
# driver.find_element(By.NAME, "password").send_keys("secret_sauce")
# driver.implicitly_wait(4)
ele=driver.find_element(By.CSS_SELECTOR, "#Form_getForm_Country")
select = Select(ele)
select.select_by_value("India")

# driver.find_element(By.CLASS_NAME, "product_sort_container").click()

#select.select_by_visible_text("Price (low to high")
#driver.implicitly_wait(10)

# driver.quit()