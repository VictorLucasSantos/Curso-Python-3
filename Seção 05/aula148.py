"""
__new__ e __init__ em classes Python
__new__ é o método responsável por criar e
retornar o novo objeto. Por isso, new recebe cls.
__new__ ❗️DEVE retornar o novo objeto❗️
__init__ é o método responsável por inicializar
a instância. Por isso, init recebe self.
__init__ ❗️NÃO DEVE retornar nada (None)❗️
object é a super classe de uma classe
"""


class A:
    # New é chamado antes do __init__ e é responsavel por criar a instância
    def __new__(cls, *args, **kwargs):
        print("Antes de criar a instancia")
        # criando a instancia
        instancia = super().__new__(cls)
        print("Depois de criar a instancia")
        # Antes de criar a instância
        return instancia

    def __init__(self, x):
        print("Sou o init")

    def __repr__(self):
        return f"{self.__class__.__name__}"


a = A()
print(a)
