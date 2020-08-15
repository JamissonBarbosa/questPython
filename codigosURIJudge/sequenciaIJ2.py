i = 1
j = 7
cont = 0

for k in range(20):
    if cont < 3:
        print("I={} J={}".format(i, j))
        j -= 1
        cont += 1
    else:
        cont = 0
        i += 2
        j += 5

        
    
