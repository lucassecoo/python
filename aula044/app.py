def Main():
    escolha = 0
    while(True):
        ler_e_imprimir_txt('aula044/menus/menuPrincipal.txt')
        match escolha:
            case 1:
                ...
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
        




def ler_e_imprimir_txt(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(f"{conteudo}/n")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo '{caminho_arquivo}': {e}")

Main()