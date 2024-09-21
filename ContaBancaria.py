class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("saldo insuficiente")
    
    def ver_saldo(self):
        return self.__saldo

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros
    
    def aplicar_juros(self):
        self.depositar(self.ver_saldo() * self.taxa_juros)


conta = ContaPoupanca(1000, 0.05)
conta.depositar(200)
print(conta.ver_saldo()) 
conta.sacar(300)
print(conta.ver_saldo())  
conta.aplicar_juros()
print(conta.ver_saldo())  
