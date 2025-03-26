"""
csv.writer e csv.DictWriter para escrever em CSV
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
"""

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "aula180.csv"

CAMINHO_CSV_1 = Path(__file__).parent / "aula180_1.csv"

lista_clientes = [
    {"Nome": "Luiz Otávio", "Endereço": "Av 1, 22"},
    {"Nome": "João Silva", "Endereço": 'R. 2, "1"'},
    {"Nome": "Maria Sol", "Endereço": "Av B, 3A"},
]

with open(CAMINHO_CSV, "w") as f:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(f)

    escritor.writerow(nome_colunas)

    for cliente in lista_clientes:
        print(cliente.values())
        escritor.writerow(cliente.values())

with open(CAMINHO_CSV_1, "w") as f:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(f, fieldnames=nome_colunas)

    escritor.writerow()

    for cliente in lista_clientes:
        escritor.writerow(cliente.values())
