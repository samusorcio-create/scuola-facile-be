from persistence.dummy_db import alimentatori_db

def create(alimentatore):
    return alimentatori_db.create(alimentatore)

def get_all():
    return alimentatori_db.get_all()

def get_by_id(alimentatore_id):
    return alimentatori_db.get_by_id(alimentatore_id)

def update_alimentatore(alimentatore_id, data):
    return alimentatori_db.update(alimentatore_id, data)

def delete_by_id(alimentatore_id):
    return alimentatori_db.delete_by_id(alimentatore_id)
