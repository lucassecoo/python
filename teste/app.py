from flask import Flask, render_template, request, redirect, url_for
from abc import ABC, abstractmethod

app = Flask(__name__)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade

class Conta(ABC):
    def __init__(self, agencia, numConta, saldo):
        self.agencia = agencia
        self.numConta = numConta
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    @abstractmethod
    def saque(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia, numConta, saldo, limite):
        super().__init__(agencia, numConta, saldo)
        self.limite = limite
        
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        return False

class ContaPoupanca(Conta):
    def __init__(self, agencia, numConta, saldo):
        super().__init__(agencia, numConta, saldo)
        
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

class Cliente(Pessoa):
    def __init__(self, nome, idade, numConta):
        super().__init__(nome, idade)
        self.numConta = numConta

class Banco:
    def __init__(self):
        self.clientes = []

    def criarConta(self, cliente, tipo_conta, agencia, numConta, saldo, limite=None):
        if tipo_conta == 'corrente':
            conta = ContaCorrente(agencia, numConta, saldo, limite)
        elif tipo_conta == 'poupança':
            conta = ContaPoupanca(agencia, numConta, saldo)
        else:
            return "Tipo de conta inválido"
        
        cliente.numConta = conta
        self.clientes.append(cliente)
        return f'Conta {tipo_conta} criada para {cliente.nome}.'

banco = Banco()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        tipo_conta = request.form['tipo_conta']
        agencia = request.form['agencia']
        numConta = request.form['numConta']
        saldo = float(request.form['saldo'])
        limite = float(request.form['limite']) if tipo_conta == 'corrente' else None
        
        cliente = Cliente(nome, idade, None)
        mensagem = banco.criarConta(cliente, tipo_conta, agencia, numConta, saldo, limite)
        return render_template('index.html', mensagem=mensagem)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)