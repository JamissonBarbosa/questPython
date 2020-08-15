i = 0.2
j = 1
d = 2
cont = 0

print("I=0 J=1")
print("I=0 J=2")
print("I=0 J=3")

for k in range(20):
    if cont < 1:
        print("I={:.1f} J={}.{}".format(i, j, d))
        print("I={:.1f} J={}.{}".format(i, j, d))
        print("I={:.1f} J={}.{}".format(i, j, d))
        j += 1
        cont += 1
    else:
        cont = 0
        i += 0.2
        j = 1
        d += 2
        if d == 9:
            d = 0

        
    
