while True:
    entrada = input().split(" ")
    numeros = list(map(int, entrada))
    n, m = numeros
    soma = 0

    if n <= 0 or m <= 0:
        break
    else:
        if n > m:
            n += 1
            for i in range(m, n):
                print(i, end=" ")
                soma += i
            print("Sum={}".format(soma))
            
        if n < m:
            m +=1
            for i in range(n, m):
                print(i, end=" ")
                soma += i
            print("Sum={}".format(soma))