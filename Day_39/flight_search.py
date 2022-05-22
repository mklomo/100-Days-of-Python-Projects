import datetime as dt
import os
import requests
from dotenv import load_dotenv


# Access your environment variables
load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    _KIWI_SERVER = os.getenv("YOUR_KIWI_SERVER")
    _TODAY = dt.datetime.now().strftime("%d/%m/%Y")
    _MAX_DEPARTURE_DATE = (dt.datetime(year=2021, month=6, day=19) + dt.timedelta(days=529)).strftime("%d/%m/%Y")
    _NIGHTS_IN_DST_FROM = 21
    _NIGHTS_IN_DST_TO = 30
    _MAX_RETURN_DATE = (dt.datetime(year=2022, month=11, day=30) + dt.timedelta(days=30)).strftime("%d/%m/%Y")
    _KIWI_API_AUTH = {"apikey": os.getenv("YOUR_KIWI_AUTH")}
    _FLY_FROM = "ACC"

    def __init__(self, fly_to: str):
        self._server = FlightSearch._KIWI_SERVER
        self._auth = FlightSearch._KIWI_API_AUTH
        self._search_extension = "v2/search"
        self._date_from = FlightSearch._TODAY
        self._date_to = FlightSearch._MAX_DEPARTURE_DATE
        self._nights_in_dst_from = FlightSearch._NIGHTS_IN_DST_FROM
        self._nights_in_dst_to = FlightSearch._NIGHTS_IN_DST_TO
        self._fly_from = FlightSearch._FLY_FROM
        self._fly_to = fly_to
        self._price = None
        self._response = None
        self._response_data = None
        self._max_stopovers = 0
        self._cheap_flight_api = f"{self._server}/{self._search_extension}"
        self._via_city = ""

    def make_request(self):
        parameters = {
            "fly_from": self._fly_from,
            "fly_to": self._fly_to,
            "date_from": self._date_from,
            "date_to": self._date_to,
            "nights_in_dst_from": self._nights_in_dst_from,
            "nights_in_dst_to": self._nights_in_dst_to,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": self._max_stopovers,
        }
        self._response = requests.get(url=self._cheap_flight_api, params=parameters, headers=self._auth)
        self._response.raise_for_status()
        self._response_data = self._response.json()    
    
    def get_cheapest_flight(self):
        # Try a direct flight
        try:
            self._max_stopovers = 0
            self.make_request()
            self._price = self._response_data["data"][0]["price"]
        # If no direct flight exists try a single stopover
        except IndexError:
            self._max_stopovers = 1
            self.make_request()
            try:
                self._price = self._response_data["data"][0]["price"]
            # If no one stopover flight exists try a two stopover
            except IndexError:
                self._max_stopovers = 2
                self.make_request()
                try:
                    self._price = self._response_data["data"][0]["price"]
                # If no two stopover flight exists try a return a zero
                except IndexError:
                    self._max_stopovers = 3
                    self.make_request()
                    try:
                        self._price = self._response_data["data"][0]["price"]
                    except IndexError:
                        self._price = None
                        return self._price
                    else:
                        return self._price
                else:
                    return self._price
            else:
                return self._price
        else:
            return self._price

    def get_departure_city(self):
        departure_city = self._response_data["data"][0]["cityFrom"]
        return departure_city

    def get_departure_airport(self):
        departure_airport = self._response_data["data"][0]["flyFrom"]
        return departure_airport

    def get_arrival_city_name(self):
        arrival_city_name = self._response_data["data"][0]["cityTo"]
        return arrival_city_name

    def get_arrival_airport_name(self):
        arrival_airport_name = self._response_data["data"][0]["flyTo"]
        return arrival_airport_name

    def get_outbound_date(self):
        outbound_date = (self._response_data["data"][0]["route"][0]["utc_departure"]).split("T")[0]
        return outbound_date

    def get_inbound_date(self):
        if self._max_stopovers == 0:
            inbound_date = (self._response_data["data"][0]["route"][1]["utc_departure"]).split("T")[0]
            return inbound_date
        elif self._max_stopovers == 1:
            inbound_date = (self._response_data["data"][0]["route"][2]["utc_departure"]).split("T")[0]
            return inbound_date
        elif self._max_stopovers == 2:
            inbound_date = (self._response_data["data"][0]["route"][3]["utc_departure"]).split("T")[0]
            return inbound_date

    def get_currency(self):
        currency = self._response_data["currency"]
        return currency

    def get_stop_over_location(self):
        if self._max_stopovers == 1:
            self._via_city = f'{self._response_data["data"][0]["route"][0]["cityTo"]}'
            return self._via_city
        elif self._max_stopovers == 2:
            self._via_city = f'{self._response_data["data"][0]["route"][0]["cityTo"]}'
            return self._via_city
        elif self._max_stopovers == 3:
            self._via_city = f'{self._response_data["data"][0]["route"][0]["cityTo"]} and {self._response_data["data"][0]["route"][1]["cityTo"]}'
            return self._via_city

    def text_message(self):
        if self._max_stopovers == 0:
            txn_currency = self.get_currency()
            dep_city = self.get_departure_city()
            dep_airport = self.get_departure_airport()
            arrival_city = self.get_arrival_city_name()
            arrival_airport = self.get_arrival_airport_name()
            outbound_date = self.get_outbound_date()
            inbound_date = self.get_inbound_date()
            link = f"https://www.google.co.uk/flights?hl=en#flt={dep_airport}.{arrival_airport}.{outbound_date}*{dep_airport}.{arrival_airport}.{inbound_date}"
            text_body = f"Low price alert! Only {txn_currency}{self._price} to fly from {dep_city}-{dep_airport} to {arrival_city}-{arrival_airport} from {outbound_date} to {inbound_date}\n\n {link}"
            return text_body

        elif self._max_stopovers == 1:
            txn_currency = self.get_currency()
            dep_city = self.get_departure_city()
            dep_airport = self.get_departure_airport()
            arrival_city = self.get_arrival_city_name()
            arrival_airport = self.get_arrival_airport_name()
            outbound_date = self.get_outbound_date()
            inbound_date = self.get_inbound_date()
            stop_over = self.get_stop_over_location()
            link = f"https://www.google.co.uk/flights?hl=en#flt={dep_airport}.{arrival_airport}.{outbound_date}*{dep_airport}.{arrival_airport}.{inbound_date}"
            text_body = f"Low price alert! Only {txn_currency}{self._price} to fly from {dep_city}-{dep_airport} to {arrival_city}-{arrival_airport} from {outbound_date} to {inbound_date}\n\nFlight has 1 stop over, via {stop_over}\n\n{link}"
            return text_body

        elif self._max_stopovers == 2:
            txn_currency = self.get_currency()
            dep_city = self.get_departure_city()
            dep_airport = self.get_departure_airport()
            arrival_city = self.get_arrival_city_name()
            arrival_airport = self.get_arrival_airport_name()
            outbound_date = self.get_outbound_date()
            inbound_date = self.get_inbound_date()
            stop_over = self.get_stop_over_location()
            link = f"https://www.google.co.uk/flights?hl=en#flt={dep_airport}.{arrival_airport}.{outbound_date}*{dep_airport}.{arrival_airport}.{inbound_date}"
            text_body = f"Low price alert! Only {txn_currency}{self._price} to fly from {dep_city}-{dep_airport} to {arrival_city}-{arrival_airport} from {outbound_date} to {inbound_date}\n\nFlight has 1 stop over, via {stop_over}\n\n{link}"
            return text_body

        elif self._max_stopovers == 3:
            txn_currency = self.get_currency()
            dep_city = self.get_departure_city()
            dep_airport = self.get_departure_airport()
            arrival_city = self.get_arrival_city_name()
            arrival_airport = self.get_arrival_airport_name()
            outbound_date = self.get_outbound_date()
            inbound_date = self.get_inbound_date()
            stop_over = self.get_stop_over_location()
            link = f"https://www.google.co.uk/flights?hl=en#flt={dep_airport}.{arrival_airport}.{outbound_date}*{dep_airport}.{arrival_airport}.{inbound_date}"
            text_body = f"Low price alert! Only {txn_currency}{self._price} to fly from {dep_city}-{dep_airport} to {arrival_city}-{arrival_airport} from {outbound_date} to {inbound_date}\n\nFlight has 2 stop overs, via {stop_over}\n\n{link}"
            return text_body
