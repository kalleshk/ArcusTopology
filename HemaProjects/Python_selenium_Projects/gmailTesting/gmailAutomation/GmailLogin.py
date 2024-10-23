import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
your_email = "example@gmail.com"
your_password = "example123"
to_email = "hemasexample1@gmail.com"
subject = "Automation Testing example"
message = "Working Well 1 All the best"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://gmail.com/")
driver.maximize_window()
driver.implicitly_wait(80)

time.sleep(20)
username_input = driver.find_element(By.NAME, "identifier")
username_input.send_keys(your_email)
username_input.send_keys(Keys.ENTER)

time.sleep(70)
password_input =driver.find_element(By.NAME, "password")
username_input.send_keys(your_password)
username_input.send_keys(Keys.ENTER)

WebDriverWait(driver,90).until((EC.element_to_be_clickable(By.CSS_SELECTOR,"button.appmagic-button-container.no-focus-outline[tittle='click here to make a payment']"))).click()

driver.implicitly_wait(140)

for i in to_email:
    compose_button = driver.find_element(By.XPATH('//div[text()="Compose"]'))
    compose_button.click()

    time.sleep(70)
    to_input = driver.find_element(By.XPATH('//input[@role="combobox"]'))
    to_input.send_keys(i)
    subject_input = driver.find_element(By.NAME, "subjectbox")
    subject_input.send_keys(subject)
    body_input = driver.find_element(By.XPATH('//div[@role="textbox"]'))
    body_input.send_keys(message)

    send_button = driver.find_element(By.XPATH('//div[text()="send"]'))
    send_button.click()

    time.sleep(150)

driver.quit()
