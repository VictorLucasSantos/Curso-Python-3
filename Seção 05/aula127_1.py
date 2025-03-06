import json

from aula127 import CAMINHO_ARQUIVO, Pessoa, fazer_dump


with open(CAMINHO_ARQUIVO, "r") as f:
    pessoas = json.load(f)

    print(Pessoa(**pessoas[0]).nome)
    print(Pessoa(**pessoas[1]).nome)
    print(Pessoa(**pessoas[2]).nome)
