from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from bson.objectid import ObjectId
from models.rides_models import get_all_requested_rides, rides_collection


class RideRequestItem(Screen):
    ride_id = StringProperty()
    pickup = StringProperty()
    drop_location = StringProperty()
    status = StringProperty()
    fare = StringProperty()
    parent_rv = ObjectProperty()
    current_user = ObjectProperty()  # reference to logged-in driver

    def accept_ride(self):
        """Accept the ride, assign driver, and update UI."""
        if not self.current_user:
            return

        # Update ride in MongoDB
        rides_collection.update_one(
            {"_id": ObjectId(self.ride_id)},
            {"$set": {"status": "Accepted", "driver_id": str(self.current_user["_id"])}}
        )

        # Update UI
        self.status = "Accepted"
        for child in self.children:
            for widget in child.children:
                if hasattr(widget, "text") and widget.text == "Accept":
                    widget.disabled = True
                    widget.text = "Accepted"


class ShowRidesScreen(Screen):
    rides_list = ObjectProperty()
    no_rides_label = ObjectProperty()

    def on_pre_enter(self, *args):
        """Load rides when screen appears."""
        Clock.schedule_once(lambda dt: self.load_rides())

    def load_rides(self):
        """Fetch all requested rides and populate the list."""
        user = getattr(self.manager, "user", None)
        rides = list(get_all_requested_rides())

        if not rides:
            self.rides_list.data = []
            self.no_rides_label.text = "No Ride Requests"
            self.no_rides_label.opacity = 1
            return

        self.no_rides_label.opacity = 0
        self.rides_list.data = [{
            "ride_id": str(ride.get("_id")),
            "pickup": ride.get("pickup", ""),
            "drop_location": ride.get("drop_location", ""),
            "status": ride.get("status", "Requested"),
            "fare": str(ride.get("fare", "")),
            "parent_rv": self.rides_list,
            "current_user": user
        } for ride in rides]
