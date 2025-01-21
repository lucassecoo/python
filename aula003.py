frutas = ['banana', 'melao', 'kiwi', 'pina']

frutas2= [iten for iten in frutas if 'a' in iten]
print(frutas2)

#IGUAL A

frutas3 = []

for itens in frutas:
    if 'a' in itens:
        frutas3.append(itens)

print(frutas3)

valores = [x for x in range(5)]
print(valores)

#PARA USAR MENOS MEMORIA DO PC USAR GENERATOR EXPRESSIONS
#SO TROCA PARA () AO INVES DE []
valores = (x for x in range(5))
print(valores)
