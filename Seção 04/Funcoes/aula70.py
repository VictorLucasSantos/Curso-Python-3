"""
Retorno das funcoes (return)
"""

# variavel = print('Oi')
# variavel é com valor de retorno nome por conta que não tem retorno
# print(variavel)

def soma1(a, b):
    # após o return não é executado o resto da função
    return a + b
    print('Oi')
    
def soma2(a, b):
    # após o return não é executado o resto da função então deve ser feito dessa forma
    print('Oi')
    return a + b

def soma3(a, b):
    if b > 10:
        return 10, 20
    return a + b

print(soma1(10, 20))
print(soma2(10, 20))
print(soma3(11, 20))