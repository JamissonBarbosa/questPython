n = int(input())

for i in range(n):
    entrada = input()
    numString = entrada.split(" ")
    numeros = list(map(float, numString))
    a, b, c = numeros
    media = (a*2+b*3+c*5)/(2+3+5)
    print("{:.1f}".format(media))