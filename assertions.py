from calculadora import soma

try:
    soma('10', 20)
except AssertionError as e:
    print(f'Erro: {e}')