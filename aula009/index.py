alunos = {'nome': 'lucas', 'idade': 14}

alunos['nome'] = 'jose'

alunos.update({'endereco': 'rua xxxx'})
del alunos ['idade']

for x in alunos.items():
    print(x)