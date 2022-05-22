# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from customer_acquisition import CustomerAcquisition
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os
from dotenv import load_dotenv
import smtplib
import ssl


# Access your environment variables
load_dotenv()


SHEETY_GET_API = os.getenv("YOUR_SHEETY_API")
SHEETY_API_HEADER = {
    "Authorization": os.getenv("YOUR_SHEETY_AUTH"),
}

SERVER = os.getenv("SMTP_SERVER")
PORT = os.getenv("SMTP_PORT")
MY_EMAIL = os.getenv("YOUR_EMAIL")
PASSWORD = os.getenv("YOUR_PASSWORD")


# Instantiate the Customer Acquisition Class
customer_acquisition = CustomerAcquisition()
# Customer Acquisition Code
print("Welcome to Marvin's Flight Club\n")

print("We find the Best Deals for you!\n")

first_name = input("What is your first name?\n")

print("\n")

last_name = input("What is your last name?\n")

print("\n")

email = input("What is you email?\n")

# Verify your mail
is_verified = True
while is_verified:
    email_verify = input("Please type your mail again?\n")
    if email_verify == email:
        # Post the details into the sheet
        customer_acquisition.update_list(firstname=first_name, lastname=last_name, email=email_verify)
        is_verified = False


# Make a request to the google data API
response_data = requests.get(url=SHEETY_GET_API, headers=SHEETY_API_HEADER)
# Raise exception if sth untoward happens
response_data.raise_for_status()
# Get the json data from the API response
flight_data_response = response_data.json()
# Initialize the class with the flight_data_response
flight_location_data_manager = DataManager(flight_details_dict=flight_data_response)

# City name variable
city_name = ""

# Now lets update the Google sheet with our IATA Codes
for entry_row_number in range(2, (len(flight_location_data_manager.get_price_list()) + 2)):
    # Get the city name
    city_name = flight_location_data_manager.get_city_name(row_number=entry_row_number)
    # city_iata_code = FlightData()
    # city_code = city_iata_code.get_iata_code(location=city_name).upper()
    location_iata_code = flight_location_data_manager.get_city_code(row_number=entry_row_number)
    flight_deal_search = FlightSearch(fly_to=location_iata_code)
    flight_deal_price = flight_deal_search.get_cheapest_flight()
    # print(f"ROUTE: ACC-{location_iata_code} LOWEST OFFER: {flight_price}")
    # if flight_deal_price <= expected_price_from_GS:
    expected_price = flight_location_data_manager.get_price_for_code(row_number=entry_row_number)
    # If no cheap flight exists
    if flight_deal_price is None:
        continue
    elif flight_deal_price <= expected_price:
        # Send a message to my number
        msg = flight_deal_search.text_message()
        notif_mgr = NotificationManager()
        notif_mgr.send_message(text=msg)
        # Then send an email to the club
        email_list = customer_acquisition.get_email_list()
        with smtplib.SMTP(SERVER, PORT) as new_connection:
            # Start a secure transport layer security
            context = ssl.create_default_context()
            new_connection.starttls(context=context)
            # Login to the email
            new_connection.login(user=MY_EMAIL, password=PASSWORD)
            for fc_email in range(len(email_list)):
                SUBJECT_LINE = f"Subject:New Low Price Flight"
                email_content = f"{SUBJECT_LINE}\n\n{msg}\n\n"
                new_connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=email_list[fc_email],
                                        msg=email_content)
