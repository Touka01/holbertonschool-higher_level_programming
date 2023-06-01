#!/usr/bin/python3

import random

# Generate a random signed number
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Determine the sign of the last digit
sign = ""
if number < 0:
    sign = "-"

# Print the last digit with the corresponding message
print("Last digit of", sign + str(number), "is", sign + str(last_digit), end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
