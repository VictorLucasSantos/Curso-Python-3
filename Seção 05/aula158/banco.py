from typing import List, Optional
import contas
import pessoas


class Banco:
    def __init__(
        self,
        agencias: Optional[List[int]] = None,
        clientes: Optional[List[pessoas.Pessoa]] = None,
        contas: Optional[List[contas.Conta]] = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_cliente(self, cliente):
        return True if cliente in self.clientes else False

    def _checa_conta(self, conta):
        return True if conta in self.contas else False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print("_checa_se_conta_e_do_cliente", True)
            return True
        print("_checa_se_conta_e_do_cliente", False)
        return False

    def _checa_agencia(self, agencia):
        return True if agencia in self.agencias else False

    def autenticar(self, cliente: pessoas.Cliente, conta: contas.Conta):
        return (
            self._checa_agencia(conta)
            and self._checa_cliente(cliente)
            and self._checa_conta(conta)
            and self._checa_se_conta_e_do_cliente(cliente, conta)
        )

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencias!r}, {self.clientes!r}, {self.contas!r})"
        return f"{class_name}{attrs}"


if __name__ == "__main__":
    c1 = pessoas.Cliente("Luiz", 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente("Maria", 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    print(banco.autenticar(c1, cc1))
    print(banco)

    # if banco.autenticar(c1, cc1):
    #     cc1.depositar(10)
    #     c1.conta.depositar(100)
    #     print(c1.conta)
