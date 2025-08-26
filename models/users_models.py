from DB.db_config import db

user_collection = db['users']

def insert_users(data):
    return user_collection.insert_one(data)

def find_by_email(email):
    return user_collection.find_one({'email': email})
