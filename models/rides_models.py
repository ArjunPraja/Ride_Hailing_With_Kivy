
from DB.db_config import db
from bson.objectid import ObjectId


rides_collection = db["rides"]


def insert_ride(data: dict):
    return rides_collection.insert_one(data)

def get_all_rides():
    return list(rides_collection.find())

def get_ride_by_id(ride_id: str):
    try:
        return rides_collection.find_one({"_id": ObjectId(ride_id)})
    except:
        return None

def get_rides_by_user(user_id: str, role: str = "passenger"):
    if role == "driver":
        return list(rides_collection.find({"driver_id": user_id}))
    return list(rides_collection.find({"user_id": user_id}))

def update_ride_status(ride_id: str, status: str):
    try:
        return rides_collection.update_one(
            {"_id": ObjectId(ride_id)},
            {"$set": {"status": status}}
        )
    except:
        return None

def delete_ride(ride_id: str):
    try:
        return rides_collection.delete_one({"_id": ObjectId(ride_id)})
    except:
        return None
