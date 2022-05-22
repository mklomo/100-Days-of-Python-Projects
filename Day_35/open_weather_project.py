import json
import os
from twilio.rest import Client
import requests


API_KEY = os.getenv("OWM_API_KEY")
MY_LAT = 5.613084
MY_LONG = -0.182318
URI = "https://api.openweathermap.org/data/2.5/onecall"
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(URI, params=parameters)
response.raise_for_status()
response_data = response.json()
# Save the data
with open("weather_data.json", mode="w") as output:
    json.dump(response_data, output, indent=4)
response_data_hour_list = response_data["hourly"]
# Slice the list to get the next 12 hours
response_data_work_hour_list = response_data_hour_list[:12]
#print(response_data_work_hour_list)

# Now for each work hour, select the weather data and create a list of the condition codes
weather_codes_list = [every_hour['weather'][0]['id'] for every_hour in response_data_work_hour_list]
print(weather_codes_list)


# Now if any of the weather codes < 700 please print rainy
def pick_umbrella(a_list: list) -> bool:
    for weather_code in a_list:
        if weather_code < 700:
            return True
    return False


message_alert = pick_umbrella(a_list=weather_codes_list)
print(message_alert)

# Sending and SMS alert with Twilio
if message_alert:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It might rain today. Remember to bring an umbrella ☔☔☔☔️!!!",
        from_='+17205711913',
        to='+233557299146'
    )

    print(message.status)