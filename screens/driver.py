from kivymd.uix.screen import MDScreen

class DriverMenuScreen(MDScreen):
    def view_ride_requests(self):
        print("View Ride Requests clicked")

    def view_my_rides(self):
        print("View My Rides clicked")

    def view_ride_by_id(self):
        print("View Ride by ID clicked")

    def accept_ride(self):
        print("Accept Ride clicked")

    def start_ride(self):
        print("Start Ride clicked")

    def add_vehicle(self):
        print("Add Vehicle clicked")

    def view_my_vehicles(self):
        print("View My Vehicles clicked")

    def update_vehicle(self):
        print("Update Vehicle clicked")

    def view_profile(self):
        print("View Profile clicked")

    def logout(self):
        print("Logout clicked")
