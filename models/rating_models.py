from DB.db_config import db
from bson.objectid import ObjectId




rating_collection = db["ratings"]


def insert_rating(ride_id: str, rider_id: str, driver_id: str, rating: int, feedback: str = "") -> str:
    if rating < 0 or rating > 5:
        raise ValueError("Rating must be between 0 and 5")

    data = {
        "ride_id": ObjectId(ride_id),
        "rider_id": ObjectId(rider_id),
        "driver_id": ObjectId(driver_id),
        "rating": rating,
        "feedback": feedback
    }

    result = rating_collection.insert_one(data)
    return str(result.inserted_id)


def get_ratings_by_driver(driver_id: str):
    ratings = rating_collection.find({"driver_id": ObjectId(driver_id)})
    return [
        {
            "ride_id": str(r["ride_id"]),
            "rider_id": str(r["rider_id"]),
            "driver_id": str(r["driver_id"]),
            "rating": r["rating"],
            "feedback": r.get("feedback", "")
        } for r in ratings
    ]


def get_ratings_by_rider(rider_id: str):
    ratings = rating_collection.find({"rider_id": ObjectId(rider_id)})
    return [
        {
            "ride_id": str(r["ride_id"]),
            "rider_id": str(r["rider_id"]),
            "driver_id": str(r["driver_id"]),
            "rating": r["rating"],
            "feedback": r.get("feedback", "")
        } for r in ratings
    ]


def get_rating_by_ride(ride_id: str):
    r = rating_collection.find_one({"ride_id": ObjectId(ride_id)})
    if not r:
        return None
    return {
        "ride_id": str(r["ride_id"]),
        "rider_id": str(r["rider_id"]),
        "driver_id": str(r["driver_id"]),
        "rating": r["rating"],
        "feedback": r.get("feedback", "")
    }


def update_rating(ride_id: str, rating: int = None, feedback: str = None):
    update_data = {}
    if rating is not None:
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        update_data["rating"] = rating
    if feedback is not None:
        update_data["feedback"] = feedback

    if not update_data:
        return None

    return rating_collection.update_one(
        {"ride_id": ObjectId(ride_id)},
        {"$set": update_data}
    )
