# Handson 10 - Output

## Task 1 - Build a Centralised API Service Layer

### Output

**Objectives Completed**
- Created a centralized API layer using Axios.
- Configured a reusable Axios instance with a common `baseURL`.
- Added default request headers and timeout configuration.
- Implemented request interceptors to attach an Authorization header.
- Implemented response interceptors for standardized response and error handling.
- Created reusable API functions (`getAllCourses()`, `getCourseById()`, and `enrollStudent()`).
- Updated application components to consume the centralized API layer instead of making direct API calls.

### Screenshots

**Centralized API Layer Output**

![Task 1 - API Integration](Screenshot/image.png)

**Application Using Reusable API Service**

![Task 1 - API Service](Screenshot/image-1.png)

---

## Task 2 - Advanced Redux Toolkit (React)

### Output

**Objectives Completed**
- Configured Redux Toolkit using `configureStore()`.
- Created a Redux slice using `createSlice()`.
- Implemented asynchronous API calls using `createAsyncThunk()`.
- Managed loading, success, and error states through Redux.
- Dispatched asynchronous actions from React components.
- Accessed Redux state using `useSelector()`.
- Triggered actions using `useDispatch()`.
- Verified Redux state updates using Redux DevTools.

### Screenshots

**Redux Toolkit Application**

![Task 2 - Redux Application](Screenshot/image-2.png)

**Redux DevTools State**

![Task 2 - Redux DevTools](Screenshot/image-3.png)

---

## Task 3 - NgRx State Management (Angular)

### Output

**Objectives Completed**
- Implemented NgRx Actions for loading course data.
- Created Reducers to manage application state.
- Implemented Effects to perform asynchronous API calls.
- Created Selectors for retrieving state from the store.
- Configured the NgRx Store.
- Retrieved API data through Effects and updated the Store.
- Displayed data using Angular components.

### Screenshots

**NgRx Application Output**

![Task 3 - NgRx Application](Screenshot/image-4.png)

**NgRx Store / State Management**

![Task 3 - NgRx State](Screenshot/image-5.png)

---

## Task 4 - Pinia Advanced Patterns (Vue)

### Output

**Objectives Completed**
- Implemented asynchronous Pinia actions.
- Managed loading and error states within the Pinia store.
- Used `storeToRefs()` to preserve Vue reactivity.
- Implemented a Reset action to clear the store state.
- Integrated the centralized Axios API layer with Pinia.
- Implemented global error handling using Axios interceptors.
- Compared state management approaches across React, Angular, and Vue.

### Screenshots

**Pinia Advanced Patterns Application**

![Task 4 - Pinia Application](Screenshot/image-6.png)

**Pinia Store State**

![Task 4 - Pinia Store](Screenshot/image-7.png)

---

## Learning Outcome

- Learned to build a centralized API service layer using Axios.
- Implemented reusable API functions and request/response interceptors.
- Applied Redux Toolkit concepts including Store, Slice, Async Thunks, and DevTools.
- Implemented NgRx architecture using Actions, Reducers, Effects, Selectors, and Store.
- Applied advanced Pinia patterns including asynchronous actions, `storeToRefs()`, loading/error state management, and store reset.
- Compared state management approaches across React (Redux Toolkit), Angular (NgRx), and Vue (Pinia).
- Understood best practices for scalable API integration and state management in modern frontend applications.