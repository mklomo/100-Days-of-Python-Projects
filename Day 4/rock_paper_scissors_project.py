"""
    This srcipt contains code for playing the rock papper scissors game.

    Rules:
    - Rock wins against scissors
    - Scissors win sagainst paper 
    - Paper wins against rock 
"""

print("Welcome to the rock paper scissors game!\n")

# Insert ASCII Art

scissors = """
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

"""

paper = """
__________
         |DAILY NEWS|
         |&&& ======|
         |=== ======|
         |=== == %%$|
         |[_] ======|
         |=== ===!##|
 ejm97   |__________|
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

print(rock)
print("\n")
print(paper)
print("\n")
print(scissors)


# Import the random module 
import random

# Ask the user for input
user_choice = input("Please select your choice. Rock, Paper or Scissors?\n")

# Ensure consistency with input hence lowercase of users input
user_choice = user_choice.lower()

game_play_options = ["rock", "paper", "scissors"]

while user_choice not in game_play_options:
    print("Invalid input \n")
    user_choice = input("Please select your choice. Rock, Paper or Scissors?\n")
    user_choice = user_choice.lower()
    

# If user choice is valid, print out their choise and pc_choice
print(f"Your choice is {user_choice}")

print("\n")

# List of choices
pc_choice = random.choice(game_play_options)

print(f"PC Player's choice is {pc_choice}")

# Winner determination using rules
if user_choice == "rock" and pc_choice == "scissors":
    print("User Wins")


elif user_choice == "scissors" and pc_choice == "paper":
    print("User wins")    

elif pc_choice == "paper" and user_choice == "rock":
    print("User wins")

elif user_choice == pc_choice:
    print("Its a draw")

else:
    print("PC Wins")