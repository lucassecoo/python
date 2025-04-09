class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
    
    def extrato(self):
        print(self.saldo)

cliente1 = ContaBancaria('lucas', 15000)
cliente1.depositar(1000)
cliente1.sacar(3000)
cliente1.extrato()