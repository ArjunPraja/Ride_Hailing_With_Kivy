from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.users_models import find_by_email

class LoginScreen(Screen):

    def do_login(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        user = find_by_email(email)

        if user:
            # Simple string password check (since no hashing yet)
            if user["password"] == password:
                if user["role"] == "Rider":
                    self.show_popup(f"Welcome {user['full_name']}! (Rider)")
                    self.manager.current = "user_menu"

                elif user["role"] == "Driver":
                    self.show_popup(f"Welcome {user['full_name']}! (Driver)")
                    self.manager.current = "driver_menu"

                # ✅ Save logged-in user globally (for profile, rides, etc.)
                self.manager.current_screen.user = user  

                # Clear fields
                self.ids.email.text = ""
                self.ids.password.text = ""

            else:
                self.show_popup("❌ Incorrect password!")
        else:
            self.show_popup("⚠️ Email not found! Please register first.")

        return user

    def show_popup(self, message):
        popup = Popup(
            title='Login Info',
            content=Label(text=message),
            size_hint=(None, None),
            size=(320, 200)
        )
        popup.open()
