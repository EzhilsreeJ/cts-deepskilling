from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome to run in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.implicitly_wait(10)

print("Headless Mode Executed Successfully")
print("Page Title:", driver.title)

driver.quit()