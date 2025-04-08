idades = []

while True:
    entrada = input('idade (digite "pare" para parar):')

    if entrada.lower() == 'pare':
        break

    try:
        idade = int(entrada)
        idades.append(idade)
    except:
        print('coloque um valor valido')


idades_em_meses = [
    x * 12
    for x in idades
    if x >= 18
]

print(idades_em_meses)