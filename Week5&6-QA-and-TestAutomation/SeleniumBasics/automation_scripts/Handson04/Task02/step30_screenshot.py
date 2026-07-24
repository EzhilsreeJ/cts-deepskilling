import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Capture screenshot
driver.save_screenshot("playground_screenshot.png")

# Verify screenshot creation
if os.path.exists("playground_screenshot.png"):
    print("Screenshot saved successfully!")
else:
    print("Screenshot was not created.")

driver.quit()