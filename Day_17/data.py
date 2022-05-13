import requests

# API for requests
URI = "https://opentdb.com/api.php?amount=15&type=boolean"

# Requests a GET Response from the URI
opent_db = requests.get(URI)

# Filter to obtain the needed dictionary
question_data = opent_db.json()['results']

print(question_data)
