from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# By ID
driver.find_element(By.ID, "user-message")
print("✓ Located using ID")

# By Class Name
driver.find_element(By.CLASS_NAME, "border")
print("✓ Located using CLASS_NAME")

# By Tag Name
driver.find_element(By.TAG_NAME, "input")
print("✓ Located using TAG_NAME")

# Absolute XPath (use the one you copied from DevTools)
driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/main/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input"
)
print("✓ Located using Absolute XPath")

# Relative XPath
driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)
print("✓ Located using Relative XPath")

# input("Press Enter to close...")

driver.quit()