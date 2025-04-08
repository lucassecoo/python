def conta_repetida(f):
    def conta(*args, **kwargs):
        #verifica se o contador já foi inicialiazado
        if not hasattr(conta, 'contador'):
            conta.contador = 0

        if conta.contador <=  3:
            raise ValueError('atingiu o maximo de 3')
        conta.contador += 1
        resultado = f(*args, **kwargs)
        return resultado
    
    return conta

@conta_repetida
def teste():
    print('oi')

teste()
teste()


