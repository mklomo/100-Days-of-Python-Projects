# Get the city code from the response body
import requests
import os
from dotenv import load_dotenv


# Access your environment variables
load_dotenv()

class FlightData:
    def __init__(self):
        self._kiwi_server = os.getenv("YOUR_KIWI_SERVER")
        self._kiwi_auth = {"apikey": os.getenv("YOUR_KIWI_AUTH")}

    def get_server(self):
        return self._kiwi_server

    def get_auth(self):
        return self._kiwi_auth

    def get_iata_code(self, location: str):
        location_api_meta = "locations/query"
        location_api = f"{self._kiwi_server}/{location_api_meta}"
        parameters = {
            "term": location,
        }
        # Since the API did not specify a json packet, please use the params parameter NOT json
        location_api_response = requests.get(url=location_api, headers=self._kiwi_auth, params=parameters)
        # If anything untoward happens, raise an Exception
        location_api_response.raise_for_status()
        iata_code = location_api_response.json()['locations'][0]['code']
        return iata_code

