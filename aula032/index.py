class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def getCor(self):
        print('ESTOU NO GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor
