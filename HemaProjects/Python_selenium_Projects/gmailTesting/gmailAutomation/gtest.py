import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open Gmail
driver.get("https://accounts.google.com/v3/signin/identifier?hl=en-gb&ifkv=ASKXGp1YeXk5lfjRJntJn--5Rdga3BmaXGraRFf_JmRk-uRtpfjO5mCTN0nssDhBtwsoXNZoFyjM&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-351568160%3A1706216172078743&theme=glif")

# Find the email input field and enter your email
email_input = driver.find_element("name", "identifier")
email_input.send_keys("heexample@gmail.com")

# Click on the "Next" button
next_button = driver.find_element(By.ID,'identifierNext')
next_button.click()

# Wait for a few seconds to load the password input field
time.sleep(2)

# Find the password input field and enter your password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("example90")

# Click on the "Next" button
password_next_button = driver.find_element(By.ID, 'passwordNext')
password_next_button.click()

# Wait for a few seconds to log in
time.sleep(5)

# Close the browser window
driver.quit()
