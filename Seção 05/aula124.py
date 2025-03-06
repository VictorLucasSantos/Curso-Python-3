"""
Mantendo estados da classe
"""


class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} já está filmando")
            return

        print(f"{self.nome} está filmando")
        self.filmando = True

    def para_de_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando")
            return

    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar pois já está filmando")
            return

        print(f"{self.nome} está fotografando")


Sony = Camera("Sony")
Canon = Camera("Canon")

Sony.filmar()
Canon.filmar()
Sony.fotografar()
