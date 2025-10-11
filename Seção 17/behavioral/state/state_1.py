"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """context"""

    def __init__(self):
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        print("Tentando executar pending()")
        self.state.pending()
        print("Estado atual", self.state)
        print()

    def approve(self):
        print("Tentando executar approve()")
        self.state.approve()
        print("Estado atual", self.state)
        print()

    def reject(self):
        print("Tentando executar reject()")
        self.state.reject()
        print("Estado atual", self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pending(self):
        pass

    @abstractmethod
    def approve(self):
        pass

    @abstractmethod
    def reject(self):
        pass

    def __str__(self):
        return self.__class__.__name__


class PaymentPending(OrderState):

    def pending(self):
        print("Pagamento já pendente")

    def approve(self):
        self.order.state = PaymentApproved(self.order)
        print("Pagamento aprovado")

    def reject(self):
        self.order.state = PaymentRejected(self.order)
        print("Pagamento recusado")


class PaymentApproved(OrderState):

    def pending(self):
        self.order.state = PaymentPending((self.order))
        print("Pagamento pendente")

    def approve(self):
        print("Pagamento já aprovado")

    def reject(self):
        self.order.state = PaymentRejected(self.order)
        print("Pagamento recusado")


class PaymentRejected(OrderState):

    def pending(self):
        # self.order.state = PaymentPending(self.order)
        print("Pagamento já recusado. Não retorna para pendente")

    def approve(self):
        print("Pagamento já recusado. Não será aprovado")

    def reject(self):
        print("Pagamento já recusado. Não será recusado novamente")


if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
