def verificar(f):

    #sempre criar função interna
    def verifica(x, y):
        print('verificando')
        if x < 0 or y < 0:
            raise ValueError('Precisa ser positivo')
        
        #armazena o valor da função em uma var
        resultado = f(x, y)

        print('verificado')
        return resultado
    
    return verifica

#chama verificador
@verificar
def soma(x, y):
    return x + y

print(soma(5, 7))