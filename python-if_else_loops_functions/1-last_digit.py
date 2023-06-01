#!/usr/bin/python3

import random

# Generate a random signed number
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Determine the output message based on the value of the last digit
if last_digit == 0:
    message = f"Last digit of {number} is {last_digit} and is 0"
elif last_digit > 5:
    message = f"Last digit of {number} is {last_digit} and is greater than 5"
else:
    message = f"Last digit of {number} is {last_digit} and is less than 6 and not 0"

# Print the message
print(message)
