from flask import jsonify, request, Blueprint
from service import cpu_service
from exception.app_exception import AppException

studente_bp = Blueprint("student", __name__, url_prefix="/api")

# GET ALL STUDENTS (con filtro opzionale per query params)
# ES: GET /api/students?corso=Informatica
@studente_bp.route("/students")
def get_students():

    # Prendo il primo query param disponibile per filtrare
    corso = request.args.get("corso")

    if corso:
        students = cpu_service.search_by_field("corso", corso)
    else:
        students = cpu_service.get_all()

    return jsonify([s.to_dict() for s in students])


# GET STUDENT BY ID
@studente_bp.route("/student/<student_id>")
def get_student_by_id(student_id):

    try:
        student_by_id = cpu_service.get_by_id(student_id)

        return jsonify(student_by_id.to_dict())

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# CREATE STUDENT
@studente_bp.route("/student", methods=["POST"])
def create():

    data = request.get_json() #Dal Body della richiesta

    try:
        new_student = cpu_service.create(data)

        # 201 --> HTTP status code per "create"
        return jsonify(new_student.to_dict()), 201

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# UPDATE STUDENT
@studente_bp.route("/student/<student_id>", methods=["PATCH"])
def update(student_id):

    data = request.get_json() #Dal Body della richiesta

    try:
        updated = cpu_service.update(student_id, data)

        return jsonify(updated.to_dict())

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# DELETE STUDENT BY ID
@studente_bp.route("/student/<student_id>", methods=["DELETE"])
def delete_student_by_id(student_id):

    cpu_service.delete_by_id(student_id)

    return jsonify({"message": "Studente Eliminato"})
