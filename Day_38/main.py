"""
Attribution to Nutritionix:https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit
#heading=h.3grsso1wll94 """
import datetime as dt
import json
import os

import requests

# Convert date time to string format
DATE_RECORD = dt.datetime.today().date().strftime("%d/%m/%Y")
TIME_RECORD = dt.datetime.today().time().strftime("%H:%M:%S")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRIONIX_HEADER = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"

}
SHEETY_API_END = os.getenv("SHEETY_API_END_POINT")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SHEETY_HEADER = {
    "Authorization": SHEETY_AUTH,
}

# Exercise Parameters
gender_input = input("Gender: (male / female) ")
querry_input = input("Please detail exercise routine: ")
weight_input = input("Please indicate your current body weight: ")
height_input = input("Please indicate your height:")
age_input = input("Please indicate your age: ")

exercise_parameters = {
    "query": querry_input,
    "gender": gender_input,
    "weight_kg": weight_input,
    "height_cm": height_input,
    "age": age_input,
}
# Making a post request
nutritionix_response_data = requests.post(url=NUTRITIONIX_ENDPOINT, headers=NUTRIONIX_HEADER, json=exercise_parameters)
# Raise an exception when sth is wrong
nutritionix_response_data.raise_for_status()
# Save and filter the response for Exercise, Duration and Calories
exercise_response_data_list = nutritionix_response_data.json()["exercises"]
# Take a look at the data
# with open("exercise_data.json", mode="w") as output_data:
#     json.dump(nutritionix_response_data.json(), output_data, indent=4)

for entry in range(len(exercise_response_data_list)):
    duration = exercise_response_data_list[entry]["duration_min"]
    exercise = exercise_response_data_list[entry]["name"]
    calories = exercise_response_data_list[entry]["nf_calories"]
    print(duration, exercise, calories)
    # Update the Parameters
    sheety_parameters = {
        "workout": {
            "date": DATE_RECORD,
            "time": TIME_RECORD,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    sheety_update_response = requests.post(url=SHEETY_API_END, json=sheety_parameters, headers=SHEETY_HEADER)
    # raise exception when sth happens
    sheety_update_response.raise_for_status()
    print(sheety_update_response.text)
