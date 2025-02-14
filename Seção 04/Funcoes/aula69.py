"""
Escopo de funções em Python

Escopo significa o local onde as variáveis globais e locais se encontram.
Escopo global é o escopo onde todo o codigo é alcançavel.
Escopo local limitado ande podem ser manipulados

A palavra global serve para manipular uma variavel global dentro de uma funcao
"""

# variavel está acessivel de fora para dentro das demais, mas não de dentro para fora por exemplo de uma funcao para fora dela ou para outra dentro da mesma
# de global para fora, definindo a palavra global a uma variavel você pode manipular essa variavel global dentro de uma funcao
x = 1

def escopo():
    # global x
    x = 10
    def outra_funcao():
        # global x
        # x = 11
        y = 2
        print(x, y)
    outra_funcao()
    # print(x)

# print(x)
escopo()