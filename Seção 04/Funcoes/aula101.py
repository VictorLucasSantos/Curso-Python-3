"""
EXERCICIO
"""


def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def executar(*args):
        return funcao(*args)

    return executar


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(1, 5))
print(multiplica_por_dez(10, 5))
