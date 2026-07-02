from flask import Blueprint, jsonify, request
from extensions import db
from courses.models import Course, Student, Enrollment

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


# GET ALL COURSES
@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses]), 200


# GET COURSE BY ID
@courses_bp.route("/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict()), 200


# CREATE COURSE
@courses_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


# UPDATE COURSE
@courses_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):
    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.name = data["name"]
    course.code = data["code"]
    course.credits = data["credits"]

    db.session.commit()

    return jsonify(course.to_dict()), 200


# DELETE COURSE
@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Course deleted successfully"
    }), 200

# GET STUDENTS ENROLLED IN A COURSE
@courses_bp.route("/<int:id>/students/", methods=["GET"])
def get_course_students(id):

    course = Course.query.get_or_404(id)

    students = []

    for enrollment in course.enrollments:
        students.append(enrollment.student.to_dict())

    return jsonify(students)

@courses_bp.route("/<int:id>/students/", methods=["GET"])
def get_students(id):

    course = Course.query.get_or_404(id)

    students = []

    for enrollment in course.enrollments:
        students.append(enrollment.student.to_dict())

    return jsonify(students)