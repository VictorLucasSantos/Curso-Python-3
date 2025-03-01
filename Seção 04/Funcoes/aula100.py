import copy
from dados import produtos

"""
copy, sorted, produtos.sort

Exercicios

Aumente os preços dos produtos a seguir em 10%

Gere novos_proudutos por deep copy (cópia profunda)
"""

novos_produtos = [
    {**p, "preco": round(p["preco"] * 1.1, 2)} for p in copy.deepcopy(produtos)
]

print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n")

"""
Ordene os produtos por nome decrescente (do maior para o menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), key=lambda p: p["nome"], reverse=True
)

print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n")

"""
Ordene os produtos por preco crescente (do menor para o maior)
gere produtos_ordenados_por_preco por deep copy (copia profunda)
"""
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p["preco"],
)

print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n")
