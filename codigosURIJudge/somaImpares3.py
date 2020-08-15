n = int(input())

soma = 0


for i in range(n):
    entrada = input().split(" ")
    x, y = map(int, entrada)
    for j in range(x, x+(2*y)):
        if j % 2 == 1:
            soma += j   
    print(soma)
    soma = 0
       