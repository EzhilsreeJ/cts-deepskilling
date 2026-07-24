import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_name = report.nodeid.replace("::", "_") + ".png"

            driver.save_screenshot(screenshot_name)

            print(f"Screenshot saved as {screenshot_name}")