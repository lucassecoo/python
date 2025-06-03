def calculadora():
    num1 = int(input("digite um numero: "))
    num2 = int(input("digite outro: "))

    if num2 != 0:
        while(True): 
            operador = input("digite um operador: ")
            if(operador == "+" or operador == "-" or operador == "/" or operador == "*"):
                break
            else:
                print("Operador invalido!")
        
        match operador:
            case "+": 
                return num1 + num2
            case "*": 
                return num1 * num2 
            case "-": 
                return num1 - num2 
            case "/": 
                return num1 / num2
    else:
        print("não é possivel dividir por 0")

while True:
    print(calculadora())    