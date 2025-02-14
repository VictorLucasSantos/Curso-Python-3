"""
Valores padrão para parâmetros 

Ao definir uma funcao, os parametros podem ter valores padrão. Se nenhum argumento for fornecido para o parâmetro, o valor padrão será usado.
"""

def somar(a=0, b=0, c=0):
    print(a + b + c)


somar(1, 2, 3)
somar(1, 2)
somar(100, 200, 300)

# verifica se o valor foi enviado ou não por conta que o 0, vazio é sempre falso e NoneType não é nada
def soma(a=0, b=0, c=None):
    if c is not None:
        print(f'{a + b + c}', a + b + c)
    else:
        print(f'{a + b}', a + b)


somar(1, 2, 3)
somar(1, 2)
somar(100, 200, 300)