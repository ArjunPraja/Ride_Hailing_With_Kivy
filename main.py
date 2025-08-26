from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

# Import all screens
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.home import HomeScreen
from screens.user import UserMenuScreen
from screens.driver import DriverMenuScreen
from screens.users.request_ride import RequestRideScreen
from screens.users.view_ride_by_id import ViewRideByIdScreen
from screens.users.view_my_all_rides import ViewMyAllRidesScreen
from screens.users.completed_rides import CompletedRidesScreen
from screens.users.profile import RiderProfileScreen
from screens.vehicle.add_vehicle import AddVehicleScreen
from screens.vehicle.view_update_vehicle import ViewUpdateVehicleScreen
from screens.vehicle.driver_profile import DriverProfileScreen
from screens.vehicle.ride_request_accept import ShowRidesScreen
from screens.vehicle.show_my_accepted_rides import MyAcceptedRidesScreen
# ScreenManager to handle screen transitions
class WindowManager(ScreenManager):
    user = None 
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


        # Users Operations
        Builder.load_file("kv/users/request_ride_screen.kv")
        Builder.load_file("kv/users/view_ride_by_id_screen.kv")
        Builder.load_file("kv/users/view_my_all_rides_screen.kv")
        Builder.load_file("kv/users/completed_rides_screen.kv")
        Builder.load_file("kv/users/rider_profile_screen.kv")

        # Driver Operations
        Builder.load_file("kv/driver/add_vehicle_screen.kv")
        Builder.load_file("kv/driver/view_update_vehicle_screen.kv")
        Builder.load_file("kv/driver/driver_profile_screen.kv")
        Builder.load_file("kv/driver/requested_rides_accept_screen.kv")
        Builder.load_file("kv/driver/my_accepted_rides_screen.kv")

        



        # Create screen manager
        sm = WindowManager()

        # Add screens with unique names
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(UserMenuScreen(name="user_menu"))
        sm.add_widget(DriverMenuScreen(name="driver_menu"))
        sm.add_widget(RequestRideScreen(name="request_ride"))
        sm.add_widget(ViewRideByIdScreen(name="view_ride_by_id"))
        sm.add_widget(ViewMyAllRidesScreen(name="view_my_all_rides"))
        sm.add_widget(RiderProfileScreen(name="rider_profile"))
        sm.add_widget(CompletedRidesScreen(name="completed_user_rides"))    
        sm.add_widget(ViewUpdateVehicleScreen(name="view_update_vehicle"))
        sm.add_widget(DriverProfileScreen(name="driver_profile"))
        sm.add_widget(ShowRidesScreen(name="show_rides"))
        sm.add_widget(MyAcceptedRidesScreen(name="my_accepted_rides"))


        # Driver 
        sm.add_widget(AddVehicleScreen(name="add_vehicle"))


        return sm


if __name__ == "__main__":
    RideHailingApp().run()
