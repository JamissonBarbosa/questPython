maior = 0

for i in range(100):
    valor = int(input())
    if valor > maior:
        maior = valor
        pos = i

print(maior)
print(pos)