from persistence.dummy_db import memoria_volatile_db

def create(memoria_volatile):
    return memoria_volatile_db.create(memoria_volatile)

def get_all():
    return memoria_volatile_db.get_all()

def get_by_id(memoria_volatile_id):
    return memoria_volatile_db.get_by_id(memoria_volatile_id)

def update_memoria_volatile(memoria_volatile_id, data):
    return memoria_volatile_db.update(memoria_volatile_id, data)

def delete_by_id(memoria_volatile_id):
    return memoria_volatile_db.delete_by_id(memoria_volatile_id)
