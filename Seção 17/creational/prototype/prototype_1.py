"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""

from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class Address(StringReprMixin):
    def __init__(self, street: str, number: str):
        self.street = street
        self.number = number


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: list[Address] = []

    def add_address(self, address: Address):
        self.addresses.append(address)

    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    from copy import deepcopy

    pessoa = Person("Qualquer", "Um")
    endereco_pessoa = Address("Lá", "não sei aonde")
    pessoa.add_address(endereco_pessoa)

    outra_pessoa = pessoa.clone()
    outra_pessoa.firstname = "Outra"
    print(pessoa)
    print(outra_pessoa)
