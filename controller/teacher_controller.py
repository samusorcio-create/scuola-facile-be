from flask import jsonify, request, Blueprint
from service import case_service
from exception.app_exception import AppException

docente_bp = Blueprint("teacher", __name__, url_prefix="/api")

# GET ALL TEACHERS
@docente_bp.route("/teachers")
def get_teachers():

    teachers = case_service.get_all()

    return jsonify([t.to_dict() for t in teachers])


# GET TEACHER BY ID
@docente_bp.route("/teacher/<teacher_id>")
def get_teacher_by_id(teacher_id):

    try:
        teacher = case_service.get_by_id(teacher_id)

        return jsonify(teacher.to_dict())

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# CREATE TEACHER
@docente_bp.route("/teacher", methods=["POST"])
def create():

    data = request.get_json()

    try:
        new_teacher = case_service.create(data)

        return jsonify(new_teacher.to_dict()), 201

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# UPDATE TEACHER
@docente_bp.route("/teacher/<teacher_id>", methods=["PATCH"])
def update(teacher_id):

    data = request.get_json()

    try:
        updated = case_service.update(teacher_id, data)

        return jsonify(updated.to_dict())

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# DELETE TEACHER BY ID
@docente_bp.route("/teacher/<teacher_id>", methods=["DELETE"])
def delete_teacher_by_id(teacher_id):

    case_service.delete_by_id(teacher_id)

    return jsonify({"message": "Docente Eliminato"})
