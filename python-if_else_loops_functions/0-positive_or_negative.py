#!/usr/bin/python3

import random

# Generate a random signed number
number = random.randint(-10, 10)

# Checks if the number is either positive, negative, or zero
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
