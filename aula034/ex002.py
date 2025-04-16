class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel
        disponivel = True    

    def __str__(self):
        return(f'{self.titulo}, {self.autor}, {self.ano_publicacao}, {self.disponivel}')
    
    def emprestar(self):
        self.disponivel = False
    
    def devolver(self):
        self.disponivel = True

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []
    
    def __str__(self):
        return(f'{self.livros_emprestados}')
    
    def pegar_emprestado(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)  # Adiciona o objeto Livro
            print(f'{self.nome} pegou emprestado "{livro.titulo}".')
        else:
            print(f'"{livro.titulo}" não está disponível.')
    
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()
            print(f'{self.nome} devolveu "{livro.titulo}".')
        else:
            print(f'{self.nome} não tem "{livro.titulo}" emprestado.')

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def listar_livros(self):
        for livro in self.livros:
            print(livro)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)
    
biblia = Livro('biblia', 'jesus', 1000)
livro2 = Livro('livro2', 'autorABC', 2020)
livro3 = Livro('livro3', 'autorKJH', 2015)

lucas = Usuario('lucas')

biblioteca = Biblioteca()
biblioteca.adicionar_livro(biblia)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_usuario(lucas)
biblioteca.listar_livros()
biblioteca.listar_usuarios()

lucas.pegar_emprestado(biblia)
