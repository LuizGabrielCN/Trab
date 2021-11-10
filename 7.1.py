from typing import Collection
import numpy

lista = ['luiz', 'joao', 'gabriel', 'pedro', 'pedro', 'luiz']
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

