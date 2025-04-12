# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {"nome": "Luiz", "nota": "A"},
    {"nome": "Letícia", "nota": "B"},
    {"nome": "Fabrício", "nota": "A"},
    {"nome": "Rosemary", "nota": "C"},
    {"nome": "Joana", "nota": "D"},
    {"nome": "João", "nota": "A"},
    {"nome": "Eduardo", "nota": "B"},
    {"nome": "André", "nota": "A"},
    {"nome": "Anderson", "nota": "C"},
]


# Para poder agrupar corretamente um iteravel com groupby deve sempre ser orndenado
# Pois se não estiver ordenado agrupa o mesmo valor mais de uma vez
def ordena(aluno):
    return aluno["nota"]


# ordenando
alunos_agrupados = sorted(alunos, key=ordena)

grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
