"""
Comparison of ORM Loading Strategies

Before joinedload():
- One query retrieves enrollments.
- Additional queries retrieve students and courses.
- This causes the N+1 query problem.

After joinedload():
- A single JOIN query retrieves enrollment,
  student and course details together.
- Total SQL queries reduced significantly.
"""
from datetime import date
from sqlalchemy.orm import joinedload
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (
    Department,
    Student,
    Course,
    Enrollment,
)

DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost/college_db"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Step 81 - Insert Departments
 

if session.query(Department).count() == 0:

    departments = [
        Department(dept_name="Computer Science"),
        Department(dept_name="Mechanical"),
        Department(dept_name="Electrical")
    ]

    session.add_all(departments)
    session.commit()

print("Departments inserted")

 
# Step 81 - Insert Students
 

if session.query(Student).count() == 0:

    students = [

        Student(
            first_name="Arjun",
            last_name="Mehta",
            email="arjun@gmail.com",
            enrollment_year=2022,
            department_id=1
        ),

        Student(
            first_name="Priya",
            last_name="Sharma",
            email="priya@gmail.com",
            enrollment_year=2023,
            department_id=1
        ),

        Student(
            first_name="Rahul",
            last_name="Kumar",
            email="rahul@gmail.com",
            enrollment_year=2022,
            department_id=2
        ),

        Student(
            first_name="Ananya",
            last_name="Rao",
            email="ananya@gmail.com",
            enrollment_year=2021,
            department_id=3
        ),

        Student(
            first_name="Kiran",
            last_name="Das",
            email="kiran@gmail.com",
            enrollment_year=2023,
            department_id=2
        )

    ]

    session.add_all(students)
    session.commit()

    print("Students inserted")
else:
    print("Students already exist")

 
# Step 82 - Insert Courses
 

if session.query(Course).count() == 0:

    courses = [

        Course(
            course_code="CS101",
            course_name="Database Systems",
            credits=4
        ),

        Course(
            course_code="CS102",
            course_name="Python Programming",
            credits=3
        ),

        Course(
            course_code="CS103",
            course_name="Operating Systems",
            credits=4
        )

    ]

    session.add_all(courses)
    session.commit()

print("Courses inserted")

 
# Step 82 - Insert Enrollments
 

if session.query(Enrollment).count() == 0:

    enrollments = [

        Enrollment(
            student_id=1,
            course_id=1,
            enrollment_date=date.today(),
            grade="A"
        ),

        Enrollment(
            student_id=2,
            course_id=2,
            enrollment_date=date.today(),
            grade="B"
        ),

        Enrollment(
            student_id=3,
            course_id=1,
            enrollment_date=date.today(),
            grade="A"
        ),

        Enrollment(
            student_id=4,
            course_id=3,
            enrollment_date=date.today(),
            grade="C"
        )

    ]

    session.add_all(enrollments)
    session.commit()

print("Enrollments inserted")

 
# Step 83
 

print("\nStudents in Computer Science\n")

students = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

for student in students:
    print(student.first_name, student.last_name)

 
# Step 84
 

print("\nEnrollment Details\n")

records = (
    session.query(Enrollment)
    .all()
)

for row in records:
    print(
        row.student.first_name,
        "->",
        row.course.course_name
    )

 
# Step 85
 

student = (
    session.query(Student)
    .filter(Student.email == "arjun@gmail.com")
    .first()
)

if student:
    student.enrollment_year = 2024
    session.commit()

print("Student updated")

 
# Step 86
 

record = session.query(Enrollment).first()

if record:
    session.delete(record)
    session.commit()

print("One enrollment deleted")

from sqlalchemy.orm import joinedload

print("\n" + "=" * 50)
print("STEP 87 - N+1 QUERY")
print("=" * 50)

records = session.query(Enrollment).all()

for record in records:
    print(
        record.student.first_name,
        "->",
        record.course.course_name
    )

print("\n")
print("=" * 50)
print("STEP 88 - FIX USING joinedload()")
print("=" * 50)

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

print("\n")
print("N+1 problem fixed using joinedload().")

session.close()
