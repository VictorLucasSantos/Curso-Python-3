"""
Relações entre classes: associação, agregação e composição
Composição é uma especialização da agregação.
Mas nela, quando o objeto "pai" for apagado, todas
as referências dos objetos filhos também são
apagadas.
"""


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        return self.enderecos.append(Endereco(rua, numero))

    def inserir_enderecos_externo(self, endereco):
        return self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    # ao deletar a classe
    def __del__(self):
        print("APAGANDO", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    # ao deletar a classe
    def __del__(self):
        print("APAGANDO", self.rua, self.numero)


cliente = Cliente("Maria")
cliente.inserir_enderecos("Av Brasil", 54)
cliente.inserir_enderecos("Av Paulista", 33)
endereco_externo = Endereco("Av 25 de Março", 70)
cliente.inserir_enderecos_externo(endereco_externo)
cliente.listar_enderecos()

## removendo cliente manualmente
del cliente

# aidna tendo acesso a endereço externo
print(endereco_externo.rua, endereco_externo.numero)
print(
    "-" * 10,
    "FIM CÓDIGO",
    "-" * 10,
)
