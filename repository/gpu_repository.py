from persistence.dummy_db import gpu_db

def create(gpu):
    return gpu_db.create(gpu)

def get_all():
    return gpu_db.get_all()

def get_by_id(gpu_id):
    return gpu_db.get_by_id(gpu_id)

def update_gpu(gpu_id, data):
    return gpu_db.update(gpu_id, data)

def delete_by_id(gpu_id):
    return gpu_db.delete_by_id(gpu_id)
