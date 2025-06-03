def conversor():
    def converte(x):
        converteF = (x * 9 / 5) + 32
        return converteF
    while(True):
        temp = float(input("Digite a temp: "))
        convertido = converte(temp)
        print(convertido)

conversor()
    