# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest


def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2) for i in range(intervalo)]


l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]

print(zipper(l1, l2))
print()
# Metodo ja existente no python que faz a mesma coisa
print(list(zip(l1, l2)))

print(list(zip_longest(l1, l2, fillvalue="SEM CIDADE")))
