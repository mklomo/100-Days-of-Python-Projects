"""
    This is an internet speed complain bot project
"""

from internet_speed_twitter_bot import InternetSpeedTwitterBot

# Initialize the class
speed = InternetSpeedTwitterBot()

# Get the speed from speedtest.com
speed.get_internet_speed()

# Tweet results to ISP on twitter
speed.tweet_at_provider()