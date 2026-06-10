from repository import cpu_repository, gpu_repository
from model.gpu import gpu
from exception.app_exception import AppException
from service.cpu_service import _validate_cpu


# data viene dalla request HTTP, non è ancora un reale oggetto Python di tipo CPU
def create(data):
    _validate_cpu(data)

    # Controllo duplicati per id
    if gpu_repository.get_by_id(data["id"]) is not None:
        raise AppException("GPU con questo id esiste già!", 409)

    # # Controllo duplicati per email
    # existing = gpu_repository.get_by_field("email", data["email"])
    # if len(existing) > 0:
    #     raise AppException("Email già registrata!", 409)

    # "converto" oggetto dalla richiesta HTTP ad un oggetto di tipo Studente perché il repo si aspetta già uno studente
    gpu_2_create = gpu(data["id"],
                                data["nome"],
                                data["descrizione"],   
                                data["img"],
                                data["core"],
                                data["memoria_VRAM"],
                                data["bandwhith"],
                                data["TDP"],
                                data["formato"],
                                data["MHz"],
                                data["tech_supportata"])

    return gpu_repository.create(gpu_2_create)

def get_all():
    return gpu_repository.get_all()

def get_by_id(gpu_id):
    gpu = gpu_repository.get_by_id(gpu_id)

    if gpu is None:
        raise AppException("GPU non trovato!", 404)

    return gpu

# Ricerca GPU per campo (es: corso=Informatica)
def search_by_field(field, value):
    return gpu_repository.get_by_field(field, value)

def update(gpu_id, data):
    if "password" in data:
        _validate_gpu(data)

    updated = gpu_repository.update(gpu_id, data)

    if updated is None:
        raise AppException("GPU non trovato!", 404)

    return updated

def delete_by_id(gpu_id):
    gpu_repository.delete_by_id(gpu_id)

# Qui metto tutti i vincoli che mi potrei anche sul DB (chiavi not null, vincoli numerici ect ect )
# data_gpu perchè non ho una gpu, ho "data" che mi arriva dal FE
def _validate_gpu(data_gpu):

    # Campi obbligatori
    for campo in ["nome", "descrizione", "img", "potenza", "certificazione", "modularita", "sistemi_di_protezione"]:
        if campo not in data_gpu or len(data_gpu[campo].strip()) == 0:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)

    # # Formato email
    # if "@" not in data_student["email"] or "." not in data_student["email"]:
    #     raise AppException("Formato email non valido!", 400)

    # # Vincolo: pwd > 4 caratteri
    # if "password" not in data_student:
    #     raise AppException("Password mancante!", 400)

    # if len(data_student["password"]) < 4:
    #     raise AppException("Password troppo corta!", 400)
