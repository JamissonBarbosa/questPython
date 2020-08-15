entrada = input()

numString = entrada.split(" ")


numeros = list(map(float, numString))

a, b, c = numeros

if abs(a - b) < c < (a+b) and abs(a - c) < b < (a+c) and abs(b - c) < a < (b + c):
    perimetro = a + b + c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((a + b)/2)*c
    print("Area = {:.1f}".format(area))