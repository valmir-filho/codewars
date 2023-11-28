# Given a non-empty array of integers, return the result of multiplying the values together in order. Example: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24.


def grow(arr):
    res = 1  # Initialize the result to 1

    for num in arr:
        res *= num

    return res


result = grow([1, 2, 3, 4])
print(result)
