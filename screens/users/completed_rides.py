from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

from models.rides_models import get_rides_by_status
from models.rating_models import get_rating_by_ride, insert_rating, update_rating


class CompletedRidesScreen(MDScreen):

    def on_pre_enter(self):
        self.load_rides()

    def load_rides(self):
        self.ids.rides_list.clear_widgets()
        user = getattr(self.manager, "user", None)
        if not user:
            toast("User not found!")
            return

        rides = get_rides_by_status(str(user["_id"]), "Completed")
        if not rides:
            from kivymd.uix.list import OneLineListItem
            self.ids.rides_list.add_widget(OneLineListItem(text="No rides found."))
            return

        for ride in rides:
            card = MDCard(
                orientation="vertical",
                size_hint=(1, None),
                height="150dp",
                padding="10dp",
                radius=[12],
                md_bg_color=(0.95, 0.95, 0.95, 1),
                elevation=4
            )
            box = MDBoxLayout(orientation="vertical", spacing="4dp")

            # Ride info
            box.add_widget(MDLabel(text=f"🆔 Ride ID: {str(ride['_id'])}", bold=True))
            box.add_widget(MDLabel(text=f"📍 {ride['pickup']} ➝ {ride['drop_location']}"))
            box.add_widget(MDLabel(text=f"💰 Fare: ₹{ride.get('fare', 'N/A')} | Status: {ride['status']}"))

            # Check existing rating
            existing_rating = get_rating_by_ride(str(ride["_id"]))
            if existing_rating:
                box.add_widget(MDLabel(
                    text=f"⭐ Rating: {existing_rating['rating']} | Feedback: {existing_rating.get('feedback', '')}"
                ))
            else:
                rate_btn = MDRaisedButton(
                    text="Rate Ride",
                    md_bg_color=(0, 0.5, 1, 1),
                    size_hint_y=None,
                    height="35dp",
                    on_release=lambda btn, r=ride: self.open_rating_popup(r)
                )
                box.add_widget(rate_btn)

            card.add_widget(box)
            self.ids.rides_list.add_widget(card)

    def open_rating_popup(self, ride):
        user = self.manager.user
        rider_id = str(user["_id"])
        driver_id = str(ride["driver_id"])
        ride_id = str(ride["_id"])

        # Text fields with proper heights
        rating_input = MDTextField(
            hint_text="Rating (0-5)",
            input_filter="int",
            max_text_length=1,
            size_hint_y=None,
            height="50dp"
        )
        feedback_input = MDTextField(
            hint_text="Optional feedback",
            multiline=True,
            size_hint_y=None,
            height="100dp"
        )

        # Container for fields with spacing
        content = MDBoxLayout(
            orientation="vertical",
            spacing="15dp",
            padding="10dp",
            size_hint_y=None
        )
        content.height = rating_input.height + feedback_input.height + 50  # extra padding
        content.add_widget(rating_input)
        content.add_widget(feedback_input)

        def submit_rating(*args):
            try:
                rating_val = int(rating_input.text)
                feedback_val = feedback_input.text
                if get_rating_by_ride(ride_id):
                    update_rating(ride_id, rating_val, feedback_val)
                    toast("Rating updated successfully!")
                else:
                    insert_rating(ride_id, rider_id, driver_id, rating_val, feedback_val)
                    toast("Rating submitted successfully!")
                dialog.dismiss()
                self.load_rides()
            except Exception as e:
                toast(f"Error: {str(e)}")

        dialog = MDDialog(
            title=f"Rate Ride {ride_id}",
            type="custom",
            content_cls=content,
            size_hint=(0.9, None),
            height="250dp",  # Set fixed height to prevent overlap
            buttons=[
                MDRaisedButton(text="Submit", on_release=submit_rating),
                MDRaisedButton(text="Cancel", on_release=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()
