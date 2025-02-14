"""
Crie funções que duplicam, triplicam e quadruplicam o numero recebido como parametro
"""

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplica = cria_multiplicador(2)
triplica = cria_multiplicador(3)
quadruplica = cria_multiplicador(4)

print(duplica(2, 2))
print(triplica(3, 3))
print(quadruplica(4, 4))