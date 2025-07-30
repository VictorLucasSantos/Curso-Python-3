"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""


class Order:
    def __init__(self, total, discount):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self.total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)
