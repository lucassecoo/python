import array

letras = array('i', ['a', 'b', 'c', 'd'])

list1 = [10, 20, 40, 80]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

num1 | num2 #uniao
num1 - num2 #diferença
num1 ^ num2 #diferenças simetricas
num1 & num2 #and