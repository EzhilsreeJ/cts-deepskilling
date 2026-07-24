from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Click the "Simple Form Demo" link
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify the URL
assert "simple-form-demo" in driver.current_url

print("Current URL:", driver.current_url)
print("URL verification successful!")

# Navigate back
driver.back()

print("Returned to:", driver.title)

driver.quit()