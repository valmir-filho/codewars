"""
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]
"""


def get_range_inclusive(a, b):
    # Check if a is greater than or equal to b
    if a >= b:
        return []    
    # Create a list using a range from a to b+1
    result = list(range(a, b + 1))
    return result


# Example usage:
a = 1
b = 4

result = get_range_inclusive(a, b)
print(result)  # Output: [1, 2, 3, 4]
