""" Introdução ao método __init__ (inicializador de atributos)
"""


class Pessoa:
    def __init__(self, nome, sobrenome):
        # Inicializando atributos
        self.nome = nome
        self.sobrenome = sobrenome


p = Pessoa("Qualquer", "Um")

p2 = Pessoa("Qualquer", "Outro")

print(p.nome)
print(p.sobrenome)
print(p2.nome)
print(p2.sobrenome)
