from flask import jsonify, request, Blueprint
from service import alimentatore_service
from exception.app_exception import AppException

corso_bp = Blueprint("course", __name__, url_prefix="/api")

# GET ALL COURSES
@corso_bp.route("/courses")
def get_courses():

    courses = alimentatore_service.get_all()

    return jsonify([c.to_dict() for c in courses])


# GET COURSE BY ID
@corso_bp.route("/course/<course_id>")
def get_course_by_id(course_id):

    try:
        course = alimentatore_service.get_by_id(course_id)

        return jsonify(course.to_dict())

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# CREATE COURSE
@corso_bp.route("/course", methods=["POST"])
def create():

    data = request.get_json()

    try:
        new_course = alimentatore_service.create(data)

        return jsonify(new_course.to_dict()), 201

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# UPDATE COURSE
@corso_bp.route("/course/<course_id>", methods=["PATCH"])
def update(course_id):

    data = request.get_json()

    try:
        updated = alimentatore_service.update(course_id, data)

        return jsonify(updated.to_dict())

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# DELETE COURSE BY ID
@corso_bp.route("/course/<course_id>", methods=["DELETE"])
def delete_course_by_id(course_id):

    alimentatore_service.delete_by_id(course_id)

    return jsonify({"message": "Corso Eliminato"})
