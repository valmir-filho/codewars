"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 == 0:
            raise ValueError("Não é possível dividir por zero.")
        return value1 / value2
    else:
        raise ValueError("Operador inválido. Use '+', '-', '*' ou '/'.")


# Exemplos de uso:
print(basic_op('+', 4, 7))   # Output: 11
print(basic_op('-', 15, 18))  # Output: -3
print(basic_op('*', 5, 5))    # Output: 25
print(basic_op('/', 49, 7))   # Output: 7
