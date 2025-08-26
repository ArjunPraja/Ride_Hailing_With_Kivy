from kivymd.uix.screen import MDScreen

class UserMenuScreen(MDScreen):
    def request_ride(self):
        print("🚖 User requested a ride")

    def view_ride_by_id(self):
        print("🔎 Viewing ride by ID")

    def view_my_rides(self):
        print("📜 Viewing all my rides")

    def complete_ride(self):
        print("✅ Completing a ride")

    def cancel_ride(self):
        print("❌ Cancelling a ride")

    def view_profile(self):
        print("👤 Viewing profile")

    def logout(self):
        print("👋 User logged out")
        self.manager.current = "login"
