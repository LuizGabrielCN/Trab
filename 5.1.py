x = (int (input ('Digite o valor: ')))

cem = x//100
x = x - (cem*100)
cinquenta = x//50
x = x - (cinquenta*50)
dez = x//10
x = x - (dez*10)
um = x

print ("Notas de cem: ", cem)
print ("Notas de cinquenta: ", cinquenta)
print ("Notas de dez: ", dez)
print ("Notas de um: ", um)