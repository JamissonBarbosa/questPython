x = int(input())
y = int(input())


if x > y:
    soma = 0
    for i in range(x-1, y, -1):
        if i % 2 == 1:
            soma += i
            print(i)
    print(soma)

else:
    soma = 0
    for i in range(x, y):
        if i % 2 == 1:
            soma += i
            print(i)
    print(soma)