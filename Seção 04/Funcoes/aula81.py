"""
Funcao lambda em Python
são funções anonimas que contém apenas uma linha, devendo tudo estar dentro de uma única expressão.
"""

lista = [12, 27, 31, 49, 52]
# Ordena a lista
lista.sort()

list = [
    {'nome': 'Qualquer', 'sobrenome': 'Um'},
    {'nome': 'Zé', 'sobrenome': 'Ramalho'},
    {'nome': 'Maria', 'sobrenome': 'Silva'},
]

def exibir(lista):
    for item in lista:
        print(item) 
    print()

# Em exemplo de uso da funcao lambda existe uma lista a ser ordenada
list1 = sorted(list, key=lambda item: item['nome']) #É ordenado pelo campo retornado
list2 = sorted(list, key=lambda item: item['sobrenome']) #É ordenado pelo campo retornado

# exibindo lista ordenada por nome e sobrenome
exibir(list1)
exibir(list2)