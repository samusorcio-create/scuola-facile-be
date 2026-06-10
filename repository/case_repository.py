from persistence.dummy_db import case_db

def create(case):
    return case_db.create(case)

def get_all():
    return case_db.get_all()

def get_by_id(case_id):
    return case_db.get_by_id(case_id)

# Cerca studenti per un campo specifico (es: "corso", "Informatica")
def get_by_field(field, value):
    return case_db.get_by_field(field, value)

def update_case(case_id, data):
    return case_db.update(case_id, data)

def delete_by_id(case_id):
    return case_db.delete_by_id(case_id)
