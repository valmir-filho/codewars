"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""


def persistence(num):
    # Base case: If num is a single-digit number, return 0.
    if num < 10:
        return 0


    # Initialize a variable to keep track of the persistence.
    persistence_count = 0
    
    # Convert the number to a string to work with its digits.
    num_str = str(num)
    
    # Multiply the digits of the number.
    product = 1
    for digit in num_str:
        product *= int(digit)
    
    # Recursively call the function with the product.
    return persistence_count + 1 + persistence(product)


# Test cases
print(persistence(39))   # Output: 3
print(persistence(999))  # Output: 4
print(persistence(4))    # Output: 0
