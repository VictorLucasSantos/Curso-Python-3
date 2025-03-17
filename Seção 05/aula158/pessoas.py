import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta = contas.Conta | None

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.nome!r}, {self.idade!r})"
        return f"{class_name}{attrs}"


if __name__ == "__main__":
    cl = Cliente("Qualquer", 30)
    cl.conta = contas.ContaCorrente(11, 22, 0, 0)
    print(cl)
    print(cl.conta)
