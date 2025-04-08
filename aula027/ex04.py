def verifica_tipo(f):
    def verifica(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError('precisa ser inteiro')
        for kwarg in kwargs:
            if not isinstance(kwarg, int):
                raise ValueError('precisa ser inteiro')
        resultado = f(*args, **kwargs)
        return resultado
    return verifica

@verifica_tipo
def soma(x,y):
    return x + y

print(soma(10, 5.6))