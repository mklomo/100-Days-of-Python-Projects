import os
import requests
from dotenv import load_dotenv


# Access your environment variables
load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, flight_details_dict: dict):
        self._flight_details_dict = flight_details_dict
        self._sheety_api = os.getenv("YOUR_SHEETY_API")
        self._response = None
        self._headers = {
        "Authorization": os.getenv("YOUR_SHEETY_AUTH"),
    }

    def get_price_list(self):
        return self._flight_details_dict["prices"]

    def get_city_name(self, row_number: int):
        sheety_get_city_api = f"{self._sheety_api}/{row_number}"
        self._response = requests.get(url=sheety_get_city_api, headers=self._headers)
        self._response.raise_for_status()
        return self._response.json()['price']["city"]

    def get_city_code(self, row_number: int):
        sheety_get_city_api = f"{self._sheety_api}/{row_number}"
        self._response = requests.get(url=sheety_get_city_api, headers=self._headers)
        self._response.raise_for_status()
        return self._response.json()['price']["iataCode"]

    def get_price_for_code(self, row_number: int):
        sheety_get_city_api = f"{self._sheety_api}/{row_number}"
        self._response = requests.get(url=sheety_get_city_api, headers=self._headers)
        self._response.raise_for_status()
        return self._response.json()['price']["lowestPrice"]

    def iata_code_row_update(self, row_number: int, iata_code_dict: dict):
        sheety_put_api = f"{self._sheety_api}/{row_number}"
        self._response = requests.put(url=sheety_put_api, headers=self._headers, json=iata_code_dict)
        self._response.raise_for_status()
