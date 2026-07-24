import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

driver.find_element(By.ID,"title").send_keys("Ezhil Sree")
driver.find_element(By.ID,"description").send_keys("Learning Selenium Wait Strategies")

submit = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"btn-submit"))
)

submit.click()

# Allow AJAX request to finish
time.sleep(3)

print("✓ AJAX form submitted successfully")
print(driver.find_element(By.ID,"submit-control").text)

# input("Press Enter to close...")

driver.quit()