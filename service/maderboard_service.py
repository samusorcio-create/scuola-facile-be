from repository import maderboard_repository
from model.maderboard import motherboard
from exception.app_exception import AppException

def create(data):
    _validate_motherboard(data)

    # Controllo duplicati per id
    if maderboard_repository.get_by_id(data["id"]) is not None:
        raise AppException("Motherboard con questo id esiste già!", 409)

    # # Controllo duplicati per email
    # existing = cpu_repository.get_by_field("email", data["email"])
    # if len(existing) > 0:
    #     raise AppException("Email già registrata!", 409)

    # "converto" oggetto dalla richiesta HTTP ad un oggetto di tipo Studente perché il repo si aspetta già uno studente
    motherboard_2_create = motherboard(data["id"],
                               data["nome"],
                                data["descrizione"],   
                                data["img"],
                                data["marcha"],
                                data["chipset"],
                                data["formato"],
                                data["socket"],
                                data["slot_espansione_gpu"],
                                data["slot_espansione_ram"],
                                data["velocita_scheda"],)

    return maderboard_repository.create(motherboard_2_create)

def get_all():
    return maderboard_repository.get_all()

def get_by_id(motherboard_id):
    motherboard = maderboard_repository.get_by_id(motherboard_id)

    if motherboard is None:
        raise AppException("Motherboard non trovato!", 404)

    return motherboard

# Ricerca Motherboard per campo (es: corso=Informatica)
def search_by_field(field, value):
    return maderboard_repository.get_by_field(field, value)

def update(motherboard_id, data):
    if "password" in data:
        _validate_motherboard(data)

    updated = maderboard_repository.update(motherboard_id, data)

    if updated is None:
        raise AppException("Motherboard non trovato!", 404)

    return updated

def delete_by_id(motherboard_id):
    maderboard_repository.delete_by_id(motherboard_id)

# Qui metto tutti i vincoli che mi potrei anche sul DB (chiavi not null, vincoli numerici ect ect )
# data_motherboard perchè non ho una motherboard, ho "data" che mi arriva dal FE
def _validate_motherboard(data_motherboard):

    # Campi obbligatori
    for campo in ["nome", "descrizione", "img", "potenza", "certificazione", "modularita", "sistemi_di_protezione"]:
        if campo not in data_motherboard or len(data_motherboard[campo].strip()) == 0:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)

    # # Formato email
    # if "@" not in data_student["email"] or "." not in data_student["email"]:
    #     raise AppException("Formato email non valido!", 400)

    # # Vincolo: pwd > 4 caratteri
    # if "password" not in data_student:
    #     raise AppException("Password mancante!", 400)

    # if len(data_student["password"]) < 4:
    #     raise AppException("Password troppo corta!", 400)
