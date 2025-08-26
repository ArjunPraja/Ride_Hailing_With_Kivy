from kivymd.uix.screen import MDScreen
from models.rides_models import get_ride_by_id
from bson import ObjectId
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class ViewRideByIdScreen(MDScreen):

    def view_ride(self):
        ride_id = self.ids.ride_id_input.text.strip()

        if not ride_id:
            self.show_popup(f"⚠ Please Enter Ride ID Bro")
            
        else:
            try:
                ride = get_ride_by_id(ObjectId(ride_id))
            except Exception:
                self.show_message("❌ Invalid Ride ID")
                return

            if not ride:
                self.show_message("❌ No Ride Found with this ID")
                return

            # Clear old details
            self.ids.ride_details_box.clear_widgets()

            # Show ride details in "table-like" format
            for key, value in ride.items():
                self.ids.ride_details_box.add_widget(
                    self.make_row(str(key), str(value))
                )

    def make_row(self, key, value):
        from kivymd.uix.boxlayout import MDBoxLayout
        from kivymd.uix.label import MDLabel

        row = MDBoxLayout(orientation="horizontal", spacing="10dp", size_hint_y=None, height="40dp")
        row.add_widget(MDLabel(text=f"{key}:", bold=True, size_hint_x=0.4))
        row.add_widget(MDLabel(text=value, size_hint_x=0.6))
        return row

    def show_message(self, message):
        from kivymd.uix.snackbar import Snackbar
        Snackbar(text=message).open()
    
    def show_popup(self, message):
        popup = Popup(
            title='Login Info',
            content=Label(text=message),
            size_hint=(None, None),
            size=(320, 200)
        )
        popup.open()