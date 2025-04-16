from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazersom(): ...

class Cachorro(Animal):
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def fazersom(self):
        print('cachorro esta latindo')

class Gato(Animal):
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca   

    def fazersom(self):
        print('gato esta miando')

cachorro = Cachorro('rex', 'pitbull')
cachorro.fazersom()