from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

# Import all screens
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.home import HomeScreen
from screens.user import UserMenuScreen
from screens.driver import DriverMenuScreen


# ScreenManager to handle screen transitions
class WindowManager(ScreenManager):
    pass


class RideHailingApp(MDApp):
    def build(self):
        # Set app theme
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"

        # Load KV files
        Builder.load_file("kv/home.kv")
        Builder.load_file("kv/login_screen.kv")
        Builder.load_file("kv/register_screen.kv")
        Builder.load_file("kv/user_menu_screen.kv")
        Builder.load_file("kv/driver_menu_screen.kv")

        # Create screen manager
        sm = WindowManager()

        # Add screens with unique names
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(UserMenuScreen(name="user_menu"))
        sm.add_widget(DriverMenuScreen(name="driver_menu"))

        return sm


if __name__ == "__main__":
    RideHailingApp().run()
