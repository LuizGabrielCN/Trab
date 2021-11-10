from typing import Collection
import numpy

num = int(input('Digite a quantidade de nomes: '))
cont = 0
lista = []

while (cont < num):
    name = str(input('Digite o nome: '))
    if (name != ''):
        lista.append(name)
        cont+=1
    else:
        break


dicionario = dict()

lista.sort()

dicionario ["nome"] = lista[0]
dicionario ["quant"] = 1

result = []

result.append (dicionario.copy())

x = 0
tam = numpy.size(lista)

for i in range (1, tam):
    if (result[x]['nome'] == lista[i]):
        result[x]['quant'] += 1
    else:
        dicionario['nome'] = lista[i]
        dicionario['quant'] = 1
        result.append(dicionario.copy())
        x+=1

for i in result:
    print()
    for x in i.values():
        print (x, end = '  ')

