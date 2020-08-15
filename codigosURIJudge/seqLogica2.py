
x, y = list(map(int, input().split()))

cont= 0
num = ''
for i in range(1, y+1):
    num += str(i)+" "
    cont += 1
    if cont == x:
        print(num[:-1])
        cont = 0
        num = ''
    else:
        continue
   
    
    