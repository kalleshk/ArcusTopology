from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Start a WebDriver session
driver = webdriver.Chrome(ChromeDriverManager().install())

# Execute JavaScript to open a new window
driver.execute_script("window.open('https://www.google.com','_blank');")

# Switch to the new window
driver.switch_to.window(driver.window_handles[1])

# Now you can interact with the new window

# Close the new window
import  time
time.sleep(3)
driver.close()

# Switch back to the original window
driver.switch_to.window(driver.window_handles[0])

# Close the browser window
driver.quit()