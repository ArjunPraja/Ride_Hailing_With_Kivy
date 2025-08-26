from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from models.rides_models import get_rides_by_status


class CompletedRidesScreen(MDScreen):
    def on_pre_enter(self):
        """Automatically load rides when this screen is opened."""
        self.load_rides()

    def load_rides(self):
        # ✅ Safely get the logged-in user
        user = getattr(self.manager, "user", None)
        if not user:
            print("⚠ No user found in manager")
            return

        user_id = str(user["_id"])

        # Clear old items
        self.ids.rides_list.clear_widgets()

        rides = get_rides_by_status(user_id, "Completed")

        if not rides:
            self.ids.rides_list.add_widget(
                OneLineListItem(text="No rides found.")
            )
            return

        # Loop rides and create card-like rows
        for ride in rides:
            ride_card = MDCard(
                orientation="vertical",
                size_hint=(1, None),
                height="120dp",
                padding="10dp",
                radius=[12, 12, 12, 12],
                md_bg_color=(0.95, 0.95, 0.95, 1),
                elevation=4,
            )

            box = MDBoxLayout(orientation="vertical", spacing="4dp")

            # Ride ID
            box.add_widget(MDLabel(
                text=f"🆔 Ride ID: {str(ride['_id'])}",
                theme_text_color="Primary",
                bold=True
            ))
            # Pickup & Drop
            box.add_widget(MDLabel(
                text=f"📍 {ride['pickup']} ➝ {ride['drop_location']}",
                theme_text_color="Secondary"
            ))
            # Fare & Status
            box.add_widget(MDLabel(
                text=f"💰 Fare: ₹{ride['fare']} | Status: {ride['status']}",
                theme_text_color="Hint"
            ))

            ride_card.add_widget(box)
            self.ids.rides_list.add_widget(ride_card)
