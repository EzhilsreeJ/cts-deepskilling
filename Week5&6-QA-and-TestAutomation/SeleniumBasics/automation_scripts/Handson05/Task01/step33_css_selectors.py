from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# CSS by ID
driver.find_element(By.CSS_SELECTOR, "#user-message")
print("✓ CSS ID Selector")

# CSS by Attribute
driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)
print("✓ CSS Attribute Selector")

# CSS Parent > Child
driver.find_element(
    By.CSS_SELECTOR,
    "div > input"
)
print("✓ CSS Parent-Child Selector")


driver.quit()