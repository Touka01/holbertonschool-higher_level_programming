#!/usr/bin/python3

import random

# Generate a random signed number
number = random.randint(-10000, 10000)

# Calculate the last digit using integer division and modulo
last_digit = number % 10 if number >= 0 else (number * -1) % 10 * -1

message = f"Last digit of {number} is {last_digit} and "
if last_digit == 0:
    message += "is 0"
elif last_digit > 5:
    message += "is greater than 5"
else:
    message += "is less than 6 and not 0"

print(message)
