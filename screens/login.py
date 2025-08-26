from kivy.uix.screenmanager import Screen
from models.users_models import find_by_email
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class LoginScreen(Screen):

    def do_login(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        user = find_by_email(email)

        if user: 
            if user["password"] == password:
                if user["role"] == "Rider":
                    self.show_popup("User Login Successful")
                    self.manager.current = "Home"

                elif user["role"] == "Driver":
                    self.show_popup("Driver Login Successful")
                    self.manager.current = "rider"

                
                self.ids.email.text = ""
                self.ids.password.text = ""

            else:
                self.show_popup("Incorrect password!")  
        else:
            self.show_popup("Email not found! Please register first.") 
        return user

    def show_popup(self, message):
        popup = Popup(
            title='Login Info',
            content=Label(text=message),
            size_hint=(None, None),
            size=(300, 200)
        )
        popup.open()
