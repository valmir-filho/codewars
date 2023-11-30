"""
Messi goals function

Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions

Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

5, 10, 2  -->  17
"""


def goals(laLiga, copaDelRey, championsLeague):
    total_goals = laLiga + copaDelRey + championsLeague
    return total_goals


# Exemplo de uso da função:
laLiga_goals = 5
copaDelRey_goals = 10
championsLeague_goals = 2

total_goals = goals(laLiga_goals, copaDelRey_goals, championsLeague_goals)
print(total_goals)  # Isso imprimirá 17, que é o total de gols do Messi nas três ligas.
