from selenium.webdriver.common.by import By

from pages.step50_base_page import BasePage


class SimpleFormPage(BasePage):

    SIMPLE_FORM_URL = (
        "https://www.lambdatest.com/selenium-playground/simple-form-demo"
    )

    MESSAGE_INPUT = (By.ID, "user-message")

    SHOW_MESSAGE_BUTTON = (
        By.XPATH,
        "//button[text()='Get Checked Value']"
    )

    def open(self):
        self.navigate_to(self.SIMPLE_FORM_URL)

    def enter_message(self, message):
        textbox = self.wait_for_element(
            self.MESSAGE_INPUT
        )
        textbox.clear()
        textbox.send_keys(message)

    def click_show_message(self):
        self.wait_for_element(
            self.SHOW_MESSAGE_BUTTON
        ).click()

    def get_displayed_message(self):
        return self.wait_for_element(
            self.MESSAGE_INPUT
        ).get_attribute("value")