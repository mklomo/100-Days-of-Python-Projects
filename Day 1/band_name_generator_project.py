"""
    This program generates a band name for a user 
    
    Input parameters:
    birth_city = (str) the city the user grew up in

    name_of_pet = (str) name of the users pet

    Ouput: 
    band_name = (str) name of users band
"""

# Create a greeting for the program
print("Hello, and welcome to the band name generator\n")

print("\n")

# What city did you grow up in?
birth_city = input("What city did you grow up in? \n")

print("\n")

# What is the name of your pet?
name_of_pet = input("What is the name of your pet? \n")

print("\n")

# Output
print(f"Congratulations, your band name is {birth_city + ' ' + name_of_pet}")