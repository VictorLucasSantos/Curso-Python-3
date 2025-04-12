# json.dump e json.load com arquivos

import json
import os

NOME_ARQUIVO = "aula177.json"

CAMINHO_ABSOLUTO_ARQUIVO = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)

# Caminho do arquivo
print(__file__)

print(os.path.dirname(__file__))

print(CAMINHO_ABSOLUTO_ARQUIVO)


movie = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None,
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, "w") as f:
    json.dump(movie, f, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, "r") as f:
    print(json.load(f))
