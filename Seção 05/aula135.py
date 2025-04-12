"""
Relações entre classes: associação, agregação e composição
Associação é um tipo de relação onde os objetos
estão ligados dentro do sistema.
Essa é a relação mais comum entre objetos e tem subconjuntos
como agregação e composição (que veremos depois).
Geralmente, temos uma associação quando um objeto tem
um atributo que referencia outro objeto.
A associação não especifica como um objeto controla
o ciclo de vida de outro objeto.
"""


class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print("".format(produto.nome, produto.preco))
        print()

    def inserir_produtos(self, *produtos):
        # for produto in produtos:
        #     self._produtos.append(produto)
        # self._produtos.extend(produtos)
        self._produtos += produtos


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()

p1, p2, p3 = (
    Produto("Lápis", 1),
    Produto("Borracha", 0.5),
    Produto("Apontador", 0.75),
)

carrinho.inserir_produtos(p1, p2, p3)
