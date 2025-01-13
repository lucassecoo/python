def soma(*num):
    total = 0
    for numeros in num:
        total += numeros
    return total

print(soma(1,2,3,4))

def carro(**modelo):
    return modelo

carro(marca = 'gol', cor = 'branco', ano = '2014')