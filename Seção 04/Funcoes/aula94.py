#Try, except else e finally parte 2

try:
    print('INICIA')
    8 / 0
except Exception as e:
    print(e)
else:
    print("Nenhuma exceção ocorreu")
finally:
    print('FINALIZA')
    
"""
INICIA
division by zero
FINALIZA

"""