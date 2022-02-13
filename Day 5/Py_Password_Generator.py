"""
    Password Generator Project
    input:  password length
            Number of Digits
            Number of Symbols
    
    output: password (as string)
"""

# importing the relevant modules
import string
import random

# List of all lowercase and uppercase characters in Python
all_alphabets = list(string.ascii_letters)

all_digits = list(string.digits)

all_symbols = list(string.punctuation)

print("Welcome to Marvin's PyPassword Generator!\n")

password_length = int(input("How many letters would you like in your password?\n"))

number_of_symbols = int(input("How many symbols would you like? \n"))

number_of_digits = int(input("How many numbers would you like? \n"))

# Computing the count of each password element
alphabet_length = password_length - number_of_symbols - number_of_digits


# Accumulator for password
password_chararcters = []

# randomly select the characters
for alphabet in range(alphabet_length):
    password_chararcters.append(random.choice(all_alphabets))

# randomly select number of symbols

# Accumulator for symbols
password_symbols = []
for symbol in range(number_of_symbols):
    password_symbols.append(random.choice(all_symbols))


# Randomly Select Digits

# Accumulator for digits
password_digits = []

for digit in range(number_of_digits):
    password_digits.append(random.choice(all_digits))


# Now, construct the password and randomize output
password_list = password_chararcters + password_symbols + password_digits


# Now lets shuffle the password_list inplace
random.shuffle(password_list)

# Convert the elements in the list to a string
final_password = "".join(password_list)


print(f"Your password is {final_password}")
