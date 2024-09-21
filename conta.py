class Conta:
    def __init__(self, saldo, limite):
        self._saldo = saldo
        self._limite = limite

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo + self._limite >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente")


class ContaEspecial(Conta):
    def sacar(self, valor):
        if self._saldo + (self._limite * 2) >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente")


conta = ContaEspecial(500, 1000)
conta.sacar(1500)
