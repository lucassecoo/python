from models.Produto import Produto
from repository.produtoRepository import ProdutoRepository

def Main():
    repositorio = ProdutoRepository()
    while(True):
        ler_e_imprimir_txt('aula044/menus/menuPrincipal.txt')
        
        try:
            escolha = int(input("Digite sua opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue
    
        match escolha:
            case 1:
                novo_produto = Produto.criar_novo_produto_do_usuario()
                if novo_produto:
                    repositorio.adicionar_produto(novo_produto) 
            case 2:
                repositorio.listar()
            case 3:
                repositorio.atualizar_produto()
            case 4:
                ...



def ler_e_imprimir_txt(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(f"{conteudo}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo '{caminho_arquivo}': {e}")

if __name__ == "__main__":
    Main()