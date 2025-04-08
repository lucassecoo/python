dados_pessoa = {
    'idade': 19,
    'altura': 1.6,
}

pessoa = {
    'nome': 'lucas',
    'sobrenome': 'alves',
}

pessoa_completo = {**pessoa, **dados_pessoa}

print(pessoa_completo)

