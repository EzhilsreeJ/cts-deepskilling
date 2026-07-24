from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Task01.step41_conftest import driver


def test_checkbox_demo(driver):

    driver.get("https://www.lambdatest.com/selenium-playground/")
    driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']"))
    )

    checkbox.click()
    assert checkbox.is_selected()

    # Locate the checkbox again before the second click
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']"))
    )

    checkbox.click()

    # Locate it again before checking its state
    checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

    assert not checkbox.is_selected()