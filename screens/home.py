from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def book_ride(self):
        print("Booking a ride... 🚖")
        # Add booking logic here, e.g., navigate to BookingScreen
        # self.manager.current = "booking"
