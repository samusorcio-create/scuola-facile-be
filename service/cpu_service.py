from repository import cpu_repository
from model.cpu import cpu
from exception.app_exception import AppException


# data viene dalla request HTTP, non è ancora un reale oggetto Python di tipo CPU
def create(data):
    _validate_cpu(data)

    # Controllo duplicati per id
    if cpu_repository.get_by_id(data["id"]) is not None:
        raise AppException("CPU con questo id esiste già!", 409)

    # # Controllo duplicati per email
    # existing = cpu_repository.get_by_field("email", data["email"])
    # if len(existing) > 0:
    #     raise AppException("Email già registrata!", 409)

    # "converto" oggetto dalla richiesta HTTP ad un oggetto di tipo Studente perché il repo si aspetta già uno studente
    cpu_2_create = cpu(data["id"],
                               data["nome"],
                                data["descrizione"],   
                               data["img"],
                               data["potenza"],
                               data["certificazione"],
                               data["modularita"],
                               data["sistemi_di_protezione"])

    return cpu_repository.create(cpu_2_create)

def get_all():
    return cpu_repository.get_all()

def get_by_id(cpu_id):
    cpu = cpu_repository.get_by_id(cpu_id)

    if cpu is None:
        raise AppException("CPU non trovato!", 404)

    return cpu

# Ricerca CPU per campo (es: corso=Informatica)
def search_by_field(field, value):
    return cpu_repository.get_by_field(field, value)

def update(cpu_id, data):
    if "password" in data:
        _validate_cpu(data)

    updated = cpu_repository.update(cpu_id, data)

    if updated is None:
        raise AppException("CPU non trovato!", 404)

    return updated

def delete_by_id(cpu_id):
    cpu_repository.delete_by_id(cpu_id)

# Qui metto tutti i vincoli che mi potrei anche sul DB (chiavi not null, vincoli numerici ect ect )
# data_cpu perchè non ho una cpu, ho "data" che mi arriva dal FE
def _validate_cpu(data_cpu):

    # Campi obbligatori
    for campo in ["nome", "descrizione", "img", "potenza", "certificazione", "modularita", "sistemi_di_protezione"]:
        if campo not in data_cpu or len(data_cpu[campo].strip()) == 0:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)

    # # Formato email
    # if "@" not in data_student["email"] or "." not in data_student["email"]:
    #     raise AppException("Formato email non valido!", 400)

    # # Vincolo: pwd > 4 caratteri
    # if "password" not in data_student:
    #     raise AppException("Password mancante!", 400)

    # if len(data_student["password"]) < 4:
    #     raise AppException("Password troppo corta!", 400)
