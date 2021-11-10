a1 = 1
a2 = 1

n = int(input('Digite o termo que quer encontrar em fibonacci: '))

print (a1)
print (a2)
cont = 3
while cont <= n:
    t = a1 + a2
    a2 = a1
    a1 = t
    cont += 1
    print (t)
    