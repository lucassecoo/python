
class Produto:
    def __init__(self, nome, preco, quantidade):
        # Validações no construtor
        if not isinstance(nome, str) or not nome:
            raise ValueError("Nome do produto não pode ser vazio.")
        if not isinstance(preco, (int, float)) or preco < 0:
            raise ValueError("Preço deve ser um número não negativo.")
        if not isinstance(quantidade, int) or quantidade < 0:
            raise ValueError("Quantidade deve ser um número inteiro não negativo.")

        self.nome = nome
        self.preco = float(preco)
        self.quantidade = int(quantidade)
    
    # Getters e Setters
    def getNome(self): return self.nome
    def getPreco(self): return self.preco
    def getQuantidade(self): return self.quantidade
    
    def setNome(self, nome):
        if not isinstance(nome, str) or not nome:
            raise ValueError("Nome não pode ser vazio.")
        self.nome = nome
    
    def setPreco(self, preco):
        if not isinstance(preco, (int, float)) or preco < 0:
            raise ValueError("Preço deve ser um número não negativo.")
        self.preco = float(preco)

    def setQuantidade(self, quantidade):
        if not isinstance(quantidade, int) or quantidade < 0:
            raise ValueError("Quantidade deve ser um número inteiro não negativo.")
        self.quantidade = int(quantidade)


    # Método __str__ para facilitar a representação do objeto como string (usado para salvar no arquivo)
    def __str__(self):
        return f"{self.nome},{self.preco:.2f},{self.quantidade}"

    # Método __repr__ para representação em listas/debug (útil para depuração)
    def __repr__(self):
        return self.__str__()
    

    #  Métodos auxiliares para entrada 
    @staticmethod
    def _obter_entrada_nao_vazia(mensagem):
        while True:
            entrada = input(mensagem).strip()
            if entrada: return entrada
            else: print("Valor não pode ser vazio!")

    @staticmethod
    def _obter_numero_valido(mensagem, tipo=float):
        while True:
            entrada_str = Produto._obter_entrada_nao_vazia(mensagem)
            try:
                numero = tipo(entrada_str)
                if numero < 0: print("Valor não pode ser negativo!")
                else: return numero
            except ValueError: print(f"Entrada inválida. Por favor, digite um número.")


    ### FUNÇÃO PARA CRIAR UM NOVO PRODUTO
    @classmethod
    def criar_novo_produto_do_usuario(cls):
        print("\n--- Criando um novo Produto ---")
        try:
            nome = cls._obter_entrada_nao_vazia("Digite o nome do produto: ")
            preco = cls._obter_numero_valido("Digite o preço do produto: ", tipo=float)
            quantidade = cls._obter_numero_valido("Digite a quantidade do produto: ", tipo=int)

            # Cria e retorna uma nova instância de Produto
            novo_produto = cls(nome, preco, quantidade)
            print(f"Produto '{nome}' criado com sucesso!")
            return novo_produto
        except ValueError as ve:
            print(f'Erro de validação ao criar produto: {ve}')
            return None # Retorna None em caso de erro de validação
        except Exception as e:
            print(f'Ocorreu um erro inesperado ao criar o produto: {e}')
            return None # Retorna None para outros erros inesperados
        
