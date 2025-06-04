def descobreVogal():
    vogais = ['a', 'e', 'i', 'o', 'u']
    while(True):
        cont = 0
        palavra = str(input("Digite uma palavra: "))
        for i in vogais:
            if palavra.__contains__(i):
                print(i)
                cont +=1
        print(cont)

descobreVogal()