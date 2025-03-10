"""
Atributos de classe
"""


class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


Pessoa1 = Pessoa("Beltrano", 20)
Pessoa2 = Pessoa("Ciclano", 30)
print(Pessoa.ano_atual)
print(Pessoa1.get_ano_nascimento())
print(Pessoa2.get_ano_nascimento())
