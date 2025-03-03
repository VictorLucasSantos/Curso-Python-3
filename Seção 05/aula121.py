"""
Metodos em instâncias de classes Python
Classe - Molde (geralmente sem dados)
Instância da classe (objeto) - Tem os dados
Uma classe pode gerar várias instâncias.
self é  a própria classe
"""


class Carro:
    def __init__(self, nome="Sei lá"):
        self.nome = nome

    def acelerar(self):
        # utilizando self.nome para mostrar a instância que está sendo utilizada
        print(f"{self.nome} está acelerando...")


fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()

print("#" * 10)

celta = Carro("Celta")
print(celta.nome)
celta.acelerar()
