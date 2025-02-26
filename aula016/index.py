lista = ['lucas', 'maria', 'jose']
cont = 0
for nome in lista:
    print(f'{cont} - {nome}')
    cont += 1


nome, *resto = ['lucas', 'maria', 'jose']