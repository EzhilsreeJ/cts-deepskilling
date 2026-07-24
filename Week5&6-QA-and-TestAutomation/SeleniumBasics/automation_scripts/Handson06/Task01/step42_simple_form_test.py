from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Task01.step41_conftest import driver


def test_simple_form_submission(driver):

    driver.get("https://www.lambdatest.com/selenium-playground/")

    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    input_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-message"))
    )

    input_box.clear()
    input_box.send_keys("Hello Selenium")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "showInput"))
    )

    submit_button.click()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message.text == "Hello Selenium"