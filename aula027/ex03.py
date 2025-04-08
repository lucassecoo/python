def contador_chamadas(func):
    # Inicializa um contador de chamadas
    def wrapper(*args, **kwargs):
        wrapper.chamadas += 1  # Incrementa o contador
        print(f"A função '{func.__name__}' foi chamada {wrapper.chamadas} vezes.")
        return func(*args, **kwargs)  # Chama a função original
    wrapper.chamadas = 0  # Inicializa o contador de chamadas
    return wrapper  # Retorna a função wrapper

# Aplicando o decorador à função saudacao
@contador_chamadas
def saudacao(nome):
    print(f"Olá, {nome}!")

# Chamando a função decorada várias vezes
saudacao("Maria")
saudacao("João")
saudacao("Ana")