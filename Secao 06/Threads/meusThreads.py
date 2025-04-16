from threading import Thread, Lock


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):

        if self.estoque < quantidade:
            print("Não temos ingressos suficientes")
            return
        self.estoque -= quantidade
        print(f"Você comprou {quantidade} ingressos. Ainda temos {self.estoque}")


if __name__ == "__main__":
    ingressos = Ingressos(10)
    for i in range(20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
        ingressos.comprar(i)
    print(ingressos.estoque)
