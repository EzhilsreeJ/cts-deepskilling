from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

# XPath using text()
label = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print("✓ Located using XPath text()")
print(label.text)

# XPath using contains()
labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print(f"✓ Located {len(labels)} labels using contains()")

for item in labels:
    print(item.text)


driver.quit()