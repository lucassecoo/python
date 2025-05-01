from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

p1 = Pessoa('lucas', 20)
