n = int(input())
soma = 0



for i in range(n):
    entrada = input().split()
    numeros = list(map(int, entrada))
    x, y = numeros

    if x < y:
        if x != y-1 or x != y:
            for j in range(x+1, y):
                if j % 2 == 1:
                    soma += j
                    print(soma)
            else:
                print("0")
        soma = 0

    if x > y:
        if x != y+1 or x != y:
            for j in range(x-1, y, -1):
                if j % 2 == 1:
                    soma += j
                    print(soma)
            else:
                print("0")
        soma = 0
                
    