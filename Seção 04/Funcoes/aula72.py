"""
Exercicios com funções

Crie uma funcao que multiplica todos os argumentos não nomeados recebidos

Retorne o total para uma variavel e mostre o valor da variavel

Crie uma funcao fala se um numero é impar ou par.
Retorne se o numero é ímpar ou par.

"""

def multiplica(*args:int):
    total = 1
    for arg in args:
        total *= arg
        # print()
    return total

def par_ou_impar(numero:int):
    if numero % 2 == 0:
        return f'{numero} é Par'
    return f'{numero} é Ímpar'

print(multiplica(10, 2, 3, 4, 5))

print(par_ou_impar(1))

print(par_ou_impar(2))