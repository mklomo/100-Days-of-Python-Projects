"""
    Building an Amazon Price Tracker
"""

from bs4 import BeautifulSoup

import lxml

from dotenv import load_dotenv

import os

import requests

import smtplib

import ssl


# Get Access to env variables
load_dotenv()
SERVER = os.getenv("SMTP_SERVER")
PORT = os.getenv("SMTP_PORT")
MY_EMAIL = os.getenv("YOUR_EMAIL")
PASSWORD = os.getenv("YOUR_PASSWORD")

PRODUCT_URL = "https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5M9XBS/ref=sr_1_4?dchild=1&keywords=15%2Binch%2BM1%2BMACBOOK&qid=1625500975&sr=8-4&th=1"

PRODUCT = "Apple-MacBook-13-inch-256GB-Storage"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
}

OFFER_PRICE = 1200

# The code below works after multiple call so lets define a way to be sure it return a value
continue_scraping = True

while continue_scraping:
    # Get response from Webpage
    response = requests.get(url=PRODUCT_URL, headers=HEADERS)

    # Check for responses
    response.raise_for_status()

    # Get the browser html
    product_webpage = response.text
    # print(product_webpage)

    # Lets make soup now
    soup = BeautifulSoup(markup=product_webpage, features="lxml")
    # Using the CSS Selector to get price information
    price_info = soup.select_one(selector=".a-color-price")
    print(price_info)
    if price_info is not None:
        # Clean the price info
        price_str = (price_info.get_text()).strip("\n").strip("$")
        # Cast the price to float
        try:
            product_price = float(price_str)
        except ValueError:
            price_str = price_str.replace(",","")
            product_price = float(price_str)
        if product_price < OFFER_PRICE:
            print("Deal Found!!!")
            with smtplib.SMTP(SERVER, PORT) as new_connection:
                # Start a secure transport layer security
                context = ssl.create_default_context()
                new_connection.starttls(context=context)
                # Login to the email
                new_connection.login(user=MY_EMAIL, password=PASSWORD)
                SUBJECT_LINE = f"Subject:Deal Found. Buy Now!!!"
                msg = f"Best Deal! {PRODUCT} available for ${product_price} now!\n\n {PRODUCT_URL}"
                email_content = f"{SUBJECT_LINE}\n\n{msg}\n\n"
                new_connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs="mklomo@misi.edu.my",
                                        msg=email_content)
                print("Mail Sent")
        break
