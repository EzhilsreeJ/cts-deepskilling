from pages.step57_input_form_page import InputFormPage


def test_input_form_submit(driver):

    page = InputFormPage(driver)

    page.open()

    page.enter_name("Ezhil")

    page.enter_email("ezhil@gmail.com")

    page.enter_password("Test123")

    page.enter_company("CTS")

    page.enter_website("www.cts.com")

    page.select_country("India")

    page.enter_city("Chennai")

    page.enter_address1("Anna Nagar")

    page.enter_address2("Near Metro")

    page.enter_state("Tamil Nadu")

    page.enter_zip("600001")

    page.click_submit()

    assert (
        page.get_success_message()
        == "Thanks for contacting us, we will get back to you shortly."
    )