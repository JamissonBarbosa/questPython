from math import sqrt

entrda = input()

entradaString = entrda.split(" ")

numeros = [float(num) for num in entradaString]

a, b = numeros

entrda = input()

entradaString = entrda.split(" ")

numeros = [float(num) for num in entradaString]

c, d = numeros

distEuclidian = sqrt((c-a)**2 + (d-b)**2)

print("{:.4f}".format(distEuclidian))

