from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from models.rides_models import update_cancel_rider
class UserMenuScreen(MDScreen):
    def request_ride(self):
        print("🚖 User requested a ride")

    def view_ride_by_id(self):
        print("🔎 Viewing ride by ID")

    def view_my_rides(self):
        print("📜 Viewing all my rides")

    def complete_ride(self):
        print("✅ Completing a ride")

    def show_popup(self, message, title="Ride Status"):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, halign="center")
        btn = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(btn)

        popup = Popup(title=title,
                      content=layout,
                      size_hint=(0.7, 0.4),
                      auto_dismiss=False)
        btn.bind(on_release=popup.dismiss)
        popup.open()


    def view_profile(self):
        print("👤 Viewing profile")

    def logout(self):
        print("👋 User logged out")
        self.manager.user =None
        self.manager.current = "login"
