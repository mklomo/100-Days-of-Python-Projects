"""
    The higher-lower game with Flask
"""

from functools import wraps
from random import randint

from flask import Flask

# Generate a random number
GENERATED_NUM = randint(0, 9)
print(GENERATED_NUM)



app = Flask(__name__)


@app.route('/')
def random_number_gen():
    return "<h1>   Guess a Number between 0 and 9  </h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200>"



@app.route("/<int:guess>")
def guess_num(guess):
    global GENERATED_NUM
    if int(guess) == GENERATED_NUM:
        return "<h1 style='color: green'>   You guessed right!!  </h1>" \
               f"The Generated Number is {GENERATED_NUM}" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=200>"

    elif int(guess) < GENERATED_NUM:
        return "<h1 style='color: red'>   You guessed too LOW  </h1>" \
               f"The Generated Number is {GENERATED_NUM}" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=200>"

    else:
        return "<h1 style='color: pink'>   You guessed too HIGH  </h1>" \
               f"The Generated Number is {GENERATED_NUM}" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200>"


if __name__ == '__main__':
    app.run(debug=True)
