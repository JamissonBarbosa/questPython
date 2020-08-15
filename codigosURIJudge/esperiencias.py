exp = int(input())

tot1, tot2, tot3 = 0, 0, 0

for i in range(exp):
    entrada = input()
    numString = entrada.split(" ")
    numeros = list(numString)
    a, b = numeros

    if b == 'C':
        tot1 += int(a)
    
    if b == 'R':
        tot2 += int(a)
    
    if b == 'S':
        tot3 += int(a)

total = tot1+tot2+tot3
print("Total:",total,"cobaias")
print("Total de coelhos:", tot1)
print("Total de ratos:", tot2)
print("Total de sapos:", tot3)
print("Percentual de coelhos: {:.2f} %".format((tot1/total)*100))
print("Percentual de ratos: {:.2f} %".format((tot2/total)*100))
print("Percentual de sapos: {:.2f} %".format((tot3/total)*100))


