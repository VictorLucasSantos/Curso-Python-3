"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod


class Pizza(ABC):
    """classe abstrata"""

    def prepare(self):
        self.add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingredients(self):
        pass

    def hook_after_add_ingredients(self):
        pass

    def cut(self):
        print(f"{self.__class__.__name__}: Cortando pizza.")

    def serve(self):
        print(f"{self.__class__.__name__}: Servindo pizza.")

    @abstractmethod
    def add_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass


class AModa(Pizza):
    def add_ingredients(self):
        print(
            f"{self.__class__.__name__} - adicionando ingredientes: Presunto, queijo, goiabada"
        )

    def cook(self):
        print(f"{self.__class__.__name__}oda - cozinhando por 45min no forno a lenha")


class Veg(Pizza):
    def add_ingredients(self):
        print(f"veg - adicionando ingredientes: veganos")

    def cook(self):
        print(f"veg - cozinhando por 5min no forno a comum")


if __name__ == "__main__":
    a_moda = AModa()
    a_moda.prepare()
    print()
    veg = Veg()
    veg.prepare()
