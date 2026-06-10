from persistence.dummy_db import maderboard_db

def create(maderboard):
    return maderboard_db.create(maderboard)

def get_all():
    return maderboard_db.get_all()

def get_by_id(maderboard_id):
    return maderboard_db.get_by_id(maderboard_id)

def update_maderboard(maderboard_id, data):
    return maderboard_db.update(maderboard_id, data)

def delete_by_id(maderboard_id):
    return maderboard_db.delete_by_id(maderboard_id)
