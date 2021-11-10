n = int(input('Digite o numero a ser fatorado: '))

cont = 1
r = 1

while cont <= n:
    r *= cont
    cont += 1

print ("Resultado: ", r)