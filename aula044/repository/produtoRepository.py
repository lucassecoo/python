def repositorio(): 
    listaProdutos = []
    try:
        with open('aula044/menus/produtos.txt', 'r', encoding='utf-8') as f:
            produtos = f.read()
            listaProdutos.append(produtos)
            print(listaProdutos)
    except FileNotFoundError:
        print(f"Erro: O arquivo produtos.txt não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo produtos.txt: {e}")