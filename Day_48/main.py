import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/marvinlomo/Documents/Development/chromedriver"

# Setup the Chrome Driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Get the Cookie Clicker website
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

# Check the current time and add 5sec
PERIODIC_CHECK = time.time() + 5  # Periodic time after 5sec


while True:
    # Now click the cookie continuously
    cookie.click()
    # After every 5 seconds
    time_now = time.time()
    if time_now > PERIODIC_CHECK:
        # Get upgrade item ID
        items = driver.find_elements_by_css_selector("#store div")
        item_ids = [item.get_attribute("id") for item in items]
        # Removing empty items in the items_id_list
        while "" in item_ids:
            item_ids.remove("")

        print(item_ids)
        # Get all the prices
        all_entries = []
        all_prices = []
        for item in driver.find_elements_by_css_selector(css_selector="#store div b"):
            all_entries.append(item.text)

        for entry in all_entries:
            if "-" in entry:
                text = int(entry.split("-")[1].strip(" ").replace(",", ""))
                all_prices.append(text)
        print(all_prices)

        # Now create a dictionary to store items and prices
        cookie_upgrades = {}
        for i in range(len(all_prices)):
            cookie_upgrades[all_prices[i]] = item_ids[i]
        print(cookie_upgrades)
        # Get the cookie_count
        cookie = driver.find_element_by_css_selector("#money")
        try:
            cookie_count = int(cookie.text)
        except ValueError:
            cookie_count = int(cookie.text.replace(",", ""))
        print(cookie_count)

        # Now, find upgrades you can afford
        affordable_upgrades = {}

        for cost, upgrade_item in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = upgrade_item

        print(affordable_upgrades)
        # Purchase the most expensive affordable upgrade
        if len(affordable_upgrades) == 0:
            pass
        else:
            # Select the last key in the affordable_upgrades dictionary
            best_affordable_upgrade = list(affordable_upgrades.keys())[-1]
            to_purchase_id = affordable_upgrades[best_affordable_upgrade]
            print(to_purchase_id)
        if len(to_purchase_id) == 0:
            pass
        else:
            purchase_element = driver.find_element_by_id(to_purchase_id)
            purchase_element.click()

        # Check the current time and add 5sec
        PERIODIC_CHECK = time.time() + 30  # Periodic time after 30 sec














