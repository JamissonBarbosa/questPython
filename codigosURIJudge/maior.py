entrda = input()

entradaString = entrda.split(" ")

numeros = [int(num) for num in entradaString]

a, b, c = numeros

maiorAB = (a + b + abs(a - b))/2
maiorABC = (maiorAB + c + abs(maiorAB - c))/2

print("{:.0f} eh o maior".format(maiorABC))