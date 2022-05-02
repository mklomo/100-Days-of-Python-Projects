# Pseudocode for Hangman

# Step 1: Generate a random word

# Step 2: Generate as many blanks as letters in word

# initiate a life accumulator

# while the user has life > 0:
    # Step 3: Ask the user to guess a letter

    # if the guessed letter is in the word:
        # Replace the blank with the word

    # else:
        # Lose a life

    # if all blanks are filled:
        # print(Congrats, You guessed right!)
        # break out of loop

    # elif life == 0:
        # print("Game Over")


# Implementing Step 1:
import random

import hangman_ascii_art
import word_list

print("Welcome to the Hangman Game!\n")

print(hangman_ascii_art.logo)

print("\n")

print(hangman_ascii_art.stages[0])


# Randomly select a word from the word list
chosen_word = random.choice(word_list.word_list)

# Creating an Empty List with dashes where len(list) == len(chosen_word)
display = []


for letter in range(len(chosen_word)):
    display.append("_")

# Number of lives the player has
user_lives = 6


while "_" in display:
    # Ask user to guess a letter and make lowercase
    print("\n")
    print(display)
    user_guess = input("Please Guess a letter: \n").lower() 


    # Now check if the user has already guessed the correct letter
    while user_guess in display:
        print("You have already guessed this letter.")
        print("Please try again!")
        user_guess = input("Please Guess a letter: \n").lower() 


    # Check if the guessed letter is in the chosen word
    if user_guess in chosen_word:
        # Loop through the chosen word
        for key, value in enumerate(chosen_word):
            # Check if letter (value) in chosen word is == user_guess
            if value == user_guess:
                # If yes, then update display
                display[key] = value
                print(f"\nWell done, the letter '{user_guess}' correct!")
            
            
    # If the guessed letter is not in chosen word
    elif user_guess not in chosen_word:
        # Reduce the life by 1
        user_lives -= 1
        # And print these outputs
        print(f"Sorry, You guessed wrong!\n")
        print(f"The letter '{user_guess}'is not in the word")
        print(f"You have {user_lives} lives more!\n")
        print(hangman_ascii_art.stages[user_lives])


    # If all lives are exhausted
    if user_lives == 0:
        # Print this
        print("You lose!")
        break


    # If all the missing letter have been guessed correctly
    if "_" not in display:
        # Print this
        print("\nCongrats, You win!")
    # Join all the elements in the list and turn it into a string
        print(f"\n{''.join(display)}")
        break
    