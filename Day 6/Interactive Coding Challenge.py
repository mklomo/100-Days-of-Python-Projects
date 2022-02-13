# Working with Functions

# Interactive coding challenge
#  @ https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

# There are six hurdles to jump hence
for hurdle in range(6):
    move()
    jump()


# While loops
# while a condition is true:
    # Do somethings
    # Is it false now

# Interactive coding challenge @
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# Interactive coding challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    if right_is_clear() == True:
        turn_right()
        move()
        turn_right()
    while front_is_clear():
        move()
    turn_left()

# While not at the flag
while not at_goal():
    # If front is not clear
    while wall_in_front() == True:
        jump()
    if front_is_clear():
        move()



# Interactive coding challenge
# @ https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Interactive coding challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    if right_is_clear() == True:
        turn_right()
        move()
        turn_right()
    while front_is_clear():
        move()
    turn_left()

# While not at the flag
while not at_goal():
    # If front is not clear
    while wall_in_front() == True:
        jump()
    if front_is_clear():
        move()