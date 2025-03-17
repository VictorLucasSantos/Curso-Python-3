"""
dataclasses - O que são dataclasses?
O módulo dataclasses fornece um decorador e funções para criar métodos como
__init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
usuário.
Em resumo: dataclasses são syntax sugar para criar classes normais.
Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
doc: https://docs.python.org/3/library/dataclasses.html
"""

from dataclasses import dataclass, asdict, astuple, field


@dataclass  # init=False desativa o metodo init para poder iniciar na classe padrão
class Pessoa:
    nome: str
    sobrenome: str

    # def __post_init__(self):
    #     self.nome_completo = f"{self.nome} {self.sobrenome}"

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = " ".join(sobrenome)


@dataclass(
    frozen=True
)  # não permite que faça alterações na classe sendo como uma constante
class Cliente:
    nome: str
    sobrenome: str

    # def __post_init__(self):
    #     self.nome_completo = f"{self.nome} {self.sobrenome}"

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = " ".join(sobrenome)


@dataclass  # init=False desativa o metodo init para poder iniciar na classe padrão
class PessoaDiferente:
    nome: str = "My"
    sobrenome: str = "Surname"
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)

    # def __post_init__(self):
    #     self.nome_completo = f"{self.nome} {self.sobrenome}"

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = " ".join(sobrenome)


if __name__ == "__main__":
    p1 = Pessoa("Luiz", "Otavio")
    p2 = Pessoa("Luiz", "Otavio")
    print(p1 == p2)
    c = Cliente("Fulano", "Qualquer")
    print(c)
    # c.nome = "TESTE"
    # Cliente(nome='Fulano', sobrenome='Qualquer')
    # Traceback (most recent call last):
    # File "d:\GIT\Curso-Python-3\Seção 05\aula159.py", line 60, in <module>
    #     c.nome = "TESTE"
    #     ^^^^^^
    # File "<string>", line 4, in __setattr__
    # dataclasses.FrozenInstanceError: cannot assign to field 'nome'
    print(asdict(c))  # convertendo a classe para dicionário
    print(astuple(c))  # convertendo a classe para uma tupla
    P = PessoaDiferente()
    print(P)
