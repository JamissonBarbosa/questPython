par, impar, pos, pos1, neg, neg1 = 0, 0, 0, 0, 0, 0

for i in range(5):
    num = int(input())
    if num %2 == 0:
        par += 1
        if num > 0:
            pos += 1
        if num < 0:
            neg += 1
        
    if num %2 == 1:
        impar += 1
        if num > 0:
            pos1 += 1
        if num < 0:
            neg1 += 1
    
print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(pos+pos1,"valor(es0 positivo(es)")
print(neg+neg1,"valor(es0 negativo(es)")
