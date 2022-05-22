"""
    
    This project uses Beautiful Soup and Selenium to create a list of rental apartments
    in Parsippany, NJ
    
"""

import os
import re
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Load the .env file
load_dotenv()

NJ_APARTMENTS_LINK = os.getenv("YOUR_LINK_TO_APARTMENTS")

GOOGLE_FORM_URL = os.getenv("YOUR_LINK_TO_FORM")

HEADERS = {
    "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "ACCEPT-ENCODING": "gzip, deflate, br",
    "ACCEPT-LANGUAGE": "en-GB,en-US;q=0.9,en;q=0.8",
    "UPGRADE-INSECURE-REQUESTS": "1",
    "USER-AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
}

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")

# Setup the Chrome Driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

link_check = True

rental_addresses = []
apartment_price = []
properties = []
property_link = []


while link_check:
    # Set the link_check to False
    link_check = False

    # Get a response from Zillow
    response = requests.get(url=NJ_APARTMENTS_LINK, headers=HEADERS)

    # Check for exceptions
    response.raise_for_status()

    # Get the response text
    apartments_webpage = response.text

    # Lets make soup with BS
    soup = BeautifulSoup(markup=apartments_webpage, features="html.parser")

    for address in soup.select(selector=".list-card-addr"):
        text = address.get_text()
        rental_addresses.append(text)

    for price in soup.select(selector=".list-card-price"):
        text = price.get_text()
        cost = text.split("$")[1]
        apartment_price.append(cost)

    for link in soup.select(selector=".list-card-link"):
        text = link.get("href")
        # Check if the link starts with "https" using regular expressions
        if re.match("^https", text):
            properties.append(text)

        else:
            # There is a bad link in here
            link_check = True
            # Now break from this loop
            break


# Now loop through the property list and select the unique links
for i in range(0, len(properties), 2):
    property_link.append(properties[i])

print(len(rental_addresses))
print(len(apartment_price))
print(len(property_link))
print(rental_addresses)
print(apartment_price)
print(property_link)


for entry in range(len(property_link)):
    # Open a Tab
    driver.get(url=GOOGLE_FORM_URL)
    time.sleep(5)
    # Find the xpath for address
    address = driver.find_element_by_xpath(xpath="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address.send_keys(f"{rental_addresses[entry]}")
    time.sleep(5)
    # Find the element for apartment_price
    price = driver.find_element_by_xpath(xpath="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price.send_keys(f"{apartment_price[entry]}")
    time.sleep(5)
    # Find the element for property_link
    link = driver.find_element_by_xpath(xpath="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link.send_keys(f"{property_link[entry]}")
    time.sleep(5)
    # Click the submit button
    submit_btn = driver.find_element_by_xpath(xpath="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span")
    submit_btn.click()
    time.sleep(5)
    # Close the Tab
    # driver.close()


