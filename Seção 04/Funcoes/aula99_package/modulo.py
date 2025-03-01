"""
Introdução a pacotes (packages)

aula99_package é a pasta  e modulo o módulo em si
Que chamando assim seria da pasta aula99_package importe o "modulo especificado"
"""

# Caso seja feito a importação de tudo e quiser especificar quais variaveis podem ser importadas do módulo
__all__ = ["variavel", "soma"]

#  Dessa forma não ocorreria problema com o a execução do pacote em outros mains que fossem para fora da pasta
from .modulo_b import exibe

# from aula99_package.modulo_b import exibe

# from modulo_b import exibe


var = "Algo"
nova_var = "Novo"


def soma(x, y) -> None:
    return x + y
