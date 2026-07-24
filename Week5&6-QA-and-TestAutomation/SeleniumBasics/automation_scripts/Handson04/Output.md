# Hands-On 04
## Selenium WebDriver Fundamentals

---

## Experiment Overview

### Aim

To gain practical experience with Selenium WebDriver by automating browser operations such as launching a browser, applying synchronization techniques, executing tests in headless mode, navigating between web pages, handling multiple browser tabs, capturing screenshots, and managing browser windows.

---

## Learning Objectives

After completing this hands-on, the following concepts were understood and implemented:

- Selenium architecture and its core components.
- Browser automation using Selenium WebDriver.
- Implicit Wait for element synchronization.
- Headless browser execution.
- Browser navigation and URL verification.
- Handling multiple browser tabs using Window Handles.
- Capturing screenshots programmatically.
- Browser window resizing for responsive UI testing.

---

# Task 01 – Selenium WebDriver Basics

---

## Step 24 – Understanding Selenium Components

### Objective

Study the primary components of Selenium and understand their purpose in test automation.

### Selenium Components

### 1. Selenium WebDriver

Selenium WebDriver is the core automation component that directly communicates with web browsers through browser-specific drivers (such as ChromeDriver). It allows automation scripts to perform actions like opening web pages, locating web elements, entering data, clicking buttons, and validating application behavior.

### 2. Selenium Grid

Selenium Grid enables the parallel execution of automation scripts across multiple browsers, operating systems, and machines. It significantly reduces execution time while supporting cross-browser compatibility testing.

### 3. Selenium IDE

Selenium IDE is a browser extension that allows recording and replaying browser interactions. It is primarily used for learning Selenium, creating quick prototypes, and generating automation scripts without extensive coding.

### Outcome

Successfully understood the purpose and functionality of Selenium WebDriver, Selenium Grid, and Selenium IDE.

---

## Step 25 – Launching Chrome Browser

### Objective

Launch the Google Chrome browser using Selenium WebDriver and open the LambdaTest Selenium Playground.

### Expected Result

The browser launches successfully, navigates to the Selenium Playground, and displays the webpage title in the terminal.

### Execution Evidence

#### Browser Output

![Browser](Screenshot/image.png)

#### Terminal Output

![Terminal](Screenshot/image-1.png)

### Observation

The browser launched successfully and Selenium established communication with ChromeDriver. The webpage title was retrieved and displayed without errors.

---

## Step 26 – Implementing Implicit Wait

### Objective

Configure Selenium to wait for web elements before throwing a `NoSuchElementException`.

### Expected Result

The browser applies an implicit wait of 10 seconds before searching for web elements.

### Execution Evidence

#### Terminal Output

![Terminal](Screenshot/image-2.png)

### Observation

The implicit wait was successfully configured. Selenium now waits for the specified duration whenever an element is searched, improving synchronization for dynamically loaded pages.

---

## Step 27 – Running Chrome in Headless Mode

### Objective

Execute browser automation without opening the graphical browser window.

### Expected Result

The automation script executes successfully while printing the webpage title in the terminal.

### Execution Evidence

#### Terminal Output

![Terminal](Screenshot/image-3.png)

### Observation

The browser executed successfully in Headless mode, making the automation faster and suitable for Continuous Integration (CI/CD) environments.

---

# Task 02 – Browser Navigation and Window Management

---

## Step 28 – Browser Navigation

### Objective

Navigate to the **Simple Form Demo** page, validate the redirected URL, and return to the Selenium Playground.

### Expected Result

The URL should contain **simple-form-demo**, and the browser should successfully return to the previous page.

### Execution Evidence

#### Terminal Output

![Terminal](Screenshot/image-4.png)

### Observation

Navigation was successfully performed. Selenium verified the redirected URL and returned to the previous webpage without any issues.

---

## Step 29 – Handling Multiple Browser Tabs

### Objective

Open a new browser tab, switch between tabs, and retrieve the title of the newly opened webpage.

### Expected Result

A second browser tab should open, Selenium should switch to it successfully, and display the page title.

### Execution Evidence

#### Terminal Output

![Terminal](Screenshot/image-5.png)

### Observation

Multiple browser tabs were handled successfully using Window Handles. Selenium switched to the newly opened Google tab and retrieved the correct page title.

---

## Step 30 – Capturing Browser Screenshot

### Objective

Capture a screenshot of the Selenium Playground and verify that the image file is created successfully.

### Expected Result

The screenshot should be stored in the project directory without any errors.

### Execution Evidence

#### Terminal Output

![Terminal](Screenshot/image-6.png)

#### Screenshot File Verification

![Folder](Screenshot/image-7.png)

### Observation

The screenshot was successfully captured and saved in the project directory. File verification confirmed successful image generation.

---

## Step 31 – Browser Window Management

### Objective

Retrieve the current browser window size and resize it to a predefined resolution.

### Expected Result

The browser window dimensions should update successfully.

### Execution Evidence

#### Terminal Output

![Terminal](Screenshot/image-8.png)

### Observation

The browser window size was successfully modified. Maintaining a consistent viewport ensures reliable execution of responsive UI tests across different environments.

---

# Key Learning Outcomes

Upon successful completion of this hands-on, the following skills were acquired:

- Understanding Selenium architecture and components.
- Browser automation using Selenium WebDriver.
- Browser synchronization using Implicit Wait.
- Headless browser execution.
- Browser navigation using Selenium APIs.
- Handling multiple browser windows and tabs.
- Programmatic screenshot capture.
- Browser window management for responsive testing.
- Basic Selenium project organization and automation workflow.

---

# Conclusion

This hands-on provided a strong foundation in Selenium WebDriver by introducing the essential concepts required for browser automation. Practical implementation of browser launching, synchronization, navigation, window handling, screenshot capture, and responsive browser management demonstrated how Selenium can be effectively used to automate web application testing. These concepts serve as the basis for implementing advanced Selenium automation frameworks in future hands-on exercises.