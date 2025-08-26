from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from models.vehicle_models import get_all_vehicles, update_vehicle_details
from bson import ObjectId

class VehicleListItem(BoxLayout):
    vehicle_id = StringProperty()
    driver_id = StringProperty()
    brand = StringProperty()
    model = StringProperty()
    year = StringProperty()
    plate = StringProperty()
    color = StringProperty()
    
    screen = None  # reference to parent screen

    def open_update_form(self):
        # populate update form in the parent screen
        if self.screen:
            self.screen.vehicle_id = self.vehicle_id
            self.screen.show_update_form = True
            self.screen.ids.brand_input.text = self.brand
            self.screen.ids.model_input.text = self.model
            self.screen.ids.year_input.text = self.year
            self.screen.ids.plate_input.text = self.plate
            self.screen.ids.color_input.text = self.color

class ViewUpdateVehicleScreen(Screen):
    vehicle_id = None
    show_update_form = BooleanProperty(False)

    def on_pre_enter(self):
        self.load_vehicles()

    def load_vehicles(self):
        user = self.manager.user  # logged-in user
        vehicles = get_all_vehicles()
        driver_vehicles = [v for v in vehicles if v['driver_id'] == str(user['_id'])]

        self.ids.vehicle_list.data = [{
            "vehicle_id": str(v["_id"]),
            "driver_id": str(v.get("driver_id", "")),
            "brand": v.get("brand", ""),
            "model": v.get("model", ""),
            "year": str(v.get("year", "")),
            "plate": v.get("plate", ""),
            "color": v.get("color", ""),
            "screen": self
        } for v in driver_vehicles]

    def update_vehicle(self):
        if not self.vehicle_id:
            self.show_popup("Error", "Select a vehicle first!")
            return

        brand = self.ids.brand_input.text.strip()
        model = self.ids.model_input.text.strip()
        year = self.ids.year_input.text.strip()
        plate = self.ids.plate_input.text.strip()
        color = self.ids.color_input.text.strip()

        if not all([brand, model, year, plate, color]):
            self.show_popup("Error", "All fields are required!")
            return

        if not year.isdigit() or len(year) != 4:
            self.show_popup("Error", "Year must be 4-digit!")
            return

        data = {
            "brand": brand,
            "model": model,
            "year": int(year),
            "plate": plate,
            "color": color
        }

        try:
            update_vehicle_details(self.vehicle_id, data)
            self.show_popup("Success", "Vehicle updated!")
            self.show_update_form = False
            self.load_vehicles()
        except Exception as e:
            self.show_popup("Error", f"Failed: {str(e)}")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(0.6, 0.4))
        popup.open()
