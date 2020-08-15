entrada = int(input())

lista = [3600, 60]


for i in lista:
    result = entrada//i
    print(result,end=":")
    entrada %= i
print(entrada)