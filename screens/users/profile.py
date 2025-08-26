from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.filemanager import MDFileManager
import os

class RiderProfileScreen(Screen):
    profile_image = StringProperty("assets/OIP.jpg")
    user_name = StringProperty("")
    user_email = StringProperty("")
    user_phone = StringProperty("")

    file_manager = None

    def on_pre_enter(self, *args):
        user = getattr(self.manager, "user", None)
        if user:
            self.user_name = user.get("full_name", "Unknown")
            self.user_email = user.get("email", "unknown@example.com")
            self.user_phone = user.get("phone", "N/A")
            self.profile_image = user.get("profile_image", self.profile_image)

    def select_image(self):
        if not self.file_manager:
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager,
                select_path=self.select_path,
                preview=True
            )
        self.file_manager.show(os.path.expanduser("~"))

    def exit_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        self.profile_image = path
        user = getattr(self.manager, "user", None)
        if user:
            user["profile_image"] = path
        self.exit_manager()
