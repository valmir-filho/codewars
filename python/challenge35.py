"""
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
"""


def solution(arr):
    # Check if the input array is empty or None
    if arr is None or len(arr) == 0:
        return []

    # Sort the array in ascending order
    arr.sort()
    
    return arr


# Test cases
print(solution([1, 2, 3, 10, 5]))  # should return [1, 2, 3, 5, 10]
print(solution(None))  # should return []
