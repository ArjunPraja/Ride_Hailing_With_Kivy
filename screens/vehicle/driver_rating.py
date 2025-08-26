from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.toast import toast

from models.rating_models import get_ratings_by_driver
from models.rides_models import get_ride_by_id  


class RatingsScreen(MDScreen):

    def on_pre_enter(self):
        """Load all ratings when screen opens."""
        self.load_ratings()

    def load_ratings(self):
        self.ids.ratings_container.clear_widgets()
        user = getattr(self.manager, "user", None)
        if not user:
            toast("User not found!")
            return

        # Fetch all ratings where the user is a driver
        ratings = get_ratings_by_driver(str(user["_id"]))
        if not ratings:
            self.ids.ratings_container.add_widget(OneLineListItem(text="No ratings found."))
            return

        # Create table header
        header = MDBoxLayout(spacing="10dp", size_hint_y=None, height="40dp")
        for title in ["Pickup", "Drop", "Rating", "Feedback"]:
            header.add_widget(MDLabel(text=title, bold=True))
        self.ids.ratings_container.add_widget(header)

        # Populate ratings
        for rating in ratings:
            ride = get_ride_by_id(str(rating["ride_id"]))
            if not ride:
                continue

            row = MDBoxLayout(spacing="10dp", size_hint_y=None, height="40dp")
            row.add_widget(MDLabel(text=ride.get("pickup", "N/A")))
            row.add_widget(MDLabel(text=ride.get("drop_location", "N/A")))
            row.add_widget(MDLabel(text=str(rating.get("rating", 0))))
            row.add_widget(MDLabel(text=rating.get("feedback", "")))

            self.ids.ratings_container.add_widget(row)
