---

# Step 35 – Ranking of Locator Strategies

## Objective

Evaluate the locator strategies used in Steps 32–34 and rank them from **most preferred** to **least preferred** based on:

- Uniqueness
- Readability
- Maintainability
- Resistance to HTML structure changes

## Ranking

| Rank | Locator Strategy | Justification |
|------|------------------|---------------|
| **1** | **By.ID** | The most preferred locator because IDs are generally unique, easy to read, fast to locate, and highly maintainable. |
| **2** | **By.CSS_SELECTOR** | Fast and flexible. CSS selectors provide concise syntax and are suitable for locating most web elements. |
| **3** | **By.NAME** | A good choice when the `name` attribute is unique. Easy to understand and maintain. |
| **4** | **Relative XPath** | Useful when ID or CSS selectors cannot uniquely identify an element. More flexible but depends on page attributes. |
| **5** | **By.CLASS_NAME** | Suitable only when the class name is unique. Since multiple elements often share the same class, it is less reliable. |
| **6** | **Absolute XPath** | Least preferred because it depends on the complete HTML structure. Any structural change in the page can break the locator. |

## Observation

- **By.ID** is the best choice whenever a unique ID is available.
- **CSS Selectors** are generally faster than XPath and are recommended for most automation scenarios.
- **Relative XPath** should be used when CSS selectors cannot express the required condition (for example, locating elements based on text).
- **Absolute XPath** should be avoided in real-world automation because it is highly brittle and difficult to maintain.

## Conclusion

The choice of locator strategy has a significant impact on the stability and maintainability of Selenium automation scripts. Using unique locators such as **ID** and **CSS Selectors** produces more reliable and readable test scripts, whereas brittle locators like **Absolute XPath** should be avoided whenever possible.