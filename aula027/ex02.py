def verificar(f):
    def verifica(x, y):
        print('começando')
        resultado = f(x,y)
        print('ok')
        return resultado
    return verifica
    

@verificar
def soma(x, y):
    return x + y

print(soma(2, 8))