class ContaBancaria:
    def __init__(self, numConta, saldo):
        self.__numConta = numConta
        self.__saldo = saldo
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def depositar(self, valor):
        self.__saldo += valor

    def getSaldo(self):
        print(self.__saldo)
    
conta = ContaBancaria(123, 1000)
conta.sacar(500)
conta.depositar(100)
conta.getSaldo()