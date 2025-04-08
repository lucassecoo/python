lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
lista_soma = []

def soma_lista(list1, list2):
    menor_lista = min(list1, list2)
    for i, menor in enumerate(menor_lista):
        lista_soma.append(menor+ list2[i])
    return lista_soma

print(soma_lista(lista_a, lista_b))