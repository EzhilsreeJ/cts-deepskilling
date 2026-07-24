import pytest

from selenium.webdriver.common.by import By


@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url + "simple-form-demo")

    textbox = driver.find_element(By.ID, "user-message")

    textbox.clear()

    textbox.send_keys(message)

    driver.find_element(By.ID, "showInput").click()

    assert textbox.get_attribute("value") == message
    # assert textbox.get_attribute("value") == "Wrong Value"