try:
    a = 19
    b = 0
    c = a / b
except (ZeroDivisionError) as error:
    print('erro:', error)