"""
    This is an implementation of the FizBuzz interview question
"""

# Fiz Buzz Interview Question
# From 1 - 100 (inclusive)
# If number is divisible by 3, we call out "Fizz"
# If number is divisible by 5, we call out "Buzz"
# If number is divisible by both 3 and 5, we call out "FizzBuzz"


# For number from 1 - 100
for number in range(1, 101):
    # Empty accumulator
    result = ''
    
    # Is the number cleanly divisible by 3?
    if (number % 3 == 0):
        # Result = 'Fizz'
        result += 'Fizz'

    # Is the number cleanly divisible by 5?        
    if (number % 5 == 0):
        result += 'Buzz'

    # If number is neither divisible by 3 or 5
    elif result == '':
        # Assign result to the number
        result = str(number)
        
    print(result)