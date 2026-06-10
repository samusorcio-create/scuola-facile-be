from persistence.dummy_db import cpu_db

def create(cpu):
    return cpu_db.create(cpu)

def get_all():
    return cpu_db.get_all()

def get_by_id(cpu_id):
    return cpu_db.get_by_id(cpu_id)

# Cerca studenti per un campo specifico (es: "corso", "Informatica")
def get_by_field(field, value):
    return cpu_db.get_by_field(field, value)

def update_cpu(cpu_id, data):
    return cpu_db.update(cpu_id, data)

def delete_by_id(cpu_id):
    return cpu_db.delete_by_id(cpu_id)
