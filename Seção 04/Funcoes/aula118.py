"""
Problemas dos parâmetros mutáveis em funções Python
"""


# Não utilizar variáveis mutaveis em parametros default pois o python não reinicializa ele ao ser executado novamente
# quando a função é chamada pela primeira vez com adiciona_clientes("luiz"),
# a lista padrão (lista=[]) é criada uma única vez, e não a cada chamada da função.
# Então, quando você chama adiciona_clientes("Ciclano", cliente), a lista ainda é a mesma usada na chamada anterior.
# Isso significa que todos os valores vão sendo acumulados.
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista


# Forma correta de tratar esse tipo de situação
def adiciona_clientes1(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente = adiciona_clientes("luiz")
adiciona_clientes("Ciclano", cliente)
adiciona_clientes("Ciclano2", cliente)
adiciona_clientes("Ciclano3", cliente)
print(cliente)

print()

cliente1 = adiciona_clientes1("luiz")
adiciona_clientes1("Beltrano", cliente1)
adiciona_clientes1("Beltrano1", cliente1)
adiciona_clientes1("Beltrano2", cliente1)
print(cliente1)
