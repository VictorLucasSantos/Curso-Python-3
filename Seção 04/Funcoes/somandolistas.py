"""
Considerando duas listas de inteiros ou floats(lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma vai considerar o tamanho da menor

EX:
listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]
================resultado
lista_soma = [2, 4, 6, 8]
"""

listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]

lista_soma = []
for i in range(len(listaB)):
    lista_soma.append(listaB[i] + listaA[i])
print(lista_soma)


lista_soma = []
for i, _ in enumerate(listaB):
    lista_soma.append(listaB[i] + listaA[i])
print(lista_soma)

print(list([x + y for x, y in zip(listaA, listaB)]))
