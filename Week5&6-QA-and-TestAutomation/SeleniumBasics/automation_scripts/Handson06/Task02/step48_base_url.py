from selenium.webdriver.common.by import By


def test_simple_form_using_base_url(driver, base_url):

    driver.get(base_url + "simple-form-demo")

    textbox = driver.find_element(By.ID, "user-message")

    textbox.send_keys("Base URL Fixture")

    driver.find_element(By.ID, "showInput").click()

    assert textbox.get_attribute("value") == "Base URL Fixture"