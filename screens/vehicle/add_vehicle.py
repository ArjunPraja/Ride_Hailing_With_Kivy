from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.vehicle_models import insert_vehicle
from datetime import datetime


class AddVehicleScreen(Screen):
    def add_vehicle(self):
        user = self.manager.user  # Assuming logged-in user info is here

        # Get input values
        brand = self.ids.brand_input.text.strip()
        model = self.ids.model_input.text.strip()
        year = self.ids.year_input.text.strip()
        plate = self.ids.plate_input.text.strip()
        color = self.ids.color_input.text.strip()

        # Basic validation
        if not all([brand, model, year, plate, color]):
            self.show_popup("Error", "All fields are required!")
            return

        if not year.isdigit() or len(year) != 4:
            self.show_popup("Error", "Year must be a 4-digit number!")
            return

        # Prepare vehicle data with timestamps
        now = datetime.now()
        vehicle_data = {
            "driver_id": str(user["_id"]),
            "brand": brand,
            "model": model,
            "year": int(year),
            "plate": plate,
            "color": color,
            "created_at": now,
            "updated_at": now
        }

        # Insert vehicle
        success = insert_vehicle(vehicle_data)
        if success:
            self.show_popup("Success", "Vehicle added successfully!")
            self.clear_inputs()
        else:
            self.show_popup("Error", "Failed to add vehicle!")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(0.6, 0.4))
        popup.open()

    def clear_inputs(self):
        self.ids.brand_input.text = ""
        self.ids.model_input.text = ""
        self.ids.year_input.text = ""
        self.ids.plate_input.text = ""
        self.ids.color_input.text = ""
