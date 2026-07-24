from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Autoclosable Success Message']"
).click()

success_alert = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class,'alert-success')]")
    )
)

print("✓ Success alert displayed")
print(success_alert.text)

input("Press Enter to close...")

driver.quit()