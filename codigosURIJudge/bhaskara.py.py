from math import sqrt

entrada = input()

numString = entrada.split(" ")

numeros = [float(numero) for numero in numString]

a, b, c = numeros

delta = (b**2) - (4*a*c)

if a != 0 and delta >=0:
    r1 = ((-b) + sqrt(delta))/(2*a)
    r2 = ((-b) - sqrt(delta))/(2*a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
else:
    print("Impossivel calcular")

