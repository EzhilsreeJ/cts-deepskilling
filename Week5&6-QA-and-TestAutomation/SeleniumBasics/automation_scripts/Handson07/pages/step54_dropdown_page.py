from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.step50_base_page import BasePage


class DropdownPage(BasePage):

    DROPDOWN_URL = (
        "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"
    )

    DAY_DROPDOWN = (By.ID, "select-demo")
    SELECTED_DAY = (By.CLASS_NAME, "selected-value")

    def open(self):
        self.navigate_to(self.DROPDOWN_URL)

    def select_day(self, day):
        dropdown = Select(
            self.wait_for_element(self.DAY_DROPDOWN)
        )
        dropdown.select_by_visible_text(day)

    def get_selected_day(self):
        return self.driver.find_element(
            *self.SELECTED_DAY
        ).text

    def get_all_options(self):
        dropdown = Select(
            self.driver.find_element(
                *self.DAY_DROPDOWN
            )
        )
        return [
            option.text
            for option in dropdown.options
        ]