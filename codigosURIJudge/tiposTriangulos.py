entrada = input()

numString = entrada.split(" ")

numeros = list(map(float, numString))

numeros.sort(reverse=True)

a, b, c = numeros

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == ((b**2) + (c**2)):
        print("TRIANGULO RETANGULO")

    if (a**2) > ((b**2) + (c**2)):
        print("TRIANGULO OBTUSANGULO")

    if (a**2) < ((b**2) + (c**2)):
        print("TRIANGULO ACUTANGULO")

    if a == b and a == c and b == c:
        print("TRIANGULO EQUILATERO")

    if (a == b and a != c and b != c) or (a != b and a == c and b != c) or (a != b and a != c and b == c):
        print("TRIANGULO ISOSCELES")