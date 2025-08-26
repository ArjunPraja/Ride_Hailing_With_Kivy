from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from models.rides_models import rides_collection
from bson.objectid import ObjectId

class AcceptedRideItem(Screen):
    ride_id = StringProperty()
    pickup = StringProperty()
    drop_location = StringProperty()
    status = StringProperty()
    fare = StringProperty()
    parent_rv = ObjectProperty()

    def start_ride(self):
        """Start ride: update status to In Progress"""
        rides_collection.update_one(
            {"_id": ObjectId(self.ride_id)},
            {"$set": {"status": "In Progress"}}
        )
        self.status = "In Progress"
        self.update_buttons()

    def complete_ride(self):
        """Complete ride: update status to Completed"""
        rides_collection.update_one(
            {"_id": ObjectId(self.ride_id)},
            {"$set": {"status": "Completed"}}
        )
        self.status = "Completed"
        self.update_buttons()

    def cancel_ride(self):
        """Cancel ride"""
        rides_collection.update_one(
            {"_id": ObjectId(self.ride_id)},
            {"$set": {"status": "Cancelled"}}
        )
        self.status = "Cancelled"
        self.update_buttons()

    def update_buttons(self):
        """Update button visibility based on status"""
        for child in self.children:
            for widget in child.children:
                if hasattr(widget, "text"):
                    if widget.text == "Start Ride":
                        widget.disabled = self.status != "Accepted"
                    elif widget.text == "Cancel Ride":
                        widget.disabled = self.status in ["Completed", "Cancelled"]
                    elif widget.text == "Completed":
                        widget.disabled = self.status != "In Progress"


class MyAcceptedRidesScreen(Screen):
    rides_list = ObjectProperty()
    no_rides_label = ObjectProperty()

    def on_pre_enter(self, *args):
        Clock.schedule_once(lambda dt: self.load_rides())

    def load_rides(self):
        """Load all accepted rides for the current driver"""
        driver = getattr(self.manager, "user", None)
        if not driver:
            self.no_rides_label.text = "Driver not logged in"
            self.no_rides_label.opacity = 1
            self.rides_list.data = []
            return

        rides_cursor = rides_collection.find({"driver_id": str(driver["_id"])})

        rides = list(rides_cursor)

        if not rides:
            self.rides_list.data = []
            self.no_rides_label.text = "No Accepted Rides"
            self.no_rides_label.opacity = 1
        else:
            self.no_rides_label.opacity = 0
            self.rides_list.data = [{
                "ride_id": str(ride.get("_id")),
                "pickup": ride.get("pickup", ""),
                "drop_location": ride.get("drop_location", ""),
                "status": ride.get("status", ""),
                "fare": str(ride.get("fare", "")),
                "parent_rv": self.rides_list
            } for ride in rides]
