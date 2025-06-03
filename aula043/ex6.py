def listaDeCompras():
    listacompras = []
    while(True):
        exibirMenu()
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                compra = input("digite oq deseja comprar: ")
                listacompras.append(compra)
            case 2: 
                exclui = str(input("digite oq deseja excluir: "))
                try:
                    listacompras.remove(exclui)
                except Exception as e:
                    print(f"Erro:  {e}")
            case 3:
                for p in listacompras:
                    print(p)

def exibirMenu():
    print("------menu-------")
    print("1. Comprar")
    print("2. Remover")
    print("3. Exibir")
    print("-----------------")

listaDeCompras()