import json
import random
import string
from tkinter import *
from tkinter import messagebox

import pyperclip

USER_ENTRY = ""


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """
        Password Generator Project
        input:  password length
                Number of Digits
                Number of Symbols

        output: password (as string)
    """

    # List of all lowercase and uppercase characters in Python
    all_alphabets = list(string.ascii_letters)

    all_digits = list(string.digits)

    all_symbols = list(string.punctuation)

    password_length = random.randrange(15, 20)

    number_of_symbols = random.randrange(3, 5)

    number_of_digits = random.randrange(2, 5)

    # Computing the count of each password element
    alphabet_length = password_length - number_of_symbols - number_of_digits

    # Accumulator for password
    password_characters = [random.choice(all_alphabets) for alphabet in range(alphabet_length)]

    # randomly select number of symbols

    # Accumulator for symbols
    password_symbols = [random.choice(all_symbols) for symbol in range(number_of_symbols)]

    # Randomly Select Digits

    # Accumulator for digits
    password_digits = [random.choice(all_digits) for digit in range(number_of_digits)]

    # Now, construct the password and randomize output
    password_list = password_characters + password_symbols + password_digits

    # Now lets shuffle the password_list inplace
    random.shuffle(password_list)

    # Convert the elements in the list to a string
    final_password = "".join(password_list)

    if len(password_entry.get()) == 0:
        password_entry.insert(0, final_password)
        pyperclip.copy(final_password)

    else:
        password_entry.delete(0, END)
        generate_password()
        pyperclip.copy(final_password)


# ---------------------------- UI SETUP ------------------------------- #

# Creating the TKinter window
window = Tk()
# Title of the window
window.title("Marvin's Password Manager")
# Windows minsize
window.minsize(width=600, height=480)
window.maxsize(width=600, height=480)
window.config(padx=40, pady=40)

# Creating the canvas
canvas = Canvas(width=220, height=288)
pwm_image = PhotoImage(file="pwm_logo.png")
canvas.create_image(130, 130, image=pwm_image)
canvas.grid(row=0, column=1)

# Creating Website label and entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

# Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, string="mklomo@icloud.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    global USER_ENTRY
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email":  email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} "
                                               f"\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            # Updating a json
            try:
                with open("master_data.json", mode="r") as master_data:
                    # Then load the read data (convert to dictionary)
                    data = json.load(master_data)
            except FileNotFoundError:
                with open("master_data.json", mode="w") as master_data:
                    json.dump(new_data, master_data, indent=4)
            else:
                # Update the json data with new_data
                data.update(new_data)

                with open("master_data.json", mode="w") as master_data:
                    # Save the updated
                    json.dump(data, master_data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


def find_password():
    # Key to search
    website = website_entry.get().lower()
    if len(website) == 0:
        messagebox.showinfo(title="Oops...", message="Please provide the website")

    # To read a dictionary to json
    try:
        with open("master_data.json", mode="r") as master_data:
            data = json.load(master_data)
        website_details = data[website]
    except FileNotFoundError:
        messagebox.showinfo(title="Oops...", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Oops...", message="No Details for the website exists")
    else:
        email_details = website_details["email"]
        password_details = website_details["password"]
        messagebox.showinfo(title=f"Your {website_details}", message=f"Your email: {email_details} \nYour password: {password_details}")


# Search Button
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, columnspan=2)










# Event listener
window.mainloop()
