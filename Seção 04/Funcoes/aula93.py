#Try, except else e finally parte 1

a = 18
b = 0

# Trata execoes de acordo com a classe
try:
    c = a / b
except (NameError, ZeroDivisionError) as e:
    print(f'Erro: {e}')
else:
    print('Nenhuma exceção ocorreu')
finally:
    print('Sempre executado')

# Trata qualquer tipo de exceção
try:
    c = a / b
except Exception as e:
    print(f'Erro: {e} classe {e.__class__.__name__}')
else:
    print('Nenhuma exceção ocorreu')
finally:
    print('Sempre executado')