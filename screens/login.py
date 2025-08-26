from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from models.users_models import find_by_email

# Replace with your email and app password
SENDER_EMAIL = ""
APP_PASSWORD = " "

# Temporary OTP storage: {email: {"otp": "123456", "expires": datetime}}
otp_storage = {}

def generate_otp(length=6):
    """Generate numeric OTP"""
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def send_email_otp(receiver_email, otp):
    """Send OTP via Gmail SMTP"""
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = "Your OTP Code"

    msg.attach(MIMEText(f"Your OTP is: {otp}", 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()

class LoginScreen(Screen):

    def do_login(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        if not email:
            self.show_popup("Enter your email!")
            return

        user = find_by_email(email)
        if not user:
            self.show_popup("⚠️ Email not found! Please register first.")
            return

        # Password login
        if password:
            if user["password"] == password:
                self.complete_login(user)
            else:
                self.show_popup(" Incorrect password! Or use OTP login.")
        else:
            self.show_popup("Enter password or use OTP login.")

    def send_otp(self):
        """Generate and send OTP to email"""
        email = self.ids.email.text.strip()
        if not email:
            self.show_popup("Enter your email first!")
            return

        user = find_by_email(email)
        if not user:
            self.show_popup("⚠️ Email not found! Please register first.")
            return

        otp = generate_otp()
        # Set OTP to expire in 5 minutes
        otp_storage[email] = {"otp": otp, "expires": datetime.now() + timedelta(minutes=5)}
        send_email_otp(email, otp)
        self.show_popup(f"✅ OTP sent to {email}. It expires in 5 minutes.")

    def verify_otp(self, otp_input):
        """Verify OTP input by user"""
        email = self.ids.email.text.strip()
        if not email:
            self.show_popup("Enter your email first!")
            return

        record = otp_storage.get(email)
        if not record:
            self.show_popup(" No OTP sent. Click 'Send OTP' first.")
            return

        if datetime.now() > record["expires"]:
            del otp_storage[email]
            self.show_popup(" OTP expired! Please request a new one.")
            return

        if otp_input == record["otp"]:
            user = find_by_email(email)
            self.complete_login(user)
            del otp_storage[email]  
        else:
            self.show_popup(" Invalid OTP!")

    def complete_login(self, user):
        """Complete login and switch screens based on role"""
        if user["role"] == "Rider":
            self.manager.current = "user_menu"
        elif user["role"] == "Driver":
            self.manager.current = "driver_menu"

        self.manager.user = user
        self.ids.email.text = ""
        self.ids.password.text = ""
        if hasattr(self.ids, "otp_input"):
            self.ids.otp_input.text = ""
        self.show_popup(f"Welcome {user['full_name']}!")

    def show_popup(self, message):
        """Utility function to show popup messages"""
        popup = Popup(
            title='Login Info',
            content=Label(text=message),
            size_hint=(None, None),
            size=(320, 200)
        )
        popup.open()
