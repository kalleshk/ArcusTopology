from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver

#start a WebDriver session
driver = webdriver.Chrome(ChromeDriverManager().install())
#open a web page with an alert
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
# try:
#     #trigger the alert by executing javascript
#     #driver.execute_script("alert('this is a sample alert');")
#     driver.execute_script("confirm('Do you want to proceed?');")
#
#     #switch to alert
#     alert=Alert(driver)
#     #get the text of the alert
#
#     alert_text=alert.text
#     print("Alert Text:", alert_text)
#
#     #Accept the alert(click Ok)
#     #alert.accept()
#     alert.dismiss()
# except:
#     print("No alert found.")
#  #close the browser window
# driver.quit()

# Open a webpage with a prompt alert
driver.get("https://www.example.com")

try:
    # Trigger the prompt alert by executing JavaScript
    driver.execute_script("prompt('Please enter your name:');")

    # Switch to the alert
    alert = Alert(driver)

    # Get the text of the alert
    alert_text = alert.text
    print("Alert text:", alert_text)

    # Send input to the prompt
    ale = alert.send_keys("John Doe")

    # Accept the alert (click OK)
    alert.accept()

    # Retrieve the input entered in the prompt
    prompt_input = driver.switch_to.alert.text
    print("Prompt input:", prompt_input)

except:
    print("No alert found.")

# Close the browser window
driver.quit()
