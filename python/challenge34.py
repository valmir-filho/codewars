"""Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

For example, if this array were passed as an argument:

["Telescopes", "Glasses", "Eyes", "Monocles"]

Your function would return the following array:

["Eyes", "Glasses", "Monocles", "Telescopes"]

All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length.
"""


def sort_strings_by_length(strings):
    # Use the sorted function with a custom sorting key
    return sorted(strings, key=lambda s: len(s))


# Example usage:
input_strings = ["Telescopes", "Glasses", "Eyes", "Monocles"]
sorted_strings = sort_strings_by_length(input_strings)
print(sorted_strings)  # This will print ["Eyes", "Glasses", "Monocles", "Telescopes"]
