"""
    The higher and lower game
"""
# Define the Global Variable for User Score
# User score count
SCORE_COUNT = 0


# Import the relevant modules

import random

from replit import clear

from art_work import logo, vs
from game_data import data

# Welcome note and logo printing

print("\nWelcome to Marvin's Version of the Higher-Lower Game\n")


print("\n")


print(logo)


# Defining a function to randomly select the 2 options


def select_options(a_list):
    """
    This function takes a list and returns the 2 questions asked in the game
    Note that the 2 question can NOT be the same

    input: a_list

    output: two questions
    """

    # Randomly Select a Dictionary from the list
    first_dict = random.choice(a_list)

    second_dict = random.choice(a_list)

    while first_dict == second_dict:
        second_dict = random.choice(a_list)

    return first_dict, second_dict


# Next ask the selected questions
def ask_options(a_dict_1, a_dict_2):
    """
    This function takes the two randomly selected dictionaries
    and asks the relevant questions to the Player

    input: a_dict_1 (Dictionary)
           a_dict_2 (Dictionary)

    output: 2 questions (str)
    """
    # Creating question for first_option
    first_option = f" Compare A: {a_dict_1['name']}, a {a_dict_1['description']}, from {a_dict_1['country']}."

    # Creating option 2
    second_option = f" Against B: {a_dict_2['name']}, a {a_dict_2['description']}, from {a_dict_2['country']}."

    return first_option, second_option


def check_answer(a_dict_1, a_dict_2):
    """
        This function takes the player's choice and Determines whether he/she is right or wrong

    input: a_dict_1 (dict)
           a_dict_2 (dict)

    output: boolean
    """

    user_input = input("Who has more followers? Type 'A' or 'B' \n").lower()

    # Followers for each dictionary
    inst_fol_count_option_1 = a_dict_1["follower_count"]

    inst_fol_count_option_2 = a_dict_2["follower_count"]

    # When is the user right?
    if user_input == "a" and inst_fol_count_option_1 > inst_fol_count_option_2:
        return "correct"

    elif user_input == "b" and inst_fol_count_option_2 > inst_fol_count_option_1:
        return "correct"

    else:
        return "wrong"


# Now lets fix the logic


# Select the Question to ask
dict_1, dict_2 = select_options(data)


# continue game flag
continue_game = True

while continue_game:

    # Now ask the questions
    quest_1, quest_2 = ask_options(dict_1, dict_2)

    print(quest_1)

    print("\n")

    print(vs)

    print("\n")

    print(quest_2)

    print("\n")

    # Then maintain score and print out message
    msg = check_answer(dict_1, dict_2)

    # Lets be clever about printing the score and all else
    if msg == "correct":
        clear()
        print(logo)
        SCORE_COUNT += 1
        print(f"\nYou're right! Current score: {SCORE_COUNT}\n")
        continue_game = True

        # Implementing sequencing of questions
        dict_1 = dict_2

        dict_2 = random.choice(data)

        # Ensure that the two dicts are different
        while dict_1 == dict_2:
            dict_2 = random.choice(data)

    elif msg == "wrong":
        clear()
        print(logo)
        print(f"\nSorry, that's wrong! Your final score: {SCORE_COUNT}\n")
        print("Thank you!")
        continue_game = False
