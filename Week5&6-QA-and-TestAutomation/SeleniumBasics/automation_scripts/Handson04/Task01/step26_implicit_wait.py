from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.lambdatest.com/selenium-playground/")

"""
Implicit Wait

Implicit wait tells Selenium to wait for a specified amount of time
while searching for web elements before throwing a NoSuchElementException.

Although easy to use, implicit waits apply globally to all element lookups.
Explicit waits are generally preferred because they wait only for
specific elements under specific conditions.
"""

driver.implicitly_wait(10)

print("Implicit Wait applied successfully.")
print("Page Title:", driver.title)


driver.quit()