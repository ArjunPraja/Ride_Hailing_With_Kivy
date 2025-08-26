from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from models.rides_models import get_rides_by_user


class ViewMyAllRidesScreen(MDScreen):
    def on_pre_enter(self):
        """Automatically load rides when this screen is opened."""
        self.load_rides()

    def load_rides(self):
        user = self.manager.user  # ✅ Logged-in user stored in App manager
        user_id = str(user["_id"])
        role = user.get("role", "passenger")

        # Clear old items
        self.ids.rides_list.clear_widgets()

        rides = get_rides_by_user(user_id, role)

        if not rides:
            self.ids.rides_list.add_widget(
                OneLineListItem(text="No rides found.")
            )
            return

        # Loop rides and create card-like table rows
        for ride in rides:
            ride_card = MDCard(
                orientation="vertical",
                size_hint=(1, None),
                height="120dp",
                padding="10dp",
                radius=[15, 15, 15, 15],
                md_bg_color=(0.95, 0.95, 0.95, 1),  # light grey
                elevation=4,              # 👈 for shadow
                ripple_behavior=True  
            )

            box = MDBoxLayout(orientation="vertical", spacing="5dp")

            box.add_widget(MDLabel(
                text=f"🆔 Ride ID: {ride['_id']}",
                theme_text_color="Primary",
                bold=True
            ))
            box.add_widget(MDLabel(
                text=f"📍 {ride['pickup']} ➝ {ride['drop_location']}",
                theme_text_color="Secondary"
            ))
            box.add_widget(MDLabel(
                text=f"💰 Fare: ₹{ride['fare']} | Status: {ride['status']}",
                theme_text_color="Hint"
            ))

            ride_card.add_widget(box)
            self.ids.rides_list.add_widget(ride_card)
