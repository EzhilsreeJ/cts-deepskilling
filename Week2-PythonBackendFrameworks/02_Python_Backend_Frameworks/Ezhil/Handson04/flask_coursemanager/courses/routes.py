from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = [
    {
        "id": 1,
        "name": "Python",
        "code": "PY101",
        "credits": 4
    }
]


def make_response_json(data, status_code):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


@courses_bp.route("/", methods=["GET"])
def get_courses():
    return make_response_json(courses, 200)


@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):

    for course in courses:
        if course["id"] == course_id:
            return make_response_json(course, 200)

    return jsonify({
        "status": "error",
        "message": "Course not found"
    }), 404


@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    if data is None:
        return jsonify({
            "status": "error",
            "message": "Content-Type must be application/json"
        }), 400

    required = ["name", "code", "credits"]

    for field in required:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"{field} is required"
            }), 400

    new_course = {
        "id": len(courses) + 1,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"]
    }

    courses.append(new_course)

    return make_response_json(new_course, 201)


@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):

    data = request.get_json()

    for course in courses:

        if course["id"] == course_id:

            course["name"] = data.get("name", course["name"])
            course["code"] = data.get("code", course["code"])
            course["credits"] = data.get("credits", course["credits"])

            return jsonify({
                "status": "success",
                "message": "Course updated successfully",
                "data": course
            }), 200

    return jsonify({
        "status": "error",
        "message": "Course not found"
    }), 404

@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):

    for course in courses:

        if course["id"] == course_id:
            courses.remove(course)

            return jsonify({
                "status": "success",
                "message": "Course deleted"
            }), 200

    return jsonify({
        "status": "error",
        "message": "Course not found"
    }), 404

#task-1
# from flask import Blueprint, jsonify

# courses_bp = Blueprint(
#     "courses",
#     __name__,
#     url_prefix="/api/courses"
# )

# @courses_bp.route("/", methods=["GET"])
# def get_courses():
#     return jsonify([]), 200


# @courses_bp.route("/", methods=["POST"])
# def create_course():
#     return jsonify({
#         "message": "Course created"
#     }), 201