"""super() e a sobreposição de membros - Python Orientado a Objetos
Classe principal (Pessoa)
  -> super class, base class, parent class
Classes filhas (Cliente)
  -> sub class, child class, derived class
"""

"""
o super() é usado para chamar métodos da classe pai dentro da classe filha.
Isso é útil quando você quer estender o comportamento de um método
da classe pai sem precisar copiar todo o código.
"""


class MinhaString(str):
    # sobrescrevendo o metodo upper
    def upper(self):
        print("CHAMOU UPPER")
        retorno = super().upper()
        print("APÓS UPPER")
        return retorno


string = MinhaString("")
# print(string.upper())


class A(object):
    atributo_a = "valor a"

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print("A")


class B(A):
    atributo_b = "valor b"

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print("B")


class C(B):
    atributo_c = "valor c"

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        A.metodo(self)
        B.metodo(self)
        print("C")


# METHOD RESOLUTION ORDER
# Ordenação de resolução de metodos a partir de cada classe com a sua herança
print(C.mro())
print(B.mro())
print(A.mro())
# c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
# c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
