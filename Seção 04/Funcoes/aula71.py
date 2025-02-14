"""
args - Argumentos não nomeados

* - *args (empacotamento e desempacotamento)
"""

# Desempacotamento
x, y, *resto = 1, 2, 3, 4

print(x, y, resto)

def soma1(x, y, z):
    return x + y + z

# Digamos que temos 3 argumentos para essa funcao e queremos empacota-los que é uma tupla 
soma1(1, 2, 3)

# a forma correta seria para empacotar os parametros dentro de uma tupla
def soma2(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# utilizando o sum nativo do python ele faz o desempacotamento para fazer a soma
print(sum((1, 2, 3)))
numeros = 1, 2, 3 
print(sum(numeros))

# desempacotando manualmente
print(*numeros)