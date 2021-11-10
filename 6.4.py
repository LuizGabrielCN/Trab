print ("1- Soma\n2- Subtracao\n3- Divisao\n4- Multiplicacao\n")

op = int(input('OP: '))

a = int(input ('Digite o primeiro valor: '))
b = int (input ('Digite o segundo valor: '))

if op == 1:
    r = a + b
    print ("Soma = ", r)
elif op == 2:
    r = a - b
    print ("Sub = ", r)
elif op == 3:
    r = a / b
    print ("Divisao = ", r)
else:
    r = a * b
    print ("Mult = ", r)