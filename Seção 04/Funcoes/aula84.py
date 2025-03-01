"""
List comprehension em Python
É uma forma rápida para criar listas a partir de iteráveis.
print(list(range(10)))
"""

# O que é feito internamente?
lista = []
# Cria um range de 0 a 9
for num in range(10):
    # inclui o numero na lista
    lista.append(num)
print(lista)

# Adiciona o numero do range na lista
lis = [numero for numero in range(10)]
print(lis)

# Adiciona o numero 1 na quantidade do range na lista
li = [1 for numero in range(10)]
print(li)


# MAPEAMENTO COM LIST COMPREHENSION
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# novos_produtos = [ produto['nome'] for produto in produtos]
novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} for produto in produtos]

novos_produtos1 = [{**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos]
print(novos_produtos)
print(*novos_produtos, sep='\n')
print()
print(novos_produtos1)
print(*novos_produtos1, sep='\n')

# FILTRO COM LIST COMPREHENSION
novos_produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} 
    for produto in produtos
    if produto['preco'] > 20
]
print()
print(novos_produtos2)
print(*novos_produtos2, sep='\n')