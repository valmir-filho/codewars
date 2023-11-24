"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def count_vowels(s):
    # Define a set of vowels
    vowels = set("aeiou")
    
    # Initialize a count variable to 0
    count = 0
    
    # Iterate through the characters in the string
    for char in s:
        # Check if the character is in the set of vowels
        if char in vowels:
            # Increment the count if it's a vowel
            count += 1
    
    return count

# Example usage:
input_string = "hello world"
result = count_vowels(input_string)
print("Number of vowels:", result)
