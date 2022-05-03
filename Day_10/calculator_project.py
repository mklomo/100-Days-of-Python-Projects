"""
    This project implements the logic of building a Calculator in Python
"""

from art_work import logo

from replit import clear


print(logo)

print("\n")


# Defining the addition 
def add(n_1, n_2):
    # Add two numbers
    return(n_1 + n_2)


# Defining the subtraction
def subtract(n_1, n_2):
    # Subtract two numbers
    return(n_1 - n_2)


# Defining the Multiply function
def multiply(n_1, n_2):
    # Multiply two numbers
    return(n_1 * n_2)


# Defining the divide function
def divide(n_1, n_2):
    # Divide two numbers
    return(n_1 / n_2)


# Creating a dictionary where the keys are the math symbos and the values are the function names
operation = {
    
    "+"  : add,
    "-"  : subtract,
    "*"  : multiply,
    "/"  : divide,

}

# The above makes this work

# function = operation["-"]
# function(2,3)

def calculator():
    # Loop through the operations dictionary and print out the key
    for symbol in operation:
        print(symbol)

    print("\n")
    # Ask user for input number 1
    number_1 = float(input("What is the first number?: "))

    print("\n")

    should_continue = True

    while should_continue:


        # Loop through the operations dictionary and print out the key
        for symbol in operation:
            print(symbol)

        print("\n")

        # Select the operation to perform
        operation_symbol = input("Pick an operation from the line above: ")


        print("\n")

        # Ask user for input number 2
        number_2 = float(input("What is the next number?: "))
        print("\n")

        # Take the operation and select the corresponding function
        operator_function = operation[operation_symbol]

        # what is the answer?
        answer = operator_function(number_1, number_2)

        print(f"{number_1} {operation_symbol} {number_2} = {answer}")

        print("\n")

        # Continue further?
        if input(f"Type 'y' to continue calculating with the {answer}, or type 'n' to start a new calculation:") == "y":
            number_1 = answer
        
        else:
            should_continue = False
            clear()
            calculator()



# Call the calculator function
if __name__ == "__main__":
    calculator()
