"""
    This is a tip calculator
    Input:  Total Bill amount (float)
            Percentage of tip you would like to give (float)
            Number of People to split the bill amongst (int)

    Output: How much each person should pay (str)
"""

# Welcome Statement
print("Welcome to the tip calculator")

print("\n")

# Accept total bill input from user

bill_total = float(input("What was the total bill? \n$"))

print("\n")

# Percentage Tip

perc_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? \n$"))

print("\n")

# How many people to split the bill?

no_of_persons = int(input("How many people to split the bill? \n"))


print("\n")

# Payment per person
payment_per_person = ((1 + (perc_tip/100)) * bill_total) / (no_of_persons)



# Printing out result
message = f"Each person should pay: ${round(payment_per_person, 2):.2f}"
print(message)
