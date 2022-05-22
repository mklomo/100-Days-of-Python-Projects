import requests
import json
# SHEETY_GET_API = f"https://api.sheety.co/0bb595b53c0dadef3c73ee17535e78e0/flightDetails/prices/"
SHEETY_API_HEADER = {
     "Authorization": "Bearer marvins_flight_details",
 }
#
# response_data = requests.get(url=SHEETY_GET_API, headers=SHEETY_API_HEADER)
# response_data.raise_for_status()
# with open(file="flight_data.json", mode="w") as outfile:
#     json.dump(response_data.json(), outfile, indent=4)
#
# sheety_get_city_api = f"https://api.sheety.co/0bb595b53c0dadef3c73ee17535e78e0/flightDetails/prices/2"
# response = requests.get(url=sheety_get_city_api, headers=SHEETY_API_HEADER)
# response.raise_for_status()
# print(response.json())


# kiwi_server = "https://tequila-api.kiwi.com/locations/query"
# kiwi_auth = {"apikey": "lGa3VRnuWruh6MQYo94nE5IK1G0sjinl"}
# parameters = {
#     "term": "Kuala Lumpur",
#     "location_types": "city"
# }
# kiwi_response = requests.get(url=kiwi_server, headers=kiwi_auth, json=parameters)
# kiwi_response.raise_for_status()
# print(kiwi_response.json())


