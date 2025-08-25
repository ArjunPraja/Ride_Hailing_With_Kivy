from kivy.uix.screenmanager import Screen

users_db = {}

class RegisterScreen(Screen):
    def do_register(self):
        name = self.ids.fullname.text
        email = self.ids.email.text
        password = self.ids.password.text

        if not name or not email or not password:
            print("Please fill all fields")
            return

        users_db[email] = {"name": name, "password": password}
        print(f"Registered: {email}")

        self.manager.current = "login"
