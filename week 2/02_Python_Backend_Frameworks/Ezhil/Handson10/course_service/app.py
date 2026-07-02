from flask import Flask, jsonify, request
from database import db
from models import Course
import requests
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///course.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# GET ALL COURSES
@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])


# GET COURSE BY ID
@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict())


# CREATE COURSE
@app.route("/api/courses", methods=["POST"])
def create_course():
    data = request.get_json()

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


# UPDATE COURSE
@app.route("/api/courses/<int:id>", methods=["PUT"])
def update_course(id):
    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.name = data["name"]
    course.code = data["code"]
    course.credits = data["credits"]

    db.session.commit()

    return jsonify(course.to_dict())


# DELETE COURSE
@app.route("/api/courses/<int:id>", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return "", 204
@app.route("/")
def home():
    return "Course Service is Running"

if __name__ == "__main__":
    app.run(port=5001, debug=True)