from pages.step51_simple_form_page import SimpleFormPage


def test_simple_form_submission(driver):

    page = SimpleFormPage(driver)

    page.open()

    message = "Hello Selenium"

    page.enter_message(message)

    page.click_show_message()

    assert page.get_displayed_message() == message