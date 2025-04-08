class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante
    
    def getCarro(self):
        return self.nome, self.motor, self.fabricante
    
class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

motor1 = Motor('V8')
fabricante1 = Fabricante("Hyunday")
carro1 = Carro('hb20', motor1, fabricante1)
print(carro1.getCarro())
