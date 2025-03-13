"""Classes decoradoras (Decorator classes)"""


# Criando uma classe para ser executavel
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador

        return interna


# utilizando a classe como um decorador
@Multiplicar(2)
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
