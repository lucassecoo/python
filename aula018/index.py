cpf_user = input('digite os 9 primeiros digitos do cpf: ')
array_cpf = (list(cpf_user))
array_int =[]
soma = 0
mult = 10 

for num in array_cpf:
    array_int.append(int(num))

for num in array_int:
    num *= mult
    soma += num
    mult -= 1

soma *= 10
soma %= 11

primeiro_dig = soma if soma <= 9 else 0

####SEGUNDO DIGITO

soma2 = 0
array_int.append(int(primeiro_dig))
mult = 11

for i in array_int:
    i *= mult
    soma2 += i
    mult -= 1

soma2 *= 10
soma2 %= 11
segundo_dig = soma2 if soma2 <= 9 else 0

array_int.append(int(segundo_dig))
print(array_int)