"""
Funções recursivas e recursividade
- funções que podem se chamar de volta
- úteis p/ dividir problemas grandes em partes menores
Toda função recursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pequeno problema
- Um caso base que para a recursão
- fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
https://brasilescola.uol.com.br/matematica/fatorial.htm

"""

import sys

# Setando limite de recursão manualmente
sys.setrecursionlimit(1004)


def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim

    print(inicio, fim)

    inicio += 1
    return recursiva(inicio, fim)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(recursiva())
print()
print(factorial(5))
# 0 10
# 1 10
# 2 10
# 3 10
# 4 10
# 5 10
# 6 10
# 7 10
# 8 10
# 9 10
# 10

# 120
