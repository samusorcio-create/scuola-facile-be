from persistence.dummy_db import rafreddamento_db

def create(rafreddamento):
    return rafreddamento_db.create(rafreddamento)

def get_all():
    return rafreddamento_db.get_all()

def get_by_id(rafreddamento_id):
    return rafreddamento_db.get_by_id(rafreddamento_id)

def update_rafreddamento(rafreddamento_id, data):
    return rafreddamento_db.update(rafreddamento_id, data)

def delete_by_id(rafreddamento_id):
    return rafreddamento_db.delete_by_id(rafreddamento_id)
