def calculaMedia():
    notas = []
    nota = 0
    while(nota != -1):
        nota = float(input("Digite uma nota(-1 para parar): "))
        if nota == -1:
            break
        else:
            notas.append(nota)
    media = sum(notas)/len(notas)
    return media

print(calculaMedia())
