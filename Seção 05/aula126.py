"""
__dict__ e vars para atributos de instância
"""


class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


Pessoa1 = Pessoa("Beltrano", 20)
print(Pessoa1.__dict__)
Pessoa1.__dict__["outra"] = "coisa"
print(Pessoa1.__dict__)
print()
print(vars(Pessoa1))
print(Pessoa1.get_ano_nascimento())
print(Pessoa1.outra)

# {'nome': 'Beltrano', 'idade': 20}
# {'nome': 'Beltrano', 'idade': 20, 'outra': 'coisa'}

# {'nome': 'Beltrano', 'idade': 20, 'outra': 'coisa'}
# 2005
# coisa


dados = {"nome": "Beltrano", "idade": 20}
qualquer = Pessoa(**dados)
print(qualquer.__dict__)
