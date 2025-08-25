from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.home import HomeScreen

class WindowManager(ScreenManager):
    pass

class RideHailingApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"

        # Load KV files dynamically
        Builder.load_file("kv/home.kv")
        Builder.load_file("kv/login_screen.kv")
        Builder.load_file("kv/register_screen.kv")

        # Add screens
        sm = WindowManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))

        return sm

if __name__ == "__main__":
    RideHailingApp().run()
