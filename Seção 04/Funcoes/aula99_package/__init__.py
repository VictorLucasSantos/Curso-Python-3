print()
"""
Podemos acessar um modulo diretamente pelo pacote fazendo a importação dos modulos no arquivo do __init__
"""

from .modulo import *
from .modulo_b import *


def dobra(x):
    return x * 2
