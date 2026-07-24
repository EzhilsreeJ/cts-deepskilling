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

# Open Google in a new tab
driver.execute_script('window.open("https://www.google.com");')

# Display window handles
print("Window Handles:", driver.window_handles)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

print("Google Tab Title:", driver.title)


driver.quit()