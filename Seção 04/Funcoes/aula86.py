"""
Dictionary Comprehension e Set comprehension
"""
item = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dict_item = {
    chave: valor
    # Verifica se o valor não é int ou float para poder utilizar o metodo upper que é de str
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in item.items()
    if chave != 'categoria'
}

print(dict_item)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave : valor
    for chave, valor in lista
}

# SET comprehension

s1 = {i for i in range(10)}

# Mesmo exemplo a cima
s2 = set(range(10))

s3 = {i ** 2 for i in range(10)}

print(s1)
print(s2)
print(s3)