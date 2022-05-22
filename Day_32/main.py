##################### Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import ssl

import pandas as pd

LETTER_1_PATH = "letter_templates/letter_1.txt"
LETTER_2_PATH = "letter_templates/letter_2.txt"
LETTER_3_PATH = "letter_templates/letter_3.txt"
LETTER_LIST = [LETTER_1_PATH, LETTER_2_PATH, LETTER_3_PATH]
MY_EMAIL = input("Please enter the sender mail here: ")
PASSWORD = input("Please enter the email password here: ")
SERVER = "smtp.gmail.com"
PORT = 587
# Create a secure SSL context
context = ssl.create_default_context()


# Today datetime object
today = dt.datetime.now()

today_tuple = (today.month, today.day)

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# Load the birthday data
birthdays_master_data = pd.read_csv("birthdays.csv")
# Make the name column the df index
birthdays_master_data = birthdays_master_data.set_index("name")

# Convert the birthdays_master_data into a dictionary
birthdays_master_data_dict = {(row.month, row.day): {"name": row.name, "email": row.email} for (index, row) in
                              birthdays_master_data.iterrows()}

# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today_tuple in birthdays_master_data_dict:
    selected_letter_path = random.choice(LETTER_LIST)
    with open(selected_letter_path, mode="r") as letter:
        birthday_card = letter.read()
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        celebrant = birthdays_master_data_dict[today_tuple]["name"]
        celebrant_mail = birthdays_master_data_dict[today_tuple]["email"]
        birthday_card = birthday_card.replace("[NAME]", celebrant)
        # 4. Send the letter generated in step 3 to that person's email address.
        # Open a connection to your email server
        with smtplib.SMTP(SERVER, PORT) as new_connection:
            # Start a secure transport layer security
            new_connection.starttls(context=context)
            # Login to the email
            new_connection.login(user=MY_EMAIL, password=PASSWORD)
            # Randomly select  content from the master data and strip
            SUBJECT_LINE = f"Subject: Happy Birthday {celebrant}"
            email_content = f"{SUBJECT_LINE}\n\n{birthday_card}\nStay Blessed!"
            new_connection.sendmail(from_addr=MY_EMAIL,
                                 to_addrs=celebrant_mail,
                                    msg=email_content)
