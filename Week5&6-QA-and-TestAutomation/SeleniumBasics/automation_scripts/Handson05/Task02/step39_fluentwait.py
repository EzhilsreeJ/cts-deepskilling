from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

name_field = wait.until(
    lambda d: d.find_element(By.ID, "title")
)

print("✓ FluentWait executed successfully")
print("Name field located using polling every 500 ms")

# input("Press Enter to close...")

driver.quit()