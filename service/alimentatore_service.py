from repository import alimentatore_repository
from model.alimentatore import alimentatore
from exception.app_exception import AppException


def create(data):
    _validate_alimentatore(data)

    # Controllo duplicati per id
    if alimentatore_repository.get_by_id(data["id"]) is not None:
        raise AppException("questo id esiste già!", 409)

    alimentatore_2_create = alimentatore(data["id"],
                             data["nome"],
                             data["descrizione"],
                             data["img"],
                             data["potenza"],
                             data["certificazione"],
                             data["modularita"],
                             data["sistemi_di_protezione"])

    return alimentatore_repository.create(alimentatore_2_create)

def get_all():
    return alimentatore_repository.get_all()

def get_by_id(alimentatore_id):
    alimentatore = alimentatore_repository.get_by_id(alimentatore_id)

    if alimentatore is None:
        raise AppException("non trovato!", 404)

    return alimentatore

def update(alimentatore_id, data):
    updated = alimentatore_repository.update_alimentatore(alimentatore_id, data)

    if updated is None:
        raise AppException("non trovato!", 404)

    return updated

def delete_by_id(alimentatore_id):
    alimentatore_repository.delete_by_id(alimentatore_id)

def _validate_alimentatore(data_alimentatore):

    # Campi obbligatori
    for campo in ["nome", "descrizione"]:
        if campo not in data_alimentatore or len(data_alimentatore[campo].strip()) == 0:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)
