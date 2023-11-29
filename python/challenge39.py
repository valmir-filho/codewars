"""
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.
"""


def switch_it_up(number):
    
    number_words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    
    if number in number_words:
        return number_words[number]
    else:
        return "Invalid input, please enter a number between 0 and 9."


result = switch_it_up(1)
print(result)
