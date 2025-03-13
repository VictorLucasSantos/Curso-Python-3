# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self, other) - self < other
# __le__(self, other) - self <= other
# __gt__(self, other) - self > other
# __ge__(self, other) - self >= other
# __eq__(self, other) - self == other
# __ne__(self, other) - self != other
# __add__(self, other) - self + other
# __sub__(self, other) - self - other
# __mul__(self, other) - self * other
# __truediv__(self, other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y, z="String"):
        self.x = x
        self.y = y
        self.z = z

    # Representação de como seria a classe
    def __repr__(self):
        # utilizando x!r para trazer a representação do tipo correto do objeto
        return f"{type(self).__name__} x({self.x!r}) y({self.y!r}) z({self.z!r})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Metodo criado para poder somar com outra classe por exemplo podendo fazer (p3 = p1 + p2)
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    # Metodo de comparação de objetos como o (print("Print é maior que p1", p2 > p2), print("Print é maior que p2", p1 > p2))
    def __gt__(self, other):
        resultado_self = self.x > self.y
        resultado_other = other.y > other.x
        return resultado_self > resultado_other


# p1 = Ponto(x=1, y=2)
# p2 = Ponto(x=978, y=978)
# print(p1)
# print(p2)
# print(repr(p2))

if __name__ == "__main__":
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)
    p3 = p1 + p2
    print(p3)
    print("Print é maior que p2", p1 > p2)
    print("Print é maior que p1", p2 > p2)
