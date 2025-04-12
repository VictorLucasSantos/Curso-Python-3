"""
reduce - reduz o iteravel

reduce(FUNCAO PARA REALIZAR A REDUCAO, ITERAVEL, VALOR INICIAL DA REDUCAO)

O reduce é uma função bem útil do módulo functools do Python, 
que permite aplicar uma função a pares de elementos de uma sequência, 
reduzindo-a a um único valor
"""

from functools import reduce

produtos = [
    {"nome": "p1", "preco": 20},
    {"nome": "p2", "preco": 10},
    {"nome": "p3", "preco": 30},
]

total = 0

for p in produtos:
    total += p["preco"]


def funcao_reduce(acumulador, produto):
    print("acumulador", acumulador)
    print("produto", produto)
    print()
    return acumulador + produto["preco"]


print(total)
# utilizando uma função
print(reduce(funcao_reduce, produtos, 0))
# forma resumida
print(reduce(lambda x, y: x + y["preco"], produtos, 0))
