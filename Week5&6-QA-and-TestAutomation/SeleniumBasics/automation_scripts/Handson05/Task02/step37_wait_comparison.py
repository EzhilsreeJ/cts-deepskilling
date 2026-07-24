import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

print("----- Using time.sleep() -----")

start = time.time()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Autoclosable Success Message']"
).click()

time.sleep(3)

print(driver.find_element(
    By.XPATH,
    "//div[contains(@class,'alert-success')]"
).text)

end = time.time()

print(f"Execution Time (time.sleep): {end-start:.2f} seconds")

print("\n----- Using WebDriverWait -----")

start = time.time()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Autoclosable Success Message']"
).click()

alert = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located(
        (By.XPATH,"//div[contains(@class,'alert-success')]")
    )
)

print(alert.text)

end = time.time()

print(f"Execution Time (WebDriverWait): {end-start:.2f} seconds")

input("Press Enter to close...")

driver.quit()