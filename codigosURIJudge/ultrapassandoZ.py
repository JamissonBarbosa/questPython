x = int(input())

z = int(input())

if z <= x:

    while z <= x:
        z = int(input())
    if z > x:
        k = 0
        soma = 0
        while True:
            soma+= x+k
            k += 1
            if soma > z:
                print(k)
                break
    

else:
    print("0")