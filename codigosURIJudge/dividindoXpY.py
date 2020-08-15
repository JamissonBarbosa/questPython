n = int(input())

for i in range(n):
    entrada = input().split(" ")
    numeros = map(int, entrada)
    x, y = numeros

    if y == 0:
        print("divisao impossivel")

    else:
        result = x / y
        print(result)