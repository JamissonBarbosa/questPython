
entrada = input().split(" ")
valores = list(map(int , entrada))

a = valores[0]
n = valores[-1]

if n <= 0:
    n = int(input())
else:
    soma = 0
    for i in range(0, n):
        soma +=a + i

print(soma) 