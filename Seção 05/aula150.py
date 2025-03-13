"""
Context Manager com função - Criando e Usando gerenciadores de contexto
"""

from contextlib import contextmanager
from os import path

LOCAL_ARQUIVO = path.dirname(__file__) + "\\aula150.txt"


# Funciona da mesma forma de uma classe criada como context manager porém com um decorator
@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding="UTF8")
        yield arquivo
    except Exception as e:
        print(f"Ocorreu o erro: {e}")
    finally:
        print("Fechando arquivo")
        arquivo.close()


with my_open(LOCAL_ARQUIVO, "w") as f:
    for i in range(0, 11):
        f.write(f"Linha {i}\n")
    print("WITH", f)
