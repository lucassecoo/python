compras = []

while True:
    print('Selecione uma opção')
    acao = input('[i]nserir [a]pagar [l]istar: ').lower()
    
    match acao:
        case 'i': 
            novo_valor = input('item: ').lower()
            compras.insert(-1, novo_valor)
            continue
        case 'a':
            apaga = input('Apagar item:').lower()
            compras.remove(apaga)
            continue
        case 'l':
            if len(compras) > 0:
                for itens in enumerate(compras):
                    indice, nome = itens
                    print(indice, nome)
            else:
                print('sem itens')
            continue