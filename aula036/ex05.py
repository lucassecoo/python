from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade, tipo):
        self.__nome = nome
        self.__idade = idade
        self.__tipo = tipo

    @abstractmethod
    def fazer_som(self):
        pass

    def info(self):
        return f'Nome: {self.__nome}, Idade: {self.__idade}, Tipo: {self.__tipo}'

class Leão(Animal):
    def fazer_som(self):
        return "Roar!"

class Elefante(Animal):
    def fazer_som(self):
        return "Trumpet!"

def emitir_sons(animais):
    for animal in animais:
        print(animal.info())
        print(f'Som: {animal.fazer_som()}')

# Criando instâncias
leão = Leão("Simba", 5, "Felino")
elefante = Elefante("Dumbo", 10, "Pachiderme")

# Lista de animais
animais = [leão, elefante]

# Emitindo sons
emitir_sons(animais)
leão.info()