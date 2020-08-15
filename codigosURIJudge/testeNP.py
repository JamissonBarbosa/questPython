from random import randint
import math

matriz = []
linha = []

nc=2
nl = 4
for k in range(nl):
    for j in range(nc):
        randomNum = randint(0, 100)
        linha.append(randomNum)
        matriz.append(linha)
        linha = []
print(matriz)

calc = 0
cont = 0
result = []
for i in matriz:
    for j in matriz:
        for k in range(cont, -1, -1):
            calc += (i[k]-j[k])**2
        raiz = calc**0.5
        result.append(round(raiz, 2))
        calc = 0
    
print(result)