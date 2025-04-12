"""
Métodos de classe + factories (fábricas)
São métodos onde "self" será "cls", ou seja,
ao invés de receber a instância no primeiro
parâmetro, receberemos a própria classe.
"""


class Pessoa:
    ano = 2025  # Atributo da classe (property)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # utilizando @classemthod o metodo se torna um metodo da classe e não da instância
    def metodo_de_classe(cls):  # cls referencia a classe
        print("Hello")

    @classmethod  # Criando um metodo para criar uma instância de pessoa com 50 anos de idade (exemplo de uso)
    def criar_com_50_anos(cls, nome):
        # NÃO EXISTE ACESSO A SELF, POIS MANIPULA A CLASSE E NÃO AINDA A INSTÂNCIA
        return cls(nome, 50)

    @classmethod  # Criando um metodo para criar uma instância de pessoa sem nome
    def criar_sem_nome(cls, nome, idade):
        return cls("Anônima", idade)


p = Pessoa("Jonas", 34)
p1 = Pessoa.criar_com_50_anos("Helena")
p2 = Pessoa.criar_sem_nome(idade=20)
print(vars(p))
print(vars(p1))
print(vars(p2))
