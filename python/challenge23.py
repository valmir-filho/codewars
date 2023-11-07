"""
Bob needs a fast way to calculate the volume of a cuboid with three values: the length, width and height of the cuboid. Write a function to help Bob with this
calculation.
"""


def get_volume_of_cuboid(length, width, height):
    return length * width * height


result = get_volume_of_cuboid(2, 4, 3)
print(f"The volum of a cuboid is {result}.")
