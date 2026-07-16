# Handson 07 - Output

## Task 1 - Angular Components & Data Binding

### Output

**Objectives Completed**
- Created Angular components using Angular CLI.
- Implemented reusable `CourseList` and `CourseCard` components.
- Passed data between components using `@Input()`.
- Rendered course information dynamically using interpolation.
- Displayed multiple course cards using `*ngFor`.
- Implemented search functionality using two-way data binding (`[(ngModel)]`).
- Displayed a **"No courses found"** message when no matching courses were available.

### Screenshots

**Course List with Data Binding**

![Task 1 - Course List](Screenshot/image-1.png)

**Search Functionality (No Courses Found)**

![Task 1 - Search Result](Screenshot/image.png)

---

## Task 2 - Services, Dependency Injection & HttpClient

### Output

**Objectives Completed**
- Created an Angular service using Angular CLI.
- Implemented Dependency Injection to consume the service within the component.
- Configured `HttpClientModule` for HTTP communication.
- Retrieved course data from a REST API using `HttpClient`.
- Rendered API response dynamically in the Course List component.
- Implemented a loading indicator while fetching data from the API.

### Screenshots

**Courses Loaded from REST API**

![Task 2 - API Output](Screenshot/image-2.png)

**Application After Service Integration**

![Task 2 - Final Output](Screenshot/image-3.png)

---

## Task 3 - Angular Routing & Reactive Forms

### Output

**Objectives Completed**
- Configured Angular Router for navigation between application views.
- Implemented navigation links for the Course List and Student Profile pages.
- Created a Reactive Form using `FormGroup` and `FormControl`.
- Applied validation using Angular Validators.
- Displayed validation messages for invalid input.
- Disabled the Submit button until the form became valid.
- Verified successful form validation using valid user input.

### Screenshots

**Routing Between Courses and Profile Pages**

![Task 3 - Routing](Screenshot/image-4.png)

**Reactive Form Validation**

![Task 3 - Validation](Screenshot/image-5.png)

**Valid Form with Submit Enabled**

![Task 3 - Final Output](Screenshot/image-6.png)

---

## Learning Outcome

- Learned to build reusable Angular components using Angular CLI.
- Implemented parent-child communication using `@Input()`.
- Applied Angular data binding techniques, including interpolation, property binding, and two-way binding.
- Used structural directives such as `*ngFor` and `*ngIf` for dynamic rendering.
- Created reusable services and consumed REST APIs using `HttpClient`.
- Implemented Dependency Injection for sharing application logic.
- Configured Angular Router for navigation between application views.
- Built Reactive Forms using `FormGroup`, `FormControl`, and Validators.
- Implemented form validation and controlled form submission using Angular Reactive Forms.