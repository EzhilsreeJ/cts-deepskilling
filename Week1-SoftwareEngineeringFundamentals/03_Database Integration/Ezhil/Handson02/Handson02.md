# Hands-On 2 – Writing SQL Queries (DML, Joins & Aggregations)

## Objective

Perform DML operations, execute SQL queries using filtering, joins, grouping, and aggregate functions to retrieve and manipulate data from the `college_db` database.

---

# Task 1 – Insert, Update and Delete Data

## Step 15 – Insert Sample Data into All Five Tables

```sql
INSERT INTO departments (dept_name, head_of_dept, budget) VALUES
('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
('Electronics', 'Dr. Priya Nair', 620000.00),
('Mechanical', 'Dr. Suresh Iyer', 540000.00),
('Civil', 'Dr. Ananya Sharma', 430000.00);

INSERT INTO students (first_name,last_name,email,date_of_birth,department_id,enrollment_year) VALUES
('Arjun','Mehta','arjun.mehta@college.edu','2003-04-12',1,2022),
('Priya','Suresh','priya.suresh@college.edu','2003-07-25',1,2022),
('Rohan','Verma','rohan.verma@college.edu','2002-11-08',2,2021),
('Sneha','Patel','sneha.patel@college.edu','2004-01-30',3,2023),
('Vikram','Das','vikram.das@college.edu','2003-09-14',1,2022),
('Kavya','Menon','kavya.menon@college.edu','2002-05-17',2,2021),
('Aditya','Singh','aditya.singh@college.edu','2004-03-22',4,2023),
('Deepika','Rao','deepika.rao@college.edu','2003-08-09',1,2022);

INSERT INTO courses (course_name,course_code,credits,department_id) VALUES
('Data Structures & Algorithms','CS101',4,1),
('Database Management Systems','CS102',3,1),
('Object Oriented Programming','CS103',4,1),
('Circuit Theory','EC101',3,2),
('Thermodynamics','ME101',3,3);

INSERT INTO enrollments (student_id,course_id,enrollment_date,grade) VALUES
(1,1,'2022-07-01','A'),
(1,2,'2022-07-01','B'),
(2,1,'2022-07-01','B'),
(2,3,'2022-07-01','A'),
(3,4,'2021-07-01','A'),
(4,5,'2023-07-01',NULL),
(5,1,'2022-07-01','C'),
(5,2,'2022-07-01','A'),
(6,4,'2021-07-01','B'),
(7,5,'2023-07-01',NULL),
(8,1,'2022-07-01','A'),
(8,3,'2022-07-01','B');

INSERT INTO professors (prof_name,email,department_id,salary) VALUES
('Dr. Anand Krishnan','anand.k@college.edu',1,95000),
('Dr. Meena Pillai','meena.p@college.edu',1,88000),
('Dr. Sunil Rajan','sunil.r@college.edu',2,82000),
('Dr. Latha Gopal','latha.g@college.edu',3,79000),
('Dr. Kartik Bose','kartik.b@college.edu',4,76000);
```

---

## Step 16 – Insert Two Additional Students

```sql
INSERT INTO students(first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Ezhil','Sree','ezhil.sree@college.edu','2005-11-14',1,2024),
('Rahul','Kumar','rahul.kumar@college.edu','2004-09-15',2,2024);
```

---

## Step 17 – Update Student Grade

```sql
UPDATE enrollments
SET grade='B'
WHERE student_id=5
AND course_id=1;
```

---

## Step 18 – Delete Enrollments with NULL Grades

```sql
SELECT *
FROM enrollments
WHERE grade IS NULL;

DELETE
FROM enrollments
WHERE grade IS NULL;
```

### Output

![alt text](Screenshot/image-18.png)

---

## Step 19 – Verify Row Counts

```sql
SELECT COUNT(*) AS Total_Students
FROM students;

SELECT COUNT(*) AS Total_Enrollments
FROM enrollments;
```

### Output

![Step 19 Output](Screenshot/image-1.png)

---

# Task 2 – Single-Table Queries and Filtering

## Step 20 – Students Enrolled in 2022

```sql
SELECT *
FROM students
WHERE enrollment_year=2022
ORDER BY last_name;
```

### Output

![Step 20 Output](Screenshot/image-2.png)

---

## Step 21 – Courses with Credits Greater than 3

```sql
SELECT *
FROM courses
WHERE credits>3
ORDER BY credits DESC;
```

