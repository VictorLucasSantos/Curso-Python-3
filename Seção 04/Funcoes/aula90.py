# Generator expression, Iteravles e Iterators
import sys

iterable = ['Eu', 'Tenho', '__iter__']
# Iterator  somene passa o proximo item e não tem conhecimento do iteravel e quando chega no fim da lista ele retorna uma exceção "StopIteration" 
iterator = iterable.__iter__()
iterator = iter(iterable) #Faz a mesma coisa do __iter__()

print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

# GENERATOR
# Não salva todos os valores na memoria de uma vez, ele gera os valores conforme eles forem solicitados
lista = [n for n in range(100000)]
generator = (n for n in range(100000))

print(f'O tamanho armazenado é : {sys.getsizeof(generator)}')
# O tamanho armazenado é : 192
print(f'O tamanho armazenado é : {sys.getsizeof(lista)}')
# O tamanho armazenado é : 800984

# Para obter os valores do generator utilizamos o next
print(next(generator))
print(next(generator))

for n in generator:
    print(n)