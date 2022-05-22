from twilio.rest import Client
import os
from dotenv import load_dotenv


# Access your environment variables
load_dotenv()

class NotificationManager:
    _TWILIO_SID = os.getenv("YOUR_TWILIO_SID")
    _TWILIO_AUTH = os.getenv("YOUR_TWILIO_AUTH")
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self._sid = NotificationManager._TWILIO_SID
        self._auth = NotificationManager._TWILIO_AUTH
        self._from = '+17205711913'
        self._to = os.getenv("YOUR_TWILIO_VERIFIED_NUMBER")

    def send_message(self, text: str):
        client = Client(self._sid, self._auth)
        message = client.messages.create(body=text, from_=self._from, to=self._to)
        print(message.status)

