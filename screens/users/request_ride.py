import random
from kivymd.uix.screen import MDScreen
from models.rides_models import insert_ride


class RequestRideScreen(MDScreen):

    def request_ride(self):
        # ✅ get the logged-in user from manager
        user = self.manager.user  

        pickup = self.ids.pickup_input.text.strip()
        drop_location = self.ids.drop_input.text.strip()

        if not pickup or not drop_location:
            print("⚠ Please fill in both pickup and drop location")
            return

  
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
        print(f"✅ Ride Requested. ID: {result.inserted_id}")

      
        self.ids.pickup_input.text = ""
        self.ids.drop_input.text = ""

        self.manager.current = "user_menu"
