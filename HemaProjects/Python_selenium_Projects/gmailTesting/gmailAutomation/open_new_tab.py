from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Start a WebDriver session
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open a webpage
driver.get("https://www.google.co.in/")

# Simulate opening a new tab by sending Ctrl (or Command for Mac) + T
# For Windows and Linux:
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# For Mac:
#driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't')
# actions = ActionChains(driver)
# actions.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()


# Alternatively, you can use ActionsChains to perform the same action
# actions = ActionChains(driver)
# actions.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

# After opening a new tab, you can switch to it using:
driver.switch_to.window(driver.window_handles[1])

# Close the browser window
driver.quit()
