"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""


def find_average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


result = find_average([1, 2, 3, 4, 5])
print(f"The average of numbers in a given list is {result}.")
