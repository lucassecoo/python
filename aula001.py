valor = [1000, 2000, 3000]

def aplica_imp(valor):
    return valor * 1.1

preco_imposto = list(map(aplica_imp, valor))

print(preco_imposto)