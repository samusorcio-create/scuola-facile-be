from repository import case_repository
from model.case import case
from exception.app_exception import AppException


def create(data):
    _validate_case(data)

    # Controllo duplicati per id
    if case_repository.get_by_id(data["id"]) is not None:
        raise AppException("Questo id esiste già!", 409)

    case_2_create = case(data["id"],
                         data["nome"],
                         data["descrizione"],
                         data["img"],
                         data["potenza"],
                         data["certificazione"],
                         data["modularita"],
                         data["sistemi_di_protezione"])

    return case_repository.create(case_2_create)

def get_all():
    return case_repository.get_all()

def get_by_id(case_id):
    case = case_repository.get_by_id(case_id)

    if case is None:
        raise AppException("Case non trovato!", 404)

    return case

def get_all():
    return case_repository.get_all()

def get_by_id(case_id):
    case = case_repository.get_by_id(case_id)

    if case is None:
        raise AppException("Case non trovato!", 404)

    return case

def update(case_id, data):
    if "password" in data:
        _validate_case(data)

    updated = case_repository.update(case_id, data)

    if updated is None:
        raise AppException("Case non trovato!", 404)

    return updated

def delete_by_id(case_id):
    case_repository.delete_by_id(case_id)

def _validate_case(data_case):

    # Campi obbligatori
    for campo in ["nome", "descrizione", "img", "potenza", "certificazione", "modularita", "sistemi_di_protezione"]:
        if campo not in data_case or len(data_case[campo].strip()) == 0:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)

        # # Formato email
        # if "@" not in data_case["email"] or "." not in data_case["email"]:
        #     raise AppException("Formato email non valido!", 400)

    # Password
    # if "password" not in data_case or len(data_case["password"].strip()) == 0:
    #     raise AppException("Password mancante!", 400)

    # if len(data_case["password"]) < 4:
    #     raise AppException("Password troppo corta!", 400)
