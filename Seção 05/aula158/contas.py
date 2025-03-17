import abc


class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor) -> float: ...

    def depositar(self, valor) -> float:
        self.saldo += valor
        self.detalhes(f"(DEPOSITO {valor:.2f})")

    def detalhes(self, msg="") -> None:
        print("--")
        print(f"O seu saldo é {self.saldo:.2f} {msg}")


class ContaPoupanca(Conta):
    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor:.2f})")
            return self.saldo

        print("Não foi possível sacar o valor desejado")
        self.detalhes(f"(SAQUE NEGADO {valor:.2f})")
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor:.2f})")
            return self.saldo

        print("Não foi possível sacar o valor desejado")
        print(f"Seu limite é {-self.limite:.2f}")
        self.detalhes(f"(SAQUE NEGADO {valor:.2f})")
        return self.saldo


if __name__ == "__main__":
    print("-" * 15, "CONTA POUPANCA", "-" * 15)
    cp = ContaPoupanca(111, 222, 0)
    cp.sacar(1)
    cp.depositar(1)
    cp.sacar(1)
    print("-" * 15, "CONTA CORRENTE", "-" * 15)
    cc = ContaCorrente(111, 222, 0, 100)
    cc.sacar(1)
    cc.depositar(1)
    cc.sacar(1)
    cc.sacar(1)
    cc.sacar(98)
    cc.sacar(1)
