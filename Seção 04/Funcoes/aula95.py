"""
raise - Lancar uma exceção
"""

#Levantando exceções
def deve_ser_int_ou_float(parametro):
    tipo = type(parametro)
    if not isinstance(parametro, (int, float)):
        raise TypeError(f'"{parametro}" deve ser int ou float. Seu tipo atual eh: {tipo.__name__}')
    
def nao_aceito_zero(parametro):
    if parametro == 0:
        raise ValueError(f'"{parametro}" nao pode ser zero')

def divide(a, b):
    deve_ser_int_ou_float(a)
    deve_ser_int_ou_float(b)
    nao_aceito_zero(a)
    nao_aceito_zero(b)

    return a / b

print(divide(0, 1))

print(divide(2, 0))

print(divide('2', '2'))