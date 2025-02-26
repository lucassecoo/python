def f1(*args):
    total = 1
    for num in args:
        total *= num
    return total

som1 = f1(1,2,3,4,5,5)
print(som1)