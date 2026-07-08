from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://127.0.0.1:5001"
STUDENT_SERVICE = "http://127.0.0.1:5002"


@app.route("/")
def home():
    return "API Gateway Running"


# ---------- Course Service ----------
@app.route("/api/courses", methods=["GET", "POST"])
def gateway_courses():
    if request.method == "GET":
        response = requests.get(f"{COURSE_SERVICE}/api/courses")
    else:
        response = requests.post(
            f"{COURSE_SERVICE}/api/courses",
            json=request.json
        )

    return jsonify(response.json()), response.status_code


# ---------- Student Service ----------
@app.route("/api/students", methods=["GET", "POST"])
def gateway_students():
    if request.method == "GET":
        response = requests.get(f"{STUDENT_SERVICE}/api/students")
    else:
        response = requests.post(
            f"{STUDENT_SERVICE}/api/students",
            json=request.json
        )

    return jsonify(response.json()), response.status_code


if __name__ == "__main__":
    app.run(port=5000, debug=True)