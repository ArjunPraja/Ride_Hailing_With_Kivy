from kivy.uix.screenmanager import Screen
from screens.register import users_db  # Import the user storage

class LoginScreen(Screen):
    def do_login(self):
        email = self.ids.email.text
        password = self.ids.password.text

        # Check if user exists in registered users
        if email in users_db and users_db[email]["password"] == password:
            self.manager.current = "home"  # Go to Home screen
        else:
            print("Invalid credentials")
