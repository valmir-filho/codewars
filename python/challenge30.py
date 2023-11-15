"""
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:

["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""


def remove_every_second_element(arr):
    return arr[::2]


# Example usage:
original_array = ["Keep", "Remove", "Keep", "Remove", "Keep"]

result_array = remove_every_second_element(original_array)
print(result_array)
