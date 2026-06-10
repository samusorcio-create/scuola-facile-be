from persistence.dummy_db import memoria_fissa_db

def create(memoria_fissa):
    return memoria_fissa_db.create(memoria_fissa)

def get_all():
    return memoria_fissa_db.get_all()

def get_by_id(memoria_fissa_id):
    return memoria_fissa_db.get_by_id(memoria_fissa_id)

def update_memoria_fissa(memoria_fissa_id, data):
    return memoria_fissa_db.update(memoria_fissa_id, data)

def delete_by_id(memoria_fissa_id):
    return memoria_fissa_db.delete_by_id(memoria_fissa_id)