### Output

![Step 21 Output](Screenshot/image-3.png)

---

## Step 22 – Professors with Salary Between 80000 and 95000

```sql
SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000;
```

### Output

![Step 22 Output](Screenshot/image-4.png)

---

## Step 23 – Students with @college.edu Email

```sql
SELECT *
FROM students
WHERE email LIKE '%@college.edu';
```

### Output

![Step 23 Output](Screenshot/image-5.png)

---

## Step 24 – Student Count by Enrollment Year

```sql
SELECT enrollment_year,
COUNT(*) AS total_students
FROM students
GROUP BY enrollment_year;
```

### Output

![Step 24 Output](Screenshot/image-6.png)

---

# Task 3 – Multi-Table Joins

## Step 25 – Student Name with Department

```sql
SELECT CONCAT(s.first_name,' ',s.last_name) AS student_name,
d.dept_name
FROM students s
JOIN departments d
ON s.department_id=d.department_id;
```

### Output

![Step 25 Output](Screenshot/image-7.png)

---

## Step 26 – Student Enrollment with Course Details

```sql
SELECT CONCAT(s.first_name,' ',s.last_name) AS student_name,
c.course_name
FROM enrollments e
JOIN students s
ON e.student_id=s.student_id
JOIN courses c
ON e.course_id=c.course_id;
```

### Output

![Step 26 Output](Screenshot/image-8.png)

---

## Step 27 – Students Not Enrolled in Any Course

```sql
SELECT CONCAT(s.first_name,' ',s.last_name) AS student_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id=e.student_id
WHERE e.student_id IS NULL;
```

### Output

![alt text](Screenshot/image-17.png)

---

## Step 28 – Course-wise Enrollment Count

```sql
SELECT c.course_name,
COUNT(e.student_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY c.course_id,c.course_name;
```

### Output

![Step 28 Output](Screenshot/image-10.png)

---

## Step 29 – Department with Professor Details

```sql
SELECT d.dept_name,
p.prof_name,
p.salary
FROM departments d
LEFT JOIN professors p
ON d.department_id=p.department_id;
```

### Output

![Step 29 Output](Screenshot/image-11.png)

---

# Task 4 – Aggregations and Grouping

## Step 30 – Total Enrollments per Course

```sql
SELECT c.course_name,
COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY c.course_id,c.course_name;
```

### Output

![Step 30 Output](Screenshot/image-12.png)

---

## Step 31 – Average Salary by Department

```sql
SELECT d.dept_name,
ROUND(AVG(p.salary),2) AS average_salary
FROM departments d
LEFT JOIN professors p
ON d.department_id=p.department_id
GROUP BY d.department_id,d.dept_name;
```

### Output

![Step 31 Output](Screenshot/image-13.png)

---

## Step 32 – Departments with Budget Above 600000

```sql
SELECT dept_name,
budget
FROM departments
WHERE budget>600000;
```

### Output

![Step 32 Output](Screenshot/image-14.png)

---

## Step 33 – Grade Distribution for CS101

```sql
SELECT grade,
COUNT(*) AS grade_count
FROM enrollments e
JOIN courses c
ON e.course_id=c.course_id
WHERE c.course_code='CS101'
GROUP BY grade;
```

### Output

![Step 33 Output](Screenshot/image-15.png)

---

## Step 34 – Departments with More Than Two Students

```sql
SELECT d.dept_name,
COUNT(DISTINCT s.student_id) AS total_students
FROM departments d
JOIN students s
ON d.department_id=s.department_id
GROUP BY d.department_id,d.dept_name
HAVING COUNT(DISTINCT s.student_id)>2;
```

### Output

![Step 34 Output](Screenshot/image-16.png)

---

# Learning Outcomes

After completing this hands-on, I was able to:

- Perform DML operations using `INSERT`, `UPDATE`, and `DELETE`.
- Retrieve data using `SELECT`, `WHERE`, `ORDER BY`, and `LIKE`.
- Work with `INNER JOIN` and `LEFT JOIN` to combine data from multiple tables.
- Use aggregate functions such as `COUNT()` and `AVG()`.
- Apply `GROUP BY` and `HAVING` clauses to summarize data.
- Write SQL queries to retrieve meaningful information from relational databases.

---

# Author

**Name:** Ezhil Sree J

**Program:** Cognizant Digital Nurture 5.0 – Python Full Stack Engineer (FSE)