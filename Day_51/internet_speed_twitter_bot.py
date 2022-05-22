"""
    This class gets the current internet speed provided by your ISP
"""
import os
import time

from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

CHROME_DRIVER_PATH = "/Users/marvinlomo/Documents/Development/chromedriver"

TWITTER_EMAIL = os.getenv("YOUR_TWITTER_EMAIL")

TWITTER_PASSWORD = os.getenv("YOUR_TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    """
        This class uses a Selenium driver to get internet speed
    """

    def __init__(self):
        self._driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self._up = ""
        self._down = ""

    def get_internet_speed(self):
        self._driver.get(url="https://www.speedtest.net/")
        go_btn = self._driver.find_element_by_css_selector(css_selector=".start-text")
        go_btn.click()
        time.sleep(60)
        self._down = self._driver.find_element_by_css_selector(css_selector=".result-data .download-speed").text
        self._up = self._driver.find_element_by_css_selector(css_selector=".result-data .upload-speed").text

    def get_internet_up_speed(self):
        return self._up

    def get_internet_down_speed(self):
        return self._down

    def tweet_at_provider(self):
        # Get to the twitter login page
        self._driver.get(url="https://twitter.com/login")
        # Insert username
        username = self._driver.find_element_by_xpath(
            xpath="/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        username.send_keys(TWITTER_EMAIL)
        # Insert Password
        password = self._driver.find_element_by_xpath(
            xpath="/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        password.send_keys(TWITTER_PASSWORD)
        # Click On Login
        login_btn = self._driver.find_element_by_xpath(
            xpath="/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
        login_btn.click()
        # Insert text into 'Whats happening?'
        time.sleep(10)
        tweet = self._driver.find_element_by_xpath(
            xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet.send_keys(f"@VodafoneGhana my internet up-speed is {self._up}Mbps and down-speed is {self._down}Mbps")
        # Click on tweet
        tweet_btn = self._driver.find_element_by_xpath(
            xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()


