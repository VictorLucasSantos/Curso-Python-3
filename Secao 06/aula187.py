"""
sys.argv - Executando arquivos com argumentos no sistema
"""

import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

print(argumentos)
print(qtd_argumentos)

if qtd_argumentos < 1:
    print("Informe argumentos")
else:
    try:
        print(f"Você passou argumentos {argumentos[1:]}")
        print(f"Faça alguma coisa com {argumentos[1]}")
        print(f"Faça outra coisa com {argumentos[2]}")
    except IndexError:
        print("Faltam argumentos")
