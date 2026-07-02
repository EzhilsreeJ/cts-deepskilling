# Hands-On 8 – RESTful API Design Best Practices

## Objective

This hands-on focuses on improving an existing FastAPI-based Course Management API by applying RESTful API design best practices, including resource naming conventions, proper HTTP methods and status codes, API versioning, pagination, filtering, and standardized error responses.

---

## Features Implemented

### Task 1 – Audit and Fix Resource Naming and HTTP Methods

- Implemented RESTful resource naming using plural nouns.
- Added PATCH endpoint for partial updates.
- Used correct HTTP status codes (200, 201, 204, 404).
- Added Location header in POST responses.
- Verified API endpoints using Swagger UI and Postman.

### Task 2 – Versioning, Pagination and Standardised Error Responses

- Implemented URL versioning (`/api/v1/`).
- Added pagination using `page` and `page_size` query parameters.
- Implemented search filtering using the `search` query parameter.
- Standardized error responses in JSON format.
- Verified all endpoints using Swagger UI and Postman.

---

## Technologies Used

- Python
- FastAPI
- SQLAlchemy (Async ORM)
- SQLite
- Uvicorn
- Pydantic
- Swagger UI (OpenAPI)
- Postman

---

## Project Structure

```
Handson8/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
├── courses.db
├── requirements.txt
├── README.md
│
└── Output Screenshot/
    ├── Task 1/
    └── Task 2/
```

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the server

```bash
uvicorn main:app --reload
```

### Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Outcome

Successfully implemented RESTful API best practices including API versioning, pagination, search filtering, PATCH support, proper HTTP status codes, Location headers, and standardized error responses using FastAPI.
