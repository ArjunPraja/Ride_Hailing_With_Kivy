import random
from kivymd.uix.screen import MDScreen
from models.rides_models import insert_ride
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class RequestRideScreen(MDScreen):

    def request_ride(self):
        # ✅ get the logged-in user from manager
        user = self.manager.user  

        pickup = self.ids.pickup_input.text.strip()
        drop_location = self.ids.drop_input.text.strip()

        if not pickup or not drop_location:
            self.show_popup(f"⚠ Please fill in both pickup and drop location")
            
        else:

    
            fare = random.randint(100, 500)

        
            ride_data = {
                "rider_id": str(user["_id"]),   
                "driver_id": None,             
                "pickup": pickup,
                "drop_location": drop_location,
                "status": "Requested",
                "fare": fare
            }

        
            result = insert_ride(ride_data)
            self.show_popup(f"✅ Ride Requested. ID: {result.inserted_id}")

        
            self.ids.pickup_input.text = ""
            self.ids.drop_input.text = ""

            self.manager.current = "user_menu"
    
    def show_popup(self, message):
        popup = Popup(
            title='Login Info',
            content=Label(text=message),
            size_hint=(None, None),
            size=(320, 200)
        )
        popup.open()