from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Display current window size
print("Current Window Size:", driver.get_window_size())

# Resize browser window
driver.set_window_size(1280, 800)

# Display updated window size
print("Updated Window Size:", driver.get_window_size())

print("\nA consistent browser window size ensures reliable responsive UI testing.")


driver.quit()