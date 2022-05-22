import random
from tkinter import *

import pandas as pd
from tkmacosx import CircleButton

BACKGROUND_COLOR = "#c84b31"
FRENCH_HEADING = "FRENCH"
ENGLISH_HEADING = "ENGLISH"
TIME_DELAY = 2000


# Lets work on the text
try:
    # If words to learn exists, use that as the master data
    master_data = pd.read_csv("data/words_to_learn.csv")

# If no words to learn file exists, please load the french words file
except FileNotFoundError:
    master_data = pd.read_csv("data/french_words.csv")
    # Convert the Dataframe into a dictionary with the french_word: english_word format
    master_data_dict = {row.French: row.English for (index, row) in master_data.iterrows()}

else:
    # Convert the Dataframe to a dictionary where the keys are the column headers
    master_data_dict = {row.French: row.English for (index, row) in master_data.iterrows()}


# Function to select a random entry from the master_data_dict
def random_selection():
    """
    This function returns a random french_word (str) and english_word translation (str)
    """
    global master_data_dict
    # Convert the master_data_dict to a list  containing tuples (french_word, english_word)
    master_data_list = list(master_data_dict.items())
    # Randomly select one tuple from the list
    selected_data = random.choice(master_data_list)
    # return the french_word, english_word
    return selected_data[0], selected_data[1]


def next_card():
    """
    This function shows the french side of the card
    """
    global french_word, english_word, flip_timer
    # Reset the incoming timer
    window.after_cancel(flip_timer)
    # Randomly select the french and english words
    french_word, english_word = random_selection()
    # Change the canvas text heading
    card_canvas.itemconfig(front_heading, text=FRENCH_HEADING)
    # Change the canvas' image to the card_front image
    card_canvas.itemconfig(card_canvas_image, image=card_front_image)
    # Change the on-card text to the french word
    card_canvas.itemconfig(front_text_body, text=french_word, fill="black")
    # Start a new timer
    flip_timer = window.after(TIME_DELAY, show_english_side)


def show_english_side():
    """
    This function shows the user the english translation pf the card
    """
    global english_word, front_heading, card_back_image
    # change the canvas heading to ENGLISH
    card_canvas.itemconfig(front_heading, text=ENGLISH_HEADING)
    # Change the canvas image to the back
    card_canvas.itemconfig(card_canvas_image, image=card_back_image)
    # change the canvas body text to the english translation
    card_canvas.itemconfig(front_text_body, text=english_word, fill="white")


def is_known():
    """
    This function deletes words the user has learnt from the master dictionary
    and creates a new csv file with those words I have to learn
    """
    global master_data_dict, french_word
    # delete the known word from the dictionary
    del master_data_dict[french_word]
    # New Dataframe of words to learn
    data = pd.DataFrame(master_data_dict.items(), columns=['French', 'English'])
    # Convert the data to a csv
    data.to_csv("data/words_to_learn.csv")
    # move to the next card
    next_card()


# Making the window
# Creating the TKinter window
window = Tk()
# Title of the window
window.title("Marvin's Flash Card App")
# Windows minsize
window.minsize(width=900, height=800)
window.maxsize(width=900, height=800)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating the Canvas
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
# Specify the position of the image on the grid
card_canvas.grid(row=0, column=0, columnspan=2)
card_canvas_image = card_canvas.create_image((400, 263), image=card_front_image)
front_heading = card_canvas.create_text((400, 150), text=FRENCH_HEADING, font=("Arial", 40, "italic"))
# Select the french word
french_word, english_word = random_selection()
# Show the front of the card
front_text_body = card_canvas.create_text((400, 280), text=french_word, font=("Arial", 60, "bold"))
# Show translation
flip_timer = window.after(TIME_DELAY, show_english_side)


# Adding circular image buttons to program
right_image = PhotoImage(file="images/right_image.png")
# Specify the button
right_button = CircleButton(image=right_image, bd=0, highlightthickness=0, borderless=1, bg=BACKGROUND_COLOR,
                            command=is_known)
# Specify the position
right_button.grid(row=1, column=1, pady=50)

wrong_image = PhotoImage(file="images/wrong_image.png")
# Specify the Button
wrong_button = CircleButton(image=wrong_image, bd=0, highlightthickness=0, borderless=1, bg=BACKGROUND_COLOR,
                            command=next_card)
# Specify the position
wrong_button.grid(row=1, column=0, pady=50)

# Event listener
window.mainloop()
