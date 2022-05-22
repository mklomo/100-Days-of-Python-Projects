import requests
import json
import os
from twilio.rest import Client
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TODAY = dt.datetime.today()
PREVIOUS_DAY = TODAY - dt.timedelta(days=1)
# Formatting the Previous Day
PREVIOUS_DAY = PREVIOUS_DAY.replace(hour=20, minute=00, second=00).strftime('%Y-%m-%d %H:%M:%S')
# Formatting the Two Days Prior Date
TWO_DAYS_AGO = TODAY - dt.timedelta(days=2)
TWO_DAYS_AGO = TWO_DAYS_AGO.replace(hour=20, minute=00, second=00).strftime('%Y-%m-%d %H:%M:%S')
stock_account_token = os.getenv("ALPHA_VANTAGE_AUTH_TOKEN")
news_account_auth = os.getenv("NEWS_API_AUTH")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

stock_api_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stock_account_token,
}

news_api_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_account_auth,
}

# Make an API request
stock_response = requests.get(STOCK_ENDPOINT, params=stock_api_parameters)
# Raise exception when sth untoward happens
stock_response.raise_for_status()

# Response data
response_data = stock_response.json()
# Dump json data into a file to get a feel of how it looks
# with open("TSLA_stock_prices.json", mode="w") as output_file:
#     json.dump(response_data, output_file, indent=4)

# Filtering the json data
previous_day_end_price = stock_response.json()["Time Series (60min)"][PREVIOUS_DAY]["4. close"]
# Convert price to float
previous_day_end_price = float(previous_day_end_price)
two_days_price_end = stock_response.json()["Time Series (60min)"][TWO_DAYS_AGO]["4. close"]
# Convert price to float
two_days_price_end = float(two_days_price_end)


def relevant_price_change(prev_day: float, two_prev_day: float):
    price_change = ((prev_day - two_prev_day) * 100) / (two_prev_day)
    if price_change < 0:
        return f"🔻{abs(round(price_change, 2))}%"
    else:
        return f"🔺{abs(round(price_change, 2))}%"


# Call the function
get_news = True

if get_news:
    # heading of message
    heading = relevant_price_change(prev_day=previous_day_end_price, two_prev_day=two_days_price_end)
    # Make an API request
    news_response = requests.get(NEWS_ENDPOINT, params=news_api_parameters)
    # Raise exception when sth untoward happens
    news_response.raise_for_status()
    # Get the news_response data and filter
    top_three_news_response_data_list = news_response.json()["articles"][:3]
    for news in range(len(top_three_news_response_data_list)):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{heading}\nHeadline: {top_three_news_response_data_list[news]['title']}\nDescription: {top_three_news_response_data_list[news]['description']}",
            from_='+17205711913',
            to='+233557299146'
        )
    print(message.status)
