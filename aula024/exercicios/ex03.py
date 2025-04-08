import copy

produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},
]

aumento = copy.deepcopy(produtos)

for i in aumento:
    i['preço'] += i['preço']/10


produtos_ordenados_por_nome = copy.deepcopy(produtos)

produtos_ordenados_por_nome.sort(key=lambda x: x['nome'])

produtos_ordenados_por_preco = copy.deepcopy(produtos)

produtos_ordenados_por_preco.sort(key = lambda x: x['preço'])
print(produtos_ordenados_por_preco)
