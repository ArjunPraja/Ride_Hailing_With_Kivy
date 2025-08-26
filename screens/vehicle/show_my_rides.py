from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from models.rides_models import show_driver_all_rides

class DriverRidesScreen(Screen):
    rides_container = ObjectProperty(None)

    def on_pre_enter(self):
        """Called before entering the screen to load driver rides"""
        self.load_driver_rides()

    def load_driver_rides(self):
        self.rides_container.clear_widgets()

        # Get current driver id
        user = self.manager.user
        driver_id = str(user["_id"])  # Assuming user has _id

        # Fetch rides
        rides = show_driver_all_rides(driver_id)

        if not rides:
            from kivymd.uix.label import MDLabel
            self.rides_container.add_widget(
                MDLabel(text="No rides found.", halign="center")
            )
            return

        from kivymd.uix.card import MDCard
        from kivymd.uix.label import MDLabel
        from kivy.uix.boxlayout import BoxLayout

        for ride in rides:
            card = MDCard(
                orientation="vertical",
                padding=15,
                size_hint=(0.9, None),
                height="160dp",
                elevation=3,
                md_bg_color=(0.95, 0.95, 0.95, 1)
            )

            info_layout = BoxLayout(orientation="vertical", spacing=5)
            info_layout.add_widget(MDLabel(text=f"🆔 Rider: {ride.get('rider_id','-')}", theme_text_color="Primary"))
            info_layout.add_widget(MDLabel(text=f"📍 Pickup: {ride.get('pickup','-')}", theme_text_color="Primary"))
            info_layout.add_widget(MDLabel(text=f"🏁 Drop: {ride.get('drop_location','-')}", theme_text_color="Primary"))
            info_layout.add_widget(MDLabel(text=f"💰 Fare: ₹{ride.get('fare','-')}", theme_text_color="Primary"))
            info_layout.add_widget(MDLabel(text=f"📌 Status: {ride.get('status','-')}", theme_text_color="Secondary"))

            card.add_widget(info_layout)
            self.rides_container.add_widget(card)
