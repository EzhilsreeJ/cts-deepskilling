# Handson06 – Selenium Basics

## Step 40: Test Discovery

Executed the pytest command to verify that all test files were automatically discovered by pytest.

**Output:**

![Step 40 - Terminal](Screenshot/image.png)

---

## Step 41: Creating Fixtures Using conftest.py

Created reusable Selenium WebDriver fixtures in `step41_conftest.py` to initialize and close the browser automatically for every test execution.

**Output:**

![Step 41 - Terminal](Screenshot/image-1.png)

---

## Step 42: Simple Form Automation

Automated the LambdaTest Simple Form Demo page by entering text into the input field and verifying the entered value.


### Terminal Output

![Step 42 - Browser](Screenshot/image-2.png)

### Browser Output

![Step 42 - Terminal](Screenshot/image-3.png)

---

## Step 43: Checkbox Automation

Automated the checkbox interaction using Selenium and verified the checkbox selection.

### Terminal Output

![Step 43 - Terminal](Screenshot/image-4.png)

### Browser Output

![Step 43 - Browser](Screenshot/image-5.png)

---

## Step 44: Running Tests with Verbose Output

Executed pytest using verbose mode to display detailed test execution information.

**Command Used**

```bash
pytest -v
```

**Output:**

![Step 44 - Terminal](Screenshot/image-6.png)

---

## Step 45: Parameterized Testing

Implemented parameterized testing using `@pytest.mark.parametrize()` to execute the same test with multiple input values.

### Terminal Output

![Step 45 - Terminal](Screenshot/image-7.png)

### Screenshots Automatically Captured During Test Execution

The automation script generated screenshots for each parameterized test execution.

![Generated Screenshots](Screenshot/image-8.png)

Generated files:

- `step45_parameterized_test.py_test_simple_form_submission[12345].png`
- `step45_parameterized_test.py_test_simple_form_submission[Hello].png`
- `step45_parameterized_test.py_test_simple_form_submission[Selenium Automation].png`

---

## Step 46: Screenshot Capture on Test Failure

Configured a pytest hook to automatically capture a screenshot whenever a test fails.

### Generated Failure Screenshot

![Generated Screenshot](Screenshot/image-9.png)



---

## Step 47: HTML Report Generation

Generated an HTML report for the executed test cases using the `pytest-html` plugin.

**Command Used**

```bash
pytest step45_parameterized_test.py --html=report.html
```

**Output:**

![Step 47 - Terminal](Screenshot/image-10.png)

---

## Step 48: Base URL Fixture

Used a reusable `base_url` fixture from `conftest.py` to simplify navigation across Selenium tests.

**Output:**

![Step 48 - Terminal](Screenshot/image-11.png)

---

## Step 49: Dropdown Automation

Automated dropdown selection using Selenium's `Select` class and verified the selected option.

**Output:**

![Step 49 - Terminal](Screenshot/image-12.png)

---

## Conclusion

Successfully completed all Selenium Basics Handson06 tasks, including:

- Test discovery using pytest
- Reusable Selenium fixtures
- Simple Form automation
- Checkbox automation
- Verbose pytest execution
- Parameterized testing
- Automatic screenshot capture
- HTML report generation
- Base URL fixture implementation
- Dropdown automation