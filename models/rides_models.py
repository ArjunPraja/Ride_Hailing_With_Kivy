
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
    return list(rides_collection.find({"rider_id": user_id}))


def get_rides_by_status(user_id: str, status: str):
    rides = list(rides_collection.find({"rider_id": user_id, "status": status}))
    for ride in rides:
        ride["_id"] = str(ride["_id"])
    return rides

def update_ride_status(ride_id: str, status: str):
    try:
        return rides_collection.update_one(
            {"_id": ObjectId(ride_id)},
            {"$set": {"status": status}}
        )
    except:
        return None
    
def get_all_requested_rides():
    """Fetch all rides with status 'Requested'."""
    rides = list(rides_collection.find({"status": "Requested"}))
    for ride in rides:
        ride["_id"] = str(ride["_id"])  
    return rides

def update_cancel_rider(rider_id: str):
    """Cancel the first requested ride for the rider."""
    ride = rides_collection.find_one({"rider_id": rider_id, "status": "Requested"})
    if not ride:
        return None  # No ride found
    rides_collection.update_one(
        {"_id": ride["_id"]},
        {"$set": {"status": "Cancelled"}}
    )
    return str(ride["_id"])



def show_my_accepted_rides(driver_id):
    rides = rides_collection.find({"driver_id": driver_id, "status": "Completed"})
    return list(rides)  



def show_driver_all_rides(driver_id: str):
    """
    Fetch all rides for a specific driver using driver_id.
    """
    try:
        rides = list(rides_collection.find({"driver_id": driver_id}))
        return rides
    except Exception as e:
        print("Error fetching driver rides:", e)
        return []
