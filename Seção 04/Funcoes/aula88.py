"""
Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
Mutaveis [] {} set()
Imutaveis str, int, float, bool, tupl, dict, range(0, 10)
"""
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(nome, valor):
    return f'{nome} = {valor} falsy' if not valor else f'{nome} = {valor} truthy'

print(falsy('lista', lista))
print(falsy('dicionario', dicionario))
print(falsy('conjunto', conjunto))
print(falsy('tupla', tupla))
print(falsy('string', string))
print(falsy('inteiro', inteiro))
print(falsy('flutuante', flutuante))
print(falsy('nada', nada))
print(falsy('falso', falso))
print(falsy('intervalo', intervalo))