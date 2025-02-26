palavra = 'lucas'
palavra_user = ''

while palavra_user != palavra:
    letra = input('letra: ').lower()
    if(next(palavra) == letra):
        palavra_user += f'{letra}'
        print(palavra_user)
        break
    else:
        print('*')
