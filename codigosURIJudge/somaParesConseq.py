matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista = []
soma, k = 0, 1
tam = len(matriz)

for i in range(len(matriz)):
    lista.append([])
    for j in range(len(matriz)):
        if k < tam-1:
            print(matriz[i][k], matriz[j][k])
            soma += ((matriz[i][k] - matriz[j][k])**2)
            lista[i].append(soma)
            k += 1
        soma = 0
    k = 1
             
        

print(lista)