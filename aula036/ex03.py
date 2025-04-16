import math

class Forma:
    def area():
        raise NotImplementedError("esse metodo deve ser implementado")

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * (self.raio**2)
    
class Retangulo(Forma):
    def __init__(self, comp, larg):
        self.comp = comp
        self.larg = larg
    
    def area(self):
        return self.comp * self.larg
        