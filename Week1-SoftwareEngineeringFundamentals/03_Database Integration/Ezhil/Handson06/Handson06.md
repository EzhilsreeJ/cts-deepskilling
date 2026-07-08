# Hands-On 6 – ORM with SQLAlchemy

## Objective

Implement Object Relational Mapping (ORM) using SQLAlchemy with MySQL by defining models, creating relationships, performing CRUD operations, and optimizing queries using eager loading.

---

# Task 1 – SQLAlchemy Models

## Step 75 – Create SQLAlchemy Models

Create the `models.py` file and import the required SQLAlchemy modules.

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import declarative_base, relationship
```

---

## Step 76 – Connect SQLAlchemy to MySQL

Configure the database connection.

```python
DATABASE_URL = "mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/college_db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Base = declarative_base()
```

---

## Step 77 – Define ORM Models

Define ORM classes for:

- Department
- Student
- Course
- Enrollment
- Professor

```python
class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)
```

Similarly create the remaining ORM classes using SQLAlchemy.

---

## Step 78 – Define Relationships

Define relationships between the tables.

```python
students = relationship(
    "Student",
    back_populates="department"
)

department = relationship(
    "Department",
    back_populates="students"
)

enrollments = relationship(
    "Enrollment",
    back_populates="student"
)
```

---

## Step 79 – Create Tables

Create all ORM tables.

```python
Base.metadata.create_all(engine)

print("All ORM tables created successfully.")
```

### Output

![Step 79 Output](Screenshot/image.png)

---

# Task 2 – CRUD Operations

## Step 80 – Create Session

Create a SQLAlchemy session using `sessionmaker`.

```python
Session = sessionmaker(bind=engine)
session = Session()
```

---

## Step 81 – Insert Departments and Students

Insert sample department and student records.

```python
session.add_all(departments)
session.commit()

session.add_all(students)
session.commit()
```

### Output

![Step 81 Output](Screenshot/image-1.png)

---

## Step 82 – Insert Courses and Enrollments

Insert sample course and enrollment records.

```python
session.add_all(courses)
session.commit()

session.add_all(enrollments)
session.commit()
```

---

## Step 83 – Retrieve Students from Computer Science Department

```python
students = (
    session.query(Student)
    .join(Department)
    .filter(
        Department.dept_name == "Computer Science"
    )
    .all()
)

for student in students:
    print(student.first_name, student.last_name)
```

### Output

![Step 83 Output](Screenshot/image-2.png)

---
# Task 2 – CRUD Operations (Continued)

## Step 84 – Retrieve Student Enrollment Details

Retrieve each student's name along with the course they are enrolled in.

```python
records = session.query(Enrollment).all()

for record in records:
    print(
        record.student.first_name,
        "->",
        record.course.course_name
    )
```

### Output

![Step 84 Output](Screenshot/image-3.png)

---

## Step 85 – Update a Student Record

Update a student's enrollment year.

```python
student = (
    session.query(Student)
    .filter(
        Student.email == "arjun@gmail.com"
    )
    .first()
)

if student:
    student.enrollment_year = 2024
    session.commit()
```

---

## Step 86 – Delete an Enrollment Record

Delete one enrollment record.

```python
record = session.query(Enrollment).first()

if record:
    session.delete(record)
    session.commit()
```

### Output

![Step 86 Output](Screenshot/image-4.png)

---

# Task 3 – N+1 Query Problem

## Step 87 – Identify the N+1 Query Problem

Retrieve enrollment records without eager loading.

```python
records = session.query(Enrollment).all()

for record in records:
    print(
        record.student.first_name,
        "->",
        record.course.course_name
    )
```

### Observation

Multiple SQL queries are generated because SQLAlchemy loads related student and course information separately for each enrollment.

### Output

![Step 87 Output](Screenshot/image-5.png)

---

## Step 88 – Fix the N+1 Problem Using `joinedload()`

```python
from sqlalchemy.orm import joinedload

records = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for record in records:
    print(
        record.student.first_name,
        "->",
        record.course.course_name
    )
```

### Observation

Using `joinedload()` retrieves enrollment, student, and course information in a single SQL query, eliminating the N+1 Query Problem.

### Output

![Step 88 Output](Screenshot/image-6.png)

---

## Step 89 – Compare SQL Queries

### Observation

Before using `joinedload()`:

- SQLAlchemy executed one query to retrieve enrollment records.
- Additional SQL queries were executed to retrieve related student and course details.
- This resulted in the **N+1 Query Problem**, increasing the total number of database queries.

After using `joinedload()`:

- SQLAlchemy executed a single SQL query using `JOIN`.
- Student and course information were loaded together.
- The number of SQL queries was significantly reduced, improving application performance.

---

## Step 90 – Compare Results

| Without `joinedload()` | With `joinedload()` |
|-------------------------|---------------------|
| Multiple SQL queries | Single SQL query using JOIN |
| N+1 Query Problem | N+1 Problem eliminated |
| Higher database round-trips | Reduced database round-trips |
| Lower performance | Better performance |

---

## Step 91 – Django ORM (Bonus)

**Note:** The Django ORM implementation using `select_related()` is an optional bonus task and was not implemented as part of this hands-on.

---

# Learning Outcomes

After completing this hands-on, I was able to:

- Connect SQLAlchemy with a MySQL database.
- Define ORM models and relationships.
- Perform CRUD operations using SQLAlchemy ORM.
- Query related records using ORM relationships.
- Identify the N+1 Query Problem.
- Optimize ORM queries using `joinedload()`.
- Compare lazy loading and eager loading techniques.

---

# Author

**Name:** Ezhil Sree J

**Program:** Cognizant Digital Nurture 5.0 – Python Full Stack Engineer (FSE)