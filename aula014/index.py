import re
pattern = r'^-?\d+(\.\d+)?$'

while True:
    num1 = input('digite um num: ')
    num2 = input('digite outro num: ')
    operador = input('operador: ')

    if re.match(pattern, num1) and re.match(pattern, num2):
        num1 = float(num1)
        num2 = float(num2)

        match operador:
            case '+':
                print(num1 + num2)
            case '-':
                print(num1 - num2)
            case '/':
                print(num1 / num2)
            case '*':
                print(num1 * num2)
    else:
        print('nao é num')

    sair = input('sair? [s] or [n]: ').lower()
    if(sair == 's'):
        break