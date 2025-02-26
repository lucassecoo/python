num = input("Digite um num:")
num_int = num.isdigit()

if(num_int):
    num = int(num)
    if(num % 2 == 0):
        print('par')
    else:
        print('impar')
else:
    print('não é int')

