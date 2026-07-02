# Hands-On 5

## Python Backend Frameworks

### Topic

Flask SQLAlchemy Models, Migrations and Database CRUD

---

## Objective

Implement SQLAlchemy models, configure Flask-Migrate, perform database migrations, and build CRUD APIs using a SQLite database.

---

## Software Used

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- Visual Studio Code
- Postman

---

# Task 1 - SQLAlchemy Models and Migrations

## Features Implemented

- Configured Flask-SQLAlchemy
- Created Department model
- Created Course model
- Created Student model
- Created Enrollment model
- Defined relationships
- Initialized Flask-Migrate
- Generated migrations
- Created database tables
- Inserted sample records using Flask Shell

---

# Task 2 - Database CRUD Operations

## Features Implemented

- GET all courses from database
- GET course by ID
- POST new course
- UPDATE existing course
- DELETE course
- Implemented `to_dict()` serialization
- Used `get_or_404()`
- Created JOIN endpoint to fetch enrolled students

---

## API Endpoints

| Method | Endpoint |
|---------|----------|
| GET | /api/courses/ |
| POST | /api/courses/ |
| GET | /api/courses/<id> |
| PUT | /api/courses/<id> |
| DELETE | /api/courses/<id> |
| GET | /api/courses/<id>/students/ |

---

## Result

Successfully implemented SQLAlchemy models, database migrations, CRUD operations, and relationship-based queries using Flask and SQLite.