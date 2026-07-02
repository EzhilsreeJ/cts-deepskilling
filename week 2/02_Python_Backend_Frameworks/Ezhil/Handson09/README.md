# Hands-On 9 – FastAPI Authentication and API Security

## Objective

Implement secure authentication and authorization in the Course Management API using JWT, password hashing, protected routes, and CORS configuration.

---

## Technologies Used

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Passlib (bcrypt)
- Python-JOSE (JWT)
- Uvicorn

---

## Features Implemented

### Task 1

- User model creation
- Password hashing using bcrypt
- User registration API
- Password verification
- Secure password storage

### Task 2

- JWT Authentication
- Login API
- Protected API endpoints
- OAuth2 Password Bearer
- CORS configuration
- OAuth2 Authorization Code Flow explanation

---

## Project Structure

```
Handson9/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
├── security.py
├── courses.db
├── requirements.txt
├── README.md
│
└── Output Screenshot/
    ├── Task 1/
    └── Task 2/
```

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## APIs Implemented

### Authentication

- POST `/api/v1/auth/register`
- POST `/api/v1/auth/login`

### Courses

- POST `/api/v1/courses/`
- GET `/api/v1/courses/`
- GET `/api/v1/courses/{id}`
- PUT `/api/v1/courses/{id}`
- PATCH `/api/v1/courses/{id}`
- DELETE `/api/v1/courses/{id}`

### Students

- POST `/api/students/`
- GET `/api/students/{id}`
- PUT `/api/students/{id}`
- DELETE `/api/students/{id}`

### Enrollments

- POST `/api/enrollments/`
- GET `/api/enrollments/{id}`
- PUT `/api/enrollments/{id}`
- DELETE `/api/enrollments/{id}`

---

## Authentication Flow

1. Register a new user.
2. Login using email and password.
3. Receive a JWT access token.
4. Click **Authorize** in Swagger.
5. Enter:

```
Bearer <access_token>
```

6. Access protected endpoints.

---

## Screenshots

### Task 1

- user_model.png
- password_hashing.png
- register_success.png
- hashed_password_db.png

### Task 2

- login_jwt.png
- protected_route_401.png
- protected_route_success.png
- cors_configuration.png
- oauth2_comment.png

---

## Outcome

- Implemented secure user authentication.
- Passwords are securely hashed using bcrypt.
- JWT-based authentication protects sensitive APIs.
- CORS is configured for cross-origin requests.
- OAuth2 concepts are documented.
- Successfully completed Hands-On 9.