from DB.db_config import db
from bson import ObjectId

vehicle_collection = db['vehicle']

def insert_vehicle(data):
    return vehicle_collection.insert_one(data)

def get_vehicle_by_id(driver_id):
    return vehicle_collection.find_one({"driver_id": driver_id})

def update_vehicle_details(id, data):
    return vehicle_collection.update_one({"_id": ObjectId(id)}, {"$set": data})

def get_all_vehicles():
    return list(vehicle_collection.find())




