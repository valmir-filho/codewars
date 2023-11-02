"""
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array
(true means present).

For example:

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined.
"""


def count_sheeps(sheeps):    
    if sheeps is None:
        return 0
    count = 0
    for sheep in sheeps:
        if sheep is not None and sheep is True:
            count += 1
    return count


sheeps = [True, True, True, False,
         True, True, True, True,
         True, False, True, False,
         True, False, False, True,
         True, True, True, True,
         False, False, True, True]

result = count_sheeps(sheeps)    
print(f"The number of sheeps in array is {result}.")
