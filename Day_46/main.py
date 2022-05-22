"""
    Python Time Machine Project with Billboard and Spotify API
"""

import os

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Get access to your local environment var
load_dotenv()


DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD \n")

URL = f"https://www.billboard.com/charts/hot-100/{DATE}"

SPOTIFY_OAUTH_TOKEN_URL = os.getenv("YOUR_SPOTIFY_OAUTH_TOKEN_URL")

SPOTIFY_CLIENT_ID = os.getenv("YOUR_SPOTIFY_CLIENT_ID")

SPOTIFY_SECRET = os.getenv("YOUR_SPOTIFY_SECRET")

REDIRECT_URI = os.getenv("YOUR_SPOTIFY_REDIRECT_URI")

# Get the response
response = requests.get(url=URL)

# Check for exceptions
response.raise_for_status()

# Get the response text
billboard_webpage = response.text
# print(billboard_webpage)


# Lets make soup with BS
soup = BeautifulSoup(markup=billboard_webpage, features="html.parser")

# Get the top 100
top_100_list = []
for song_title_tag in soup.select(selector=".chart-element__information__song"):
    text = song_title_tag.get_text()
    top_100_list.append(text)
# print(top_100_list)


# Working with the Spotify API

# Authentication using SpotifyOAuth
scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri=REDIRECT_URI,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]

song_uris = []

year = DATE.split("-")[0]

for song in top_100_list:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in spotify. Skipped")


# Create a playlist
play_list = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)

# Add tracks to playlist
sp.playlist_add_items(playlist_id=play_list["id"], items=song_uris)
