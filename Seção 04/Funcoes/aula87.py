"""
isinstance - saber se objeto é de determinado tipo
"""
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Beltrano'}
]

# Iterando sobre a lista para poder verificar qual é o tipo set
for item in lista:
    isinstance(item, set)
    # print(item, isinstance(item, set))
    # a False
    # 1 False
    # 1.1 False
    # True False
    # [0, 1, 2] False
    # (1, 2) False
    # {0, 1} True
    # {'nome': 'Beltrano'} False
    if isinstance(item, set):
        print('SET')
        item.add(5)
        
    elif isinstance(item, str):
        print('STR')
        print(item.upper())
        # STR
        # A
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 5)
        # NUM
        #1 5
    else:
        print('OUTRO')