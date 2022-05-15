import turtle

import pandas as pd

from us_states_data import us_states_names_list, xy_coord

from display import Display

# Creating a Screen Object
screen = turtle.Screen()

# Setting the screen title
screen.title("U.S. States Game")

# Importing the screen image
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)


# Game Loop
game_is_on = True

# TODO 5: Record the correct Guesses in a list
correct_guesses = []

# States to learn
missing_states = []

# TODO 6: Keep track of the Score
# Keeping Track of Player Score
player_score = 0

# TODO 4: Use a Loop to keep the User Guessing
while game_is_on:

    # Ask user to Guess a State
    answer_state = screen.textinput(title=f"Guess the State {player_score}/50", prompt="What's another state name?")

    # Initialize the Display Object
    display = Display(state_name=answer_state)
    
    # TODO 1: Convert Users Guess to Title Case
    answer_state = answer_state.title()

    # TODO 2: Check if the guess is among the 50 states ans if the guess hasn't been given already
    if answer_state in us_states_names_list and answer_state not in correct_guesses:
        is_right_answer = True
        correct_guesses.append(answer_state)
        player_score += 1

    else:
        is_right_answer = False

    # TODO 3: Write correct guesses unto the map
    if is_right_answer:
        # Get the coord on the state
        answer_coord = xy_coord(state_name=answer_state)
        # Initialize the display
        display.update_canvas(coord=answer_coord)

    if answer_state.lower() == "exit":
        display.game_over(score=player_score)
        for state in us_states_names_list:
            if state not in correct_guesses:
                missing_states.append(state)
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_learn.csv")
        game_is_on = False

# When to Exit
screen.exitonclick()
