try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except:
    print('erro')

try:
    valor = int(input('digite: '))
    print(valor)
except ValueError:
    print('valor nao e inteiro')
else:
    print('valor correto') #SO VEM NO ELSE SE DA CERTO O TRY
finally:
    print('codigo terminou')