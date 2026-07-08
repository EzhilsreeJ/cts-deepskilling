import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="college_db"
)

cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

query_count = 1

for enrollment in enrollments:
    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id=%s",
        (enrollment["student_id"],)
    )
    cursor.fetchone()
    query_count += 1

print("Queries Executed:", query_count)

cursor.close()
conn.close()