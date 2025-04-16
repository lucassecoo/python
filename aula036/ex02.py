from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod
    def info(self): ...
        
    
class Carro(Veiculo):
    def info(self):
        print(f'CARRO - marca: {self.marca} e modelo: {self.modelo}')

class Moto(Veiculo):
    def info(self):
        print(f'MOTO - marca: {self.marca} e modelo: {self.modelo}')

moto = Moto('bmw', 'bis')
carro = Carro('audi', 'A8')
moto.info()
carro.info()