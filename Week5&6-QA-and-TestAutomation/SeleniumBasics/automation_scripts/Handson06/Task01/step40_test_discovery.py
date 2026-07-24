from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_simple_form_submission():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")

    print("Page Title:", driver.title)

    driver.quit()


def test_checkbox_interaction():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")

    print("Page Title:", driver.title)

    driver.quit()