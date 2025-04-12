"""
Complemento de entendimento de uso das funções lambda
"""

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

# A funcao lamba aqui esta sendo representada pela funcao a cima soma
print(
    executa(
        lambda x, y: x + y,
        2, 3
        ),
    executa(soma, 2, 3),
    soma(2, 3)
    )

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# A funcao lamba aqui esta sendo representada pela funcao a cima cria_multiplicador
# EXEMPLO SOMENTE PARA ENTENDIMENTO, NÃO UTILIZAR EXPRESSOES COMPLEXAS PARA SOMENTE UMA LINHA
duplica = executa(
    # uma funcao que recebe o numero e retorna uma funcao que recebe o multiplicador e multiplica o numero
    lambda m: lambda n: n * m,
    2
)

# Também é possivel passar *args para funcoes lambda
print(executa(lambda *args: sum(args), 1, 2, 3))