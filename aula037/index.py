import enum

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()

print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção nao encontrada')
    
    print(f'Movendo para a {direcao.name}')

mover(Direcoes.ESQUERDA)