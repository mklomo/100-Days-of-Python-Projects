import requests
import os
from dotenv import load_dotenv

load_dotenv()


class CustomerAcquisition:

    _USERS_API = os.getenv("YOUR_SHEETY_USERS_GET_API")
    _USERS_POST_API = os.getenv("YOUR_SHEETY_USERS_POST_API")
    _USERS_AUTH = os.getenv("YOUR_SHEETY_AUTH")

    def __init__(self):
        self._get_api = CustomerAcquisition._USERS_API
        self._post_api = CustomerAcquisition._USERS_POST_API
        self._auth = {
            "Authorization": CustomerAcquisition._USERS_AUTH
        }
        self._firstname = None
        self._lastname = None
        self._email = None
        self._response = None

    def get_list(self):
        self._response = requests.get(url=self._get_api, headers=self._auth)
        self._response.raise_for_status()
        return self._response.json()["users"]

    def update_list(self, firstname, lastname, email):
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        parameters = {
            "user": {
                "firstName": self._firstname.title(),
                "lastName": self._lastname.title(),
                "email": self._email
            }
        }
        self._response = requests.post(url=self._post_api, headers=self._auth, json=parameters)
        self._response.raise_for_status()
        print("Welcome to the Club")

    def get_email_list(self):
        email_list = []
        body_list = self.get_list()
        for row in body_list:
            email_list.append(row["email"])
        return email_list
