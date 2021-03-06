n = int(input())
x = list(map(int, input().split()))

menor = x[0]
for i in range(len(x)):
    if menor > x[i]:
        menor = x[i]
        pos = i

print("Menor valor: ", menor)
print("Posicao: ", pos)