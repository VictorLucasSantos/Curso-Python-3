"""
Json em Python é convertido quando importado para dicionário
Json somente suporta dados

###### NÃO SUPORTADO A JSON ######
ex: {1, 2 ,3}
"""

import json
import os

pessoa = {
    "nome": "Luiz Otávio 2",
    "sobrenome": "Miranda",
    "enderecos": [
        {"rua": "R1", "numero": 32},
        {"rua": "R2", "numero": 55},
    ],
    "altura": 1.8,
    "numeros_preferidos": (2, 4, 6, 8, 10),
    "dev": True,
    "nada": None,
}
PATH = os.path.dirname(__file__)

caminho = PATH + "\\aula117.json"
# with open(
#     caminho,
#     "w",
# ) as f:
#     json.dump(pessoa, f, indent=2, ensure_ascii=False)

with open(
    caminho,
    "r",
) as f:
    pessoa1 = json.load(f)
    print(pessoa1)
    print(type(pessoa1))
