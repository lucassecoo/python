from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getNome(self):
        print(f'Nome: {self.nome}')
    
    def getIdade(self):
        print(f'Nome: {self.idade}')



class Conta(ABC):
    def __init__(self, agencia, numConta, saldo):
        self.agencia = agencia
        self.numConta = numConta
        self.saldo = saldo


    def deposito(self, valor):
        self.saldo += valor
        print(f'DEPOSITADO: {valor}, saldo atual: {self.saldo}')

    @abstractmethod
    def saque(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia, numConta, saldo, limite):
        super().__init__(agencia, numConta, saldo)
        self.limite = limite
        
    
    def saque(self, valor):
        if(self.saldo + self.limite >= valor):
            self.saldo -= valor
            print(f'SACADO: {valor}, saldo atual: {self.saldo}')
        else:
            print(f'Saldo insuficiente!')        

class ContaPoupança(Conta):
    def __init__(self, agencia, numConta, saldo):
        super().__init__(agencia, numConta, saldo)
        
    
    def saque(self, valor):
        if(self.saldo >= valor):
            self.saldo -= valor
            print(f'SACADO: {valor}, saldo atual: {self.saldo}')
        else:
            print(f'Saldo insuficiente!')     

class Cliente(Pessoa):
    def __init__(self, nome, idade, numConta):
        super().__init__(nome, idade)
        self.numConta = numConta

class Banco:
    def criarConta(self, cliente, tipo_conta, agencia, numConta, saldo, limite = None):
        if tipo_conta == 'corrente':
            conta = ContaCorrente(agencia, numConta, saldo, limite)
        elif tipo_conta == 'poupança':
            conta = ContaPoupança(agencia, numConta, saldo)
        else:
            print(f'Tipo de conta invalida')
            return

        cliente.numConta = conta
        print(f'Conta {tipo_conta} criada para {cliente.nome}.')
    
    def realizarDeposito(self, cliente, valor):
        cliente.numConta.deposito(valor)
    
    def realizarSaque(self, cliente, valor):
        cliente.numConta.saque(valor)


banco = Banco()
cliente1 = Cliente("Lucas", 30, None)

banco.criarConta(cliente1, 'corrente', 123, 456789, 1000, 500)
banco.realizarDeposito(cliente1, 200)
banco.realizarSaque(cliente1, 1500)