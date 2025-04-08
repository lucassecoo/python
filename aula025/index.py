lista = ['meu', 'nome', 'é', 'lucas']
iterator = iter(lista)

print(next(iterator))

#generator = (n for n in range(1000))
#

def generator(n = 0):
    yield 1