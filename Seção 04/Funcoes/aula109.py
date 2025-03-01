""""
Combinations, Permutations e Product - Itertools
    Combinação - Ordem não importa - iteravel + tamanho do grupo
    Permutação - Ordem importa
    Produto - Ordem importa e repete valores unicos
"""

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


pessoas = [
    "João",
    "Joana",
    "Luiz",
    "Letícia",
]

camisetas = [
    ["preta", "branca"],
    ["p", "m", "g"],
    ["masculino", "feminino", "unisex"],
    ["algodão", "poliéster"],
]

# combinacoes das pessoas em grupos de 2
print_iter(combinations(pessoas, 2))

# permutacoes das pessoas em grupos de 2
print_iter(permutations(pessoas, 2))

# Produto das camisetas, combinações com todos
print_iter(product(*camisetas))
