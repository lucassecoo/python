lista1 = [1,2,3,4]

multi = lambda x: x * 2

lista2 = map(multi, lista1)

print(list(lista2))

valores = [10,20,30,90,80]

reduz20 = lambda x: x > 20

print(list(filter(reduz20, valores)))