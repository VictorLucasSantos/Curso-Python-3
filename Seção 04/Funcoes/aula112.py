"""
filter - realiza filtro no iterator

filter(FUNCAO PARA REALIZAR O FILTRO, ITERAVEL)
"""


def print_iter(iter):
    print(*list(iter), sep="\n")
    print()


produtos = [
    {"nome": "p1", "preco": 20},
    {"nome": "p2", "preco": 10},
    {"nome": "p3", "preco": 30},
]

novos_produtos = [p for p in produtos if p["preco"] > 10]

novos_produtos1 = filter(lambda p: p["preco"] > 20, produtos)

print("produtos")
print(produtos)
print()
print("novos_produtos")
print(novos_produtos)
print()
print("novos_produtos1")
print(list(novos_produtos1))
