import json

CAMINHO_ARQUIVO = r"D:\GIT\Curso-Python-3\Seção 05\aula127.json"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p = Pessoa("João", 33)
p1 = Pessoa("helena", 21)
p2 = Pessoa("Joana", 11)
tds = [p.__dict__, p1.__dict__, p2.__dict__]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, "w") as arq:
        json.dump(tds, arq, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    fazer_dump()
