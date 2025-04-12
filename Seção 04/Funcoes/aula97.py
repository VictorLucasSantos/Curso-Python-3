"""
Modularização

O primeiro módulo executado chama-se __main__.py

Voce pode importar módulos inteiros ou parte em outros módulos

Python conhece as pastas aonde o __main__ está e as pastar abaixo dele

Ele não conhece todos os módulos e pacotes presentes no caminhos de sys.path

################### IMPORTANTE #########################

Não é possivel fazer importações para pastas posteriores somente pastas, somente pastas a frente dele

Qualquer busca de modulos em outros locais o sys.path() deve ser adicionado como no exemplo
########################################################
"""
import sys


# Exemplo de importacao de modulo separado em outra pasta
try:
    sys.path.append('D:\\')
except ModuleNotFoundError:
    ...

import modulo_python

import aula97_m
from aula97_m import qualquer, Variavel

print('Esse modulo se chama',__name__)

print(*sys.path, sep='\n')

print(qualquer)
print(Variavel)