entrada = input()

numString = entrada.split(" ")

numeros = list(map(int, numString))

a, b = numeros

if a < b:
    result = b % a
    if result == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    result = a % b
    if result == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

