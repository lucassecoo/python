import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def dicionario(self):
        return {'nome': self.nome, 'idade': self.idade}

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @property
    def idade(self):
        return self.idade

pessoa1 = Pessoa('lucas', 20)
db = pessoa1

with open('aula031/json.json', 'w') as arquivo:
    json.dump(db, arquivo, ensure_ascii=False, indent=2)