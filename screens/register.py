from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.users_models import insert_users, find_by_email
import re

class RegisterScreen(Screen):

    def register_user(self, full_name, email, phone, password, verify_password, role):
        
        if not all([full_name, email, phone, password, verify_password, role != "None"]):
            self.show_popup("All fields are required!")
            return

        if password != verify_password:
            self.show_popup("Passwords do not match!")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_popup("Invalid email format!")
            return

        if find_by_email(email):
            self.show_popup("Email already registered!")
            return

       
        user_data = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "password": password,  
            "role": role
        }
        insert_users(user_data)
        self.show_popup("Registration Successful!")
       
        self.ids.full_name.text = ""
        self.ids.email.text = ""
        self.ids.phone.text = ""
        self.ids.password.text = ""
        self.ids.verify_password.text = ""
        self.ids.role_label.text = "None"
        self.manager.current = "login"

    def show_popup(self, message):
        popup = Popup(
            title='Info',
            content=Label(text=message),
            size_hint=(None, None),
            size=(300, 200)
        )
        popup.open()
