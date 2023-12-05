"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only
alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicate_count(text):
    text = text.lower()  # Converter todo o texto para letras minúsculas para ser case-insensitive
    count = 0  # Inicializar a contagem de caracteres duplicados
    char_count = {}  # Dicionário para contar a ocorrência de cada caractere

    for char in text:
        if char.isalnum():  # Verificar se o caractere é uma letra ou número
            if char in char_count:
                if char_count[char] == 1:
                    count += 1  # Incrementar a contagem quando um caractere duplicado é encontrado
                char_count[char] += 1
            else:
                char_count[char] = 1

    return count


# Exemplos de uso:
print(duplicate_count("abcde"))  # Saída: 0
print(duplicate_count("aabbcde"))  # Saída: 2
print(duplicate_count("aabBcde"))  # Saída: 2
print(duplicate_count("indivisibility"))  # Saída: 1
print(duplicate_count("Indivisibilities"))  # Saída: 2
print(duplicate_count("aA11"))  # Saída: 2
print(duplicate_count("ABBA"))  # Saída: 2
