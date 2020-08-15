entrada = input()

numString = entrada.split(" ")

numeros = [int(numero) for numero in numString]

valores = numeros
valoreOrd = sorted(valores)

for valor in valoreOrd:
    print(valor)

print()

for valor in valores:
    print(valor)
