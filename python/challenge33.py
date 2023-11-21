"""
You ask a small girl, "How old are you?" She always says, "x years old", where x is a random number between 0 and 9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always
a number.
"""

import random


def get_girls_age(input_string):
    # Split the input string by spaces
    words = input_string.split()

    # Get the first word, which should be a number
    age_str = words[0]

    # Convert the age string to an integer
    age = int(age_str)

    return age


# Test the program with a random age between 0 and 9
random_age = random.randint(0, 9)
input_string = f"{random_age} years old."
girl_age = get_girls_age(input_string)
print(f"The girl's age is: {girl_age}.")
