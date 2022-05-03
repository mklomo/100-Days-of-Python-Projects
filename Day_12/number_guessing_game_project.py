"""
    This project implements the number guessing game
"""

import random

from art_work import logo


# Welcome Message

print("\nWelcome to Marvin's Number Guessing Game\n")

# Print the Logo

print(logo)


print("\n")


# Now ask the user's choice, "easy" or "hard"

user_choice = input(
    "Do you choose the easy or hard option? Type 'hard' or 'easy' \n"
).lower()


# Determining the number of lives from the users choice (Global Variables)

if user_choice == "hard":
    number_of_lives = 5
    print(f"You have {number_of_lives} lives")

else:
    number_of_lives = 10
    print(f"You have {number_of_lives} lives")


# The computer's choosen number b/n 1 - 100

valid_number = random.randrange(1, 101)

user_guess = 0

# While the number of lives is not 0

while number_of_lives != 0 and user_guess != valid_number:

    # Ask the user for their guess
    user_guess = int(input("\nPlease enter a number between 1 and 100: "))

    print("\n")

    # What happens if the user guesses correctly?
    if user_guess == valid_number:
        print(f"\nWell done! You guessed correctly\n")

    # What happens if the user guesses wrongly?
    elif user_guess > valid_number:
        print("\nSorry, you guessed higher!\n")

        # Reduce the number of lives
        number_of_lives -= 1

        # Print the number of lives the user has left
        print(f"You now have {number_of_lives} left!\n")

    elif user_guess < valid_number:
        print("Sorry you guessed lower\n")

        # Reduce number of lives by 1
        number_of_lives -= 1

        # Print the number of lives the user has left
        print(f"You now have {number_of_lives} left!\n")

    # What happens if number_of_lives == 0:
    if number_of_lives == 0:
        print("Sorry, Game Over!")
        