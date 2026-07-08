from flask import Flask, jsonify, request
from database import db
from models import Student,Enrollment
app = Flask(__name__)
import requests
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Student Service is Running"


# GET ALL STUDENTS
@app.route("/api/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])


# GET STUDENT
@app.route("/api/students/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())


# CREATE STUDENT
@app.route("/api/students", methods=["POST"])
def create_student():
    data = request.get_json()

    student = Student(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(student)
    db.session.commit()

    return jsonify(student.to_dict()), 201


# UPDATE STUDENT
@app.route("/api/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)

    data = request.get_json()

    student.name = data["name"]
    student.email = data["email"]

    db.session.commit()

    return jsonify(student.to_dict())


# DELETE STUDENT
@app.route("/api/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    return "", 204


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll_student(id):

    data = request.get_json()

    course_id = data["course_id"]

    try:
        response = requests.get(
            f"http://127.0.0.1:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({
                "message": "Course not found"
            }), 404

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service Unavailable"
        }), 503

    enrollment = Enrollment(
        student_id=id,
        course_id=course_id
    )

    db.session.add(enrollment)
    db.session.commit()

    return jsonify({
        "message": "Enrollment Successful"
    }), 201

if __name__ == "__main__":
    app.run(port=5002, debug=True)
