from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast
from models.rides_models import get_rides_by_status, update_ride_status
from bson import ObjectId

class ViewRideByIdScreen(MDScreen):

    def on_pre_enter(self):
        """Automatically load all requested rides for the current rider."""
        self.show_requested_rides()

    def show_requested_rides(self):
        """Display all rides for the current rider with status 'Requested'."""
        self.ids.ride_details_box.clear_widgets()
        user_id = str(self.manager.user["_id"])  # Current logged-in user ID

        rides = get_rides_by_status(user_id, status="Requested")
        if not rides:
            toast("No rides with status 'Requested'.")
            return

        for ride in rides:
            ride_box = MDBoxLayout(
                orientation="vertical",
                spacing="5dp",
                padding="5dp",
                size_hint_y=None
            )
            ride_box.height = 150  # Adjust height as needed

            # Show ride details clearly
            for key, label in [("_id", "Ride ID"), ("pickup", "Pickup"), ("drop_location", "Drop"), ("status", "Status")]:
                ride_box.add_widget(MDLabel(
                    text=f"{label}: {ride.get(key)}",
                    size_hint_y=None,
                    height="25dp"
                ))

            # Add Cancel button only if ride is requested
            if ride.get("status") == "Requested":
                cancel_btn = MDRaisedButton(
                    text="Cancel Ride",
                    md_bg_color=(1, 0, 0, 1),
                    size_hint_y=None,
                    height="35dp",
                    on_release=lambda btn, rid=ride["_id"]: self.cancel_ride(rid)
                )
                ride_box.add_widget(cancel_btn)

            self.ids.ride_details_box.add_widget(ride_box)

    def cancel_ride(self, ride_id):
        """Cancel ride by updating its status and refresh list."""
        try:
            update_ride_status(str(ride_id), "Cancelled")
            toast(f"Ride {ride_id} cancelled successfully!")
            self.show_requested_rides()  # Refresh list
        except Exception as e:
            toast(f"Failed to cancel ride: {str(e)}")
