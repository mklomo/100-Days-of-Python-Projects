import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"


# Get the response from the website
response = requests.get(url=URL)

# Check for exception
response.raise_for_status()

# Get the response in a text format
empire_webpage = response.text

# Lets start making our soup
soup = BeautifulSoup(markup=empire_webpage, features="html.parser")

# Next get the titles of the movies
movie_list = soup.select(selector="h3 a")

# Loop through movies and save
for movie_index in range(len(movie_list)):
    text = movie_list[movie_index].getText()
    with open("top_50_movies_of_all_time.txt", mode="a") as file:
        file.write(f"{movie_index+1} {text}\n")



