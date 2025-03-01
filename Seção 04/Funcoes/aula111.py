"""
map - Map reliza operações com os dados de um iterator (passa sobre todo o iterator fazendo a operacao da função)
map(FUNCAO A SER UTILIZADA, ITERATOR A SER MAPEADO)
"""

from functools import partial


def print_iter(iter):
    print(*list(iter), sep="\n")
    print()


produtos = [
    {"nome": "p1", "preco": 20},
    {"nome": "p2", "preco": 10},
    {"nome": "p3", "preco": 30},
]

novos_produtos = [{**p, "preco": 123} for p in produtos]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem)


aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

novos_produtos = [{**p, "preco": aumentar_dez_porcento(p["preco"])} for p in produtos]


def muda_preco_produtos(produto):
    return {**produto, "preco": aumentar_dez_porcento(produto["preco"])}


novos_produtos1 = map(muda_preco_produtos, produtos)

print("padrão")
print_iter(produtos)
print_iter(novos_produtos)


print("map")
print_iter(produtos)
print_iter(list(novos_produtos1))

# Triplicando valores com map
print(list(map(lambda x: x * 3, [1, 2, 3, 4])))
