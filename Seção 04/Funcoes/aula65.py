"""
Introdução as funções (def) em Python
Funções são trechos de código que recebem parametros (argumentos) e podem retornar um valor especifico, por padrão retorna None (nada)
"""

def exibir():
    print('Oi')
    
# nesse caso vai informar o tipo do dado e mostrar em qual local da memoria está armazenado
print(exibir)

# nesse caso vai executar a funcao e retornar none pois não foi definido retorno para a mesma
print(exibir())

# criar uma funcao e atribuir parametros para a funcao, sem tipagem de dados
def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)

# criar uma funcao e atribuir tipagem de dados para os parametros
def imprimir1(a:int, b:int, c:int):
    print(a, b, c)

imprimir1(1, 2, 3)

# criar uma funcao e atrobuir valores default (padrao) para os argumentos
def imprimir2(a:int=1, b:int=2, c:int=3):
    print(a, b, c)

imprimir2()