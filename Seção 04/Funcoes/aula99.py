"""
Introdução a pacotes (packages)

aula99_package é a pasta  e modulo o módulo em si
Que chamando assim seria da pasta aula99_package importe o "modulo especificado"
"""

from sys import path

import aula99_package.modulo
from aula99_package import modulo

# from aula99_package.modulo import *
from aula99_package.modulo import soma

print(*path, sep="\n")
print(soma(1, 3))


"""
Fazendo dessa forma ocorre o erro por conta que o primeiro modulo está fazendo uma importação também 
e o ponto de vista do python é de pacotes/modulos dentro da mesma pasta mas não posteriores como o exemplo
(porém é possivel manipular o PYTHONPATH)
"""
from aula99_package.modulo import soma

print(__name__)

"""
Podemos acessar um modulo diretamente pelo pacote fazendo a importação dos modulos no arquivo do __init__
"""
import aula99_package

print(aula99_package.dobra(2))
