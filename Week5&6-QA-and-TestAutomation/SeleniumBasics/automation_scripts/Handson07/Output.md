# Handson07 – Selenium Page Object Model (POM)

## Objective

The objective of this hands-on is to implement the Page Object Model (POM) design pattern using Selenium WebDriver and PyTest. The framework separates page elements and page actions from test scripts, making the automation code reusable, maintainable, and scalable.

---

# Task 1 – Creating Page Object Classes

## Step 50: Create BasePage Class

Created a reusable **BasePage** class that contains common Selenium operations such as page navigation, retrieving the page title, and waiting for web elements using explicit waits. This class acts as the parent class for all page objects.

---

## Step 51: Create SimpleFormPage Class

Created the **SimpleFormPage** class by inheriting from the BasePage class. Added the URL and web element locators required for automating the Simple Form Demo page.

---

## Step 52: Add Interaction Methods

Implemented reusable methods inside the **SimpleFormPage** class to:

- Open the Simple Form Demo page
- Enter text into the input field
- Click the Get Checked Value button
- Retrieve the entered message for validation

---

## Step 53: Create CheckboxPage Class

Created the **CheckboxPage** class to automate the Checkbox Demo page. Implemented reusable methods to:

- Select a checkbox
- Unselect a checkbox
- Verify the checkbox selection status

---

## Step 54: Create InputFormPage Class

Created the **InputFormPage** class to automate the Input Form Submit page. Implemented reusable methods for entering user information, selecting a country, submitting the form, and retrieving the success message.

---

# Task 2 – Refactor Test Scripts Using Page Object Model

## Step 55: Refactor Simple Form Test

Refactored the Simple Form automation using the Page Object Model. The test navigates to the Simple Form Demo page, enters a message, clicks the **Get Checked Value** button, and verifies that the entered message is displayed successfully.

### Terminal Output

![Step 55 - Terminal](Screenshot/image.png)

---

## Step 56: Refactor Checkbox Test

Refactored the Checkbox Demo automation using the **CheckboxPage** class. The test selects the checkbox, verifies its selected state, unchecks it, and confirms that the checkbox is no longer selected.

### Terminal Output

![Step 56 - Terminal](Screenshot/image-1.png)

---

## Step 57: Refactor Input Form Test

Refactored the Input Form Submit automation using the **InputFormPage** class. The test fills all mandatory fields, selects the country, submits the form, and verifies the successful form submission.

### Terminal Output

![Step 57 - Terminal](Screenshot/image-2.png)

---

## Step 58: Execute Complete Test Suite

Executed all Selenium Page Object Model test cases together using PyTest. Verified that the complete automation suite executed successfully.

### Command Used

```powershell
py -m pytest tests\step55_test_simple_form_submission.py tests\step56_test_checkbox_demo.py tests\step57_test_input_form_submit.py -v
```

### Terminal Output

![Step 58 - Terminal](Screenshot/image-3.png)

---

## Step 59: Final Verification

Verified the successful implementation of the Selenium Page Object Model framework by executing all automation scripts and validating the expected results.

### Result

- Successfully implemented the Page Object Model (POM).
- Created reusable page classes.
- Refactored Selenium test scripts using page objects.
- Executed all automation scripts successfully using PyTest.
- Verified the functionality of:
  - Simple Form Demo
  - Checkbox Demo
  - Input Form Submit Demo

### Terminal Output

![Step 59 - Final Verification](Screenshot/image-3.png)

---

# Conclusion

Successfully completed **Handson07 – Selenium Page Object Model (POM)** by implementing reusable page classes and modular Selenium test scripts. The automation framework follows the Page Object Model design pattern, improving code reusability, maintainability, and readability. All test cases executed successfully using PyTest, confirming the correctness of the implemented framework.