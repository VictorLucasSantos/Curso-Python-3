# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=[]):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


def adiciona_clientes1(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes("luiz")
adiciona_clientes("Joana", cliente1)
adiciona_clientes("Fernando", cliente1)
cliente1.append("Edu")

cliente2 = adiciona_clientes("Helena")
adiciona_clientes("Maria", cliente2)

cliente3 = adiciona_clientes("Moreira")
adiciona_clientes("Vivi", cliente3)

print(cliente1)
print(cliente2)
print(cliente3)

print()

cliente1 = adiciona_clientes1("luiz")
adiciona_clientes1("Joana", cliente1)
adiciona_clientes1("Fernando", cliente1)
cliente1.append("Edu")

cliente2 = adiciona_clientes1("Helena")
adiciona_clientes1("Maria", cliente2)

cliente3 = adiciona_clientes1("Moreira")
adiciona_clientes("Vivi", cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
