from models.Produto import Produto 

class ProdutoRepository:
    def __init__(self, caminho_arquivo='aula044/menus/produtos.txt'):
        self.caminho_arquivo = caminho_arquivo
        self.lista_produtos = [] 
        self._carregar_produtos_do_arquivo() 

    def _carregar_produtos_do_arquivo(self):
        self.lista_produtos = []
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
                for linha in f:
                    partes = linha.strip().split(',')
                    if len(partes) == 3:
                        try:
                            nome = partes[0]
                            preco = float(partes[1])
                            quantidade = int(partes[2])
                            self.lista_produtos.append(Produto(nome, preco, quantidade))
                        except ValueError as e:
                            print(f"Erro ao parsear linha no arquivo '{self.caminho_arquivo}': {linha.strip()} - {e}")
            print(f"Produtos carregados com sucesso do '{self.caminho_arquivo}'!")
        except FileNotFoundError:
            print(f"Aviso: O arquivo '{self.caminho_arquivo}' não foi encontrado. Uma nova lista será iniciada.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar o arquivo '{self.caminho_arquivo}': {e}")
    
    def listar(self):
        if not self.lista_produtos:
            print("Nenhum produto cadastrado ainda.")
            return

        print("\n--- Lista de Produtos ---")
        for i, produto_obj in enumerate(self.lista_produtos):
            print(f"{i+1}. Nome: {produto_obj.nome}, Preço: R${produto_obj.preco:.2f}, Quantidade: {produto_obj.quantidade}")
        print("-------------------------\n")

    def adicionar_produto(self, produto: 'Produto'):        
        self.lista_produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao repositório.")
        self._salvar_produtos_no_arquivo()

    def _salvar_produtos_no_arquivo(self):
        try:
            with open(self.caminho_arquivo, 'w', encoding='utf-8') as f:
                for produto_obj in self.lista_produtos:
                    # O método __str__ do Produto já formata corretamente
                    f.write(f"{produto_obj}\n") 
            print(f"Produtos salvos no arquivo '{self.caminho_arquivo}' com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar produtos no arquivo '{self.caminho_arquivo}': {e}")
        

    def buscar_por_nome(self, nome):
        for produto in self.lista_produtos:
            if produto.nome.lower() == nome.lower(): # Busca case-insensitive
                return produto
        return None


    def atualizar_produto(self):
            print("\n--- Atualizar Produto ---")

            nome_para_atualizar = Produto._obter_entrada_nao_vazia("Digite o NOME do produto que deseja atualizar: ")
            produto_existente = self.buscar_por_nome(nome_para_atualizar)
            if produto_existente:
                print(f"Produto encontrado: Nome: {produto_existente.nome}, Preço: R${produto_existente.preco:.2f}, Quantidade: {produto_existente.quantidade}")
                print("Digite as novas informações (deixe em branco para manter o valor atual):")
                    
                novo_nome = input(f"Novo nome (atual: {produto_existente.nome}): ").strip()
                if not novo_nome:
                    novo_nome = produto_existente.nome # Mantém o nome antigo se o usuário deixar em branco
                    
                novo_preco_str = input(f"Novo preço (atual: {produto_existente.preco:.2f}): ").strip()
                novo_preco = produto_existente.preco # Valor padrão é o antigo
                if novo_preco_str:
                    try:
                        novo_preco = float(novo_preco_str)
                        if novo_preco < 0:
                            print("Preço não pode ser negativo. Mantendo o preço antigo.")
                            novo_preco = produto_existente.preco
                    except ValueError:
                            print("Entrada inválida para preço. Mantendo o preço antigo.")
                            novo_preco = produto_existente.preco

                nova_quantidade_str = input(f"Nova quantidade (atual: {produto_existente.quantidade}): ").strip()
                nova_quantidade = produto_existente.quantidade # Valor padrão é a antiga
                if nova_quantidade_str:
                    try:
                        nova_quantidade = int(nova_quantidade_str)
                        if nova_quantidade < 0:
                            print("Quantidade não pode ser negativa. Mantendo a quantidade antiga.")
                            nova_quantidade = produto_existente.quantidade
                    except ValueError:
                            print("Entrada inválida para quantidade. Mantendo a quantidade antiga.")
                            nova_quantidade = produto_existente.quantidade
                try:
                    # Atualiza as propriedades do objeto Produto encontrado
                    produto_existente.setNome(novo_nome)
                    produto_existente.setPreco(novo_preco)
                    produto_existente.setQuantidade(nova_quantidade)
                    
                    self._salvar_produtos_no_arquivo() # Salva a lista atualizada no arquivo
                    print(f"Produto '{nome_para_atualizar}' atualizado para '{novo_nome}' com sucesso!")
                    return True
                except ValueError as ve:
                    print(f"Erro de validação ao atualizar produto: {ve}")
                    return False
                except Exception as e:
                    print(f"Erro inesperado ao atualizar produto: {e}")
                    return False
            else:
                print(f"Produto '{nome_para_atualizar}' não encontrado para atualização.")
                return False