# Introdução a POO Programação Orientada a Objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))


class Pessoa: ...


# Criando uma instância da classe Pessoa
p = Pessoa()
# Inicializando atributos
p.nome = "Qualquer"
p.sobrenome = "Um"

# Criando uma nova instância da classe
p2 = Pessoa()
p2.nome = "Qualquer"
p2.sobrenome = "Um"

print(p.nome)
print(p.sobrenome)
