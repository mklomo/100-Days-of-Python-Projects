"""
    Creating a NATO Alphabet List from user input Project
"""

import pandas as pd

# Read the NATO-PHONETIC ALPHABET LIST
master_data_df = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary with letter:code key:value pair
nato_code_dict = {row.letter: row.code for (index, row) in master_data_df.iterrows()}


def generate_phonetic():
    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    user_input = input("Please enter a word: ").upper()

    # Create a nato_translation_list
    try:
        nato_translation_list = [nato_code_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters in the alphabet allowed")
        generate_phonetic()
    else:
        # for letter in user_input:
        print(nato_translation_list)


if __name__ == '__main__':
    generate_phonetic()
    
    