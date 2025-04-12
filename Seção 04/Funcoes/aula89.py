# dir, hasattr e getattr

string = 'José'
metodo = 'upper'

# Otendo metodos de uma string
print(dir(string))

# Verificando se o metodo passado existe na string
print(hasattr(string, 'upper'))

# Obtendo o metodo
print(getattr(string, 'upper'))

if hasattr(string, metodo):
    print(f'Existe {metodo} na string')
    print(getattr(string, metodo))
else:
    print(f'Nao existe {metodo} na string')

