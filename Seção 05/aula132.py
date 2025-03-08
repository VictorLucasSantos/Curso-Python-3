"""# @property + @setter - getter e setter no modo Pythônico
como getter
p/ evitar quebrar código cliente
p/ habilitar setter
p/ executar ações ao obter um atributo
Atributos que começar com um ou dois underlines
não devem ser usados fora da classe.
🐍🤓🤯🤯🤯🤯
"""


class Caneta:
    def __init__(self, cor):
        # ATRIBUTOS QUE COMEÇAR COM UM OU DOIS UNDERLINES NÃO DEVEM SER USADOS FORA DA CLASSE
        self._cor = cor

    # obter o valor
    @property
    def cor(self):
        print("PROPERTY")
        return self._cor

    # criando um setter com a property cor para definir o valor
    @cor.setter
    def cor(self, cor):
        print("SETTER COR", cor)
        self._cor = cor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, cor_tampa):
        print("SETTER COR_TAMPA", cor_tampa)
        self._cor_tampa = cor_tampa


c = Caneta("Azul")
# c.cor = "Rosa"

print(c.cor)
c.cor_tampa = "Azul"
print(c.cor_tampa)
