"""
List Comprehension com mais de um for Ex:
"""

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
        
# Mesma operação realizada a cima
lista1 = [(x, y) for x in range(3) for y in range(3)]

print(lista)
print()
print(lista1)