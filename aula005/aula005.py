from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc

    def nome_completo(self):
        print(self.nome)
        ano_atual = datetime.now().year
        print(ano_atual - int(self.ano_nasc))


user1 = Funcionarios('lucas', 'seco', 2004)
user1.nome_completo()