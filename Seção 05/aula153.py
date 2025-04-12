"""
Método especial __call__
callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz a instância de uma
classe "callable".
"""


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    # O método especial __call__ em Python permite que uma instância de uma classe
    # seja chamada como uma função. Isso significa que, ao implementar o método
    # __call__ dentro de uma classe, você pode invocar suas instâncias como se fossem funções
    def __call__(self, nome):
        print(nome, "esta chamando", self.phone)
        return 123


call = CallMe("9912503")
call("Ciclano")

# Neste exemplo, a instância obj da classe MinhaClasse
# é chamada como uma função com o argumento 5,
# e o método __call__ é executado, retornando a soma
# do valor armazenado na instância (10) com o argumento (5).
# O método __call__ é útil em várias situações,
# como na criação de APIs claras e convenientes,
# na implementação de decoradores baseados em
# classes e no padrão de design Strategy
