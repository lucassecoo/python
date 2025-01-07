compra = float(input('digite o valor'))

if compra > 200:
    valor = compra - compra * 0.2
elif compra > 100:
    valor = compra - compra * 0.1
else:
    valor = compra - compra * 0.05

print(f'{valor:.2f}')