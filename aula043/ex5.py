def tabuada():
    num = int(input("digite um num: "))
    for i in range(1, num + 1, 1):
        print(num * i)

def inteiros():
    num1 = int(input("digite um num: "))
    cont = 1
    while(cont<=num1):
        if(cont%2 == 0):
            print(num1, "+", cont, "=", cont + num1)
        cont+=1

