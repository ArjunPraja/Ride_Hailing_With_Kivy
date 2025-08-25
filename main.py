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
        return Builder.load_file("app.kv")

if __name__ == "__main__":
    RideHailingApp().run()
