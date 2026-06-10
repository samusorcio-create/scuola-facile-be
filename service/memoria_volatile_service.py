from repository import maderboard_repository, memoria_volatile_repository
from model.memoria_volatile import memoria_volatile
from exception.app_exception import AppException

def create(data):
    _validate_memoria_volatile(data)

    # Controllo duplicati per id
    if memoria_volatile_repository.get_by_id(data["id"]) is not None:
        raise AppException("Memoria volatile con questo id esiste già!", 409)

    # # Controllo duplicati per email
    # existing = cpu_repository.get_by_field("email", data["email"])
    # if len(existing) > 0:
    #     raise AppException("Email già registrata!", 409)

    # "converto" oggetto dalla richiesta HTTP ad un oggetto di tipo Studente perché il repo si aspetta già uno studente
    memoria_volatile_2_create = memoria_volatile(data["id"],
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

    return memoria_volatile_repository.create(memoria_volatile_2_create)

def get_all():
    return memoria_volatile_repository.get_all()

def get_by_id(memoria_volatile_id):
    memoria_volatile = memoria_volatile_repository.get_by_id(memoria_volatile_id)

    if memoria_volatile is None:
        raise AppException("Memoria volatile non trovato!", 404)

    return memoria_volatile

# Ricerca Memoria volatile per campo (es: corso=Informatica)
def search_by_field(field, value):
    return memoria_volatile_repository.get_by_field(field, value)

def update(memoria_volatile_id, data):
    if "password" in data:
        _validate_memoria_volatile(data)

    updated = memoria_volatile_repository.update(memoria_volatile_id, data)

    if updated is None:
        raise AppException("Memoria volatile non trovato!", 404)

    return updated

def delete_by_id(memoria_volatile_id):
    memoria_volatile_repository.delete_by_id(memoria_volatile_id)

# Qui metto tutti i vincoli che mi potrei anche sul DB (chiavi not null, vincoli numerici ect ect )
# data_memoria_volatile perchè non ho una memoria_volatile, ho "data" che mi arriva dal FE
def _validate_memoria_volatile(data_memoria_volatile):

    # Campi obbligatori
    for campo in ["nome", "descrizione", "img", "potenza", "certificazione", "modularita", "sistemi_di_protezione"]:
        if campo not in data_memoria_volatile or len(data_memoria_volatile[campo].strip()) == 0:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)

    # # Formato email
    # if "@" not in data_student["email"] or "." not in data_student["email"]:
    #     raise AppException("Formato email non valido!", 400)

    # # Vincolo: pwd > 4 caratteri
    # if "password" not in data_student:
    #     raise AppException("Password mancante!", 400)

    # if len(data_student["password"]) < 4:
    #     raise AppException("Password troppo corta!", 400)
