# Handson 09 - Output

## Task 1 - Accessibility Audit & Semantic Fixes

### Output

**Objectives Completed**
- Performed an accessibility audit using Chrome Lighthouse.
- Recorded the initial accessibility score and identified accessibility issues.
- Added descriptive labels for form input fields.
- Corrected the heading hierarchy using semantic HTML elements.
- Improved the page structure for better accessibility and screen reader support.
- Fixed all identified accessibility issues and achieved a Lighthouse Accessibility score of **100**.

### Screenshots

**Initial Lighthouse Accessibility Report (Score: 90)**

![Task 1 - Before Fix](Screenshot/image.png)

**Final Lighthouse Accessibility Report (Score: 100)**

![Task 1 - After Fix](Screenshot/image-1.png)

---

## Task 2 - ARIA & Keyboard Navigation

### Output

**Objectives Completed**
- Added `aria-label="Main navigation"` to the navigation bar.
- Applied `aria-current="page"` to the active navigation link.
- Made all course cards keyboard accessible using `tabindex="0"`.
- Enabled keyboard activation of course cards using the **Enter** key.
- Added `role="status"` and `aria-live="polite"` to announce search results dynamically.
- Verified keyboard navigation using the **Tab** key.
- Confirmed that search results are announced as the user types.
- Step 131 (`aria-expanded`) was not applicable because the application does not contain any expandable components such as a hamburger menu.

### Screenshots

**ARIA Live Search Result Announcement**

![Task 2 - Keyboard Navigation](Screenshot/image-2.png)


**Keyboard Navigation (Tab Focus on Course Card)**

![Task 2 - Search Result](Screenshot/image-3.png)

---

## Task 3 - Colour Contrast & Cross-Browser Compatibility

### Output

**Objectives Completed**
- Improved colour contrast to satisfy WCAG 2.1 accessibility requirements.
- Verified the Student Portal in different browsers.
- Confirmed consistent layout and functionality across browsers.
- Validated the final accessibility compliance using Chrome Lighthouse.
- Achieved a Lighthouse Accessibility score of **100** after implementing all accessibility improvements.

### Screenshots

**Application in Different Browser**

![Task 3 - Cross Browser Compatibility](Screenshot/image-4.png)

**Final Lighthouse Accessibility Verification (Score: 100)**

![Task 3 - Final Verification](Screenshot/image-5.png)

---

## Learning Outcome

- Learned to perform accessibility audits using Chrome Lighthouse.
- Applied semantic HTML to improve accessibility and document structure.
- Implemented ARIA attributes to enhance screen reader support.
- Enabled complete keyboard navigation using the **Tab** and **Enter** keys.
- Improved colour contrast to meet WCAG 2.1 accessibility guidelines.
- Verified cross-browser compatibility across different browsers.
- Successfully achieved a **100/100 Lighthouse Accessibility Score**.