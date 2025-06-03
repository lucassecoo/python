def teste():
    try:
        num = int(input("Digite um num: "))
    except ValueError:
        print("apenas num inteiro")
    
    for i in range(num, -1, -1):
        print(i)
        print("fogo") if i == 0 else None
            
teste()