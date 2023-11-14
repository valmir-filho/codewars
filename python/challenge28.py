"""
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only

Cat Years

15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

Dog Years

15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""


def calculate_pet_ages(human_years):
    # Initial ages for cat and dog in their first year
    cat_years = 15
    dog_years = 15

    # If more than one year, add the second year
    if human_years > 1:
        cat_years += 9
        dog_years += 9

    # For each additional year, add respective years for cat and dog
    if human_years > 2:
        cat_years += 4 * (human_years - 2)
        dog_years += 5 * (human_years - 2)

    return [human_years, cat_years, dog_years]


# Example usage of the function
human_years = 5  # Replace 5 with the desired number of human years
result = calculate_pet_ages(human_years)
print(result)
