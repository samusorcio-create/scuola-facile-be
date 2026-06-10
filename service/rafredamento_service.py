from repository import memoria_volatile_repository, rafredamento_repository
from model.rafredamento import memoria_volatile, rafredamento
from exception.app_exception import AppException

def create(data):
    _validate_rafredamento(data)

    # Controllo duplicati per id
    if rafredamento_repository.get_by_id(data["id"]) is not None:
        raise AppException("Raffreddamento con questo id esiste già!", 409)

    # # Controllo duplicati per email
    # existing = cpu_repository.get_by_field("email", data["email"])
    # if len(existing) > 0:
    #     raise AppException("Email già registrata!", 409)

    # "converto" oggetto dalla richiesta HTTP ad un oggetto di tipo Studente perché il repo si aspetta già uno studente
    memoria_volatile_2_create = rafredamento(data["id"],
                               data["nome"],
                                data["descrizione"],   
                                data["img"],
                                data["marca"],
                                data["rumorosita"],
                                data["compatibilita"],
                                data["flusso_aria"],
                                data["size_radiatore"],
                                data["compatibilita_socket"],)

    return rafredamento_repository.create(memoria_volatile_2_create)

def get_all():
    return rafredamento_repository.get_all()

def get_by_id(rafredamento_id):
    rafredamento = rafredamento_repository.get_by_id(rafredamento_id)

    if rafredamento is None:
        raise AppException("Raffreddamento non trovato!", 404)

    return rafredamento

# Ricerca Raffreddamento per campo (es: corso=Informatica)
def search_by_field(field, value):
    return rafredamento_repository.get_by_field(field, value)

def update(rafredamento_id, data):
    if "password" in data:
        _validate_rafredamento(data)

    updated = rafredamento_repository.update(rafredamento_id, data)

    if updated is None:
        raise AppException("Raffreddamento non trovato!", 404)

    return updated

def delete_by_id(rafredamento_id):
    rafredamento_repository.delete_by_id(rafredamento_id)

# Qui metto tutti i vincoli che mi potrei anche sul DB (chiavi not null, vincoli numerici ect ect )
# data_rafredamento perchè non ho una rafredamento, ho "data" che mi arriva dal FE
def _validate_rafredamento(data_rafredamento):

    # Campi obbligatori
    for campo in ["nome", "descrizione", "img", "potenza", "certificazione", "modularita", "sistemi_di_protezione"]:
        if campo not in data_rafredamento or len(data_rafredamento[campo].strip()) == 0:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)

    # # Formato email
    # if "@" not in data_student["email"] or "." not in data_student["email"]:
    #     raise AppException("Formato email non valido!", 400)

    # # Vincolo: pwd > 4 caratteri
    # if "password" not in data_student:
    #     raise AppException("Password mancante!", 400)

    # if len(data_student["password"]) < 4:
    #     raise AppException("Password troppo corta!", 400)
